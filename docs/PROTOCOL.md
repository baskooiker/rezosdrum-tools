# RezOSDrum SysEx protocol

Reverse-engineered from **Cyclone Studio 2.0** (2.0.1612.4, 12-07-2016), the
official backup/restore/firmware utility, plus live capture from a TT-78.

Source of truth: `CycloneStudio2.0_Windows.zip` from the vendor's download page.
It is a 32-bit Qt5 C++ application with **unstripped symbols** — the class name
`FwUpdateCore`, the method `validateBackupPacket(std::vector<unsigned char>&)`
and the original project path are all still in the binary. Disassembled with
`objdump -d -M intel` (it reads `pei-i386` directly).

Confidence is marked per item. **Confirmed** = read directly out of the
disassembly or observed on the wire. **Inferred** = strongly implied but not yet
proven against hardware.

## Frame format — confirmed

```
F0  00 01 7A  <product>  <command>  <payload ...>  F7
    |         |          |
    |         |          +-- command byte, offset 5
    |         +------------- product code, offset 4
    +----------------------- three-byte manufacturer id
```

`validateBackupPacket` checks, in order, and these are its own error strings:

| check | failure message |
|---|---|
| length >= 15 | (silent reject) |
| bytes 0-3 == `F0 00 01 7A` | `SYSEX ERROR: invalid header` |
| byte 4 == the device's product code | `SYSEX ERROR: wrong product code` |
| byte 5 == `0x14` | `SYSEX ERROR: not a backup packet` |

## Product codes — offset 4

From the jump table in the product-code setter at `0x401370`, which selects the
firmware-update button prompt shown for each device.

| code | prompt string | device | confidence |
|---|---|---|---|
| 0 | `TAP / WRITE` | TT-303 family | confirmed table entry |
| 1 | `WRITE / NEXT` | TT-303 family | confirmed table entry |
| 2 | `NEXT/TAP` | TT-303 family | confirmed table entry |
| 3-7 | (none) | unused | confirmed |
| 8 | `TAP` | TT-606 Drum Drone | inferred |
| 9 | `TAP` | TT-78 Beat Bot | **confirmed on the wire** |
| `00` | — | wildcard, used before the device is known | confirmed |

## Commands — offset 5

| cmd | direction | meaning | confidence |
|---|---|---|---|
| `0x10` | host to device | carries a 32-bit value and a byte; sent in mode 2 | confirmed shape, purpose inferred |
| `0x12` | device to host | emitted on front-panel activity; 31-byte frame | observed |
| `0x13` | host to device | control, with a sub-command byte | confirmed |
| `0x14` | device to host | **backup data packet** | confirmed |

### cmd 0x13 sub-commands

The sub-command sits at offset 18 of the 22-byte frame.

| sub | built at | reached from | confidence |
|---|---|---|---|
| `0x00` | `0x40676b` | state-machine mode 2 | confirmed |
| `0x01` | `0x406526` | state-machine mode 1 (startup discovery) | confirmed |
| `0x02` | `0x40692b` | state-machine mode 4 | confirmed |

### Discovery message — reconstructed

Mode 1 is entered by the UI setup function at `0x40dfa0`, so this is the poll
Studio fires before it knows what is attached. Product code is the `00` wildcard:

```
F0 00 01 7A 00 13 00 00 00 00 00 00 00 00 00 00 00 00 01 00 01 F7
```

Untested against hardware — the interface was unplugged before it could be sent.

## Payload encoding: 6 bits per byte — confirmed

Cyclone does **not** use the usual 7-bit MIDI packing. Every pair of payload
bytes becomes three SysEx bytes: the low 6 bits of each byte get their own
slot, and the high 2 bits of both are collected into a third.

```
encode(b0, b1) -> out0 = b0 & 0x3F
                  out1 = b1 & 0x3F
                  out2 = ((b1 >> 6) & 0x03) << 2 | ((b0 >> 6) & 0x03)

decode(out0, out1, out2) -> b0 = out0 | ((out2 & 0x03) << 6)
                            b1 = out1 | (((out2 >> 2) & 0x03) << 6)
```

Read from the packing loop at `0x406330` and repeated verbatim in every builder.
Implemented in `tools/cyclone_sysex.py`.

## State machine

`FwUpdateCore` dispatcher at `0x408610`, five modes via a jump table at
`0x408a40`.

| mode | handler | sends | entered from |
|---|---|---|---|
| 0 | `0x40864d` | (tick / timeout bookkeeping) | the MIDI receive path |
| 1 | `0x40879b` | cmd 13 sub 01 | UI setup `0x40dfa0` — startup discovery |
| 2 | `0x4088b3` | cmd 10, then cmd 13 sub 00 | mode 1, on a reply |
| 3 | `0x4089f5` | (none) | UI `0x40e410` |
| 4 | `0x408a07` | cmd 13 sub 02 | UI |

Bulk firmware transfer is a separate path: the packed builder at `0x406415`,
wrapper `0x4071f0`, driven from `0x410e00`. **Keep clear of that one.**

## What is still unknown

- Which cmd 13 sub-command starts a backup. Three candidates, and one of the
  five modes is firmware-related, so this wants care rather than brute force.
- The layout inside a cmd `0x14` backup packet — how patterns, steps, accents,
  flams and rolls are arranged. This is the actual goal, and it needs a real
  dump to diff against known pattern content.
- Whether there is a checksum, and over what span.

## Boot mode — the missing precondition

Every reconstructed control frame was sent to a TT-78 in normal running mode and
**none drew a reply**, with a deliberately malformed control frame sent before
and after each batch to prove the capture path was live and not echoing:

| frame | result |
|---|---|
| cmd 13 sub 01, wildcard product, serial `FFFFFFFF` | no reply |
| cmd 13 sub 01, product 09, serial `FFFFFFFF` | no reply |
| cmd 13 sub 00 / 01 / 02, products 00 and 09, device's own serial | no reply |

Cyclone Studio's own UI text explains why. It walks the user through a
power-cycle into a service mode before it talks to the device:

```
While pressing the <TAP> button, turn the device OFF now.
While still pressing the <TAP> button, turn the device ON now.
You may release the <TAP> button, click [ Continue ].
```

The button named in those prompts is chosen by product code — the same jump
table that gives the device mapping. For product codes 8 and 9, the drum
machines, the button is **TAP**. Studio ships matching artwork: the binary
contains `panel off boot_78.png`, `panel on boot_78.png` and
`panel updating boot_78.png`.

So the working hypothesis is that the RezOSDrum SysEx command set is only live
in boot mode, and that in normal mode the machine merely *broadcasts* — the
spontaneous cmd `0x12` event frames we captured on button presses, which carry
the product code and what appears to be the serial. That would also explain how
Studio populates `TT-78 Beat Bot: Firmware v%s, Serial: %s` without a handshake.

Entering boot mode is a documented, user-facing procedure and is undone by an
ordinary power cycle.

### Serial number

The cmd `0x12` event frame carries, at offsets 6-11, the 6-bit-packed bytes
`SS SS SS SS SS SS`, which decode to the four bytes `SS SS SS SS`. That is almost certainly the
unit's serial number, and it is what to put in the serial field when addressing
this specific machine.

## Boot mode confirmed, and the hello frame

Holding **TAP** through a power cycle does enter a distinct mode: the PAGE
button stays blue, and the machine emits one frame at power-on and then waits.
Releasing TAP drops it into normal operation.

```
F0 00 01 7A 09 11 00 00 00 00 00 00 00 00 00 00 00 00 05 01 01 00 00 00 F7
            ^^ ^^ product 09, command 0x11
```

Command `0x11` appears nowhere in Studio's send path — it is device-to-host
only. It is a **repeating beacon**, not a one-shot: the machine re-emits it
while sitting idle in boot mode. (An earlier note here said it fired once at
power-on; that was wrong, and it matters, because it means a host can answer it
at any time rather than having to race the power-up.) Its 18 packed body bytes
decode to 12 bytes:

```
00 00 00 00 00 00 00 00 45 01 00 00
```

The leading four bytes, where the serial sits in other frames, are zero. A CC
message (`B0 2C 6A`) precedes it on power-up.

Capturing this reliably requires **one continuously open listener**. A loop of
`amidi -S ... -r` invocations closes the port between iterations and drops the
one-shot hello; run `amidi -p <port> -r <file> -t <n> &` as a separate process
and send from a second process. The two coexist fine.

### Boot mode was a wrong turn

Ten candidate frames — cmd `0x10` and cmd `0x13` sub `00`/`01`/`02`, both
product codes — were sent to the machine in boot mode across two runs. The
hello was captured both times; **not one frame drew a reply**.

Re-reading Studio's UI text, the TAP power-cycle belongs to the *firmware
update* flow ("To begin the firmware update..."). Backup has its own, much
gentler precondition: "Make sure your device is switched on and if applicable,
set the MIDI OUT/THRU switch to the OUT position." So backup is expected to work
in **normal** mode, and boot mode is not the missing precondition for it.

## Backup packet structure — from the sequencer at 0x4016a0

This function gates incoming backup packets. It accepts **only** command `0x14`,
then indexes the packet from its decoded payload:

```
index = data[5] + (data[4] << 5)        i.e. data[4] * 32 + data[5]
```

It rejects anything whose index is below a running counter at `+0xa4048`, so
packets arrive in ascending order and the counter tracks progress. `data[4]` is
bounded:

| data[4] | meaning |
|---|---|
| 0x00-0x06 | ordinary payload pages |
| 0x64-0x6A | a second range, accepted | 
| 0x7E | accepted, terminator-like |
| 0x7F | sets a completion flag at `+0xa405c` |

The per-device branch is chosen by `product_code - 1` through a table at
`0x401800` with a jump table at `0x4017f0`.

## The search space is closed

Studio contains exactly **five** SysEx builders, all now reconstructed:

| builder | command | notes |
|---|---|---|
| `0x4062fc` | `0x10` | 16 bytes, serial + one byte argument |
| `0x406526` | `0x13` sub `01` | 22 bytes, wildcard product |
| `0x40676b` | `0x13` sub `00` | 22 bytes |
| `0x40692b` | `0x13` sub `02` | 22 bytes |
| `0x406415` | `0x13` packed | bulk firmware transfer - do not send |

So the backup request is certainly one of `0x10`, or `0x13` with sub `00`, `01`
or `02`. What is not yet right is one of the *fields* — most likely the serial,
or the byte argument to cmd `0x10`, both of which are supplied by the caller
from object state rather than as constants.

## State machine, decoded

Dispatcher `0x408610`, state variable at `+0xa4090`, set through vtable slot
`+0x4c`.

| mode | states that act | what it sends |
|---|---|---|
| 0 | 1, 2, 6, 8, 10 | nothing — this is the timer tick; it advances state on elapsed time |
| 1 | 1-5, 10 | cmd `0x13` sub `01`, every 3000 ms |
| 2 | 0 | cmd `0x10`, byte argument `0` |
| 2 | 2, 13 | cmd `0x13` sub `00` |
| 2 | 12 | backup in progress — this is the state the receive path requires before it will accept a cmd `0x14` packet |
| 4 | — | cmd `0x13` sub `02` |

`0x405f00`, which every builder calls with its buffer, is only
`std::vector::assign`. There is **no checksum and no post-processing** — the
bytes each builder lays down are exactly what goes on the wire. So the frames
reconstructed here are byte-identical to Studio's, and the reason the machine
ignores them is not a malformed frame.

## Why guessing stopped working

Every field that is a constant has been read off. The fields that remain are
supplied from object state — the serial at `+0xa40a4`, the product code at
`+0xa40cc`, the state at `+0xa4090` — and their values depend on a conversation
the app has already had with the device. Reconstructing that conversation by
guessing field values one at a time is not converging.

## Next step: run Cyclone Studio under Wine

The app is a 32-bit Qt5 Windows binary; Wine 9.0 is packaged on this machine's
distribution and the ALSA sequencer modules needed to expose the MidiSport to it
are already loaded. Running the real application against the real hardware
settles everything at once:

* If Backup works, it writes a `.tt78bak` file — and the remaining problem
  becomes offline diffing of saved files, which is far easier than live
  protocol work and needs no special timing.
* Either way, a MIDI monitor on the port captures the genuine conversation,
  which pins the field values that cannot be read as constants.

This also removes the dependency on a Mac install that will not run.

# SOLVED: Cyclone Studio runs under Wine

The live-protocol work above is superseded. The real application runs on this
Linux box against the real hardware, which makes the whole handshake question
moot.

## Setup

```
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y wine wine32:i386          # Wine 9.0, Ubuntu 24.04

export WINEPREFIX=~/.cyclone-wine WINEARCH=win32
export WINEDLLOVERRIDES="mscoree,mshtml="
wineboot -i
```

Unzip `CycloneStudio2.0_Windows.zip` into the prefix and run
`wine "Cyclone Studio.exe"`.

### The one non-obvious step

Studio opens MIDI **port index 0** at startup. On a PipeWire desktop that index
is a virtual port with no usable capabilities; opening it throws inside RtMidi
and the app dies before drawing its window, printing only:

```
MidiInWinMM::openPort: error creating Windows MM MIDI input port.
```

The fix is to pre-select the interface. Studio stores its port choice through
QSettings under keys `inPort` and `outPort`, which on Wine live in the registry.
Find the index of the wanted interface in Wine's own enumeration
(`WINEDEBUG=+midi wine "Cyclone Studio.exe"` prints a `port_add MidiIn [n]`
line per port), then:

```
wine reg add "HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0" \
     /v inPort  /t REG_DWORD /d <n> /f
wine reg add "HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0" \
     /v outPort /t REG_DWORD /d <n> /f
```

With that seeded, Studio starts, detects the machine and reports:
`TT-78 Beat Bot: Firmware v1.0, Serial: <unit serial>`.
Backup and Restore then work normally. The device must be in **normal** mode,
not boot mode, with the rear switch on OUT.

## Backup file format

A `.tt78bak` is just the concatenated SysEx stream, every message a command
`0x14` packet. Decoding each payload with the 6-bit unpacker gives:

| offset | meaning |
|---|---|
| 0-3 | device serial, little-endian |
| 4 | section id |
| 5 | index within the section |
| 6.. | section data |

This confirms the static analysis exactly: command `0x14`, the serial field
packing, and the `data[4]`/`data[5]` indexing read out of the sequencer at
`0x4016a0`, including `0x7F` as the terminating section.

A 66,355-byte TT-78 backup contains 658 packets:

| section | packets | data per packet | total |
|---|---|---|---|
| 0 | 80 | 70 B | 5600 B |
| 1 | 128 | 70 B | 8960 B |
| 2 | 128 | 70 B | 8960 B |
| 3 | 122 | 70 B | 8540 B |
| 7 | **64** | 76 B | 4864 B |
| 100-108 | 15 each | 14x2 B + 1x4 B | — |
| 127 | 1 | 6 B | terminator |

Section 7 having exactly 64 packets, one per pattern slot, is the obvious
candidate for per-pattern metadata. Sections 0-3 hold the bulk, 32,060 bytes,
which is where step data must live.

Note that no section is all-zero even though 63 of the 64 pattern slots are
empty, so the encoding is bit-packed rather than sparse. Identifying fields by
inspection is therefore unreliable; use the diff protocol below.

## Diff protocol, now that backups are cheap

Each backup is about 30 seconds. Change exactly one thing between them and run:

```
python3 tools/parse_backup.py captures/a.tt78bak captures/b.tt78bak
```

It reports the changed packets by section and index, and the individual bit
flips, which is what pins the layout.

| backup | edit made first |
|---|---|
| `empty.tt78bak` | clear a slot with `[CLEAR]+[#]` |
| `bd1.tt78bak` | add BD on step 1 |
| `bd12.tt78bak` | add BD on step 2 as well |
| `bd1_acc.tt78bak` | accent step 1 |
| `bd1_flam.tt78bak` | flam instead |
| `bd1_roll.tt78bak` | roll instead |
| `sd1.tt78bak` | clear BD, add SD on step 1 |
| `len64.tt78bak` | set the pattern length to 64 |

Keep the very first backup untouched: **Restore overwrites patterns, tracks,
clips, kits and user settings**, and it is the only way back.

# Pattern step encoding — DECODED

Established by diffing four backups that differ by one deliberate edit each,
all on pattern 1, instrument 1 (Bass Drum):

| edit | byte that changed | bits |
|---|---|---|
| accent on step 8 | `data[33]` `01` -> `05` | bit 2 set |
| flam on step 1 | `data[5]` `05` -> `06` | bits 0-1: `01` -> `10` |
| roll on step 5 | `data[21]` `0d` -> `0f` | bits 0-1: `01` -> `11` |

## Packet layout, sections 0-3

70 data bytes per packet (after the 6-byte serial/section/index header):

| offset | size | meaning |
|---|---|---|
| 0-4 | 5 | record header (`20 01 08 10 00` for pattern 1) |
| 5-68 | 64 | **16 steps x 4 bytes** |
| 69 | 1 | trailer |

Step *N* of the packet begins at `data[5 + 4*(N-1)]`: step 1 at 5, step 5 at 21,
step 8 at 33. The stride is confirmed by all three edits independently.

## Within a step block

Byte 0 of each 4-byte step block carries **instrument 1**:

```
bit 1 0   state    00 off    01 on    10 flam    11 roll
bit 2     accent
bit 3+    belong to other instruments, not yet mapped
```

Decoding instrument 1 across pattern 1 gives a musically coherent part, which
is the strongest confirmation that the mapping is right:

```
base            X...X..xX...X..x      accented kick on all four beats,
+accent step 8  X...X..XX...X..x      pickups on 8 and 16
+flam step 1    F...X..XX...X..x
+roll step 5    F...R..XX...X..x
```

Each edit appears at exactly the step the edit was made on.

## Still open

* **The other 13 instruments.** Only 3 bits of each 32-bit step block are
  mapped. 14 instruments x 3 bits is 42 bits, which does not fit in 32, and
  section-0 packets come in pairs sharing an index — so a pattern's instruments
  are almost certainly split across two packets. Diffing an edit on instrument 2
  and on instrument 8 would settle the split and the per-instrument stride.
* **The trailer `data[69]`.** For pattern 1's packet it equals
  `sum(data[0:69]) & 0xFF` across all four files, and its delta tracked every
  edit exactly. But only 2 of 458 packets in the file satisfy that relation, so
  it is not a uniform packet checksum. Treat it as unresolved rather than
  assuming it is safe to recompute.
* **Tone is not stored.** A backup taken after setting instrument 1's Tone to
  zero was **byte-identical** to the one before it. The Tone control is a live
  analog potentiometer, not per-pattern state, so voice variation cannot be
  written through a backup file. It would only persist inside a Kit, if at all.
* **Pattern length and time scale** are presumably in the 5-byte record header
  `20 01 08 10 00`; a backup taken after changing a pattern's length would
  identify those bytes.

# Pattern record layout — from the pattern-5 and length diffs

## Addressing

* A pattern's packets sit in section 0 at `index = pattern number - 1`
  (pattern 1 -> index 0, pattern 5 -> index 4, both confirmed).
* A pattern occupies **2 packets per 16-step page**: a 16-step pattern is 2
  packets, a 64-step pattern is 8. Changing pattern 5 from 16 to 64 steps grew
  section 0 by exactly 6 packets and the file by 726 bytes.
* The two packets of a page are distinguished by the low bits of `data[0]`, and
  instruments are split between them.

## Record header, `data[0..4]`

| byte | meaning | evidence |
|---|---|---|
| 0 | `(pages << 5) \| packet sequence` | `20`/`21` for a 1-page pattern, `80`..`87` for a 4-page one |
| 1-4 | `ff ff ff ff` marks a **never-used pattern**; written on first edit | pattern 5 went `ff ff ff ff` -> `01 fe 10 00` when a step was added |
| 3 | length-related: `10` at 16 steps, `40` at 64 steps | the length edit changed only this and `data[0]` |

`data[3]` is *probably* the step count, but one other pattern in the file shows
`90` there, which is out of range for a 1-64 step length, so it carries flags as
well. Not safe to treat as a plain length byte yet.

## Instrument bits within a step block

Each step is 4 bytes = 32 bits. Instruments occupy a **3-bit stride**: two state
bits plus one accent bit.

| instrument | state bits | accent bit | evidence |
|---|---|---|---|
| 1 Bass Drum | 0-1 | 2 | plain hit set bit 0; flam `01`->`10`; roll `01`->`11`; accent set bit 2 |
| 2 Snare Drum | 3-4 | 5 | plain hit set bit 3 |

State enum, confirmed on the Bass Drum by three independent edits:
`00` off, `01` on, `10` flam, `11` roll.

### Unresolved: the rest of the instrument map

Two further data points do **not** fit a simple contiguous 3-bit map:

* Tambourine on step 1 set **bit 19** — the *second* state bit of the slot at
  bits 18-20, which would read as "flam", not a plain hit.
* Guiro on step 5 set **bit 6** — the first state bit of the slot at bits 6-8.

The TT-78 front panel groups voices under shared Track/Instrument positions
(Low Conga/Low Bongo, Clave/Cowbell, Cymbal/Hi-hat, Maracas/Tambourine/Guiro),
so a slot's 2-bit field may select *which voice of the group* rather than
flam/roll, with the meaning differing between grouped and ungrouped slots. That
would reconcile Tambourine reading as `10`, but not Guiro landing at bit 6.

Resolving this needs one diff per instrument, each a **plain hit on step 1 of an
otherwise empty pattern**, taken one instrument at a time.

# SOLVED: the packet checksum

```
decoded[-1] = sum(decoded[4:-1]) & 0xFF
```

The sum runs from the **section byte** to the second-to-last decoded byte. The
four serial bytes at the start are **excluded**, which is why earlier attempts
starting the sum at offset 0 or 6 failed.

Validated across all 22 backup files captured so far, roughly 11,500 packets,
with no exceptions among the long records.

The 19-byte records in sections 100-108 do not follow this rule; their trailer
appears to be `section + index - 1`. They are kit or system data that no pattern
edit touches, so `tools/write_backup.py` passes them through untouched rather
than recomputing them.

## Proof that the format is writable

`python3 tools/write_backup.py --verify <file>` re-encodes every packet from
scratch - unpacking, rebuilding the payload, recomputing checksums, repacking to
6-bit - and compares against the original. **All 22 files rebuild
byte-identically**, which validates the codec in both directions, the packet
framing, and the checksum together.

A generated pattern was then injected into packet 0 of a backup: exactly one
packet changed, the file size was unchanged, and reading it back reproduced the
pattern exactly.

# Pattern addressing across sections

Sections 0-3 each hold **16 patterns**, matching the machine's four coloured
pattern pages:

| section | patterns | page |
|---|---|---|
| 0 | 1-16 | red |
| 1 | 17-32 | yellow |
| 2 | 33-48 | green |
| 3 | 49-64 | blue |

```
section = (pattern - 1) // 16
index   = (pattern - 1) %  16
```

Within a section an index holds `2 * pages` packets, where `pages = length/16`:
2 packets for a 16-step pattern, 8 for a 64-step one.

**The packet order is grouped, not interleaved** - confirmed on hardware by
restoring a generated file and playing it back:

```
sequence 0 .. pages-1          the pattern's 16-step pages, in order
sequence pages .. 2*pages-1    the Fill's pages, in the same order
```

`data[0] = (pages << 5) | sequence`. An interleaved layout was tried first and
produced pages 2 and 4 silent, which is what identified the error.

`data[3]` is the **literal step count**: `0x10` = 16, `0x40` = 64, and a
pattern accidentally set to end on step 49 recorded `0x31` = 49.

Section 7 holds 4 packets per pattern of per-pattern metadata, not yet decoded.

# Remaining before writing to hardware

1. The generator must stop placing accents, flams and rolls on the five
   single-bit voices (Guiro, Low Bongo, High Bongo, Cowbell, Clave).
2. Writing 64-step patterns into slots that currently hold 16-step ones means
   **adding packets** (2 -> 8) and renumbering, not just editing in place.
3. The record header bytes `data[1..4]` are only partly understood: `ff ff ff ff`
   marks an unused slot, and `data[2]` varies between patterns (`08` vs `fe`)
   for reasons not yet established.
4. Section 7's per-pattern metadata may also need updating.
5. A Restore test on a slot that does not matter, with the original backup kept
   as the way back. **Restore overwrites patterns, tracks, clips, kits and user
   settings.**

# Fills

Sequences `pages..2*pages-1` of a pattern record hold the Fill variation. An
**empty Fill makes the FILL button replay the normal pattern**, which is what
the first generated bank did.

`gen/fills.py` builds a Fill from each pattern:

* Bars 1-2 are left alone, so the Fill is recognisably the same groove.
* Bar 3 thickens - sixteenth hats, a shaker on the offbeats - unless the
  pattern is sparse, in which case it is left as it is.
* Bar 4 turns around: the last eight steps clear for a descending run across
  whichever full voices the pattern uses (high conga, low conga, snare), with a
  flam leading in and a roll on the final step, and an accented kick and cymbal
  on the downbeat.
* **Timekeepers keep playing.** Hi-hat, maracas, tambourine and cowbell run
  through the fill rather than stopping dead. An earlier version cleared them
  and the result was a hole in the bar rather than a fill - obvious in the
  latin and disco patterns, where the shaker *is* the pulse.
* The five single-bit voices are switched on and off only, never modified.

Set an Auto-Fill Interval with `[TIME]`+`[FILL]` (or CC16, values 0/1/2/4/8/16)
and the machine fires the Fill automatically every N bars.
