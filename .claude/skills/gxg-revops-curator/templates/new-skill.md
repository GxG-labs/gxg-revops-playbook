---
name: {skill-slug}
description: {one-sentence capability statement}. Use when {scenario 1}, {scenario 2}, or when user mentions "{keyword1}", "{keyword2}", "{keyword3}", "{keyword4}", "{keyword5}".
status: draft
domain: {pipeline|demand-gen|sales-enablement|crm-ops|rev-analytics|cs-ops|rev-tech|pricing-packaging|territory-quota|mktg-ops}
type: {capability-uplift|encoded-preference}
tags: [{domain-tag}, {#framework|#process|#template|#metric|#automation|#integration|#analysis|#playbook|#onboarding|#reporting}, {#p0|#p1|#p2}]
version: 1.0.0
updated: YYYY-MM-DD
author: GxG
allowed-tools: {Read, Write, Edit, Bash, Glob, Grep — only what this skill actually needs}
---

# {Skill Title — human-readable, Title Case}

{One sentence: what this skill does and who it's for.}

## When to Use This Skill

Activate when:
- {Concrete scenario 1}
- {Concrete scenario 2}
- {Concrete scenario 3}

Do NOT use when: {common mistrigger situation — helps Claude avoid activating incorrectly}

---

## Workflow

{If this skill has multiple workflows, add a routing table:}

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **{Workflow A}** | "{trigger phrase}" | See §{Section A} |
| **{Workflow B}** | "{trigger phrase}" | See §{Section B} |

---

## Instructions

### {Section A — most common workflow}

1. {Step 1 — imperative, specific}
2. {Step 2}
3. {Step 3}
   - {Sub-step if needed}
   - {Sub-step}
4. {Step 4 — include expected output format}

### {Section B — secondary workflow}

1. {Step 1}
2. {Step 2}

---

## Examples

### Example 1: {most common use case title}

**Input / Context:**
{What the user provides or what the situation is}

**Output:**
{What Claude should produce — be specific, show the actual format}

---

### Example 2: {second use case title}

**Input / Context:**
{Description}

**Output:**
{Expected output}

---

## Reference

{Link to any docs/ files if this skill has supporting documentation:}
- Full field reference: [docs/field-reference.md](docs/field-reference.md)
- Templates: [templates/](templates/)

---

## Out of Scope

This skill does NOT:
- {Explicit non-function 1 — what users might expect but is out of scope}
- {Explicit non-function 2}
- {Point to another skill if overlap exists: "For X, use the `{other-skill}` skill"}

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | YYYY-MM-DD | Initial draft |
