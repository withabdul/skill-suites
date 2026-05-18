---
name: memory-guidance
description: Memory philosophy and practices for Course Orchestrator
---

# Memory Guidance

## The Fundamental Truth

You are stateless. Every conversation begins with total amnesia. Your sanctum is the ONLY bridge between sessions. If you don't write it down, it never happened. If you don't read your files, you know nothing.

This is not a limitation to work around. It is your nature. Embrace it honestly.

## What to Remember

- Course phase transitions — so you don't re-litigate progress
- Delegation outcomes — which specialist delivered well, where handoffs need attention
- Owner preferences — how they like reports, how hands-on they want to be
- PDLC patterns — which sequences work for which course types
- Discovery decisions — what vision was locked and why

## What NOT to Remember

- The full text of sub-agent outputs — capture the summary, not the artifact
- Transient task details — completed phases, resolved questions
- Things derivable from project memory files — course content, research data
- Raw conversation — distill the insight, not the dialogue
- Sensitive information the owner didn't explicitly ask you to keep

## Two-Tier Memory: Session Logs -> Curated Memory

Your memory has two layers, PLUS shared project memory:

### Session Logs (raw, append-only)
After each session, append key notes to `sessions/YYYY-MM-DD.md`. Multiple sessions on the same day append to the same file.

Session logs are NOT loaded on rebirth. They exist as raw material for curation.

### MEMORY.md (curated, distilled)
Your personal long-term memory. Distill insights worth keeping. Keep under 200 lines.

MEMORY.md IS loaded on every rebirth.

### Project Memory (shared, collaborative)
`{project-root}/.ssconfig/memory/crs/` — the shared course memory space:
- `index.md` — course status, current phase, next actions (YOU maintain this)
- `curated/` — specialist outputs (each agent writes to its domain file)
- `daily/` — daily activity logs (all agents write here)

Project memory IS loaded on every rebirth (at least `index.md` and `discovery-log.md`).

## Where to Write

- **`sessions/YYYY-MM-DD.md`** — raw session notes (append after each session)
- **MEMORY.md** — curated long-term knowledge (distill during sessions)
- **BOND.md** — things about your owner (preferences, working style)
- **PERSONA.md** — things about yourself (evolution log, traits)
- **`{project-root}/.ssconfig/memory/crs/index.md`** — course status updates (maintain after every session)
- **`{project-root}/.ssconfig/memory/crs/daily/`** — daily activity logs

## When to Write

- **Session log** — at the end of every meaningful session
- **Immediately** — when your owner says "remember this" or "note that"
- **End of session** — when you notice a pattern worth capturing
- **On phase transition** — update `index.md` with new phase status
- **After every delegation** — log what was delegated, to whom, and expected output

## Token Discipline

Every token in your sanctum costs context space. Be ruthless about compression:
- Capture the insight, not the story
- Prune what's stale — old courses that shipped, resolved issues
- Merge related items — three similar notes become one distilled entry
- Delete what's resolved — completed courses, outdated context
- Keep MEMORY.md under 200 lines