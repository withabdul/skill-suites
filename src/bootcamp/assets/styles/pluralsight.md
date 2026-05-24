# Pluralsight Style Guide
*Treatment, templates, and output goals for Pluralsight-format bootcamp content*

---

## Platform Character

Pluralsight is a platform for professional developers. There are no beginners here — students already have baseline knowledge and come to level up. Content must be expert-to-expert: dense, precise, no nonsense.

**Tone target:** Precise, technical, confident. Like a senior engineer briefing a team — no time for fluff, every word must earn its place.

---

## Treatment

### Voice & Tone
- **Expert-to-expert.** No need to explain basics. "As you know, REST is stateless — here's why that matters for our caching strategy."
- **Dense but not arrogant.** Information-rich, but not insulting to those who do not know.
- **No filler.** No "great question!", no "so basically...", no unnecessary recap.
- **Opinionated with justification.** "I recommend X over Y because in production, Y causes Z."
- **Benchmark-driven.** If there are numbers, use numbers. "This reduces latency by ~40% in our benchmarks."

### Pacing
- Clips are very short: 2–5 minutes per clip. This is not a typo.
- Module = a collection of clips with one theme (15–30 minutes total).
- No filler intro. Get to the point within the first 15 seconds.
- Skill IQ assessment before and after the course — students should be able to measure progress.

### Worked Examples
- Code must be production-quality. No toy examples.
- Always show real context: "This is how we'd do this at scale."
- Compare approaches: "Approach A vs B — here's the trade-off."
- Demo tools and workflows used in real industry settings.

---

## Structure Template

### Course Level
```
[Course Title]: [Specific Skill Outcome]
├── Module 1: [Foundation — assume baseline knowledge]
│   ├── Clip: [Concept] (2–4 min)
│   ├── Clip: [Demo] (3–5 min)
│   ├── Clip: [Trade-offs / When to use] (2–3 min)
│   └── [Check: 3–5 questions]
├── Module 2–N: [Progressive complexity]
│   └── [Same structure]
└── Module Final: [Real-world scenario / capstone]
    ├── Clip: Problem setup
    ├── Clip: Implementation
    ├── Clip: Testing & edge cases
    └── Clip: Production considerations
```

### Clip Level (Gagné-adapted for expert learners)
```
[0:00–0:15] State the specific thing you'll cover — no hook needed
[0:15–X:XX] Content — dense, precise, no padding
[X:XX–Y:YY] Demo or code walkthrough
[Y:YY–end] Key takeaway in one sentence + transition
```

### Module Check Template
```
Q1: [Recall — specific fact or syntax]
Q2: [Apply — given scenario, what would you do?]
Q3: [Analyze — what's wrong with this code/approach?]
Q4: [Evaluate — which approach is better and why?]
Q5: [Edge case — what happens when X?]
```

---

## Naming Conventions

### Module Names
Format: `[Specific Technical Theme]`
- ✅ `Implementing the Repository Pattern`
- ✅ `Optimizing Database Query Performance`
- ❌ `Introduction to Databases`
- ❌ `Module 3: Backend Stuff`

### Clip Names
Format: `[Specific action or concept]`
- ✅ `Configuring Connection Pooling`
- ✅ `Benchmarking Query Execution Plans`
- ✅ `Handling Distributed Transaction Failures`
- ❌ `Overview`
- ❌ `Introduction to the Topic`

---

## Output Goals

### Per Clip
- [ ] Script (tight — every sentence earns its place)
- [ ] Code: production-quality, no toy examples
- [ ] One specific takeaway stated explicitly

### Per Module
- [ ] All clips (4–8)
- [ ] Module check (3–5 questions, mix of levels)
- [ ] Exercise or lab (optional but recommended)
- [ ] "Further depth" resources for those who want to go deeper

### Per Course
- [ ] Skill IQ pre/post assessment questions (10–15 questions)
- [ ] Course description (technical, specific — what exact skills will improve)
- [ ] Prerequisites stated explicitly
- [ ] Learning path placement (where does this fit in a skill progression?)

---

## Quality Checklist (Pluralsight-specific)
- [ ] No clip exceeds 5 minutes
- [ ] No filler phrases ("great", "basically", "so...")
- [ ] Every code example is production-quality
- [ ] Trade-offs discussed for every major decision
- [ ] Prerequisites explicitly stated — no hand-holding for basics
- [ ] Skill IQ questions test real understanding, not trivia
- [ ] "When NOT to use this" addressed somewhere in the course
