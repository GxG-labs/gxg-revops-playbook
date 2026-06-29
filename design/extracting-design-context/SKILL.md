---
name: extracting-design-context
description: "Extracts a product's design DNA — design tokens, qualitative style, and visual effects — from screenshots (and optionally URLs or code) into one structured design-context profile an AI or design agent can build against. Use when analyzing a reference UI's look and feel, capturing design style from screenshots, reverse-engineering a design language, preparing a style profile to hand to an AI build agent, or when the user mentions \"design DNA\", \"extract design style\", \"design tokens from screenshot\", \"analyze design\", \"style profile\", \"reverse-engineer UI\", \"visual effects analysis\"."
status: active
domain: design
type: capability-uplift
tags: [design, #framework, #process, #template, #analysis, #p1]
version: 1.0.0
updated: 2026-06-29
author: GxG
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Extracting Design Context

Extracts a product's design DNA from screenshots — the measurable tokens, the qualitative style, and the visual effects — and consolidates them into a single structured design-context profile any AI or design agent can read and build against.

Design DNA has three dimensions. Every extraction covers all three:

1. **Design System** — what you can *measure*: color, typography, spacing, layout, shape, elevation, iconography, motion, components. Exact hex values, pixel sizes, scales.
2. **Design Style** — what you can *feel*: mood, visual language, composition, imagery treatment, interaction feel, brand voice in UI. Qualitative, descriptive.
3. **Visual Effects** — what you can *see but can't express in CSS alone*: background animations, particles, 3D, shaders, scroll effects, text effects, cursor effects, glassmorphism, canvas drawings, SVG animations.

## Path Constants

```
SKILL_DIR = design/extracting-design-context
OUTPUT    = design-context.json   # written next to the source / in the target project
```

Resolve `SKILL_DIR` against the playbook root. `OUTPUT` defaults to wherever the user wants the profile saved. The output is **JSON** — machine-readable, so a downstream build/generation agent can parse it directly.

## When to Use This Skill

Activate when:
- A user provides screenshots (images) of a reference UI and wants its design captured as a structured profile
- A user wants to reverse-engineer a design language / "design DNA" from a reference
- A user is preparing a style profile to hand off to an AI build, clone, or migration agent
- A user provides a URL and wants the live page's design analyzed into the same profile
- A user says "extract the design", "analyze this design", "capture the style", "give me the design DNA / tokens from this screenshot"

Do NOT use when: the user wants to *generate* UI from a DNA profile (that is a separate generation skill — this one only extracts); the user wants an accessibility or contrast audit; the user wants production component code written; or there is no visual reference at all to extract from.

---

## Workflow

| Workflow | Trigger | Steps |
|----------|---------|-------|
| **Extract from screenshots** | user provides images/screenshots, or "analyze this design" | See §Extract from Screenshots |
| **Extract from URL** | user provides a live URL, no screenshot | See §Extract from URL |
| **Show the schema** | "show me the design DNA structure / schema" | See §Show the Schema |

If the user provides neither screenshots nor a URL, ask one question: *"Share screenshots of the reference UI, or give me a URL — and I'll extract the design DNA."* Then route.

The full field schema for all three dimensions lives in [docs/extraction-spec.md](docs/extraction-spec.md). The output JSON skeleton lives in [templates/design-context.json](templates/design-context.json) — use it, do not invent a new structure.

---

## Instructions

### Extract from Screenshots

This is the primary workflow. The user gives one or more screenshots (images) of a reference UI.

1. **Load the schema.** Read [docs/extraction-spec.md](docs/extraction-spec.md) so every field is in context before you analyze. You will fill all three dimensions.

2. **Inventory the references.** Note how many screenshots were provided and what each shows (e.g. "hero + nav", "pricing section", "mobile menu"). If multiple references conflict, record the dominant pattern and mention variants inline — do not silently pick one.

3. **Extract Dimension 1 — Design System (measurable).** For each field in [docs/extraction-spec.md](docs/extraction-spec.md) §Design System, read the value off the screenshot:
   - **color**: sample the dominant palette. Primary by area dominance, secondary by supporting role, accent by CTA usage. Map the neutral scale from lightest background to darkest text. Capture semantic colors only if visible.
   - **typography**: identify font class by visual characteristics (geometric sans, humanist sans, serif, mono). Estimate the type scale ratios from heading/body size relationships; give px values where you can measure them.
   - **spacing**: assess density by element proximity; measure the section rhythm by gap consistency; derive a base unit if a scale is visible.
   - **layout**: identify the grid by content alignment; note max content width, column count, asymmetry, breakpoints only if observable.
   - **shape**: measure border radius by comparing to element height; note border and divider presence.
   - **elevation**: classify shadow softness, spread, and layering.
   - **iconography**: note style (stroke / filled / duotone), stroke weight, size scale.
   - **motion**: only if observable from the static frame or stated by the user — otherwise mark `unobserved`, never invent.
   - **components**: describe observed patterns for button, input, card, navigation, modal, list.
   Every value is either `observed` (you can see/measure it) or `inferred` (you derived it). Flag each.

4. **Extract Dimension 2 — Design Style (qualitative).** Synthesize holistic impressions for each field in [docs/extraction-spec.md](docs/extraction-spec.md) §Design Style:
   - **aesthetic**: 3–5 mood words, genre archetype (corporate SaaS, indie creative, luxury editorial, neo-brutalist…), personality traits, adjectives.
   - **visual_language**: complexity, ornamentation, whitespace usage, visual weight distribution, focal strategy, contrast level, texture usage.
   - **composition**: hierarchy method, balance type, flow direction, grouping strategy, negative-space role.
   - **imagery**: photo treatment, illustration style, graphic elements, pattern usage, image shape.
   - **interaction_feel**: feedback style, hover behavior, transition personality, loading style, microinteraction density (mark `unobserved` where a static screenshot can't reveal it).
   - **brand_voice_in_ui**: tone, formality, CTA style, empty-state approach, error tone.
   Use descriptive language. This dimension is subjective by design — be specific, not generic.

5. **Extract Dimension 3 — Visual Effects.** For each effect category in [docs/extraction-spec.md](docs/extraction-spec.md) §Visual Effects, decide whether it is present in the screenshot:
   - Describe visible effects that go beyond standard CSS — glowing particles, 3D object renders, noise textures, gradient animations, parallax depth, cursor trails, text distortions, glassmorphic surfaces.
   - Set `enabled: false` for every effect category not present in the reference.
   - Where the effect is visible but the exact implementation can't be determined from a static frame, describe it in `composite_notes` rather than fabricating params.
   - Rate `overview.effect_intensity` (none / subtle-accent / moderate / heavy-immersive) and `overview.performance_tier` (lightweight / medium / heavy) from what's observed.

6. **Emit the profile.** Fill [templates/design-context.json](templates/design-context.json) completely — every field populated, valid JSON. Never use empty strings (`""`) or `null` for unrevealable values; use the string `"unobserved"` instead. Mark every measurable `design_system` value with a `"confidence": "observed"|"inferred"` field (already in the skeleton). Save to `OUTPUT`. Tell the user the path.

7. **Report confidence and gaps.** The JSON already carries `confidence_and_gaps`; also summarize it in chat: how many references were used, overall confidence (high / medium / low), and the list of `inferred` / `unobserved` fields that would need source access or a live URL to confirm. Ask: *"Want to adjust any values before using this?"*

### Extract from URL

When the user gives a live URL instead of screenshots:

1. Follow §Extract from Screenshots, but in step 2 also fetch and inspect the live page (and its code where accessible) to resolve values a static screenshot cannot reveal — motion easing/durations, hover/transition behavior, scroll-driven effects, exact font families, real semantic colors.
2. For **Visual Effects**, scan the page source for `<canvas>`, WebGL contexts, Three.js / Pixi.js / GSAP / Lottie imports, custom shaders, IntersectionObserver scroll triggers, SVG `<animate>` elements. Where the source confirms an effect, mark it `observed` with the technology; where only the visual is visible, mark `inferred`.
3. Confidence is higher than screenshot-only — record source-level values where you have them.

### Show the Schema

When the user just wants the structure / field list (no extraction yet):

1. Read [docs/extraction-spec.md](docs/extraction-spec.md).
2. Present the three dimensions and every field, with the one-line guidance for each.
3. Explain the roles: design_system = what you measure; design_style = what you feel; visual_effects = what you can't express in CSS alone.
4. Ask whether to customize or extend any dimension, then offer to run §Extract from Screenshots or §Extract from URL.

---

## Examples

### Example 1: Extract DNA from a single hero-section screenshot

**Input / Context:**
> Two screenshots of a SaaS landing page — the hero + nav, and the pricing section. The user wants the design DNA captured to hand to a build agent.

**Output:** A `design-context.json` saved next to the source. Abbreviated for brevity — every field is present in the real file:

```json
{
  "meta": {
    "name": "Reference SaaS landing",
    "source_references": ["hero-nav.png", "pricing.png"],
    "method": "screenshot extraction",
    "confidence": "medium",
    "created_at": "2026-06-29"
  },
  "design_system": {
    "color": {
      "palette_type": "complementary",
      "primary": { "hex": "#4F46E5", "role": "brand + primary CTA", "confidence": "observed" },
      "secondary": { "hex": "#0EA5E9", "role": "supporting accent", "confidence": "observed" },
      "accent": { "hex": "#F59E0B", "role": "highlight badge", "confidence": "observed" },
      "neutral": { "scale": "#F8FAFC -> #0F172A", "usage": "backgrounds to text" },
      "surface": { "background": "#FFFFFF", "card": "#FFFFFF", "elevated": "#F8FAFC" },
      "contrast_strategy": "dark-on-light dominant"
    },
    "typography": {
      "font_families": { "heading": "geometric sans (Inter-class)", "body": "geometric sans (Inter-class)", "mono": "mono" },
      "type_scale": {
        "display": { "size": "56px", "weight": "700", "line_height": "1.05", "tracking": "-0.02em", "confidence": "observed" },
        "body": { "size": "17px", "weight": "400", "line_height": "1.6", "tracking": "0em", "confidence": "observed" }
      }
    },
    "motion": { "easing": "unobserved", "philosophy": "unobserved" }
  },
  "design_style": {
    "aesthetic": {
      "mood": ["confident", "clean", "modern"],
      "genre": "corporate SaaS",
      "personality_traits": ["approachable", "precise", "optimistic"]
    },
    "visual_language": { "complexity": "minimal", "ornamentation": "subtle accents", "whitespace_usage": "generous" }
  },
  "visual_effects": {
    "overview": { "effect_intensity": "subtle-accent", "performance_tier": "lightweight", "primary_technology": "CSS only" },
    "particle_systems": { "enabled": false, "type": "none" },
    "glassmorphism_neumorphism": { "enabled": true, "style": "frosted-layers", "params": { "blur_radius": "12px" } },
    "composite_notes": "Hero background looks like an animated mesh gradient; can't confirm loop speed from a static frame — marked inferred in background_effects."
  },
  "confidence_and_gaps": {
    "confidence": "medium",
    "why": "2 static screenshots",
    "inferred_fields": ["typography.font_families.heading", "visual_effects.overview.primary_technology"],
    "unobserved_fields": ["motion.easing", "motion.duration_scale", "interaction_feel.hover_behavior", "visual_effects.scroll_effects"]
  }
}
```

The agent reports the output path and asks if any values should be adjusted before use.

### Example 2: Extract from a URL (higher confidence)

**Input / Context:**
> "Extract the design DNA of https://example-studio.com — I can give you the live site, not just screenshots."

**Output:** Same `design-context.json` structure, but:
- `design_system.motion` fields now `"observed"` with real values (`"easing": "cubic-bezier(0.16,1,0.3,1)"`, durations in ms), read from the page.
- `visual_effects.3d_elements`: `"enabled": true`, `"technology": "Three.js"`, `"params.renderer": "WebGLRenderer"`, `"params.post_processing": ["bloom", "FXAA"]` — confirmed from source.
- `meta.confidence`: `"high"`; `confidence_and_gaps.unobserved_fields` lists only fields behind login or interaction (e.g. `brand_voice_in_ui.error_tone`).
- `meta.source_references` records the URL.

The agent flags the few fields still unobserved and offers adjustments.

---

## Reference

- Full three-dimension field schema: [docs/extraction-spec.md](docs/extraction-spec.md)
- Output JSON skeleton: [templates/design-context.json](templates/design-context.json)

---

## Out of Scope

This skill does NOT:
- **Generate UI from a DNA profile** — extraction only; building matching UI from the profile is a separate generation skill
- Run accessibility, contrast-ratio, or WCAG audits — use a dedicated accessibility skill
- Write production component code — this skill produces a context profile, not shipping code
- Create or edit design files (Figma and the like) — it reads references only
- Capture copywriting or content strategy — only visual and structural design DNA
- Work without any visual reference — extraction requires at least a screenshot or a URL

---

## Import Notes

- Source: `https://github.com/zanwei/design-dna` — Design DNA skill (3-phase: Structure / Analyze / Generate; 3-dimension schema: design_system / design_style / visual_effects)
- Adapted: 2026-06-29
- Changes: focused the skill on the user's primary need — **extraction from screenshots** (the source's Phase 2 / Analyze) — and made screenshot the headline workflow with URL as a higher-confidence variant; kept the three-dimension DNA model and full field schema intact (moved to `docs/extraction-spec.md`); dropped the source's Phase 3 (Generate UI from DNA) as out of scope for this skill — a separate generation skill can consume the profile this skill produces; kept the source's JSON output (`design-context.json`) since the profile is machine-consumed by a downstream generation agent — only this skill's own documentation (`SKILL.md`, `docs/`) stays Markdown; added GxG frontmatter, Design-domain taxonomy, two concrete examples, Out of Scope, and a docs/ + templates/ split; added an explicit `"confidence": "observed|inferred"` field on measurable `design_system` values plus a top-level `confidence_and_gaps` object, because screenshot extraction is inherently partial — `"unobserved"` is used for anything a static frame cannot reveal (never `""` or `null`).

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-06-29 | Initial addition — adapted from `zanwei/design-dna` (Design DNA) into the `design` domain as `extracting-design-context`, focused on screenshot-based extraction |