---
name: style-adaptation
description: Adapt writing style to match the selected course platform style guide
code: SA
---

# Style Adaptation

Adapt all written content to match the tone, pacing, and structural conventions of the selected platform style. Style is not cosmetic — it determines how students experience the material. A Scrimba-style course that reads like a Pluralsight course will feel wrong and lose students.

## What Success Looks Like

Every piece of content produced in this session feels native to the selected platform style. A reader familiar with the platform would not notice a difference. Tone, sentence length, pacing, analogy density, and structural markers all align with the style guide.

## Your Approach

### Step 1: Load the Style

Read `{project-root}/.ssconfig/memory/crs/{active-project}/project-config.yaml` to get `style_file`.

Load `{skill-root}/../{style_file}` — read the full file, especially:
- **Platform Character** — the core identity and tone target
- **Treatment → Voice & Tone** — specific language rules
- **Treatment → Pacing** — length and rhythm guidelines
- **Naming Conventions** — how to title lessons, sections, exercises

Also load `{skill-root}/../assets/styles/academic-foundations.md` section 2 (Bloom's Taxonomy) to ensure content targets the right cognitive level.

### Step 2: Audit Existing Content

If content drafts already exist in `{project-root}/.ssconfig/memory/crs/{active-project}/curated/content-drafts/`, read them and identify style mismatches:

| Mismatch Type | Example |
|---------------|---------|
| **Tone drift** | Formal language in a Scrimba-style course |
| **Wrong pacing** | 800-word lesson in a Pluralsight clip |
| **Missing style markers** | No hooks in Udemy-style lectures |
| **Wrong naming** | "Introduction to X" in a Scrimba course (should be action-based) |
| **Analogy density** | No analogies in beginner Scrimba content |

### Step 3: Adapt or Write

**If adapting existing content:**
1. List all mismatches found
2. Rewrite each section to match the style guide
3. Preserve all technical accuracy — only change style, not substance

**If writing new content:**
1. Apply style guide from the first sentence
2. Use the Naming Conventions from the style file for all titles
3. Follow the Structure Template for lesson/section organization
4. Match the tone target exactly — read a sample from the style guide before writing

### Style Quick Reference

| Style | Tone | Sentence length | Analogy density |
|-------|------|----------------|-----------------|
| **Udemy** | Energetic, personal, opinionated | Short-medium | Medium |
| **Coursera** | Structured, precise, evidence-based | Medium-long | Low |
| **Pluralsight** | Dense, expert-to-expert, no filler | Short | Very low |
| **Frontend Masters** | Thoughtful, exploratory, honest | Variable | Low-medium |
| **Scrimba** | Warm, encouraging, celebratory | Short | High |
| **Academic** | Principled, evidence-backed | Medium | Medium |

### Step 4: Verify

After adapting, do a final pass:
- Read the content out loud (mentally) — does it sound like the platform?
- Check every title against the Naming Conventions
- Verify no section exceeds the platform's length guidelines
- Confirm tone is consistent throughout — no sudden formality shifts

## Memory Integration

- Read `project-config.yaml` for `style_file` and `platform`
- Read BOND.md for any style preferences the owner has expressed
- Write adapted content back to `{project-root}/.ssconfig/memory/crs/{active-project}/curated/content-drafts/`
- Note style decisions in session log — what was changed and why

## After the Session

Log which style mismatches were most common. If the owner consistently drifts toward a different style than selected, note it in BOND.md — they may want to reconsider their platform choice.
