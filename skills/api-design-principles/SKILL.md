---
name: api-design-principles
description: Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications, or establishing API design standards.
---

# API Design Principles

Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time.

## Use this skill when
- Designing new REST or GraphQL APIs
- Refactoring existing APIs for better usability
- Establishing API design standards for your team
- Reviewing API specifications before implementation
- Migrating between API paradigms (REST to GraphQL, etc.)
- Creating developer-friendly API documentation
- Optimizing APIs for specific use cases (mobile, third-party integrations)

## Do not use this skill when
- You only need implementation guidance for a specific framework
- You are doing infrastructure-only work without API contracts
- You cannot change or version public interfaces

## Workflow
1. Identify consumers (public, partner, internal, mobile) and their top use cases.
2. Pick the style: REST for resource CRUD and caching, GraphQL for many client-shaped reads, gRPC for internal service-to-service.
3. Write the contract first (OpenAPI 3.1 or GraphQL SDL), lint it (e.g. Spectral), and review it before writing handlers.
4. Specify errors, pagination, auth, rate limits, and versioning explicitly, then validate with example requests/responses.

## Core rules
- Resources are plural nouns and HTTP methods carry the action: `POST /orders`, not `POST /createOrder`. Nest at most one level (`/users/{id}/orders`).
- Use precise status codes: 201 + `Location` on create, 204 on empty success, 400 malformed, 401 unauthenticated, 403 forbidden, 404, 409 conflict, 422 validation, 429 + `Retry-After`. 5xx only for server faults.
- One error envelope everywhere. Prefer RFC 9457 Problem Details (`application/problem+json`: `type`, `title`, `status`, `detail`, `instance`, plus a field-level `errors[]`).
- Paginate every collection from day one. Use cursors for large or changing data, cap `limit`, and return the next cursor/link.
- GET/PUT/DELETE must be idempotent. Accept an `Idempotency-Key` header on POSTs with side effects (payments, orders).
- Never break a published contract: make additive changes only, version with `/v1` or a header (pick one), and announce removals with `Deprecation`/`Sunset` headers.
- Be consistent: one JSON casing, ISO 8601 UTC timestamps, opaque string IDs, and the same filter/sort/fields query-parameter conventions on every endpoint.
- GraphQL: Relay-style connections for lists, one `input` argument per mutation, a payload type with `userErrors`, DataLoader against N+1, and depth/complexity limits on public endpoints.

## Output format
- Contract (OpenAPI/SDL) or endpoint table
- Error, pagination, auth and versioning decisions
- Example requests/responses
- Open questions and breaking-change risks

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- REST API Design Patterns
- GraphQL Design Patterns
- Best Practices
- Common Pitfalls
