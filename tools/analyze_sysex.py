#!/usr/bin/env python3
"""Compare SysEx captures to locate where pattern data lives.

No extra dependencies. Give it two or more .syx captures that differ by one
known edit and it reports exactly which bytes and bits moved.

    python3 tools/analyze_sysex.py captures/*.syx
    python3 tools/analyze_sysex.py captures/empty.syx captures/bd_step1.syx --bits

Suggested protocol (see tools/README.md):
  1. clear pattern P1, back up            -> empty.syx
  2. add BD on step 1 only, back up       -> bd_step1.syx
  3. add BD on step 2 as well, back up    -> bd_step12.syx
  4. accent step 1, back up               -> bd_step1_accent.syx
Each diff should isolate one bit, which pins down the step bitmap, the
per-instrument stride and where the accent/flam/roll planes sit.
"""

import argparse
import sys


def split_messages(data):
    msgs = []
    i = 0
    while i < len(data):
        if data[i] != 0xF0:
            i += 1
            continue
        j = data.find(0xF7, i)
        if j == -1:
            msgs.append(data[i:])
            break
        msgs.append(data[i:j + 1])
        i = j + 1
    return msgs


def describe(name, data):
    msgs = split_messages(data)
    lens = {}
    for m in msgs:
        lens[len(m)] = lens.get(len(m), 0) + 1
    print(f"{name}: {len(data)} bytes, {len(msgs)} messages")
    for ln in sorted(lens):
        print(f"    {lens[ln]:>4} x {ln} bytes")
    if msgs:
        head = msgs[0]
        print(f"    first message header: {head[:10].hex(' ')}")
        if len(msgs) > 1:
            print(f"    last  message header: {msgs[-1][:10].hex(' ')}")
    return msgs


def diff(a, b, name_a, name_b, show_bits):
    print(f"\ndiff {name_a} -> {name_b}")
    if len(a) != len(b):
        print(f"  length differs: {len(a)} vs {len(b)} — "
              f"comparing the common prefix")
    n = min(len(a), len(b))
    changes = [(i, a[i], b[i]) for i in range(n) if a[i] != b[i]]
    if not changes:
        print("  identical over the common prefix")
        return
    print(f"  {len(changes)} byte(s) differ")
    runs = []
    for i, x, y in changes:
        if runs and i == runs[-1][-1][0] + 1:
            runs[-1].append((i, x, y))
        else:
            runs.append([(i, x, y)])
    for run in runs[:40]:
        first = run[0][0]
        print(f"  offset 0x{first:04X} ({first}) — {len(run)} byte(s)")
        for i, x, y in run[:16]:
            line = f"    [{i}] {x:02X} -> {y:02X}"
            if show_bits:
                bits = [k for k in range(7) if (x ^ y) >> k & 1]
                line += f"   bits {bits}   {x:07b} -> {y:07b}"
            print(line)
    if len(runs) > 40:
        print(f"  ... and {len(runs) - 40} more runs")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--bits", action="store_true", help="show which bits flipped")
    args = ap.parse_args()

    blobs = []
    for path in args.files:
        data = open(path, "rb").read()
        describe(path, data)
        blobs.append((path, data))
        print()

    for (na, a), (nb, b) in zip(blobs, blobs[1:]):
        diff(a, b, na, nb, args.bits)

    if len(blobs) > 2:
        print("\nbytes that never change across all captures are structural "
              "(header, ids, padding); bytes that change in every diff are "
              "likely a checksum.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
