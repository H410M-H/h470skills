---
name: microservices-patterns
description: Design microservices architectures with service boundaries, event-driven communication, and resilience patterns. Use when building distributed systems, decomposing monoliths, or implementing microservices.
---

# Microservices Patterns

Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems.

## Use this skill when
- Decomposing monoliths into microservices
- Designing service boundaries and contracts
- Implementing inter-service communication
- Managing distributed data and transactions
- Building resilient distributed systems
- Implementing service discovery and load balancing
- Designing event-driven architectures

## Do not use this skill when
- The system is small enough for a modular monolith
- You need a quick prototype without distributed complexity
- There is no operational support for distributed systems

## Workflow
1. Identify domain boundaries and ownership for each service.
2. Define contracts, data ownership, and communication patterns.
3. Plan resilience, observability, and deployment strategy.
4. Provide migration steps and operational guardrails.

## Core rules
- Default to a modular monolith. Split out a service only for a proven need: independent deployability, scaling, fault isolation, or team autonomy.
- Draw boundaries by business capability or bounded context. Each service owns its data, with no shared database tables.
- Use asynchronous events for cross-service state propagation. Keep synchronous calls (REST or gRPC) for queries that need an immediate answer.
- Every remote call gets a timeout, retries with exponential backoff and jitter (idempotent operations only), a circuit breaker, and a bulkhead.
- Replace distributed transactions with sagas (orchestrated or choreographed) and compensating actions. Publish events through a transactional outbox, and make consumers idempotent by deduplicating on event ID.
- Keep contracts versioned and backward compatible, verified by consumer-driven contract tests (e.g. Pact).
- Build observability in from day one: structured logs, OpenTelemetry trace propagation, and RED metrics (rate, errors, duration) per service.
- Anti-patterns: chatty synchronous call chains, the distributed monolith (lock-step deploys), shared domain libraries, and one service per table.

## Output format
- Service map with ownership and data stores
- Communication matrix (sync/async, contracts)
- Resilience and observability plan
- Migration (strangler) steps

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Service Decomposition Patterns
- Communication Patterns
- Resilience Patterns
- Best Practices
- Common Pitfalls
