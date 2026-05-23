# Scrimba Style Guide
*Treatment, templates, and output goals for Scrimba-format bootcamp content*

---

## Platform Character

Scrimba adalah platform interaktif di mana student bisa pause video dan langsung edit kode instructor di dalam video itu sendiri. Ini bukan video biasa — ini adalah interactive scrims. Setiap beberapa menit, student harus solve a challenge sebelum bisa lanjut. Engagement adalah core mechanic, bukan fitur tambahan.

**Tone target:** Friendly, encouraging, beginner-welcoming. Seperti kakak yang sabar mengajari adiknya coding — tidak pernah menghakimi, selalu supportive, tapi tetap challenging.

---

## Treatment

### Voice & Tone
- **Warm dan encouraging.** "You've got this!", "Great job getting this far!", "Don't worry if this feels confusing — it will click."
- **Celebrate small wins.** Setiap challenge yang selesai = momen positif.
- **Simple language.** Hindari jargon tanpa penjelasan. Kalau harus pakai jargon, define immediately.
- **Short sentences.** Mudah diikuti, tidak ada kalimat panjang yang membingungkan.
- **Frequent check-ins.** "Does that make sense so far?" "Try this yourself before I show you."

### Pacing
- Scrim (interactive video) sangat pendek: 2–5 menit.
- Setiap 2–3 scrim = satu coding challenge yang harus diselesaikan student.
- Tidak ada passive watching yang panjang — student harus aktif setiap 5–10 menit.
- Challenge harus bisa diselesaikan dalam 5–15 menit.
- Immediate feedback setelah challenge (automated test atau solution reveal).

### Worked Examples
- Instructor menulis kode perlahan, menjelaskan setiap baris.
- Highlight kode yang sedang dibahas — tidak ada "scroll past" tanpa penjelasan.
- Setelah demo, student langsung diberi challenge yang mirip tapi sedikit berbeda.
- Solution selalu tersedia setelah student mencoba sendiri.

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
