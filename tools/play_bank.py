#!/usr/bin/env python3
"""Play the generated patterns straight into a TT-606 / TT-78 over MIDI.

The drum machines respond to Note On for every instrument in all four of
their modes, so this drives the voices live without touching pattern memory.
Velocity >= 112 is read as an accented strike by the machine.

    pip install mido python-rtmidi

    python3 tools/play_bank.py --list
    python3 tools/play_bank.py --machine TT-606 --port "USB MIDI" --slot 5
    python3 tools/play_bank.py --machine TT-78  --port "USB MIDI" --all
    python3 tools/play_bank.py --machine TT-606 --port "USB MIDI" --probe

--probe plays a plain kick/snare/hat loop so you can check whether the
machine writes incoming notes into the selected pattern while it is in
Pattern Write mode with the sequencer running. If it does, that is a much
easier route than SysEx (see tools/README.md).
"""

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "out")

ON = set("xXfFrR")
ACCENT = set("XFR")
FLAM = set("fF")
ROLL = set("rR")
VEL_NORMAL = 100
VEL_ACCENT = 127
VEL_GRACE = 90


def load(machine):
    path = os.path.join(OUT, f"{machine}_patterns.json")
    if not os.path.exists(path):
        sys.exit(f"{path} not found — run gen/build.py first")
    return json.load(open(path))


def schedule(bank, pattern):
    """Return [(step_fraction, note, velocity)] sorted by time, in steps."""
    voices = bank["voices"]
    ga = pattern["lanes"].get("GA", "." * 64)
    events = []
    for key, lane in pattern["lanes"].items():
        if key == "GA":
            continue
        note = voices[key]["note"]
        for step, ch in enumerate(lane):
            if ch not in ON:
                continue
            vel = VEL_ACCENT if (ch in ACCENT or ga[step] in ON) else VEL_NORMAL
            if ch in FLAM:
                events.append((step - 1 / 3, note, VEL_GRACE))
            events.append((float(step), note, vel))
            if ch in ROLL:
                events.append((step + 0.5, note, vel))
    events.sort()
    return events


def cc_setup(bank, pattern):
    out = []
    if pattern.get("flam_time") is not None:
        out.append((17, pattern["flam_time"]))
    if pattern.get("shuffle") is not None:
        out.append((18, pattern["shuffle"]))
    voices = bank["voices"]
    for key, spec in sorted((pattern.get("kit") or {}).items()):
        v = voices[key]
        for field, num in (("tone", v["tone_cc"]), ("shape", v["shape_cc"]),
                           ("amount", v["amount_cc"]), ("sel", v["select_cc"])):
            if field in spec and num:
                out.append((num, spec[field]))
    return out


def play(port, bank, pattern, channel, repeats, send_cc=True):
    import mido
    step_seconds = 60.0 / pattern["tempo"] / 4
    if send_cc:
        for num, val in cc_setup(bank, pattern):
            port.send(mido.Message("control_change", channel=channel,
                                   control=num, value=max(0, min(127, val))))
    events = schedule(bank, pattern)
    print(f"P{pattern['slot']:02d} {pattern['name']} — {pattern['tempo']} BPM, "
          f"{len(events)} strikes/loop, {repeats}x")
    for _ in range(repeats):
        t0 = time.perf_counter()
        for offset, note, vel in events:
            target = t0 + max(0.0, offset) * step_seconds
            now = time.perf_counter()
            if target > now:
                time.sleep(target - now)
            port.send(mido.Message("note_on", channel=channel, note=note,
                                   velocity=vel))
            port.send(mido.Message("note_off", channel=channel, note=note,
                                   velocity=0))
        rest = t0 + 64 * step_seconds - time.perf_counter()
        if rest > 0:
            time.sleep(rest)


PROBE = {
    "slot": 0, "name": "PROBE kick/snare/hat", "tempo": 120, "kit": {},
    "flam_time": None, "shuffle": None,
    "lanes": {
        "BD": "x...x...x...x..." * 4,
        "SD": "....x.......x..." * 4,
        "CH": "x.x.x.x.x.x.x.x." * 4,
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--machine", choices=["TT-606", "TT-78"])
    ap.add_argument("--port", help="substring of the MIDI output port name")
    ap.add_argument("--list", action="store_true", help="list MIDI ports and exit")
    ap.add_argument("--slot", type=int, help="play a single pattern (1-64)")
    ap.add_argument("--all", action="store_true", help="play all 64 in order")
    ap.add_argument("--probe", action="store_true",
                    help="play a plain loop to test MIDI-note recording")
    ap.add_argument("--repeats", type=int, default=4)
    ap.add_argument("--channel", type=int, default=1,
                    help="MIDI channel 1-16 (machine default is 1)")
    args = ap.parse_args()

    try:
        import mido
    except ImportError:
        sys.exit("mido not installed — pip install mido python-rtmidi")

    if args.list:
        for name in mido.get_output_names():
            print(name)
        return

    if not args.machine or not args.port:
        sys.exit("--machine and --port are required (see --list)")

    matches = [n for n in mido.get_output_names() if args.port.lower() in n.lower()]
    if not matches:
        sys.exit(f"no output port matching {args.port!r}; try --list")
    print("using port:", matches[0])

    bank = load(args.machine)
    channel = max(0, min(15, args.channel - 1))
    with mido.open_output(matches[0]) as port:
        try:
            if args.probe:
                play(port, bank, PROBE, channel, args.repeats, send_cc=False)
            elif args.all:
                for p in bank["patterns"]:
                    play(port, bank, p, channel, args.repeats)
            elif args.slot:
                p = next(x for x in bank["patterns"] if x["slot"] == args.slot)
                play(port, bank, p, channel, args.repeats)
            else:
                sys.exit("choose --slot N, --all or --probe")
        except KeyboardInterrupt:
            print("\nstopped")
        finally:
            for note in range(128):
                port.send(mido.Message("note_off", channel=channel, note=note))


if __name__ == "__main__":
    main()
