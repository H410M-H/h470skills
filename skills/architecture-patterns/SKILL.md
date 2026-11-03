---
name: architecture-patterns
description: Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use when architecting complex backend systems or refactoring existing applications for better maintainability.
---

# Architecture Patterns

Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build maintainable, testable, and scalable systems.

## Use this skill when
- Designing new backend systems from scratch
- Refactoring monolithic applications for better maintainability
- Establishing architecture standards for your team
- Migrating from tightly coupled to loosely coupled architectures
- Implementing domain-driven design principles
- Creating testable and mockable codebases
- Planning microservices decomposition

## Do not use this skill when
- You only need small, localized refactors
- The system is primarily frontend with no backend architecture changes
- You need implementation details without architectural design

## Workflow
1. Map the domain: core vs. supporting subdomains, invariants, and the team(s) that own them.
2. Match the pattern to the complexity. CRUD-heavy work → layered or modular monolith. Rich business rules → Clean/Hexagonal plus DDD tactical patterns.
3. Define module boundaries, ports (interfaces), and the dependency rule. Record each decision as an ADR.
4. Plan an incremental (strangler) migration with tests at each step instead of a big-bang rewrite.

## Core rules
- Dependency rule: source code dependencies point inward. Domain code imports nothing from frameworks, ORMs, HTTP, or queues.
- The core owns its ports (interfaces). Adapters (DB, HTTP, messaging, external APIs) implement them and are wired up in one composition root.
- Use cases (application services) orchestrate a single business operation and own the transaction. Entities enforce their own invariants.
- Value objects are immutable and validated at construction. Entities have identity. Aggregates are consistency boundaries: reference other aggregates by ID and modify one aggregate per transaction.
- Use domain events for cross-aggregate side effects. Publish externally through a transactional outbox, not inline.
- Repositories exist per aggregate root and return domain objects, never ORM rows or query builders.
- Testing follows the layers: fast domain unit tests with no I/O, use-case tests with in-memory fake adapters, and a few adapter integration tests.
- Don't impose DDD ceremony on simple CRUD. Too many layers is as costly as too few.

## Output format
- Chosen pattern and why (ADR style)
- Module/package layout and dependency rules
- Port and adapter list
- Migration steps with checkpoints

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Clean Architecture Pattern
- Hexagonal Architecture Pattern
- Domain-Driven Design Pattern
- Best Practices
- Common Pitfalls
