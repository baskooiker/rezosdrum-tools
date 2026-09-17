"""64 pattern styles for the Cyclone Analogic TT-606 Drum Drone.

Voices: BD SD LT HT CY OH CH RS CP, plus the Global Accent lane (GA).
Motifs are 16 steps and are developed into 64-step patterns by develop.py.
"""

from engine import GLOBAL_ACCENT as GA
from export import Style

# Common lanes (16 steps each)
FOUR = "x...x...x...x..."
TWO = "x.......x......."
OFF8 = "..x...x...x...x."
E8 = "x.x.x.x.x.x.x.x."
E16 = "xxxxxxxxxxxxxxxx"
BACK = "....x.......x..."
ONE = "x..............."
TRES = "x..x..x.x..x..x."   # 3-3-2 tresillo at sixteenth resolution


def S(*a, **k):
    return Style(*a, **k)


TT606_STYLES = [
    # ---------------- Page 1: four-to-the-floor ----------------
    S("House", 124, {
        "BD": FOUR, "CP": BACK, "OH": OFF8, "CH": "x.x.x.x.x.x.x.x.",
        "RS": "..............x.", GA: "x...............",
    }, family="Four-to-the-floor", fills=["snare"],
       kit={"CH": {"sel": 1, "tone": 64}, "OH": {"sel": 2, "tone": 70},
            "CP": {"tone": 60, "shape": 6, "amount": 40}},
       flam_time=32,
       notes="Textbook 4/4 house: offbeat open hat, clap on the backbeat, rim ghost lifting into the next bar."),

    S("Deep House", 120, {
        "BD": FOUR, "CP": "....x...........", "OH": OFF8,
        "CH": "x..xx..xx..xx..x", "RS": "......x.....x...",
        GA: "x.......x.......",
    }, family="Four-to-the-floor",
       kit={"CH": {"sel": 3, "tone": 44, "shape": 12, "amount": 52},
            "OH": {"sel": 4, "tone": 52}, "BD": {"tone": 40, "shape": 8, "amount": 30}},
       notes="Softer hats, one clap per bar, kick tuned long and round."),

    S("Tech House", 126, {
        "BD": "x...x...x...x..x", "CP": BACK, "OH": OFF8,
        "CH": "xxxxxxxxxxxxxxxx", "RS": "..x.......x.....",
        GA: "x.......",
    }, family="Four-to-the-floor", fills=["snare"],
       kit={"CH": {"sel": 2, "tone": 78}, "OH": {"sel": 1, "tone": 66}},
       notes="Sixteenth hats with a pushed kick on the last step."),

    S("Techno", 132, {
        "BD": FOUR, "CH": OFF8, "OH": "............x...",
        "CY": ONE, "RS": "..x...x...x...x.", GA: "x...x...x...x...",
    }, family="Four-to-the-floor", strict=True,
       kit={"CH": {"sel": 0, "tone": 90, "shape": 2, "amount": 20},
            "CY": {"sel": 1, "tone": 30}},
       notes="Deliberately strict — no bar-to-bar variation. Let the Tone knobs do the moving."),

    S("Hard Techno", 145, {
        "BD": "X...X...X...X...", "CH": E16, "OH": "..x...x...x...x.",
        "CY": "x.......x.......", "SD": "..............X.",
        GA: "X...X...X...X...",
    }, family="Four-to-the-floor", fills=["snare", "tom"],
       kit={"BD": {"tone": 20, "shape": 30, "amount": 96},
            "CH": {"sel": 5, "tone": 110}, "CY": {"sel": 3, "tone": 100}},
       notes="Everything accented, kick tuned short and clicky, snare slam into the turnaround."),

    S("Minimal", 128, {
        "BD": FOUR, "CH": "..x.....x.......", "RS": "......x.........",
        "CP": "............x...", GA: "x...............",
    }, family="Four-to-the-floor", strict=True,
       kit={"CH": {"sel": 1, "tone": 50, "shape": 20, "amount": 24},
            "RS": {"tone": 70}},
       notes="Almost nothing. Space is the instrument."),

    S("Dub Techno", 122, {
        "BD": FOUR, "CH": "..x...x...x...x.", "OH": "..............x.",
        "RS": "........x.......", "CP": "....x...........",
        GA: "x.......",
    }, family="Four-to-the-floor",
       kit={"CH": {"sel": 4, "tone": 34, "shape": 16, "amount": 64},
            "OH": {"sel": 5, "tone": 40, "shape": 22, "amount": 80}},
       notes="Long, soft open hat as the only bright thing in the pattern."),

    S("Tribal Techno", 130, {
        "BD": FOUR, "LT": "..x..x..x..x..x.", "HT": "....x.......x...",
        "CH": E8, "OH": "......x.........", "RS": "x...x...x...x...",
        GA: "x.....x.....x...",
    }, family="Four-to-the-floor", fills=["tom"],
       kit={"LT": {"tone": 44, "shape": 10, "amount": 48},
            "HT": {"tone": 80, "shape": 10, "amount": 48}},
       notes="Toms carry the groove; the three-against-four rim keeps it rolling."),

    S("Detroit Techno", 134, {
        "BD": FOUR, "CP": BACK, "OH": OFF8, "CH": "x.xxx.xxx.xxx.xx",
        "CY": ONE, "HT": "..........x.....", GA: "x...x...",
    }, family="Four-to-the-floor", fills=["snare"],
       kit={"CH": {"sel": 2, "tone": 84}, "CY": {"sel": 2, "tone": 62},
            "CP": {"tone": 72, "shape": 4, "amount": 56}},
       notes="Stuttering hat figure, cymbal wash on the downbeat."),

    S("Acid Techno", 138, {
        "BD": FOUR, "SD": BACK, "CH": E16, "OH": "..x...x...x...x.",
        "CY": "x.......", "RS": ".....x.....x....",
        GA: "x...X...x...X...",
    }, family="Four-to-the-floor", fills=["snare", "tom"],
       kit={"CH": {"sel": 3, "tone": 96}, "SD": {"tone": 88, "shape": 14, "amount": 70}},
       notes="The classic 606-under-a-303 pattern. Global accent alternates strong/stronger."),

    S("Hardgroove", 136, {
        "BD": FOUR, "CH": "xxxxxxxxxxxxxxxx", "OH": "..x.......x.....",
        "LT": "......x.....x...", "HT": "..........x.....",
        "RS": "x..x..x..x..x..x", "CP": BACK, GA: "x..x..x..x..x..x",
    }, family="Four-to-the-floor", fills=["tom"],
       kit={"CH": {"sel": 4, "tone": 100}, "RS": {"tone": 90, "shape": 8, "amount": 60}},
       notes="Dense percussive layers with an accent lane in threes against the four."),

    S("Schranz", 150, {
        "BD": "X..xX..xX..xX..x", "CH": E16, "CY": "x...x...x...x...",
        "SD": "..............X.", "OH": "......x.........",
        GA: "X...X...X...X...",
    }, family="Four-to-the-floor", fills=["snare"],
       kit={"BD": {"tone": 12, "shape": 31, "amount": 110}, "CY": {"sel": 3, "tone": 118}},
       notes="Distorted-kick territory: double kick figure, cymbal on every beat."),

    S("Trance", 138, {
        "BD": FOUR, "CP": BACK, "OH": OFF8, "CH": E16,
        "CY": ONE, "RS": "...........x....", GA: "x...x...x...x...",
    }, family="Four-to-the-floor", fills=["snare", "tom"],
       kit={"OH": {"sel": 3, "tone": 90}, "CY": {"sel": 1, "tone": 74}},
       notes="Big offbeat hat, rolling sixteenths, fills every fourth bar."),

    S("Psy", 145, {
        "BD": FOUR, "CH": "..x...x...x...x.", "OH": "......x.......x.",
        "LT": ".x.x.x.x.x.x.x.x", "CY": "x.......",
        GA: "x...x...x...x...",
    }, family="Four-to-the-floor", strict=True,
       kit={"LT": {"tone": 30, "shape": 6, "amount": 20},
            "CH": {"sel": 5, "tone": 104}},
       notes="Rolling triplet-feel tom underneath a rigid kick. Strict on purpose."),

    S("Hardcore", 165, {
        "BD": "X...X...X...X...", "SD": BACK, "CY": E8,
        "CH": E16, "HT": "..........x.x...", "OH": "..............x.",
        GA: "X...X...X...X...",
    }, family="Four-to-the-floor", fills=["snare", "tom"],
       kit={"BD": {"tone": 8, "shape": 31, "amount": 120}, "SD": {"tone": 100}},
       notes="Fast and blunt. Cymbal eighths give it the rave sheen."),

    S("Industrial Techno", 128, {
        "BD": "x...x...x..x.x..", "SD": "........X.......",
        "CH": "x.x.x.x.x.x.x.x.", "CY": "x...............",
        "LT": "..x.........x...", "RS": ".....x.....x....",
        GA: "x.......X.......",
    }, family="Four-to-the-floor", fills=["tom"],
       kit={"BD": {"tone": 24, "shape": 26, "amount": 88},
            "SD": {"tone": 30, "shape": 28, "amount": 100},
            "CY": {"sel": 3, "tone": 20}},
       notes="Snare on the half-bar, kick limping slightly off the grid."),

    # ---------------- Page 2: breaks & electro ----------------
    S("Electro", 128, {
        "BD": "x.....x.x.....x.", "SD": BACK, "CH": E8,
        "OH": "..x.......x.....", "CP": "....x...........",
        "CY": ONE, GA: "x...x...x...x...",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"CH": {"sel": 2, "tone": 88}, "SD": {"tone": 76, "shape": 10, "amount": 44}},
       notes="Syncopated electro kick, straight backbeat, eighth hats."),

    S("Miami Bass", 132, {
        "BD": "x..x..x...x..x..", "SD": BACK, "CH": E16,
        "CP": "....x.......x...", "OH": "..............x.",
        GA: "x.......x.......",
    }, family="Breaks & electro", fills=["snare"],
       kit={"BD": {"tone": 18, "shape": 4, "amount": 24}, "CH": {"sel": 1, "tone": 92}},
       notes="808-style bass pattern with clap doubling the snare."),

    S("Breakbeat", 136, {
        "BD": "x.....x.....x...", "SD": "....x..x..x.x...",
        "CH": "x.x.x.x.x.x.x.x.", "OH": "......x.........",
        "CY": ONE, "RS": "..........x.....",
        GA: "x...x...",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"SD": {"tone": 70, "shape": 12, "amount": 60}},
       notes="Loose funk break skeleton, snare doing the talking."),

    S("Big Beat", 118, {
        "BD": "x...x..x..x.x...", "SD": "....X.......X...",
        "CH": E8, "OH": "..x.......x.....", "CY": ONE,
        "HT": "...........x....", GA: "x...X...x...X...",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"SD": {"tone": 62, "shape": 18, "amount": 82}, "CY": {"sel": 2, "tone": 54}},
       notes="Heavy, slightly slow, snare hit hard."),

    S("Boom Bap", 90, {
        "BD": "x.....x...x.....", "SD": "....x.......x...",
        "CH": "x.x.x.x.x.x.x.x.", "OH": "..............x.",
        "RS": "..........x.....", GA: "x...x...",
    }, family="Breaks & electro", fills=["snare"], flam_time=20,
       kit={"SD": {"tone": 58, "shape": 20, "amount": 74}, "CH": {"sel": 3, "tone": 48}},
       notes="Slow, dusty, flammed snare in the turnaround."),

    S("Trip-Hop", 84, {
        "BD": "x.......x.......", "SD": "....x.........x.",
        "CH": "..x...x...x...x.", "RS": "........x.......",
        "CY": ONE, GA: "x...x...",
    }, family="Breaks & electro", fills=["snare"], flam_time=40,
       kit={"SD": {"tone": 44, "shape": 24, "amount": 90}, "CY": {"sel": 0, "tone": 28}},
       notes="Half-speed feel, snare dragged late in the bar."),

    S("Jungle", 165, {
        "BD": "x.......x.x.....", "SD": "....x......x....",
        "CH": E16, "OH": "..x.......x.....", "CY": ONE,
        "RS": "......x.....x...", GA: "x...x...",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"SD": {"tone": 84, "shape": 14, "amount": 66}, "CH": {"sel": 4, "tone": 96}},
       notes="Chopped-break placement at jungle tempo; sixteenth hats hold it together."),

    S("Drum & Bass", 172, {
        "BD": "x.........x.....", "SD": "....x.......x...",
        "CH": "..x...x...x...x.", "OH": "..............x.",
        "CY": ONE, GA: "x...x...x...x...",
    }, family="Breaks & electro", fills=["snare"],
       kit={"SD": {"tone": 90}, "CH": {"sel": 2, "tone": 100}},
       notes="Two-step: the whole point is the space between kick and snare."),

    S("Halftime", 172, {
        "BD": "x...............", "SD": "........x.......",
        "CH": "x.x.x.x.x.x.x.x.", "OH": "......x.........",
        "RS": "..........x...x.", GA: "x.......x.......",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"SD": {"tone": 66, "shape": 22, "amount": 88}},
       notes="Fast hats, half-time backbone. Huge and slow-feeling."),

    S("Funk Break", 104, {
        "BD": "x..x....x..x....", "SD": "....x..x..x.x..x",
        "CH": "x.xxx.xxx.xxx.xx", "OH": "..x.............",
        "CY": ONE, GA: "x...x...",
    }, family="Breaks & electro", fills=["snare"],
       kit={"CH": {"sel": 1, "tone": 58}, "SD": {"tone": 68, "shape": 16, "amount": 56}},
       notes="Sixteenth-note hat shuffle under a busy snare."),

    S("Amen Feel", 168, {
        "BD": "x.......x.......", "SD": "....x..x.x..x..x",
        "CH": "..x...x...x...x.", "CY": ONE,
        "RS": "...........x....", GA: "x...x...",
    }, family="Breaks & electro", fills=["snare", "tom"],
       kit={"SD": {"tone": 78, "shape": 18, "amount": 72}},
       notes="Ghost-snare density approximating the classic break."),

    S("Broken Beat", 126, {
        "BD": "x....x..x...x..x", "SD": "....x.......x...",
        "CH": "x.x.xx.x.xx.x.x.", "OH": "..x.......x.....",
        "RS": "......x.........", "CP": "............x...",
        GA: "x....x..",
    }, family="Breaks & electro", fills=["snare"],
       kit={"CH": {"sel": 3, "tone": 72}},
       notes="Everything slightly displaced — West London swing."),

    S("Footwork", 160, {
        "BD": "x..x..x.x..x..x.", "CP": "....x.......x...",
        "CH": "..x...x...x...x.", "RS": "x.x.x.x.x.x.x.x.",
        GA: "x.......x.......",
    }, family="Breaks & electro", fills=["snare"],
       kit={"RS": {"tone": 96, "shape": 6, "amount": 40}, "CP": {"tone": 80}},
       notes="Triplet-feel kick against a straight rim sixteenth pulse."),

    S("Ghetto House", 138, {
        "BD": FOUR, "CP": "..x...x...x...x.", "CH": E16,
        "SD": "..............X.", "OH": "............x...",
        GA: "x...x...x...x...",
    }, family="Breaks & electro", fills=["snare"],
       kit={"CP": {"tone": 90, "shape": 8, "amount": 50}},
       notes="Offbeat claps, relentless hats."),

    S("Baltimore Club", 132, {
        "BD": "x..x..x.x..x..x.", "SD": "....x.......x...",
        "CH": E8, "CP": "....x..x....x..x", "OH": "..............x.",
        GA: "x..x..x.",
    }, family="Breaks & electro", fills=["snare"],
       kit={"CP": {"tone": 84}},
       notes="The Think-break bounce, stripped to a 606."),

    S("UK Garage", 132, {
        "BD": "x.....x...x.....", "SD": "....x.......x...",
        "CH": "x.x.x.x.x.x.x.x.", "OH": "..x.......x.....",
        "RS": "......x.....x...", "CP": "............x...",
        GA: "x...x...",
    }, family="Breaks & electro", fills=["snare"], shuffle=42,
       kit={"CH": {"sel": 2, "tone": 80}, "SD": {"tone": 86}},
       notes="Two-step garage with shuffle dialled in on CC18."),

    # ---------------- Page 3: 606 heritage & machine rock ----------------
    S("606 Rock", 120, {
        "BD": "x.......x.......", "SD": BACK, "CH": E8,
        "CY": ONE, "OH": "..............x.",
        GA: "x...x...x...x...",
    }, family="Machine rock & wave", fills=["snare", "tom"],
       kit={"CH": {"sel": 0, "tone": 64}, "CY": {"sel": 0, "tone": 60}},
       notes="The original TR-606 Rock 1 idea, developed over four bars."),

    S("Post-Punk", 148, {
        "BD": "x...x...x...x...", "SD": "....X.......X...",
        "CH": E8, "CY": "x.......x.......",
        "HT": "..........x.....", GA: "x...X...x...X...",
    }, family="Machine rock & wave", fills=["snare", "tom"],
       kit={"SD": {"tone": 72, "shape": 12, "amount": 64}},
       notes="Driving and hard-hit, cymbal marking the half bars."),

    S("EBM", 126, {
        "BD": "x.x.x.x.x.x.x.x.", "SD": BACK, "CH": "..x...x...x...x.",
        "CY": ONE, "RS": "x...x...x...x...",
        GA: "x...X...x...X...",
    }, family="Machine rock & wave", strict=True,
       kit={"BD": {"tone": 28, "shape": 12, "amount": 40}, "SD": {"tone": 80}},
       notes="Eighth-note kick engine. Strict, because EBM does not swing."),

    S("Coldwave", 112, {
        "BD": "x.......x...x...", "SD": BACK, "CH": "..x...x...x...x.",
        "RS": "x...............", "CY": ONE,
        GA: "x...x...",
    }, family="Machine rock & wave", fills=["snare"],
       kit={"CH": {"sel": 4, "tone": 40}, "CY": {"sel": 0, "tone": 34}},
       notes="Sparse, dry, a little sad."),

    S("Synth-Pop", 118, {
        "BD": "x.......x.......", "SD": BACK, "CP": BACK,
        "CH": E8, "OH": "..............x.", "CY": ONE,
        GA: "x...x...x...x...",
    }, family="Machine rock & wave", fills=["snare", "tom"],
       kit={"CP": {"tone": 70, "shape": 6, "amount": 48}},
       notes="Clap doubling the snare — the 80s move."),

    S("Italo", 122, {
        "BD": FOUR, "CP": BACK, "OH": OFF8, "CH": E16,
        "HT": "..........x.x...", "CY": ONE,
        GA: "x...x...x...x...",
    }, family="Machine rock & wave", fills=["tom"],
       kit={"OH": {"sel": 2, "tone": 78}, "HT": {"tone": 92}},
       notes="Tom answer phrase in the second half of each bar."),

    S("Freestyle", 116, {
        "BD": "x.....x.x.......", "SD": BACK, "CP": "....x.......x...",
        "CH": E16, "HT": "..........x.....", "LT": "............x...",
        GA: "x.....x.",
    }, family="Machine rock & wave", fills=["tom"],
       kit={"CH": {"sel": 1, "tone": 86}},
       notes="Electro-latin freestyle kick with tom answers."),

    S("New Beat", 108, {
        "BD": FOUR, "SD": BACK, "CH": OFF8, "CY": "x.......x.......",
        "RS": "..x...x...x...x.", GA: "x...x...x...x...",
    }, family="Machine rock & wave", strict=True,
       kit={"BD": {"tone": 22, "shape": 18, "amount": 60}},
       notes="Slow, stiff, heavy. Belgian tempo."),

    S("IDM Glitch", 140, {
        "BD": "x..x.....x..x...", "SD": "....x..x....x.x.",
        "CH": "x.xx..x.xx.x..xx", "RS": "..x....x..x.....",
        "HT": ".........x......", GA: "x..x....",
    }, family="Machine rock & wave", fills=["snare", "tom"], flam_time=8,
       kit={"CH": {"sel": 3, "tone": 108, "shape": 30, "amount": 70},
            "SD": {"tone": 94, "shape": 28, "amount": 86}},
       notes="Deliberately unstable. Rolls and flams used as glitches."),

    S("Braindance", 130, {
        "BD": "x....x..x...x...", "SD": "....x.....x.x...",
        "CH": "x.x.xx.xx.x.xx.x", "OH": "......x.........",
        "LT": "...........x....", "CY": ONE, GA: "x....x..",
    }, family="Machine rock & wave", fills=["snare", "tom"], flam_time=16,
       kit={"CH": {"sel": 2, "tone": 94}, "LT": {"tone": 36, "shape": 20, "amount": 64}},
       notes="Warp-era wonk: displaced kick, chattering hats."),

    S("Cut-Up", 150, {
        "BD": "x.x.....x.x.....", "SD": "..x..x..x..x..x.",
        "CH": "xx.xx.xx.xx.xx.x", "HT": "....x.......x...",
        "RS": ".......x.......x", GA: "x.x.....",
    }, family="Machine rock & wave", fills=["snare", "tom"], flam_time=6,
       kit={"SD": {"tone": 100, "shape": 31, "amount": 90}},
       notes="Fast, chopped, almost arrhythmic — but it loops."),

    S("Motorik", 142, {
        "BD": "x...x.x.x...x.x.", "SD": "....x.......x...",
        "CH": E16, "OH": "..............x.", "CY": ONE,
        GA: "x...x...x...x...",
    }, family="Machine rock & wave", strict=True,
       kit={"CH": {"sel": 1, "tone": 70}},
       notes="Neu! pulse. Strict so it hypnotises."),

    S("Shoegaze Drive", 130, {
        "BD": "x...x...x...x...", "SD": "....x..x....x..x",
        "CH": E8, "CY": "x.......x.......", "OH": "..x.............",
        GA: "x...x...",
    }, family="Machine rock & wave", fills=["snare", "tom"],
       kit={"CY": {"sel": 2, "tone": 46, "shape": 22, "amount": 84}},
       notes="Washy cymbal every half bar, snare pushing sixteenths."),

    S("Noise Industrial", 100, {
        "BD": "X..x..X...x.X...", "SD": "....X.......X...",
        "CY": "x...x...x...x...", "LT": "..x.......x.....",
        "CH": "x.x.x.x.x.x.x.x.", GA: "X...X...X...X...",
    }, family="Machine rock & wave", fills=["tom"],
       kit={"BD": {"tone": 14, "shape": 31, "amount": 118},
            "SD": {"tone": 24, "shape": 30, "amount": 110},
            "CY": {"sel": 3, "tone": 14}},
       notes="All extremes on the nuance settings. Abrasive by design."),

    S("16th Shuffle", 108, {
        "BD": "x.....x.x.....x.", "SD": BACK, "CH": E16,
        "OH": "..x.......x.....", "RS": "......x.....x...",
        GA: "x...x...",
    }, family="Grooves & polyrhythm", fills=["snare"], shuffle=64,
       kit={"CH": {"sel": 1, "tone": 62}},
       notes="Shuffle amount pushed past half — swung sixteenths."),

    S("Swung Boom Bap", 88, {
        "BD": "x.....x...x.....", "SD": "....x.......x...",
        "CH": "x.x.x.x.x.x.x.x.", "RS": "..........x.....",
        GA: "x...x...",
    }, family="Grooves & polyrhythm", fills=["snare"], shuffle=76, flam_time=24,
       kit={"SD": {"tone": 54, "shape": 22, "amount": 78}, "CH": {"sel": 4, "tone": 44}},
       notes="Heavy swing plus flams — the drunkest pattern in the bank."),

    S("Dembow", 96, {
        "BD": "x.....x.x.....x.", "SD": "...x..x....x..x.",
        "CH": E8, "RS": "..x...x...x...x.", "CP": "....x.......x...",
        GA: "x.....x.",
    }, family="Grooves & polyrhythm", fills=["snare"],
       kit={"SD": {"tone": 74}, "RS": {"tone": 84}},
       notes="The boom-ch-boom-chick, with rim on the offbeats."),

    S("Reggaeton", 94, {
        "BD": "x.......x.......", "SD": "...x..x....x..x.",
        "CH": OFF8, "CP": "...x..x....x..x.", "OH": "..............x.",
        GA: "x.......x.......",
    }, family="Grooves & polyrhythm", fills=["snare"],
       kit={"CP": {"tone": 78, "shape": 8, "amount": 46}},
       notes="Clap doubling the dembow snare for weight."),

    S("Baile Funk", 130, {
        "BD": "x..x..x.x..x..x.", "SD": "....x.......x...",
        "LT": "..x.x...x.x.....", "CH": E8, "CP": "....x.......x...",
        GA: "x..x..x.",
    }, family="Grooves & polyrhythm", fills=["tom"],
       kit={"LT": {"tone": 40, "shape": 14, "amount": 58}},
       notes="Tamborzão-flavoured tom answer under a bouncing kick."),

    S("Afro House", 122, {
        "BD": FOUR, "LT": "..x..x..x..x..x.", "HT": "....x..x....x..x",
        "CH": E8, "OH": "..x.......x.....", "RS": "x..x..x..x..x..x",
        GA: "x.....x.....x...",
    }, family="Grooves & polyrhythm", fills=["tom"],
       kit={"LT": {"tone": 42}, "HT": {"tone": 86}, "RS": {"tone": 88}},
       notes="Layered percussion in threes over a straight four."),

    S("6/8 Feel", 116, {
        "BD": "x.....x.....x...", "LT": "..x..x..x..x..x.",
        "HT": "...x.....x.....x", "CH": "x..x..x..x..x..x",
        "RS": "....x.....x.....", GA: "x.....x.....x...",
    }, family="Grooves & polyrhythm", fills=["tom"],
       kit={"CH": {"sel": 2, "tone": 66}},
       notes="Twelve-feel bell pattern mapped onto the 16-step grid."),

    S("Cumbia Machine", 100, {
        "BD": "x...x...x...x...", "SD": "....x.......x...",
        "LT": "..x.....x.....x.", "RS": "x..x..x..x..x..x",
        "CH": E8, GA: "x...x...",
    }, family="Grooves & polyrhythm", fills=["tom"],
       kit={"RS": {"tone": 92}, "LT": {"tone": 38}},
       notes="Cumbia's limping guiro figure translated to rim and tom."),

    S("Samba Electro", 132, {
        "BD": "x..x..x.x..x..x.", "SD": "..x.x.x...x.x.x.",
        "CH": E16, "LT": "....x.......x...", "RS": "x.x.x.x.x.x.x.x.",
        GA: "x..x..x.",
    }, family="Grooves & polyrhythm", fills=["snare", "tom"],
       kit={"CH": {"sel": 3, "tone": 90}, "SD": {"tone": 82}},
       notes="Surdo-ish kick with a busy caixa-style snare."),

    S("Bossa Electro", 128, {
        "BD": "x.....x.x.....x.", "RS": "..x..x..x..x..x.",
        "CH": E8, "SD": "............x...", "OH": "..............x.",
        GA: "x.......",
    }, family="Grooves & polyrhythm", strict=True,
       kit={"RS": {"tone": 76, "shape": 10, "amount": 40}},
       notes="Clave-like rim over a soft two-feel. Strict to keep it polite."),

    S("Disco", 120, {
        "BD": FOUR, "SD": BACK, "OH": OFF8, "CH": E16,
        "CY": ONE, "HT": "..........x.x...", "CP": BACK,
        GA: "x...x...x...x...",
    }, family="Grooves & polyrhythm", fills=["snare", "tom"],
       kit={"OH": {"sel": 1, "tone": 74}, "CH": {"sel": 0, "tone": 68}},
       notes="Open hat on every offbeat, clap on the backbeat, tom pickups."),

    S("Boogie", 112, {
        "BD": "x...x.....x.x...", "SD": BACK, "CH": E16,
        "OH": "..x.......x.....", "RS": "......x.....x...",
        "CP": "............x...", GA: "x...x...",
    }, family="Grooves & polyrhythm", fills=["snare"], shuffle=36,
       kit={"CH": {"sel": 2, "tone": 72}},
       notes="Slinky early-80s kick with a touch of shuffle."),

    S("Nu-Disco", 118, {
        "BD": FOUR, "CP": BACK, "OH": OFF8, "CH": "x.xxx.xxx.xxx.xx",
        "RS": "..........x.....", "CY": ONE, GA: "x...x...",
    }, family="Grooves & polyrhythm", fills=["snare"],
       kit={"CH": {"sel": 1, "tone": 60}, "CP": {"tone": 64, "shape": 4, "amount": 36}},
       notes="Disco frame, softer tone settings, stuttered hats."),

    S("Polyrhythm 5", 124, {
        "BD": FOUR, "RS": "x....x....x....x", "CH": "..x...x...x...x.",
        "LT": "x......x......x.", "CY": ONE,
        GA: "x....x....x....x",
    }, family="Grooves & polyrhythm", strict=True,
       kit={"RS": {"tone": 86}, "LT": {"tone": 40}},
       notes="Rim in fives, tom in sevens, kick in fours. Phases across the 64 steps."),

    S("Drone Pulse", 70, {
        "BD": "x.......x.......", "CY": "x...............",
        "CH": "x..x..x..x..x..x", "RS": "....x.......x...",
        "LT": "..........x.....", GA: "x.......",
    }, family="Grooves & polyrhythm", strict=True,
       kit={"CY": {"sel": 1, "tone": 8, "shape": 28, "amount": 110},
            "CH": {"sel": 5, "tone": 16}},
       notes="Slowest pattern in the bank. Meant to sit under a long drone."),
    # ---------------- tresillo & kick-driven ----------------
    S("Tresillo", 124, {
        "BD": TRES, "CP": BACK, "OH": OFF8, "CH": E8,
        "RS": "......x.....x...", GA: "x..x..x.x..x..x.",
    }, family="Tresillo & kick-driven", fills=["snare"],
       kit={"CH": {"sel": 1, "tone": 66}, "CP": {"tone": 68, "shape": 6, "amount": 44}},
       notes="The 3-3-2 kick, straight. Clap on the backbeat so the displacement is audible against something fixed."),

    S("Tresillo Techno", 134, {
        "BD": TRES, "CH": E16, "OH": "......x.......x.",
        "CY": ONE, "SD": "..............X.",
        GA: "x..x..x.x..x..x.",
    }, family="Tresillo & kick-driven", fills=["snare", "tom"],
       kit={"BD": {"tone": 26, "shape": 22, "amount": 76}, "CH": {"sel": 4, "tone": 98}},
       notes="Same kick at techno tempo under relentless sixteenths. Every kick accented."),

    S("Half Tresillo", 110, {
        "BD": "x.....x.....x...", "SD": BACK, "CH": E8,
        "OH": "..x.......x.....", "RS": "...........x....",
        GA: "x.....x.....x...",
    }, family="Tresillo & kick-driven", fills=["snare"],
       kit={"CH": {"sel": 2, "tone": 58}, "BD": {"tone": 34, "shape": 10, "amount": 48}},
       notes="The 3-3-2 stretched over the whole bar, so the kick lands three times and leaves room."),
]

assert len(TT606_STYLES) == 64, len(TT606_STYLES)
