---
name: code-review-excellence
description: Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining team morale. Use when reviewing pull requests, establishing review standards, or mentoring developers.
---

# Code Review Excellence

Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

## Use this skill when
- Reviewing pull requests and code changes
- Establishing code review standards
- Mentoring developers through review feedback
- Auditing for correctness, security, or performance

## Do not use this skill when
- There are no code changes to review
- The task is a design-only discussion without code
- You need to implement fixes instead of reviewing

## Workflow
1. Read the PR description, the linked issue, and the tests first, so you know the intent before you judge the code.
2. Skim the whole diff for shape (files, size, risky areas), then review in depth.
3. Run or reason through the risky paths. Check that the tests would fail without the change.
4. Write findings grouped by severity, each with a location and a concrete suggestion. Then give the verdict.

## Core rules
- Review in priority order: correctness → security → data/migration safety → performance → API/design → readability. Leave formatting and style to linters.
- Hunt at the edges: error paths, null/empty inputs, concurrency and races, off-by-one, time zones, retries/idempotency, backward compatibility, and rollback safety.
- Label every comment: **blocking**, **should-fix**, **nit**, **question**, or **praise**. Cite `file:line` and propose the fix.
- Critique the code, not the person. Ask ("What happens if `items` is empty?") rather than command, and explain *why*.
- Ask for large mixed PRs (≳ 400 changed lines, or refactor + feature together) to be split.
- Approve when the change is safe and leaves the codebase better than before. Perfect is not the bar.

## Output format
- One-paragraph summary and verdict (approve / request changes / comment)
- Findings grouped by severity with file:line
- Questions for the author
- Test and coverage notes

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Principles
- Review Process
- Review Techniques
- Language-Specific Patterns
- Advanced Review Patterns
- Giving Difficult Feedback
- Best Practices
- Common Pitfalls
- Templates
