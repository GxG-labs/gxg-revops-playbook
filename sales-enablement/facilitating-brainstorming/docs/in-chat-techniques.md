# Choosing Techniques In Chat

Loaded only when the user won't use the composer page (no browser, or they declined). Pick the batch in conversation. **3–4 is the sweet spot.** Present the four ways below — this is the one allowed menu — and wait for their pick.

- **Facilitator Chosen (default)** — from the goal, name a batch of 3–4. Confirm exact names with a targeted `list --category` on only the categories you're drawing from; never enumerate the library to choose.
- **Browse** — direct them to open `sales-enablement/facilitating-brainstorming/assets/brain-selector.html` themselves; they tick techniques and paste the result back.
- **Category** — the user names 1–n categories; `BRAIN random --category <cat> -n 4` draws the batch from them.
- **Inventive Flow** — invent at least 3 brand-new techniques on the fly, announce the order before the first, touch no script. Log each one's name + description in the memlog.

The library is large — never pull it whole into context. BRAIN commands:

```bash
BRAIN categories                          # names + counts; the cheap survey
BRAIN list --category <cat>               # index (name + gist) for one category
BRAIN random --category <cat> -n 4       # draw a batch blind, listing nothing
BRAIN show "<name>"                       # full method — call only when it's about to run
BRAIN html --out <path>                   # regenerate composer page (e.g. after adding custom techniques)
```

`list` without `--category` or `--all` is refused — it's a footgun. Bare `list` dumps the catalog into context, which defeats lazy-loading.
