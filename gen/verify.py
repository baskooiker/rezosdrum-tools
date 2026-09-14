#!/usr/bin/env python3
"""Sanity checks over the generated banks and MIDI files."""

import glob
import json
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "out")
ON = set("xXfFrR")


def read_vlq(buf, i):
    val = 0
    while True:
        b = buf[i]
        i += 1
        val = (val << 7) | (b & 0x7F)
        if not b & 0x80:
            return val, i


def parse_midi(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd", path
    _len, fmt, ntrk, ppq = struct.unpack(">IHHH", data[4:14])
    i = 14
    notes = 0
    ccs = 0
    maxtick = 0
    for _ in range(ntrk):
        assert data[i:i + 4] == b"MTrk", (path, i)
        tlen = struct.unpack(">I", data[i + 4:i + 8])[0]
        j = i + 8
        end = j + tlen
        tick = 0
        running = None
        while j < end:
            delta, j = read_vlq(data, j)
            tick += delta
            status = data[j]
            if status == 0xFF:
                j += 1
                _type = data[j]
                j += 1
                ln, j = read_vlq(data, j)
                j += ln
                continue
            if status in (0xF0, 0xF7):
                j += 1
                ln, j = read_vlq(data, j)
                j += ln
                continue
            if status & 0x80:
                running = status
                j += 1
            assert running is not None, path
            kind = running & 0xF0
            nbytes = 1 if kind in (0xC0, 0xD0) else 2
            payload = data[j:j + nbytes]
            j += nbytes
            if kind == 0x90 and payload[1] > 0:
                notes += 1
            elif kind == 0xB0:
                ccs += 1
            maxtick = max(maxtick, tick)
        assert j == end, (path, j, end)
        i = end
    return {"format": fmt, "tracks": ntrk, "ppq": ppq, "notes": notes,
            "ccs": ccs, "maxtick": maxtick}


def main():
    problems = []
    for machine in ("TT-606", "TT-78"):
        dump = json.load(open(os.path.join(OUT, f"{machine}_patterns.json")))
        notes_by_key = {k: v["note"] for k, v in dump["voices"].items()}
        assert len(dump["patterns"]) == 64

        repeats = 0
        empty = 0
        for p in dump["patterns"]:
            lanes = {k: v for k, v in p["lanes"].items() if k != "GA"}
            for k, lane in p["lanes"].items():
                if len(lane) != 64:
                    problems.append(f"{machine} P{p['slot']} {k}: length {len(lane)}")
                if k != "GA" and k not in notes_by_key:
                    problems.append(f"{machine} P{p['slot']}: unknown voice {k}")
            hits = sum(1 for lane in lanes.values() for c in lane if c in ON)
            if hits < 8:
                empty += 1
                problems.append(f"{machine} P{p['slot']} {p['name']}: only {hits} hits")
            bars = [tuple(lane[b * 16:(b + 1) * 16] for lane in lanes.values())
                    for b in range(4)]
            if len(set(bars)) == 1:
                repeats += 1
        strict = sum(1 for p in dump["patterns"] if p["slot"] and False)
        print(f"{machine}: 64 patterns, {repeats} with four identical bars, "
              f"{empty} suspiciously empty")

        mids = sorted(glob.glob(os.path.join(OUT, "midi", machine, "*.mid")))
        if len(mids) != 64:
            problems.append(f"{machine}: {len(mids)} midi files, expected 64")
        total_notes = 0
        for m in mids:
            info = parse_midi(m)
            total_notes += info["notes"]
            if info["notes"] == 0:
                problems.append(f"{m}: no notes")
            if info["maxtick"] > 64 * 24 + 24:
                problems.append(f"{m}: runs past 4 bars ({info['maxtick']} ticks)")
        bank = parse_midi(os.path.join(OUT, "midi", f"{machine}_bank_all64.mid"))
        print(f"  {len(mids)} pattern files parsed, {total_notes} note-ons; "
              f"bank file: {bank['tracks']} tracks, {bank['notes']} note-ons, "
              f"{bank['maxtick']} ticks ({bank['maxtick'] / 96 / 4:.0f} bars)")
        if bank["notes"] != total_notes:
            problems.append(f"{machine}: bank note count {bank['notes']} != "
                            f"sum of pattern files {total_notes}")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(" -", p)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
