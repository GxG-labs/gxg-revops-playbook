# Converging: Narrow & Decide

Load this when divergence is spent and the user wants to narrow the field — or asks to "decide," "prioritize," "pick," or "make it real." The catalog is *divergent* by design; this is the deliberate opposite phase. Never run convergence while ideas are still flowing.

`{doc_workspace}/.memlog.md` is the canonical record; everything here works from it.

**Mode holds.** In Facilitator you run convergence *on the user's verdicts* — you structure and prompt, they judge. In Creative Partner you weigh in too, each call logged by author. In Ideate for me you converge yourself and show the result.

## How to run it

First, reflect the field back: pull live candidates from the memlog (include odd and buried ones, not just the recent obvious ones). Then pick **one** convergence move that fits the goal — don't hand a menu; choose the one that suits *this* decision and name it. Run it to a result, log the outcome, and stop when a clear short-list emerges.

Pick by what the decision needs:

- **Affinity Clustering** — when there are many scattered ideas: group into themes, name each cluster, surface the through-line.
- **Impact–Effort** — when the goal is action: place each candidate on impact vs effort; harvest high-impact/low-effort first.
- **NUF Test** — when novelty matters: score each New, Useful, Feasible (1–10); totals expose quiet winners and dazzling-but-doomed.
- **Forced Ranking / Dot Vote** — when you need a ranked top-N: make ideas compete, no ties.
- **PMI (Plus / Minus / Interesting)** — when one strong candidate needs pressure-testing before commitment.
- **MoSCoW** — when scoping a build: Must / Should / Could / Won't-this-time.

Log surviving directions with:
```bash
MEMLOG append --workspace {doc_workspace} --type decision --text "<one-line gist>"
```

Two or three convergence moves chained is fine; more is usually over-processing.

## Then finalize

Once a short-list is settled, load `docs/finalize.md` — synthesis, `status: complete`, and artifacts. Do not set `status: complete` here; that belongs to finalize.
