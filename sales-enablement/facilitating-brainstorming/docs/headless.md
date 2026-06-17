# Headless Mode

Load this file ONLY when `facilitating-brainstorming` is invoked headless. It is quarantined here on purpose: headless is the single context in which you generate ideas yourself, which is the exact inverse of the interactive stance. Loading it in a normal session would corrupt the facilitation.

## Detection

**If a human is sending messages in this session, you are interactive — no payload shape or phrasing overrides that.** Headless requires the *absence* of an interactive user. It is in effect only when one of these unambiguous machine signals holds:

- the caller sets a `headless: true` flag (or the equivalent argument the harness exposes),
- the invocation comes from another skill or a non-interactive runner (no TTY, no user message stream),
- the activation instructions explicitly declare headless.

When in doubt, you are interactive — a present human asking you to "brainstorm X and give me the HTML" is a normal interactive opening, not a headless trigger.

## The inversion

There is no user to draw ideas out of, so you become the brainstormer. Run a real divergent session against the supplied topic:

```bash
python3 sales-enablement/facilitating-brainstorming/scripts/brain.py list --all
```

Use the whole catalog (fine here — you are generating, not pacing a user). Prefer techniques that fit the goal, and **shift the creative domain every ~10 ideas** — technical, then experiential, then business, then failure modes, then wildcards. Push past the obvious. Aim past 100. The same anti-clustering discipline applies.

## Inputs the caller is expected to provide

Free-form structured payload in the first message:

- `topic` — what to brainstorm. Required. If absent and uninferable, halt with `"status": "blocked"`.
- `goal` — desired outcome / framing, if any.
- `techniques` — specific methods to use; otherwise you choose fitting ones.
- `context` — file paths or text to ground the session.
- `doc_workspace` — a specific run folder; otherwise use `_output/brainstorming/brainstorm-{topic_slug}-{date}/`.
- `artifacts` — which outputs to produce: `html`, `intent`, or both. Default: both.

## Run

1. Bind `{doc_workspace}` and create the memlog:
   ```bash
   python3 sales-enablement/facilitating-brainstorming/scripts/memlog.py init \
     --workspace {doc_workspace} \
     --field topic="<topic>" \
     --field goal="<goal>"
   ```

2. Run the divergent session, capturing each idea:
   ```bash
   python3 sales-enablement/facilitating-brainstorming/scripts/memlog.py append \
     --workspace {doc_workspace} --type idea --text "<idea>"
   ```
   Mark each technique switch:
   ```bash
   python3 sales-enablement/facilitating-brainstorming/scripts/memlog.py append \
     --workspace {doc_workspace} --type technique --text "started <name>"
   ```

3. Synthesize: surface conclusions and key directions. Record as `--type insight`. Then:
   ```bash
   python3 sales-enablement/facilitating-brainstorming/scripts/memlog.py set \
     --workspace {doc_workspace} --key status --value complete
   ```

4. Produce requested artifacts from the log — `brainstorm.html` and/or `brainstorm-intent.md` — as described in `docs/finalize.md`, delegating each to a subagent that reads the log as its sole source.

5. No questions, no greetings. Record any inferred assumptions in `assumptions[]`.

## Return

End with a JSON status block:

```json
{
  "status": "complete",
  "intent": "brainstorm",
  "memlog": "{doc_workspace}/.memlog.md",
  "html": "{doc_workspace}/brainstorm.html",
  "intent_doc": "{doc_workspace}/brainstorm-intent.md",
  "assumptions": [],
  "external_handoffs": []
}
```

Use `partial` when artifacts were produced but key inputs were inferred; `blocked` when no artifact was produced.
