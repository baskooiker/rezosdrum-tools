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

Everything is plain Python 3 with no dependencies except `play_bank.py`, which
wants `mido`. `write_backup.py --verify <file>` re-encodes a backup from
scratch and compares it against the original; it reproduces every captured file
byte-for-byte.

## The pattern banks

`gen/` generates 64 patterns per machine, each 64 steps on the 16th-note scale,
across four pages of sixteen: four-to-the-floor, breaks and electro, machine
rock, and grooves and polyrhythm on the TT-606; CR-78 preset heritage, latin
and afro, electronic reinterpretations, and percussion studies on the TT-78.

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

Studio is a 32-bit Qt5 Windows application and runs under Wine, which is how
the hardware verification here was done.

```
sudo dpkg --add-architecture i386 && sudo apt update
sudo apt install -y wine wine32:i386
export WINEPREFIX=~/.cyclone-wine WINEARCH=win32
export WINEDLLOVERRIDES="mscoree,mshtml="
wineboot -i
```

Studio opens MIDI **port index 0** at startup. On a PipeWire desktop that is a
virtual port it cannot open, and it dies before drawing its window with only
`MidiInWinMM::openPort: error creating Windows MM MIDI input port.` to show for
it. Find your interface's index with
`WINEDEBUG=+midi wine "Cyclone Studio.exe"`, then pre-select it:

```
wine reg add "HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0" \
     /v inPort  /t REG_DWORD /d <n> /f
wine reg add "HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0" \
     /v outPort /t REG_DWORD /d <n> /f
```

The machine must be in normal mode, not the TAP-held boot mode, with its rear
MIDI Out/Thru switch set to **OUT**.

## Caution

Cyclone Studio's **Restore overwrites everything**: all patterns, tracks,
clips, kits and user settings. Take a backup before you restore anything and
keep it. Backup files contain your unit's serial number, which is why none are
committed here.

## Related

[`modmatrix/tt303editor`](https://github.com/modmatrix/tt303editor) documents
the SysEx format of the **TT-303 Bass Bot**, the sibling instrument this
repository does not cover.

## License

MIT.
