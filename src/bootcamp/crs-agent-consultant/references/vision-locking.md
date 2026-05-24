---
name: vision-locking
description: Consolidate Discovery findings into locked vision parameters in discovery-log.md
code: VL
---

# Vision Locking

Summarize Discovery results into binding project parameters. When vision is sharp and feasible, lock everything in `discovery-log.md` so the execution phase can begin with a solid foundation.

For Bootcamp that chooses Daily Matter, these parameters also include the agreed DM template rules.

## What Success Looks Like

The `discovery-log.md` file contains a complete, specific, unambiguous vision that any specialist can work from. No loose ends. No vague intentions. The Manager can confidently transition to Design phase because Discovery is truly complete.

## Your Approach

**Locking is not summarizing — it's committing.** Every parameter in the locked vision should be specific enough that two different people reading it would build the same course. "A course about React" is not locked. "A 6-module online bootcamp for junior developers transitioning from class components to hooks, targeting 15 hours total study time, with 3 mini-projects" is locked.

### The Locking Process

1. **Review all Discovery outputs** — Read every question-answer exchange, every audit finding from `discovery-log.md` daily logs.
2. **Identify loose ends** — Flag anything still vague or undecided. Resolve these before locking.
3. **Draft the locked parameters** — Write each parameter as a specific, measurable commitment.
4. **Explicit confirmation** — Present the locked vision to the owner. Ask: "Is this correct and complete? If yes, this becomes the foundation for all subsequent phases — cannot be changed without a new discussion."
5. **Write to discovery-log.md** — Only after explicit user confirmation.

### Required Parameters for Lock

| Parameter | Example of Locked | Example of Unlocked (vague) |
|-----------|-------------------|------------------------------|
| Course title | "Full-Stack Next.js: From Zero to Deploy" | "Course about Next.js" |
| Target audience | "Junior React devs with 6+ months experience, Indonesian speakers" | "Developers" |
| Learning outcome | "Can build and deploy a full-stack Next.js app with auth and database" | "Understands Next.js" |
| Format | "Online, 6 modules, hybrid text/video, 3 mini-projects" | "Online course" |
| Duration | "15 hours total, 2.5 hours per module" | "A few weeks" |
| Difficulty | "Beginner-intermediate — assumes basic React knowledge" | "For everyone" |
| Style | "Text-heavy with code exercises (Dicoding style)" | "Interactive" |
| Course Type | "Bootcamp" or "Regular" | Not specified |
| Daily Matter | "Yes — 6 mandatory components + Icebreaker + Pre-class Reading" or "No" | Not decided |

### Daily Matter Locking (Bootcamp + DM = YES only)

If user chooses Bootcamp + Daily Matter, additional parameters that must be locked:

- **DM Template Rules** — Refer to `references/daily-matter-template.md`. Lock agreed mandatory components + user-selected optional components.
- **DM Delivery Channel** — How is DM distributed? (WhatsApp group, Discord, LMS, email?)
- **DM Frequency** — Every bootcamp day? Only specific days? (Default: every day)

Write the locked DM rules to `discovery-log.md` under a dedicated section.

### After Locking

Once locked, `discovery-log.md` becomes the source of truth for all subsequent phases. Changes to locked parameters require a new Discovery session — they're not adjusted casually.

This is what the Manager checks before authorizing Design phase to start.

## Memory Integration

- Read all Discovery exchanges from `daily/` logs
- Read BOND.md for owner's preferences on specificity level
- Write the locked vision parameters to `{crs_output_folder}/{active-project}/curated/discovery-log.md`
- Update `{project-root}/.ssconfig/memory/crs/{active-project}/index.md` with Discovery status = "LOCKED"

## After the Session

Log what was easy and hard to lock. Note which parameters the owner hesitated on. Write any postponed decisions to MEMORY.md for future sessions. Write the locked vision confirmation to `daily/`.
