"""64 pattern styles for the Cyclone Analogic TT-78 Beat Bot.

Voices: BD SD HH CY TB CB CL MA GS GL LC HC LB HB, plus Global Accent (GA).
The TT-78 has no Inst Select CCs, so voice variation is expressed through the
per-instrument Tone and Nuance Shape / Amount controls.
"""

from engine import GLOBAL_ACCENT as GA
from export import Style

FOUR = "x...x...x...x..."
TWO = "x.......x......."
OFF8 = "..x...x...x...x."
E8 = "x.x.x.x.x.x.x.x."
E16 = "xxxxxxxxxxxxxxxx"
BACK = "....x.......x..."
ONE = "x..............."
# Son clave 3-2 and 2-3 on a 16-step bar
CLAVE32 = "x..x..x...x.x..."
CLAVE23 = "..x.x...x..x..x."
CASCARA = "x.xx.x.xx.x.xx.x"
TUMBAO = "......x.x.....x."
TRES = "x..x..x.x..x..x."   # 3-3-2 tresillo at sixteenth resolution


def S(*a, **k):
    return Style(*a, **k)


TT78_STYLES = [
    # ---------------- Page 1: CR-78 preset heritage ----------------
    S("Rock 1", 120, {
        "BD": TWO, "SD": BACK, "HH": E8, "CY": ONE,
        GA: "x...x...x...x...",
    }, family="CR-78 heritage", fills=["snare", "conga"],
       kit={"HH": {"tone": 64}, "CY": {"tone": 60}},
       notes="The plain preset, given four bars of life and a conga fill."),

    S("Rock 2", 128, {
        "BD": "x.......x...x...", "SD": BACK, "HH": E16,
        "CY": ONE, "TB": "..............x.",
        GA: "x...x...",
    }, family="CR-78 heritage", fills=["snare", "conga"],
       kit={"HH": {"tone": 72, "shape": 6, "amount": 30}},
       notes="Busier hat and an extra kick before the backbeat."),

    S("Disco 1", 120, {
        "BD": FOUR, "SD": BACK, "HH": E16, "CY": ONE,
        "TB": OFF8, GA: "x...x...x...x...",
    }, family="CR-78 heritage", fills=["snare"],
       kit={"TB": {"tone": 80, "shape": 8, "amount": 44}, "HH": {"tone": 76}},
       notes="Tambourine on the offbeats is the whole disco trick."),

    S("Disco 2", 124, {
        "BD": FOUR, "SD": BACK, "HH": E16, "CB": "..x.......x.....",
        "TB": OFF8, "CY": ONE, GA: "x...x...x...x...",
    }, family="CR-78 heritage", fills=["snare", "conga"],
       kit={"CB": {"tone": 88}, "TB": {"tone": 84}},
       notes="Cowbell answering the tambourine."),

    S("Slow Rock", 76, {
        "BD": "x.....x.........", "SD": "........x.......",
        "HH": "x..x..x..x..x..x", "CY": ONE,
        GA: "x.......x.......",
    }, family="CR-78 heritage", fills=["snare"],
       kit={"HH": {"tone": 48, "shape": 14, "amount": 60}},
       notes="Twelve-feel ballad. Hat in threes."),

    S("Foxtrot", 104, {
        "BD": FOUR, "SD": BACK, "HH": E8, "CL": "..x...x...x...x.",
        GA: "x...x...",
    }, family="CR-78 heritage", strict=True,
       kit={"CL": {"tone": 72}},
       notes="Stiff ballroom four. Strict, as the original was."),

    S("Swing", 132, {
        "BD": TWO, "SD": BACK, "HH": "x..x..x..x..x..x",
        "CY": "x..x..x..x..x..x", "GA": "x...x...",
    }, family="CR-78 heritage", fills=["snare"], shuffle=80,
       kit={"CY": {"tone": 54, "shape": 12, "amount": 50}},
       notes="Ride-style cymbal in triplet feel with shuffle at 80."),

    S("Shuffle", 116, {
        "BD": "x.....x.x.....x.", "SD": BACK, "HH": E8,
        "TB": "..x...x...x...x.", GA: "x...x...",
    }, family="CR-78 heritage", fills=["snare"], shuffle=72,
       kit={"HH": {"tone": 58}},
       notes="Swung eighths, tambourine on the skips."),

    S("Waltz Feel", 108, {
        "BD": "x.....x.....x...", "SD": "...x.....x.....x",
        "HH": "x..x..x..x..x..x", "CY": ONE,
        GA: "x.....x.....x...",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"HH": {"tone": 52}},
       notes="Three-feel mapped onto 16 steps so it phases nicely over 64."),

    S("Bossa Nova", 128, {
        "BD": "x.....x.x.....x.", "CL": CLAVE32, "HH": E8,
        "MA": E16, "SD": "............x...",
        GA: "x.......",
    }, family="CR-78 heritage", strict=True,
       kit={"CL": {"tone": 76, "shape": 10, "amount": 38},
            "MA": {"tone": 60, "shape": 6, "amount": 26}},
       notes="Clave over maracas sixteenths. Strict to stay authentic."),

    S("Samba", 136, {
        "BD": "x..x..x.x..x..x.", "SD": "..x.x.x...x.x.x.",
        "MA": E16, "CB": "....x.......x...", "GS": "..x.......x.....",
        "LC": TUMBAO, GA: "x..x..x.",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"LC": {"tone": 40, "shape": 12, "amount": 48}, "CB": {"tone": 92}},
       notes="Surdo kick, caixa snare, agogô-style cowbell."),

    S("Cha-Cha", 124, {
        "BD": "x...x...x...x...", "CB": E8, "CL": CLAVE23,
        "HC": "..x.......x.....", "LC": "......x.......x.",
        "MA": OFF8, GA: "x...x...",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"CB": {"tone": 96, "shape": 4, "amount": 30}},
       notes="Cowbell eighths, congas trading the offbeats."),

    S("Rhumba", 112, {
        "BD": "x.....x...x.....", "CL": "x..x..x...x.x...",
        "MA": E8, "LC": "......x.x.....x.", "HC": "....x.......x...",
        GA: "x.......",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"CL": {"tone": 70}, "MA": {"tone": 56}},
       notes="Rhumba clave with a tumbao conga underneath."),

    S("Tango", 116, {
        "BD": "x...x...x...x...", "SD": "..............x.",
        "CL": "x...x...x..x....", "MA": E8, "CY": ONE,
        GA: "x...x...x...x...",
    }, family="CR-78 heritage", strict=True,
       kit={"CL": {"tone": 82}},
       notes="Dotted tango accent figure. Deliberately rigid."),

    S("Beguine", 108, {
        "BD": "x.....x.x.....x.", "CL": CLAVE32, "MA": E16,
        "HC": "....x.......x...", "LB": "..x.......x.....",
        GA: "x.......",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"MA": {"tone": 52, "shape": 8, "amount": 34}},
       notes="Soft two-feel with bongo colour."),

    S("Mambo", 140, {
        "BD": "x...x...x...x...", "CB": "x..x..x.x..x..x.",
        "CL": CLAVE23, "LC": TUMBAO, "HC": "....x..x....x..x",
        "MA": E8, GA: "x...x...x...x...",
    }, family="CR-78 heritage", fills=["conga"],
       kit={"CB": {"tone": 100}, "HC": {"tone": 90}},
       notes="Bell pattern plus tumbao. The busiest of the presets."),

    # ---------------- Page 2: Latin, Afro & Caribbean ----------------
    S("Songo", 104, {
        "BD": "x.....x.x.....x.", "SD": "...x.......x....",
        "HH": OFF8, "CL": CLAVE32, "LC": TUMBAO,
        "HC": "....x.......x...", GA: "x.......",
    }, family="Latin & Afro", fills=["conga", "snare"],
       kit={"LC": {"tone": 38, "shape": 14, "amount": 52}, "SD": {"tone": 70}},
       notes="Songo's snare-and-conga conversation."),

    S("Guaguanco", 100, {
        "BD": "x.......x.......", "CL": CLAVE32, "LC": "......x.x.....x.",
        "HC": "..x.x.....x.x...", "LB": "....x.......x...",
        "MA": E8, GA: "x.......",
    }, family="Latin & Afro", fills=["conga"],
       kit={"LC": {"tone": 36}, "HC": {"tone": 88}},
       notes="Three congas in dialogue over clave."),

    S("Bomba", 108, {
        "BD": "x...x...x...x...", "LC": "x..x..x...x.x...",
        "HC": "..x.x...x..x..x.", "CL": "x.....x.......x.",
        "MA": E16, GA: "x...x...",
    }, family="Latin & Afro", fills=["conga"],
       kit={"MA": {"tone": 64}},
       notes="Sicá-flavoured bomba figure."),

    S("Plena", 112, {
        "BD": "x.....x.x.......", "SD": "....x..x....x..x",
        "GS": "..x...x...x...x.", "MA": E8, "CL": CLAVE23,
        GA: "x.....x.",
    }, family="Latin & Afro", fills=["snare", "conga"],
       kit={"GS": {"tone": 74, "shape": 10, "amount": 40}},
       notes="Guiro on the offbeats, panderos as snare."),

    S("Merengue", 144, {
        "BD": "x...x...x...x...", "SD": "..x.x.x...x.x.x.",
        "GS": E8, "MA": E16, "CB": "....x.......x...",
        GA: "x...x...x...x...",
    }, family="Latin & Afro", fills=["snare"],
       kit={"SD": {"tone": 84, "shape": 16, "amount": 60}},
       notes="Fast tambora-style snare, güira running eighths."),

    S("Cumbia", 96, {
        "BD": "x...x...x...x...", "SD": "....x.......x...",
        "GL": "..x.....x.....x.", "GS": "x..x..x..x..x..x",
        "LC": "......x.......x.", "MA": E8, GA: "x...x...",
    }, family="Latin & Afro", fills=["conga"],
       kit={"GL": {"tone": 66}, "GS": {"tone": 78}},
       notes="Long and short guiro strokes doing the cumbia limp."),

    S("Salsa", 132, {
        "BD": "x.....x.x.....x.", "CB": "x..x..x.x..x..x.",
        "CL": CLAVE32, "LC": TUMBAO, "HC": "....x..x....x..x",
        "MA": E8, "GS": "..............x.",
        GA: "x.......x.......",
    }, family="Latin & Afro", fills=["conga"],
       kit={"CB": {"tone": 98}, "LC": {"tone": 40}},
       notes="Full salsa engine: bell, clave, tumbao, maracas."),

    S("Afrobeat", 116, {
        "BD": "x...x.....x.x...", "SD": "....x.......x...",
        "HH": "x.xxx.xxx.xxx.xx", "CB": "..x...x...x...x.",
        "LC": "..x..x..x..x..x.", "TB": "....x.......x...",
        GA: "x...x...",
    }, family="Latin & Afro", fills=["conga", "snare"],
       kit={"HH": {"tone": 70}, "CB": {"tone": 86}},
       notes="Tony Allen displacement — nothing lands where you expect."),

    S("Highlife", 124, {
        "BD": "x...x...x...x...", "SD": "....x..x....x..x",
        "HH": E8, "CB": "x..x..x..x..x..x", "HC": "..x.......x.....",
        "MA": E16, GA: "x...x...",
    }, family="Latin & Afro", fills=["conga"],
       kit={"CB": {"tone": 92}},
       notes="Bell in threes against the four."),

    S("Soukous", 140, {
        "BD": "x..x..x.x..x..x.", "SD": "....x.......x...",
        "HH": E16, "HC": "..x.x.....x.x...", "LC": "......x.......x.",
        "TB": OFF8, GA: "x..x..x.",
    }, family="Latin & Afro", fills=["conga", "snare"],
       kit={"HH": {"tone": 82}, "HC": {"tone": 94}},
       notes="Fast, bright, congas chattering."),

    S("Bembe 6/8", 112, {
        "BD": "x.....x.....x...", "CB": "x..x.x.x..x.x.x.",
        "LC": "..x..x..x..x..x.", "HC": "...x.....x.....x",
        "MA": "x..x..x..x..x..x", GA: "x.....x.....x...",
    }, family="Latin & Afro", strict=True,
       kit={"CB": {"tone": 90, "shape": 6, "amount": 32}},
       notes="Standard 12/8 bell pattern. Strict — the phasing is the interest."),

    S("Calypso", 120, {
        "BD": "x.....x.x.....x.", "SD": "....x.......x...",
        "HH": E8, "CL": CLAVE23, "TB": OFF8,
        "HB": "..x.......x.....", GA: "x.......",
    }, family="Latin & Afro", fills=["conga", "snare"],
       kit={"TB": {"tone": 78}},
       notes="Two-feel calypso with bongo accents."),

    S("One Drop", 72, {
        "BD": "........x.......", "SD": "........X.......",
        "HH": OFF8, "TB": "..x...x...x...x.",
        "CY": ONE, GA: "........X.......",
    }, family="Latin & Afro", fills=["snare"],
       kit={"SD": {"tone": 62, "shape": 20, "amount": 78}, "HH": {"tone": 46}},
       notes="Reggae one drop: nothing on beat 1, everything on beat 3."),

    S("Steppers", 76, {
        "BD": FOUR, "SD": "........x.......", "HH": OFF8,
        "TB": E8, "CY": ONE, GA: "x...x...x...x...",
    }, family="Latin & Afro", fills=["snare"],
       kit={"BD": {"tone": 34, "shape": 10, "amount": 40}},
       notes="Four-to-the-floor reggae. Kick tuned deep."),

    S("Dub", 70, {
        "BD": "........x.......", "SD": "........x.......",
        "HH": "..x.......x.....", "CY": ONE,
        "HB": "............x...", GA: "........x.......",
    }, family="Latin & Afro", strict=True,
       kit={"CY": {"tone": 24, "shape": 26, "amount": 100},
            "SD": {"tone": 44, "shape": 24, "amount": 96}},
       notes="Almost empty, long decays. Leave room for the delay."),

    S("Nyabinghi", 84, {
        "BD": "x.....x.....x...", "SD": "...x.....x.....x",
        "LC": "..x..x..x..x..x.", "HC": "x..x..x..x..x..x",
        "TB": "....x.....x.....", GA: "x.....x.....x...",
    }, family="Latin & Afro", fills=["conga"],
       kit={"LC": {"tone": 36}, "HC": {"tone": 84}},
       notes="Hand-drum three-feel, no hats at all."),

    # ---------------- Page 3: electronic reinterpretations ----------------
    S("Motorik 78", 140, {
        "BD": "x...x.x.x...x.x.", "SD": BACK, "HH": E16,
        "CY": ONE, "TB": "..............x.",
        GA: "x...x...x...x...",
    }, family="Electronic", strict=True,
       kit={"HH": {"tone": 74}},
       notes="Neu! pulse on the Beat Bot. Strict."),

    S("Italo 78", 122, {
        "BD": FOUR, "SD": BACK, "HH": E16, "TB": OFF8,
        "CB": "..........x.x...", "CY": ONE,
        GA: "x...x...x...x...",
    }, family="Electronic", fills=["conga", "snare"],
       kit={"CB": {"tone": 94}, "TB": {"tone": 82}},
       notes="Cowbell answer phrase in the back half of the bar."),

    S("Synth-Pop 78", 118, {
        "BD": TWO, "SD": BACK, "HH": E8, "TB": BACK,
        "CY": ONE, GA: "x...x...x...x...",
    }, family="Electronic", fills=["snare"],
       kit={"TB": {"tone": 76, "shape": 6, "amount": 40}},
       notes="Tambourine doubling the snare — the CR-78 pop sound."),

    S("City Pop", 112, {
        "BD": "x...x.....x.x...", "SD": BACK, "HH": E16,
        "TB": OFF8, "HC": "..........x.....", "CY": ONE,
        GA: "x...x...",
    }, family="Electronic", fills=["snare", "conga"], shuffle=24,
       kit={"HH": {"tone": 68, "shape": 8, "amount": 36}},
       notes="Slinky kick, a touch of shuffle, bright tambourine."),

    S("Boogie 78", 110, {
        "BD": "x...x.....x.x...", "SD": BACK, "HH": E16,
        "CB": "..x.......x.....", "TB": OFF8,
        GA: "x...x...",
    }, family="Electronic", fills=["snare"], shuffle=36,
       kit={"CB": {"tone": 90}},
       notes="Early-80s boogie with cowbell punctuation."),

    S("Nu-Disco 78", 118, {
        "BD": FOUR, "SD": BACK, "HH": "x.xxx.xxx.xxx.xx",
        "TB": OFF8, "MA": E16, "CY": ONE,
        GA: "x...x...",
    }, family="Electronic", fills=["snare", "conga"],
       kit={"HH": {"tone": 62}, "MA": {"tone": 54, "shape": 6, "amount": 28}},
       notes="Stuttered hats plus maraca sixteenths."),

    S("House 78", 124, {
        "BD": FOUR, "SD": BACK, "HH": E8, "TB": OFF8,
        "CL": "..............x.", GA: "x...x...x...x...",
    }, family="Electronic", fills=["snare"],
       kit={"HH": {"tone": 78}, "CL": {"tone": 84}},
       notes="House frame using tambourine where an open hat would go."),

    S("Deep House 78", 120, {
        "BD": FOUR, "SD": "....x...........", "HH": "x..xx..xx..xx..x",
        "MA": E16, "HB": "......x.....x...",
        GA: "x.......x.......",
    }, family="Electronic", fills=["conga"],
       kit={"HH": {"tone": 44, "shape": 12, "amount": 56}, "MA": {"tone": 48}},
       notes="Soft and shuffly, bongo filling the gaps."),

    S("Downtempo", 90, {
        "BD": "x.......x.......", "SD": "....x.......x...",
        "HH": OFF8, "MA": E8, "CY": ONE,
        "HB": "..........x.....", GA: "x...x...",
    }, family="Electronic", fills=["snare", "conga"],
       kit={"HH": {"tone": 52}, "CY": {"tone": 32, "shape": 22, "amount": 88}},
       notes="Unhurried. Cymbal set long."),

    S("Trip-Hop 78", 84, {
        "BD": "x.......x.......", "SD": "....x.........x.",
        "HH": "..x...x...x...x.", "TB": "........x.......",
        "CY": ONE, GA: "x...x...",
    }, family="Electronic", fills=["snare"], flam_time=40,
       kit={"SD": {"tone": 46, "shape": 24, "amount": 92}},
       notes="Late snare, flams in the fill bar."),

    S("Lo-Fi", 82, {
        "BD": "x.....x...x.....", "SD": "....x.......x...",
        "HH": E8, "MA": "..x...x...x...x.",
        GA: "x...x...",
    }, family="Electronic", fills=["snare"], shuffle=68, flam_time=28,
       kit={"HH": {"tone": 40, "shape": 16, "amount": 66},
            "SD": {"tone": 50, "shape": 20, "amount": 74}},
       notes="Swung, soft, slightly late. Tone controls rolled down."),

    S("Balearic", 106, {
        "BD": FOUR, "SD": "............x...", "HH": OFF8,
        "MA": E16, "GS": "..x.......x.....", "CY": ONE,
        GA: "x.......",
    }, family="Electronic", fills=["conga"],
       kit={"MA": {"tone": 58}, "GS": {"tone": 70}},
       notes="Sunset tempo, guiro scrape as the hook."),

    S("Cosmic Disco", 116, {
        "BD": FOUR, "SD": BACK, "HH": E16, "TB": OFF8,
        "CB": "x..x..x..x..x..x", "CY": ONE,
        GA: "x..x..x..x..x..x",
    }, family="Electronic", fills=["snare", "conga"],
       kit={"CB": {"tone": 96, "shape": 8, "amount": 40}},
       notes="Cowbell in threes over a straight four — the accent lane follows the bell."),

    S("Krautrock Shuffle", 132, {
        "BD": "x...x.x.x...x.x.", "SD": BACK, "HH": E8,
        "MA": E16, "CY": ONE, GA: "x...x...",
    }, family="Electronic", fills=["snare"], shuffle=44,
       kit={"MA": {"tone": 62}},
       notes="Motorik with the shuffle knob at 44 — it lopes."),

    S("Minimal 78", 126, {
        "BD": FOUR, "HH": "..x.....x.......", "CL": "......x.........",
        "MA": "............x...", GA: "x...............",
    }, family="Electronic", strict=True,
       kit={"CL": {"tone": 80}, "HH": {"tone": 56, "shape": 18, "amount": 30}},
       notes="Sparse to the point of rudeness. Strict."),

    # ---------------- Page 4: percussion studies & polyrhythm ----------------
    S("Conga Workout", 108, {
        "BD": "x.......x.......", "LC": "x..x..x...x.x...",
        "HC": "..x.x...x..x..x.", "LB": "....x.......x...",
        "HB": "......x.......x.", "MA": E16,
        GA: "x.......x.......",
    }, family="Percussion & polyrhythm", fills=["conga"],
       kit={"LC": {"tone": 34}, "HC": {"tone": 86}, "LB": {"tone": 44},
            "HB": {"tone": 100}},
       notes="All four hand drums, each on its own figure, tuned apart."),

    S("Bongo Cascara", 116, {
        "BD": "x.....x.x.....x.", "LB": CASCARA, "HB": "..x...x...x...x.",
        "CL": CLAVE32, "MA": E8, GA: "x.......",
    }, family="Percussion & polyrhythm", fills=["conga"],
       kit={"LB": {"tone": 46, "shape": 8, "amount": 34}, "HB": {"tone": 102}},
       notes="Cascara on the bongos with clave underneath."),

    S("Clave & Maracas", 104, {
        "BD": "x.......x.......", "CL": CLAVE32, "MA": E16,
        "GS": "..............x.", GA: "x.......",
    }, family="Percussion & polyrhythm", strict=True,
       kit={"CL": {"tone": 78, "shape": 4, "amount": 24},
            "MA": {"tone": 56, "shape": 6, "amount": 28}},
       notes="Two voices and a kick. A study in restraint."),

    S("Guiro Groove", 100, {
        "BD": "x...x...x...x...", "GL": "..x.....x.....x.",
        "GS": "x..x..x..x..x..x", "MA": E8, "CB": "....x.......x...",
        GA: "x...x...",
    }, family="Percussion & polyrhythm", fills=["conga"],
       kit={"GL": {"tone": 62}, "GS": {"tone": 82, "shape": 10, "amount": 44}},
       notes="Long and short guiro traded against each other."),

    S("Tambourine Pulse", 122, {
        "BD": FOUR, "TB": E16, "SD": BACK, "HH": OFF8,
        GA: "x...x...x...x...",
    }, family="Percussion & polyrhythm", fills=["snare"],
       kit={"TB": {"tone": 86, "shape": 12, "amount": 48}},
       notes="Sixteenth tambourine with accents wandering by bar."),

    S("Cowbell Drive", 130, {
        "BD": FOUR, "CB": E8, "SD": BACK, "MA": E16,
        "HC": "..........x.....", GA: "x...x...x...x...",
    }, family="Percussion & polyrhythm", fills=["conga", "snare"],
       kit={"CB": {"tone": 104, "shape": 6, "amount": 36}},
       notes="More cowbell. Non-negotiable."),

    S("Dembow 78", 96, {
        "BD": "x.....x.x.....x.", "SD": "...x..x....x..x.",
        "HH": E8, "TB": "..x...x...x...x.", "CB": "....x.......x...",
        GA: "x.....x.",
    }, family="Percussion & polyrhythm", fills=["snare"],
       kit={"SD": {"tone": 72}, "TB": {"tone": 80}},
       notes="Dembow with the tambourine on the offbeats."),

    S("Reggaeton 78", 94, {
        "BD": "x.......x.......", "SD": "...x..x....x..x.",
        "HH": OFF8, "MA": E16, "GS": "..............x.",
        GA: "x.......x.......",
    }, family="Percussion & polyrhythm", fills=["snare", "conga"],
       kit={"MA": {"tone": 52}},
       notes="Maracas smoothing out the dembow."),

    S("Baile 78", 128, {
        "BD": "x..x..x.x..x..x.", "SD": "....x.......x...",
        "LC": "..x.x...x.x.....", "HC": "......x.......x.",
        "HH": E8, GA: "x..x..x.",
    }, family="Percussion & polyrhythm", fills=["conga"],
       kit={"LC": {"tone": 38, "shape": 14, "amount": 56}},
       notes="Tamborzão figure on the congas."),

    S("Afro House 78", 122, {
        "BD": FOUR, "LC": "..x..x..x..x..x.", "HC": "....x..x....x..x",
        "HH": E8, "TB": "..x.......x.....", "CB": "x..x..x..x..x..x",
        GA: "x.....x.....x...",
    }, family="Percussion & polyrhythm", fills=["conga"],
       kit={"CB": {"tone": 88}, "LC": {"tone": 40}},
       notes="Threes stacked over a straight four."),

    S("Broken 78", 126, {
        "BD": "x....x..x...x..x", "SD": BACK, "HH": "x.x.xx.x.xx.x.x.",
        "HB": "......x.........", "TB": "............x...",
        "MA": E16, GA: "x....x..",
    }, family="Percussion & polyrhythm", fills=["snare", "conga"],
       kit={"HH": {"tone": 72}},
       notes="Displaced kick, uneven hats."),

    S("Poly 3:4", 118, {
        "BD": FOUR, "CB": "x..x..x..x..x..x", "MA": "x....x....x....x",
        "CL": "x.......x.......", "HC": "..x..x..x..x..x.",
        GA: "x..x..x..x..x..x",
    }, family="Percussion & polyrhythm", strict=True,
       kit={"CB": {"tone": 92}, "MA": {"tone": 60}},
       notes="Bell in threes, maracas in fives, kick in fours. Strict so the phasing is clean."),

    S("Poly 5", 120, {
        "BD": FOUR, "CL": "x....x....x....x", "HH": "..x...x...x...x.",
        "LC": "x......x......x.", "TB": "........x.......",
        GA: "x....x....x....x",
    }, family="Percussion & polyrhythm", strict=True,
       kit={"CL": {"tone": 74}, "LC": {"tone": 42}},
       notes="Fives against sevens against fours — a different alignment every bar."),

    S("Free Percussion", 112, {
        "BD": "x.........x.....", "LC": "..x....x..x...x.",
        "HC": "....x.x.....x...", "LB": ".x...x....x..x..",
        "HB": "...x....x....x.x", "GS": "......x.........",
        "MA": E8, GA: "x.........x.....",
    }, family="Percussion & polyrhythm", fills=["conga"], flam_time=18,
       kit={"LC": {"tone": 32}, "HC": {"tone": 82}, "LB": {"tone": 48},
            "HB": {"tone": 104}},
       notes="Four hand drums interlocking with no obvious downbeat. Flams add hand-drum grace notes."),
    # ---------------- tresillo & kick-driven ----------------
    S("Tresillo", 120, {
        "BD": TRES, "CL": CLAVE32, "MA": E16, "HH": OFF8,
        "SD": "............x...", GA: "x..x..x.x..x..x.",
    }, family="Tresillo & kick-driven", fills=["conga"],
       kit={"CL": {"tone": 78, "shape": 6, "amount": 30}, "MA": {"tone": 58}},
       notes="The 3-3-2 kick against son clave, which is where the figure comes from in the first place."),

    S("Tresillo Cumbia", 100, {
        "BD": TRES, "GS": "x..x..x..x..x..x", "GL": "..x.....x.....x.",
        "CB": "....x.......x...", "MA": E8, "SD": "....x.......x...",
        GA: "x..x..x.x..x..x.",
    }, family="Tresillo & kick-driven", fills=["conga", "snare"],
       kit={"GS": {"tone": 80, "shape": 10, "amount": 44}, "CB": {"tone": 92}},
       notes="Tresillo kick under a guiro ostinato. The long and short scrapes pull against the kick."),

    S("Half Tresillo", 96, {
        "BD": "x.....x.....x...", "LC": TUMBAO, "HC": "....x.......x...",
        "HH": E8, "MA": OFF8, "CL": "......x.......x.",
        GA: "x.....x.....x...",
    }, family="Tresillo & kick-driven", fills=["conga"],
       kit={"LC": {"tone": 38, "shape": 12, "amount": 50}, "HC": {"tone": 88}},
       notes="Three kicks a bar with a tumbao underneath - the most space of the tresillo set."),
]

assert len(TT78_STYLES) == 64, len(TT78_STYLES)
