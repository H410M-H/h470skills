---
name: termux-android-poweruser
description: >-
  Advanced system administration, build toolchains, and hardware integration for Termux on Android.
  Use when compiling native binaries on ARM64, managing background services, preventing Android OS
  process kills (wake-locks), using termux-api for device hardware access, setting up glibc/proot
  environments, or troubleshooting Termux packaging and filesystem issues.
---

# Termux Android Power-User Guide

Comprehensive runbook and operational patterns for running complex development pipelines, servers, and AI tooling natively on Android via Termux.

## When to Use This Skill

- Setting up developer toolchains (Node, Python, Go, Rust, Clang/LLVM) on Termux.
- Managing background tasks and preventing process termination via `termux-wake-lock`.
- Accessing Android system features (clipboard, notifications, storage) via `termux-api`.
- Configuring `proot-distro` or Termux glibc bridges for binaries requiring standard GNU libc.
- Debugging filesystem path issues (resolving `$PREFIX`, `/data/data/com.termux/files/...`).

---

## 1. Environment & Path Standards

Unlike standard Linux distributions (`/usr`, `/etc`), Termux operates inside the Android sandbox:
- **Prefix Root**: `$PREFIX` = `/data/data/com.termux/files/usr`
- **Home Directory**: `$HOME` = `/data/data/com.termux/files/home`
- **Temporary Files**: `$TMPDIR` = `$PREFIX/tmp`

### Crucial Fixes for Scripts & Binaries
- **Shebang Fixing**: Scripts using `#!/bin/bash` or `#!/usr/bin/env` must be sanitized with `termux-fix-shebang <file>` so they point to `$PREFIX/bin`.
- **Shared Libraries**: Termux uses Android Bionic libc. For standard Linux binaries compiled against glibc, use `glibc-repo` or `proot-distro`.

---

## 2. Preventing Background Process Termination

Android's Low Memory Killer (LMK) and battery savers will aggressively terminate long-running processes (compiles, dev servers, agents).

### Keep-Alive Commands
```bash
# Acquire wake-lock to prevent CPU sleep
termux-wake-lock

# Release wake-lock when finished
termux-wake-unlock
```

> [!TIP]
> Ensure **Battery Optimization** is set to "Unrestricted" for the Termux app in Android Settings -> Apps -> Termux -> Battery.

---

## 3. Native Hardware Integration via `termux-api`

Install with `pkg install termux-api` (requires the Termux:API companion APK from F-Droid).

| Command | Action |
| :--- | :--- |
| `termux-clipboard-get` | Read device clipboard text |
| `termux-clipboard-set "<text>"` | Write text to device clipboard |
| `termux-toast "<message>"` | Display native Android toast message |
| `termux-notification -t "Title" -c "Body"` | Send persistent Android notification |
| `termux-battery-status` | Get JSON battery level and thermal state |
| `termux-vibrate -d 500` | Trigger device haptic vibration |

---

## 4. Native Development Toolchain Setup

### Compilers & Core Languages
```bash
# Essential build tools (gcc/clang, make, cmake)
pkg install build-essential clang binutils git cmake

# Modern package managers and runtimes
pkg install nodejs-lts python golang rust
```

### PostgreSQL Native Service in Termux
```bash
pkg install postgresql
initdb -D $PREFIX/var/lib/postgresql
pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start
```
