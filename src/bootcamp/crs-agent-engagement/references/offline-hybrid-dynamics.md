---
name: offline-hybrid-dynamics
description: Design physical and interactive activities for offline and hybrid bootcamp sessions that can't be replicated online
code: OH
---

# Offline/Hybrid Dynamics

Offline sessions are a superpower — they offer things pure online can't: body language, pair energy, real-time debugging side-by-side, the buzz of collective struggle. Design for that superpower or you're just doing an online course in a room.

## What Success Looks Like

Offline/hybrid sessions have activities that are **impossible to replicate online** — group debugging, physical movement, live pair programming, whiteboard chaos, retrospective circles. Every offline moment is intentional: either leveraging physical presence or creating connection that sustains the online-only parts.

## Style Context
Before designing activities, read `{project-root}/.ssconfig/memory/crs/{active-project}/project-config.yaml` to get `style_file`. Load `{skill-root}/../{style_file}` and read the Pacing and Structure Template sections. Offline/hybrid activity design must align with the selected style:
- **Scrimba style** — frequent short challenges, immediate feedback loops, celebrate every win
- **Frontend Masters style** — deep group exploration, think-out-loud sessions, whiteboard architecture discussions
- **Udemy style** — code-along workshops, instructor-led demos with student follow-along
- **Coursera style** — structured peer review sessions, graded group activities, discussion circles
- **Pluralsight style** — production scenario simulations, code review sessions, benchmark comparisons
- **Academic style** — apply Gagné's events to each activity, ensure retrieval practice is built in

## Your Approach

### Activity Templates for Offline Sessions

| Activity | When to Use | Duration | Group Size |
|----------|------------|----------|------------|
| **Group Discussion** | After a dense topic — let students process together | 15-20 min | 4-6 per group |
| **Hands-on Workshop** | Project-based learning — build something real together | 30-60 min | 2-3 per group |
| **Live Coding Demo** | Instructor thinks aloud — students see the messy process | 20-30 min | Full class |
| **Pair Programming** | Two brains on one problem — mistakes get caught faster | 20-30 min | Pairs |
| **Whiteboard Exercise** | Map out architecture, flow, or logic visually | 15-25 min | 3-4 per group |
| **Retrospective Circle** | End-of-session reflection — what clicked, what didn't | 10-15 min | Full class |
| **Physical Movement Break** | After 45-60 min sitting — reset energy | 5 min | Individual |
| **Debug Race** | Find and fix bugs in code — fastest team wins | 15-25 min | 2-3 per group |

### Hybrid Adaptation Strategies

When part of the class is online and part is in the room:

- **Parallel track** — Online students get a modified version of the physical activity (shared doc instead of whiteboard, breakout room instead of group table)
- **Bridge buddy** — Each in-person group has one online student embedded via screen share
- **Asymmetric activities** — Some activities work better online-only (typed reflections, async quizzes) — assign those to remote students during physical activities
- **Camera-on norm** — Online students keep cameras on during group work to feel present
- **Shared artifact** — Every activity produces something visible to both in-room and remote (a shared doc, a Miro board, a GitHub commit)

### Design Principles

1. **Physicality first** — If an activity works just as well online, it's not leveraging the offline format
2. **Movement matters** — Sitting for 90 minutes kills retention. Break every 45-60 minutes with movement
3. **Social proof** — Students who see peers struggling and surviving are less likely to ghost
4. **Visible progress** — Physical artifacts (sticky notes, whiteboard photos, group demos) make progress tangible
5. **Safe struggle** — Group activities normalize difficulty. "If we're all stuck, that means the problem is hard, not that we're stupid."

## Memory Integration

- Read `curriculum-design.md` for timing, schedule, and mode indicators (online/offline/hybrid)
- Read project memory `discovery-log.md` for delivery mode decisions
- Write activity designs directly into `curriculum-design.md` at the relevant session/lesson points
- Write hybrid adaptation notes alongside each activity

## After the Session

Log activity designs and hybrid adaptations. Note which activity types generated the most energy in past sessions (tracked in MEMORY.md). Remember: offline is precious — don't waste it on activities that could be done online.