# rezosdrum-tools

Cyclone Analogic's **TT-78 Beat Bot** and **TT-606 Drum Drone** ship with no
factory patterns and no published pattern format. Cyclone Studio can back a
machine up and restore it, but the file it produces is undocumented, so there
has been no way to author patterns anywhere except on the front panel, one step
at a time.

This repository documents that format and implements it. The frame layout, the
payload encoding, the packet checksum, the per-voice step encoding and the
pattern addressing were recovered by disassembling Cyclone Studio and by
differential analysis of backups taken from a real machine. It is verified end
to end: generated backup files restore onto a TT-78 and play.

It also contains a generator that produces 64 patterns per machine, written for
each machine's actual voice set and using its accents, flams, rolls and Fill
variations.

| | status |
|---|---|
| SysEx frame format, 6-bit payload encoding, checksum | confirmed |
| TT-78 pattern format, voice bit map, Fills | confirmed on hardware |
| TT-606 pattern format | frame format shared; voice bit map not yet mapped |
| Pattern generator, step charts, MIDI export | both machines |

## The format

Start with **[docs/PROTOCOL.md](docs/PROTOCOL.md)** for the SysEx frame, the
backup file structure and the checksum, and
**[docs/instrument_bitmap.md](docs/instrument_bitmap.md)** for the TT-78 voice
bit map. Every claim in both is marked as confirmed or inferred.

The short version:

```
F0 00 01 7A <product> <command> <payload…> F7
```

Payloads are packed **six bits per byte** — two payload bytes become three
SysEx bytes — not the usual seven. A backup file is simply the concatenated
stream of command `0x14` packets the device sends, and each packet carries a
trailing checksum:

```
checksum = sum(decoded[4:-1]) & 0xFF
```

Patterns live in sections 0-3, sixteen per section, matching the machine's four
coloured pattern pages. Each step of a pattern occupies four bytes, and each
byte packs **3 + 3 + 1 + 1** bits: two "full" voices carrying two state bits
(off / on / flam / roll) plus an accent bit, and two "simple" voices carrying a
single on/off bit. Guiro, both bongos, cowbell and clave are simple voices and
physically cannot hold an accent or a modifier.

## Tools

| script | what it does |
|---|---|
| `tools/cyclone_sysex.py` | frame codec, 6-bit pack/unpack, message decoding |
| `tools/parse_backup.py` | parse and diff `.tt78bak` files |
| `tools/write_backup.py` | rebuild backup files, recompute checksums |
| `tools/tt78_pattern.py` | TT-78 voice bit map, step encode/decode |
| `tools/build_full_bank.py` | write a generated 64-pattern bank into a backup |
| `tools/play_bank.py` | play the banks over MIDI (`mido`) |
| `tools/capture_alsa.sh`, `tools/send_alsa.sh` | capture and send SysEx via ALSA |
| `tools/run-cyclone-studio.sh` | launch Cyclone Studio under Wine with the MIDI port pre-selected |

Everything is plain Python 3 with no dependencies except `play_bank.py`, which
wants `mido`. `write_backup.py --verify <file>` re-encodes a backup from
scratch and compares it against the original; it reproduces every captured file
byte-for-byte.

## The pattern banks

`gen/` generates 64 patterns per machine, each 64 steps on the 16th-note scale.

The four pages are arranged by **feel of the kick** rather than by genre, since
while playing you reach for a page rather than a pattern number:

| page | | contents |
|---|---|---|
| 1 | red | four-to-the-floor - the steadiest material, kick on every beat |
| 2 | yellow | tresillo and kick-driven syncopation - dense kicks, displaced |
| 3 | green | breaks, rock and song styles |
| 4 | blue | percussion, grooves, texture and polyrhythm |

So pages 1 and 2 are the kick-forward half of each machine and pages 3 and 4
are everything else. `gen/page_order.py` holds the slot assignment and checks it
covers every style exactly once.

Every pattern carries a Fill variation: the same groove through bars 1-2, a
thicker bar 3, and a turnaround in bar 4 with a descending run over hats and
shakers that keep playing. Set an Auto-Fill Interval on the machine and it
fires automatically every few bars.

```
python3 gen/build.py        # step charts, MIDI files, JSON
python3 gen/verify.py       # checks over the generated output
python3 gen/build_ui.py     # a browsable pattern book, out/pattern-book.html
```

Output lands in `out/`: per-machine step charts, one MIDI file per pattern plus
a full-bank file, and the JSON the other tools read.

### Getting them onto a machine

Two routes.

**Over MIDI**, which needs nothing decoded: the machines respond to Note On for
every instrument and read velocity ≥ 112 as an accent, so
`out/midi/<machine>_bank_all64.mid` plays the whole bank on the real voices.
Note that received notes are **not** recorded into pattern memory — that was
tested and does not work.

**Into pattern memory**, via a backup file:

```
python3 tools/build_full_bank.py <a-backup-from-your-machine>.tt78bak out.tt78bak
```

then restore `out.tt78bak` with Cyclone Studio. The base file supplies your
machine's serial and the sections this project does not generate.

## Running Cyclone Studio under Wine

Cyclone Studio is the only way to get a bank *into* a machine, and it is a
32-bit Qt5 Windows application. It runs fine under Wine, which is how the
hardware verification here was done.

### One-time setup

```bash
sudo dpkg --add-architecture i386 && sudo apt update
sudo apt install -y wine wine32:i386

export WINEPREFIX=~/.cyclone-studio WINEARCH=win32
export WINEDLLOVERRIDES="mscoree,mshtml="
wineboot -i
```

Download `CycloneStudio2.0_Windows.zip` from the Cyclone Analogic download page
and unpack it into the prefix:

```bash
unzip CycloneStudio2.0_Windows.zip -d ~/.cyclone-studio/drive_c/CycloneStudio
```

### Launching

```bash
tools/run-cyclone-studio.sh              # picks the first MidiSport it finds
tools/run-cyclone-studio.sh "My Iface"   # or match your interface by name
tools/run-cyclone-studio.sh --list       # show what Wine can see
```

The script exists because of one specific trap. Studio opens **MIDI port index
0** at startup; on a PipeWire desktop that index is a virtual port it cannot
open, so it throws inside RtMidi and dies before drawing its window, leaving
only this in the terminal:

```
MidiInWinMM::openPort: error creating Windows MM MIDI input port.
```

Studio stores its port choice through QSettings, which on Wine means the
registry, so the fix is to pre-select the interface. The script enumerates the
ports as Wine sees them, finds yours, writes the index to
`HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0`, and launches.

**Do not hardcode the index.** It shifts depending on what else holds an ALSA
sequencer client at the time - another running Wine instance is enough to move
it. Detect it at launch, which is what the script does.

### Before you connect

* The machine must be in **normal mode**, not the TAP-held boot mode.
* Its rear **MIDI Out/Thru switch must be on OUT**, not THRU. On THRU the jack
  only echoes what arrives at MIDI In and the machine sends nothing of its own.
* Cables both ways: machine **Out** to interface **In**, interface **Out** to
  machine **In**.

When it connects, the status line reads
`TT-78 Beat Bot: Firmware v1.0, Serial: ...`. If it stays blank, work through
the three points above before anything else.

## Backup and restore

### Backing up

Click **Backup** and save the file. Do this before your first restore and keep
it: it is the only way back, and it is also the base file the bank builder
needs.

### Building a bank

```bash
python3 tools/build_full_bank.py <your-backup>.tt78bak out.tt78bak
```

The base file supplies your unit's serial number and every section this project
does not generate; only the pattern sections are rewritten.

### Restoring

Click **Restore**. Wine's file dialog has no bookmark for your home directory,
so type the full path into the *File name* box, with `Z:` standing in for `/`:

```
Z:\home\you\rezosdrum-tools\out.tt78bak
```

It takes about half a minute and the progress bar runs to 100%.

## What is not done yet: the TT-606

The TT-606 has step charts, MIDI files and a pattern book like the TT-78, so it
plays over MIDI today. It **cannot yet be written into pattern memory**, for two
reasons:

1. **No base backup.** `build_full_bank.py` needs a backup taken from the
   machine to supply its serial number and the sections this project does not
   generate.
2. **The voice bit map is unknown.** `tools/tt78_pattern.py` maps which voice
   occupies which bits of a step, and every entry in it came from diffing a
   TT-78. The TT-606 has a different voice set - two toms, open and closed
   hats, rim shot and hand clap in place of the congas, bongos and guiro - so it
   needs its own map.

Everything else should carry over unchanged: the frame format, the six-bit
packing, the checksum, the section and index addressing and the record headers
are properties of the firmware, which both machines share.

Producing the map is mechanical. Back the machine up, then for each voice in
turn: clear a pattern slot, add a single plain hit on step 1 with that voice,
back up again, and diff:

```bash
python3 tools/parse_backup.py before.tt606bak after.tt606bak
```

Each diff reports one changed byte and the bit within it, which is that voice's
position. `docs/instrument_bitmap.md` describes the procedure and the traps -
chiefly that combining two voices in one capture makes the result ambiguous.

## Caution

Cyclone Studio's **Restore overwrites everything**: all patterns, tracks,
clips, kits and user settings. Take a backup before you restore anything and
keep it - it is the only way back.

Backup files contain your unit's serial number, which is why none are committed
here.

## Related

[`modmatrix/tt303editor`](https://github.com/modmatrix/tt303editor) documents
the SysEx format of the **TT-303 Bass Bot**, the sibling instrument this
repository does not cover.

## License

MIT.
