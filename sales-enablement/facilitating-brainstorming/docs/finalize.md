# Wrap-Up: Synthesis & Artifacts

Load this when the user signals they're spent or the topic is mined out. `{doc_workspace}/.memlog.md` is the canonical record — everything derives from it.

## Synthesis

In Facilitator mode this is the one place your own creative contribution is welcome; in Creative Partner and Ideate-for-me you've been contributing all along.

1. **Hand them the mirror first.** Reflect a vivid sampling of *their* ideas back — deliberately include the odd and buried ones, not just the recent obvious ones (in Creative Partner mode the `(... by user)` tags tell you which were theirs). Ask what they see now: conclusions, synergies, themes. Let them connect first.
2. **Then add the connections they would miss.** Non-obvious links: this idea from technique one quietly solves that tension from technique four; these three are one idea wearing three hats.

Record insights and chosen directions:
```bash
MEMLOG append --workspace {doc_workspace} --type insight --text "<one-line gist>"
```

Then mark the session complete:
```bash
MEMLOG set --workspace {doc_workspace} --key status --value complete
```

Do this even if the user declines every artifact below.

## Artifacts

In **Ideate for me**, the imaginative HTML keepsake is the deliverable you promised — produce it automatically, no asking. In **Facilitator** and **Creative Partner**, every artifact is opt-in.

**Delegate each artifact to a subagent.** The memlog holds everything, so the subagent needs only: the spec below, the memlog path `{doc_workspace}/.memlog.md` (read it in full), the output path, and "return ONLY the written file path."

- **Imaginative HTML keepsake (recommended default).** A single self-contained `brainstorm.html` in `{doc_workspace}`. No template — let the session's subject, energy, and whimsy drive the visual language. Give each technique its own treatment, render synthesis as the climax. Inline all CSS/JS; no external dependencies. Open once complete.
- **Intent doc.** A succinct `brainstorm-intent.md` — chosen and critical discoveries only, structured to drop into a downstream RevOps skill as clean input.
- **Other options based on context** — a pitch, a one-pager, a task list; ask the user, be creative.

After producing artifacts: share paths, offer ideas for follow-up brainstorming sessions, and suggest which GxG RevOps skills the intent doc could feed into next (e.g. `writing-business-cases`, `building-battlecards`).
