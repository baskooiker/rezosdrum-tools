#!/usr/bin/env python3
"""TT-606 Drum Drone step encoding: the voice bit map, plus decode and encode.

Same container as the TT-78 - four bytes per step at data[5 + 4*(step-1)] of a
section-0 backup packet, read as a 32-bit little-endian field - but a different
voice layout, since the Drum Drone has nine voices rather than thirteen.

Each voice has two state bits and an accent bit:

    00 off    01 on    10 flam    11 roll

Eight voices keep their accent bit immediately above their state bits. The
cymbal is the exception: byte 3 is full after the two hi-hats, so the cymbal's
state sits in the two bits left at the top of it and its **accent is stored
remotely, in the spare bit 22 of byte 2**.

    byte 0   BD 0-2      SD 3-5      spare 6, 7
    byte 1   LT 8-10     HT 11-13    spare 14, 15
    byte 2   RS 16-18    CP 19-21    CY accent 22    spare 23
    byte 3   CH 24-26    OH 27-29    CY state 30-31

Every position was read from a single backup in which each of the nine voices
was placed alone in its own pattern, plain on step 1 and then accented,
flammed and rolled on steps 5, 9 and 13.
"""

# voice -> (first state bit, accent bit)
VOICES = {
    "BD": (0, 2),     # Bass Drum
    "SD": (3, 5),     # Snare Drum
    "LT": (8, 10),    # Low Tom
    "HT": (11, 13),   # High Tom
    "RS": (16, 18),   # Rim Shot
    "CP": (19, 21),   # Hand Clap
    "CH": (24, 26),   # Closed Hi-hat
    "OH": (27, 29),   # Open Hi-hat
    "CY": (30, 22),   # Cymbal - accent stored remotely
}

NAMES = {"BD": "Bass Drum", "SD": "Snare Drum", "LT": "Low Tom",
         "HT": "High Tom", "RS": "Rim Shot", "CP": "Hand Clap",
         "CH": "Closed Hi-hat", "OH": "Open Hi-hat", "CY": "Cymbal"}

#: the Drum Drone places no restrictions - every voice takes every modifier
SIMPLE_VOICES = ()

STATE = {0: ".", 1: "x", 2: "f", 3: "r"}
ACCENT_SYM = {"x": "X", "f": "F", "r": "R"}
SYM_STATE = {".": 0, "x": 1, "X": 1, "f": 2, "F": 2, "r": 3, "R": 3}
ACCENTED_SYMS = set("XFR")

STEP_BASE = 5
STEP_STRIDE = 4
STEPS_PER_PACKET = 16


def step_word(data, step_index):
    o = STEP_BASE + step_index * STEP_STRIDE
    return int.from_bytes(data[o:o + STEP_STRIDE], "little")


def set_step_word(data, step_index, word):
    o = STEP_BASE + step_index * STEP_STRIDE
    out = bytearray(data)
    out[o:o + STEP_STRIDE] = word.to_bytes(STEP_STRIDE, "little")
    return bytes(out)


def read_voice(word, voice):
    state_bit, accent_bit = VOICES[voice]
    sym = STATE[(word >> state_bit) & 0x03]
    if sym != "." and (word >> accent_bit) & 1:
        sym = ACCENT_SYM[sym]
    return sym


def write_voice(word, voice, sym):
    state_bit, accent_bit = VOICES[voice]
    word &= ~(0x03 << state_bit)
    word &= ~(1 << accent_bit)
    word |= (SYM_STATE[sym] & 0x03) << state_bit
    if sym in ACCENTED_SYMS:
        word |= 1 << accent_bit
    return word


def decode_packet(data, steps=STEPS_PER_PACKET):
    lanes = {v: [] for v in VOICES}
    for s in range(steps):
        w = step_word(data, s)
        for v in VOICES:
            lanes[v].append(read_voice(w, v))
    return {v: "".join(c) for v, c in lanes.items()}


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from parse_backup import parse

    path = sys.argv[1]
    slot = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    pk = parse(path)[1]
    sel = sorted([p for p in pk if p["section"] == 0 and p["index"] == slot - 1],
                 key=lambda p: p["data"][0] & 0x1F)
    print(f"{path}, pattern {slot}")
    for v in VOICES:
        lane = "".join(decode_packet(p["data"])[v] for p in sel[:4])
        if any(c != "." for c in lane):
            print(f"  {v} {NAMES[v]:<14} {lane}")
