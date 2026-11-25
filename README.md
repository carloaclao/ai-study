# ai-study

Self-study from the math up to CUDA: linear algebra, deep learning, LLMs from scratch, agents, and GPU kernels. About 13 hours a week, from November 2026 to August 2027.

## What's in here

| Path | What it is | How often you open it |
|---|---|---|
| [STUDY_SCHEDULE.md](STUDY_SCHEDULE.md) | **What to do today.** Every day, with a checkbox, plus a Reinforce block each week | Every session |
| [AI_ROADMAP.md](AI_ROADMAP.md) | **Why, and what else to read.** The full syllabus, all links, and the study method | When you want context or extra depth |
| `notes/` | One file per week: what you learned, Reinforce answers, what you missed | Every session |
| `phase-*/` | Your code for each phase: labs, builds, projects | Weekends, mostly |

The schedule is the plan you follow; the roadmap is the reference it is built from. You never need to read the roadmap start to finish.

## A normal week

**Weekday (1 hour)**

1. Open `STUDY_SCHEDULE.md` and find today's checkbox.
2. On Monday, spend the first 10 minutes redoing whatever you got wrong in last week's Reinforce (it's listed at the bottom of last week's note).
3. Do the day's material. Before watching or reading an explanation, try to predict where it is going.
4. Spend the last 5 minutes writing 2 or 3 *claims* in this week's note: a one-line statement plus why it is true. For example: "Matrix-vector multiplication is a linear combination of the columns, because each column is where a basis vector lands."
5. Tick the box and commit.

**Weeks 1 to 4 are different:** weekends become mostly an agents side track while weekdays stay on math. The layout is at the top of the schedule.

**Saturday (4 hours):** build. Code along if the schedule says so, then close the reference and write it again yourself in the matching `phase-*` folder.

**Sunday (4 hours):** about 3 hours finishing the build, then the 1-hour **Reinforce** block:

1. Do every Reinforce task closed-book, writing your answers in the week's note.
2. Check them: math in NumPy, explanations by asking a model (or a LearnHarness Practice session) to grade your answer and point out the gap.
3. Copy anything you got wrong into the note's "Misses" list. That list is Monday's warm-up.

Never skip Reinforce to catch up. Cut new material instead.

## Falling behind

- Lost a weekday: fold it into the weekend.
- Lost a weekend: slide that week, and the rest of the schedule moves with it.
- Weeks 18 and 36 are buffers. Use them to catch up or move them around travel and busy stretches at work.
- The dates in the schedule are a guide. The order is what matters.

## Commands

```bash
# Start a week's note
cp notes/_template.md notes/week-01.md

# Check your environment (kickoff weekend)
uv run phase-0-setup/check_env.py

# End of each session
git add -A && git commit -m "week 1: chapter 4, composition" && git push
```

## Setup

Done once, on the kickoff weekend. See [phase-0-setup/README.md](phase-0-setup/README.md).
