---
name: dynamic-timeline
code: DT
description: Allocate time per topic based on difficulty, adjust timelines for format and complexity
---

# Dynamic Timeline Planning

## What Success Looks Like

An achievable timeline that accounts for difficulty curves — abstract concepts get more time, hands-on practice needs longer sessions not more sessions, and buffer is built in for unknown unknowns. The learner never hits a wall because time was underestimated.

## Approach

### Difficulty-Based Allocation

Not all topics are equal. Time allocation must reflect cognitive load:

1. **Abstract concepts** (theoretical foundations, mental models) — allocate 1.5x base time. Learners need repetition and analogy, not speed.
2. **Procedural skills** (step-by-step processes, tool usage) — allocate 1x base time. Demonstration + practice = competence.
3. **Integration topics** (combining multiple skills, project work) — allocate 2x base time. This is where learners struggle most.
4. **Review and reinforcement** — allocate 0.5x base time. Not filler — essential for retention.

### Session Length vs Session Count

- Shorter, more frequent sessions beat longer, fewer sessions for most content
- Online format: 45-90 minute sessions (attention drops after this)
- Offline format: 90-180 minute sessions (in-person momentum sustains focus longer)
- Hands-on practice needs session length, not more sessions — cramming practice into 30-minute blocks doesn't work

### Buffer for Unknown Unknowns

Every timeline MUST include buffer:
- 10% buffer for courses you've designed before (familiar domain)
- 20% buffer for new domains or first-time course designs
- 30% buffer for topics that are notoriously hard to teach (abstract math, systems thinking, debugging)

Buffer is not padding. Buffer is realism. Without it, timelines become wishful thinking.

### Hybrid Format Adjustments

See `references/hybrid-logistics.md` for detailed format-specific adjustments. In summary:
- Online sessions are shorter → more sessions needed for the same content
- Offline sessions can go deeper → fewer sessions but more preparation
- Hybrid needs explicit mode-switching documented in the timeline

## Timeline Template

When presenting a timeline, use this structure:

```markdown
## [Course Name] — Timeline

### Module [N]: [Module Title]
**Difficulty:** [Abstract / Procedural / Integration]
**Format:** [Online / Offline / Hybrid]
**Total Time:** [X hours Y minutes]
**Sessions:** [N sessions × duration each]

| Topic | Time | Format Notes |
|-------|------|-------------|
| [Topic 1] | [X min] | [Delivery notes] |
| [Topic 2] | [X min] | [Delivery notes] |

**Buffer:** [X%] — [Reason for buffer level]
**Prerequisites:** [What learners must know before this module]
```

## Memory Integration

- Read `{project-root}/_bmad/memory/crs/curated/discovery-log.md` for course scope, audience level, and format decisions
- Read `{project-root}/_bmad/memory/crs/curated/knowledge-base.md` for technical complexity ratings
- Cross-reference with `PREREQUISITE_MAPPING` output to ensure timeline order matches prerequisite sequence
- Write finalized timeline to `{project-root}/_bmad/memory/crs/curated/curriculum-design.md`

## After the Session

- Log timeline decisions and their reasoning in session log
- Update MEMORY.md with timeline estimation patterns — were allocations realistic?
- If timeline requires session break changes or duration adjustments beyond 15%, **consult the Manager** before finalizing