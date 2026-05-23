---
name: exercise-generation
description: Create graded coding exercises from fill-in-the-blank to build-from-scratch, with proper difficulty tiers
code: EG
---

# Exercise Generation

Create coding exercises that teach through doing — from gentle fill-in-the-blank to full build-from-scratch challenges. Every exercise must be runnable, testable, and accompanied by environment setup.

## What Success Looks Like

The owner has a set of exercises that students can actually run, submit, and get feedback on. Each exercise is clearly scoped, has a difficulty tier, includes starter code where appropriate, and comes with a Dockerfile or docker-compose.yml. No exercise is just a text description — everything is executable.

## Your Approach

### Difficulty Tiers

| Tier | Type | Student Does | Example |
|------|------|-------------|---------|
| **Tier 1** | Fill-in-the-blank | Replace `___` placeholder with correct code | Complete a function body |
| **Tier 2** | Guided build | Follow step-by-step instructions to write code | Build a REST endpoint with spec |
| **Tier 3** | Build from spec | Implement from requirements, no starter code | Create a module that passes given tests |
| **Tier 4** | Open challenge | Solve an open-ended problem with constraints | Design and implement a rate limiter |

### Exercise Anatomy

Every exercise includes:

1. **Objective** — Clear, measurable learning outcome
2. **Starter code** — Template with `___` placeholders (Tier 1-2) or empty scaffolding (Tier 3)
3. **Test suite** — Unit tests that validate correctness (can use [AG] capability)
4. **Docker setup** — `Dockerfile` or `docker-compose.yml` for environment consistency
5. **Solution** — Reference solution stored separately
6. **Hints** — Progressive hints that don't give away the answer

### Exercise Design Principles

- **One concept per Tier 1 exercise** — Don't mix async/await and error handling in one blank

### Style Alignment
Before generating exercises, read `{project-root}/.ssconfig/memory/crs/{active-project}/project-config.yaml` to get `style_file`. Load `{skill-root}/../{style_file}` and read the Structure Template and Output Goals sections. Exercise format, naming convention, and deliverable structure must match the selected style (e.g., Scrimba uses 3-tier hints + automated tests; Pluralsight uses production-quality code + module checks; Udemy uses starter + solution files).
- **Progressive dependency** — Later exercises build on concepts from earlier ones
- **Runnable before solving** — Student should be able to run code immediately, even if it fails
- **Meaningful failure** — Wrong answers should produce informative errors, not silent wrong results
- **Real-world relevance** — Exercises resemble actual development tasks, not toy problems

### Starter Code Format

```language
// exercise-01-solution.js
// TODO: Replace ___ with the correct code

function greetUser(name) {
  return `Hello, ___!`
}

module.exports = { greetUser }
```

### Naming Convention

```
content-drafts/
├── exercises/
│   ├── module-01/
│   │   ├── exercise-01-fill-blank/
│   │   │   ├── starter/
│   │   │   │   └── solution.js
│   │   │   ├── tests/
│   │   │   │   └── solution.test.js
│   │   │   ├── Dockerfile
│   │   │   └── README.md
│   │   ├── exercise-02-guided/
│   │   │   └── ...
```

## Memory Integration

- Read `curriculum-design.md` to align exercises with module structure and learning objectives
- Read `knowledge-base.md` for validated technical content
- Read BOND.md for the owner's preferred exercise format and difficulty calibration
- Read MEMORY.md for exercise patterns that worked well previously
- Write exercises to `{project-root}/.ssconfig/memory/crs/{active-project}/curated/content-drafts/`

## After the Session

Log which exercises were created and their difficulty tiers. Note which concepts were easy vs. hard to design exercises for. Track exercise patterns that produce the best learning outcomes. Update MEMORY.md with effective exercise structures.