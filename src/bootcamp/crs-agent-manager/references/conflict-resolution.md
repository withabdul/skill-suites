---
name: conflict-resolution
description: Resolve misalignment between sub-agent outputs and the original course vision
code: CR
---

# Conflict Resolution

When sub-agent outputs diverge from the locked vision or from each other, realign them. The user should never see inconsistent deliverables — conflicts get resolved before they reach the user.

## What Success Looks Like

Every deliverable traces cleanly back to the vision in `discovery-log.md`. When conflicts exist, the user receives a clear explanation of the tension and a recommended resolution — not a messy patchwork of contradictory outputs.

## Your Approach

**Vision is the north star.** The locked vision in `discovery-log.md` is the arbiter. If an output contradicts it, the vision wins. If the vision itself needs updating, that requires a new Discovery session with the Consultant — not a unilateral decision by any agent.

**Common conflict patterns:**

| Conflict Type | Example | Resolution Approach |
|---------------|---------|---------------------|
| **Vision drift** | Theory-Writer's tone doesn't match the target audience Consultant defined | Flag the drift, redirect to vision |
| **Timeline mismatch** | Code-Smith's exercises need more time than Architect allocated | Renegotiate timeline with Architect |
| **Scope creep** | Researcher discovered exciting tangents beyond original scope | Acknowledge, park for v2, stay focused |
| **Engagement vs Substance** | Engagement's Aha! moment disrupts Architect's flow | Find the integration point, don't sacrifice either |

**Escalate, don't decide unilaterally.** When you can't resolve a tension by referencing the vision, present the tradeoff to the user clearly: "Ada tension antara X dan Y — kamu lebih prioritasin yang mana?"

## Resolution Process

1. **Detect** — Read curated outputs and cross-reference with `discovery-log.md`
2. **Classify** — Is this a clear vision violation or a genuine tradeoff?
3. **Resolve** — Vision violations get corrected. Tradeoffs get presented to the user.
4. **Document** — Write the resolution to `{project-root}/.ssconfig/memory/crs/daily/` and update relevant curated files if needed.
5. **Notify** — Inform the user of what was resolved and why.

## Memory Integration

- Read `{project-root}/.ssconfig/memory/crs/curated/discovery-log.md` as the source of truth
- Read all curated files to detect cross-specialist conflicts
- Read BOND.md for owner's preferences about tradeoffs (speed vs quality, depth vs breadth)
- Write resolution decisions to `{project-root}/.ssconfig/memory/crs/daily/`

## After the Session

Log what conflicts were found, how they were resolved, and whether the owner needed to intervene. Track conflict patterns over time — if the same type of conflict recurs, it may indicate a structural issue in the PDLC flow.