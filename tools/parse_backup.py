#!/usr/bin/env python3
"""Parse a Cyclone Studio .tt78bak / .tt606bak backup file.

A backup file is simply the concatenated SysEx stream the device sent, every
message being a command 0x14 backup packet. Each packet's payload is 6-bit
packed; decoded it begins with a 6-byte header:

    [0..3]  device serial, little-endian
    [4]     section id  ("page")
    [5]     index within the section
    [6..]   section data

Section ids observed on a TT-78 with firmware v1.0:

    0,1,2,3   bulk data, 70 data bytes per packet
    7         64 packets of 76 data bytes - one per pattern slot
    100..108  nine small sections, 14 packets of 8 bytes plus one of 10
    127       single terminating packet

    python3 tools/parse_backup.py captures/base.tt78bak
    python3 tools/parse_backup.py a.tt78bak b.tt78bak      # diff two backups
"""

import sys
import os
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclone_sysex import split_messages, unpack6


def parse(path):
    raw = open(path, "rb").read()
    packets = []
    for m in split_messages(raw):
        if len(m) < 8 or m[5] != 0x14:
            continue
        d = unpack6(m[6:-1])
        packets.append({"serial": bytes(d[0:4]), "section": d[4],
                        "index": d[5], "data": bytes(d[6:]), "raw_len": len(m)})
    return raw, packets


def summarise(path):
    raw, pk = parse(path)
    print(f"{path}: {len(raw)} bytes, {len(pk)} backup packets")
    if not pk:
        return pk
    print(f"  serial: {pk[0]['serial'].hex(' ')}")
    by = defaultdict(list)
    for p in pk:
        by[p["section"]].append(p)
    print(f"  {'section':>8} {'packets':>8} {'data/pkt':>9}")
    for s in sorted(by):
        sizes = Counter(len(p["data"]) for p in by[s])
        sz = ", ".join(f"{n}x{v}B" for v, n in sorted(sizes.items()))
        print(f"  {s:>8} {len(by[s]):>8} {sz:>9}")
    return pk


def diff(path_a, path_b):
    pa = parse(path_a)[1]
    pb = parse(path_b)[1]
    print(f"\ndiff {os.path.basename(path_a)} -> {os.path.basename(path_b)}")
    if len(pa) != len(pb):
        print(f"  packet count differs: {len(pa)} vs {len(pb)}")
    changed = 0
    for i, (a, b) in enumerate(zip(pa, pb)):
        if a["data"] == b["data"]:
            continue
        changed += 1
        bits = [(j, x, y) for j, (x, y) in enumerate(zip(a["data"], b["data"])) if x != y]
        print(f"  packet {i} section {a['section']} index {a['index']}: "
              f"{len(bits)} byte(s) differ")
        for j, x, y in bits[:12]:
            flips = [k for k in range(8) if (x ^ y) >> k & 1]
            print(f"    data[{j}] {x:02x} -> {y:02x}   bits {flips}")
    if not changed:
        print("  identical")
    else:
        print(f"  {changed} packet(s) changed")


STEP_BASE = 5          # first step block within a packet's data
STEP_STRIDE = 4        # bytes per step
STEPS_PER_PACKET = 16
STATE = {0: ".", 1: "x", 2: "f", 3: "r"}
ACCENTED = {"x": "X", "f": "F", "r": "R"}


def decode_instrument1(data):
    """Decode instrument 1's 16 steps out of one packet.

    Within each step's 4-byte block, byte 0 carries instrument 1:
        bits 0-1   state: 0 off, 1 on, 2 flam, 3 roll
        bit  2     accent
    The higher bits belong to other instruments and are not yet mapped.
    """
    out = []
    for s in range(STEPS_PER_PACKET):
        b = data[STEP_BASE + s * STEP_STRIDE]
        ch = STATE[b & 0x03]
        if (b >> 2) & 1 and ch != ".":
            ch = ACCENTED[ch]
        out.append(ch)
    return "".join(out)


def show_patterns(path, limit=8):
    pk = parse(path)[1]
    sel = [p for p in pk if p["section"] == 0 and len(p["data"]) == 70]
    print(f"\ninstrument 1 (Bass Drum), first {min(limit, len(sel))} section-0 packets:")
    for p in sel[:limit]:
        print(f"  index {p['index']:>3}  {decode_instrument1(p['data'])}")
    print("  legend: . off  x on  X on+accent  f flam  F flam+accent  r roll  R roll+accent")


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--patterns":
        summarise(sys.argv[2])
        show_patterns(sys.argv[2])
    elif len(sys.argv) == 2:
        summarise(sys.argv[1])
        show_patterns(sys.argv[1], limit=4)
    elif len(sys.argv) == 3:
        summarise(sys.argv[1])
        summarise(sys.argv[2])
        diff(sys.argv[1], sys.argv[2])
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
