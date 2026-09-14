"""Style container plus the MIDI and chart exporters."""

import struct

from engine import (
    ACCENTED, FLAMMED, FLAM_OFFSET, GLOBAL_ACCENT, NOTE_LEN, ON, PPQ,
    ROLLED, ROLL_OFFSET, STEPS, TICKS_PER_STEP, VEL_ACCENT, VEL_FLAM_GRACE,
    VEL_NORMAL, CC_AUTOFILL, CC_FLAM_TIME, CC_SHUFFLE, voices_of,
)


class Style:
    def __init__(self, name, tempo, lanes, family="", notes="", kit=None,
                 shuffle=None, flam_time=None, autofill=None, fills=(),
                 strict=False, snare_fill=(12, 13, 14, 15),
                 tom_fill_high=(8, 10, 12), tom_fill_low=(13, 14, 15)):
        self.name = name
        self.family = family
        self.tempo = tempo
        self.notes = notes
        self.lanes = lanes
        self.kit = kit or {}
        self.shuffle = shuffle
        self.flam_time = flam_time
        self.autofill = autofill
        self.fills = list(fills)
        self.strict = strict
        self.snare_fill = list(snare_fill)
        self.tom_fill_high = list(tom_fill_high)
        self.tom_fill_low = list(tom_fill_low)


# --------------------------------------------------------------------------
# MIDI writing
# --------------------------------------------------------------------------

def _vlq(value):
    out = [value & 0x7F]
    value >>= 7
    while value:
        out.append((value & 0x7F) | 0x80)
        value >>= 7
    return bytes(reversed(out))


def _events(style, lanes, machine, channel=0):
    """Return a list of (tick, order, bytes) MIDI events for one pattern."""
    vmap = voices_of(machine)
    ev = []

    def cc(number, value):
        ev.append((0, 0, bytes([0xB0 | channel, number & 0x7F, max(0, min(127, value))])))

    if style.flam_time is not None:
        cc(CC_FLAM_TIME, style.flam_time)
    if style.shuffle is not None:
        cc(CC_SHUFFLE, style.shuffle)
    if style.autofill is not None:
        cc(CC_AUTOFILL, style.autofill)
    for key in sorted(style.kit):
        v = vmap[key]
        spec = style.kit[key]
        for field, number in (("tone", v.tone_cc), ("shape", v.shape_cc),
                              ("amount", v.amount_cc), ("sel", v.select_cc)):
            if field in spec and number is not None:
                cc(number, spec[field])

    ga = lanes.get(GLOBAL_ACCENT, "." * STEPS)

    def emit(note, tick, vel):
        tick = max(0, tick)
        ev.append((tick, 1, bytes([0x90 | channel, note, vel])))
        ev.append((tick + NOTE_LEN, 2, bytes([0x80 | channel, note, 0])))

    for key, lane in lanes.items():
        if key == GLOBAL_ACCENT:
            continue
        note = vmap[key].note
        for step, ch in enumerate(lane):
            if ch not in ON:
                continue
            accent = ch in ACCENTED or ga[step] in ON
            vel = VEL_ACCENT if accent else VEL_NORMAL
            tick = step * TICKS_PER_STEP
            if ch in FLAMMED:
                emit(note, tick - FLAM_OFFSET, VEL_FLAM_GRACE)
            emit(note, tick, vel)
            if ch in ROLLED:
                emit(note, tick + ROLL_OFFSET, vel)
    return ev


def _track_bytes(events, tempo_bpm=None, name=None, end=True):
    data = bytearray()
    if name:
        payload = name.encode("ascii", "replace")[:127]
        data += _vlq(0) + b"\xFF\x03" + _vlq(len(payload)) + payload
    if tempo_bpm:
        us = int(round(60_000_000 / tempo_bpm))
        data += _vlq(0) + b"\xFF\x51\x03" + us.to_bytes(3, "big")
    last = 0
    for tick, _order, payload in events:
        data += _vlq(tick - last) + payload
        last = tick
    if end:
        data += _vlq(0) + b"\xFF\x2F\x00"
    return bytes(data)


def _smf(tracks, fmt=0):
    out = b"MThd" + struct.pack(">IHHH", 6, fmt, len(tracks), PPQ)
    for t in tracks:
        out += b"MTrk" + struct.pack(">I", len(t)) + t
    return out


def write_pattern_midi(path, machine, slot, style, lanes):
    ev = sorted(_events(style, lanes, machine), key=lambda e: (e[0], e[1]))
    name = f"{machine} P{slot:02d} {style.name}"
    with open(path, "wb") as fh:
        fh.write(_smf([_track_bytes(ev, style.tempo, name)]))


def write_bank_midi(path, machine, patterns):
    """All 64 patterns back to back in one file, 4 bars each."""
    ev = []
    offset = 0
    span = STEPS * TICKS_PER_STEP
    meta = bytearray()
    last_meta = 0
    for slot, style, lanes in patterns:
        label = f"P{slot:02d} {style.name}".encode("ascii", "replace")
        meta += _vlq(offset - last_meta) + b"\xFF\x06" + _vlq(len(label)) + label
        last_meta = offset
        us = int(round(60_000_000 / style.tempo))
        meta += _vlq(0) + b"\xFF\x51\x03" + us.to_bytes(3, "big")
        for tick, order, payload in _events(style, lanes, machine):
            ev.append((tick + offset, order, payload))
        offset += span
    meta += _vlq(0) + b"\xFF\x2F\x00"
    ev.sort(key=lambda e: (e[0], e[1]))
    track0 = _track_bytes([], None, f"{machine} pattern bank") [:-4] + bytes(meta)
    track1 = _track_bytes(ev, None, f"{machine} drums")
    with open(path, "wb") as fh:
        fh.write(_smf([track0, track1], fmt=1))


# --------------------------------------------------------------------------
# Chart writing
# --------------------------------------------------------------------------

LEGEND = (
    "`.` off   `x` on   `X` accent   `f` flam   `F` flam+accent   "
    "`r` roll   `R` roll+accent"
)


def chart_lines(machine, slot, style, lanes):
    vmap = voices_of(machine)
    order = [v.key for v in vmap.values()]
    keys = [k for k in order if k in lanes and any(c in ON for c in lanes[k])]
    if GLOBAL_ACCENT in lanes and any(c in ON for c in lanes[GLOBAL_ACCENT]):
        keys.append(GLOBAL_ACCENT)

    lines = []
    lines.append(f"### P{slot:02d} — {style.name}")
    head = f"*{style.family} · {style.tempo} BPM · 64 steps · 16th-note scale"
    if style.shuffle:
        head += f" · shuffle {style.shuffle}"
    if style.flam_time is not None:
        head += f" · flam time {style.flam_time}"
    lines.append(head + "*")
    if style.notes:
        lines.append("")
        lines.append(style.notes)
    lines.append("")
    lines.append("```")
    lines.append("        page 1 (1-16)    page 2 (17-32)   page 3 (33-48)   page 4 (49-64)")
    for key in keys:
        label = "ACC*" if key == GLOBAL_ACCENT else key
        lane = lanes[key]
        cells = " ".join(lane[b * 16:(b + 1) * 16] for b in range(4))
        lines.append(f"  {label:<5} {cells}")
    lines.append("```")
    if GLOBAL_ACCENT in keys:
        lines.append("`ACC*` = Global Accent lane ([FUNC]+[ACCENT]) — accents every voice on those steps.")
    if style.kit:
        lines.append("")
        lines.append("Voice settings:")
        for key in sorted(style.kit):
            v = vmap[key]
            spec = style.kit[key]
            bits = []
            if "sel" in spec:
                bits.append(f"variation {spec['sel']} (CC{v.select_cc}={spec['sel']})")
            if "tone" in spec:
                bits.append(f"tone CC{v.tone_cc}={spec['tone']}")
            if "shape" in spec:
                bits.append(f"nuance shape CC{v.shape_cc}={spec['shape']}")
            if "amount" in spec:
                bits.append(f"nuance amount CC{v.amount_cc}={spec['amount']}")
            lines.append(f"- **{v.name} ({key})** — " + ", ".join(bits))
    lines.append("")
    return lines
