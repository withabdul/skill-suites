---
name: multi-level-content
description: Write prose adapted to a specific audience level with appropriate depth and terminology
code: MC
---

# Multi-Level Content Writing

Produce course prose that matches the target audience's level — from beginner-friendly with analogies to advanced with precision.

## What Success Looks Like

Every piece of content is calibrated to the audience level defined in `discovery-log.md`. Beginner material has zero unexplained jargon. Advanced material is concise and technical. Intermediate material bridges both worlds. The reader never feels talked down to or overwhelmed.

## Your Approach

### The Level Spectrum

| Level | Depth | Jargon | Analogy | Example Style |
|-------|-------|--------|---------|---------------|
| **Beginner** | Deep, step-by-step | None without explanation | Required for every new concept | "Bayangkan kamu punya restoran..." |
| **Intermediate** | Moderate, assumption-aware | Introduced with brief context | For complex concepts only | "Seperti yang kamu tahu dari X, sekarang kita lanjut ke Y..." |
| **Advanced** | Concise, technical | Used freely with brief refresher | Rare, only for paradigm shifts | "Mirip pattern X, tapi dengan twist Y..." |

### The Non-Negotiable in Practice

For Beginner-level content:
- Every technical term gets defined on first use
- At least 1 real-world analogy per concept
- No assumption of prior knowledge outside the stated prerequisites
- Sentences are shorter, paragraphs are tighter

For Advanced-level content:
- Brief refresher references instead of full explanations ("seperti yang kita bahas di modul X")
- Depth over breadth — assume prerequisites are solid
- Performance and edge cases matter more than basics

### Writing Process

1. **Read the audience level** from `discovery-log.md` — don't guess
2. **Read the curriculum structure** from `curriculum-design.md` — know where this content fits
3. **Read the knowledge base** from `knowledge-base.md` — ensure technical accuracy
4. **Write at the right level** — adjust depth, jargon, and analogy density
5. **Review against the Non-Negotiable** — no unexplained jargon in Beginner material

## Memory Integration

- Read `discovery-log.md` for audience level and style preferences
- Read `curriculum-design.md` for module position and prerequisites
- Read `knowledge-base.md` for technical accuracy
- Read BOND.md for owner's tone and style preferences
- Write drafts to `{project-root}/.ssconfig/memory/crs/curated/content-drafts/`

## After the Session

Log which audience level was targeted, what analogies landed, and any style adjustments the owner requested. Update BOND.md if new style preferences emerged.