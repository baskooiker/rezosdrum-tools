#!/usr/bin/env bash
# Launch Cyclone Studio under Wine, with the MIDI interface pre-selected.
#
#   tools/run-cyclone-studio.sh                  # use the default interface name
#   tools/run-cyclone-studio.sh "MidiSport"      # pick an interface by substring
#   tools/run-cyclone-studio.sh --list           # show the interfaces Wine can see
#
# Studio opens MIDI port index 0 at startup. On a PipeWire desktop that index is
# a virtual port it cannot open, and it dies before drawing its window with only
#   MidiInWinMM::openPort: error creating Windows MM MIDI input port.
# to show for it. This script finds the wanted interface in Wine's own
# enumeration and writes the index into Studio's settings before launching.
set -euo pipefail

PREFIX="${WINEPREFIX:-$HOME/.cyclone-studio}"
APP="$PREFIX/drive_c/CycloneStudio/Cyclone Studio.exe"
MATCH="${1:-MidiSport}"

export WINEPREFIX="$PREFIX"
export WINEARCH=win32
export WINEDLLOVERRIDES="mscoree,mshtml="
export DISPLAY="${DISPLAY:-:0}"

if [[ ! -f "$APP" ]]; then
  echo "Cyclone Studio not found at:" >&2
  echo "  $APP" >&2
  echo >&2
  echo "Download CycloneStudio2.0_Windows.zip from the Cyclone Analogic site and" >&2
  echo "unpack it there, or set WINEPREFIX to a prefix that already has it." >&2
  exit 1
fi

# Ask Wine to enumerate MIDI ports. Studio exits on its own once it fails to
# open port 0, so this costs a couple of seconds and needs no cleanup.
enumerate() {
  WINEDEBUG=+midi timeout 25 wine "$APP" 2>&1 |
    sed -n "s/.*port_add MidiIn *\[\([0-9]*\)\].*name='L\"\(.*\)\"'.*/\1\t\2/p"
}

PORTS="$(enumerate || true)"
if [[ -z "$PORTS" ]]; then
  echo "Wine reported no MIDI input ports. Is the interface plugged in?" >&2
  exit 1
fi

if [[ "$MATCH" == "--list" ]]; then
  echo "MIDI input ports as Wine sees them:"
  echo "$PORTS" | sed 's/^/  index /'
  exit 0
fi

INDEX="$(echo "$PORTS" | grep -i -- "$MATCH" | head -1 | cut -f1)"
if [[ -z "$INDEX" ]]; then
  echo "No MIDI interface matching '$MATCH'. Available:" >&2
  echo "$PORTS" | sed 's/^/  index /' >&2
  exit 1
fi
NAME="$(echo "$PORTS" | grep -i -- "$MATCH" | head -1 | cut -f2)"
echo "using MIDI port index $INDEX  ($NAME)"

KEY='HKCU\Software\Cyclone Analogic\Cyclone Studio 2.0'
WINEDEBUG=-all wine reg add "$KEY" /v inPort  /t REG_DWORD /d "$INDEX" /f >/dev/null 2>&1
WINEDEBUG=-all wine reg add "$KEY" /v outPort /t REG_DWORD /d "$INDEX" /f >/dev/null 2>&1

echo "starting Cyclone Studio..."
WINEDEBUG=-all exec wine "$APP"
