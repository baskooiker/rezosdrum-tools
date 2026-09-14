# Getting the banks into pattern memory

Two jobs live here: playing patterns into the machines over MIDI (works now),
and decoding the SysEx pattern format so the banks can be written into memory.

On this box an M-Audio MidiSport 2x4 is on USB, so ALSA's `amidi` and
`aplaymidi` do everything and no Python MIDI bindings are needed. MIDI Out 1
(the TT-78) is port `hw:2,0,0` for `amidi`, `24:0` for `aplaymidi`. Check with
`amidi -l` after any re-plug, since numbering can move.

The `.py` tools below use `mido` instead, for a machine without ALSA:

```
pip install mido python-rtmidi
```

## play_bank.py — play the banks on the real voices

```
python3 tools/play_bank.py --list
python3 tools/play_bank.py --machine TT-606 --port "USB MIDI" --slot 5
python3 tools/play_bank.py --machine TT-78  --port "USB MIDI" --all --repeats 8
python3 tools/play_bank.py --machine TT-606 --port "USB MIDI" --probe
```

Sends Note On per step (velocity 127 for accents, ≥112 is what the machines
read as accented), a grace note a third of a step early for flams, an extra
strike halfway to the next step for rolls, and the per-pattern Tone / Nuance /
Inst Select CCs up front. Default channel 1, which is the machines' default.

`--probe` plays a plain kick/snare/hat loop, which is how the question below was
settled — leave it in place if you ever want to re-test on the TT-606.

On ALSA, `aplaymidi` plays the generated files directly with no install:

```
aplaymidi -l
aplaymidi -p 24:0 out/midi/TT-78/P01_rock-1.mid
aplaymidi -p 24:0 out/midi/TT-78_bank_all64.mid
```

### Settled: received notes do NOT record into pattern memory

Tested on the TT-78, 2026-09-09 — MIDI IN channel 1, Pattern Write mode,
sequencer running, empty slot selected, ten repeats of the probe loop. Every
repeat sounded; no step was written. Received Note On triggers the voices live
and never reaches the sequencer, so playing a bank in cannot fill the machine.
SysEx is the only route to pattern memory.

## Decoding the SysEx format

The MIDI implementation chart lists SysEx as recognised for "Pattern backup,
Firmware updates". Cyclone Studio (Mac) does Backup and Restore over it. The
format is undocumented, so it has to be diffed out of your own machine.

### Wiring

Capture needs the machine's **MIDI OUT** cabled into the interface's **MIDI IN**,
and the machine's rear **MIDI Out/Thru switch set to OUT**. If the MIDI OUT
channel was ever cleared with `[CLEAR]` in the channel menu, note and CC output
is disabled — re-select channel 1 with `[FUNC]+[MIDI OUT]`.

### Capture

```
tools/capture_alsa.sh --list
tools/capture_alsa.sh hw:2,0,0 captures/empty.syx
```

The script waits, then summarises what arrived and hands it to
`analyze_sysex.py`. `tools/capture_sysex.py` is the same job via `mido`, for a
machine without ALSA.

Two things are worth capturing, and the second needs no extra software at all:

1. **Cyclone Studio → Backup** (Mac/PC). The whole memory: patterns, tracks,
   clips, kits and system settings. Big, but it is what Restore consumes, so
   cracking it means writing all 64 slots in one shot.
2. **A pattern clone — the better first target.** Select a pattern and press
   `[FUNC]+[COPY]`. The machine sends that one pattern as SysEx out of its MIDI
   OUT, which is exactly what the pattern-cloning feature between two units
   relies on. One pattern per message, no Cyclone Studio needed, and the
   receiving side is a plain `[FUNC]+[PASTE]` — so a decoded clone message is a
   per-slot loader you can drive with `tools/send_alsa.sh`.

### Sending it back

```
tools/send_alsa.sh hw:2,0,0 captures/pattern.syx
```

Send a captured clone message, then press `[FUNC]+[PASTE]` with the destination
pattern selected. Round-tripping an unmodified capture is the first test: if
copy-from-slot-1 then paste-into-slot-2 reproduces the pattern, the transport
works and only the payload layout is left to decode.

A Cyclone Studio **Restore overwrites the machine's entire memory** — back up
anything you care about first.

### Diff protocol

Change exactly one thing between captures. Each diff should isolate a bit or
two, which is what pins down the layout:

| capture | edit made first |
|---|---|
| `empty.syx` | `[CLEAR]+[1]`, pattern P1 empty, length 16 |
| `len64.syx` | set P1 length to 64 (`[FUNC]+[LENGTH]`, page 4, `[16]`) |
| `bd1.syx` | add BD on step 1 |
| `bd12.syx` | add BD on step 2 as well |
| `bd1_acc.syx` | accent step 1 |
| `bd1_flam.syx` | flam on step 1 instead |
| `bd1_roll.syx` | roll on step 1 instead |
| `sd1.syx` | clear BD, add SD on step 1 |
| `p2_bd1.syx` | same single BD hit, but in slot P2 |

Then:

```
python3 tools/analyze_sysex.py captures/empty.syx captures/bd1.syx --bits
python3 tools/analyze_sysex.py captures/*.syx --bits
```

What each pair tells you:

* `empty → bd1` — where the step bitmap for the first instrument starts, and
  which bit is step 1.
* `bd1 → bd12` — the bit order within a step byte (SysEx data bytes carry
  7 bits, so a 64-step lane is at least 10 bytes).
* `bd1 → sd1` — the per-instrument stride, and therefore the instrument order.
* `bd1 → bd1_acc` / `_flam` / `_roll` — whether the modifiers are separate
  bit-planes alongside the step bitmap or packed per step.
* `bd1 → p2_bd1` — the per-pattern stride and where slot numbering lives.
* `empty → len64` — where pattern length and time scale are stored.
* Bytes that move in *every* diff are almost certainly a checksum; work out
  its span last, once the payload layout is known.

Once the layout is known, `out/*_patterns.json` has every pattern in exactly
the form an encoder needs: one 64-character lane per voice, plus the `GA`
Global Accent lane, plus `kit` / `shuffle` / `flam_time` for the pattern's
voice settings.
