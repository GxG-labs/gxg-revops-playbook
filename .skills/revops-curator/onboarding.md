# Curator - External Skill Onboarding

Use this workflow when the user provides a link to a skill, pastes a `SKILL.md`, drops a local file, or asks to bring an external skill into the GxG RevOps Playbook.

The goal is not to copy the source skill. The goal is to extract the reusable operating pattern, remove vendor- or assistant-specific assumptions, and publish a clean playbook skill that fits this repository's taxonomy, format, and quality gates.

---

## Triggers

Use this workflow when the user says:
- "onboard this skill"
- "import this skill"
- "adapt this skill"
- "bring this into the playbook"
- "convert this skill to our format"
- "normalize this skill"
- "причеши скилл"
- "добавь этот скилл"
- "адаптируй skill"
- "вот ссылка на skill"
- "вот файл скилла"

---

## Inputs

The user can provide any of:

| Input | How to handle it |
|-------|------------------|
| URL to a skill | Fetch/read the source, then capture source metadata in the import notes. |
| Local file path | Read the file directly. If it is outside the repo, treat it as an external source. |
| Pasted skill body | Treat the conversation as the source and preserve only the derived playbook skill in files. |
| Folder/repo with a skill | Identify the actual entry point first, usually `SKILL.md` or equivalent. |

If a source cannot be accessed, ask the user to paste the file or place it in `workbench/input/` if that folder exists. Do not invent missing source details.

---

## Project-Template Alignment

Follow the organization model from `/Users/dk1/go/_template project`: separate intent, sources, working analysis, reusable instructions, and final deliverables.

In this repository, apply that model as:

| Lifecycle role | Location in this playbook |
|----------------|---------------------------|
| User intent | The current request, or `briefs/` if the repo later adopts that folder. |
| Temporary source files | `workbench/input/` if it exists; otherwise read the provided path directly without creating permanent source folders. |
| Working analysis | Keep in the session unless it needs to become a staging note. |
| Incomplete reusable knowledge | `_staging/{slug}.md`. |
| Production reusable instruction | `{domain}/{slug}/SKILL.md`. |
| Stable supporting detail | `{domain}/{slug}/docs/`, `templates/`, or `scripts/`. |
| Master registry | `INDEX.md`. |

Use lazy folder creation: create only the domain skill folder and supporting subfolders that the imported skill actually needs.

---

## Workflow

### Step 1 - Capture Source

1. Read the provided source.
2. Identify:
   - source name and path or URL
   - source author/vendor if visible
   - original activation triggers
   - required tools, connectors, APIs, or platform assumptions
   - core workflow steps
   - examples and expected outputs
   - reusable templates, scripts, or reference docs
3. If the source is large, summarize only the parts that affect the final skill.

Do not preserve secrets, credentials, private endpoints, account IDs, internal vendor URLs, or personal data.

### Step 2 - Classify Fit

Decide whether the source becomes:

| Outcome | Use when |
|---------|----------|
| Production skill | It maps to a RevOps workflow and can pass G1-G7 after cleanup. |
| Staging note | It has useful knowledge but lacks examples, domain fit, or clear workflow shape. |
| Reference only | It is background material, not an executable AI procedure. |
| Reject/defer | It duplicates an active skill or is too vendor-specific to generalize. |

If the source is not RevOps-related, ask whether it belongs in this playbook before creating files.

### Step 3 - Vendor-Neutral Rewrite

Rewrite the skill around the job-to-be-done, not the original vendor or assistant.

Apply these conversion rules:

| Source pattern | Convert to |
|----------------|------------|
| Assistant-specific syntax | Plain imperative instructions any LLM can follow. |
| Vendor product as the main concept | Generic capability, with vendor as optional stack context only when needed. |
| Tool-specific command sequence | Outcome-driven steps plus optional tool notes. |
| "Use Claude/Codex/Gemini" language | "The agent" or direct imperative instructions. |
| Hidden platform assumptions | Explicit prerequisites and input requirements. |
| Long embedded reference material | `docs/` file under the new skill folder. |
| Large reusable prompt/output format | `templates/` file under the new skill folder. |
| Executable helper logic | `scripts/` file under the new skill folder. |

Keep vendor names only when the workflow genuinely depends on that system. If kept, add the stack tag from `.skills/revops-curator/taxonomy.md` when available and include a generic fallback path.

### Step 4 - Map to Playbook Taxonomy

1. Read `.skills/revops-curator/taxonomy.md`.
2. Choose the primary domain folder.
3. Add secondary domain tags only when the workflow materially spans domains.
4. Generate a slug using `{gerund}-{object}`.
5. Choose `type: capability-uplift` when the skill gives the agent a new tool/process capability.
6. Choose `type: encoded-preference` when the skill captures GxG's way of doing an already-known task.

If domain or slug is ambiguous and the choice affects discoverability, present 2-3 options and ask for confirmation.

### Step 5 - Build the Skill

1. Create `{domain}/{slug}/SKILL.md` from `.skills/revops-curator/templates/new-skill.md`.
2. Fill frontmatter:
   - `name` equals the folder slug
   - `description` follows the Description Optimizer in `.skills/revops-curator/index.md`
   - `status: draft` until all gates pass
   - `domain`, `type`, `tags`, `version`, `updated`, `author`
3. Write the body:
   - one-sentence role statement
   - "When to Use This Skill"
   - routing table if there are multiple workflows
   - numbered instructions
   - at least two concrete examples
   - reference links to any `docs/`, `templates/`, or `scripts/`
   - "Out of Scope"
   - changelog
4. Keep `SKILL.md` under the line limit from `.skills/config.yaml`; move detail into supporting files.

### Step 6 - Source Attribution

Add a short "Import Notes" section near the end of the new `SKILL.md` only when it helps future maintainers.

Use this format:

```markdown
## Import Notes

- Source: {URL or local path, if shareable}
- Adapted: YYYY-MM-DD
- Changes: generalized vendor-specific steps, normalized frontmatter, mapped to `{domain}` taxonomy, added examples/out-of-scope.
```

Do not include private URLs, credentials, proprietary copied text, or long verbatim source excerpts.

### Step 7 - Gate Check and Promotion

Run the G1-G7 checks from `.skills/revops-curator/index.md`.

| Score | Action |
|-------|--------|
| 7/7 | Set `status: active`. |
| 5-6/7 | Set `status: active` only if failures are minor and documented; otherwise keep `draft`. |
| 3-4/7 | Set `status: needs-work` and document blockers. |
| 0-2/7 | Do not create a production skill; use staging or reject/defer. |

Then update `INDEX.md` for any created skill and run the README freshness check from `.skills/revops-curator/lifecycle.md`.

### Step 8 - Report Back

Report:

```text
Onboarded: {skill-name}
Location: {domain}/{slug}/SKILL.md
Status: {draft|active|needs-work}
Domain: {domain}
Tags: {tags}
Gate score: {n}/7
Vendor-neutral changes: {1-3 bullets}
Open issues: {none or blockers}
```

If the source went to staging instead:

```text
Added to staging: _staging/{slug}.md
Reason: {why not production-ready}
Next step: {refine|provide examples|confirm domain|promote later}
```

---

## Quality Checklist

Before finishing, verify:

- [ ] The new skill is in `{domain}/{slug}/SKILL.md`.
- [ ] Frontmatter contains all required fields from `.skills/revops-curator/taxonomy.md`.
- [ ] Description is third-person, includes "Use when", and has at least 5 quoted trigger keywords.
- [ ] The body has at least two concrete examples.
- [ ] "Out of Scope" is present and specific.
- [ ] Vendor-specific dependencies are removed or clearly marked optional.
- [ ] Any supporting docs/templates/scripts are inside the skill folder.
- [ ] `INDEX.md` is updated if a skill was created.
- [ ] README freshness check was performed.

---

## Out of Scope

This workflow does NOT:
- Blindly mirror external skill text into the repo.
- Import non-RevOps skills without explicit user approval.
- Preserve assistant-specific invocation syntax as the production workflow.
- Store raw third-party content when a concise derived workflow is enough.
- Bypass taxonomy, frontmatter, or quality gates for convenience.
