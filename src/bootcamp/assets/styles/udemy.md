# Udemy Style Guide
*Treatment, templates, and output goals for Udemy-format bootcamp content*

---

## Platform Character

Udemy is an open marketplace. The instructor is the brand. The instructor's personality and energy are what make a course succeed — not the institution. Students buy because they trust the instructor, not the platform.

**Tone target:** Energetic, direct, personal. Like talking with a senior developer who is excited to share knowledge.

---

## Treatment

### Voice & Tone
- **First person, direct.** "I'll show you how to..." not "In this lesson, we will..."
- **Conversational.** Contractions are welcome (you'll, we'll, let's). Avoid formal language.
- **Enthusiastic but not over the top.** High energy, but not forced.
- **Acknowledge struggle.** "This part trips up a lot of people — here's why." Empathy for the learner.
- **Opinionated.** The instructor can have preferences. "I prefer this approach because..." is more engaging than "there are multiple ways."

### Pacing
- One concept per video. Do not combine two topics in one lecture.
- Video 5–10 minutes. More than 12 minutes = split into two.
- Every section (3–8 lectures) should have one clear deliverable.
- Start the course with a "quick win" in lectures 2–3 — something students can try immediately.

### Worked Examples
- Always code live, not paste finished code. Students should see the process, not just the result.
- Make a typo and fix it on camera — this is normal and helps students learn debugging.
- After the demo, give an exercise that is similar but with a small variation.

---

## Structure Template

### Course Level
```
[Course Title] — [Outcome in 5 words]
├── Section 0: Welcome & Setup (2–3 lectures)
│   ├── What you'll build (show the final project)
│   ├── Tools & environment setup
│   └── Quick win: first working code
├── Section 1–N: [Theme] (4–8 lectures each)
│   ├── Lecture: Concept intro (5–8 min)
│   ├── Lecture: Live demo / code-along (8–12 min)
│   ├── Lecture: Exercise walkthrough (5–10 min)
│   └── [Quiz: 3–5 questions] (optional, end of section)
└── Section Final: Capstone Project
    ├── Project brief & requirements
    ├── Guided build (broken into 3–5 lectures)
    └── Review & next steps
```

### Lecture Level (Gagné-aligned)
```
[0:00–0:30] Hook — show the problem or the end result
[0:30–1:00] Objective — "By the end of this, you'll be able to..."
[1:00–X:XX] Content — explain the concept (max 5 min)
[X:XX–Y:YY] Demo — live code the example
[Y:YY–end] Wrap — summarize + preview next lecture
```

### Section Resource Pack (per section)
- `code-starter/` — starter files for exercises
- `code-solution/` — solution files (released after exercise)
- `cheatsheet.pdf` — key concepts, syntax reference
- `resources.md` — links to docs, further reading

---

## Naming Conventions

### Section Names
Format: `Section [N]: [Action Phrase]`
- ✅ `Section 3: Building the REST API`
- ✅ `Section 5: Adding Authentication`
- ❌ `Section 3: REST API Concepts`
- ❌ `Module 3 — Backend`

### Lecture Names
Format: `[Action verb] [specific thing]`
- ✅ `Setting Up Express Routes`
- ✅ `Connecting to MongoDB`
- ✅ `Debugging the Login Flow`
- ❌ `Introduction to Routes`
- ❌ `MongoDB Overview`

### Exercise Names
Format: `Exercise: [specific task]`
- ✅ `Exercise: Build a GET /users endpoint`
- ✅ `Exercise: Add JWT validation middleware`

---

## Output Goals

### Per Lecture
- [ ] Video script or outline (not word-for-word, but key points + code flow)
- [ ] Code files: starter + solution
- [ ] One exercise with clear success criteria

### Per Section
- [ ] Section intro text (shown in Udemy UI, 2–3 sentences)
- [ ] Resource pack (cheatsheet + links)
- [ ] Optional quiz (3–5 questions, concept check)
- [ ] One deliverable student can show/run

### Per Course
- [ ] Course description (Udemy format: bold hook → bullet outcomes → who it's for → requirements)
- [ ] Promo video script (2 min: problem → solution → what you'll build → CTA)
- [ ] Final capstone project spec with rubric
- [ ] Certificate-worthy outcome statement

---

## Quality Checklist (Udemy-specific)
- [ ] Every lecture starts with a hook (problem or demo of end result)
- [ ] No lecture exceeds 12 minutes
- [ ] Every section ends with something students can run/show
- [ ] Worked example shown BEFORE exercise is assigned
- [ ] Code files provided for every coding lecture
- [ ] Instructor personality comes through — not robotic
- [ ] Quick win exists within first 30 minutes of course
