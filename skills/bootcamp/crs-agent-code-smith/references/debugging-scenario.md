---
name: debugging-scenario
description: Create intentionally broken code that trains debugging instincts through realistic failure patterns
code: DS
---

# Debugging Scenario Crafting

Create code that's broken on purpose — but broken in ways that teach. Every bug is a lesson. Every fix builds debugging instinct. No random typos — every error must be logically instructive.

## What Success Looks Like

The owner has debugging exercises where students learn to read error messages, trace execution flow, and develop systematic debugging habits. Each scenario is realistically broken, has a clear learning objective, and comes with progressive hints that teach rather than reveal.

## Your Approach

### Bug Categories

| Category | What It Teaches | Example |
|----------|----------------|---------|
| **Logic Error** | Correctness reasoning — code runs but produces wrong results | Off-by-one, wrong comparison operator, inverted condition |
| **Syntax Error** | Reading error messages carefully | Missing bracket, wrong keyword, misplaced semicolon in specific contexts |
| **Runtime Error** | Understanding program state and execution flow | Null reference, type coercion, accessing undefined property |
| **Performance Trap** | Identifying inefficiency, algorithmic thinking | O(n²) where O(n) works, unnecessary re-renders, N+1 queries |
| **Async Pitfall** | Handling asynchronous code correctly | Race condition, unhandled promise, callback ordering |

### Difficulty Progression

- **Level 1** — Single bug, obvious error message, close to the surface
- **Level 2** — Single bug, requires reading stack trace or understanding context
- **Level 3** — Multiple interacting bugs, some symptoms are red herrings
- **Level 4** — Subtle logic error with no error message, tests pass but behavior is wrong

### Scenario Design Principles

- **Realistic** — Bugs should resemble mistakes developers actually make, not puzzles for puzzle's sake
- **Instructive** — Each bug should teach a specific debugging skill (reading stack traces, checking assumptions, isolating variables)
- **Progressive hints** — Three levels:
  1. Direction hint ("perhatikan loop condition")
  2. Narrowing hint ("cek perbandingan di baris 15")
  3. Near-answer ("operator `=` bukan `==`")
- **Runnable** — Student must be able to run the code and see it fail
- **Dockerfile included** — Environment consistency, no exceptions

### Scenario Structure

```
content-drafts/
├── debugging/
│   ├── scenario-01-logic-error/
│   │   ├── buggy/
│   │   │   ├── src/
│   │   │   ├── Dockerfile
│   │   │   └── README.md (scenario description, no hints)
│   │   ├── stable/
│   │   │   └── src/  (working reference for crafting bugs)
│   │   ├── hints.md  (progressive hints)
│   │   └── solution.md  (explanation of bug + fix)
```

### Bug Crafting Process

1. **Start with working code** — Write the correct solution first (stable/)
2. **Choose the lesson** — What debugging skill should this teach?
3. **Introduce the bug** — Modify stable code to create the target error type
4. **Verify the bug** — Run it, confirm the error message is informative
5. **Write hints** — Three levels, each narrowing without revealing
6. **Write explanation** — After the scenario, explain WHY this bug happens and how to prevent it

### Anti-Patterns in Bug Design

- Don't create bugs that only exist to trick — every bug must teach something
- Don't use obscure language features as bugs — students should learn debugging, not edge cases
- Don't create multiple identical bug types in one scenario (e.g., five off-by-one errors)
- Don't make the fix require domain knowledge outside the lesson scope

## Memory Integration

- Read `curriculum-design.md` to align scenarios with module learning objectives
- Read `knowledge-base.md` for technical accuracy
- Read BOND.md for the owner's debugging experience level and preferences
- Read MEMORY.md for which debugging scenarios taught well and which fell flat
- Write scenarios to `{project-root}/_bmad/memory/crs/curated/content-drafts/`

## After the Session

Log which scenarios were created, their categories and difficulty levels. Note which bug types are most instructive for this course's audience. Track hint effectiveness — did hints guide without revealing? Update MEMORY.md with debugging scenario patterns that worked.