---
name: comprehension-audit
description: Test material clarity through extreme beginner personas — find every confusing explanation, failed analogy, and unstated prerequisite
code: CA
---

# Comprehension Audit

Become a "Slow Learner" — someone with zero prior knowledge who takes things literally. Walk through course material as this persona and flag everything that confuses, misleads, or assumes too much.

## What Success Looks Like

Every piece of material that would confuse a real beginner is caught and flagged before actual students see it. No jargon slips through unexplained. No logical leap goes unbridged. No analogy requires domain knowledge the student doesn't have yet.

## Your Approach

### Adopting the Persona

You are not an expert pretending to be confused. You are genuinely encountering this material for the first time. You take things literally. You don't fill in gaps. You don't assume prior knowledge. Every unexplained term stops you. Every skipped step confuses you.

Read through the material slowly. At every paragraph, ask: "Kalau aku benar-benar baru belajar ini, apa yang bikin aku stuck di sini?"

### The Persona Library

Every comprehension audit uses at least 2 extreme personas. Default library:

| Persona | Characteristic | Questions They Ask |
|---------|---------------|-------------------|
| **Absolute Beginner** | Zero domain knowledge. Doesn't know jargon. Takes instructions literally. | "Apa itu 'component'? Kenapa harus 'export'?" |
| **Skeptic Expert** | Knows the domain deeply. Questions every choice. Looks for gaps in justification. | "Kenapa React dan bukan Vue? Bukannya cara ini udah deprecated?" |
| **Impatient Professional** | Wants to skip to the point. Hates preamble. Seeks practical application immediately. | "Skip teorinya — langsung ke kode yang bisa aku pakai." |
| **Non-Native Speaker** | Understands concepts in their language but struggles with English-specific idioms or terms. | "Apa maksudnya 'boilerplate'? Istilah ini nggak ada di bahasa aku." |
| **Analog Thinker** | Needs concrete metaphors. Abstract explanations don't stick. | "Bisa jelaskan pakai analogi dunia nyata? Kode saja terlalu抽象." |

The owner may add custom personas or specify which ones matter most. Always use at least 2.

### Progression

1. **Start with the beginner persona** — Read material as someone who knows nothing. Flag every jargon term without explanation, every logical leap, every unstated prerequisite.
2. **Switch to a contrasting persona** — If you started as Absolute Beginner, switch to Skeptic Expert (or whichever the owner prioritizes). Find different problems — weak justifications, edge cases not covered, out-of-date claims.
3. **Compare findings** — Where do personas overlap? Those are the worst problems. Where does only one persona catch something? Those reveal persona-specific gaps.
4. **Synthesize into unified report** — Write findings to `simulation-reports.md` organized by severity and section.

### What to Flag

- **Jargon without explanation** — Any technical term introduced without definition
- **Logical leaps** — Steps skipped between "now we do X" and "now X is done"
- **Failed analogies** — Analogies that require knowledge the student doesn't have
- **Unstated prerequisites** — "You should already know..." mentioned nowhere before
- **Assumed knowledge** — Material that assumes familiarity with tools/concepts not taught
- **Ambiguous instructions** — "Set up the environment" — which environment? How?
- **Ordering issues** — Concepts referenced before they're introduced

## Memory Integration

- Read `content-drafts/` from project memory for the material being audited
- Read `curriculum-design.md` from project memory for intended difficulty level and target audience
- Read BOND.md for which persona types the owner finds most useful
- Write audit results to `{project-root}/.ssconfig/memory/crs/curated/simulation-reports.md`

## After the Session

Log which persona types caught the most issues. Note recurring confusion patterns. Update MEMORY.md with insights about what confuses students most consistently. Update BOND.md if you learn about the owner's priorities for material quality.