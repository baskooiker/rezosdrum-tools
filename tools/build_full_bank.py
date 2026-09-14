#!/usr/bin/env python3
"""Write all 64 generated TT-78 patterns into a .tt78bak backup file.

    python3 tools/build_full_bank.py <base.tt78bak> <out.tt78bak>

Sections 0-3 are regenerated from out/TT-78_patterns.json; every other section
is copied through byte-for-byte. Each pattern becomes a 64-step record: 8
packets, header `80|seq 01 fe 40 00`, with even sequence numbers carrying the
pattern's four 16-step pages in sequences 0-3, and the (empty) Fill pages in
sequences 4-7. The layout is grouped, not interleaved: sequence n < PAGES is
pattern page n, sequence n >= PAGES is fill page n - PAGES. Fills are generated
by gen/fills.py.

Two constraints from the hardware are enforced:
  * Guiro, Low/High Bongo, Cowbell and Clave are single-bit voices; accents and
    modifiers on them are downgraded to plain hits.
  * The generator's Global Accent lane has no known home in the format, so it is
    folded into per-voice accents on the voices that can hold one.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclone_sysex import split_messages, unpack6
from write_backup import build_message, checksum
from tt78_pattern import (VOICES, SIMPLE_VOICES, write_voice, set_step_word,
                          step_word)

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "gen"))
from fills import make_fill

USED_HDR_64 = bytes([0x01, 0xFE, 0x40, 0x00])   # data[1..4] for a used 64-step pattern
PAGES = 4
PACKETS_PER_PATTERN = PAGES * 2
DATA_LEN = 70

# generator voice key -> machine voice key
ALIAS = {"GS": "GU", "GL": "GU"}
PLAIN = {"X": "x", "F": "x", "R": "x", "f": "x", "r": "x", "x": "x", ".": "."}
ACCENT_OF = {"x": "X", "f": "F", "r": "R"}


def lanes_for(pattern):
    """Return {machine voice: 64-char lane}, hardware-legal."""
    ga = pattern["lanes"].get("GA", "." * 64)
    out = {v: ["."] * 64 for v in VOICES}
    stats = {"downgraded": 0, "ga_folded": 0}
    for key, lane in pattern["lanes"].items():
        if key == "GA":
            continue
        v = ALIAS.get(key, key)
        if v not in VOICES:
            continue
        for s, ch in enumerate(lane):
            if ch == ".":
                continue
            if v in SIMPLE_VOICES:
                if ch != "x":
                    stats["downgraded"] += 1
                new = "x"
            else:
                new = ch
                if ga[s] != "." and new in ACCENT_OF:
                    new = ACCENT_OF[new]
                    stats["ga_folded"] += 1
            # merge (guiro short+long both map to GU)
            prev = out[v][s]
            out[v][s] = new if prev == "." else max(prev, new, key="xXfFrR".index)
    return {v: "".join(c) for v, c in out.items()}, stats


def make_packets(serial, section, index, lanes, fill_lanes):
    """Return the 8 decoded payloads for one 64-step pattern plus its Fill."""
    packets = []
    for seq in range(PACKETS_PER_PATTERN):
        data = bytearray(DATA_LEN)
        data[0] = 0x80 | seq
        data[1:5] = USED_HDR_64
        src = lanes if seq < PAGES else fill_lanes
        page = seq if seq < PAGES else seq - PAGES
        for s in range(16):
            step = page * 16 + s
            w = step_word(data, s)
            for v in VOICES:
                w = write_voice(w, v, src[v][step])
            data = bytearray(set_step_word(data, s, w))
        dec = bytearray(serial) + bytes([section, index]) + data
        dec[-1] = checksum(dec)
        packets.append(bytes(dec))
    return packets


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    base_path, out_path = sys.argv[1], sys.argv[2]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bank = json.load(open(os.path.join(root, "out", "TT-78_patterns.json")))
    by_slot = {p["slot"]: p for p in bank["patterns"]}

    raw = open(base_path, "rb").read()
    msgs = split_messages(raw)
    serial = unpack6(msgs[0][6:-1])[0:4]

    out = bytearray()
    done = set()
    totals = {"downgraded": 0, "ga_folded": 0}
    written = 0
    for m in msgs:
        dec = unpack6(m[6:-1])
        section, index = dec[4], dec[5]
        if section not in (0, 1, 2, 3):
            out += m
            continue
        if (section, index) in done:
            continue                            # originals replaced wholesale
        done.add((section, index))
        slot = section * 16 + index + 1
        lanes, stats = lanes_for(by_slot[slot])
        fill_lanes = make_fill(lanes, slot, by_slot[slot]["name"])
        for k in totals:
            totals[k] += stats[k]
        for dec_new in make_packets(serial, section, index, lanes, fill_lanes):
            out += build_message(m[4], m[5], dec_new)
        written += 1

    open(out_path, "wb").write(bytes(out))
    print(f"base    : {base_path}  {len(raw)} bytes, {len(msgs)} packets")
    print(f"written : {out_path}  {len(out)} bytes")
    print(f"patterns: {written} (expect 64), {written * PACKETS_PER_PATTERN} pattern packets")
    print(f"modifiers downgraded on single-bit voices: {totals['downgraded']}")
    print(f"global-accent hits folded into voice accents: {totals['ga_folded']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
