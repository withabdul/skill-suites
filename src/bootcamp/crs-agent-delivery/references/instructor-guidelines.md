---
name: instructor-guidelines
description: Write Tone of Voice guides, Q&A handling strategies, and teaching tempo for course instructors
code: IG
---

# Instructor Guidelines

## What Success Looks Like

An instructor who has never taught this course before can pick up the delivery guide and know exactly how to present each section — tone, tempo, what to emphasize, what to simplify, how to handle hard questions. The guide is self-contained and usable by any instructor, not just the expert who wrote the material.

## Style Context
Before writing any guidelines, read `{project-root}/.ssconfig/memory/crs/{active-project}/project-config.yaml` to get `style_file`. Load `{skill-root}/../{style_file}` and read the Treatment section — specifically Voice & Tone and Pacing. The instructor guidelines must align with the selected style. A Scrimba-style course needs warm, encouraging delivery notes. A Pluralsight-style course needs precise, no-filler delivery notes. A Frontend Masters-style course needs "think out loud" coaching.

## Your Approach

### 1. Tone of Voice Profile

Define the instructor persona for this course:
- **Formal vs. Casual** — Is this a university lecture, a friendly workshop, or something in between? The tone determines trust and accessibility.
- **Technical Depth** — How much jargon is acceptable? When to use technical terms vs. plain language? Define the ceiling and the floor.
- **Humor Level** — Is humor appropriate? What kind? Self-deprecating, observational, situational? Humor disarms but can also distract.
- **Encouragement Style** — How does the instructor signal "you're doing fine" without being patronizing? When to push and when to reassure?

**Example tone variations for different content types:**

| Content Type | Tone | Example Phrase |
|--------------|------|----------------|
| Concept Introduction | Warm, inviting | "Okay, now we get to the fun part..." |
| Technical Deep-Dive | Precise, steady | "Pay attention to this detail — this is what often trips people up." |
| Exercise Instructions | Encouraging, clear | "Try it yourself first. If you get stuck, that's okay — that's part of learning." |
| Error Explanation | Patient, normalizing | "If you get this error, it doesn't mean you're wrong. This is the MOST common error." |
| Recap | Confident, summarizing | "So what did we learn? Three important things..." |

### 2. Tempo Planning

Map which sections need slow, careful delivery vs. which can be brisk:
- **Slow Zones** — New concepts, paradigm shifts, error-prone areas. Mark these as "pause points" where students need processing time.
- **Brisk Zones** — Review material, familiar patterns, exercises that click quickly. Energy stays up but comprehension isn't at risk.
- **Pause Points** — Explicit marks like `[PAUSE 3 seconds]` or `[CHECK FOR UNDERSTANDING]` where the instructor should stop and let the material sink in.

**Tempo pattern example:**
```
Module 3: React State Management
├── Introduction (brisk) — they know state conceptually
├── useState deep-dive (slow) — new mental model
│   └── [PAUSE] after first example — let them process
├── Common mistakes (slow) — error-prone territory  
│   └── [CHECK] "Who has ever gotten stuck in an infinite loop?"
├── Exercise (brisk) — hands-on, energy up
└── Recap (brisk) — reinforcement, confidence builder
```

### 3. Q&A Strategy

Prepare responses for common difficult questions:
- **Explain Now** — Questions that reveal a gap everyone has. Answer immediately, even if it means diverging slightly.
- **Park for Later** — Questions that are valid but would derail the current topic. Acknowledge, validate, and commit to revisiting.
- **Redirect** — Questions where the student is on the wrong track. Guide them back without dismissing.
- **Honest Unknown** — Questions where the instructor doesn't know. Model how to say "I'm not sure, let me check" — this builds trust.

**Template for parked questions:**
> "Good question. We haven't gotten there yet, but I'll note it — we'll cover it after this module."

**Template for redirected questions:**
> "Your line of thinking is right, but let's look at it from this angle first..."

### 4. Transition Scripts

How to move between topics naturally:
- **Bridge:** Connect previous knowledge to upcoming material ("If we just covered X, now imagine X combined with Y...")
- **Reset:** Clear the mental slate for a new topic ("Okay, now we move into a new topic. Set aside what we just covered for a moment...")
- **Motivation:** Why the next section matters ("This part often makes people want to give up — but it's also what gives them that 'aha!' at the end.")

### 5. Energy Management

When to raise energy, lower energy, or use humor:
- **After difficult sections** — Raise energy with an exercise, a relatable story, or a "you survived!" moment
- **During processing time** — Lower energy deliberately. Silence is okay. Pauses are pedagogical tools.
- **Humor timing** — Best after tension (a hard concept), worst during focus (a step-by-step walkthrough)
- **Near the end** — Energy pick-me-up. Students are tired. Use interactive moments, not more lecture.

## Memory Integration

- Read `discovery-log.md` for instructor persona preferences and course context
- Read `content-drafts/` for the material to guide
- Read `BOND.md` for owner's teaching style preferences
- Write results to `instructor-profile.md` and `content-drafts/` as delivery annotations

## After the Session

Log to session notes:
- Tone patterns that worked well for this owner
- Common difficult questions identified in this domain
- Tempo insights — which sections naturally need more time
- Anything the owner explicitly asked to remember about delivery style