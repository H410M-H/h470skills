---
name: auth-implementation-patterns
description: Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing APIs, or debugging security issues.
---

# Authentication & Authorization Implementation Patterns

Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices.

## Use this skill when
- Implementing user authentication systems
- Securing REST or GraphQL APIs
- Adding OAuth2/social login or SSO
- Designing session management or RBAC
- Debugging authentication or authorization issues

## Do not use this skill when
- You only need UI copy or login page styling
- The task is infrastructure-only without identity concerns
- You cannot change auth policies or credential storage

## Workflow
1. Define actors, tenants, clients (web, mobile, machine), and the threat model.
2. Choose the mechanism: server sessions for first-party web, OIDC/OAuth2 for SSO and third-party clients, short-lived JWTs for stateless APIs.
3. Design authorization (RBAC, ABAC, or ReBAC) and decide where it is enforced.
4. Plan secret storage, key rotation, audit logging, and account recovery before you ship.

## Core rules
- Prefer a vetted provider or library (an OIDC provider, Auth.js, or the framework's auth module) over hand-rolled crypto or token handling.
- Hash passwords with Argon2id (or bcrypt cost ≥ 12). Rate-limit and back off on login, screen against breached-password lists, and offer MFA (TOTP, WebAuthn/passkeys).
- Session cookies: `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`. Rotate the session ID on login and on privilege change, and support server-side revocation.
- JWTs: short-lived access tokens (5–15 min) plus rotating refresh tokens with reuse detection. Pin the algorithm (reject `none` and alg confusion) and validate `iss`, `aud`, `exp`, and `nbf`. Avoid `localStorage` where XSS is a risk.
- OAuth 2.1 / OIDC: Authorization Code + PKCE for every client type. Implicit and password grants are deprecated. Validate `state` and `nonce`, and match redirect URIs exactly.
- Authorization denies by default and is enforced server-side at every entry point. Always check object ownership (IDOR/BOLA) and centralise policy instead of scattering `if` checks.
- Protect cookie-authenticated state-changing requests from CSRF. Use a CORS allowlist and never `*` with credentials.
- Keep keys in a secret manager and rotate signing keys via `kid`/JWKS. Log auth events without tokens or passwords, and return uniform errors so attackers can't enumerate users.

## Safety
- Never log secrets, tokens, or credentials.
- Enforce least privilege and secure storage for keys.

## Output format
- Chosen flow(s) with sequence diagram
- Token/session lifecycle table
- Authorization model and enforcement points
- Security checklist results

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- JWT Authentication
- Session-Based Authentication
- OAuth2 / Social Login
- Authorization Patterns
- Security Best Practices
- Best Practices
- Common Pitfalls
