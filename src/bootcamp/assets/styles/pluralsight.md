# Pluralsight Style Guide
*Treatment, templates, and output goals for Pluralsight-format bootcamp content*

---

## Platform Character

Pluralsight adalah platform untuk professional developers. Tidak ada pemula di sini — student sudah punya baseline knowledge dan datang untuk naik level. Konten harus expert-to-expert: padat, presisi, tanpa basa-basi.

**Tone target:** Precise, technical, confident. Seperti senior engineer yang briefing tim — tidak ada waktu untuk fluff, setiap kata harus earn its place.

---

## Treatment

### Voice & Tone
- **Expert-to-expert.** Tidak perlu explain basics. "As you know, REST is stateless — here's why that matters for our caching strategy."
- **Dense tapi tidak arrogant.** Padat informasi, tapi tidak menghina yang belum tahu.
- **No filler.** Tidak ada "great question!", tidak ada "so basically...", tidak ada recap yang tidak perlu.
- **Opinionated dengan justifikasi.** "I recommend X over Y because in production, Y causes Z."
- **Benchmark-driven.** Kalau ada angka, pakai angka. "This reduces latency by ~40% in our benchmarks."

### Pacing
- Clips sangat pendek: 2–5 menit per clip. Ini bukan typo.
- Module = kumpulan clips dengan satu tema (15–30 menit total).
- Tidak ada filler intro. Langsung ke inti dalam 15 detik pertama.
- Skill IQ assessment sebelum dan sesudah course — student harus bisa ukur progress.

### Worked Examples
- Code harus production-quality. Tidak ada toy examples.
- Selalu tunjukkan konteks nyata: "This is how we'd do this at scale."
- Bandingkan pendekatan: "Approach A vs B — here's the trade-off."
- Demo tools dan workflow yang dipakai di industri nyata.

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
