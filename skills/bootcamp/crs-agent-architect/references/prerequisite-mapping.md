---
name: prerequisite-mapping
code: PM
description: Structure learning sequences with no prerequisite gaps, ensuring every concept builds on prior knowledge
---

# Prerequisite Mapping

## What Success Looks Like

A learning path where every concept builds on prior knowledge — no leaps, no assumptions of untaught material, no "you should already know this" moments. A learner following the sequence never encounters a concept they can't understand because a prerequisite was skipped.

## Approach

### Dependency Mapping

1. **List all concepts** in the course scope (from `discovery-log.md` and `knowledge-base.md`)
2. **For each concept, identify prerequisites** — what must a learner understand BEFORE this concept makes sense?
3. **Build a dependency graph** — concepts that depend on the same foundation cluster together
4. **Identify prerequisite chains** — linear sequences where A → B → C (must learn in order)
5. **Identify prerequisite clusters** — concepts that can be learned in parallel after a shared foundation

### The "No Leaps" Rule

**Every concept in the curriculum must be reachable through prerequisites that are ALSO in the curriculum.**

If Module 3 requires understanding of X, then either:
- X is taught in Module 1 or 2, OR
- X is explicitly listed as a pre-course assumption (stated in discovery-log.md), OR
- X needs to be added to an earlier module

There are NO exceptions. "They probably know this" is not a valid prerequisite.

### Concept Trees

Present prerequisite relationships as a structured tree:

```
Foundation (Module 1)
├── Concept A → feeds into Module 2 and Module 3
├── Concept B → feeds into Module 3 only
└── Concept C → standalone, Module 2

Intermediate (Module 2)
├── Concept D (requires A) → feeds into Module 4
└── Concept E (requires A + C) → feeds into Module 4

Advanced (Module 3)
├── Concept F (requires A + B) → feeds into Module 5
└── ...
```

### Prerequisite Checkpoints

At the START of each module, include a prerequisite checkpoint:
- What learners should already know
- A quick self-assessment or recap that confirms readiness
- If a learner can't pass the checkpoint, point them to the correct earlier module

## Mapping Format

When presenting a prerequisite map, use this structure:

```markdown
## [Course Name] — Prerequisite Map

### Module [N]: [Module Title]
**Prerequisites:** [What modules/concepts must be completed first]
**Enables:** [What later concepts/modules this unlocks]
**Checkpoint:** [Quick assessment to confirm readiness]

| Concept | Requires | Enables | Module |
|---------|----------|---------|--------|
| [Concept] | [Prereqs] | [Downstream] | [M#] |
```

## Non-Negotiable Reminder

⚠️ You CANNOT make autonomous decisions about session breaks or drastic duration changes. If prerequisite mapping reveals that a module needs significantly more/fewer sessions than expected, **ask the Manager** before adjusting.

## Memory Integration

- Read `{project-root}/_bmad/memory/crs/curated/discovery-log.md` for course scope and audience baseline knowledge
- Read `{project-root}/_bmad/memory/crs/curated/knowledge-base.md` for technical dependencies and concept relationships
- Cross-reference with `DYNAMIC_TIMELINE` output to ensure prerequisite order matches time allocation
- Write finalized prerequisite map to `{project-root}/_bmad/memory/crs/curated/curriculum-design.md`

## After the Session

- Log prerequisite decisions and flagged gaps in session log
- Update MEMORY.md with prerequisite patterns — which concept sequences consistently need more scaffolding
- If you find prerequisite gaps that require adding new modules or reshuffling the curriculum significantly, flag these to the Manager for coordination