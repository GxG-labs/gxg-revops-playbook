# Design Context Extract — Design DNA Schema

Three-dimensional design profile, adapted from `zanwei/design-dna`. Used by `SKILL.md` to keep the entry point lean. Fill [templates/design-context.json](../templates/design-context.json) from this schema.

**Every field must appear in the final output (valid JSON).** Use the string `"unobserved"` (never `""` or `null`) for anything a static screenshot cannot reveal. Add a `"confidence": "observed|inferred"` field on every measurable `design_system` value.

## Top-Level

### `meta`
- `name` — a label for the reference design
- `description` — one-line description
- `source_references` — screenshot filenames or URL
- `method` — `screenshot extraction` / `url extraction`
- `confidence` — `high` / `medium` / `low`
- `created_at` — date

## Dimension 1 — `design_system` (measurable)

Concrete, token-level values. Extract exact values where visible; estimate from visual inspection otherwise and mark `inferred`.

### `color`
- `palette_type` — monochromatic / complementary / analogous / triadic / split-complementary
- `primary.hex` · `primary.role`
- `secondary.hex` · `secondary.role`
- `accent.hex` · `accent.role`
- `neutral.scale` — lightest background → darkest text
- `neutral.usage`
- `semantic.success` · `semantic.warning` · `semantic.error` · `semantic.info` (only if visible)
- `surface.background` · `surface.card` · `surface.elevated`
- `contrast_strategy` — e.g. "high contrast", "subtle layers", "dark-on-light dominant"

### `typography`
- `font_families.heading` · `font_families.body` · `font_families.mono`
- `font_style_notes` — e.g. "geometric sans with humanist touches"
- `type_scale` — one entry per role: `display`, `heading_1`, `heading_2`, `heading_3`, `body`, `body_small`, `caption`, `overline`
  - each with `.size` · `.weight` · `.line_height` · `.tracking`

### `spacing`
- `base_unit`
- `scale`
- `content_density` — compact / comfortable / spacious
- `section_rhythm` — how vertical spacing varies between sections

### `layout`
- `grid_system` · `max_content_width` · `columns` · `gutter`
- `breakpoints` (only if observable)
- `alignment_tendency` — strict grid / centered / asymmetric / mixed

### `shape`
- `border_radius.small` · `.medium` · `.large` · `.pill`
- `border_usage` — none / subtle 1px / bold borders / only on inputs
- `divider_style`

### `elevation`
- `shadow_style` — none / soft diffused / hard drop / layered
- `levels.low` · `levels.medium` · `levels.high`
- `depth_cues` — shadows / overlapping layers / blur-glass / color intensity

### `iconography`
- `style` — stroke / filled / duotone
- `stroke_weight`
- `size_scale`
- `preferred_set` (if identifiable)

### `motion`
- `easing` · `duration_scale.micro` · `.normal` · `.macro`
- `entrance_pattern` · `exit_pattern`
- `philosophy` — minimal functional / playful bouncy / cinematic / none
- Mark `unobserved` from static screenshots unless stated.

### `components`
- `button_style` · `input_style` · `card_style` · `navigation_pattern` · `modal_style` · `list_style`
- `component_notes` — e.g. "ghost buttons with thick borders, rounded inputs with inner shadow"

## Dimension 2 — `design_style` (qualitative)

Subjective assessments. Use specific descriptive language, not generic adjectives.

### `aesthetic`
- `mood` — array of 3–5 mood words, e.g. ["calm", "professional", "warm"]
- `visual_metaphor`
- `era_influence`
- `genre` — e.g. corporate SaaS / indie creative / luxury editorial / neo-brutalist
- `personality_traits` — as if the design were a person
- `adjectives`

### `visual_language`
- `complexity` — minimal / moderate / rich / maximal
- `ornamentation` — none / subtle accents / decorative / heavily ornamented
- `whitespace_usage`
- `visual_weight_distribution`
- `focal_strategy` — single hero element / distributed interest / progressive reveal
- `contrast_level`
- `texture_usage`

### `composition`
- `hierarchy_method` — scale contrast / color weight / spatial isolation / typographic hierarchy
- `balance_type` — symmetric / asymmetric / radial / mosaic
- `flow_direction`
- `grouping_strategy`
- `negative_space_role`

### `imagery`
- `photo_treatment` · `illustration_style` · `graphic_elements` · `pattern_usage` · `image_shape`

### `interaction_feel`
- `feedback_style` · `hover_behavior` · `transition_personality` — snappy / smooth glide / bouncy elastic / fade-subtle
- `loading_style` · `microinteraction_density`
- Mark `unobserved` where a static screenshot can't reveal behavior.

### `brand_voice_in_ui`
- `tone` · `formality` · `cta_style` — direct imperative / friendly invitation / urgent scarcity / subtle suggestion
- `empty_state_approach` · `error_tone`

## Dimension 3 — `visual_effects` (special rendering)

Effects beyond standard CSS — Canvas, WebGL, SVG animation, shaders, JS animation libraries. Set `enabled: false` for every category not present in the reference.

### `overview`
- `effect_intensity` — none / subtle-accent / moderate / heavy-immersive
- `performance_tier` — lightweight (CSS + simple JS) / medium (Canvas 2D, SVG anim) / heavy (WebGL, Three.js, shaders)
- `fallback_strategy` — disable effects / reduce to CSS / static snapshot
- `primary_technology` — CSS only / Canvas 2D / WebGL+Three.js / GSAP / Lottie / SVG SMIL / Pixi.js

### `background_effects`
- `type` — gradient-animation / noise-field / mesh-gradient / video-bg / generative-art / none
- `description` · `technology`
- `params`: `color_palette` · `speed` · `density` · `opacity` · `blend_mode`

### `particle_systems`
- `enabled` · `type` — floating-dots / confetti / snow / fireflies / connected-nodes / custom
- `description` · `technology`
- `params`: `count` · `shape` · `size_range` · `movement_pattern` · `color_behavior` · `interaction` (mouse-repel / mouse-attract / click-burst / none) · `spawn_area`

### `3d_elements`
- `enabled` · `type` — hero-model / product-viewer / scene-bg / text-extrusion / abstract-geometry
- `description` · `technology`
- `params`: `renderer` · `lighting` · `camera` · `materials` · `geometry` · `post_processing` (e.g. [bloom, FXAA, depth-of-field, chromatic-aberration]) · `interaction_model`

### `shader_effects`
- `enabled` · `type` — noise-distortion / wave / morph / color-shift / custom-GLSL
- `description` · `technology`
- `params`: `uniforms` · `vertex_manipulation` · `fragment_output` · `noise_type` (perlin / simplex / worley / fbm) · `distortion`

### `scroll_effects`
- `parallax`: `enabled` · `layers` · `depth_range` · `speed_curve`
- `scroll_triggered_animations`: `enabled` · `trigger_points` · `animation_type` (fade-up / scale-in / clip-reveal / counter / draw-SVG) · `scrub_behavior`
- `scroll_morphing`: `enabled` · `description`

### `text_effects`
- `type` — split-letter-animate / typewriter / glitch / gradient-fill / 3d-extrude / none
- `description` · `technology`
- `params`: `split_strategy` (by-char / by-word / by-line) · `animation_per_unit` · `stagger` · `effect_style`

### `cursor_effects`
- `enabled` · `type` — custom-cursor / magnetic-buttons / spotlight / trail / none
- `description`
- `params`: `shape` · `size` · `blend_mode` · `trail` · `interaction_zone`

### `image_effects`
- `type` — hover-distortion / reveal-clip / parallax-tilt / rgb-shift / none
- `description` · `technology`
- `params`: `filter_pipeline` · `hover_transform` · `reveal_animation` · `distortion_type` (barrel / wave / liquid / glitch)

### `glassmorphism_neumorphism`
- `enabled` · `style` — glass / neumorphic-light / neumorphic-dark / frosted-layers / none
- `params`: `blur_radius` · `transparency` · `border_treatment` · `shadow_type` · `light_source_angle`

### `canvas_drawings`
- `enabled` · `type` — generative-lines / interactive-blobs / data-visualization / pattern-fill / none
- `description` · `technology`
- `params`: `draw_method` · `animation_loop` · `color_scheme` · `responsiveness` · `interaction`

### `svg_animations`
- `enabled` · `type` — path-draw / morph-shapes / logo-reveal / decorative-loop / none
- `description`
- `params`: `animation_method` · `path_morphing` · `stroke_animation` · `filter_effects`

### `composite_notes`
Free-text notes for layered effects, implementation ambiguity, performance trade-offs, or screenshot-only observations that cannot be fully captured in structured fields.

## Validation

Run before emitting:

- [ ] Valid JSON; every field present — no `""` or `null`; `"unobserved"` used where a static screenshot can't reveal a value
- [ ] Every `design_system` measurable value carries a `"confidence": "observed"|"inferred"` field
- [ ] Every `visual_effects` category present has `enabled: true`; absent categories have `enabled: false`
- [ ] `overview.effect_intensity` and `overview.performance_tier` rated from what's observed
- [ ] `design_style` uses specific descriptive language, not generic adjectives
- [ ] Conflicting references resolved: dominant pattern recorded, variants mentioned inline
- [ ] `meta.confidence` set honestly (screenshot-only = medium at best; URL with source = high)
- [ ] `confidence_and_gaps` object lists every `inferred` and `unobserved` field

Record findings in the JSON profile under `confidence_and_gaps`. Do not silently fix — the gaps object is the point.