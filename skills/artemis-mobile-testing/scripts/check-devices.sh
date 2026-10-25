#!/bin/bash
# ARTEMIS Device Health & Status Diagnostic Script
set -e

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
for serial in $(adb devices | tail -n +2 | awk '{print $1}' | sed '/^$/d'); do
  STATE=$(adb devices | grep "$serial" | awk '{print $2}')
  if [ "$STATE" = "device" ]; then
    MODEL=$(adb -s "$serial" shell getprop ro.product.model 2>/dev/null || echo "Unknown")
    SDK=$(adb -s "$serial" shell getprop ro.build.version.sdk 2>/dev/null || echo "Unknown")
    ABI=$(adb -s "$serial" shell getprop ro.product.cpu.abi 2>/dev/null || echo "Unknown")
    echo "    Device: $serial | Model: $MODEL | SDK: $SDK | ABI: $ABI"
  else
    echo "    Device: $serial | State: $STATE (Needs authorization or recovery)"
  fi
done
echo "=== Diagnostic Complete ==="
