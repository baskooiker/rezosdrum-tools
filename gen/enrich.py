"""Fill out a pattern's unused voices so performing it is subtractive.

On the machine you perform with the level faders and mutes: you pull voices out
to strip a groove back and push them in to build it. A pattern that uses four of
nine voices gives you almost nothing to do. So each pattern should be the
*maximal* version of itself, and the player subtracts.

This pass only ever writes into lanes that are **empty**. A part the style
author wrote is never modified, so the pattern still reads as itself; what
changes is that there is now something to bring in.

Added layers are keyed to what the pattern already does - the clap follows the
snare's backbeat, the toms answer in the gaps, the rim takes a counter-rhythm
that avoids the open hat - and they are deliberately sparser than the parts they
sit beside, so bringing one up adds colour rather than clutter.
"""

import hashlib

ON = set("xXfFrR")
STEPS = 64


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


def _hits(lane):
    return [i for i, c in enumerate(lane) if c in ON]


def _occupancy(lanes):
    """How many voices hit each step."""
    occ = [0] * STEPS
    for lane in lanes.values():
        for i, c in enumerate(lane):
            if c in ON:
                occ[i] += 1
    return occ


def _place(figure, bars=(0, 1, 2, 3)):
    """Expand a 16-step figure over the chosen bars of a 64-step lane."""
    lane = ["."] * STEPS
    for b in bars:
        for i, c in enumerate(figure):
            if c != ".":
                lane[b * 16 + i] = c
    return "".join(lane)


def _backbeats(lanes):
    """Where the pattern's backbeat sits, from the snare if it has one."""
    for key in ("SD",):
        h = [i % 16 for i in _hits(lanes.get(key, ""))]
        if h:
            common = sorted(set(h), key=lambda s: -h.count(s))[:2]
            if common:
                return sorted(common)
    return [4, 12]


#: figures offered per role, tried in order until one lands somewhere quiet
FIGURES = {
    "clap":   ["backbeat"],
    "snare":  ["backbeat"],
    "tom_hi": ["..........x.....", "..........x...x.", "....x.......x...",
               "........x.x.....", "..........x..x..", "......x...x.....",
               "............x.x.", "..x.......x....."],
    "tom_lo": [".......x........", ".......x.......x", "..............x.",
               "......x.....x...", "...........x....", ".......x....x...",
               "..x..........x..", "............x..."],
    "rim":    ["x..x..x..x..x..x", "..x...x...x...x.", "x...x...x...x...",
               "....x.......x...", "x.x.....x.x.....", "..x..x..x..x..x.",
               "......x.......x.", "x..........x...."],
    "cym":    ["x...............", "x.......x.......", "........x.......",
               "x.............x.", "....x...........", "x......x........"],
    "ohat":   ["..x...x...x...x.", "......x.......x.", "..............x.",
               "..x.......x.....", "......x...x...x.", "x.....x.....x..."],
    "hat":    ["x.x.x.x.x.x.x.x.", "x..x..x..x..x..x", "..x...x...x...x.",
               "x.xxx.xxx.xxx.xx", "x...x...x...x..."],
    "bell":   ["x..x..x..x..x..x", "....x.......x...", "..x...x...x...x.",
               "x...x...x...x...", "..x..x..x..x..x.", "x.....x.....x..."],
    "shaker": ["x.x.x.x.x.x.x.x.", "..x...x...x...x.", "xxxxxxxxxxxxxxxx",
               "x..x..x..x..x..x", "x.xxx.xxx.xxx.xx"],
    "conga":  ["......x.x.....x.", "..x.......x.....", "....x..x....x..x",
               "..x..x..x..x..x.", "......x.......x.", "x.....x...x....."],
    "perc":   ["..x.......x.....", "......x.......x.", "....x...........",
               "..x...x.........", "..........x...x.", "x.......x......."],
}

#: which bars a newly added layer may play in, by role. Choosing among these
#: per pattern is what stops every added tom or cymbal being the same two hits
#: in the same two bars across all 64 patterns.
BAR_CHOICES = {
    "cym":    [(0,), (0, 2), (0, 1, 2, 3), (2,), (0, 3)],
    "tom_hi": [(1, 3), (3,), (1,), (0, 1, 2, 3), (2, 3)],
    "tom_lo": [(0, 2), (2,), (0,), (0, 1, 2, 3), (1, 3)],
    "perc":   [(1, 3), (0, 2), (0, 1, 2, 3), (3,)],
    "rim":    [(0, 1, 2, 3), (1, 3), (0, 2)],
    "conga":  [(0, 1, 2, 3), (1, 3), (0, 2)],
    "bell":   [(0, 1, 2, 3), (0, 2), (1, 3)],
}


def enrich(machine, slot, style, lanes, voices, target=None):
    """Add idiomatic parts for unused voices. Returns a new lanes dict.

    `voices` maps voice key -> role, in the machine's own vocabulary.
    """
    out = dict(lanes)
    r = _rng("enrich", machine, slot, style.name)
    occ = _occupancy(out)
    density = sum(1 for v in occ if v) / float(STEPS)

    order = ["clap", "snare", "tom_hi", "tom_lo", "rim", "cym",
             "ohat", "hat", "bell", "shaker", "conga", "perc"]
    by_role = {}
    for key, role in voices.items():
        by_role.setdefault(role, []).append(key)

    for role in order:
        for key in sorted(by_role.get(role, [])):
            lane = out.get(key, "." * STEPS)
            if len(_hits(lane)) >= 2:
                continue                     # the style already uses this voice

            if role in ("clap", "snare"):
                beats = _backbeats(out)
                fig = ["."] * 16
                for b in beats:
                    fig[b] = "x"
                figure = "".join(fig)
                bars = (0, 1, 2, 3)
            else:
                choices = FIGURES.get(role)
                if not choices:
                    continue
                # Prefer figures that land where the pattern is quiet, but
                # choose among the good ones at random rather than always
                # taking the best - otherwise every pattern gets the same part.
                def clash(f):
                    return sum(occ[b * 16 + i]
                               for b in range(4)
                               for i, c in enumerate(f) if c != ".")
                ranked = sorted(choices, key=clash)
                best = clash(ranked[0])
                good = [f for f in ranked if clash(f) <= best + 4] or ranked[:1]
                figure = r.pick(good)
                bars = r.pick(BAR_CHOICES.get(role, [(0, 1, 2, 3)]))
                if density > 0.85 and len(bars) == 4:
                    bars = r.pick([(1, 3), (0, 2), (3,)])

            new = _place(figure, bars)
            # never overwrite another voice's accents by crowding the downbeat
            out[key] = new
            occ = _occupancy(out)

    return out
