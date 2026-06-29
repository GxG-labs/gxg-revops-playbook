# design — Domain Overview

**Scope:** Design context — extracting a product's design DNA (measurable tokens, qualitative style, and visual effects) from screenshots or URLs, so AI and design agents can build against a structured style profile. Screenshot-first extraction; URL gives higher confidence by reading live source.

**Out of scope:** Generating UI from a DNA profile (separate generation skill), visual asset/image generation, accessibility audits, production component code generation — those belong to separate skills (not yet in this domain).

**Coverage target:** 5 active skills

---

## Skills in This Domain

| Skill | Status | Tags | Last Updated |
|-------|--------|------|-------------|
| [extracting-design-context](extracting-design-context/SKILL.md) | active | #framework #process #template #analysis #p1 | 2026-06-29 |

---

## Key Metrics

Token coverage (share of design decisions expressed as tokens vs hardcoded), component reuse rate, orphan-token count, extraction confidence level (high / medium / low), observed-vs-inferred field ratio.

---

## Coverage Map

| Priority | Skill slug | Status | Notes |
|----------|-----------|--------|-------|
| P1 | extracting-design-context | active | First skill in the domain |
| P2 | *(identify via gap analysis)* | — | design-system creation, asset generation, accessibility audit are candidates |

Run the curator gap analysis to expand this map:
> "/gxg-revops-curator — run gap analysis for design"

---

## Stack References

*(Add the GxG design tools — Figma, Storybook, design-token pipelines — once known)*

---

## Notes

- `design/` is a non-RevOps branch of the playbook. It exists because GxG agents need design DNA extraction the same way they need RevOps workflows. It follows the same SKILL.md conventions and the same curator lifecycle as the ten RevOps domains.
- First skill onboarded from `zanwei/design-dna` (Design DNA — screenshot/URL → 3-dimension design profile), following the same import pattern as `facilitating-brainstorming` (which came from BMad). Named `extracting-design-context` to follow the playbook's gerund+object naming rule (G1).