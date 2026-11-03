# ADB, Device & ARTEMIS Troubleshooting

Work top to bottom. Run `scripts/check-devices.sh` first: it covers steps 1–3 in one pass.

## 1. `adb: command not found`

- Desktop: install Android SDK **platform-tools** and add them to `PATH`
  (`export PATH="$ANDROID_HOME/platform-tools:$PATH"`).
- Termux: `pkg install android-tools`. Termux's `adb` talks to *other* devices or to the
  same phone over wireless debugging (see §4); it cannot attach to itself over USB.
- Check the version: `adb version`. Very old servers (< 1.0.41) don't support `adb pair`.

## 2. Device not listed / wrong state

`adb devices -l` prints one of these states per serial:

| State | Meaning | Fix |
| :--- | :--- | :--- |
| *(no line)* | Device not seen at all | Check cable is data-capable, try another port, enable **USB debugging** in Developer options, set USB mode to *File transfer*. Linux: add a udev rule (`51-android.rules`) and add yourself to `plugdev`. |
| `unauthorized` | RSA key not accepted | Unlock the phone and accept the prompt (tick *Always allow*). If no prompt: *Developer options → Revoke USB debugging authorizations*, then `adb kill-server && adb start-server`. Delete `~/.android/adbkey*` as a last resort. |
| `offline` | Transport up, adbd not responding | `adb reconnect offline`, re-plug, or toggle USB debugging. Emulators: cold-boot the AVD. |
| `no permissions` | Host OS denies USB access (Linux) | Fix udev rule / group, or run `adb kill-server` then start it as the right user (never as root by accident). |
| `recovery` / `sideload` / `bootloader` | Not booted into Android | `adb reboot` (or `fastboot reboot`). |

## 3. Multiple devices: `more than one device/emulator`

- Always pass `-s <serial>` (or set `ANDROID_SERIAL`). For ARTEMIS, set `device_serial`
  explicitly on every `mobile_run_task` / `mobile_get_device_state` call.
- `-d` targets the single USB device, `-e` the single emulator.

## 4. Wireless debugging (Android 11+)

```bash
# On device: Developer options → Wireless debugging → Pair device with pairing code
adb pair <ip>:<pair-port>          # enter the 6-digit code
adb connect <ip>:<connect-port>     # port shown on the Wireless debugging screen (differs from pair port)
adb devices -l
```

- Ports change after every toggle or reboot; re-read them from the screen.
- Both devices must be on the same network, with no client isolation (guest Wi-Fi often blocks it).
- Legacy (Android ≤ 10): `adb tcpip 5555` over USB, then `adb connect <ip>:5555`.

## 5. `adb server version doesn't match this client` / port 5037 in use

Two different `adb` binaries are fighting (Android Studio vs. distro package vs. Termux).
`which -a adb`, keep one on `PATH`, then `adb kill-server && adb start-server`.
If another process holds 5037: `lsof -i :5037` (or `ss -ltnp | grep 5037`).

## 6. UI hierarchy dump fails

| Symptom | Cause | Fix |
| :--- | :--- | :--- |
| `ERROR: could not get idle state` | Animations / constantly updating view | Disable animations: `adb shell settings put global window_animation_scale 0` (also `transition_animation_scale`, `animator_duration_scale`). Retry once the screen settles. |
| `null root node returned by UiTestAutomationBridge` | Screen locked, secure window, or another UiAutomation client (uiautomator2/Appium server) holds the connection | Unlock screen; stop the other automation server (`adb shell am force-stop com.github.uiautomator`); retry. |
| Empty / partial XML | WebView or Flutter content | Enable WebView debugging (`WebView.setWebContentsDebuggingEnabled(true)`) and use Chrome DevTools / Playwright `connectOverCDP`; for Flutter use semantics labels or Flutter Driver / Patrol. |
| `FLAG_SECURE` black screenshots | App blocks capture | Use a debug build without `FLAG_SECURE`; coordinates from a dump still work. |

## 7. Taps or text input do nothing

- Coordinates are **physical pixels**: check `adb shell wm size` and `adb shell wm density`;
  if an override is set, convert accordingly. Rotation changes axes.
- `input text` cannot type spaces or most symbols directly: use `%s` for spaces
  (`adb shell input text "hello%sworld"`) and escape shell metacharacters. For Unicode,
  use an IME such as ADBKeyboard, or set the field via the UI framework instead.
- Some OEM ROMs (MIUI/HyperOS, ColorOS) require **USB debugging (Security settings)** to be
  enabled before `input` events are accepted.
- An overlay (permission dialog, keyboard, toast) may be eating the tap: dump the hierarchy
  and look at the top-most window.

## 8. App install / launch problems

| Error | Fix |
| :--- | :--- |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` | Signature differs from installed build: `adb uninstall <pkg>` first. |
| `INSTALL_FAILED_VERSION_DOWNGRADE` | `adb install -r -d app.apk`. |
| `INSTALL_FAILED_NO_MATCHING_ABIS` | APK lacks the device ABI (`adb shell getprop ro.product.cpu.abi`); build a matching split or universal APK. |
| `INSTALL_FAILED_INSUFFICIENT_STORAGE` | Free space or `adb shell pm trim-caches 1G`. |
| Activity won't start | Find the launcher activity: `adb shell cmd package resolve-activity --brief <pkg>`, then `adb shell am start -n <pkg>/<activity>`. Or `adb shell monkey -p <pkg> 1`. |

Collect crash context with `adb logcat -b crash -d` and
`adb logcat --pid=$(adb shell pidof -s <pkg>)`.

## 9. ARTEMIS-specific failures

1. Call `mobile_diagnose(attempt_fix=True)` and read every reported check, not only the summary.
2. Confirm `mobile_get_device_state` returns the expected `device_serial`, foreground package and screen size.
3. **Flash** steps time out on slow screens: add explicit wait instructions to the task prompt
   (≈ *T − 5 s*, see SKILL.md §2) or switch to **Pro** for multi-step journeys.
4. **Pro** checker keeps rejecting a step: the expected state in your prompt is probably
   ambiguous; name the exact text/ID that proves success.
5. After any fix, re-run the smallest failing step before resuming the whole journey.

## 10. Emulators

- `emulator -list-avds`; start headless with `emulator -avd <name> -no-window -no-audio -no-snapshot`.
- Wait for boot: `adb wait-for-device shell 'while [ "$(getprop sys.boot_completed)" != 1 ]; do sleep 1; done'`.
- Hardware acceleration: Linux needs `/dev/kvm` access (`kvm-ok`); in CI use an x86_64 image with KVM, or an ARM64 image on ARM hosts.
