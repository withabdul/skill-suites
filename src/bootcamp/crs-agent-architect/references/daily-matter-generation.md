---
name: daily-matter-generation
description: Generate per-day Daily Matter structure based on locked DM template and curriculum design
code: DMG
---

# Daily Matter Generation

Based on DM template rules locked by Consultant in `discovery-log.md` and curriculum already structured, generate per-day Daily Matter structure. Output saved in `curated/content-drafts/daily-matter/`.

## What Success Looks Like

Every bootcamp day has a ready-to-use Daily Matter file. File contains 6 mandatory components (or more if user chose optional components), meets quality checklist, and is aligned with that day's material.

## Prerequisites

Before loading this capability, ensure:
- `discovery-log.md` is already LOCKED (parameter `Course Type = Bootcamp` and `Daily Matter = Yes`)
- `curriculum-design.md` already contains timeline and per-day material
- `knowledge-base.md` has usable research bites

## Your Approach

### Generation Flow

1. **Load DM template rules** — Read `discovery-log.md` Daily Matter section. Note: mandatory components, selected optional components, delivery channel, frequency.
2. **Load curriculum** — Read `curriculum-design.md` for day-to-material mapping.
3. **Per-day generation** — For each bootcamp day, generate 1 Daily Matter file.
4. **Quality check** — Every file must pass quality checklist (from `daily-matter-template.md`).

### DM File Structure

Each DM file is saved in `curated/content-drafts/daily-matter/day-NN.md`:

```markdown
# Daily Matter — Day [NN]: [Topic]

## Daily Goal
[1 sentence — what is achieved today]

## Recall Trigger
[1–2 retrieval questions about yesterday's material]

## Today's Map
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

## Research Bite
[2–4 sentence insight from research. Must include source.]

## Mini Exercise
[Link or embed from separate mini exercise file]

## Reflection Prompt
[1 metacognitive question for end of day]

## [Optional: Icebreaker]
[Only if user chose — fun fact or light question]

## [Optional: Pre-class Reading]
[Only if user chose — link to short article/video]

## [Optional: Instructor's Note]
[Only if user chose — personal message from instructor]
```

### Research Bite — Quality Requirements

Research Bite MUST meet standards:
- **Valid source**: Scientific journals (IEEE, ACM, Springer, Elsevier), official tech blogs (React docs, Next.js blog, Vercel blog), or verifiable research
- **Relevant to today's topic**: Not random trivia
- **Not promotional**: No affiliate links, no sponsored content
- **Concise**: 2–4 sentences, straight to insight

**How to find Research Bite:**
1. Check `knowledge-base.md` — Researcher may already have data
2. If not available, do independent research: find 1–2 valid sources
3. Write insight in format: finding + practical implication
4. Include source (journal name/year or URL)

**Example of a good Research Bite:**
> "Study from IEEE (2023) found that 68% of production bugs come from outdated dependencies. That's why current best practice: always pin dependency versions, don't use `^` or `~` in `package.json`."
> — Source: IEEE Software Engineering Conference, 2023

**Example of a bad Research Bite (PROHIBITED):**
> "Many developers like using React because React is cool and popular."
> — No source, no specific insight, subjective opinion

### Mini Exercise — Linked, Not Embedded

Mini exercise is written in a separate file: `curated/content-drafts/daily-matter/day-NN-exercise.md`.
Daily Matter just references (links) to that exercise file.

Mini exercise file structure:
```markdown
# Exercise — Day [NN]: [Title]

**Time:** [5–15 minutes]
**Objective:** [1 sentence]

## Instructions
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Starter Code
[Starter code — optional]

## Expected Output
[Expected result — optional]

## Hint
[Hint if stuck — optional]
```

### Quality Checklist (Per File)

- [ ] All mandatory components present
- [ ] Research Bite has valid source (not random blog)
- [ ] Recall Trigger tests memory of yesterday's material (not trivia)
- [ ] Total DM words <300 (not including exercise file)
- [ ] No Aha! moment spoilers
- [ ] Mini exercise can be completed <15 minutes
- [ ] No jargon without explanation
- [ ] Reflection Prompt is metacognitive (not "understood?")
- [ ] DM aligned with that day's material in curriculum

## Memory Integration

- Read `discovery-log.md` (DM rules, delivery channel, frequency)
- Read `curriculum-design.md` (timeline, per-day material)
- Read `knowledge-base.md` (research bite candidates)
- Write to `curated/content-drafts/daily-matter/` (DM files)
- Update `daily/YYYY-MM-DD.md` with generation log

## After the Session

Log number of DMs generated. Note research bites successfully found vs not yet found (todo for Researcher). Update `index.md` if DM generation complete.
