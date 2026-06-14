# Curator — README Workflows

Creating and updating README.md for the GxG RevOps Playbook repository.
Based on analysis of 500+ top GitHub repositories (awesome-readme, 20k+ ⭐).

---

## Two types of README in this repo

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` (root) | Main repo page — what this is, why, how to start | New contributors, RevOps team |
| `{domain}/README.md` | Domain overview — what's inside, coverage, metrics | Those working with a specific domain |

This module covers both types. Different templates — see below.

---

## When to update README

| Trigger | What to update |
|---------|----------------|
| New skill added | Badges (skill counter), Coverage table in root README |
| Folder structure changed | Structure section |
| New domain added | Domains table, Structure |
| Coverage target reached | Badges, Coverage table |
| Workflow changed (how to contribute) | Quick Start, Contributing |
| Domain renamed | All domain links throughout README |
| Quarterly (routine) | Badges, Coverage, "What's New" |

---

## Create: root README.md

**Trigger:** "create README", "write README for repo", "readme for playbook"

### README anatomy for a knowledge/playbook repo

Section order is strict. Each section is justified by data from top repositories.

```
1. Banner/Logo              ← first impression, 42% more stars with visuals
2. Badges                   ← instant trust signals (4-7 max)
3. One-liner                ← ≤10 words, what this is
4. Why (value prop)         ← 3-5 bullets: what problems it solves
5. Quick Start              ← how to use in ≤3 steps
6. What's Inside            ← domains + coverage map
7. Skill count / Stats      ← progress and momentum
8. How to Use               ← how to invoke skills
9. How to Contribute        ← CONTRIBUTING link + 4 steps
10. Structure               ← folder tree
11. License / Credits       ← if needed
```

### Writing rules

**First screen (above the fold)** — contains badges + one-liner + why. Reader decides "interesting / not" in 5 seconds.

**Language** — active voice, imperative. "Run `/skill-name`", not "Skills can be run by..."

**Length** — for knowledge repos, optimal is 400–900 words. Details go in domain READMEs.

**Links** — all relative (`./pipeline/README.md`), not absolute URLs.

**Tables** — for coverage map and structure. Not for regular text.

**Emoji** — sparingly, only as visual anchors in headers or bullets (not in body text).

### Badges for knowledge repos

Standard code badges (build, npm) don't fit. Use content badges:

```markdown
![Skills](https://img.shields.io/badge/skills-{N}%20active-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-{N}%25-{color})
![Domains](https://img.shields.io/badge/domains-10-blue)
![Updated](https://img.shields.io/badge/updated-{month}%20{year}-lightgrey)
```

Color logic for coverage badge:
- ≥80% → `brightgreen`
- 60–79% → `yellow`
- 40–59% → `orange`
- <40% → `red`

Maximum 5 badges. More = noise.

---

## Create: domain README.md

**Trigger:** "write README for domain X", "update readme pipeline"

### Domain README structure

```
1. Domain name + scope (1 paragraph)
2. Coverage map (table: skill | status | description)
3. Key metrics (3-5 most important KPIs for this domain)
4. Stack references (GxG tools in this domain)
5. Coverage targets
6. Notes (GxG-specific context)
```

Shorter than root README — focus on navigation within the domain.

---

## Update: updating an existing README

**Trigger:** "update README", "actualize readme", "обнови readme"

### Steps

1. Read the current README
2. Run audit (`python .skills/revops-curator/scripts/audit.py`) to get current numbers
3. Identify what's outdated:
   - Skill counter in badges
   - Coverage table
   - Folder structure
   - Links (any broken?)
4. Update only what changed — don't rewrite the whole document
5. Report what changed (diff summary)

### Common updates

**Badges** — update whenever a skill is added:
```
Was: ![Skills](https://img.shields.io/badge/skills-3%20active-red)
Now: ![Skills](https://img.shields.io/badge/skills-7%20active-orange)
```

**Coverage table** — take numbers from audit.py, not manually.

**"What's New" section** (if present) — rotate: keep last 3 events, rest goes to CHANGELOG.

---

## README Quality Score

10-point scale (adapted for knowledge repos):

| # | Criterion | Score |
|---|----------|-------|
| 1 | 4–5 content badges (skills count, coverage, domains, updated) | /1 |
| 2 | One-liner ≤10 words describes the essence | /1 |
| 3 | Visual element (banner, architecture diagram, coverage table) | /1 |
| 4 | Quick Start — how to begin in ≤3 steps | /1 |
| 5 | Domains table with coverage % and links | /1 |
| 6 | Concrete example of using a skill | /1 |
| 7 | Link to CONTRIBUTING.md + brief steps | /1 |
| 8 | Folder structure is current | /1 |
| 9 | No broken links | /1 |
| 10 | Written for a newcomer (no context required) | /1 |

**8–10** → Excellent ✅ | **6–7** → Good ⚠️ | **<6** → Needs work 🔧

---

## Anti-patterns (from analysis of real repos)

| Anti-pattern | Why it's bad | How to fix |
|-------------|-------------|------------|
| Wall of text without structure | Reader leaves in 3 sec | Add headers, bullets, tables |
| Outdated numbers in badges | Undermines trust | Auto-generate from audit.py |
| "This repo contains..." as first line | Weak opener, doesn't describe value | Start with benefit, not description |
| TOC without anchor links | Navigation doesn't work | Verify all `#` anchors exist |
| Folder structure maintained manually | Goes stale quickly | Generate from `tree` when updating |
| Contributing in 1 line | Discourages contributors | Minimum 4 steps + link to CONTRIBUTING.md |
| README as only documentation | Too long | README = hub, details in domain README |

---

## Example: root README.md for GxG RevOps Playbook

Use `.skills/revops-curator/templates/repo-readme.md` as a base. Steps:

1. Read `.skills/revops-curator/templates/repo-readme.md`
2. Run audit.py, get current numbers
3. Fill in `{placeholders}` with real data
4. Save as `README.md` at the repo root
5. Run README Quality Score — should be ≥8/10

---

## Out of Scope

This module does NOT:
- Create READMEs for individual skills (those have SKILL.md, not README)
- Generate GitHub Pages or a documentation site
- Manage CHANGELOG.md (that's a separate workflow)
