#!/usr/bin/env python3
"""Build the pattern banks: step charts, MIDI files and a JSON dump.

Usage:  python3 gen/build.py [output_dir]
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import GLOBAL_ACCENT, ON, STEPS, voices_of
from develop import develop
from enrich import enrich


def role_map(machine):
    """voice key -> enrichment role, splitting toms and hand drums by pitch."""
    out = {}
    for key, v in voices_of(machine).items():
        role = v.role
        if role in ("tom", "conga"):
            role = "tom_hi" if key[0] == "H" else "tom_lo"
        out[key] = role
    return out
from export import LEGEND, chart_lines, write_bank_midi, write_pattern_midi
from styles_tt606 import TT606_STYLES
from styles_tt78 import TT78_STYLES
from page_order import TT606_ORDER, TT78_ORDER, PAGE_TITLES, reorder

BANKS = [("TT-606", reorder(TT606_STYLES, TT606_ORDER, "TT-606")),
         ("TT-78", reorder(TT78_STYLES, TT78_ORDER, "TT-78"))]
PAGE_COLOURS = ["Red", "Yellow", "Green", "Blue"]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build(outdir):
    summary = {}
    for machine, styles in BANKS:
        vmap = voices_of(machine)
        midi_dir = os.path.join(outdir, "midi", machine)
        os.makedirs(midi_dir, exist_ok=True)

        patterns = []
        roles = role_map(machine)
        for i, style in enumerate(styles, start=1):
            lanes = develop(machine, i, style)
            lanes = enrich(machine, i, style, lanes, roles)
            for key, lane in lanes.items():
                assert len(lane) == STEPS, (machine, i, key, len(lane))
            patterns.append((i, style, lanes))

        # per-pattern MIDI
        for slot, style, lanes in patterns:
            name = f"P{slot:02d}_{slug(style.name)}.mid"
            write_pattern_midi(os.path.join(midi_dir, name), machine, slot, style, lanes)

        # one file with all 64
        write_bank_midi(os.path.join(outdir, "midi", f"{machine}_bank_all64.mid"),
                        machine, patterns)

        # chart
        doc = []
        doc.append(f"# {machine} — 64-pattern bank")
        doc.append("")
        doc.append(f"Every pattern is **64 steps** long on the 16th-note time scale "
                   f"(4 bars). Set pattern length with `[FUNC]+[LENGTH]`, then page to "
                   f"step 64 and press `[16]`.")
        doc.append("")
        doc.append(f"Legend: {LEGEND}")
        doc.append("")
        doc.append("Voices on this machine:")
        doc.append("")
        doc.append("| Key | Instrument | MIDI note | Tone CC | Nuance shape | Nuance amount | Inst select |")
        doc.append("|---|---|---|---|---|---|---|")
        for v in vmap.values():
            doc.append(f"| {v.key} | {v.name} | {v.note} | {v.tone_cc or '-'} | "
                       f"{v.shape_cc or '-'} | {v.amount_cc or '-'} | "
                       f"{v.select_cc or '-'} |")
        doc.append("")
        for slot, style, lanes in patterns:
            page = (slot - 1) // 16
            if (slot - 1) % 16 == 0:
                doc.append("")
                doc.append(f"## Page {page + 1} ({PAGE_COLOURS[page]}) — "
                           f"{PAGE_TITLES[machine][page]} — "
                           f"patterns P{slot}–P{slot + 15}")
                doc.append("")
            doc += chart_lines(machine, slot, style, lanes)

        chart_path = os.path.join(outdir, f"{machine}_patterns.md")
        with open(chart_path, "w") as fh:
            fh.write("\n".join(doc) + "\n")

        # machine-readable dump
        dump = {
            "machine": machine,
            "steps": STEPS,
            "time_scale": "16th",
            "voices": {v.key: {"name": v.name, "note": v.note,
                               "tone_cc": v.tone_cc, "shape_cc": v.shape_cc,
                               "amount_cc": v.amount_cc,
                               "select_cc": v.select_cc} for v in vmap.values()},
            "patterns": [
                {"slot": slot, "name": style.name, "family": style.family,
                 "tempo": style.tempo, "notes": style.notes,
                 "shuffle": style.shuffle, "flam_time": style.flam_time,
                 "kit": style.kit, "lanes": lanes}
                for slot, style, lanes in patterns
            ],
        }
        with open(os.path.join(outdir, f"{machine}_patterns.json"), "w") as fh:
            json.dump(dump, fh, indent=1, sort_keys=True)

        hits = sum(1 for _, _, l in patterns for lane in l.values()
                   for c in lane if c in ON)
        mods = sum(1 for _, _, l in patterns for k, lane in l.items()
                   if k != GLOBAL_ACCENT for c in lane if c in "fFrR")
        accents = sum(1 for _, _, l in patterns for k, lane in l.items()
                      if k != GLOBAL_ACCENT for c in lane if c in "XFR")
        summary[machine] = {"patterns": len(patterns), "steps_on": hits,
                            "accented": accents, "flam_or_roll": mods,
                            "chart": chart_path}
    return summary


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out")
    os.makedirs(out, exist_ok=True)
    for machine, info in build(out).items():
        print(f"{machine}: {info['patterns']} patterns, {info['steps_on']} steps on, "
              f"{info['accented']} accented, {info['flam_or_roll']} flam/roll")
    print("output ->", out)
