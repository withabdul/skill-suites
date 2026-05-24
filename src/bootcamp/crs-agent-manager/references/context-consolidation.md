---
name: context-consolidation
description: Merge sub-agent outputs into unified progress reports and track course status across all phases
code: CC
---

# Context Consolidation

Merge outputs from multiple sub-agents into a single coherent progress picture. The user sees one face — yours. They should never have to piece together what happened across different specialists.

## What Success Looks Like

The user receives a clear, unified report that shows exactly where the course stands: what's done, what's in progress, what's blocked, and what's next. No conflicting outputs. No orphaned work. Everything traces back to the locked vision in `discovery-log.md`.

## Your Approach

**Consolidate, don't just concatenate.** Read all relevant curated files in `{crs_output_folder}/{active-project}/curated/` and find the story. How does the research feed into the curriculum? How does the engagement design align with the delivery guide? Where are the gaps?

**Surface misalignment early.** If Theory-Writer's tone doesn't match the audience the Consultant defined, flag it. If Code-Smith's exercises don't align with the Architect's timeline, note it. This is your quality gate between phases.

**Report formats adapt to the moment.** A quick status check gets a one-paragraph summary. A phase transition gets a full cross-reference report. A conflict gets a structured brief. Match the format to the need.

## Progress Report Structure

When generating a full progress report:

1. **Current Phase** — where we are in PDLC
2. **Vision Check** — does everything still align with `discovery-log.md`?
3. **What's Done** — completed deliverables per specialist
4. **What's In Progress** — active work and expected completion
5. **Gaps & Risks** — misalignments, missing pieces, timeline concerns
6. **Next Actions** — what happens next and who leads it

## Memory Integration

- Read all curated files in `{crs_output_folder}/{active-project}/curated/` for full context
- Read `{project-root}/.ssconfig/memory/crs/{active-project}/index.md` for current status
- Check BOND.md for owner's quality and format preferences
- Write consolidated reports to `{project-root}/.ssconfig/memory/crs/{active-project}/daily/`

## After the Session

Note what each specialist produced, any alignment issues found, and the owner's reactions to the consolidated report. Update MEMORY.md if the owner shows new preferences about report format or detail level.