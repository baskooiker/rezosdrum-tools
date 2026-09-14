#!/usr/bin/env python3
"""TT-78 pattern step encoding: the voice bit map, plus decode and encode.

Each step of a pattern occupies 4 bytes starting at data[5 + 4*(step-1)] of a
section-0 backup packet, read as a 32-bit little-endian bit field. Each byte
holds 3 + 3 + 1 + 1 bits: two "full" voices carrying two state bits plus an
accent bit, and two "simple" voices carrying a single on/off bit.

Full voice state: 0 off, 1 on, 2 flam, 3 roll, with accent in the bit above.
Simple voices are on/off only and cannot take accent, flam or roll.

Every position below was established by diffing backups that differ by exactly
one deliberate edit; see docs/instrument_bitmap.md for the provenance.
"""

# voice -> (first bit, is_full)
FULL = True
SIMPLE = False

VOICES = {
    "BD": (0,  FULL),    # Bass Drum
    "SD": (3,  FULL),    # Snare Drum
    "GU": (6,  SIMPLE),  # Guiro
    "LC": (8,  FULL),    # Low Conga
    "HC": (11, FULL),    # High Conga
    "LB": (14, SIMPLE),  # Low Bongo
    "HB": (15, SIMPLE),  # High Bongo
    "MA": (16, FULL),    # Maracas
    "TB": (19, FULL),    # Tambourine
    "CB": (23, SIMPLE),  # Cowbell
    "HH": (24, FULL),    # Hi-hat
    "CY": (27, FULL),    # Cymbal
    "CL": (30, SIMPLE),  # Clave
}

NAMES = {"BD": "Bass Drum", "SD": "Snare Drum", "GU": "Guiro",
         "LC": "Low Conga", "HC": "High Conga", "LB": "Low Bongo",
         "HB": "High Bongo", "MA": "Maracas", "TB": "Tambourine",
         "CB": "Cowbell", "HH": "Hi-hat", "CY": "Cymbal", "CL": "Clave"}

STATE_SYM = {0: ".", 1: "x", 2: "f", 3: "r"}
ACCENT_SYM = {"x": "X", "f": "F", "r": "R"}
SYM_STATE = {".": 0, "x": 1, "X": 1, "f": 2, "F": 2, "r": 3, "R": 3}
ACCENTED_SYMS = set("XFR")

STEP_BASE = 5
STEP_STRIDE = 4
STEPS_PER_PACKET = 16

#: voices that physically cannot carry accent, flam or roll
SIMPLE_VOICES = tuple(k for k, (_, full) in VOICES.items() if not full)


def step_word(data, step_index):
    """Read one step's 32-bit field out of a packet's data (0-based step)."""
    o = STEP_BASE + step_index * STEP_STRIDE
    return int.from_bytes(data[o:o + STEP_STRIDE], "little")


def set_step_word(data, step_index, word):
    o = STEP_BASE + step_index * STEP_STRIDE
    out = bytearray(data)
    out[o:o + STEP_STRIDE] = word.to_bytes(STEP_STRIDE, "little")
    return bytes(out)


def read_voice(word, voice):
    """Return the symbol for one voice in one step."""
    bit, full = VOICES[voice]
    if not full:
        return "x" if (word >> bit) & 1 else "."
    state = (word >> bit) & 0x03
    sym = STATE_SYM[state]
    if sym != "." and (word >> (bit + 2)) & 1:
        sym = ACCENT_SYM[sym]
    return sym


def write_voice(word, voice, sym):
    """Return `word` with one voice's step set from a notation symbol.

    Raises ValueError if a modifier or accent is asked of a simple voice.
    """
    bit, full = VOICES[voice]
    if not full:
        if sym in ACCENTED_SYMS or sym in ("f", "r"):
            raise ValueError(
                f"{voice} ({NAMES[voice]}) is a single-bit voice and cannot "
                f"take accent, flam or roll; got {sym!r}")
        word &= ~(1 << bit)
        if sym == "x":
            word |= 1 << bit
        return word
    word &= ~(0x07 << bit)
    state = SYM_STATE[sym]
    word |= (state & 0x03) << bit
    if sym in ACCENTED_SYMS:
        word |= 1 << (bit + 2)
    return word


def decode_packet(data, steps=STEPS_PER_PACKET):
    """Return {voice: symbol string} for one packet."""
    lanes = {v: [] for v in VOICES}
    for s in range(steps):
        w = step_word(data, s)
        for v in VOICES:
            lanes[v].append(read_voice(w, v))
    return {v: "".join(c) for v, c in lanes.items()}


if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from parse_backup import parse

    path = sys.argv[1] if len(sys.argv) > 1 else "captures/base.tt78bak"
    slot = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    pk = parse(path)[1]
    sel = [p for p in pk if p["section"] == 0 and p["index"] == slot - 1]
    if not sel:
        sys.exit(f"no packets for pattern {slot}")
    print(f"{path}, pattern {slot} ({len(sel)} packets)\n")
    for n, p in enumerate(sel):
        lanes = decode_packet(p["data"])
        print(f"  packet {n} (steps {n // 2 * 16 + 1}-{n // 2 * 16 + 16}, "
              f"sub {p['data'][0] & 1}):")
        for v in VOICES:
            if any(c != "." for c in lanes[v]):
                print(f"    {v}  {NAMES[v]:<12} {lanes[v]}")
        print()
