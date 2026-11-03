---
name: tailwind-design-system
description: >-
  Build scalable design systems with Tailwind CSS v3 or v4: semantic design tokens (v4
  @theme CSS variables or v3 config), cva component variants, dark mode, responsive and
  container-query layouts, and accessible components. Use when creating a component
  library, implementing design tokens or theming, standardizing UI patterns, or migrating
  a project from Tailwind v3 to v4.
---

# Tailwind Design System

Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility.

## Use this skill when
- Creating a component library with Tailwind
- Implementing design tokens and theming
- Building responsive and accessible components
- Standardizing UI patterns across a codebase
- Migrating to or extending Tailwind CSS
- Setting up dark mode and color schemes

## Do not use this skill when
- The project uses a different styling system (CSS Modules only, styled-components, vanilla-extract) and isn't adopting Tailwind

## Workflow
1. Detect the version. **v4** if CSS has `@import "tailwindcss"` / `@theme`. **v3** if there's a `tailwind.config.*` plus `@tailwind base`. The playbook's Quick Start covers both versions.
2. Define tokens in layers: primitives (palette, spacing, radii) → semantic (`primary`, `surface`, `muted`, `ring`) → component tokens where needed.
3. Build primitives (Button, Input, Card, Dialog) with variants via `cva`, and merge classes with `cn()` (clsx + tailwind-merge).
4. Verify responsive behaviour, dark mode, focus states, and contrast for every component.

## Core rules
- Components consume only **semantic** tokens backed by CSS variables, so theming and dark mode are a variable swap with no per-component `dark:` sprawl.
- Never build class names dynamically (`bg-${color}-500`): the scanner can't see them. Map props to full literal class strings.
- Expose `variant`/`size` props, not arbitrary class strings. Allow a `className` escape hatch merged last through `tailwind-merge`.
- Design mobile-first (`sm:` and up). Use container queries (`@container`, built into v4) for components that live in varied layouts.
- Accessibility: a visible `focus-visible:` ring, ≥ 4.5:1 text contrast (3:1 for UI and large text), `motion-reduce:` variants, `sr-only` labels, and 24×24px minimum targets.
- Prefer composing components over `@apply`. Reserve `@apply` for styling markup you don't control.

## Version notes
- **Tailwind v4** (CSS-first): `@import "tailwindcss";` plus `@theme { --color-primary: oklch(...); --radius-lg: ...; }` generates utilities from the variables. Class-based dark mode: `@custom-variant dark (&:where(.dark, .dark *));`. Content is detected automatically; add extra paths with `@source`. Install through `@tailwindcss/vite` or `@tailwindcss/postcss`.
- **Upgrading v3 → v4**: run `npx @tailwindcss/upgrade`. Renamed utilities: `shadow-sm`→`shadow-xs`, `shadow`→`shadow-sm`, `rounded-sm`→`rounded-xs`, `rounded`→`rounded-sm`, `blur-sm`→`blur-xs`, `outline-none`→`outline-hidden`. `ring` defaults to 1px (use `ring-3` for the old look). The default border colour is `currentColor`.
- **React 19**: `forwardRef` in the playbook's components is optional, because `ref` can be taken as a normal prop.

## Output format
- Token definitions (`@theme` or config)
- Component code with variants
- Usage examples
- Accessibility and dark-mode checks

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Quick Start
- Patterns
- Utility Functions
- Best Practices
