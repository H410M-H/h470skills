---
name: lms-android-codebase
description: >
  Comprehensive codebase memory for LMS-android (MSNS Mobile ERP & Capacitor App). Use this skill to recall Android native build pipelines, Capacitor 8 plugins, offline SQLite caching, barcode scanning, push notifications, release signing, and mobile-specific architecture.
---

# LMS Android (Capacitor & Mobile ERP) Codebase Memory

## Overview
- **Name:** `msns-lms` (Android / Capacitor Edition)
- **Repository:** `https://github.com/H410M-H/LMS-android`
- **Output Artifact:** Android App Bundle (`.aab`) & APKs for Google Play Store.
- **Base ERP Stack:** Next.js 15, React 18, TypeScript, Tailwind CSS, Prisma 6, PostgreSQL, tRPC v11.
- **Mobile Engine:** Capacitor 8 with native Android runtime (`android/` project).

---

## Mobile & Android Architecture

### 1. Capacitor 8 Core & Plugins
- `@capacitor/core` & `@capacitor/android` (v8.5.0) — Native web-to-Android bridge.
- `@capacitor-community/sqlite` (v8.1.1) — Native SQLite database for offline timetable and diary caching.
- `@capacitor-mlkit/barcode-scanning` (v8.1.0) — High-performance Google ML Kit native barcode and QR scanner for student/staff cards.
- `@capacitor/camera` (v8.2.2) — Native camera integration for document scanning and biometric verification.
- `@capacitor/local-notifications` (v8.3.1) & `@capacitor/push-notifications` (v8.1.2) — Push & scheduled local notifications for exams, fees, and homework.
- `@capacitor/network` & `@capacitor/preferences` (v8.0.1) — Connectivity status listener and encrypted key-value storage.
- `@fingerprintjs/fingerprintjs-pro-react` — Device fingerprinting and biometric security.

### 2. Edge-to-Edge & Immersive UI
- Layout configuration in Next.js viewport: `viewportFit: "cover"`.
- Native status bar overlay: Capacitor `StatusBar.overlaysWebView: true`.
- Android display cutout handling: `shortEdges` window layout mode in Android styles.
- Tailwind safe-area utility classes: `pt-safe`, `pb-safe`, `pl-safe`, `pr-safe`, `h-[100dvh]`.

### 3. Offline First & Dual-Tier Persistence ([`src/lib/mobile/offline-cache.ts`](file:///data/data/com.termux/files/home/LMS-android/src/lib/mobile/offline-cache.ts))
- **Primary Tier:** Capacitor SQLite database (`msns_offline.db`) storing:
  - Class timetables & master period rosters.
  - Homework diaries and student attendance records.
  - Published exam datesheets and report cards.
- **Fallback Tier:** Browser `LocalStorage` for web/preview environments.

---

## Android Build & Release Pipeline

### Key Scripts & Native Files
- [`capacitor.config.ts`](file:///data/data/com.termux/files/home/LMS-android/capacitor.config.ts) — App ID (`com.msns`), app name (`MSNS LMS`), webDir (`public` / Next.js export).
- [`generate-release-keystore.sh`](file:///data/data/com.termux/files/home/LMS-android/generate-release-keystore.sh) — Keytool script to generate production release keystore (`msns-release-key.keystore`).
- [`setup-android-sdk.sh`](file:///data/data/com.termux/files/home/LMS-android/setup-android-sdk.sh) — Headless Android SDK & command-line tools installer for Termux / Linux.
- `android/app/build.gradle` — Android app Gradle build script, version codes, signingConfigs, and dependency trees.

### Build Commands
- `npm run cap:sync`: Sync Next.js web assets and plugins to the `android/` project.
- `npm run android:build`: Syncs Capacitor and invokes `./gradlew bundleRelease` inside `android/` to generate production `.aab`.
- `npm run android:keystore`: Generates release signing credentials.
- `npm run check`: Run Next.js linting and TypeScript compilation checks.

---

## Core LMS Features Integrated in Mobile
1. **Student & Parent Portals:** Enrolled courses, daily timetable viewer, attendance records, digital fee challans, exam report cards.
2. **Teacher Workspace:** Daily period schedule, attendance marker (biometric / manual), homework diary publisher, exam marks entry.
3. **Admin & Governance:** Multi-role governance matrix (Admin, Principal, Head, Clerk, Teacher, Student, Parent, Worker).
4. **Push Notification Dispatcher:** Automated triggers for fee due dates, exam datesheet publication, and emergency school alerts.
