---
name: e2e-testing-patterns
description: Master end-to-end testing with Playwright and Cypress to build reliable test suites that catch bugs, improve confidence, and enable fast deployment. Use when implementing E2E tests, debugging flaky tests, or establishing testing standards.
---

# E2E Testing Patterns

Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do.

## Use this skill when
- Implementing end-to-end test automation
- Debugging flaky or unreliable tests
- Testing critical user workflows
- Setting up CI/CD test pipelines
- Testing across multiple browsers
- Validating accessibility requirements
- Testing responsive designs
- Establishing E2E testing standards

## Do not use this skill when
- You only need unit or integration tests
- The environment cannot support stable UI automation
- You cannot provision safe test accounts or data

## Workflow
1. List the critical user journeys (sign-up, checkout, core CRUD) and their success criteria.
2. Choose the tool: Playwright by default (multi-browser, parallel, traces); Cypress if the team already uses it.
3. Build fixtures for auth and test data, then write the journeys with stable selectors.
4. Wire into CI with sharding, artifacts (trace, video, screenshots), and a flaky-test policy.

## Core rules
- Cover only the critical journeys end to end. Push edge cases down to unit and integration tests (test pyramid).
- Select elements the way users find them: `getByRole`, `getByLabel`, `getByText`, then `data-testid`. Never use CSS chains, XPath, or `nth-child`.
- No fixed sleeps. Rely on auto-waiting and web-first assertions (`await expect(locator).toBeVisible()`, `toHaveURL`).
- Every test is isolated and parallel-safe: it creates its own data through the API or fixtures and never depends on test order. Reuse login with `storageState`.
- Mock only third parties you don't control (payments, email) with network routing. Keep your own backend real.
- Page objects and fixtures hold reusable actions. Assertions stay in the test body.
- CI: run retries only in CI (e.g. 2), record a trace on first retry, and keep artifacts on failure. Quarantine flaky tests and fix them; don't silently retry forever.
- Never run destructive tests against production, and scrub secrets and PII from traces and videos.

## Safety
- Avoid running destructive tests against production.
- Use dedicated test data and scrub sensitive output.

## Output format
- Journey list with priority
- Test files / page objects
- CI configuration
- Flakiness and data strategy notes

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Playwright Patterns
- Cypress Patterns
- Advanced Patterns
- Best Practices
- Common Pitfalls
- Debugging Failing Tests
