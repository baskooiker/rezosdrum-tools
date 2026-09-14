"""Core engine: voice maps, pattern notation, development, MIDI + chart export.

Step notation (one character per step, 64 steps per pattern):
    .  step off
    x  step on
    X  step on, accented
    f  step on, flam modifier
    F  step on, accented, flam modifier
    r  step on, roll modifier
    R  step on, accented, roll modifier

The vocabulary is deliberately limited to what the TT-606 / TT-78 sequencer
can actually store: a step is off, on, or accented, optionally carrying the
flam and/or roll modifier. There is no per-step velocity on the hardware.
"""

import hashlib
import struct

PPQ = 96
TICKS_PER_STEP = PPQ // 4          # 16th note
STEPS = 64
VEL_NORMAL = 100
VEL_ACCENT = 127
VEL_FLAM_GRACE = 90
FLAM_OFFSET = TICKS_PER_STEP // 3  # grace note ahead of the beat
ROLL_OFFSET = TICKS_PER_STEP // 2  # second strike halfway to the next step
NOTE_LEN = 6

ON = set("xXfFrR")
ACCENTED = set("XFR")
FLAMMED = set("fF")
ROLLED = set("rR")


class Voice:
    def __init__(self, key, name, note, role, tone_cc=None, shape_cc=None,
                 amount_cc=None, select_cc=None, select_max=0):
        self.key = key
        self.name = name
        self.note = note
        self.role = role
        self.tone_cc = tone_cc
        self.shape_cc = shape_cc
        self.amount_cc = amount_cc
        self.select_cc = select_cc
        self.select_max = select_max


# --- TT-606 Drum Drone -------------------------------------------------------
TT606_VOICES = [
    Voice("BD", "Bass Drum",      36, "kick",  20, 22, 23),
    Voice("SD", "Snare Drum",     38, "snare", 28, 30, 31),
    Voice("LT", "Low Tom",        43, "tom",   36, 38, 39),
    Voice("HT", "High Tom",       48, "tom",   44, 46, 47),
    Voice("CY", "Cymbal",         51, "cym",   52, 54, 55, 56, 3),
    Voice("OH", "Open Hi-hat",    46, "ohat",  60, 62, 63, 64, 5),
    Voice("CH", "Closed Hi-hat",  42, "hat",   68, 70, 71, 72, 5),
    Voice("RS", "Rim Shot",       37, "rim",   76, 78, 79),
    Voice("CP", "Hand Clap",      39, "clap",  84, 86, 87),
]

# --- TT-78 Beat Bot ----------------------------------------------------------
TT78_VOICES = [
    Voice("BD", "Bass Drum",      36, "kick",  20, 22, 23),
    Voice("SD", "Snare Drum",     38, "snare", 28, 30, 31),
    Voice("HH", "Hi-hat",         42, "hat",   68, 70, 71),
    Voice("CY", "Cymbal",         51, "cym",   60, 62, 63),
    Voice("TB", "Tambourine",     54, "shaker", 84, 86, 87),
    Voice("CB", "Cowbell",        56, "bell",  53, 54, 55),
    Voice("CL", "Clave",          75, "bell",  52, 54, 55),
    Voice("MA", "Maracas",        70, "shaker", 76, 78, 79),
    Voice("GS", "Guiro (short)",  73, "perc",  85, 86, 87),
    Voice("GL", "Guiro (long)",   74, "perc",  85, 86, 87),
    Voice("LC", "Low Conga",      64, "conga", 36, 38, 39),
    Voice("HC", "High Conga",     63, "conga", 44, 46, 47),
    Voice("LB", "Low Bongo",      61, "conga", 37, 38, 39),
    Voice("HB", "High Bongo",     60, "conga", 45, 46, 47),
]

MACHINES = {
    "TT-606": TT606_VOICES,
    "TT-78": TT78_VOICES,
}

# Global (pattern-wide) CCs, identical on both machines.
CC_AUTOFILL = 16
CC_FLAM_TIME = 17
CC_SHUFFLE = 18

GLOBAL_ACCENT = "GA"   # pseudo-voice: the pattern's dedicated Global Accent lane


def voices_of(machine):
    return {v.key: v for v in MACHINES[machine]}


# --- notation helpers --------------------------------------------------------

def tile(motif, length=STEPS):
    """Repeat a motif until `length` steps."""
    if not motif:
        return "." * length
    return (motif * (length // len(motif) + 1))[:length]


def merge(base, overlay):
    """Overlay non-'.' characters of `overlay` onto `base`."""
    base = tile(base)
    overlay = tile(overlay)
    return "".join(o if o != "." else b for b, o in zip(base, overlay))


def bars(*four):
    """Concatenate four 16-step bars into a 64-step lane."""
    out = "".join(tile(b, 16) for b in four)
    assert len(out) == STEPS, len(out)
    return out


def bar(lane, index):
    return lane[index * 16:(index + 1) * 16]


def set_step(lane, index, char):
    return lane[:index] + char + lane[index + 1:]


def accentuate(lane, indices):
    """Promote the given steps to accented, if they are on."""
    out = list(lane)
    for i in indices:
        if out[i] in ON:
            out[i] = {"x": "X", "f": "F", "r": "R"}.get(out[i], out[i])
    return "".join(out)


def rng(*parts):
    """Deterministic pseudo-random stream from a string seed."""
    seed = "|".join(str(p) for p in parts).encode()
    digest = hashlib.sha256(seed).digest()
    state = {"buf": digest, "pos": 0}

    def nxt():
        if state["pos"] >= len(state["buf"]):
            state["buf"] = hashlib.sha256(state["buf"]).digest()
            state["pos"] = 0
        b = state["buf"][state["pos"]]
        state["pos"] += 1
        return b

    class R:
        def rand(self):
            return nxt() / 255.0

        def chance(self, p):
            return self.rand() < p

        def pick(self, seq):
            return seq[nxt() % len(seq)]

    return R()
