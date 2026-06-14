# Curator — Staging Workflows

Detailed instructions for working with the staging area (`_staging/`).
`index.md` routes here for staging-related requests.

---

## When to use staging

**Add to staging when:**
- There's useful domain knowledge, but no time to build a full skill right now
- The knowledge is incomplete — needs more examples or context
- It's unclear which domain this belongs to
- Source is raw notes (meeting, document, conversation) that need processing

**Don't add to staging:**
- Links to external resources without GxG-specific context
- Widely known RevOps concepts without GxG-specific application
- Duplicates of existing active skills

---

## Scan Staging

**Trigger:** "scan staging", "что в staging", "staging status"

1. Find all `.md` files in `_staging/` except `README.md` and `_template.md`
2. Read each frontmatter: `title`, `domain`, `status`, `skill_candidate`, `added`
3. Calculate `days_in_staging = today - added`
4. Assess readiness for skill (0–3):
   - +1 if `skill_candidate: yes`
   - +1 if "Knowledge" section > 100 words
   - +1 if "Open Questions" are empty or marked as resolved
5. Output table:

```
| Note | Domain | Status | Days | Readiness | Action |
|------|--------|--------|------|-----------|--------|
| {title} | {domain} | {status} | {n} | {0-3}★ | {promote|refine|park|review} |
```

Warning flags (thresholds from `.skills/config.yaml`):
- ⏰ `ready` > 30 days → "time to promote"
- 🗑️  `parked` > 90 days → "reconsider or delete"
- 📝 `raw` > 14 days without changes → "needs refining"

---

## Refine Note

**Trigger:** "refine {note}", "help me structure {note}", "доработай заметку {note}"

Goal: turn `raw` → `refining` → `ready`

1. Read the note
2. Determine:
   - Is the domain correct?
   - Are there concrete examples (G4 requirement)?
   - Are there open questions blocking the skill?
3. Suggest structure for the "Knowledge" section:
   - Main workflow / process
   - GxG-specific parameters (thresholds, criteria, decisions)
   - Examples (at least 2)
4. Ask clarifying questions about open questions
5. Update `status: refining` and add notes to "Curator Notes" section
6. If ready after refining → offer to promote

---

## Promote Note to Skill

**Trigger:** "promote {note}", "make skill from {note}", "promote {slug} to skill"

1. Read the staging note
2. Check readiness:
   - Is there a concrete workflow/process?
   - Are there ≥2 examples (or can they be extracted from knowledge)?
   - No blocking open questions?
   - If not → offer to refine first
3. Determine `domain` and `slug` (use `skill_candidate_slug` from frontmatter or suggest one)
4. Scaffold the skill from `.skills/revops-curator/templates/new-skill.md` using knowledge from the note:
   - Description from "Context" + Description Optimizer
   - Instructions from "Knowledge"
   - Examples from examples in the note or created from knowledge
   - Out of scope from "Open Questions" (what we don't know = out of scope for now)
5. Run G1–G7 gate check
6. Save skill to `{domain}/{slug}/SKILL.md` with status `draft`
7. Update the staging note: add `promoted_to: {domain}/{slug}` and `status: promoted` to frontmatter
8. Update INDEX.md
9. **README freshness check** ← automatically after promote
   Skill became active — run §README Freshness Check from lifecycle.md.

---

## Park Note

**Trigger:** "park {note}", "not ready yet {note}", "запаркуй {note}"

1. Update `status: parked` in frontmatter
2. Add to "Curator Notes":
   ```
   Parked: {date}
   Reason: {why not turning into a skill now}
   Return trigger: {what needs to change to revisit this}
   ```
3. Don't delete — leave in `_staging/`

---

## Add to Staging

**Trigger:** "add to staging", "save to staging", "добавь в базу знаний"

1. Clarify:
   - Domain (or suggest one)
   - Source (meeting-notes / doc / conversation / research)
   - `skill_candidate`: yes / no / maybe
2. Suggest a slug based on the content
3. Create `_staging/{slug}.md` from `_staging/_template.md`
4. Fill in knowledge from the provided content
5. Set `status: raw`
6. Report: "Added to staging. Run scan staging to see the full picture."

---

## Staging Health Rules

Thresholds come from `.skills/config.yaml` `settings.*_warning_days`.

| Rule | Action |
|------|--------|
| `ready` > 30 days | Remind about promote on next scan |
| `parked` > 90 days | Offer to delete or reconsider |
| `raw` > 14 days | Offer to refine or park |
| >20 notes in staging | Warning — staging full, needs cleanup |
| >5 `ready` notes | Urgent: lots of ready knowledge without skills |
