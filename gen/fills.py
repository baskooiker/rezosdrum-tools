"""Generate a Fill variation for a TT-78 pattern.

A Fill plays in place of the pattern when [FILL] is pressed, or automatically
every N bars when an Auto-Fill Interval is set. It should therefore stay
recognisably the same groove rather than lurching into something unrelated: the
first half is left alone, the third bar thickens, and the fourth bar turns
around into a run that resolves.

Everything here works in the machine's own voice vocabulary and respects the
hardware: the five single-bit voices (Guiro, Low/High Bongo, Cowbell, Clave)
cannot carry accent, flam or roll, so they are only ever switched on or off.
"""

import hashlib

ON = set("xXfFrR")

#: Per machine: which voices can carry a descending run, which keep time
#: through a fill rather than stopping dead, which crashes on the downbeat,
#: and which cannot hold a modifier.
#:
#: Timekeepers matter more than they look. An early version cleared every voice
#: for the last eight steps and the result was a hole in the bar rather than a
#: fill - obvious on the latin and disco patterns, where the shaker *is* the
#: pulse. Hats and shakers now play through.
MACHINES = {
    "TT-78": {
        "run": ("HC", "LC", "SD", "TB", "MA"),
        "timekeepers": ("HH", "MA", "TB", "CB"),
        "hats": ("HH",),
        "shakers": ("MA", "TB"),
        "crash": "CY",
        "kick": "BD",
        "simple": ("GU", "LB", "HB", "CB", "CL"),
    },
    "TT-606": {
        # the Drum Drone's fill is a tom run, which is what the machine is for
        "run": ("HT", "LT", "SD", "CP", "RS"),
        "timekeepers": ("CH", "OH", "RS"),
        "hats": ("CH",),
        "shakers": ("RS",),
        "crash": "CY",
        "kick": "BD",
        "simple": (),
    },
}
ACCENT_OF = {"x": "X", "f": "F", "r": "R"}


def _rng(*parts):
    digest = hashlib.sha256("|".join(str(p) for p in parts).encode()).digest()
    state = {"buf": digest, "pos": 0}

    def nxt():
        if state["pos"] >= len(state["buf"]):
            state["buf"] = hashlib.sha256(state["buf"]).digest()
            state["pos"] = 0
        b = state["buf"][state["pos"]]
        state["pos"] += 1
        return b

    class R:
        def chance(self, p):
            return nxt() / 255.0 < p

        def pick(self, seq):
            return seq[nxt() % len(seq)]
    return R()


def _density(lanes):
    hits = sum(1 for l in lanes.values() for c in l if c in ON)
    return hits / (64.0 * max(1, len(lanes)))


def make_fill(lanes, slot, name="", machine="TT-78"):
    """Return a Fill variant of `lanes` ({voice: 64-char string})."""
    cfg = MACHINES[machine]
    RUN_ORDER = cfg["run"]
    TIMEKEEPERS = cfg["timekeepers"]
    SIMPLE_VOICES = cfg["simple"]
    CRASH, KICK = cfg["crash"], cfg["kick"]
    r = _rng("fill", slot, name)
    out = {v: list(l) for v, l in lanes.items()}
    present = [v for v, l in lanes.items() if any(c in ON for c in l)]
    sparse = _density(lanes) < 0.10

    # ---- bar 3: thicken, without changing the groove's identity -----------
    if not sparse:
        for hat in cfg["hats"]:             # straight 16ths on the hats
            if hat in out:
                for s in range(32, 48):
                    if out[hat][s] == ".":
                        out[hat][s] = "x"
                break
        for shaker in cfg["shakers"]:       # a shaker on the offbeats
            if shaker in out:
                for s in range(34, 48, 4):
                    if out[shaker][s] == ".":
                        out[shaker][s] = "x"
                break

    # ---- bar 4: the turnaround -------------------------------------------
    run_voices = [v for v in RUN_ORDER if v in present] or ["SD"]
    if len(run_voices) > 3:
        run_voices = run_voices[:3]
    # Clear the last eight steps so the run reads cleanly, but leave the kick,
    # the cymbal and the timekeepers playing - a fill is the drums moving
    # underneath a groove that keeps running, not a hole in the bar.
    tail = range(56, 64)
    keep = set((KICK, CRASH)) | (set(TIMEKEEPERS) - set(run_voices))
    for v in out:
        if v in keep:
            continue
        for s in tail:
            out[v][s] = "."

    # descending run over those eight steps
    step = 56
    for i, v in enumerate(run_voices):
        span = 8 // len(run_voices)
        for k in range(span):
            s = step + k
            if s > 63:
                break
            sym = "x"
            if k == 0:
                sym = "X"                   # accent the head of each group
            out[v][s] = sym
        step += span

    # a flam into the run and a roll on the very last step, snare for choice
    lead = "SD" if "SD" in out else run_voices[0]
    if out[lead][56] in ON or True:
        out[lead][56] = "F"
    last = run_voices[-1]
    out[last][63] = "R"

    # keep the downbeat of the bar anchored, and crash if the kit has a cymbal
    if KICK in out:
        out[KICK][48] = ACCENT_OF.get(out[KICK][48], "X") if out[KICK][48] in ON else "X"
    if CRASH in out and not sparse:
        out[CRASH][48] = "X"

    # ---- hardware legality ------------------------------------------------
    for v in SIMPLE_VOICES:
        if v in out:
            out[v] = ["x" if c in ON else "." for c in out[v]]

    return {v: "".join(l) for v, l in out.items()}
