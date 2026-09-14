#!/usr/bin/env bash
# Send a .syx file to a TT-606 / TT-78 using ALSA's amidi.
#
#   tools/send_alsa.sh hw:2,0,0 captures/pattern.syx
#   tools/send_alsa.sh hw:2,0,0 captures/bank.syx 100    # 100ms between messages
#
# For a captured pattern-clone message: send it, then press [FUNC]+[PASTE] on
# the machine with the destination pattern selected.
#
# A Cyclone Studio restore overwrites the machine's entire memory. Back up
# anything you care about first.
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: $0 <port> <file.syx> [sysex-interval-ms]"
  echo
  amidi -l
  exit 1
fi

PORT="$1"
FILE="$2"
INTERVAL="${3:-50}"

echo "sending $(stat -c%s "$FILE") bytes to $PORT (${INTERVAL}ms between messages)"
amidi -p "$PORT" -s "$FILE" -i "$INTERVAL"
echo "sent"
