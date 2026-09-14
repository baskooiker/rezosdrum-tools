#!/usr/bin/env python3
"""Rebuild and modify Cyclone .tt78bak backup files.

Checksum, established across 22 backup files and ~11,500 packets with no
exceptions outside the short section-100+ records:

    decoded[-1] = sum(decoded[4:-1]) & 0xFF

The sum starts at the section byte, so the four serial bytes are excluded.
The 19-byte records in sections 100-108 follow a different rule; they are never
modified here and are passed through untouched.

    python3 tools/write_backup.py --verify captures/base.tt78bak
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclone_sysex import HEADER, SYSEX_END, pack6, split_messages, unpack6

SHORT_RECORD_LEN = 19       # section 100+ records, different checksum rule


def checksum(decoded):
    """The trailer byte for a decoded payload."""
    return sum(decoded[4:-1]) & 0xFF


def build_message(product, command, decoded):
    """Re-encode a decoded payload into a complete SysEx message."""
    return (HEADER + bytes([product, command]) + pack6(decoded)
            + bytes([SYSEX_END]))


def rebuild(raw, edit=None):
    """Re-encode every packet of a backup file.

    `edit(index, decoded) -> decoded or None` may return a replacement payload.
    Checksums are recomputed for any payload that is long enough to have one.
    """
    out = bytearray()
    for i, m in enumerate(split_messages(raw)):
        dec = bytearray(unpack6(m[6:-1]))
        if edit is not None and len(m) != SHORT_RECORD_LEN:
            new = edit(i, bytes(dec))
            if new is not None:
                dec = bytearray(new)
                dec[-1] = checksum(dec)
        out += build_message(m[4], m[5], bytes(dec))
    return bytes(out)


def verify(path):
    raw = open(path, "rb").read()
    again = rebuild(raw)
    same = again == raw
    print(f"{path}: {len(raw)} bytes")
    print(f"  rebuilt {len(again)} bytes, byte-identical: {same}")
    if not same:
        n = sum(1 for a, b in zip(raw, again) if a != b)
        first = next(i for i, (a, b) in enumerate(zip(raw, again)) if a != b)
        print(f"  {n} bytes differ, first at offset {first}")
        return 1
    # and the checksum rule itself
    bad = 0
    total = 0
    for m in split_messages(raw):
        if len(m) == SHORT_RECORD_LEN:
            continue
        dec = unpack6(m[6:-1])
        total += 1
        if checksum(dec) != dec[-1]:
            bad += 1
    print(f"  checksum rule holds on {total - bad}/{total} long packets")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--verify":
        sys.exit(verify(sys.argv[2]))
    print(__doc__)
