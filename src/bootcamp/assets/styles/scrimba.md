# Scrimba Style Guide
*Treatment, templates, and output goals for Scrimba-format bootcamp content*

---

## Platform Character

Scrimba is an interactive platform where students can pause the video and directly edit the instructor's code inside the video itself. This is not a regular video — it is interactive scrims. Every few minutes, students must solve a challenge before they can continue. Engagement is the core mechanic, not an extra feature.

**Tone target:** Friendly, encouraging, beginner-welcoming. Like an older sibling patiently teaching a younger sibling to code — never judgmental, always supportive, but still challenging.

---

## Treatment

### Voice & Tone
- **Warm and encouraging.** "You've got this!", "Great job getting this far!", "Don't worry if this feels confusing — it will click."
- **Celebrate small wins.** Each completed challenge = a positive moment.
- **Simple language.** Avoid jargon without explanation. If you must use jargon, define it immediately.
- **Short sentences.** Easy to follow, no long confusing sentences.
- **Frequent check-ins.** "Does that make sense so far?" "Try this yourself before I show you."

### Pacing
- Scrims (interactive videos) are very short: 2–5 minutes.
- Every 2–3 scrims = one coding challenge that the student must solve.
- No long passive watching — students must be active every 5–10 minutes.
- Challenges should be solvable in 5–15 minutes.
- Immediate feedback after each challenge (automated test or solution reveal).

### Worked Examples
- The instructor writes code slowly, explaining every line.
- Highlight code that is being discussed — no "scroll past" without explanation.
- After the demo, students immediately get a similar challenge with a small variation.
- A solution is always available after the student tries it themselves.

---

## Structure Template

### Course Level
```
[Course Title] — [Beginner-friendly outcome]
├── Module 1: [Foundation]
│   ├── Scrim: Concept intro (2–3 min)
│   ├── Scrim: Demo (3–5 min)
│   ├── 🎯 Challenge: [Specific task] (5–10 min)
│   ├── Scrim: Solution walkthrough (3–5 min)
│   └── Scrim: Recap + preview (1–2 min)
├── Module 2–N: [Building on foundation]
│   └── [Same pattern: Scrim → Scrim → Challenge → Solution → Recap]
└── Module Final: [Mini project]
    ├── Project brief scrim
    ├── 🎯 Challenge: Build the project
    └── Solution + celebration
```

### Scrim Level (per interactive video)
```
[0:00–0:20] Quick context — what we're about to do
[0:20–X:XX] Concept or demo — slow, clear, every line explained
[X:XX–end] "Now it's your turn" — transition to challenge
```

### Challenge Template
```markdown
## 🎯 Challenge: [Specific Task]

**What to do:**
[1–3 clear, specific instructions]

**Starter code is already in the editor.**

**Hints** (click to reveal):
- Hint 1: [Gentle nudge]
- Hint 2: [More specific hint]
- Hint 3: [Almost the answer]

**When you're done:** Click "Submit" to check your solution.
```

---

## Naming Conventions

### Module Names
Format: `[Simple, outcome-focused]`
- ✅ `Building Your First Component`
- ✅ `Working with Arrays`
- ✅ `Making Things Interactive`
- ❌ `Component Architecture Patterns`
- ❌ `Advanced Array Methods`

### Scrim Names
Format: `[Action verb] [simple thing]`
- ✅ `Build a color picker`
- ✅ `Fix the broken navbar`
- ✅ `Add a click event`
- ❌ `Event Handling Overview`
- ❌ `Introduction to DOM Manipulation`

### Challenge Names
Format: `🎯 [Specific, achievable task]`
- ✅ `🎯 Make the button change color on click`
- ✅ `🎯 Filter the array to show only even numbers`
- ✅ `🎯 Build a simple counter`

---

## Output Goals

### Per Scrim
- [ ] Interactive code environment (student can edit instructor's code)
- [ ] Clear, slow explanation of every line
- [ ] Transition to challenge at the end

### Per Challenge
- [ ] Starter code with clear TODO comments
- [ ] 3-tier hints (gentle → specific → near-answer)
- [ ] Automated test OR solution reveal
- [ ] Estimated completion time

### Per Module
- [ ] 3–6 scrims
- [ ] 2–4 challenges
- [ ] Module recap scrim
- [ ] Progress indicator

### Per Course
- [ ] Beginner-friendly course description (no jargon)
- [ ] "What you'll build" shown upfront (visual demo)
- [ ] Prerequisites: honest and minimal
- [ ] Certificate of completion criteria

---

## Quality Checklist (Scrimba-specific)
- [ ] No scrim exceeds 5 minutes
- [ ] Challenge follows every 2–3 scrims
- [ ] Every challenge has 3-tier hints
- [ ] Starter code is ready — student doesn't need to set up anything
- [ ] Tone is warm and encouraging throughout
- [ ] No jargon without immediate definition
- [ ] Student can complete each challenge in under 15 minutes
- [ ] Solution is available after student attempts (not before)
- [ ] Automated tests or clear success criteria for every challenge
