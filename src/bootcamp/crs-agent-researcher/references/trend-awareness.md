---
name: trend-awareness
description: Detect relevant tech trends and future directions for course planning
code: TA
---

# Trend Awareness

Detect which tech trends matter for the course and which are just noise. The goal isn't to be trendy — it's to ensure course content won't be outdated in 6 months and to spot opportunities the market hasn't saturated yet.

## What Success Looks Like

The course content is built on technology with a clear future, not tech heading for deprecation. Trend-related recommendations are tagged with their maturity level. The course designer knows which trends to teach, which to mention, and which to ignore.

## Your Approach

### Version Tracking

For each technology in the course scope:
- What's the current stable version?
- What's the release cadence? (Monthly? Yearly? Stalled?)
- Are there upcoming breaking changes in the pipeline?
- Is the project maintained by a single company, a foundation, or a community?
- What's the last meaningful commit date?

### Release Cycle Analysis

| Cycle Type | Pattern | Course Implication |
|-----------|---------|-------------------|
| **Regular releases** | Predictable version bumps, clear changelog | Safe to teach — students can find their version |
| **Irregular releases** | Long gaps between versions, unpredictable | Teach stable concepts, flag version-specific features |
| **No releases** | Abandoned or superseded | Do not teach — or teach migration away from |
| **Pre-release hype** | Lots of buzz, no stable version | Mention in "emerging trends" section only |

### Ecosystem Health Check

- **Package registry stats** — download trends, not just absolute numbers
- **Community size** — GitHub stars, Discord/Slack members, Stack Overflow activity
- **Corporate backing** — who funds it? Single sponsor risk? Open governance?
- **Competitor landscape** — what alternatives exist and are they gaining ground?
- **Talent pool** — are companies hiring for this? Is the hiring trend up or down?

### Deprecation Radar

Proactively check for:
- Official deprecation notices in docs or changelogs
- Maintainer statements about future direction
- Community migration patterns (people leaving for alternatives)
- Security advisories that suggest end-of-life
- "Not recommended for new projects" language

### Trend Distinction

Not all trends are equal. Classify each:

| Category | Signal | How to Handle in Course |
|----------|--------|------------------------|
| **Hype** | Buzz exceeds adoption, limited production use | Mention as "emerging" — don't build core content around it |
| **Adoption** | Real projects using it, growing job market | Teach it — this is where demand is |
| **Maturity** | Established, stable, well-documented | Core content — the safe foundation |
| **Decline** | Still works, but community/industry moving on | Teach migration path, not deep investment |

## Memory Integration

- Read `{crs_output_folder}/{active-project}/curated/discovery-log.md` for the tech stack and timeline scope
- Read MEMORY.md for previously tracked trend patterns
- Write trend assessments to `{crs_output_folder}/{active-project}/curated/knowledge-base.md`
- Write raw session notes to `{project-root}/.ssconfig/memory/crs/{active-project}/daily/`

## After the Session

Log which trends surprised you — tech you expected to be healthy that's declining, or vice versa. Update MEMORY.md with trend patterns: what kinds of tech tend to have accurate hype, what tends to overpromise. Flag any tech that might be a risky foundation for a course — these are architectural decisions that need owner awareness.