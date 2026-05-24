---
name: daily-matter-template
description: Define the Daily Matter template rules during Discovery — what to include, what to avoid, and quality standards
code: DM
---

# Daily Matter Template

When user chooses Bootcamp + Daily Matter = YES, Consultant is responsible for defining Daily Matter template rules. This template becomes a contract that Architect will later use to generate per-day structure.

## What Success Looks Like

Daily Matter template locked in `discovery-log.md` contains rules specific enough that Architect can directly generate per-day DM structure without re-asking. Template defines what MUST be present, what is PROHIBITED, and quality standards that must be met.

## Research Foundation

This template is designed based on research findings:

- **Retrieval Practice**: End-of-day review + recall exercise strengthens long-term memory (PMC, 2018; Frontiers in Psychology, 2025)
- **Daily Reflection**: 85% of students reported positive impact from daily reflection on learning (Perspectives on Medical Education, 2016)
- **Student Check-ins**: Regular check-ins improve metacognition, confidence, and student engagement (University of Iowa Center for Teaching, 2022)
- **Spaced Repetition**: Combination of retrieval + distributed practice is more effective than passive review (Frontiers, 2025)

## Your Approach

### The Template Discovery Flow

1. **Explain Daily Matter concept** — "Daily Matter is the daily opening material for bootcamp students. Not the main material, but warm-up + direction before the session starts. It works like a 'morning briefing' — gets students mentally ready, recalls yesterday's material, and lets them know what will be learned today."

2. **Walk through template components** — Present MANDATORY and OPTIONAL components. Let user customize (add/remove/modify).

3. **Quality standards check** — Ensure user agrees with research-based quality standards.

4. **Lock to discovery-log.md** — After user confirmation, write template rules to discovery log.

### Mandatory Components (Default)

Every Daily Matter MUST have:

| # | Component | Description | Research Basis |
|---|----------|-----------|----------------|
| 1 | **Daily Goal** | 1 sentence — what students will achieve today. Specific, measurable. Example: "Today you will build your first REST API using Express." | Goal-setting theory (Locke & Latham) |
| 2 | **Recall Trigger** | 1–2 retrieval practice questions about yesterday's material. Not a formal quiz — memory triggers. Example: "Try to name 3 HTTP methods you remember from yesterday." | Retrieval practice (Karpicke & Roediger, 2008) |
| 3 | **Today's Map** | 2–4 bullet points — today's journey map. No detailed theory, just direction. Example: "- Setup Express project - Create first route - Test with Postman" | Advance organizer (Ausubel, 1960) |
| 4 | **Research Bite** | 1 short insight from a journal/blog/scientific research relevant to today's topic. 2–4 sentences. Must include source/link. | Evidence-based learning (Hattie, 2009) |
| 5 | **Mini Exercise** | 1 small task that can be done independently before or at session start. Max 15 minutes. Use separate template (see Mini Exercise Template). | Active learning (Freeman et al., 2014) |
| 6 | **Reflection Prompt** | 1 reflective question for end of day. Not about "what did you understand", but about the learning process. Example: "Which concept is still confusing you today? Why?" | Metacognition & self-regulated learning (Flavell, 1979; Zimmerman, 2002) |

### Optional Components (User chooses)

| # | Component | When Suitable |
|---|----------|----------------|
| A | **Icebreaker / Fun Fact** | Bootcamp with new students, first sessions, or heavy topics |
| B | **Pre-class Reading** | Topics that need additional context before the session (articles, short videos) |
| C | **Peer Challenge** | Bootcamp with active cohort — small challenges between students |
| D | **Instructor's Note** | Personal message from instructor (motivation, tips, personal experience) |

### What is PROHIBITED in Daily Matter

| # | Prohibition | Reason |
|---|-------------|--------|
| 1 | **Long theory / concept explanation** | That's the domain of main material. Daily Matter = briefing, not lecture. |
| 2 | **Spoiling the Aha! moment** | Don't leak key insights intentionally saved for "Aha!" moments in the session. |
| 3 | **>300 words total** | Daily Matter must be readable in <3 minutes. Dense, not long. |
| 4 | **Copy-paste from main material** | DM must be original content. Not a material summary. |
| 5 | **Exercises that need >5 min setup** | Environment setup, dependency installation = main material's concern, not DM. |
| 6 | **Jargon without context** | Every new term in DM must have a 1-sentence explanation. DM is often read before the material. |
| 7 | **Research Bite without source** | Every research-based claim must have a link or journal name. |

### Mini Exercise Template (Separate)

Mini exercise uses a separate structure that is more detailed than DM itself:

| Element | Description |
|--------|-------------|
| **Title** | Exercise name, engaging and descriptive |
| **Time** | Time estimate (5–15 minutes) |
| **Objective** | 1 sentence — what is being practiced |
| **Instructions** | Clear steps, max 5 steps |
| **Starter Code** | (Optional) Starter code if coding exercise |
| **Expected Output** | (Optional) What the expected result is |
| **Hint** | (Optional) 1 hint if student gets stuck |

### Quality Checklist

Every Daily Matter later generated by Architect MUST pass this checklist:

- [ ] All 6 mandatory components present
- [ ] Research Bite has valid source (not random blogs without credibility)
- [ ] Recall Trigger genuinely tests memory of yesterday's material (not trivia)
- [ ] Total words <300
- [ ] No Aha! moment spoilers
- [ ] Mini exercise can be completed in <15 minutes
- [ ] No jargon without explanation
- [ ] Reflection Prompt is metacognitive in nature (not "understood?")

## Memory Integration

- Read `discovery-log.md` to ensure DM rules are already locked
- Write template rules (mandatory components, user-selected optional, quality checklist) to `discovery-log.md`
- Note user preferences about optional components in BOND.md

## After the Session

Log which components user chose/rejected. Note if user has special preferences about DM format or tone. Update discovery-log.md with agreed DM rules.
