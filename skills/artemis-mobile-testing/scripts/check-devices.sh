#!/usr/bin/env bash
# ARTEMIS Device Health & Status Diagnostic Script
set -euo pipefail

echo "=== Android Device & ADB Diagnostic ==="

if ! command -v adb >/dev/null 2>&1; then
  echo "[-] Error: 'adb' command not found in PATH."
  echo "    Ensure Android SDK platform-tools are installed."
  exit 1
fi

echo "[+] Checking ADB server status..."
adb start-server

echo "[+] Attached devices:"
DEVICES=$(adb devices -l | tail -n +2 | sed '/^$/d')

if [ -z "$DEVICES" ]; then
  echo "[-] No connected Android devices or emulators found."
  echo "    Troubleshooting tips:"
  echo "    1. Check USB debugging toggle on device Developer Options."
  echo "    2. Accept RSA key authorization popup on phone screen."
  echo "    3. Run 'adb kill-server && adb start-server'."
  exit 1
fi

echo "$DEVICES"
echo ""
echo "[+] Device architecture & SDK level summary:"
# </dev/null stops `adb shell` eating the loop's stdin; tr strips the \r some devices append.
prop() { adb -s "$1" shell getprop "$2" </dev/null 2>/dev/null | tr -d '\r' || echo "Unknown"; }

adb devices | tail -n +2 | sed '/^$/d' | while read -r serial STATE _; do
  if [ "$STATE" = "device" ]; then
    MODEL=$(prop "$serial" ro.product.model)
    SDK=$(prop "$serial" ro.build.version.sdk)
    ABI=$(prop "$serial" ro.product.cpu.abi)
    echo "    Device: $serial | Model: $MODEL | SDK: $SDK | ABI: $ABI"
  else
    echo "    Device: $serial | State: $STATE (see references/troubleshooting.md §2)"
  fi
done
echo "=== Diagnostic Complete ==="
