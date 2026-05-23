# Frontend Masters Style Guide
*Treatment, templates, and output goals for Frontend Masters-format bootcamp content*

---

## Platform Character

Frontend Masters adalah platform workshop live yang direkam. Konten terasa seperti kamu duduk di workshop intensif bersama expert terbaik di bidangnya. Instructor berpikir keras di depan kamu — termasuk membuat kesalahan dan memperbaikinya. Ini bukan lecture, ini adalah pair programming dengan master.

**Tone target:** Live workshop energy. Thoughtful, deep, unscripted-feeling. Seperti nonton seorang expert bekerja dan menjelaskan pikirannya secara real-time.

---

## Treatment

### Voice & Tone
- **Think out loud.** "Hmm, let me think about this... actually, I think the better approach here is..."
- **Embrace uncertainty.** "I'm not 100% sure this is the best way, but here's my reasoning."
- **Deep over broad.** Satu topik dibahas sampai tuntas, bukan survey semua topik.
- **Socratic.** Sering tanya ke audience: "What do you think would happen if we did X?"
- **Honest about complexity.** "This is genuinely hard. Here's why it's hard, and here's how I think about it."

### Pacing
- Workshop format: 4–8 jam total, dibagi jadi sections.
- Tidak ada target durasi per segment — berhenti ketika konsep selesai, bukan ketika timer habis.
- Banyak pause untuk pertanyaan dan diskusi.
- Code-along: student diharapkan coding bersamaan dengan instructor.
- Tidak ada "quick win" di awal — depth dimulai dari menit pertama.

### Worked Examples
- Instructor membangun sesuatu dari scratch, live, tanpa safety net.
- Kesalahan adalah bagian dari konten — jangan edit out.
- Setiap keputusan design dijelaskan: "I'm choosing X here because..."
- Refactoring adalah bagian normal dari flow — "Actually, let me rethink this structure."

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
