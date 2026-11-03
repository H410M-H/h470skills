---
name: nextjs-app-router-patterns
description: >-
  Next.js App Router patterns for Next.js 14, 15 and 16: Server Components, client
  islands, streaming with Suspense, parallel and intercepting routes, Server Actions,
  caching and revalidation (including Next 15 uncached-by-default fetch and Next 16 'use
  cache' / Cache Components / proxy.ts). Use when building or reviewing Next.js App Router
  code, migrating from the Pages Router, upgrading between Next.js majors, or debugging
  data fetching, caching, or rendering behavior.
---

# Next.js App Router Patterns

Comprehensive patterns for Next.js 14–16 App Router architecture, Server Components, and modern full-stack React development.

## Use this skill when
- Building new Next.js applications with App Router
- Migrating from Pages Router to App Router
- Implementing Server Components and streaming
- Setting up parallel and intercepting routes
- Optimizing data fetching and caching
- Building full-stack features with Server Actions

## Workflow
1. Check the installed version (`next` in package.json). APIs differ between 14, 15, and 16 (see Version notes).
2. Sketch the route tree: layouts, route groups `(group)`, dynamic segments, parallel `@slot` and intercepting `(.)` routes.
3. Decide per route: static, dynamic, or streamed. Then decide what is cached, and how it is revalidated.
4. Implement Server Components first, add client islands, wire mutations through Server Actions, and verify with `next build` output.

## Core rules
- Components are Server Components by default. Add `'use client'` only at interactive leaves, pass them serialisable props, and keep secrets server-side (`import 'server-only'`).
- Fetch on the server, close to where data is used, in parallel (`Promise.all`) to avoid waterfalls. Stream slow parts with `loading.tsx` or `<Suspense>`.
- Do mutations in Server Actions (`'use server'`). Validate input (e.g. zod) and re-check authentication/authorisation **inside every action**, then `revalidatePath` / `revalidateTag` / `redirect`.
- Use `error.tsx` (must be a Client Component), `not-found.tsx`, and `global-error.tsx` for failure states.
- Use `generateMetadata` for SEO, `generateStaticParams` to pre-render dynamic routes, and `next/image`, `next/font`, `next/link` for assets and navigation.
- Parallel routes need a `default.tsx` for unmatched slots. Modals = parallel slot + intercepting route.
- Read `next build` output to confirm each route's static/dynamic status. One stray `cookies()` call makes the whole route dynamic.

## Version notes
- **Next.js 15**: `params`, `searchParams`, `cookies()`, `headers()`, and `draftMode()` are async, so `await` them. `fetch` requests and GET route handlers are **no longer cached by default**: opt in with `cache: 'force-cache'` or `next: { revalidate }`. Ships with React 19.
- **Next.js 16**: Cache Components (`cacheComponents: true`) with the `'use cache'` directive plus `cacheLife` / `cacheTag`. `revalidateTag(tag, profile)` takes a cacheLife profile as its second argument, and `updateTag()` gives read-your-writes inside Server Actions. `middleware.ts` is renamed `proxy.ts`. Turbopack is the default bundler. Synchronous access to request APIs is removed.
- **Next.js 14** projects: `params` are plain objects and `fetch` is cached by default. Don't apply the 15+ patterns blindly.

## Output format
- Route tree
- Rendering/caching decision per route
- Code (server components, client islands, actions)
- Verification (`next build` route table)

## Playbook
Open `resources/implementation-playbook.md` when you need full code samples. It covers:

- Core Concepts
- Quick Start
- Patterns
- Caching Strategies
- Best Practices
