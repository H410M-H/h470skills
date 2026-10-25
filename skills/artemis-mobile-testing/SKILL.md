---
name: artemis-mobile-testing
description: >-
  Author and execute robust mobile tests and device automation using ARTEMIS MCP,
  ADB, and Android UI frameworks. Use when interacting with Android devices or emulators,
  diagnosing mobile test issues, running exploratory UI tasks with Flash/Pro models,
  or writing resilient end-to-end test scripts (Dynamic-First, Coordinate-Fallback).
---

# ARTEMIS Mobile Testing & Automation

This skill equips the agent to perform closed-loop mobile testing, interactive device exploration, and robust test script authoring using ARTEMIS and native Android tooling.

## When to Use This Skill

- Authoring end-to-end mobile tests for Android applications (Capacitor, React Native, Flutter, Native Kotlin/Java).
- Exploring target app UI hierarchy, screen transitions, and gestures using ARTEMIS MCP tools (`mobile_run_task`, `mobile_get_device_state`, `mobile_diagnose`).
- Generating resilient test code using the **Dynamic-First, Coordinate-Fallback** pattern.
- Diagnosing connected devices, emulators, or ADB connection failures.

---

## 1. Core Principles

### A. The Runnable Code Principle
- Always deliver executable, self-contained test scripts with explicit wait conditions rather than arbitrary sleeps.
- Before writing test code, explore the application interactively via ARTEMIS or direct ADB commands to uncover exact element IDs, text anchors, and transition delays.

### B. Dynamic-First, Coordinate-Fallback Pattern
To avoid brittle tests caused by layout shifts or screen resolution differences:
1. **Try Dynamic Locators**: Target elements by Resource ID, accessibility label (`content-desc`), or text matching.
2. **Catch / Fallback to Coordinates**: If dynamic lookup times out or the element lacks accessibility metadata, fall back to normalized or absolute screen coordinates discovered during exploration.

```python
# Example: Resilient Click Pattern (Python UIAutomator2 / Appium)
def safe_click(d, resource_id=None, text=None, fallback_coords=None, timeout=5):
    try:
        if resource_id and d(resourceId=resource_id).wait(timeout=timeout):
            d(resourceId=resource_id).click()
            return
        if text and d(text=text).wait(timeout=timeout):
            d(text=text).click()
            return
    except Exception as e:
        pass
    
    if fallback_coords:
        x, y = fallback_coords
        d.click(x, y)
    else:
        raise TimeoutError(f"Element {resource_id or text} not found")
```

---

## 2. Choosing the ARTEMIS Execution Model

When invoking `mobile_run_task`:

| Capability | ARTEMIS Flash | ARTEMIS Pro |
| :--- | :--- | :--- |
| **Model Type** | Single-pass reactive loop | Multi-agent graph (Planner, Operator, Checker) |
| **Best For** | Fast, deterministic UI actions, simple forms, quick taps | Complex multi-step journeys, edge cases, error recovery |
| **Turn Latency** | ~5 seconds / step | ~30 seconds / turn |
| **Waiting Compensation** | Request $(T - 5\text{s})$ wait in prompt | Natural pipeline turn interval often covers waits |
| **Safety Net** | None (direct execution) | Pre-execution XML validation & visual checkpointing |

---

## 3. Device Diagnostics & Management

### Environment Self-Diagnosis Flow
Whenever an ARTEMIS tool fails or no device is found:
1. Call `mobile_diagnose(attempt_fix=True)`.
2. Check `adb devices -l` in terminal to verify device state (`device`, `unauthorized`, `offline`).
3. For multi-device setups, always confirm the target `device_serial` before launching tasks.

### ADB Essential Commands
- List devices: `adb devices -l`
- Screenshot: `adb exec-out screencap -p > screen.png`
- Dump UI hierarchy: `adb shell uiautomator dump /sdcard/window_dump.xml && adb pull /sdcard/window_dump.xml`
- Tap coordinate: `adb shell input tap <X> <Y>`
- Input text: `adb shell input text "<STRING>"`
- Key events: `adb shell input keyevent 4` (Back), `adb shell input keyevent 3` (Home)

---

## References & Helpers

- [Locators & Framework Guide](./references/locators-guide.md): Patterns for Appium, Maestro, UIAutomator2, and Playwright.
- [Troubleshooting & Diagnostics](./references/troubleshooting.md): Step-by-step resolution for ADB and environment errors.
- [Device Checker Script](./scripts/check-devices.sh): Automated diagnostic script for connected hardware.
