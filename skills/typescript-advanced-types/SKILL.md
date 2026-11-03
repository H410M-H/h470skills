---
name: typescript-advanced-types
description: Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications. Use when implementing complex type logic, creating reusable type utilities, or ensuring compile-time type safety in TypeScript projects.
---

# TypeScript Advanced Types

Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for building robust, type-safe applications.

## Use this skill when
- Building type-safe libraries or frameworks
- Creating reusable generic components
- Implementing complex type inference logic
- Designing type-safe API clients
- Building form validation systems
- Creating strongly-typed configuration objects
- Implementing type-safe state management
- Migrating JavaScript codebases to TypeScript

## Core rules
- The baseline is `"strict": true` plus `noUncheckedIndexedAccess`. Prefer inference internally, and annotate exported function signatures and public types.
- Use `unknown` instead of `any`. Narrow with `typeof`/`instanceof`/`in`, user-defined type guards, and assertion functions.
- Model state as discriminated unions and make switches exhaustive with a `never` check (`const _exhaustive: never = x`).
- Use `satisfies` to check a value against a type while keeping its literal type, and `as const` (or `const` type parameters) to preserve literals.
- Constrain generics (`<T extends Record<string, unknown>>`). If a type parameter is used only once, you probably don't need it.
- Conditional types distribute over unions; wrap as `[T] extends [U]` to stop that. Use `infer` to extract, and mapped types with `as` key remapping plus template literal types to derive APIs.
- Brand primitives that must not mix (`type UserId = string & { readonly __brand: 'UserId' }`).
- Validate runtime data at boundaries (zod, valibot, arktype) and infer types from the schema instead of duplicating them.
- Keep the compiler fast: avoid deeply recursive types, prefer `interface extends` over large intersections, and test types with `expectTypeOf`, `tsd`, or `// @ts-expect-error`.

## Output format
- Type definitions with brief rationale
- Usage examples that compile
- Type tests for tricky cases

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Advanced Patterns
- Type Inference Techniques
- Best Practices
- Type Testing
- Common Pitfalls
- Performance Considerations
