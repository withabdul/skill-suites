---
name: slide-architecture
description: Convert text drafts into visual presentation structures with anti-text-wall enforcement
code: SL
---

# Slide Architecture

## What Success Looks Like

Slides that are visual aids — not text walls. Each slide has ONE idea, maximum 5 supporting points, and clear visual hierarchy. The slide structure can be handed to any slide-maker tool and produce clean results. An instructor can look at the structure and know exactly what to show and what to say.

## Your Approach

### 1. One Idea Per Slide

Extract the single core message from each content section:
- Every slide answers ONE question or presents ONE concept
- If a section has multiple ideas, each gets its own slide
- The slide title IS the idea — not a label, but a statement

**Examples:**
- ❌ "State Management" → too broad, multiple ideas hiding
- ✅ "React State Lives Closest to Where It's Used" → one idea, clear
- ❅ "Common Errors" → could be 5 slides in a trench coat
- ✅ "The Most Common Error: Stale Closure in useEffect" → one idea, specific

### 2. Visual Hierarchy

Every slide follows this structure:

```
## [Title: The One Idea]

**Key Message:** One sentence that captures the core takeaway.

- Supporting point 1
- Supporting point 2
- Supporting point 3
(max 5 supporting points)

> Speaker Notes: What the instructor SAYS — not what's ON the slide.
```

**Visual hierarchy rules:**
- **Title** → The idea (6 words or fewer when possible)
- **Key Message** → The takeaway (one sentence)
- **Supporting Points** → Evidence, examples, or steps (max 5, preferably 3)
- **Speaker Notes** → What to say (the real content lives here)
- **Visual Suggestion** → What image, diagram, or code snippet to show

### 3. Anti-Text-Wall Check

This is the non-negotiable. For every slide:
1. Count the bullet points. **More than 5? Split the slide.**
2. Check for paragraphs. **Paragraphs of text? Redesign.** Convert to speaker notes.
3. Check the title. **Is it a label instead of a statement?** Rewrite it.
4. Check the key message. **Can you remove it and still understand the slide?** If yes, it's not adding value — make it essential.

**Anti-text-wall examples:**

❌ Text wall slide:
```
## React Hooks

React Hooks were introduced in React 16.8. They let you use state and other
React features without writing a class. Hooks are functions that let you
"hook into" React state and lifecycle features from function components. Common
hooks include useState, useEffect, useContext, useReducer, useCallback,
useMemo, useRef, and useImperativeHandle. Hooks must be called at the top
level of your component and cannot be called inside loops, conditions, or
nested functions.
```

✅ Redesigned as multiple slides:

```
## Hooks Let Functions Use State

**Key Message:** React Hooks allow function components to do what only class
components could do before.

- Functions can now hold state
- No more `this` confusion
- Same capabilities, simpler syntax

> Speaker Notes: "Sebelum Hooks, kalau mau pakai state, harus bikin class
> component. Ini yang bikin React terasa berat buat pemula..."
```

```
## The Rules of Hooks

**Key Message:** Hooks have two strict rules — break them and React breaks.

- Only call at the top level (not in loops/conditions)
- Only call from React function components
- ESLint plugin enforces these rules automatically

> Speaker Notes: "Dua aturan ini nggak negotiable. Kalau kamu panggil Hook
> di dalam if-statement, React nggak bisa track urutannya..."
```

### 4. Slide Types

Categorize each slide by type — this helps the slide-maker choose the right template:

| Type | Purpose | Visual Focus |
|------|---------|--------------|
| **Title Slide** | Open a section or module | Bold text, thematic image |
| **Concept Slide** | Introduce one idea | Key message + 3-5 points |
| **Code Slide** | Show code example | Code block, minimal text |
| **Demo Slide** | Point to live demo | Screenshot placeholder, link |
| **Exercise Slide** | Give hands-on task | Clear instructions, time box |
| **Recap Slide** | Summarize a section | Key takeaways only |
| **Discussion Slide** | Prompt interaction | One question, space to think |

### 5. Speaker Notes

Every slide MUST include speaker notes. The slide is what the AUDIENCE sees. The speaker notes are what the INSTRUCTOR says.

**Speaker notes rules:**
- Written in conversational language (not academic tone)
- Include the "why" — why this slide matters, why now
- Include transitions — how to connect to the previous slide
- Include timing — rough estimate of how long to spend here
- Include interaction prompts — questions to ask, signals to watch for

**Example:**
```
> Speaker Notes: "Oke, kita masuk bagian yang paling sering bikin orang stuck.
> Jangan khawatir kalau belum langsung ngerti — ini normal. Yang penting:
> setiap efek punya cleanup, setiap dependency punya alasan. Kita bahas
> pelan-pelan." [2-3 minutes, pause after first code example]
```

## Output Format

### Markdown Structure (default)

```markdown
---

### [Slide Type: Concept Slide]

## [Title]

**Key Message:** [One sentence]

- [Point 1]
- [Point 2]
- [Point 3]

> Speaker Notes: [What to say]

_[Visual suggestion: description of image/diagram/code]_

---
```

### JSON Structure (for programmatic generation)

```json
{
  "slides": [
    {
      "type": "concept",
      "title": "Hooks Let Functions Use State",
      "key_message": "React Hooks allow function components to do what only class components could do before.",
      "points": [
        "Functions can now hold state",
        "No more `this` confusion",
        "Same capabilities, simpler syntax"
      ],
      "speaker_notes": "Sebelum Hooks, kalau mau pakai state...",
      "visual_suggestion": "Side-by-side: class component vs function component with Hook",
      "timing_minutes": 3
    }
  ]
}
```

## Common Slide Patterns

### Concept Introduction
```
## [Concept Name]

**Key Message:** [What it is in one sentence]

- Why it exists (the problem it solves)
- How it works (simplified)
- Where you'll use it (practical context)

> Speaker Notes: Context → definition → example flow
```

### Code Walkthrough
```
## [What This Code Does]

**Key Message:** [One thing this code demonstrates]

```language
// Only the essential lines — annotated
```

- [Line-by-line explanation — max 3-4 lines shown]
- [What to watch for]

> Speaker Notes: Walk through slowly. Point at each line.
_[Visual: syntax-highlighted code with line numbers]_
```

### Exercise Instruction
```
## [Exercise Title]

**Goal:** [One sentence what they'll achieve]

1. [Step 1]
2. [Step 2]
3. [Step 3]

⏱️ [Time box: X minutes]

> Speaker Notes: "Coba sendiri dulu X menit. Kalau stuck, angkat tangan."
```

### Section Recap
```
## What We Learned

- [Key takeaway 1]
- [Key takeaway 2]
- [Key takeaway 3]

> Speaker Notes: Quick recap, ask if anyone has questions before moving on.
```

## Memory Integration

- Read `content-drafts/` for the material to convert into slides
- Read `curriculum-design.md` for flow and sequence context
- Read `instructor-profile.md` for tone and pace guidance
- Write slide structures to `content-drafts/` with `-slides` suffix

## After the Session

Log to session notes:
- Slide patterns that worked well for this content domain
- Any content sections that resisted visual simplification (flag for redesign)
- Bullet point counts on all slides produced (audit yourself)
- Owner preferences around visual density and code on slides