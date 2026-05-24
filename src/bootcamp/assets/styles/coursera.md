# Coursera Style Guide
*Treatment, templates, and output goals for Coursera-format bootcamp content*

---

## Platform Character

Coursera is an academic-adjacent platform. Content is often created with universities or institutions. Students come for recognized credentials, not just skills. Structure and rigor matter more than personality.

**Tone target:** Authoritative but accessible. Like a good professor — structured, clear, but not stiff.

---

## Treatment

### Voice & Tone
- **Third-person aware, second-person delivery.** "In this course, you will..." not "I'll show you..."
- **Structured.** Every statement has context. No implicit assumptions.
- **Precise.** Use the correct terminology. Define terms before use.
- **Measured pacing.** Not rushed. Give concepts room to settle.
- **Evidence-based.** If there is a claim, there is justification. "Research shows..." or "In practice, this means..."

### Pacing
- Video 6–12 minutes per clip. More structured than Udemy.
- Each week = one big theme with 3–5 videos + reading + quiz.
- A graded assignment is required at the end of every week.
- A discussion prompt in each module for peer interaction.

### Worked Examples
- More annotated code and diagrams than live coding.
- Each concept has a "real-world application" section — where this is used in industry.
- Case studies from real companies are more effective than abstract examples.

---

## Structure Template

### Course Level
```
[Course Title]: [Outcome Statement]
├── Week 1: [Foundation Theme]
│   ├── Video: Introduction & Overview (5–8 min)
│   ├── Video: Core Concept A (8–12 min)
│   ├── Video: Core Concept B (8–12 min)
│   ├── Reading: [Supplementary material]
│   ├── Practice Quiz (ungraded, 5–10 questions)
│   └── Graded Assignment: [Deliverable]
├── Week 2–N: [Progressive Theme]
│   └── [Same structure]
└── Week Final: Capstone
    ├── Project brief
    ├── Peer review rubric
    └── Final submission
```

### Video Level (Gagné-aligned)
```
[0:00–0:30] Learning objective stated explicitly
[0:30–2:00] Context — why this matters, real-world relevance
[2:00–8:00] Content delivery — concept + examples
[8:00–10:00] Summary + connection to next video
[End] "In the next video, we'll explore..."
```

### Weekly Reading Template
```markdown
## [Topic Name]

### Overview
[2–3 sentence summary of what this reading covers]

### Key Concepts
**[Term 1]:** [Definition + example]
**[Term 2]:** [Definition + example]

### Deep Dive
[Main content — 400–800 words]

### Real-World Application
[How this is used in industry — specific example]

### Further Reading
- [Link 1] — [why it's relevant]
- [Link 2] — [why it's relevant]
```

---

## Naming Conventions

### Week/Module Names
Format: `Week [N]: [Descriptive Theme]`
- ✅ `Week 2: Data Structures and Algorithm Complexity`
- ✅ `Week 4: Building RESTful APIs`
- ❌ `Week 2: More Advanced Topics`

### Video Names
Format: `[N.M] [Descriptive Title]`
- ✅ `2.1 Understanding Big O Notation`
- ✅ `3.4 Implementing JWT Authentication`
- ❌ `Video 4: Authentication`

### Assignment Names
Format: `[Week N] Assignment: [Specific Task]`
- ✅ `Week 2 Assignment: Implement a Binary Search Tree`
- ✅ `Week 4 Assignment: Build a CRUD API with Authentication`

---

## Assessment Design

### Practice Quiz (ungraded, per video or module)
- 5–10 multiple choice questions
- Immediate feedback with explanation
- Tests Remember + Understand levels (Bloom's)
- Can be retaken unlimited times

### Graded Assignment (per week)
- Peer-reviewed OR auto-graded
- Must have a clear rubric (3–5 criteria, each with point values)
- Submission format: code + written reflection OR just code with tests
- Rubric criteria example:
  ```
  Functionality (40 pts): Does the code work as specified?
  Code Quality (30 pts): Is the code readable and well-structured?
  Documentation (20 pts): Are functions documented?
  Edge Cases (10 pts): Does it handle invalid inputs?
  ```

### Peer Review Guidelines
- Reviewer must complete the assignment before reviewing others
- Minimum 3 reviews per student
- Structured feedback form: What works well? What could be improved? Specific suggestion?

---

## Output Goals

### Per Video
- [ ] Script (full or detailed outline)
- [ ] Slide deck (if applicable) — clean, minimal text, visual-heavy
- [ ] Transcript (for accessibility + subtitles)
- [ ] Code examples with annotations

### Per Week
- [ ] All videos (3–5)
- [ ] Reading material (1–2 documents)
- [ ] Practice quiz with answer key + explanations
- [ ] Graded assignment with rubric
- [ ] Discussion prompt (1 open-ended question)

### Per Course
- [ ] Course syllabus (week-by-week breakdown)
- [ ] Learning outcomes (Bloom's-aligned, measurable)
- [ ] Glossary of key terms
- [ ] Final capstone with peer review rubric
- [ ] Certificate criteria statement

---

## Quality Checklist (Coursera-specific)
- [ ] Every video states learning objective in first 30 seconds
- [ ] All technical terms defined before use
- [ ] Real-world application included in every module
- [ ] Graded assignment has clear rubric
- [ ] Practice quiz available before graded assessment
- [ ] Discussion prompt encourages peer learning
- [ ] Accessibility: transcripts available, slides readable without audio
- [ ] Bloom's level explicitly targeted per assessment
