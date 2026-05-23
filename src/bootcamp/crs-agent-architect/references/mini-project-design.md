---
name: mini-project-design
code: MP
description: Design integrative mini-projects that combine all learned material into practical outcomes
---

# Mini-Project Design

## What Success Looks Like

A final project (or series of projects) that every learner can point to and say "I built this, and it uses everything I learned." The project isn't bolted on — it grows naturally from the prerequisite chain and validates every module's learning outcomes.

## Approach

### Backward Design

Start from the end. What should a learner be able to BUILD after completing the course?

1. **Define the outcome** — the final artifact, working demo, or portfolio piece
2. **Map to modules** — each module's learning outcome must contribute something the project needs
3. **Scope appropriately** — the project should be achievable in 1-2 focused sessions, not a multi-week marathon
4. **Define a rubric** — what "done" looks like, what "excellent" looks like, what common mistakes to watch for

### Project Scoping Rules

- If a learning outcome isn't exercised by the project, either the outcome or the project needs adjustment
- The project should require COMBINATION of skills, not just repetition of one
- Include stretch goals for advanced learners — same project, deeper implementation
- The project brief should be clear enough that a learner can start without hand-holding

### Integration Throughout vs Capstone Only

Two valid approaches, choose based on course style:

**Integrated (recommended for longer courses):**
- Each module has a small project exercise
- These build toward the final project incrementally
- Learners see progress at every step
- Final project = assembling + extending what they've already built

**Capstone (valid for shorter or focused courses):**
- One comprehensive project at the end
- All smaller exercises throughout the course feed skills into it
- Learners discover the project is achievable because they've been building all the pieces

## Project Template

When designing a mini-project, use this structure:

```markdown
## Mini-Project: [Project Name]

### Overview
**Goal:** [What the learner will build]
**Modules Covered:** [Which modules' outcomes this project validates]
**Estimated Time:** [How long to complete]

### Prerequisites
- [ ] Module [N] completed — [Concept name]
- [ ] Module [N] completed — [Concept name]

### Requirements (Must Have)
1. [Core requirement 1]
2. [Core requirement 2]
3. [Core requirement 3]

### Stretch Goals (Nice to Have)
1. [Advanced enhancement 1]
2. [Advanced enhancement 2]

### Success Criteria
| Level | Criteria |
|-------|----------|
| Complete | [Minimum viable project] |
| Solid | [Good implementation, clean code/content] |
| Excellent | [Advanced features, polished presentation] |

### Common Pitfalls
- [Pitfall 1] → [How to avoid it]
- [Pitfall 2] → [How to avoid it]
```

## Memory Integration

- Read `{project-root}/.ssconfig/memory/crs/{active-project}/curated/discovery-log.md` for course scope, audience, and desired outcomes
- Read `{project-root}/.ssconfig/memory/crs/{active-project}/curated/knowledge-base.md` for technical reference and existing examples
- Cross-reference with `PREREQUISITE_MAPPING` output — the project must validate concepts in the prerequisite chain
- Cross-reference with `DYNAMIC_TIMELINE` output — project time must be budgeted in the timeline
- Write finalized project design to `{project-root}/.ssconfig/memory/crs/{active-project}/curated/curriculum-design.md`

## After the Session

- Log project design decisions in session log
- Update MEMORY.md with what project structures work well for which course types
- Verify that every module's learning outcome is exercised by the project — if any are orphaned, flag to the Manager