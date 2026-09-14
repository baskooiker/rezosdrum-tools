"""Expand a style's base motifs into a full 64-step pattern.

Styles are authored as short motifs (16 or 32 steps). This module tiles them
over the four bars of a 64-step pattern and applies role-aware, deterministic
variation so that no bar is a literal repeat: small displacements in bars 2
and 3, and a fill in bar 4. Every edit stays inside the hardware's vocabulary
(on / accent / flam / roll).
"""

from engine import (
    ON, STEPS, GLOBAL_ACCENT, bar, set_step, tile, voices_of, rng,
)

PROMOTE_ACCENT = {"x": "X", "f": "F", "r": "R"}
PROMOTE_FLAM = {"x": "f", "X": "F"}
PROMOTE_ROLL = {"x": "r", "X": "R"}


def _apply(lane, index, table):
    ch = lane[index]
    if ch in table:
        return set_step(lane, index, table[ch])
    return lane


def _bar_slice(lane, b):
    return slice(b * 16, (b + 1) * 16)


def _vary_kick(lane, b, r, style):
    off = b * 16
    if b == 1 and r.chance(0.30):
        for s in (14, 7, 11):
            if lane[off + s] == ".":
                return set_step(lane, off + s, "x")
    if b == 3:
        if r.chance(0.50):
            for s in (14, 15, 11):
                if lane[off + s] == ".":
                    lane = set_step(lane, off + s, "x")
                    break
        if r.chance(0.20) and lane[off + 8] in ON:
            lane = set_step(lane, off + 8, ".")
    return lane


def _vary_snare(lane, b, r, style):
    off = b * 16
    if b == 1 and r.chance(0.25):
        for s in (10, 6, 14):
            if lane[off + s] == ".":
                return set_step(lane, off + s, "x")
    if b == 3:
        if "snare" in style.fills:
            for s in style.snare_fill:
                lane = set_step(lane, off + s, "x")
            lane = _apply(lane, off + style.snare_fill[-1], PROMOTE_ROLL)
        if r.chance(0.45):
            lane = _apply(lane, off + 12, PROMOTE_FLAM)
    return lane


def _vary_hat(lane, b, r, style):
    off = b * 16
    if b == 2 and r.chance(0.40):
        for s in (6, 10, 14):
            if lane[off + s] in ON and r.chance(0.5):
                lane = _apply(lane, off + s, PROMOTE_ROLL)
                break
    if b == 3 and r.chance(0.55):
        lane = _apply(lane, off + 15, PROMOTE_ROLL)
    return lane


def _vary_ohat(lane, b, r, style):
    off = b * 16
    if b in (1, 3) and r.chance(0.35):
        for s in (2, 6, 10, 14):
            if lane[off + s] == "." and lane[off + (s + 4) % 16] in ON:
                return set_step(lane, off + s, "x")
    return lane


def _vary_cym(lane, b, r, style):
    off = b * 16
    if b == 2 and r.chance(0.30) and lane[off] == ".":
        lane = set_step(lane, off, "x")
    if b == 3 and r.chance(0.25) and lane[off + 12] == ".":
        lane = set_step(lane, off + 12, "x")
    return lane


def _vary_tom(lane, b, r, style, low):
    off = b * 16
    if b == 3 and "tom" in style.fills:
        run = style.tom_fill_low if low else style.tom_fill_high
        for s in run:
            lane = set_step(lane, off + s, "x")
        if run:
            lane = _apply(lane, off + run[0], PROMOTE_ACCENT)
    if b == 1 and r.chance(0.20):
        for s in (7, 11):
            if lane[off + s] == ".":
                return set_step(lane, off + s, "x")
    return lane


CONGA_FILL = {
    "HB": (8, 10),
    "HC": (11, 12),
    "LB": (13, 14),
    "LC": (15,),
}


def _vary_conga(lane, b, r, style, key):
    off = b * 16
    if b == 3 and "conga" in style.fills:
        for s in CONGA_FILL.get(key, ()):
            lane = set_step(lane, off + s, "x")
        first = CONGA_FILL.get(key, ())
        if first:
            lane = _apply(lane, off + first[0], PROMOTE_ACCENT)
    return _vary_perc(lane, b, r, style)


def _vary_perc(lane, b, r, style):
    off = b * 16
    if b in (1, 3) and r.chance(0.30):
        cands = [s for s in range(16) if lane[off + s] == "."]
        if cands:
            lane = set_step(lane, off + r.pick(cands), "x")
    if b == 3 and r.chance(0.20):
        hits = [s for s in range(16) if lane[off + s] in ON]
        if hits:
            lane = _apply(lane, off + hits[-1], PROMOTE_FLAM)
    return lane


VARY = {
    "kick": _vary_kick,
    "snare": _vary_snare,
    "hat": _vary_hat,
    "ohat": _vary_ohat,
    "cym": _vary_cym,
    "clap": _vary_perc,
    "rim": _vary_perc,
    "bell": _vary_perc,
    "shaker": _vary_hat,
    "conga": _vary_perc,
    "perc": _vary_perc,
}


PRIORITY = ["hat", "shaker", "snare", "conga", "perc", "bell", "rim",
            "clap", "ohat", "kick", "tom", "cym"]


def _force_variation(machine, slot, style, out, vmap, b):
    """Guarantee bar `b` is not a literal repeat of bar 1.

    Some styles are dense enough that every probabilistic variation misses.
    Rather than let a bar repeat verbatim, add one deterministic edit to the
    highest-priority lane that has room for it.
    """
    r = rng(machine, slot, style.name, "force", b)
    keys = [k for k in out if k != GLOBAL_ACCENT and k in vmap]
    keys.sort(key=lambda k: (PRIORITY.index(vmap[k].role)
                             if vmap[k].role in PRIORITY else 99, k))
    off = b * 16
    for key in keys:
        lane = out[key]
        role = vmap[key].role
        if role in ("hat", "shaker"):
            for s in (14, 10, 6, 2):
                if lane[off + s] in ON:
                    out[key] = _apply(lane, off + s, PROMOTE_ROLL)
                    return True
        holes = [s for s in (14, 10, 6, 11, 7, 3) if lane[off + s] == "."]
        if holes:
            out[key] = set_step(lane, off + r.pick(holes), "x")
            return True
    return False


def develop(machine, slot, style):
    """Return {voice_key: 64-step lane} for one pattern."""
    vmap = voices_of(machine)
    out = {}
    for key, motif in style.lanes.items():
        if key == GLOBAL_ACCENT:
            out[key] = tile(motif, STEPS)
            continue
        if key not in vmap:
            raise KeyError(f"{machine} has no voice {key!r} (style {style.name})")
        lane = tile(motif, STEPS)
        if not style.strict:
            role = vmap[key].role
            r = rng(machine, slot, style.name, key)
            fn = VARY.get(role)
            if fn is _vary_tom:
                pass
            if role == "tom":
                low = key in ("LT", "LB", "LC")
                for b in range(4):
                    lane = _vary_tom(lane, b, r, style, low)
            elif role == "conga":
                for b in range(4):
                    lane = _vary_conga(lane, b, r, style, key)
            elif fn:
                for b in range(4):
                    lane = fn(lane, b, r, style)
        out[key] = lane

    if not style.strict:
        for b in (1, 2):
            same = all(bar(lane, b) == bar(lane, 0)
                       for k, lane in out.items() if k != GLOBAL_ACCENT)
            if same:
                _force_variation(machine, slot, style, out, vmap, b)

    # Toms are handled above only when present; add a fill lane if the style
    # asks for a tom fill but never stated a tom motif.
    if "conga" in style.fills and not style.strict:
        for key, v in vmap.items():
            if v.role == "conga" and key not in out and key in CONGA_FILL:
                lane = "." * STEPS
                r = rng(machine, slot, style.name, key)
                lane = _vary_conga(lane, 3, r, style, key)
                if any(c in ON for c in lane):
                    out[key] = lane

    if "tom" in style.fills and not style.strict:
        for key, v in vmap.items():
            if v.role == "tom" and key not in out:
                lane = "." * STEPS
                low = key in ("LT", "LB", "LC")
                r = rng(machine, slot, style.name, key)
                lane = _vary_tom(lane, 3, r, style, low)
                if any(c in ON for c in lane):
                    out[key] = lane
    return out
