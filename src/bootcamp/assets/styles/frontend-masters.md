# Frontend Masters Style Guide
*Treatment, templates, and output goals for Frontend Masters-format bootcamp content*

---

## Platform Character

Frontend Masters is a recorded live-workshop platform. The content feels like you're sitting in an intensive workshop with the best experts in the field. The instructor thinks out loud in front of you — including making mistakes and fixing them. This is not a lecture; it is pair programming with a master.

**Tone target:** Live workshop energy. Thoughtful, deep, unscripted-feeling. Like watching an expert work and explain their thinking in real time.

---

## Treatment

### Voice & Tone
- **Think out loud.** "Hmm, let me think about this... actually, I think the better approach here is..."
- **Embrace uncertainty.** "I'm not 100% sure this is the best way, but here's my reasoning."
- **Deep over broad.** One topic is explored to completion, not a survey of every topic.
- **Socratic.** Frequently ask the audience: "What do you think would happen if we did X?"
- **Honest about complexity.** "This is genuinely hard. Here's why it's hard, and here's how I think about it."

### Pacing
- Workshop format: 4–8 hours total, divided into sections.
- No target duration per segment — stop when the concept is complete, not when the timer ends.
- Many pauses for questions and discussion.
- Code-along: students are expected to code alongside the instructor.
- No "quick win" at the start — depth begins in minute one.

### Worked Examples
- The instructor builds something from scratch, live, without a safety net.
- Mistakes are part of the content — do not edit them out.
- Every design decision is explained: "I'm choosing X here because..."
- Refactoring is a normal part of the flow — "Actually, let me rethink this structure."

---

## Structure Template

### Course Level
```
[Course Title]: [Deep Concept]
├── Introduction (15–30 min)
│   ├── What we'll build / explore
│   ├── Why this topic matters deeply
│   └── Prerequisites check
├── Part 1–N: [Deep Theme] (60–120 min each)
│   ├── Concept exploration (think out loud)
│   ├── Live implementation
│   ├── Q&A / discussion
│   ├── Exercise (students try independently)
│   └── Solution walkthrough + discussion
└── Conclusion (15–30 min)
    ├── What we built / learned
    ├── Where to go deeper
    └── Common pitfalls to avoid
```

### Segment Level
```
[No strict timing — follow the concept]
- Open with the problem or question, not the answer
- Explore multiple approaches before settling
- Implement live — mistakes included
- Pause for questions at natural breakpoints
- Summarize the insight, not just the code
```

### Exercise Template
```markdown
## Exercise: [Specific Challenge]

**Context:** [1–2 sentences setting up the scenario]

**Your task:**
1. [Specific step]
2. [Specific step]
3. [Stretch goal — optional]

**Hints:**
- [Hint 1 — only if genuinely needed]
- [Hint 2]

**Time:** ~[N] minutes

**After:** We'll walk through the solution together and discuss different approaches.
```

---

## Naming Conventions

### Course Names
Format: `[Deep Concept] [optional: with/in/for context]`
- ✅ `The Hard Parts of Closures and Scope`
- ✅ `Complete Intro to React`
- ✅ `Full Stack for Front-End Engineers`
- ❌ `React Tutorial`
- ❌ `JavaScript Basics`

### Part/Section Names
Format: `[Conceptual theme — not action-based]`
- ✅ `Closure and the Execution Context`
- ✅ `Prototypal Inheritance`
- ❌ `Building the Component`
- ❌ `Step 3: Adding State`

### Exercise Names
Format: `Exercise: [Open-ended challenge]`
- ✅ `Exercise: Implement your own bind()`
- ✅ `Exercise: Build a pub/sub system from scratch`

---

## Output Goals

### Per Segment
- [ ] Concept outline (not a script — key questions to explore, not answers to deliver)
- [ ] Live code starting point
- [ ] Exercise with solution
- [ ] "Deeper dive" references for those who want more

### Per Part
- [ ] All segments
- [ ] One substantial exercise
- [ ] Discussion questions for Q&A

### Per Course
- [ ] Course outline with conceptual arc (not just topic list)
- [ ] Prerequisites stated honestly
- [ ] "What you'll understand deeply" (not just "what you'll build")
- [ ] Recommended follow-up courses/resources

---

## Quality Checklist (Frontend Masters-specific)
- [ ] Instructor thinking process is visible — not just the result
- [ ] Mistakes happen and are fixed on camera
- [ ] Every major decision is explained, not just executed
- [ ] Exercises require genuine thinking, not just copying
- [ ] Depth over breadth — one concept fully understood beats five concepts surveyed
- [ ] "Why" is answered before "how"
- [ ] Student can follow along and code simultaneously
