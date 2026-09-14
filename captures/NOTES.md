# SysEx findings — Cyclone TT-78 (RezOSDrum)

Captured with `amidi -p hw:2,0,0 -r`, TT-78 MIDI OUT into MidiSport MIDI IN 1,
machine's MIDI OUT channel 1.

## Confirmed working

The MIDI OUT leg is good: 843 Note On events captured while a pattern played,
on notes 36, 42, 63, 64, 75 — Bass Drum, Hi-hat, High Conga, Low Conga, Clave.
That matches the note map in the RezOSDrum implementation chart exactly.
Transport bytes came through too (0xFA start, 0xFC stop).

## The [FUNC]+[COPY] message is an event frame, not pattern data

Four presses of `[FUNC]+[COPY]` in Pattern Play mode produced eight SysEx
messages, every one exactly 31 bytes, identical apart from a single byte:

```
f0 00 01 7a 09 12 SS SS SS SS SS SS 00 XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 f7
                                    ^^ byte 13: 01, 00, 01, 00, 01, 00, 01, 00
```

| offset | bytes | reading |
|---|---|---|
| 0 | `f0` | SysEx start |
| 1–3 | `00 01 7a` | three-byte manufacturer id |
| 4–10 | `09 12` then `SS SS SS SS SS SS` | product, command, then the packed unit serial |
| 11–12 | `00 00` | always zero here |
| 13 | `01` / `00` | the only byte that moves — press / release |
| 14–29 | zero | unused in this frame |
| 30 | `f7` | SysEx end |

Byte 13 alternating 1/0 across exactly twice the number of button presses makes
this a **press/release event frame**. A fixed 31-byte frame whose only variable
is one flag cannot encode a 64-step pattern — that needs 140+ bytes just for the
step bitmaps of 14 voices, before modifiers.

## Conclusion: pattern cloning is a handshake

The manual requires cables in **both** directions for cloning between two units.
Combined with the above, the protocol is almost certainly: the source announces
the copy, the destination answers, and only then does the payload flow. With no
peer answering, the announcement is all we ever see.

## Next experiment

Put the hub between the two machines and log both directions:

```
TT-78  MIDI OUT -> hub MIDI IN  1        hub MIDI OUT 1 -> TT-606 MIDI IN
TT-606 MIDI OUT -> hub MIDI IN  2        hub MIDI OUT 2 -> TT-78  MIDI IN

aconnect 24:0 24:1        # TT-78  -> TT-606
aconnect 24:1 24:0        # TT-606 -> TT-78
aseqdump -p 24:0 &        # log the TT-78 side
aseqdump -p 24:1 &        # log the TT-606 side
```

Then `[FUNC]+[COPY]` on the TT-78 and `[FUNC]+[PASTE]` on the TT-606 captures
the whole exchange, payload included. Both machines' rear switches must be on
OUT, not THRU.

Cheaper probe, if cables are short: echo the captured 31-byte frame back at the
TT-78 and watch for a reply. It is a frame the machine itself emitted and paste
still needs a button press, but it is unknown-effect SysEx sent to hardware, so
ask first.

## Echo probe — negative, and weak by construction

Sent the captured 31-byte frame back at the TT-78 three ways (press alone,
press+release, press twice), 6-second reply window each. No reply to any.

This result is not very informative. Replaying the *source's* announcement back
at the source is not the handshake: what the source waits for is the
*destination's* reply, and we have never observed one. The probe was cheap, so
it was worth a shot, but its failure rules little out.

## No front-panel dump exists

Manual lesson 21: firmware update, backup and restore are all driven from the
Cyclone Studio app. There is no button combination that makes the machine dump
its memory on its own — it answers a request from the app. So a live capture
from this Linux box cannot provoke a backup.

## Revised plan: work on Cyclone Studio backup *files*, not live MIDI

This removes the need for any live capture, and needs neither the TT-606 nor
this machine in the MIDI loop:

1. Move the MidiSport to the Mac, install Cyclone Studio, connect the TT-78.
2. Click **Backup** and save the file. That file is the whole memory:
   patterns, tracks, clips, kits and user settings.
3. Make one small, known edit on the machine, back up again to a new file.
4. Diff the files with `tools/analyze_sysex.py` — it takes any pair of binaries.

Each diff isolates a bit or two, exactly as in the protocol in tools/README.md,
except the inputs are saved files rather than captures. Once the layout is
known, the endgame is to write a modified backup file and let Studio **Restore**
it, which writes all 64 slots in one shot.

Restore overwrites Patterns, Tracks, Clips, Kits *and* user settings. Keep the
very first backup untouched as the way back.

## Still open

The 31-byte frame is unexplained. A controlled capture would settle it — one
single `[FUNC]+[COPY]` press, long window, nothing else touched; then the same
with only a pattern-select press. Two frames per press means press/release;
frames without any press means it is a periodic ping. Worth doing only for
completeness: understanding this frame does not by itself yield the payload.
