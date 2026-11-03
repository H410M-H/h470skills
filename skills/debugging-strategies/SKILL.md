---
name: debugging-strategies
description: Master systematic debugging techniques, profiling tools, and root cause analysis to efficiently track down bugs across any codebase or technology stack. Use when investigating bugs, performance issues, or unexpected behavior.
---

# Debugging Strategies

Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches.

## Use this skill when
- Tracking down elusive bugs
- Investigating performance issues
- Debugging production incidents
- Analyzing crash dumps or stack traces
- Debugging distributed systems

## Do not use this skill when
- There is no reproducible issue or observable symptom
- The task is purely feature development
- You cannot access logs, traces, or runtime signals

## Workflow
1. Reproduce: capture exact inputs, environment, versions, and the full error or stack trace. Reduce it to a minimal, deterministic repro, ideally a failing test.
2. Ask what changed: `git log`, recent deploys, dependency bumps, config, feature flags, and data shape.
3. Form one falsifiable hypothesis, design an experiment that changes one variable, run it, and write down the result.
4. Narrow with binary search (`git bisect`, halving the input, or disabling half the code path) until the root cause is isolated.
5. Fix the root cause, keep the repro as a regression test, and search for the same bug pattern elsewhere.

## Core rules
- Read the whole error message and stack trace before touching code. The first frame in *your* code is usually where to start.
- Instrument instead of guessing: debugger breakpoints, structured logs with correlation IDs, and tracing. Remove ad-hoc prints afterwards.
- Flaky bugs come from timing, ordering, shared state, randomness, time zones, caching, or resource limits. Loop the test to measure the failure rate before and after the fix.
- Performance bugs: profile first (CPU, memory, I/O, queries) and optimise the measured hotspot only.
- Production incidents: mitigate first (roll back, flip a flag, scale), then root-cause from logs, metrics, and traces. Don't attach debuggers to live traffic.
- When stuck, re-check your assumptions: are you running the code you think you are (build cache, wrong branch, stale container, env vars)?

## Output format
- Symptom and repro steps
- Root cause with evidence
- Fix and regression test
- Follow-ups / similar risks

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Principles
- Systematic Debugging Process
- Debugging Tools
- Advanced Debugging Techniques
- Debugging Patterns by Issue Type
- Best Practices
- Common Debugging Mistakes
- Quick Debugging Checklist
