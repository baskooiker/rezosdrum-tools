# TT-606 instrument bit map

The container is the same as the TT-78's: four bytes per step starting at
`data[5 + 4*(step-1)]` of a section-0 backup packet, read as a 32-bit
little-endian field. The voice layout differs, because the Drum Drone has nine
voices where the Beat Bot has thirteen.

State enum, identical on both machines:
`00` off, `01` on, `10` flam, `11` roll.

## The map

| voice | state bits | accent bit |
|---|---|---|
| BD Bass Drum | 0-1 | 2 |
| SD Snare Drum | 3-4 | 5 |
| LT Low Tom | 8-9 | 10 |
| HT High Tom | 11-12 | 13 |
| RS Rim Shot | 16-17 | 18 |
| CP Hand Clap | 19-20 | 21 |
| CH Closed Hi-hat | 24-25 | 26 |
| OH Open Hi-hat | 27-28 | 29 |
| **CY Cymbal** | **30-31** | **22** |

By byte:

```
byte 0   BD 0-2      SD 3-5      spare 6, 7
byte 1   LT 8-10     HT 11-13    spare 14, 15
byte 2   RS 16-18    CP 19-21    CY accent 22    spare 23
byte 3   CH 24-26    OH 27-29    CY state 30-31
```

Eight voices keep their accent bit directly above their two state bits. The
cymbal cannot: byte 3 is full after the two hi-hats, so its state occupies the
two bits left at the top and **its accent is stored remotely in bit 22**, the
spare bit of byte 2.

**Every TT-606 voice takes accent, flam and roll.** Unlike the TT-78 there are
no restricted voices.

## How it was established

A single backup, using a much better method than the per-voice diffing used on
the TT-78. Each of the nine voices was placed alone in its own pattern - voice
one in pattern 1, voice two in pattern 2, and so on in Track/Instrument switch
order - and within each pattern the voice was written four times:

| step | modifier |
|---|---|
| 1 | plain |
| 5 | accent |
| 9 | flam |
| 13 | roll |

Because each voice sits in its own packet there is nothing to diff: every bit
position, and every modifier encoding, reads directly out of one file. Two
captures were enough for the whole machine.

Verify a capture with:

```
python3 tools/tt606_pattern.py <file>.tt606bak <pattern number>
```

which should print `x...X...f...r...` for the voice in that pattern.

## Still needed for a TT-606 bank

The step encoding is solved, so what remains is the generator side: a
`build_full_bank.py` equivalent that writes TT-606 lanes, and confirmation that
the record headers and page layout behave as they do on the TT-78. The frame
format, six-bit packing, checksum and addressing are already confirmed
identical - the checksum rule validates on 326 of 328 long packets in a TT-606
backup, the two exceptions being the same short kit and terminator records that
differ on the TT-78.
