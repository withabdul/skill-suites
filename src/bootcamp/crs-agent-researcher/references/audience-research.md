---
name: audience-research
description: Map pain points, skill levels, and community needs of target audience
code: AR
---

# Audience Research

Map who the course is really for — not who you assume it's for, but who actually needs it and where they struggle. Real pain points from real communities, not imagined demand.

## What Success Looks Like

A clear audience persona with validated pain points drawn from actual community signals, not assumptions. The course designer knows exactly who they're building for, what those people struggle with, and where they go for help. No "I think the audience wants X" — only "the audience said X in these threads/posts/job listings."

## Your Approach

### Forum Mining

Search community hubs where your target audience asks questions:
- **Stack Overflow** — what questions come up repeatedly? What's genuinely confusing?
- **Reddit/Discord** — what do practitioners complain about? What resources do they share?
- **GitHub Issues** — what errors do users hit? What features are requested?
- **Dev.to / Hashnode** — what tutorials resonate? What gaps do comments reveal?

Look for patterns, not individual posts. Three separate people asking the same thing = a signal. One person = a data point.

### Job Posting Analysis

Search job listings for the tech/skill the course covers:
- What skills are employers actually asking for?
- What's the gap between beginner listings and senior listings?
- What tools/frameworks appear together?
- What soft skills or domain knowledge are paired with the technical skills?

Job postings reveal market demand, not just community interest.

### Community Sentiment

Assess the emotional landscape:
- What frustrates people about learning this topic?
- What excites them?
- What tools do they wish existed?
- Where do they feel abandoned by existing resources?
- What's the "I wish someone had told me" pattern?

### Skill Gap Identification

Map where learners actually get stuck:
- What prerequisites are assumed but not taught?
- Where's the cliff between "I followed the tutorial" and "I can build something real"?
- What concepts require multiple attempts to click?
- What's the progression from beginner → intermediate → advanced?

### Audience Persona Structure

Document your findings in `knowledge-base.md` using this structure:

```markdown
## Audience: [Name]

**Who:** [1-sentence description]
**Skill Level:** [Beginner / Intermediate / Advanced]
**Current Stack:** [What they're using now]
**Pain Points:**
- [Validated pain point 1 — source: ...]
- [Validated pain point 2 — source: ...]
**Learning Gaps:**
- [Gap between tutorial knowledge and real-world application]
**Where They Hang Out:** [forums, communities, platforms]
**What They Wish Existed:** [from community signals]
```

## Memory Integration

- Read `{crs_output_folder}/{active-project}/curated/discovery-log.md` for the target audience definition
- Read MEMORY.md for audience patterns from past research
- Write audience findings to `{crs_output_folder}/{active-project}/curated/knowledge-base.md`
- Write raw session notes to `{project-root}/.ssconfig/memory/crs/{active-project}/daily/`

## After the Session

Log which communities had the richest signal and which were noise. Update MEMORY.md with audience patterns: what pain points keep appearing across different courses, what learning gaps are universal. Note if the target audience in `discovery-log.md` matches or conflicts with your findings — flag mismatches immediately.