---
name: bias-validity-audit
description: Filter biased/promotional info and validate references for educational content
code: BV
---

# Bias & Validity Audit

Filter every reference and source through the credibility framework before it enters the knowledge base. No unchallenged marketing claims. No citations without credibility notes. This is the Non-Negotiable in action.

## What Success Looks Like

Every reference in `knowledge-base.md` has a credibility note explaining why it's useful and any bias concerns. No marketing claims presented as facts. No outdated version references without deprecation warnings. The course content built on this research stands up to scrutiny.

## Your Approach

### Three-Tier Credibility Framework

| Tier | Source Type | Credibility | Handling |
|------|------------|-------------|----------|
| **High** | Official docs, RFC/spec, maintainer statements, release notes | Authoritative, current | Cite directly. Note version and last-updated date. |
| **Medium** | Established tutorials, MDN, conference talks by core contributors, respected community members | Reliable with verification | Cite with version check. Note any sponsorship or affiliation. |
| **Low** | Personal blogs, Reddit, Stack Overflow, vendor marketing, affiliate content | Useful with caveats | Cite only with explicit credibility note. State what's useful and what's suspect. |

### Bias Red Flags

Watch for these and flag them immediately:

- **Affiliate links** — any source that earns from the technology it recommends
- **Vendor marketing** — "10x faster", "industry standard", "most popular" without data
- **Outdated stack** — tutorials from 2+ years ago for actively-developed tech
- **Sponsored content** — paid placement disguised as independent review
- **Echo chamber** — multiple sources repeating the same claim without independent verification
- **Survivorship bias** — "everyone uses X" when the data only shows who shouts loudest

### Audit Process

1. **Collect** all sources that will inform course content
2. **Classify** each source by credibility tier
3. **Cross-reference** — does any claim appear only in one tier? Verify it up
4. **Flag conflicts** — when sources contradict, document both sides with credibility notes
5. **Annotate** — add credibility notes to every `knowledge-base.md` entry

### The Non-Negotiable

Every link or information from non-official sources MUST include a credibility note explaining:
- Why this source is useful despite not being official
- Any bias concern or conflict of interest
- How recently the information was verified
- Whether the claim is independently corroborated

"I found this on a blog" is not enough. "Medium-tier: This 2024 tutorial by a known contributor explains the migration path clearly. Official docs for this feature are sparse. Verified against release notes for v3.2." is enough.

## Memory Integration

- Read `{project-root}/.ssconfig/memory/crs/{active-project}/curated/discovery-log.md` for what tech and audience the course targets
- Read MEMORY.md for credibility patterns from past audits
- Write audited findings to `{project-root}/.ssconfig/memory/crs/{active-project}/curated/knowledge-base.md` with credibility annotations
- Write raw session notes to `{project-root}/.ssconfig/memory/crs/{active-project}/daily/`

## After the Session

Log which sources surprised you — either by being more reliable or less than expected. Update MEMORY.md with credibility patterns: which blogs consistently deliver, which vendor docs are actually marketing in disguise. Flag any claims that couldn't be independently verified — these are risk items for the course.