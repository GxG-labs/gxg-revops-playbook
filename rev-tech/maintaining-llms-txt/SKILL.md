---
name: maintaining-llms-txt
description: Maintains a repository-level llms.txt file so LLM agents can quickly understand the project, key documents, and current navigation paths. USE WHEN the user asks to update agent-facing repository guidance, refresh LLM navigation, document important files, validate llms.txt links, or mentions "llms.txt", "LLM docs", "agent navigation", "repo guide", "update llms", "documentation map".
status: active
domain: rev-tech
type: capability-uplift
tags: [rev-tech, #process, #automation, #p2]
version: 1.0.0
updated: 2026-06-15
author: GxG
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Maintaining LLMs.txt

This skill keeps a repository's `llms.txt` accurate, concise, and useful as a navigation file for LLM agents and humans.

## When to Use This Skill

Activate when:
- A repository already has `llms.txt` and its docs, structure, or key workflows changed.
- The user asks for an LLM-readable project map, agent guide, documentation index, or `llms.txt` refresh.
- A new RevOps skill, domain, adapter, README, or project guide changes what an agent should inspect first.

Do NOT use when the user asks to update `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or skill runtime instructions directly; those files have their own adapter conventions.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Refresh existing file** | "update llms.txt", "refresh LLM docs" | See Refresh Existing `llms.txt` |
| **Create missing file** | "create llms.txt", "add agent navigation" | See Create `llms.txt` |
| **Validate file** | "check llms.txt", "validate links" | See Validate `llms.txt` |

---

## Instructions

### Refresh Existing `llms.txt`

1. Read the current root-level `llms.txt`.
2. Read the core project navigation files, usually `README.md`, `PROJECT.md`, `PROJECT_STRUCTURE.md`, `INDEX.md`, and relevant domain `README.md` files.
3. Inspect the current repository structure and identify:
   - new or removed top-level files
   - new or removed documentation files
   - new or removed production skill folders
   - changed adapter or orchestrator locations
4. Compare the current `llms.txt` references with the files that actually exist.
5. Update `llms.txt` using this structure:
   - one H1 project title
   - optional blockquote summary
   - concise context paragraphs without excessive detail
   - H2 sections containing markdown file links with short descriptions
6. Keep links relative to the repository root.
7. Remove stale links, duplicate entries, and generated/build artifacts.
8. Preserve clear organization for LLM consumption: put the most important orientation files first and secondary references in `## Optional` when useful.

### Create `llms.txt`

1. Confirm the repository does not already contain root-level `llms.txt`.
2. Read the same core orientation files listed in Refresh Existing `llms.txt`.
3. Draft a concise file with:
   - project name as the H1
   - one blockquote summary
   - essential documentation links
   - skill registry or workflow links
   - optional secondary references
4. Create the file at the repository root only.
5. Validate every relative link before finishing.

### Validate `llms.txt`

1. Check that the file is at repository root and named exactly `llms.txt`.
2. Confirm the file starts with a single H1.
3. Confirm file references use markdown links in this format:
   ```markdown
   - [Descriptive Name](relative/path.md): Short description
   ```
4. Verify every referenced path exists.
5. Flag unclear section names, redundant links, stale references, or overly verbose descriptions.
6. Report only actionable findings, then patch the file if the user asked for a fix.

---

## File Selection Rules

Include files that help an LLM understand:
- what the repository is for
- where primary workflows live
- how production skills are organized
- which files are the source of truth
- how to contribute or maintain the repository

Exclude files that are:
- generated artifacts
- temporary workbench files
- lockfiles and dependency manifests unless setup context is essential
- duplicate documentation
- private notes, credentials, account identifiers, or local-only paths

---

## Examples

### Example 1: Refresh After Adding a Skill

**Input / Context:**
The user says: "We added `rev-tech/maintaining-llms-txt`; update llms.txt."

**Output:**
The agent reads the current `llms.txt`, confirms the new skill path exists, updates the relevant `## Skills` or `## RevOps Skill Library` section, removes stale entries if found, and reports:

```text
Updated llms.txt:
- Added rev-tech/maintaining-llms-txt/SKILL.md under RevTech skills.
- Verified all referenced links still exist.
- No stale references found.
```

### Example 2: Validate Existing Navigation

**Input / Context:**
The user says: "Check whether llms.txt is still accurate."

**Output:**
The agent checks the file format and links, then reports findings such as:

```text
Findings:
- llms.txt references docs/architecture.md, but that file no longer exists.
- INDEX.md is missing from the Documentation section even though it is the master skill registry.
- The Optional section includes duplicate links to PROJECT_STRUCTURE.md.

Recommended patch:
- Remove docs/architecture.md.
- Add INDEX.md with a short registry description.
- Keep PROJECT_STRUCTURE.md only in Documentation.
```

---

## Import Notes

- Source: https://github.com/github/awesome-copilot/blob/main/skills/update-llms/SKILL.md
- Adapted: 2026-06-15
- Changes: generalized assistant-specific wording, mapped to `rev-tech` taxonomy, added creation and validation workflows, added examples and out-of-scope boundaries.

---

## Out of Scope

This skill does NOT:
- Define or change RevOps domain workflows.
- Replace `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or runtime-specific adapter instructions.
- Store raw third-party skill text in this repository.
- Decide which skills belong in the playbook; use the curator workflow for taxonomy and quality gates.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-15 | Initial active version adapted from external `update-llms` skill |
