#!/usr/bin/env python3
"""Assemble the pattern-book page: inject both banks into gen/ui_template.html.

    python3 gen/build_ui.py            # -> out/pattern-book.html
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from engine import MACHINES


def main():
    banks = {}
    for machine in ("TT-606", "TT-78"):
        path = os.path.join(ROOT, "out", f"{machine}_patterns.json")
        if not os.path.exists(path):
            sys.exit(f"{path} missing - run gen/build.py first")
        d = json.load(open(path))
        banks[machine] = {
            "order": [v.key for v in MACHINES[machine]],
            "voices": d["voices"],
            "patterns": [
                {"slot": p["slot"], "name": p["name"], "family": p["family"],
                 "tempo": p["tempo"], "notes": p["notes"], "shuffle": p["shuffle"],
                 "flam_time": p["flam_time"], "kit": p["kit"], "lanes": p["lanes"]}
                for p in sorted(d["patterns"], key=lambda x: x["slot"])
            ],
        }

    data = json.dumps(banks, separators=(",", ":"), ensure_ascii=True)
    if "</script" in data:
        sys.exit("data would break out of the script tag")

    tpl = open(os.path.join(HERE, "ui_template.html"), encoding="utf-8").read()
    if tpl.count("__DATA__") != 1:
        sys.exit("template needs exactly one __DATA__ placeholder")
    html = tpl.replace("__DATA__", data)
    if any(ord(c) > 127 for c in html):
        sys.exit("page contains non-ASCII; keep it escaped so charset cannot bite")

    out = os.path.join(ROOT, "out", "pattern-book.html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"{len(html)} bytes -> {out}")


if __name__ == "__main__":
    main()
