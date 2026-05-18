---
name: hybrid-logistics
code: HL
description: Adapt curriculum timing, pacing, and structure for Online, Offline, and Hybrid delivery formats
---

# Hybrid Logistics Adjustment

## What Success Looks Like

A curriculum that works equally well online and offline, with documented adjustments for each format. No learner gets a worse experience because of the delivery mode — the content and outcomes are identical, but the pacing, exercises, and interaction style adapt to what each format does best.

## Approach

### Format-Specific Adjustments

**Online format:**
- Sessions: 45-90 minutes max (attention drops sharply after 90 min on screen)
- More async work between sessions — reading, exercises, reflection
- Break complex topics into shorter sessions with practice between
- Use screen-share and live-coding as primary demonstration mode
- Reduce group work — pair programming or 2-3 person breakout rooms max
- Check for understanding more frequently (polls, quick quizzes, chat prompts)

**Offline format:**
- Sessions: 90-180 minutes (in-person momentum sustains longer focus)
- More group work possible — discussions, group projects, peer review
- Hands-on practice during session time (not just homework)
- Whiteboard explanation + live demo + guided practice in one session
- Less frequent check-ins needed — body language provides feedback
- Longer deep-dive blocks — leverage the luxury of co-located focus time

**Hybrid format:**
- Explicit mode-switching documented in the timeline ("Session 1: Online — concept intro", "Session 2: Offline — hands-on lab")
- Every concept has BOTH an online and offline delivery path
- Async bridging material between sessions (both groups need to stay in sync)
- Online sessions handle concept introduction, discussion, and reflection
- Offline sessions handle hands-on practice, group work, and integration
- Never assume a concept was "covered in the other format" — each session must be self-contained enough to stand on its own

### Adjustment Matrix

| Factor | Online | Offline | Hybrid |
|--------|--------|---------|--------|
| Session length | 45-90 min | 90-180 min | Varies by mode |
| Breaks | Every 20-30 min | Every 45-60 min | Per session type |
| Group work | Pairs/small breakouts | Full group possible | Offline-heavy |
| Practice | Mostly async between | During session | Split both |
| Demo style | Screen share/live code | Whiteboard + live | Format-specific |
| Check understanding | Polls, chat, quizzes | Body language, Q&A | Both methods |
| Async load | High | Low- medium | Medium |
| Deep practice | Between sessions | During sessions | Offline sessions |

### Mode-Switching Template

When documenting a hybrid curriculum, tag each session clearly:

```markdown
### Session [N]: [Topic] — [ONLINE / OFFLINE / HYBRID-ONLINE / HYBRID-OFFLINE]
**Duration:** [X min]
**Mode:** [Online / Offline]
**Focus:** [Concept intro / Hands-on practice / Integration / Assessment]
**Async work:** [What learners do between this and next session]
**Sync point:** [What both formats must have covered before next session]
```

## Non-Negotiable

⚠️ Wajib konsultasi Manager untuk perubahan durasi drastis. If format adjustments require more than 20% change to total course duration, or if sessions need to be restructured beyond the standard adjustments above, **ask the Manager first**.

## Memory Integration

- Read `{project-root}/.ssconfig/memory/crs/curated/discovery-log.md` for format decisions (online/offline/hybrid) and audience context
- Read `{project-root}/.ssconfig/memory/crs/curated/knowledge-base.md` for content that needs format-specific adaptation
- Cross-reference with `DYNAMIC_TIMELINE` and `PREREQUISITE_MAPPING` outputs — format adjustments must not break the prerequisite chain
- Write format-adjusted curriculum to `{project-root}/.ssconfig/memory/crs/curated/curriculum-design.md`

## After the Session

- Log format adjustment decisions in session log
- Update MEMORY.md with which format adaptations worked well — track this over time
- If format conflicts arise (content that simply doesn't work in one format), flag to the Manager for triage