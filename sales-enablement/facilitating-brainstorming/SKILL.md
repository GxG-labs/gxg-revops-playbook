---
name: facilitating-brainstorming
description: Facilitates structured brainstorming and ideation sessions using 108 creative techniques across Facilitator, Creative Partner, and Ideate-for-me modes. Use when planning a GTM strategy, generating sales plays, ideating campaign angles, solving RevOps design challenges, getting unstuck on a problem, or when user mentions "brainstorm", "ideate", "generate ideas", "creative session", "workshop", "what if we", "помозгуем", "давай покреативим".
status: active
domain: sales-enablement
type: capability-uplift
tags: [sales-enablement, demand-gen, #framework, #playbook, #process, #p2]
version: 1.0.0
updated: 2026-06-17
author: GxG
allowed-tools: Read, Write, Bash, Glob
---

# Facilitating Brainstorming

Runs a structured ideation session — someone brings a topic and leaves with far more ideas than they could generate alone, pushed past the obvious by sharper questions, harder constraints, and a shifting lens every 5–10 turns.

## Path Constants

```
SKILL_DIR  = sales-enablement/facilitating-brainstorming
BRAIN      = python3 sales-enablement/facilitating-brainstorming/scripts/brain.py
MEMLOG     = python3 sales-enablement/facilitating-brainstorming/scripts/memlog.py
SESSION_DIR = _output/brainstorming/brainstorm-{topic_slug}-{date}
```

`{topic_slug}` is a kebab-case slug derived from the session topic.
`{date}` is today's date in YYYY-MM-DD format, determined at session start.
`{doc_workspace}` = SESSION_DIR — used throughout docs/ files.

## When to Use This Skill

Activate when:
- User wants to brainstorm GTM strategy, sales plays, ICP angles, campaign concepts, or messaging
- User is stuck and needs to break out of existing thinking patterns
- Team needs structured creative facilitation for a RevOps design decision
- User explicitly asks to "brainstorm", "ideate", "generate ideas", or "workshop" a topic

Do NOT use when: user wants to execute a known workflow (e.g. "build me a battlecard") — use the appropriate execution skill instead. Brainstorming is for generating options, not producing deliverables.

---

## Facilitation Modes

| Mode | What it means | Read |
|------|--------------|------|
| **Facilitator** | Agent never supplies ideas — questions and constraints only | `docs/mode-facilitator.md` |
| **Creative Partner** | Agent facilitates AND plays, trading ideas collaboratively | `docs/mode-partner.md` |
| **Ideate for me** | Agent runs the whole session autonomously, then shows the result | `docs/mode-autonomous.md` |

---

## Framing — hold for the whole run

- **Aim past 100 ideas; resist concluding.** The urge to organize is the enemy of divergence — push for one more until the topic is mined out.
- **Keep shifting the creative domain** — every 5–10 turns, move to the next technique.
- **One prompt per message in dialogue modes; no multiple-choice menus.** The only allowed menus are the two up-front process choices (mode, and technique batch).

---

## On Activation

1. Glob `_output/brainstorming/*/.memlog.md`, read each frontmatter, and offer to resume any with `status` not `complete` (→ `docs/resume.md`) or start fresh (→ `## Run a Session`).
2. If launched headless (machine-triggered, no interactive user): load `docs/headless.md` and follow it for the whole run.

---

## The Memlog

The session's memory — the single source every artifact derives from. Every idea, decision, question, and direction goes in; prompts and small talk stay out. All writes are atomic:

```bash
# Create once (after topic + goal + mode are known):
MEMLOG init --workspace {doc_workspace} --field topic="<topic>" --field goal="<goal>" --field mode="<facilitator|partner|autonomous>"

# Log one entry:
MEMLOG append --workspace {doc_workspace} --type <idea|insight|question|decision|direction|technique> --text "<one-line gist>"
# In Creative Partner mode add: --by user  OR  --by coach

# Mark complete at wrap-up:
MEMLOG set --workspace {doc_workspace} --key status --value complete
```

Never read the memlog back mid-session — the one exception is resume.

---

## Run a Session

1. **Open** with one compound question: what are we brainstorming, and what's the goal behind it? (If already clear, confirm and move on.) Derive `{topic_slug}` and set `{doc_workspace} = SESSION_DIR`.

2. **Choose mode + technique batch together** — the composer page (`SKILL_DIR/assets/brain-selector.html`) does both:
   - Try `open SKILL_DIR/assets/brain-selector.html` (or `xdg-open` / `start` on Linux/Windows).
   - Tell the user: *"It should open in your browser — compose your session, click Copy prompt, and paste it back. If it didn't open, open the file yourself, or say 'let's do it in chat'."*
   - Parse the pasted block: `Facilitation mode:` line → mode; listed techniques → run them as given.
   - If they can't open the page: load `docs/in-chat-techniques.md` and pick the batch in chat (3–4 techniques is the sweet spot).

3. **Create the memlog** (`MEMLOG init …`) and load the mode frame (see routing table above). Tell the user the memlog path.

4. **Run each technique** until it stops producing. Log each idea as it lands and the technique switch itself. When the batch is spent, offer three paths: another batch / converge (`docs/converge.md`) / wrap up (`docs/finalize.md`).

---

## Choosing Techniques

Read `docs/in-chat-techniques.md` when the user skips the composer page. Key commands:

```bash
BRAIN categories                          # cheap survey — names + counts
BRAIN list --category <cat>               # index (name + gist) for one category
BRAIN random --category <cat> -n 4       # draw a batch blind
BRAIN show "<technique name>"             # full method (call only when it's about to run)
```

Never pull the full library into context. `list` without `--category` is refused by the script.

---

## Converging

When the user is ready to narrow and decide, load `docs/converge.md` and follow it. Convergence is a separate phase — never fold it into a generating batch.

## Resuming

Load `docs/resume.md`.

## Wrap-Up

Load `docs/finalize.md` (after converging or when the topic is mined out).

---

## Examples

### Example 1: GTM strategy ideation for a new RevOps product segment

**Input:** "Help me brainstorm how we could position our product for mid-market CFOs. We're losing deals to spreadsheets."

**Output:** Agent opens with "What's the goal — are we generating messaging angles, identifying blockers, or both?" Launches in Creative Partner mode. Runs SCAMPER on the current pitch, then Assumption Reversal on "CFOs prefer spreadsheets," then Laddering to surface the real anxiety (control + visibility). Memlog captures 35+ ideas. Synthesis surfaces 3 positioning themes. Produces `brainstorm.html` keepsake + `brainstorm-intent.md` ready to hand off to a positioning skill.

---

### Example 2: Unstuck — pipeline review process overhaul

**Input:** "Our pipeline reviews aren't working. Reps game the forecast, managers don't trust the data. Brainstorm what we could change."

**Output:** Agent chooses Facilitator mode (user does the thinking). Runs Five Whys to surface the root trust gap, then Reverse Brainstorming ("how would we make this worse?") to invert into fixes, then Constraint Roulette. 40+ ideas generated by user. Converge phase clusters into 3 structural changes + 2 quick wins. Intent doc written for `auditing-crm-data` skill handoff.

---

## Out of Scope

This skill does NOT:
- Produce final RevOps deliverables — it generates ideas; execution goes to domain-specific skills
- Replace structured analysis (attribution modeling, quota setting) — use `rev-analytics` / `territory-quota` skills
- Access live CRM/pipeline data — all brainstorming is ideas-only, no data queries
- Modify the technique library (`assets/brain-methods.csv`) — editing the catalog is a separate curation task

---

## Reference

- Technique library: `SKILL_DIR/assets/brain-methods.csv` (108 techniques, 13 categories)
- Technique selector: `SKILL_DIR/assets/brain-selector.html` (offline, self-contained)
- Library CLI: `SKILL_DIR/scripts/brain.py` (`--help` for full command reference)
- Session logger: `SKILL_DIR/scripts/memlog.py`
- Mode docs: `SKILL_DIR/docs/mode-{facilitator,partner,autonomous}.md`
- Phase docs: `SKILL_DIR/docs/{converge,finalize,resume,headless}.md`

---

## Import Notes

- Source: `https://github.com/bmad-code-org/BMAD-METHOD/tree/main/src/core-skills/bmad-brainstorming`
- Adapted: 2026-06-17
- Changes: stripped BMad runtime (`resolve_customization.py`, `customize.toml` variables, `_bmad/core/config.yaml`); replaced `{skill-root}` and `{workflow.*}` with concrete GxG paths; removed BMad cross-skill references (`bmad-party-mode`, `bmad-advanced-elicitation`, `bmad-help`, `bmad-customize`); renamed `references/` → `docs/`; added GxG frontmatter, RevOps examples, and Out of Scope; scripts and assets copied unchanged (pure Python, no vendor dependencies).

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-17 | Onboarded from BMad Method; adapted to GxG format |
