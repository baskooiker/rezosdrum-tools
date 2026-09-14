#!/usr/bin/env python3
"""Record SysEx from a TT-606 / TT-78 so the pattern format can be decoded.

    pip install mido python-rtmidi

    python3 tools/capture_sysex.py --list
    python3 tools/capture_sysex.py --port "USB MIDI" --out captures/base.syx

Leave it running, then trigger a dump on the other side:
  * Cyclone Studio -> Backup  (full memory dump), or
  * a pattern-clone COPY from the machine ([FUNC]+[COPY] with the two units
    cabled MIDI-Out-to-MIDI-In both ways) — a much smaller message and the
    easier decoding target.

Writes the raw bytes to <out> and a per-message hex log to <out>.jsonl.
"""

import argparse
import json
import sys
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", help="substring of the MIDI input port name")
    ap.add_argument("--out", default="capture.syx")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--quiet-seconds", type=float, default=4.0,
                    help="stop after this long with no SysEx (0 = run until Ctrl-C)")
    args = ap.parse_args()

    try:
        import mido
    except ImportError:
        sys.exit("mido not installed — pip install mido python-rtmidi")

    if args.list:
        for name in mido.get_input_names():
            print(name)
        return
    if not args.port:
        sys.exit("--port is required (see --list)")

    matches = [n for n in mido.get_input_names() if args.port.lower() in n.lower()]
    if not matches:
        sys.exit(f"no input port matching {args.port!r}; try --list")
    print("listening on:", matches[0])
    print("trigger the dump now; Ctrl-C to stop")

    raw = bytearray()
    log = []
    last = None
    started = time.time()
    try:
        with mido.open_input(matches[0]) as port:
            while True:
                for msg in port.iter_pending():
                    if msg.type != "sysex":
                        continue
                    payload = bytes([0xF0]) + bytes(msg.data) + bytes([0xF7])
                    raw += payload
                    log.append({"t": round(time.time() - started, 4),
                                "len": len(payload),
                                "hex": payload.hex()})
                    last = time.time()
                    print(f"  msg {len(log):>4}  {len(payload):>6} bytes  "
                          f"{payload[:12].hex(' ')} ...")
                if last and args.quiet_seconds and \
                        time.time() - last > args.quiet_seconds:
                    print("quiet — stopping")
                    break
                time.sleep(0.005)
    except KeyboardInterrupt:
        print("\ninterrupted")

    if not raw:
        sys.exit("no SysEx captured")
    with open(args.out, "wb") as fh:
        fh.write(raw)
    with open(args.out + ".jsonl", "w") as fh:
        for entry in log:
            fh.write(json.dumps(entry) + "\n")
    print(f"wrote {len(raw)} bytes in {len(log)} messages -> {args.out}")


if __name__ == "__main__":
    main()
