---
name: tech-stack-scoping
description: Identify official docs, tech stability status, and documentation landscape
code: TS
---

# Tech Stack Scoping

Map the technical landscape for course content — identify what's official, what's stable, what's deprecated, and where the documentation gaps live. Every piece of tech gets a credibility assessment before it enters the knowledge base.

## What Success Looks Like

A complete tech stack map with stability status for each component. Official documentation sources identified and prioritized. Documentation gaps flagged. The Architect and Theory-Writer can build course content knowing exactly which sources to trust and where the pitfalls are.

## Your Approach

### Prioritize Official Documentation

Always start with official docs. If a technology's official documentation is incomplete or outdated, that's a finding worth reporting — not a reason to skip it.

1. **Identify the tech stack** from `discovery-log.md` — what technologies will the course cover?
2. **Locate official sources** — docs sites, GitHub repos, RFCs, official blog posts
3. **Assess stability** — is this tech in active development? Maintenance mode? Deprecated?
4. **Map documentation quality** — are the official docs thorough? Current? Translated?
5. **Find community supplements** — where do practitioners go when official docs fall short?

### Classify Tech Status

| Status | Meaning | Credibility Implication |
|--------|---------|------------------------|
| **Stable** | Production-ready, actively maintained, clear roadmap | Official docs are primary source |
| **Beta** | Functional but changing, API may shift | Official docs + recent community input needed |
| **Deprecated** | Replaced or sunsetting, migration path exists | Flag for course design — is teaching this responsible? |
| **Bleeding Edge** | Very new, limited production use | Community experimentation > official docs |

### Note Documentation Gaps

When official docs are insufficient:
- What topics are underdocumented?
- Where do practitioners find answers instead? (Stack Overflow, Discord, GitHub Issues)
- Is there a community-maintained resource that fills the gap?
- How recently was the gap identified?

## Credibility Framework

| Tier | Source Type | Credibility | When to Use |
|------|------------|-------------|-------------|
| **High** | Official documentation, RFC/spec, maintainers' blog | Direct, current, authoritative | Primary source for all factual claims |
| **Medium** | Established tutorials (MDN, established blogs), conference talks by core contributors | Reliable but verify version currency | Supplementary explanations, practical examples |
| **Low** | Personal blog posts, Reddit, Stack Overflow answers | Useful but requires verification | Starting points for investigation, never as final citations |

Every entry in `knowledge-base.md` must include a credibility tier annotation.

## Memory Integration

- Read `{project-root}/_bmad/memory/crs/curated/discovery-log.md` for the course scope and tech stack to research
- Read MEMORY.md for previously validated source patterns
- Write findings to `{project-root}/_bmad/memory/crs/curated/knowledge-base.md` — this is YOUR primary output
- Write raw session notes to `{project-root}/_bmad/memory/crs/daily/`

## After the Session

Log what was easy to find and what required deep digging. Note which official docs impressed you and which disappointed you. Update MEMORY.md with source patterns — which vendors maintain great docs, which leave you guessing. Flag any tech that might not be around in 12 months — that's architectural risk for the course.