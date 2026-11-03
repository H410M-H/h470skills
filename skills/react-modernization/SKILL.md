---
name: react-modernization
description: >-
  Upgrade React applications across majors (16/17 → 18 → 19), migrate class components to
  hooks, adopt concurrent features (transitions, Suspense) and React 19 APIs (ref as prop,
  use(), useActionState, useOptimistic, form actions), and apply official codemods and the
  React Compiler. Use when modernizing a React codebase, fixing React 19 upgrade
  breakages, or converting legacy class components.
---

# React Modernization

Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation.

## Use this skill when
- Upgrading React applications to latest versions
- Migrating class components to functional components with hooks
- Adopting concurrent React features (Suspense, transitions)
- Applying codemods for automated refactoring
- Modernizing state management patterns
- Updating to TypeScript
- Improving performance with React 18+ features

## Do not use this skill when
- The app is not React (Preact, Solid, Vue)
- You only need a new feature, not an upgrade or migration

## Workflow
1. Inventory the current React and react-dom versions, the renderer (CRA, Vite, Next), test setup, and blocking dependencies (UI kits, state libraries, router).
2. Upgrade one major version at a time. First move to the latest minor of your current major (18.3 prints React 19 deprecation warnings) and fix every warning.
3. Run the codemods, then fix the remaining type and runtime errors by hand.
4. Migrate class components to hooks incrementally, covered by tests. Enable StrictMode and profile with React DevTools.

## Core rules
- Codemods first: `npx codemod@latest react/19/migration-recipe` and, for TypeScript, `npx types-react-codemod@latest preset-19 ./src`.
- React 18: `createRoot`/`hydrateRoot`, automatic batching, StrictMode double-invokes effects in dev (fix the cleanups, don't disable it), `useTransition`, `useDeferredValue`, `useId`, and Suspense for data.
- React 19 removals: `ReactDOM.render`/`hydrate`, `unmountComponentAtNode`, `findDOMNode`, string refs, legacy context, and `propTypes`/`defaultProps` on function components (use default parameters). The new JSX transform is required.
- React 19 additions: `ref` is a regular prop (no `forwardRef` needed), `<Context>` works as the provider, the `use()` hook, `useActionState` (replaces `useFormState`), `useOptimistic`, `useFormStatus`, form `action` functions, native `<title>`/`<meta>`/`<link>` hoisting, and ref callbacks may return a cleanup function.
- Class → hooks: `this.state` → `useState`/`useReducer`; lifecycles → `useEffect` with correct dependencies and cleanup. Don't mirror props into state; derive values during render.
- React Compiler (stable since 1.0) auto-memoises. Adopt it before deleting manual `useMemo`/`useCallback`, and verify with the profiler.

## Output format
- Upgrade plan with ordered steps
- Codemods run and manual fixes
- Breaking-change checklist status
- Test/profiling results

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Version Upgrade Path
- Class to Hooks Migration
- React 18 Concurrent Features
- Codemods for Automation
- Performance Optimization
- TypeScript Migration
- Migration Checklist
- Best Practices
- Common Pitfalls
