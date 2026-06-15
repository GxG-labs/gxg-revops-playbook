# GxG RevOps Playbook — Skill Lifecycle

The lifecycle governs how a skill moves from idea to production and, eventually, retirement. Every skill has a `status` field in its frontmatter that reflects its current lifecycle stage.

---

## Lifecycle Stages

```
[ idea ] → [ draft ] → [ review ] → [ active ] → [ deprecated ]
                           ↑                           ↓
                     [ needs-work ] ←──────────── [ archived ]
```

| Status | Description | Who can change to this |
|--------|-------------|----------------------|
| `draft` | Work in progress, not yet usable | Curator |
| `review` | Submitted for quality gate check | Curator |
| `needs-work` | Failed gates, returned with comments | Curator |
| `active` | Passes all gates, live in the playbook | Curator after G1–G7 pass |
| `deprecated` | Superseded or outdated, still readable | Curator |
| `archived` | Fully removed from active index | Curator |

---

## Stage: Create

### Trigger
User says: "new skill", "add skill", "scaffold", "write a skill for X", "create a RevOps skill"

### Steps

**Step 1 — Capture intent**
Ask (or infer from context):
- What problem does this skill solve?
- What triggers it? (what would a user type to invoke it?)
- What's the expected output?
- Is this Capability Uplift or Encoded Preference? (see taxonomy.md)

**Step 2 — Domain assignment**
Read `.skills/revops-curator/taxonomy.md` §Domains. Pick the primary folder. If ambiguous, ask the user.

**Step 3 — Generate slug**
Apply naming rules from taxonomy.md §Naming Conventions.
Present 2–3 options if not obvious. Let user confirm.

**Step 4 — Scaffold**
```bash
mkdir -p "{playbook-root}/{domain}/{slug}"
```
Copy `.skills/revops-curator/templates/new-skill.md` to `{playbook-root}/{domain}/{slug}/SKILL.md`.
Fill in frontmatter: name, domain, tags, status=draft, version=1.0.0, updated=today, author=GxG.

**Step 5 — Write description**
Apply the Description Optimizer from `.skills/revops-curator/index.md`. Draft 2–3 description options. Test each:
- Does it answer "what does it do"?
- Does it answer "when to use it"?
- Does it have ≥5 trigger keywords?
- Is it third-person, ≤1024 chars?

**Step 6 — Write body**
Structure:
1. One-sentence role statement
2. Quick reference table (if multiple workflows)
3. Instructions — numbered steps, imperative voice
4. Examples (≥2, concrete input → output)
5. Out of scope section

**Step 7 — Gate check**
Run G1–G7 from `.skills/revops-curator/index.md`. Document score. If ≥5/7, set status → `active`. If <5/7, set status → `needs-work` with inline comments.

**Step 8 — Index update**
Add to `INDEX.md` under the correct domain section.

**Step 9 — README freshness check** ← run automatically after every create
Run §README Freshness Check below. If stale — offer to update immediately.

---

## Stage: Audit

### Trigger
User says: "audit", "health check", "quality score", "review skills", "how's the playbook"

### Audit Script
Run `python .skills/revops-curator/scripts/audit.py` or manually:

```bash
# Find all skills
find "{playbook-root}" -name "SKILL.md" -not -path "*/.agents/*" -not -path "*/.claude/*" -not -path "*/.skills/*"
```

For each skill found:
1. Read frontmatter (name, description, status, tags, updated, version)
2. Score G1–G7 (1 point each):
   - G1: name matches kebab-case verb+noun pattern?
   - G2: description has USE WHEN + ≥5 keywords + ≤1024 chars + third-person?
   - G3: SKILL.md ≤500 lines?
   - G4: ≥2 concrete examples?
   - G5: "Out of scope" section present?
   - G6: domain + tags in frontmatter?
   - G7: uses required frontmatter fields (status, version, updated, author)?
3. Flag critical issues (score ≤2)
4. Note last-updated date (stale = >90 days without update — see `.skills/config.yaml` `settings.stale_threshold_days`)

Output using `.skills/revops-curator/templates/audit-report.md`.

### Audit Frequency
Run a full audit:
- When adding more than 3 skills at once
- Before sharing the playbook externally
- Monthly during active development
- Quarterly in steady state

---

## Stage: Improve

### Trigger
User says: "improve skill X", "fix description", "optimize trigger", "strengthen", "update skill"

### Steps

**Step 1 — Diagnose**
Read the target SKILL.md. Run G1–G7 gate check. Identify lowest-scoring gates.

**Step 2 — Prioritize fixes**
Order of impact:
1. G2 (description) — highest impact on activation
2. G4 (examples) — second highest
3. G1 (name) — if slug is wrong
4. G3, G5, G6, G7 — structural completeness

**Step 3 — Description improvement**
Apply Description Optimizer. Present old vs. new description side-by-side. Explain what changed and why.

**Step 4 — Example improvement**
If examples are weak:
- Make them concrete (specific inputs, specific outputs)
- Show the most common use cases first
- Add an edge case example if domain knowledge warrants it

**Step 5 — Structural improvement**
- Split long SKILL.md into SKILL.md + docs/ files
- Add a quick-reference routing table if there are multiple workflows
- Ensure out-of-scope section is specific, not generic

**Step 6 — Bump version + update date**
Patch version (1.0.0 → 1.0.1) for content fixes.
Minor version (1.0.x → 1.1.0) for structural changes.
Major version (1.x.x → 2.0.0) for complete rewrites.

**Step 7 — Update INDEX.md**
Refresh the description excerpt in the index row.

---

## Stage: Deprecate

### Trigger
User says: "retire skill X", "deprecate", "this skill is outdated", "superseded by Y"

### When to deprecate
- A newer skill covers the same ground with better structure
- The underlying process/tool no longer exists at GxG
- The skill hasn't been updated in >6 months AND has score <4/7
- Two skills with significant overlap — deprecate the weaker one

### Steps

1. **Set status** → `deprecated` in frontmatter
2. **Add deprecation notice** at the top of SKILL.md:
   ```markdown
   > ⚠️ **Deprecated** as of YYYY-MM-DD.
   > Reason: [why deprecated]
   > Superseded by: [{skill-name}]({path}) (if applicable)
   ```
3. **Remove from active sections of INDEX.md** — move to a `## Deprecated` section at the bottom
4. **Do NOT delete the file** — keep for historical reference
5. **README freshness check** ← automatically after deprecate
   Run §README Freshness Check — active count changed, badges may be stale.

### Archive (full removal)
Only archive (physically move to an `_archived/` folder) if:
- The skill has been deprecated for >12 months AND
- No other skill references it

---

## Version Management

Each skill uses semantic versioning in its frontmatter:

| Change type | Version bump | Examples |
|-------------|-------------|---------|
| Typo, wording | Patch `x.x.+1` | Fix a typo in examples |
| Content update | Minor `x.+1.0` | New example, improved description, new section |
| Structural rewrite | Major `+1.0.0` | New file structure, domain reassignment, full rewrite |

Track version history in a `## Changelog` section at the bottom of SKILL.md (optional, required for major versions).

---

## Staleness Rules

A skill is considered **stale** if:
- `status: active` AND `updated` date > 90 days ago (see `.skills/config.yaml` `settings.stale_threshold_days`) AND
- The underlying process or tool has changed

Stale skills surface in the audit report with a ⏰ flag. The recommended action is Improve (bump updated date + re-verify accuracy) or Deprecate.

---

## README Freshness Check

Run automatically at the end of: Create (step 9), Improve (if status → active), Deprecate (step 5), Promote from staging.

### Algorithm

1. Read `README.md` at the playbook root
2. Find the skills badge: `![Skills](https://img.shields.io/badge/skills-{N}%20active-...)`
   Extract N (the number before `%20active`)
3. Find the coverage badge: `![Coverage](https://img.shields.io/badge/coverage-{PCT}%25-...)`
   Extract PCT
4. Count actual data: number of `SKILL.md` files with `status: active` (excluding `.agents/`, `.claude/`, and `.skills/`)
5. Calculate actual coverage: `active / 51 * 100` (total target from `.skills/config.yaml`)

### Decision

| Situation | Action |
|-----------|--------|
| badge_count == actual_count AND badge_pct ≈ actual_pct | README is current — do nothing, say nothing |
| badge_count != actual_count | README is stale → offer to update |
| coverage color doesn't match thresholds | README is stale → offer to update |

### How to propose the update

One line, postscript to the main response:

> README is stale (was {OLD_N} skills → now {NEW_N}). Update now? (`yes` / `later`)

If the user says `yes` or `update` → run Update README workflow from [readme-workflows.md](readme-workflows.md).
If `later` or no response → don't repeat in this session.

**Don't interrupt the main workflow** for README. This check is a postscript, not a blocker.

## Contributing Standards (for the CONTRIBUTING.md file)

When creating CONTRIBUTING.md at the playbook root, include these rules:

1. All PRs/additions must use the skill template
2. Description must pass the Description Optimizer test
3. Every skill must have a domain assignment before merging
4. Status must be `draft` on first submission — only the curator promotes to `active`
5. Breaking changes (major version bumps) require a one-line summary in the commit message
6. No skill should duplicate functionality of an existing `active` skill — check the index first
