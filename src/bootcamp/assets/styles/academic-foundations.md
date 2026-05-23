# Academic Foundations for Bootcamp Course Design
*Evidence-based principles distilled from instructional design research*
*Sources: Bloom (1956/2001), Gagné (1965), Sweller (1988), Wiggins & McTighe (1998), Lang & Sharp (2022, ISEDJ), UF STEM bootcamp study (2019, PMC)*

---

## 1. Backward Design (Wiggins & McTighe, 1998)

**Core principle:** Start from the desired end result, work backward to design instruction.

### Three Stages
1. **Identify desired results** — What should students be able to DO? Not "cover topic X" but "student can build Y."
2. **Determine acceptable evidence** — How will you know they can do it? (assessment, project, demo)
3. **Plan learning experiences** — Only then design lessons, exercises, content

### Application to Bootcamp
- Define the capstone project FIRST, then reverse-engineer the curriculum
- Every lesson must answer: "Does this directly enable the capstone?"
- Cut anything that doesn't trace to a capstone skill

---

## 2. Bloom's Revised Taxonomy (Anderson & Krathwohl, 2001)

**Core principle:** Learning is hierarchical — lower levels must be solid before higher levels are attempted.

### Six Levels (low → high)
| Level | Verb examples | Bootcamp application |
|-------|--------------|---------------------|
| **Remember** | define, list, recall | Terminology, syntax, API names |
| **Understand** | explain, describe, summarize | Concept explanations, analogies |
| **Apply** | use, execute, implement | Guided exercises, code-along |
| **Analyze** | differentiate, compare, debug | Debugging exercises, code review |
| **Evaluate** | judge, critique, justify | Architecture decisions, trade-off discussions |
| **Create** | design, build, produce | Mini-projects, capstone |

### Application to Bootcamp
- Each lesson should target ONE level explicitly
- Don't jump to Apply before Remember/Understand are solid
- Exercises should climb the taxonomy within a module: guided → independent → creative
- Assessment verbs must match the target level — "explain" ≠ "build"

---

## 3. Gagné's Nine Events of Instruction (1965)

**Core principle:** Effective instruction follows a predictable sequence that mirrors how the brain processes and stores new information.

### Nine Events Applied to a Bootcamp Lesson
| Event | What it means | Concrete implementation |
|-------|--------------|------------------------|
| 1. **Gain attention** | Hook the learner | Real problem, surprising fact, demo of what they'll build |
| 2. **Inform objectives** | Tell them what they'll be able to do | "After this lesson, you can build X" |
| 3. **Stimulate recall** | Connect to prior knowledge | "Remember when we did Y? This builds on that." |
| 4. **Present content** | Deliver the new material | Video, text, live demo — max 10 min |
| 5. **Provide guidance** | Show HOW to do it | Worked example, annotated code, step-by-step walkthrough |
| 6. **Elicit performance** | Make them do it | Exercise, coding challenge |
| 7. **Provide feedback** | Tell them if they did it right | Automated tests, rubric, instructor review |
| 8. **Assess performance** | Formal check | Quiz, submission, code review |
| 9. **Enhance retention** | Help them remember long-term | Spaced review, apply in next module's project |

### Application to Bootcamp
- Every lesson should hit events 1–7 at minimum
- Events 8–9 happen at module level (not every lesson)
- Event 5 (guidance) is the most skipped — always include a worked example before asking students to do it themselves

---

## 4. Cognitive Load Theory (Sweller, 1988; applied to programming by multiple studies)

**Core principle:** Working memory is limited. Instruction that overloads it causes failure to learn, not failure of the student.

### Three Types of Load
| Type | Definition | Design implication |
|------|-----------|-------------------|
| **Intrinsic** | Complexity of the material itself | Can't eliminate, but can sequence (simple → complex) |
| **Extraneous** | Complexity caused by poor design | ELIMINATE — unclear instructions, irrelevant info, bad formatting |
| **Germane** | Mental effort that builds understanding | MAXIMIZE — worked examples, self-explanation prompts |

### Worked Example Effect (Sweller; confirmed in programming education)
- Novices learn better from studying worked examples than from solving problems independently
- **Faded worked examples** are most effective: full example → partial example → blank problem
- Research (Chen et al., 2025, ACM TOCE): worked examples with self-explanation prompts outperform worked examples alone

### Application to Bootcamp
- **Never** give a blank exercise before showing a worked example
- Sequence: full worked example → guided exercise (partial) → independent exercise → creative challenge
- Keep each lesson to ONE new concept — introducing two concepts simultaneously doubles intrinsic load
- Code examples must be minimal — strip everything not relevant to the concept being taught
- Avoid "split attention effect": don't separate code from its explanation (keep them together on screen/page)

---

## 5. Spaced Repetition & Retrieval Practice

**Core principle:** Memory is strengthened by retrieval, not by re-reading. Spacing practice over time beats massed practice.

### Evidence
- Springer Nature (2024): spaced retrieval practice shows positive effects across 9 introductory STEM courses
- Karpicke (2025): retrieval-based learning review confirms robust effects across domains
- Programming-specific: students who practice retrieval (quizzes, recall exercises) retain more than those who re-read code

### Application to Bootcamp
- **Interleave** concepts across modules — don't teach a concept once and never revisit it
- **Low-stakes quizzes** at the start of each session (recall from previous session)
- **Spaced projects** — capstone should require applying skills from earlier modules, not just the current one
- **Reflection prompts** at end of each module: "What were the 3 key things you learned? Where would you use them?"

---

## 6. Coding Bootcamp Satisfaction Research (Lang & Sharp, 2022, ISEDJ)

**Source:** Qualitative analysis of 28,000+ student reviews across 500+ coding bootcamps.

### Top 5 Satisfaction Factors (by complexity/impact)
1. **Appropriateness of Pedagogy** (10 variables) — most complex, highest impact
   - Balance conceptual and hands-on learning
   - Support varying levels of prior knowledge (scaffolding)
   - Facilitate real-world exercises/projects
   - Timely and detailed feedback on assessments
   - Challenge without overwhelming

2. **Provision of Career Services** (7 variables)
   - Job search support, mock interviews, portfolio positioning

3. **Rigor of Curriculum** (6 variables)
   - Teach in-demand skills and industry best practices
   - Balance hard and soft skills
   - Structure topics logically

4. **Quality of Instructors** (6 variables)
   - Knowledgeable, caring, passionate, industry-experienced, inspiring, available

5. **Use of Appropriate Technology** (5 variables)
   - Collaboration tools, Q&A facilitation, assignment submission + feedback

### Key Insight for Content Design
Students value **immediate, detailed feedback** and **real-world relevance** above almost everything else. A technically perfect curriculum with slow/vague feedback will fail. A slightly imperfect curriculum with fast, specific feedback will succeed.

---

## 7. Bootcamp Format Effectiveness (UF STEM Study, PMC 2019)

**Finding:** Bootcamp format (compressed, intensive) produces **comparable learning outcomes** to traditional semester-long format. GPA (prior academic ability) is the strongest predictor of success — not format.

### Implications
- Intensity works — don't dilute the curriculum to reduce difficulty
- Pre-course preparation matters: students who completed an online prep module before the face-to-face bootcamp performed better
- **Hybrid model** (online prep + intensive face-to-face) is the most effective format tested

### Application to Bootcamp Design
- Include a **pre-course module** that sets foundations and expectations
- Intensive pacing is fine — but prerequisites must be clearly communicated and enforced
- Don't assume format alone drives outcomes — instructor quality and curriculum rigor matter more

---

## Summary: Design Principles Hierarchy

When designing any bootcamp module or lesson, apply in this order:

1. **Backward Design** — define the outcome and capstone first
2. **Bloom's Taxonomy** — sequence lessons from Remember → Create
3. **Gagné's Events** — structure each lesson with all 9 events
4. **Cognitive Load** — worked examples before exercises, one concept per lesson
5. **Spaced Retrieval** — interleave and revisit concepts across modules
6. **Satisfaction Research** — prioritize feedback speed, real-world relevance, scaffolding
