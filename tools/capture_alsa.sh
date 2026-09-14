#!/usr/bin/env bash
# Capture SysEx from a TT-606 / TT-78 using ALSA's amidi. No Python bindings needed.
#
#   tools/capture_alsa.sh --list
#   tools/capture_alsa.sh hw:2,0,0 captures/empty.syx
#   tools/capture_alsa.sh hw:2,0,0 captures/empty.syx 20     # 20s idle timeout
#
# Requires the machine's MIDI OUT cabled into the interface's MIDI IN, and the
# machine's rear MIDI Out/Thru switch set to OUT.
#
# Then trigger a dump on the machine: select a pattern and press [FUNC]+[COPY].
# That sends the pattern as SysEx (the pattern-clone feature) - a much smaller
# and cleaner target than a whole Cyclone Studio memory backup.
set -euo pipefail

if [[ "${1:-}" == "--list" || $# -lt 2 ]]; then
  echo "hardware ports:"
  amidi -l
  echo
  echo "usage: $0 <port> <outfile.syx> [idle-timeout-seconds]"
  exit 0
fi

PORT="$1"
OUT="$2"
TIMEOUT="${3:-15}"

mkdir -p "$(dirname "$OUT")"
echo "listening on $PORT -> $OUT (stops after ${TIMEOUT}s idle, or Ctrl-C)"
echo "press [FUNC]+[COPY] on the machine now"

# amidi already filters active sensing and clock unless -a / -c are given.
amidi -p "$PORT" -r "$OUT" -t "$TIMEOUT" || true

if [[ ! -s "$OUT" ]]; then
  echo "nothing captured - check the cable direction, the rear MIDI Out/Thru"
  echo "switch (must be OUT), and that the MIDI OUT channel is not cleared"
  exit 1
fi

echo
echo "captured $(stat -c%s "$OUT") bytes"
python3 "$(dirname "$0")/analyze_sysex.py" "$OUT"
