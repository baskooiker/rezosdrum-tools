#!/usr/bin/env python3
"""RezOSDrum SysEx codec for the Cyclone TT-606 / TT-78.

Frame and encoding reverse-engineered from Cyclone Studio 2.0; see
docs/PROTOCOL.md for where each piece comes from and how confident it is.

    python3 tools/cyclone_sysex.py --selftest
    python3 tools/cyclone_sysex.py --show-discovery
    python3 tools/cyclone_sysex.py --send-discovery hw:2,0,0
    python3 tools/cyclone_sysex.py --decode captures/first.syx
"""

import argparse
import subprocess
import sys

HEADER = bytes([0xF0, 0x00, 0x01, 0x7A])
SYSEX_END = 0xF7

PRODUCT_WILDCARD = 0x00
PRODUCT_TT606 = 0x08          # inferred
PRODUCT_TT78 = 0x09           # confirmed on the wire
PRODUCT_NAMES = {0x00: "wildcard", 0x08: "TT-606 (inferred)", 0x09: "TT-78"}

CMD_10 = 0x10
CMD_EVENT = 0x12              # device to host, seen on front-panel activity
CMD_CONTROL = 0x13
CMD_BACKUP_PACKET = 0x14      # device to host, per validateBackupPacket
CMD_NAMES = {0x10: "cmd10", 0x12: "event", 0x13: "control", 0x14: "backup-packet"}

OFF_PRODUCT = 4
OFF_COMMAND = 5
OFF_SUBCOMMAND = 18           # within the 22-byte cmd 0x13 control frame


# --- 6-bit payload packing --------------------------------------------------
# Cyclone packs two payload bytes into three SysEx bytes: the low 6 bits of each
# byte take a slot of their own, and the high 2 bits of both are collected into
# a third byte. Read from the packing loop at 0x406330.

def pack6(data):
    """Encode payload bytes as 6-bit-packed SysEx data bytes."""
    out = bytearray()
    for i in range(0, len(data), 2):
        b0 = data[i]
        b1 = data[i + 1] if i + 1 < len(data) else 0
        out.append(b0 & 0x3F)
        out.append(b1 & 0x3F)
        out.append(((b1 >> 6) & 0x03) << 2 | ((b0 >> 6) & 0x03))
    return bytes(out)


def unpack6(data):
    """Decode 6-bit-packed SysEx data bytes back to payload bytes."""
    out = bytearray()
    for i in range(0, len(data) - 2, 3):
        o0, o1, o2 = data[i], data[i + 1], data[i + 2]
        out.append(o0 | ((o2 & 0x03) << 6))
        out.append(o1 | (((o2 >> 2) & 0x03) << 6))
    return bytes(out)


# --- frames -----------------------------------------------------------------

def build_frame(product, command, body=b""):
    return HEADER + bytes([product, command]) + bytes(body) + bytes([SYSEX_END])


def discovery_frame(product=PRODUCT_WILDCARD):
    """Studio's startup poll: cmd 0x13, sub 0x01, everything else zero.

    Reconstructed from the builder at 0x406526. The frame is 22 bytes, so the
    body is 16 bytes sitting between the command and the F7 terminator.
    """
    body = bytearray(15)                # 4 header + product + cmd + 15 + F7 = 22
    body[OFF_SUBCOMMAND - 6] = 0x01     # frame offset 18
    body[20 - 6] = 0x01                 # frame offset 20, fixed in every builder
    return build_frame(product, CMD_CONTROL, body)


def split_messages(raw):
    msgs, i = [], 0
    while i < len(raw):
        if raw[i] == 0xF0:
            j = raw.find(b"\xF7", i)
            if j == -1:
                break
            msgs.append(raw[i:j + 1])
            i = j + 1
        else:
            i += 1
    return msgs


def describe(msg):
    if len(msg) < 6 or msg[:4] != HEADER:
        return f"{len(msg):>4}B  not a Cyclone frame: {msg[:8].hex(' ')}"
    product, command = msg[OFF_PRODUCT], msg[OFF_COMMAND]
    bits = [f"{len(msg):>4}B",
            f"product={product:#04x} ({PRODUCT_NAMES.get(product, '?')})",
            f"cmd={command:#04x} ({CMD_NAMES.get(command, '?')})"]
    if command == CMD_CONTROL and len(msg) > OFF_SUBCOMMAND:
        bits.append(f"sub={msg[OFF_SUBCOMMAND]:#04x}")
    body = msg[6:-1]
    if command == CMD_BACKUP_PACKET:
        bits.append(f"payload={len(unpack6(body))}B decoded")
    return "  ".join(bits)


# --- entry points -----------------------------------------------------------

def selftest():
    import os
    ok = True
    for n in range(0, 64):
        data = bytes((i * 37 + 11) & 0xFF for i in range(n))
        packed = pack6(data)
        back = unpack6(packed)[:len(data)]
        if back != data:
            print(f"FAIL round-trip at length {n}")
            ok = False
            break
        if any(b > 0x7F for b in packed):
            print(f"FAIL packed byte out of 7-bit range at length {n}")
            ok = False
            break
    # every byte value survives
    data = bytes(range(256))
    if unpack6(pack6(data))[:256] != data:
        print("FAIL full byte-range round-trip")
        ok = False
    f = discovery_frame()
    if len(f) != 22 or f[OFF_SUBCOMMAND] != 0x01 or f[-1] != 0xF7:
        print(f"FAIL discovery frame shape: {f.hex(' ')}")
        ok = False
    print("pack6/unpack6 round-trip: OK" if ok else "SELFTEST FAILED")
    print("discovery frame:", f.hex(" "))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--show-discovery", action="store_true")
    ap.add_argument("--send-discovery", metavar="PORT",
                    help="send the discovery poll via amidi, e.g. hw:2,0,0")
    ap.add_argument("--decode", metavar="FILE", help="describe frames in a capture")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.show_discovery:
        print(discovery_frame().hex(" ").upper())
        return 0
    if args.decode:
        raw = open(args.decode, "rb").read()
        msgs = split_messages(raw)
        print(f"{len(raw)} bytes, {len(msgs)} sysex messages")
        for k, m in enumerate(msgs):
            print(f"  [{k:>3}] {describe(m)}")
        return 0
    if args.send_discovery:
        frame = discovery_frame()
        hexs = frame.hex(" ").upper()
        print("sending:", hexs)
        r = subprocess.run(["amidi", "-p", args.send_discovery, "-S", hexs,
                            "-r", "/dev/stdout", "-t", "5"],
                           capture_output=True)
        if r.returncode != 0:
            print(r.stderr.decode(errors="replace").strip())
            return 1
        if not r.stdout:
            print("no reply")
            return 0
        for m in split_messages(r.stdout):
            print("  reply:", describe(m))
            print("        ", m.hex(" "))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
