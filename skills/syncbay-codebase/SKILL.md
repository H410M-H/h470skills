---
name: syncbay-codebase
description: Comprehensive codebase memory for the Syncbay PaaS platform project. Use this skill to recall the architecture, hybrid compute orchestration, edge routing middleware, PR preview pipeline, and daemon runner architecture.
---

# Syncbay PaaS Codebase Memory

## Architecture Overview
Syncbay is a Vercel/Railway-class PaaS platform built with Next.js, tRPC, and Prisma.
It leverages a hybrid compute execution layer and an automated global edge routing fabric.

### 1. Control Plane & Orchestration
- **Deployment Engine** (`src/lib/orchestrator/engine.ts`): Triggers deployments, detects runtimes, runs Knip code quality analysis, dispatches builds to the runner daemon via `RunnerDriverFactory`, probes health endpoints (`/health` and root `/`), and registers edge routes.
- **PR Manager** (`src/lib/orchestrator/pr-manager.ts`): Processes GitHub webhooks to manage ephemeral preview environments, handles scale-to-zero sleeping, teardown hooks, and GitHub commit status updates.
- **Runner Drivers** (`src/lib/orchestrator/runner-driver.ts`): Extensible interface (`WebhookRunnerDriver`, `QueueRunnerDriver`, `SshRunnerDriver`, `LocalRunnerDriver`) for executing builds.
- **Serverless Fallback** (`runner/src/pipeline.ts`): Gracefully handles execution on serverless platforms (e.g. Vercel) by dynamically falling back to a `MockPipelineExecutor` when native tools (`git`, `docker`) are absent, producing realistic streaming logs and simulating deployments.
- **Redeploy & Rebuild Subsystem** (`src/server/routers/deployment.ts`): Fast redeploy (`rebuild: false`) rotates instances using existing validated build IDs; clean rebuild (`rebuild: true`) purges build artifacts (`node_modules`, `dist`, `.next`, `build`, `out`), applies `--no-cache`, and generates a fresh build record. Failed deployments automatically force a clean rebuild on retry.
- **Error Diagnostics & Log Stream Classification** (`src/lib/orchestrator/engine.ts` & `runner/src/pipeline.ts`): Binds `{ onLog: log }` to all execution phases. Lines matching `[build:error]`, `[app:stderr]`, or compiler syntax errors route to `stderr` and record into `logEventBus`. The runner buffers the last 25 lines of process startup `stderr` to surface exact crash traces and exit codes if health checks fail.

### 2. Execution Daemon (`runner/`)
- A standalone containerized agent (`runner/src/index.ts` & `runner/src/pipeline.ts`).
- Normalizes git clones (e.g., `owner/repo` to `https://github.com/...`) and injects OAuth credentials.
- Detects project types and installs dependencies (`npm install`, `pnpm`, `yarn`) before executing build commands.
- Dynamically allocates host ports and spawns native child processes or Docker containers.
- Prioritizes compiled distribution output (`dist`, `build`, `out`) over source directories for live production serving.
- Enforces strict health checks and monitors child process lifecycle (`error`, `exit`).

### 3. Edge Ingress & Routing
- **Edge Service Registry** (`src/lib/edge/service-registry.ts`): An Edge-Runtime compatible in-memory registry resolving case-insensitive subdomains and `.localhost` counterparts to target ports.
- **Next.js Middleware** (`src/middleware.ts`): Transparently intercepts wildcard requests. If a service is `ACTIVE` in the registry, it proxies traffic to the upstream URL (e.g. `http://127.0.0.1:<port>`). Otherwise, it rewrites traffic to the preview splash screen.
- **Cold-Start UX** (`src/app/service-preview/[subdomain]/page.tsx`): Real-time pulsing status UI with SSE live build logs and a client-side `/health` polling probe that triggers an automatic page refresh upon `200 OK`.

## Key Dependencies & Integrations
- **Database**: PostgreSQL (via Prisma Adapter).
- **Compute Drivers**: Local native processes, mock simulators, Docker CLI, Nixpacks.
- **Tunneling**: Cloudflare Tunnels (generated via `src/lib/tunnel/tunnel-config.ts`).
- **Webhooks**: GitHub App integrations for push/PR triggers.
