# 🚀 h470skills — The Master Antigravity & Agentic Skills Repository

[![Antigravity](https://img.shields.io/badge/Google-Antigravity%20AGY-4285F4?style=flat-square&logo=google)](https://antigravity.google)
[![Skills Count](https://img.shields.io/badge/Skills-51%20Total-00C853?style=flat-square)](#-skills-inventory)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS-FF6F00?style=flat-square)](#-installation)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

**`h470skills`** is a curated, production-grade master repository of **51 Agent Skills** engineered for **Google Antigravity (`agy`)**, Antigravity IDE, Antigravity 2.0, and compatible AI agent runtimes.

It unifies:
1. **Google Antigravity Core Builtins**: The complete official system skills (customizations, automations, generative UI, dynamic workflows, and plugins).
2. **Missing & Power-User Skills**: Handcrafted specialized skills including `artemis-mobile-testing`, `termux-android-poweruser`, and `docker-containerization-expert`.
3. **Curated Production Skills**: Battle-tested playbooks across Next.js 15, React, TypeScript, FastAPI, PostgreSQL, Tailwind, CI/CD, and Security.
4. **Codebase Memories**: Deep architectural context packages for user projects (`emochipk`, `msns-build`, `msns-home`, `syncbay`, and `lms-android`).

---

## ⚡ Quick Installation

Clone or navigate to the repository and run the installer:

```bash
# Clone the repository
git clone https://github.com/h410m-h/h470skills.git ~/h470skills
cd ~/h470skills

# Option 1: Install globally for all workspaces (Default, symlinks to ~/.gemini/config/skills)
./install.sh

# Option 2: Install into current project (.agents/skills)
./install.sh --local

# Option 3: Hard-copy skills instead of symlinking
./install.sh --global --copy
```

---

## 🧠 How Antigravity Skills Work

In Google Antigravity, **skills** are structured runbooks (`skills/<name>/SKILL.md`) that teach agents specialized procedures, domain patterns, and tool workflows without polluting the model's base context window.

- **Progressive Disclosure**: Only skill names and descriptions are loaded initially. Full instructions and references are read into context only when triggered or activated.
- **Autonomous Activation**: The agent semantically evaluates user prompts against skill descriptions and loads relevant procedures automatically.
- **Manual Slash Commands**: Any skill can be explicitly activated by typing its name as a slash command in the chat box (e.g., `/artemis-mobile-testing`, `/nextjs-app-router-patterns`, `/database-optimizer`).

---

## 📦 Skills Inventory by Category

### 1. ⚙️ Antigravity Core & Builtin Skills
Official system skills packaged with Google Antigravity:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`agy-customizations`](./skills/agy-customizations/SKILL.md) | `/agy-customizations` | Master reference for the AGY Customization System (rules, skills, plugins, hooks, MCP). |
| [`antigravity_guide`](./skills/antigravity_guide/SKILL.md) | `/antigravity-guide` | Complete sitemap & docs for Antigravity CLI, IDE, 2.0 Desktop app, and Python SDK. |
| [`automation`](./skills/automation/SKILL.md) | `/automation` | Interactive guide to design and create scheduled background automations & cron sidecars. |
| [`generative_ui`](./skills/generative_ui/SKILL.md) | `/generative_ui` | Render rich interactive HTML widgets inline in chat or as standalone artifacts. |
| [`migrate-workflows`](./skills/migrate-workflows/SKILL.md) | `/migrate-workflows` | Autonomous migration of legacy `.agents/workflows/*.md` to modern skills format. |
| [`permissioned-github`](./skills/permissioned-github/SKILL.md) | `/permissioned-github` | Authoritative guidelines for using `gh` CLI and Git commands within permission boundaries. |
| [`plugin`](./skills/plugin/SKILL.md) | `/plugin` | Lifecycle management for AGY plugins (install, enable, disable, package). |
| [`run-workflow`](./skills/run-workflow/SKILL.md) | `/run-workflow` | Dynamic Python orchestration scripts using `agent`, `parallel`, `pipeline`, and `phase`. |
| [`ui-plugin-navigation`](./skills/ui-plugin-navigation/SKILL.md) | `/ui-plugin-navigation` | Discover and surface one-click UI plugin sidecar navigation pills in chat. |

---

### 2. 📱 Mobile & Hardware Engineering
Deep mobile testing, native Android integrations, and Termux power-user workflows:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`artemis-mobile-testing`](./skills/artemis-mobile-testing/SKILL.md) | `/artemis-mobile-testing` | Closed-loop mobile testing with ARTEMIS MCP, ADB diagnostics, and Dynamic-First/Coordinate-Fallback locating. |
| [`termux-android-poweruser`](./skills/termux-android-poweruser/SKILL.md) | `/termux-android-poweruser` | Termux Linux-on-Android runtime, toolchain setups, background wake locks, and `termux-api` hardware access. |
| [`lms-android-codebase`](./skills/lms-android-codebase/SKILL.md) | `/lms-android-codebase` | MSNS Mobile ERP & Capacitor 8 application codebase memory, offline SQLite sync, and native build pipelines. |

---

### 3. ☁️ Cloud, Database & Backend Architecture
Serverless cloud primitives, API engineering, database profiling, and distributed systems:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`neon`](./skills/neon/SKILL.md) | `/neon` | Complete cloud backend primitives (Lakebase Postgres, Auth, Data API, S3, AI Gateway). |
| [`neon-postgres`](./skills/neon-postgres/SKILL.md) | `/neon-postgres` | Deep dive into Lakebase Postgres: scale-to-zero, autoscaling, connection pooling, and vector search. |
| [`database-optimizer`](./skills/database-optimizer/SKILL.md) | `/database-optimizer` | SQL query profiling, index strategies (B-Tree, GIN, BRIN), `EXPLAIN ANALYZE`, and deadlock prevention. |
| [`postgresql`](./skills/postgresql/SKILL.md) | `/postgresql` | PostgreSQL features, JSONB queries, CTEs, window functions, concurrency control, and pooling. |
| [`fastapi-pro`](./skills/fastapi-pro/SKILL.md) | `/fastapi-pro` | High-performance Python APIs, Pydantic v2 schemas, async routes, dependency injection, and OpenAPI. |
| [`python-pro`](./skills/python-pro/SKILL.md) | `/python-pro` | Modern Python 3.12+, async/await concurrency, type protocols, packaging with uv/poetry, profiling. |
| [`typescript-advanced-types`](./skills/typescript-advanced-types/SKILL.md) | `/typescript-advanced-types` | Conditional types, template literals, type guards, mapped types, brand types, strict inference. |
| [`api-design-principles`](./skills/api-design-principles/SKILL.md) | `/api-design-principles` | RESTful and RPC API contract design, error formatting, versioning, pagination, idempotency. |
| [`backend-architect`](./skills/backend-architect/SKILL.md) | `/backend-architect` | Distributed systems, modular monoliths, caching layers (Redis), event-driven patterns. |
| [`microservices-patterns`](./skills/microservices-patterns/SKILL.md) | `/microservices-patterns` | Service decomposition, resilience patterns, circuit breakers, saga orchestration, event sourcing. |
| [`auth-implementation-patterns`](./skills/auth-implementation-patterns/SKILL.md) | `/auth-implementation-patterns` | OAuth 2.0, JWT, session management, RBAC, secure tokens, PKCE, SSO. |
| [`stripe-integration`](./skills/stripe-integration/SKILL.md) | `/stripe-integration` | Payment processing, webhooks, idempotency, checkout sessions, customer billing lifecycle. |

---

### 4. 🎨 Frontend, UI/UX & Design Systems
Full-stack React, App Router, responsive styling, and accessible web interfaces:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`nextjs-app-router-patterns`](./skills/nextjs-app-router-patterns/SKILL.md) | `/nextjs-app-router-patterns` | Next.js 14/15 App Router architecture, Server Components, streaming SSR, parallel routes, Server Actions. |
| [`react-modernization`](./skills/react-modernization/SKILL.md) | `/react-modernization` | Modern React patterns, migrating Class components/legacy hooks, React 19 transitions, Suspense. |
| [`react-state-management`](./skills/react-state-management/SKILL.md) | `/react-state-management` | Zustand, TanStack Query, React Context, optimistic updates, server state synchronization. |
| [`tailwind-design-system`](./skills/tailwind-design-system/SKILL.md) | `/tailwind-design-system` | Design systems, token architecture, Radix/shadcn UI styling, dark mode, responsive fluid typography. |
| [`ui-ux-designer`](./skills/ui-ux-designer/SKILL.md) | `/ui-ux-designer` | Component design, visual hierarchy, UX heuristics, micro-interactions, responsive accessibility. |
| [`wcag-audit-patterns`](./skills/wcag-audit-patterns/SKILL.md) | `/wcag-audit-patterns` | Web accessibility auditing, screen reader compatibility, ARIA semantics, color contrast validation. |
| [`preview`](./skills/preview/SKILL.md) | `/preview` | Interactive visual explanations, slides, diagrams, markdown & self-contained HTML previews. |

---

### 5. 🛠️ DevOps, Quality & Workflow Acceleration
Infrastructure as code, CI/CD, testing, refactoring, security auditing, and developer tooling:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`docker-containerization-expert`](./skills/docker-containerization-expert/SKILL.md) | `/docker-containerization-expert` | Multi-stage Docker builds, Alpine/Distroless hardening, layer caching, compose production orchestration. |
| [`deployment-pipeline-design`](./skills/deployment-pipeline-design/SKILL.md) | `/deployment-pipeline-design` | Multi-stage CI/CD pipelines with approval gates, GitHub Actions, Docker caching, zero-downtime releases. |
| [`turborepo-caching`](./skills/turborepo-caching/SKILL.md) | `/turborepo-caching` | Monorepo architecture, task pipelines, remote caching, workspace dependency graphs. |
| [`e2e-testing-patterns`](./skills/e2e-testing-patterns/SKILL.md) | `/e2e-testing-patterns` | End-to-end testing, Playwright, page object models, test fixtures, CI/CD browser testing. |
| [`debugging-strategies`](./skills/debugging-strategies/SKILL.md) | `/debugging-strategies` | Root cause analysis, bisection, logging instrumentation, state reproduction, memory leak hunting. |
| [`performance-engineer`](./skills/performance-engineer/SKILL.md) | `/performance-engineer` | Web performance optimization, Core Web Vitals (LCP, FID, CLS), bundle size reduction, memory profiling. |
| [`git-advanced-workflows`](./skills/git-advanced-workflows/SKILL.md) | `/git-advanced-workflows` | Interactive rebasing, atomic commits, squash merges, cherry-picking, complex conflict resolution. |
| [`git-pr-workflows-git-workflow`](./skills/git-pr-workflows-git-workflow/SKILL.md) | `/git-pr-workflows-git-workflow` | PR creation, conventional commit standards, branch naming, changelog automation. |
| [`security-auditor`](./skills/security-auditor/SKILL.md) | `/security-auditor` | Comprehensive vulnerability scanning, secret detection, input sanitization, OWASP Top 10 mitigation. |
| [`code-review-excellence`](./skills/code-review-excellence/SKILL.md) | `/code-review-excellence` | Systematic code review checklists, cognitive complexity analysis, edge-case auditing. |
| [`code-refactoring-refactor-clean`](./skills/code-refactoring-refactor-clean/SKILL.md) | `/code-refactoring-refactor-clean` | Clean code principles, DRY/SOLID refactoring, eliminating technical debt safely. |
| [`architecture-patterns`](./skills/architecture-patterns/SKILL.md) | `/architecture-patterns` | Clean Architecture, Hexagonal/Ports & Adapters, Domain-Driven Design (DDD), CQRS. |
| [`mermaid-expert`](./skills/mermaid-expert/SKILL.md) | `/mermaid-expert` | Advanced architecture diagrams, sequence flows, ERDs, state machines, Gantt charts. |
| [`prompt-engineering-patterns`](./skills/prompt-engineering-patterns/SKILL.md) | `/prompt-engineering-patterns` | Few-shot prompting, chain-of-thought, system prompt optimization, structured JSON output. |
| [`seo-structure-architect`](./skills/seo-structure-architect/SKILL.md) | `/seo-structure-architect` | Technical SEO, schema markup, Core Web Vitals, sitemaps, OpenGraph metadata. |
| [`antigravity-skills-manager`](./skills/antigravity-skills-manager/SKILL.md) | `/antigravity-skills-manager` | Search, install, update, and manage community skills directly within Antigravity. |

---

### 6. 🏛️ Private Codebase Memories
Persistent architectural memory packages for key project codebases:

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| [`emochipk-codebase`](./skills/emochipk-codebase/SKILL.md) | `/emochipk-codebase` | Executive Mochi (emochipk) e-commerce platform codebase memory & architecture. |
| [`msns-build-codebase`](./skills/msns-build-codebase/SKILL.md) | `/msns-build-codebase` | MSNS-build LMS/ERP project architecture memory, tRPC routes, and schema. |
| [`msns-home-codebase`](./skills/msns-home-codebase/SKILL.md) | `/msns-home-codebase` | MSNS-home public website architecture, SEO, and CMS integrations. |
| [`syncbay-codebase`](./skills/syncbay-codebase/SKILL.md) | `/syncbay-codebase` | Syncbay PaaS platform memory, hybrid compute orchestration, and preview pipeline. |

---

## 📂 Repository Directory Structure

```text
h470skills/
├── .git/
├── README.md               # Master guide and inventory
├── CATALOG.md              # Detailed categorized catalog with full descriptions
├── skills.json             # Machine-readable skill manifest
├── install.sh              # One-command installer (global or local)
├── generate_manifest.py    # Automation script to rebuild catalog & manifest
└── skills/                 # All 51 skill runbooks
    ├── agy-customizations/
    ├── antigravity_guide/
    ├── artemis-mobile-testing/
    ├── docker-containerization-expert/
    ├── nextjs-app-router-patterns/
    ├── termux-android-poweruser/
    └── ... (51 skills)
```

---

## 📜 Complete Catalogue Reference

For the comprehensive catalog with detailed triggers, scenarios, and instructions for every skill, see **[CATALOG.md](./CATALOG.md)**.
