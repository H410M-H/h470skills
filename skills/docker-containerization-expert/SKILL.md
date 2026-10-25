---
name: docker-containerization-expert
description: >-
  Expert patterns for writing secure, production-grade, multi-stage Dockerfiles,
  docker-compose configurations, and image optimization strategies. Use when containerizing
  applications, optimizing Docker image sizes, setting up local development compose environments,
  or building multi-platform (ARM64/AMD64) images.
---

# Docker Containerization Expert

Master patterns for authoring secure, minimal, reproducible container images and orchestration configurations across Node.js, Next.js, Python, and Go.

## When to Use This Skill

- Authoring `Dockerfile` or `docker-compose.yml` for new or existing projects.
- Reducing container image size (using Alpine, Chainguard, or Distroless).
- Fixing container permission bugs, multi-stage layer caching, and rootless user security.
- Configuring development environments with live reload volumes.
- Cross-compiling for multiple architectures (ARM64, AMD64) using Buildx.

---

## 1. Production Dockerfile Best Practices

### The Gold Standard Checklist
1. **Multi-Stage Builds**: Separate dependencies/build stages from runtime images.
2. **Non-Root Execution**: Never run application processes as `root`. Create a dedicated user (`USER node` or `USER appuser`).
3. **Explicit Layer Caching**: Copy lockfiles first (`package.json`, `pnpm-lock.yaml`, `requirements.txt`), run dependency install, and only then copy application source code.
4. **Clean Cache**: Remove package manager caches (`npm cache clean --force`, `rm -rf /var/cache/apk/*`, `pip install --no-cache-dir`).
5. **Use `.dockerignore`**: Always exclude `.git`, `node_modules`, `dist`, `.env*`, and log files.

---

## 2. Framework Templates

### Next.js Standalone Dockerfile
```dockerfile
# 1. Base
FROM node:20-alpine AS base
WORKDIR /app
RUN apk add --no-cache libc6-compat

# 2. Dependencies
FROM base AS deps
COPY package.json pnpm-lock.yaml* package-lock.json* yarn.lock* ./
RUN \
  if [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm ci; \
  else yarn install --frozen-lockfile; fi

# 3. Builder
FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

# 4. Runner
FROM base AS runner
ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
ENV PORT 3000
CMD ["node", "server.js"]
```

### Python FastAPI Production Dockerfile
```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml requirements.txt* ./
RUN uv pip install --no-cache --system -r requirements.txt

# Final runtime
FROM python:3.12-slim AS runner
WORKDIR /app
RUN groupadd -g 1001 appgroup && useradd -u 1001 -g appgroup -m appuser

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --chown=appuser:appgroup . /app

USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 3. Docker Compose Production Patterns
Always use modern Compose syntax (`compose.yaml`):
```yaml
services:
  app:
    build:
      context: .
      target: runner
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:password@db:5432/app
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d app"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```
