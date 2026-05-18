---
name: environment-scaffolding
description: Create Docker, .env, and README setups that guarantee environment consistency for any tech stack
code: ES
---

# Environment Scaffolding

Create ready-to-run environment setups — Docker files, .env templates, and README instructions — so every exercise runs identically on any machine. No "works on my machine" exceptions.

## What Success Looks Like

The owner has a complete, runnable environment setup that any student can clone, build, and run without friction. Zero guesswork about dependencies, versions, or configuration. The `docker-compose up` command should Just Work.

## Your Approach

### The Stack Audit

Before generating any scaffolding, understand what's needed:

1. **Read `curriculum-design.md` and `knowledge-base.md`** from project memory to understand the tech stack and exercise context
2. **Clarify the stack** — What language, runtime version, database, and framework? Pin exact versions.
3. **Identify dependencies** — What does the student need installed vs. what Docker provides?
4. **Determine isolation level** — Single container for simple exercises, multi-container for full-stack

### Scaffolding Components

Every environment setup must include:

| Component | Purpose | Non-Negotiable |
|-----------|---------|----------------|
| `Dockerfile` or `docker-compose.yml` | Environment consistency | **Always** required |
| `.env.example` | Configuration template without secrets | Variables with sensible defaults |
| `README.md` | Setup and run instructions | Step-by-step, tested commands |
| `.dockerignore` | Keep images lean | Exclude node_modules, .git, etc. |

### Dockerfile Principles

- **Pin versions** — `node:20.11-alpine`, not `node:latest`
- **Multi-stage builds** for production-relevant patterns when appropriate
- **Non-root user** in container (security best practice)
- **Health checks** for multi-service setups
- **Volume mounts** for hot-reload during development
- **Minimal images** — Alpine-based when possible

### README Structure

```markdown
## Prerequisites
- Docker & Docker Compose installed

## Quick Start
1. Clone this repo
2. Copy `.env.example` to `.env`
3. Run `docker-compose up`
4. Open localhost:XXXX

## Troubleshooting
Common issues and fixes

## Stopping
`docker-compose down`
```

### Progressive Complexity

- **Beginner exercises** — Single Dockerfile, minimal configuration
- **Intermediate** — docker-compose with services, environment variables
- **Advanced** — Multi-service orchestration, networking, volumes

## Memory Integration

- Read `knowledge-base.md` for validated tech stack information
- Read BOND.md for the owner's Docker experience level and format preferences
- Read MEMORY.md for previously used environment setups that worked
- Write generated scaffolding to `{project-root}/.ssconfig/memory/crs/curated/content-drafts/`

## After the Session

Log which stack was scaffolded and any decisions made (version pins, service architecture choices). Note if the owner has preferences about Docker vs. docker-compose approach. Update MEMORY.md with successful environment patterns. Write scaffolding files to `content-drafts/`.