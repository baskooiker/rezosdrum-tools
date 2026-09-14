# TT-78 instrument bit map (in progress)

Each step of a pattern occupies **4 bytes** starting at `data[5 + 4*(step-1)]`
of a section-0 packet, read as a 32-bit little-endian bit field. A plain hit
sets the voice's first state bit; the position of that bit is what this table
records.

State enum per voice, confirmed on the Bass Drum:
`00` off, `01` on, `10` flam, `11` roll — with the accent bit immediately above
the two state bits.

## The map

Each byte of the 4-byte step block is laid out as **3 + 3 + 1 + 1 bits**: two
"full" voices carrying two state bits plus an accent bit, and two "simple"
voices carrying a single on/off bit.

| byte | full voice (bits) | full voice (bits) | simple | simple |
|---|---|---|---|---|
| 0 | BD Bass Drum (0-2) | SD Snare Drum (3-5) | GU Guiro (6) | unassigned (7) |
| 1 | LC Low Conga (8-10) | HC High Conga (11-13) | LB Low Bongo (14) | HB High Bongo (15) |
| 2 | MA Maracas (16-18) | TB Tambourine (19-21) | unassigned (22) | CB Cowbell (23) |
| 3 | HH Hi-hat (24-26) | CY Cymbal (27-29) | CL Clave (30) | unassigned (31) |

Full voices encode `00` off, `01` on, `10` flam, `11` roll, with the accent bit
immediately above. Simple voices are a single bit and **cannot carry accent,
flam or roll** - a real hardware limit, not a gap in the reverse engineering.

Voices that cannot be accented or modified: **Guiro, Low Bongo, High Bongo,
Cowbell, Clave.**

## Cymbal and Hi-hat - resolved

They are separate full slots. A backup with both hit on step 1 gave
`data[8] 00 -> 09`, bits 24 and 27. A follow-up with **Hi-hat alone from switch
position 7** gave `data[8] 00 -> 01`, bit 24, confirming:

* **Hi-hat = bits 24-26**
* **Cymbal = bits 27-29**

The earlier `09-hihat` capture had in fact recorded the cymbal; its label was
wrong, which is why it and `12-cymbal` produced the same bit.

## Packet pairs: pattern and Fill

Each 16-step page of a pattern is stored as two packets, distinguished by
bit 0 of `data[0]`. Sub-packet **0 carries the pattern's steps**. Sub-packet 1
decodes to nothing coherent under the voice map, and since the manual gives
every pattern an optional **Fill** variation - and a 16-step pattern occupies
exactly 2 packets while a 64-step one occupies 8 - sub 1 is almost certainly the
Fill. Not yet confirmed by a targeted diff.

## Validation

Decoding pattern 1 of the original backup with this map yields a coherent
groove rather than noise, which is the strongest available check:

```
BD  Bass Drum    X...X..xX...X..x
SD  Snare Drum   ...xx....xx...x.
LC  Low Conga    .X....X....X....
HC  High Conga   ...x..........x.
HB  High Bongo   ......x.x.......
MA  Maracas      xxxxxxxxXxxxxxXx
TB  Tambourine   ...........x..x.
CB  Cowbell      .x..............
HH  Hi-hat       x.x.x.x.x.x.x.x.
CY  Cymbal       ..x......x......
CL  Clave        ......x...x...x.
```

## MB / Metallic Beat

`MB` is silkscreened on switch positions 6 and 7 but no second voice can be
selected there, and it has no note number in the MIDI implementation chart. It
is CR-78 heritage printing, not a reachable voice. **Thirteen voices.**

## Voices that cannot take modifiers

Single-bit voices, on/off only - no accent, flam or roll:
**Guiro, Low Bongo, High Bongo, Cowbell, Clave.**

The pattern generator must respect this; several generated TT-78 patterns
currently place accents or flams on these voices.
