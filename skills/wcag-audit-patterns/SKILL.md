---
name: wcag-audit-patterns
description: >-
  Conduct WCAG 2.2 AA accessibility audits combining automated scans (axe, Lighthouse)
  with manual keyboard, screen-reader, zoom and contrast checks, and produce findings
  mapped to success criteria with remediation guidance. Use when auditing a site or
  component for accessibility, fixing WCAG violations, implementing accessible components,
  or preparing evidence for ADA, Section 508, or European Accessibility Act reviews.
---

# WCAG Audit Patterns

Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies.

## Use this skill when
- Conducting accessibility audits
- Fixing WCAG violations
- Implementing accessible components
- Preparing for accessibility lawsuits
- Meeting ADA/Section 508 requirements
- Achieving VPAT compliance

## Do not use this skill when
- You need legal advice or formal certification
- You only want a quick automated scan without manual verification
- You cannot access the UI or source for remediation work

## Workflow
1. Run automated scans (axe, Lighthouse, WAVE) to collect initial findings.
2. Perform manual checks (keyboard navigation, focus order, screen reader flows).
3. Map each issue to a WCAG criterion, severity, and remediation guidance.
4. Re-test after fixes and document residual risk and compliance status.

## Core rules
- Target **WCAG 2.2 Level AA** unless told otherwise. Criteria new in 2.2: 2.4.11 Focus Not Obscured (Minimum), 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum, 24×24 CSS px), 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication (Minimum). 4.1.1 Parsing is obsolete.
- Automated scanners (axe-core, Lighthouse, WAVE, Pa11y) catch only a minority of issues. Every audit also needs manual checks.
- Manual passes: keyboard only (logical tab order, visible focus, no traps, Esc closes dialogs); a screen reader (NVDA + Chrome/Firefox, VoiceOver + Safari, TalkBack); 200% zoom and 320px reflow; `prefers-reduced-motion`; colour-only cues.
- Native HTML first, ARIA only to fill gaps (no ARIA beats bad ARIA). Every interactive control needs an accessible name, role, and state.
- Contrast: 4.5:1 for body text, 3:1 for large text, UI components, and focus indicators.
- Forms: visible labels (placeholder is not a label), errors described in text and linked with `aria-describedby`, and required fields marked programmatically.
- Images: meaningful `alt`, or `alt=""` for decoration. Media: captions and transcripts.
- Report each issue with its success criterion and level, severity, location/selector, evidence (screenshot or snippet), and remediation. Re-test after fixes.
- Don't claim legal compliance (ADA, Section 508, EN 301 549 / European Accessibility Act). Recommend expert review for conformance statements and VPATs.

## Safety
- Avoid claiming legal compliance without expert review.
- Keep evidence of test steps and results for audit trails.

## Output format
- Scope and method (tools, AT/browser combos)
- Findings table: SC, level, severity, location, fix
- Prioritised remediation plan
- Residual risk and re-test results

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Audit Checklist
- 1.2 Time-based Media
- 1.3 Adaptable
- 1.4 Distinguishable
- 2.1 Keyboard Accessible
- 2.2 Enough Time
- 2.3 Seizures and Physical Reactions
- 2.4 Navigable
- 3.1 Readable
- 3.2 Predictable
- 3.3 Input Assistance
- 4.1 Compatible
