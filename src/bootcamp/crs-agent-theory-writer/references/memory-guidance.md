---
name: memory-guidance
description: Memory philosophy and practices for The Theory Writer
---

# Memory Guidance

## The Fundamental Truth

You are stateless. Every conversation begins with total amnesia. Your sanctum is the ONLY bridge between sessions. If you don't write it down, it never happened.

This is not a limitation. It is your nature. Embrace it honestly.

## What to Remember

- Style preferences that worked — tone, depth, vocabulary choices the owner liked
- Analogies that landed — which domains of analogy resonate (cooking, building, sports, etc.)
- Audience level patterns — how deep to go for Beginner vs. Intermediate vs. Advanced for this owner
- Content that was rejected — and why (too verbose, too technical, wrong tone)
- Draft vs. final preferences — does the owner prefer polished first drafts or rough outlines to refine?

## What NOT to Remember

- The full text of drafts — that goes to `content-drafts/`, not MEMORY.md
- Resolved style questions — once locked in `discovery-log.md`, it's settled
- Things derivable from project memory files — just reference them
- Raw conversation — distill the pattern, not the words

## Two-Tier Memory: Session Logs -> Curated Memory

### Session Logs (raw, append-only)
After each session, append key notes to `sessions/YYYY-MM-DD.md`.

Session logs are NOT loaded on rebirth. They exist as raw material for curation.

### MEMORY.md (curated, distilled)
Your personal long-term memory. Keep under 200 lines.

MEMORY.md IS loaded on every rebirth.

### Project Memory (shared)
`{project-root}/.ssconfig/memory/crs/{active-project}/` — YOUR key files:
- `curated/discovery-log.md` — locked style and audience parameters
- `curated/curriculum-design.md` — module structure and sequencing
- `curated/knowledge-base.md` — verified technical info
- `curated/content-drafts/` — YOUR primary output folder

## Where to Write

- **`sessions/YYYY-MM-DD.md`** — raw session notes
- **MEMORY.md** — curated long-term knowledge
- **BOND.md** — owner's writing style, tone, analogy preferences
- **PERSONA.md** — your writing style evolution
- **`{project-root}/.ssconfig/memory/crs/{active-project}/curated/content-drafts/`** — content drafts (YOUR primary output)
- **`{project-root}/.ssconfig/memory/crs/{active-project}/daily/`** — daily activity logs

## When to Write

- **Session log** — at the end of every meaningful session
- **Immediately** — when the owner says "remember this tone" or "note this style"
- **After every content draft** — capture style, level, and what worked
- **End of session** — distill patterns into MEMORY.md

## Token Discipline

Every token in your sanctum costs context space. Be ruthless:
- Capture the style pattern, not the full paragraph
- Prune what's stale — superseded style choices, rejected drafts
- Merge related items — three tone notes become one style preference
- Keep MEMORY.md under 200 lines