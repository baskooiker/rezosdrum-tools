# TT-606 — 64-pattern bank

Every pattern is **64 steps** long on the 16th-note time scale (4 bars). Set pattern length with `[FUNC]+[LENGTH]`, then page to step 64 and press `[16]`.

Legend: `.` off   `x` on   `X` accent   `f` flam   `F` flam+accent   `r` roll   `R` roll+accent

Voices on this machine:

| Key | Instrument | MIDI note | Tone CC | Nuance shape | Nuance amount | Inst select |
|---|---|---|---|---|---|---|
| BD | Bass Drum | 36 | 20 | 22 | 23 | - |
| SD | Snare Drum | 38 | 28 | 30 | 31 | - |
| LT | Low Tom | 43 | 36 | 38 | 39 | - |
| HT | High Tom | 48 | 44 | 46 | 47 | - |
| CY | Cymbal | 51 | 52 | 54 | 55 | 56 |
| OH | Open Hi-hat | 46 | 60 | 62 | 63 | 64 |
| CH | Closed Hi-hat | 42 | 68 | 70 | 71 | 72 |
| RS | Rim Shot | 37 | 76 | 78 | 79 | - |
| CP | Hand Clap | 39 | 84 | 86 | 87 | - |


## Page 1 (Red) — patterns P1–P16

### P01 — House
*Four-to-the-floor · 124 BPM · 64 steps · 16th-note scale · flam time 32*

Textbook 4/4 house: offbeat open hat, clap on the backbeat, rim ghost lifting into the next bar.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x.......x.x.
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ..............x. ..............x. ..............x. ..............x.
  CP    ....x.......x... ..x.x.......x... ....x.......x... ....x.......f...
  ACC*  x............... x............... x............... x...............
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=64
- **Hand Clap (CP)** — tone CC84=60, nuance shape CC86=6, nuance amount CC87=40
- **Open Hi-hat (OH)** — variation 2 (CC64=2), tone CC60=70

### P02 — Deep House
*Four-to-the-floor · 120 BPM · 64 steps · 16th-note scale*

Softer hats, one clap per bar, kick tuned long and round.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x...x...x...
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    x..xx..xx..xx..x x..xx..xx..xx..x x..xx..xx..xx.xx x..xx..xx..xx..r
  RS    ......x.....x... ......x.....x.x. ......x.....x... ......x.....x...
  CP    ....x........... ....x..........x ....x........... ....f...........
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=40, nuance shape CC22=8, nuance amount CC23=30
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=44, nuance shape CC70=12, nuance amount CC71=52
- **Open Hi-hat (OH)** — variation 4 (CC64=4), tone CC60=52

### P03 — Tech House
*Four-to-the-floor · 126 BPM · 64 steps · 16th-note scale*

Sixteenth hats with a pushed kick on the last step.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x..x x...x...x...x..x x...x...x...x..x x...x...x...x.xx
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxx
  RS    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=78
- **Open Hi-hat (OH)** — variation 1 (CC64=1), tone CC60=66

### P04 — Techno
*Four-to-the-floor · 132 BPM · 64 steps · 16th-note scale*

Deliberately strict — no bar-to-bar variation. Let the Tone knobs do the moving.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  CY    x............... x............... x............... x...............
  OH    ............x... ............x... ............x... ............x...
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  RS    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 0 (CC72=0), tone CC68=90, nuance shape CC70=2, nuance amount CC71=20
- **Cymbal (CY)** — variation 1 (CC56=1), tone CC52=30

### P05 — Hard Techno
*Four-to-the-floor · 145 BPM · 64 steps · 16th-note scale*

Everything accented, kick tuned short and clicky, snare slam into the turnaround.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X.x.
  SD    ..............X. ..............X. ..............X. ............fxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x.......x....... x.......x....... x.......x....... x.......x.......
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxx
  ACC*  X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=20, nuance shape CC22=30, nuance amount CC23=96
- **Closed Hi-hat (CH)** — variation 5 (CC72=5), tone CC68=110
- **Cymbal (CY)** — variation 3 (CC56=3), tone CC52=100

### P06 — Minimal
*Four-to-the-floor · 128 BPM · 64 steps · 16th-note scale*

Almost nothing. Space is the instrument.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  CH    ..x.....x....... ..x.....x....... ..x.....x....... ..x.....x.......
  RS    ......x......... ......x......... ......x......... ......x.........
  CP    ............x... ............x... ............x... ............x...
  ACC*  x............... x............... x............... x...............
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=50, nuance shape CC70=20, nuance amount CC71=24
- **Rim Shot (RS)** — tone CC76=70

### P07 — Dub Techno
*Four-to-the-floor · 122 BPM · 64 steps · 16th-note scale*

Long, soft open hat as the only bright thing in the pattern.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x.......x...
  OH    ..............x. ..............x. ..............x. ..............x.
  CH    ..x...x...x...x. ..x...x...x...r. ..x...r...x...x. ..x...x...x...x.
  RS    ........x....... ........x....... ........x....... ........x.......
  CP    ....x........... ....x........... ....x........... ..x.x...........
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 4 (CC72=4), tone CC68=34, nuance shape CC70=16, nuance amount CC71=64
- **Open Hi-hat (OH)** — variation 5 (CC64=5), tone CC60=40, nuance shape CC62=22, nuance amount CC63=80

### P08 — Tribal Techno
*Four-to-the-floor · 130 BPM · 64 steps · 16th-note scale*

Toms carry the groove; the three-against-four rim keeps it rolling.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x.......x...
  LT    ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x.Xxx
  HT    ....x.......x... ....x..x....x... ....x.......x... ....x...X.x.x...
  OH    ......x......... ......x......... ......x......... ..x...x.........
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  ACC*  x.....x.....x... x.....x.....x... x.....x.....x... x.....x.....x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **High Tom (HT)** — tone CC44=80, nuance shape CC46=10, nuance amount CC47=48
- **Low Tom (LT)** — tone CC36=44, nuance shape CC38=10, nuance amount CC39=48

### P09 — Detroit Techno
*Four-to-the-floor · 134 BPM · 64 steps · 16th-note scale*

Stuttering hat figure, cymbal wash on the downbeat.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x.x.
  HT    ..........x..... ..........x..... ..........x..... ..........x.....
  CY    x............... x............... x............... x...............
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    x.xxx.xxx.xxx.xx x.xxx.xxx.xxx.rx x.xxx.xxx.xxx.rx x.xxx.xxx.xxx.xx
  CP    ....x.......x... ....x.......x... ....x.......x... ....x...x...x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=84
- **Hand Clap (CP)** — tone CC84=72, nuance shape CC86=4, nuance amount CC87=56
- **Cymbal (CY)** — variation 2 (CC56=2), tone CC52=62

### P10 — Acid Techno
*Four-to-the-floor · 138 BPM · 64 steps · 16th-note scale*

The classic 606-under-a-303 pattern. Global accent alternates strong/stronger.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x...x...x...
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x.......x....... x.......x....... x.......x....... x.......x...x...
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  RS    .....x.....x.... .....x.....x.... .....x.....x.... x....x.....x....
  ACC*  x...X...x...X... x...X...x...X... x...X...x...X... x...X...x...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=96
- **Snare Drum (SD)** — tone CC28=88, nuance shape CC30=14, nuance amount CC31=70

### P11 — Hardgroove
*Four-to-the-floor · 136 BPM · 64 steps · 16th-note scale*

Dense percussive layers with an accent lane in threes against the four.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  LT    ......x.....x... ......x.....x... ......x.....x... ......x.....xXxx
  HT    ..........x..... .......x..x..... ..........x..... ........X.x.x...
  OH    ..x.......x..... ..x...x...x..... ..x.......x..... ..x...x...x.....
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxx
  RS    x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..xx.x
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......f...
  ACC*  x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 4 (CC72=4), tone CC68=100
- **Rim Shot (RS)** — tone CC76=90, nuance shape CC78=8, nuance amount CC79=60

### P12 — Schranz
*Four-to-the-floor · 150 BPM · 64 steps · 16th-note scale*

Distorted-kick territory: double kick figure, cymbal on every beat.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    X..xX..xX..xX..x X..xX..xX..xX.xx X..xX..xX..xX..x X..xX..xX..xX..x
  SD    ..............X. ..............X. ..............X. ............xxxr
  CY    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  OH    ......x......... ..x...x......... ......x......... ......x.........
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxrxxxxxxxxx xxxxxxxxxxxxxxxx
  ACC*  X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=12, nuance shape CC22=31, nuance amount CC23=110
- **Cymbal (CY)** — variation 3 (CC56=3), tone CC52=118

### P13 — Trance
*Four-to-the-floor · 138 BPM · 64 steps · 16th-note scale*

Big offbeat hat, rolling sixteenths, fills every fourth bar.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x.x.
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  RS    ...........x.... ...........x.... ...........x.... ...........x....
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......f...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Cymbal (CY)** — variation 1 (CC56=1), tone CC52=74
- **Open Hi-hat (OH)** — variation 3 (CC64=3), tone CC60=90

### P14 — Psy
*Four-to-the-floor · 145 BPM · 64 steps · 16th-note scale*

Rolling triplet-feel tom underneath a rigid kick. Strict on purpose.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  LT    .x.x.x.x.x.x.x.x .x.x.x.x.x.x.x.x .x.x.x.x.x.x.x.x .x.x.x.x.x.x.x.x
  CY    x.......x....... x.......x....... x.......x....... x.......x.......
  OH    ......x.......x. ......x.......x. ......x.......x. ......x.......x.
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 5 (CC72=5), tone CC68=104
- **Low Tom (LT)** — tone CC36=30, nuance shape CC38=6, nuance amount CC39=20

### P15 — Hardcore
*Four-to-the-floor · 165 BPM · 64 steps · 16th-note scale*

Fast and blunt. Cymbal eighths give it the rave sheen.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X.x.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......fxxr
  LT    ................ ................ ................ .............Xxx
  HT    ..........x.x... .......x..x.x... ..........x.x... ........X.x.x...
  CY    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x.
  OH    ..............x. ..............x. ..............x. ..........x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  ACC*  X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=8, nuance shape CC22=31, nuance amount CC23=120
- **Snare Drum (SD)** — tone CC28=100

### P16 — Industrial Techno
*Four-to-the-floor · 128 BPM · 64 steps · 16th-note scale*

Snare on the half-bar, kick limping slightly off the grid.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x..x.x.. x...x...x..x.x.. x...x...x..x.x.. x...x...x..x.x..
  SD    ........X....... ........X....... ........X....... ........X.......
  LT    ..x.........x... ..x.........x... ..x.........x... ..x.........xXxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    .....x.....x.... .....x.....x.... .....x.....x.... .....x.....x....
  ACC*  x.......X....... x.......X....... x.......X....... x.......X.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=24, nuance shape CC22=26, nuance amount CC23=88
- **Cymbal (CY)** — variation 3 (CC56=3), tone CC52=20
- **Snare Drum (SD)** — tone CC28=30, nuance shape CC30=28, nuance amount CC31=100


## Page 2 (Yellow) — patterns P17–P32

### P17 — Electro
*Breaks & electro · 128 BPM · 64 steps · 16th-note scale*

Syncopated electro kick, straight backbeat, eighth hats.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.x.....x. x.....xxx.....x. x.....x.x.....x. x.....x.x.....xx
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  CP    ....x........... ....x........... ....x........... ....f...........
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=88
- **Snare Drum (SD)** — tone CC28=76, nuance shape CC30=10, nuance amount CC31=44

### P18 — Miami Bass
*Breaks & electro · 132 BPM · 64 steps · 16th-note scale*

808-style bass pattern with clap doubling the snare.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x..x...x..x.. x..x..x...x..x.. x..x..x...x..x.. x..x..x...x..xx.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......fxxr
  OH    ..............x. ..........x...x. ..............x. ..........x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  CP    ....x.......x... ....x..x....x... ....x.......x... x...x.......f...
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=18, nuance shape CC22=4, nuance amount CC23=24
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=92

### P19 — Breakbeat
*Breaks & electro · 136 BPM · 64 steps · 16th-note scale*

Loose funk break skeleton, snare doing the talking.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.....x... x.....x.....x... x.....x.....x... x.....x.....x...
  SD    ....x..x..x.x... ....x..x..x.x... ....x..x..x.x... ....x..x..x.xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ......x......... ......x......... ......x......... ..x...x.........
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ..........x..... ..........x..... ..........x..... ..........x.....
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Snare Drum (SD)** — tone CC28=70, nuance shape CC30=12, nuance amount CC31=60

### P20 — Big Beat
*Breaks & electro · 118 BPM · 64 steps · 16th-note scale*

Heavy, slightly slow, snare hit hard.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x..x..x.x... x...x..x..x.x.x. x...x..x..x.x... x...x..x..x.x...
  SD    ....X.......X... ....X.......X... ....X.......X... ....X.......xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ...........x.... .......x...x.... ...........x.... ........X.xxx...
  CY    x............... x............... x............... x...............
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  ACC*  x...X...x...X... x...X...x...X... x...X...x...X... x...X...x...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Cymbal (CY)** — variation 2 (CC56=2), tone CC52=54
- **Snare Drum (SD)** — tone CC28=62, nuance shape CC30=18, nuance amount CC31=82

### P21 — Boom Bap
*Breaks & electro · 90 BPM · 64 steps · 16th-note scale · flam time 20*

Slow, dusty, flammed snare in the turnaround.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x...x..... x.....x...x..... x.....x...x..... x.....x...x...x.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  OH    ..............x. ..........x...x. ..............x. ..............x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ..........x..... ..........x..... ..........x..... ...x......x.....
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=48
- **Snare Drum (SD)** — tone CC28=58, nuance shape CC30=20, nuance amount CC31=74

### P22 — Trip-Hop
*Breaks & electro · 84 BPM · 64 steps · 16th-note scale · flam time 40*

Half-speed feel, snare dragged late in the bar.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x....... x.......x....... x.............x.
  SD    ....x.........x. ....x.....x...x. ....x.........x. ....x.......xxxr
  CY    x............... x............... x............... x...............
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...r. ..x...x...x...x.
  RS    ........x....... ........x...x... ........x....... ........x.......
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Cymbal (CY)** — variation 0 (CC56=0), tone CC52=28
- **Snare Drum (SD)** — tone CC28=44, nuance shape CC30=24, nuance amount CC31=90

### P23 — Jungle
*Breaks & electro · 165 BPM · 64 steps · 16th-note scale*

Chopped-break placement at jungle tempo; sixteenth hats hold it together.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x.x..... x.......x.x..... x.......x.x..... x.......x.x.....
  SD    ....x......x.... ....x......x.... ....x......x.... ....x......xxxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...........x...
  OH    ..x.......x..... ..x...x...x..... ..x.......x..... ..x.......x.....
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxrxxxxxxxxx xxxxxxxxxxxxxxxr
  RS    ......x.....x... ......x.....x... ......x.....x... ......x.....x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 4 (CC72=4), tone CC68=96
- **Snare Drum (SD)** — tone CC28=84, nuance shape CC30=14, nuance amount CC31=66

### P24 — Drum & Bass
*Breaks & electro · 172 BPM · 64 steps · 16th-note scale*

Two-step: the whole point is the space between kick and snare.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.........x..... x.........x...x. x.........x..... x.........x.....
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  CY    x............... x............... x............... x...............
  OH    ..............x. ..........x...x. ..............x. ..............x.
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...r. ..x...x...x...x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=100
- **Snare Drum (SD)** — tone CC28=90

### P25 — Halftime
*Breaks & electro · 172 BPM · 64 steps · 16th-note scale*

Fast hats, half-time backbone. Huge and slow-feeling.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x............... x.............x. x............... x.............x.
  SD    ........x....... ........x.x..... ........x....... ........x...xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  OH    ......x......... ......x......... ......x......... ......x.........
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.r.x.x.x.x. x.x.x.x.x.x.x.x.
  RS    ..........x...x. ..........x...x. ..........x...x. ..........x...x.
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Snare Drum (SD)** — tone CC28=66, nuance shape CC30=22, nuance amount CC31=88

### P26 — Funk Break
*Breaks & electro · 104 BPM · 64 steps · 16th-note scale*

Sixteenth-note hat shuffle under a busy snare.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x....x..x.... x..x....x..x.... x..x....x..x.... x..x....x..x..x.
  SD    ....x..x..x.x..x ....x.xx..x.x..x ....x..x..x.x..x ....x..x..x.fxxr
  CY    x............... x............... x............... x...............
  OH    ..x............. ..x............. ..x............. ..x.............
  CH    x.xxx.xxx.xxx.xx x.xxx.xxx.xxx.xx x.xxx.xxx.xxx.rx x.xxx.xxx.xxx.xx
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=58
- **Snare Drum (SD)** — tone CC28=68, nuance shape CC30=16, nuance amount CC31=56

### P27 — Amen Feel
*Breaks & electro · 168 BPM · 64 steps · 16th-note scale*

Ghost-snare density approximating the classic break.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x.....x. x.......x....... x.......x.......
  SD    ....x..x.x..x..x ....x..x.x..x..x ....x..x.x..x..x ....x..x.x..xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...r. ..x...x...x...x.
  RS    ...........x.... ........x..x.... ...........x.... ...x.......x....
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Snare Drum (SD)** — tone CC28=78, nuance shape CC30=18, nuance amount CC31=72

### P28 — Broken Beat
*Breaks & electro · 126 BPM · 64 steps · 16th-note scale*

Everything slightly displaced — West London swing.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x....x..x...x..x x....x..x...x..x x....x..x...x..x x....x..x...x..x
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  CH    x.x.xx.x.xx.x.x. x.x.xx.x.xx.x.r. x.x.xx.x.xx.x.r. x.x.xx.x.xx.x.x.
  RS    ......x......... ......x......... ......x......... ......x.........
  CP    ............x... ............x... ............x... ............x...
  ACC*  x....x..x....x.. x....x..x....x.. x....x..x....x.. x....x..x....x..
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=72

### P29 — Footwork
*Breaks & electro · 160 BPM · 64 steps · 16th-note scale*

Triplet-feel kick against a straight rim sixteenth pulse.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..xx
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...r...x. ..x...x...x...x.
  RS    x.x.x.x.x.x.x.x. x.x.x.xxx.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x.
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Hand Clap (CP)** — tone CC84=80
- **Rim Shot (RS)** — tone CC76=96, nuance shape CC78=6, nuance amount CC79=40

### P30 — Ghetto House
*Breaks & electro · 138 BPM · 64 steps · 16th-note scale*

Offbeat claps, relentless hats.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  SD    ..............X. ..............X. ..............X. ............xxxr
  OH    ............x... ............x... ............x... ............x...
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxx
  CP    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..xx..x...x...x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Hand Clap (CP)** — tone CC84=90, nuance shape CC86=8, nuance amount CC87=50

### P31 — Baltimore Club
*Breaks & electro · 132 BPM · 64 steps · 16th-note scale*

The Think-break bounce, stripped to a 606.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x.
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......xxxr
  OH    ..............x. ..............x. ..............x. ..............x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  CP    ....x..x....x..x ....x..x....x..x ....x..x....x..x ....x..x....x..x
  ACC*  x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x.
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Hand Clap (CP)** — tone CC84=84

### P32 — UK Garage
*Breaks & electro · 132 BPM · 64 steps · 16th-note scale · shuffle 42*

Two-step garage with shuffle dialled in on CC18.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x...x..... x.....x...x..... x.....x...x..... x.....x...x.....
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......xxxr
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ......x.....x... ......x.....x... ......x.....x... ......x.....x...
  CP    ............x... ............x... ............x... ............x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=80
- **Snare Drum (SD)** — tone CC28=86


## Page 3 (Green) — patterns P33–P48

### P33 — 606 Rock
*Machine rock & wave · 120 BPM · 64 steps · 16th-note scale*

The original TR-606 Rock 1 idea, developed over four bars.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x....... x.......x....... x.......x.....x.
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......fxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ..............x. ..........x...x. ..............x. ..............x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 0 (CC72=0), tone CC68=64
- **Cymbal (CY)** — variation 0 (CC56=0), tone CC52=60

### P34 — Post-Punk
*Machine rock & wave · 148 BPM · 64 steps · 16th-note scale*

Driving and hard-hit, cymbal marking the half bars.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x...x...x...
  SD    ....X.......X... ....X.......X... ....X.......X... ....X.......xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ..........x..... .......x..x..... ..........x..... ........X.x.x...
  CY    x.......x....... x.......x....... x.......x....... x.......x...x...
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  ACC*  x...X...x...X... x...X...x...X... x...X...x...X... x...X...x...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Snare Drum (SD)** — tone CC28=72, nuance shape CC30=12, nuance amount CC31=64

### P35 — EBM
*Machine rock & wave · 126 BPM · 64 steps · 16th-note scale*

Eighth-note kick engine. Strict, because EBM does not swing.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  CY    x............... x............... x............... x...............
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  RS    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  ACC*  x...X...x...X... x...X...x...X... x...X...x...X... x...X...x...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=28, nuance shape CC22=12, nuance amount CC23=40
- **Snare Drum (SD)** — tone CC28=80

### P36 — Coldwave
*Machine rock & wave · 112 BPM · 64 steps · 16th-note scale*

Sparse, dry, a little sad.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x...x... x.......x...x... x.......x...x... x.......x...x...
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......fxxr
  CY    x............... x............... x............... x...........x...
  CH    ..x...x...x...x. ..x...x...x...r. ..x...r...x...x. ..x...x...x...x.
  RS    x............... x............... x............... x...............
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 4 (CC72=4), tone CC68=40
- **Cymbal (CY)** — variation 0 (CC56=0), tone CC52=34

### P37 — Synth-Pop
*Machine rock & wave · 118 BPM · 64 steps · 16th-note scale*

Clap doubling the snare — the 80s move.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x....... x.......x....... x.......x.......
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ..............x. ..............x. ..............x. ..............x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Hand Clap (CP)** — tone CC84=70, nuance shape CC86=6, nuance amount CC87=48

### P38 — Italo
*Machine rock & wave · 122 BPM · 64 steps · 16th-note scale*

Tom answer phrase in the second half of each bar.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x...x...x...
  LT    ................ ................ ................ .............Xxx
  HT    ..........x.x... ..........x.x... ..........x.x... ........X.x.x...
  CY    x............... x............... x............... x...........x...
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **High Tom (HT)** — tone CC44=92
- **Open Hi-hat (OH)** — variation 2 (CC64=2), tone CC60=78

### P39 — Freestyle
*Machine rock & wave · 116 BPM · 64 steps · 16th-note scale*

Electro-latin freestyle kick with tom answers.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.x....... x.....x.x....... x.....x.x....... x.....x.x.......
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  LT    ............x... .......x....x... ............x... ............xXxx
  HT    ..........x..... .......x..x..... ..........x..... ........X.x.x...
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxrxxxxxxxxx xxxxxxxxxxxxxxxr
  CP    ....x.......x... ....x.......x... ....x.......x... ....xx......f...
  ACC*  x.....x.x.....x. x.....x.x.....x. x.....x.x.....x. x.....x.x.....x.
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=86

### P40 — New Beat
*Machine rock & wave · 108 BPM · 64 steps · 16th-note scale*

Slow, stiff, heavy. Belgian tempo.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  CY    x.......x....... x.......x....... x.......x....... x.......x.......
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  RS    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=22, nuance shape CC22=18, nuance amount CC23=60

### P41 — Dark Pulse
*Machine rock & wave · 96 BPM · 64 steps · 16th-note scale*

Barely a beat. Good bed for drones.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x....... x.......x....... x.......x.......
  CY    x............... x............... x............... x...............
  CH    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  RS    ..x.......x..... ..x.......x..... ..x.......x..... ..x.......x.....
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 5 (CC72=5), tone CC68=22
- **Cymbal (CY)** — variation 0 (CC56=0), tone CC52=18, nuance shape CC54=26, nuance amount CC55=96

### P42 — IDM Glitch
*Machine rock & wave · 140 BPM · 64 steps · 16th-note scale · flam time 8*

Deliberately unstable. Rolls and flams used as glitches.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x.....x..x... x..x.....x..x.x. x..x.....x..x... x..x.....x..x...
  SD    ....x..x....x.x. ....x..x..x.x.x. ....x..x....x.x. ....x..x....fxxr
  LT    ................ ................ ................ .............Xxx
  HT    .........x...... .......x.x...... .........x...... ........Xxx.x...
  CH    x.xx..x.xx.x..xx x.xx..x.xx.x..xx x.xx..x.xx.x..rx x.xx..x.xx.x..xr
  RS    ..x....x..x..... ..x....x..x..... ..x....x..x..... ..x....x..x.....
  ACC*  x..x....x..x.... x..x....x..x.... x..x....x..x.... x..x....x..x....
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=108, nuance shape CC70=30, nuance amount CC71=70
- **Snare Drum (SD)** — tone CC28=94, nuance shape CC30=28, nuance amount CC31=86

### P43 — Braindance
*Machine rock & wave · 130 BPM · 64 steps · 16th-note scale · flam time 16*

Warp-era wonk: displaced kick, chattering hats.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x....x..x...x... x....x..x...x... x....x..x...x... x....x..x...x...
  SD    ....x.....x.x... ....x.....x.x... ....x.....x.x... ....x.....x.xxxr
  LT    ...........x.... ...........x.... ...........x.... ...........x.Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x............... x............... x............... x...........x...
  OH    ......x......... ......x......... ......x......... ..x...x.........
  CH    x.x.xx.xx.x.xx.x x.x.xx.xx.r.xx.x x.x.xx.xx.r.xx.x x.x.xx.xx.x.xx.x
  ACC*  x....x..x....x.. x....x..x....x.. x....x..x....x.. x....x..x....x..
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=94
- **Low Tom (LT)** — tone CC36=36, nuance shape CC38=20, nuance amount CC39=64

### P44 — Cut-Up
*Machine rock & wave · 150 BPM · 64 steps · 16th-note scale · flam time 6*

Fast, chopped, almost arrhythmic — but it loops.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.x.....x.x..... x.x.....x.x...x. x.x.....x.x..... x.x.....x.x.....
  SD    ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..xxxxr
  LT    ................ ................ ................ .............Xxx
  HT    ....x.......x... ....x.......x... ....x.......x... ....x...X.x.x...
  CH    xx.xx.xx.xx.xx.x xx.xx.xx.xx.xx.x xx.xx.xx.xr.xx.x xx.xx.xx.xx.xx.r
  RS    .......x.......x .......x.......x .......x.......x .......x.......x
  ACC*  x.x.....x.x..... x.x.....x.x..... x.x.....x.x..... x.x.....x.x.....
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Snare Drum (SD)** — tone CC28=100, nuance shape CC30=31, nuance amount CC31=90

### P45 — Motorik
*Machine rock & wave · 142 BPM · 64 steps · 16th-note scale*

Neu! pulse. Strict so it hypnotises.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x.x.x...x.x. x...x.x.x...x.x. x...x.x.x...x.x. x...x.x.x...x.x.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  CY    x............... x............... x............... x...............
  OH    ..............x. ..............x. ..............x. ..............x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=70

### P46 — Shoegaze Drive
*Machine rock & wave · 130 BPM · 64 steps · 16th-note scale*

Washy cymbal every half bar, snare pushing sixteenths.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x.x. x...x...x...x... x...x...x...x.x.
  SD    ....x..x....x..x ....x..x....x..x ....x..x....x..x ....x..x....xxxr
  LT    ................ ................ ................ .............Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x.......x....... x.......x....... x.......x....... x.......x.......
  OH    ..x............. ..x...........x. ..x............. ..x.............
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Cymbal (CY)** — variation 2 (CC56=2), tone CC52=46, nuance shape CC54=22, nuance amount CC55=84

### P47 — Noise Industrial
*Machine rock & wave · 100 BPM · 64 steps · 16th-note scale*

All extremes on the nuance settings. Abrasive by design.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    X..x..X...x.X... X..x..X...x.X... X..x..X...x.X... X..x..X...x.X.x.
  SD    ....X.......X... ....X.......X... ....X.......X... ....X.......X...
  LT    ..x.......x..... ..x....x..x..... ..x.......x..... ..x.......x..Xxx
  HT    ................ ................ ................ ........X.x.x...
  CY    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  ACC*  X...X...X...X... X...X...X...X... X...X...X...X... X...X...X...X...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=14, nuance shape CC22=31, nuance amount CC23=118
- **Cymbal (CY)** — variation 3 (CC56=3), tone CC52=14
- **Snare Drum (SD)** — tone CC28=24, nuance shape CC30=30, nuance amount CC31=110

### P48 — Power Pulse
*Machine rock & wave · 88 BPM · 64 steps · 16th-note scale*

Two enormous hits per bar. Everything else is decoration.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    X.......X....... X.......X....... X.......X....... X.......X.......
  LT    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  CY    X.......X....... X.......X....... X.......X....... X.......X.......
  RS    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  ACC*  X.......X....... X.......X....... X.......X....... X.......X.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=10, nuance shape CC22=28, nuance amount CC23=120
- **Cymbal (CY)** — variation 3 (CC56=3), tone CC52=10


## Page 4 (Blue) — patterns P49–P64

### P49 — 16th Shuffle
*Grooves & polyrhythm · 108 BPM · 64 steps · 16th-note scale · shuffle 64*

Shuffle amount pushed past half — swung sixteenths.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.x.....x. x.....x.x.....x. x.....x.x.....x. x.....x.......xx
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......xxxr
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x...x...x.....
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxr
  RS    ......x.....x... ......x.....x... ......x.....x... ......x.....x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=62

### P50 — Swung Boom Bap
*Grooves & polyrhythm · 88 BPM · 64 steps · 16th-note scale · shuffle 76 · flam time 24*

Heavy swing plus flams — the drunkest pattern in the bank.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x...x..... x.....x...x...x. x.....x...x..... x.....x...x...x.
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......xxxr
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ..........x..... .....x....x..... ..........x..... ..x.......x.....
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 4 (CC72=4), tone CC68=44
- **Snare Drum (SD)** — tone CC28=54, nuance shape CC30=22, nuance amount CC31=78

### P51 — Dembow
*Grooves & polyrhythm · 96 BPM · 64 steps · 16th-note scale*

The boom-ch-boom-chick, with rim on the offbeats.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.x.....x. x.....x.x.....x. x.....x.x.....x. x.....x.x.....x.
  SD    ...x..x....x..x. ...x..x....x..x. ...x..x....x..x. ...x..x....xxxxr
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    ..x...x...x...x. ..x.x.x...x...x. ..x...x...x...x. ..x..xx...x...x.
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......f...
  ACC*  x.....x.x.....x. x.....x.x.....x. x.....x.x.....x. x.....x.x.....x.
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Rim Shot (RS)** — tone CC76=84
- **Snare Drum (SD)** — tone CC28=74

### P52 — Reggaeton
*Grooves & polyrhythm · 94 BPM · 64 steps · 16th-note scale*

Clap doubling the dembow snare for weight.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x.....x. x.......x....... x.......x.......
  SD    ...x..x....x..x. ...x..x...xx..x. ...x..x....x..x. ...x..x....xxxxr
  OH    ..............x. ..............x. ..............x. ..........x...x.
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...r. ..x...x...x...x.
  CP    ...x..x....x..x. ..xx..x....x..x. ...x..x....x..x. ...x..x....x..x.
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Hand Clap (CP)** — tone CC84=78, nuance shape CC86=8, nuance amount CC87=46

### P53 — Baile Funk
*Grooves & polyrhythm · 130 BPM · 64 steps · 16th-note scale*

Tamborzão-flavoured tom answer under a bouncing kick.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x....x..x.
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  LT    ..x.x...x.x..... ..x.x...x.x..... ..x.x...x.x..... ..x.x...x.x..Xxx
  HT    ................ ................ ................ ........X.x.x...
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  CP    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x.
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Low Tom (LT)** — tone CC36=40, nuance shape CC38=14, nuance amount CC39=58

### P54 — Afro House
*Grooves & polyrhythm · 122 BPM · 64 steps · 16th-note scale*

Layered percussion in threes over a straight four.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  LT    ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x.Xxx
  HT    ....x..x....x..x ....x..x....x..x ....x..x....x..x ....x..xX.x.x..x
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x...x...x.....
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x
  ACC*  x.....x.....x... x.....x.....x... x.....x.....x... x.....x.....x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **High Tom (HT)** — tone CC44=86
- **Low Tom (LT)** — tone CC36=42
- **Rim Shot (RS)** — tone CC76=88

### P55 — 6/8 Feel
*Grooves & polyrhythm · 116 BPM · 64 steps · 16th-note scale*

Twelve-feel bell pattern mapped onto the 16-step grid.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.....x... x.....x.....x... x.....x.....x... x.....x.....x.x.
  LT    ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x.Xxx
  HT    ...x.....x.....x ...x.....x.....x ...x.....x.....x ...x....Xxx.x..x
  CH    x..x..x..x..x..x x..x..x..x..x..x x..x..r..x..x..x x..x..x..x..x..x
  RS    ....x.....x..... ...xx.....x..... ....x.....x..... ....x.....f.....
  ACC*  x.....x.....x... x.....x.....x... x.....x.....x... x.....x.....x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=66

### P56 — Cumbia Machine
*Grooves & polyrhythm · 100 BPM · 64 steps · 16th-note scale*

Cumbia's limping guiro figure translated to rim and tom.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  SD    ....x.......x... ....x.....x.x... ....x.......x... ....x.......x...
  LT    ..x.....x.....x. ..x.....x.....x. ..x.....x.....x. ..x.....x....Xxx
  HT    ................ ................ ................ ........X.x.x...
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.r. x.x.x.x.x.x.x.x.
  RS    x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Low Tom (LT)** — tone CC36=38
- **Rim Shot (RS)** — tone CC76=92

### P57 — Samba Electro
*Grooves & polyrhythm · 132 BPM · 64 steps · 16th-note scale*

Surdo-ish kick with a busy caixa-style snare.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x.
  SD    ..x.x.x...x.x.x. ..x.x.x...x.x.x. ..x.x.x...x.x.x. ..x.x.x...x.fxxr
  LT    ....x.......x... ....x.......x... ....x.......x... ....x.......xXxx
  HT    ................ ................ ................ ........X.x.x...
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxrxxxxx xxxxxxxxxxxxxxxx
  RS    x.x.x.x.x.x.x.x. x.x.x.x.x.xxx.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x.
  ACC*  x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x. x..x..x.x..x..x.
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 3 (CC72=3), tone CC68=90
- **Snare Drum (SD)** — tone CC28=82

### P58 — Bossa Electro
*Grooves & polyrhythm · 128 BPM · 64 steps · 16th-note scale*

Clave-like rim over a soft two-feel. Strict to keep it polite.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.....x.x.....x. x.....x.x.....x. x.....x.x.....x. x.....x.x.....x.
  SD    ............x... ............x... ............x... ............x...
  OH    ..............x. ..............x. ..............x. ..............x.
  CH    x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x. x.x.x.x.x.x.x.x.
  RS    ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x. ..x..x..x..x..x.
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Rim Shot (RS)** — tone CC76=76, nuance shape CC78=10, nuance amount CC79=40

### P59 — Disco
*Grooves & polyrhythm · 120 BPM · 64 steps · 16th-note scale*

Open hat on every offbeat, clap on the backbeat, tom pickups.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......fxxr
  LT    ................ ................ ................ .............Xxx
  HT    ..........x.x... ..........x.x... ..........x.x... ........X.x.x...
  CY    x............... x............... x............... x...............
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxrx xxxxxxxxxxxxxxxx
  CP    ....x.......x... ....x.......x..x ....x.......x... ....x.......x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 0 (CC72=0), tone CC68=68
- **Open Hi-hat (OH)** — variation 1 (CC64=1), tone CC60=74

### P60 — Boogie
*Grooves & polyrhythm · 112 BPM · 64 steps · 16th-note scale · shuffle 36*

Slinky early-80s kick with a touch of shuffle.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x.....x.x... x...x.....x.x.x. x...x.....x.x... x...x.....x.x...
  SD    ....x.......x... ....x.......x... ....x.......x... ....x.......xxxr
  OH    ..x.......x..... ..x.......x..... ..x.......x..... ..x...x...x.....
  CH    xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxrxxxxxxxxx xxxxxxxxxxxxxxxr
  RS    ......x.....x... ......x.....x... ......x.....x... ......x.....f...
  CP    ............x... ............x.x. ............x... ............xx..
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 2 (CC72=2), tone CC68=72

### P61 — Nu-Disco
*Grooves & polyrhythm · 118 BPM · 64 steps · 16th-note scale*

Disco frame, softer tone settings, stuttered hats.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x.x.
  CY    x............... x............... x............... x...............
  OH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  CH    x.xxx.xxx.xxx.xx x.xxx.xxx.xxx.xx x.xxx.rxx.xxx.xx x.xxx.xxx.xxx.xr
  RS    ..........x..... ..........x..... ..........x..... ..........x.x...
  CP    ....x.......x... ..x.x.......x... ....x.......x... ....x.......x...
  ACC*  x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 1 (CC72=1), tone CC68=60
- **Hand Clap (CP)** — tone CC84=64, nuance shape CC86=4, nuance amount CC87=36

### P62 — Ambient Sparse
*Grooves & polyrhythm · 76 BPM · 64 steps · 16th-note scale*

Four events per bar. Long cymbal decay does the work.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x............... x............... x............... x...............
  CY    x............... x............... x............... x...............
  CH    ............x... ............x... ............x... ............x...
  RS    ........x....... ........x....... ........x....... ........x.......
  ACC*  x............... x............... x............... x...............
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Bass Drum (BD)** — tone CC20=34, nuance shape CC22=20, nuance amount CC23=44
- **Cymbal (CY)** — variation 0 (CC56=0), tone CC52=12, nuance shape CC54=24, nuance amount CC55=100

### P63 — Polyrhythm 5
*Grooves & polyrhythm · 124 BPM · 64 steps · 16th-note scale*

Rim in fives, tom in sevens, kick in fours. Phases across the 64 steps.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x...x...x...x... x...x...x...x... x...x...x...x... x...x...x...x...
  LT    x......x......x. x......x......x. x......x......x. x......x......x.
  CY    x............... x............... x............... x...............
  CH    ..x...x...x...x. ..x...x...x...x. ..x...x...x...x. ..x...x...x...x.
  RS    x....x....x....x x....x....x....x x....x....x....x x....x....x....x
  ACC*  x....x....x....x x....x....x....x x....x....x....x x....x....x....x
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Low Tom (LT)** — tone CC36=40
- **Rim Shot (RS)** — tone CC76=86

### P64 — Drone Pulse
*Grooves & polyrhythm · 70 BPM · 64 steps · 16th-note scale*

Slowest pattern in the bank. Meant to sit under a long drone.

```
        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)
  BD    x.......x....... x.......x....... x.......x....... x.......x.......
  LT    ..........x..... ..........x..... ..........x..... ..........x.....
  CY    x............... x............... x............... x...............
  CH    x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x x..x..x..x..x..x
  RS    ....x.......x... ....x.......x... ....x.......x... ....x.......x...
  ACC*  x.......x....... x.......x....... x.......x....... x.......x.......
```
`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.

Voice settings:
- **Closed Hi-hat (CH)** — variation 5 (CC72=5), tone CC68=16
- **Cymbal (CY)** — variation 1 (CC56=1), tone CC52=8, nuance shape CC54=28, nuance amount CC55=110

