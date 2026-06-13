# Logo Generator Skill

*The Brand Design System for AI Agents*

**Agent Skills** that turn a brand brief into a complete visual identity — logo direction, brand-system board, mascot marks, and scenario colorways. Pair with **Codex** to generate polished boards directly via `imagegen`, or use the prompts with GPT Image, Midjourney, Flux, and Ideogram.

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Supported agents](https://img.shields.io/badge/Tools-Codex%20%C2%B7%20Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20ChatGPT-blue.svg)](#installing) [![Skills](https://img.shields.io/badge/Skills-3-green.svg)](#skills) [![Image generation](https://img.shields.io/badge/Image%20Generation-GPT%20Image%20%C2%B7%20Midjourney%20%C2%B7%20Flux%20%C2%B7%20Ideogram-orange.svg)](#codex--image-generation)

**[中文](README.zh-CN.md)** &nbsp;·&nbsp; **English**

<p align="center"><sub>Base Logo &mdash; premium, restrained identity marks</sub></p>
<p align="center">
  <img src="skills/base-logo-generator/assets/sanbaotech-brand-system-board.png" alt="SanBaoTech brand system board" width="32%" />
  <img src="skills/base-logo-generator/assets/moss-lab-brand-system-board.png" alt="Moss Lab brand system board" width="32%" />
  <img src="skills/base-logo-generator/assets/low-energy-brand-system-board.png" alt="Low Energy brand system board" width="32%" />
</p>

<p align="center"><sub>Mascot Logo &mdash; feature extraction from animals, characters, and celestial forms</sub></p>
<p align="center">
  <img src="skills/mascot-logo-generator/assets/aster-koi-brand-system-board.png" alt="Aster Koi mascot brand system board" width="32%" />
  <img src="skills/mascot-logo-generator/assets/strix-forge-brand-system-board.png" alt="Strix Forge mascot brand system board" width="32%" />
  <img src="skills/mascot-logo-generator/assets/manta-vale-brand-system-board.png" alt="Manta Vale mascot brand system board" width="32%" />
</p>

<p align="center"><sub>Colorway &mdash; scenario-based recolor and signature brand color</sub></p>
<p align="center">
  <img src="skills/logo-colorway-generator/assets/sanbaotech-colorway-board.png" alt="SanBaoTech colorway board" width="32%" />
  <img src="skills/logo-colorway-generator/assets/aster-koi-colorway-board.png" alt="Aster Koi colorway board" width="32%" />
  <img src="skills/logo-colorway-generator/assets/manta-vale-colorway-board.png" alt="Manta Vale colorway board" width="32%" />
</p>

[Install](#installing) · [Skills](#skills) · [Which one?](#which-skill-should-i-use) · [Codex & Images](#codex--image-generation) · [Workflow](#workflow) · [Base](#base-logo-generator) · [Mascot](#mascot-logo-generator) · [Colorway](#logo-colorway-generator) · [Schemas](#input-schemas) · [FAQ](#faq)

---

## Why This Exists

Most logo prompts stop at *"make a minimal logo."* This repo is a **complete brand design system** — three modular skills that work independently or as a pipeline:

1. **`base-logo-generator`** — premium, restrained logo design for companies and products
2. **`mascot-logo-generator`** — mascot-derived marks that extract one recognizable feature from an animal, character, or celestial form
3. **`logo-colorway-generator`** — scenario-based color systems that make any existing logo pop at first glance

Every skill outputs a **brand-system board** — a square guideline grid with numbered modules: main logo, favicon, seal, wordmark lockup, black/ivory applications, mockups, embossed application, and symbol meaning. Not just a centered logo on white.

Each skill does one job. Install only what you need, or chain them for a full brief → logo → colorway pipeline.

## Installing

The [`npx skills add`](https://github.com/vercel-labs/agent-skills) CLI scans the `skills/` folder, so all three skills install the same way.

Install all skills:

```bash
npx skills add https://github.com/SanbaoAI/logo-generator-skill
```

Install a single skill by its **install name**:

```bash
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "base-logo-generator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "mascot-logo-generator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "logo-colorway-generator"
```

You can also copy any `SKILL.md` into your project or paste it into Codex / Claude Code / Cursor conversations:

```bash
cp -r skills/base-logo-generator ~/.codex/skills/
```

## Skills

Each skill does one job; you do not need all of them at once. The `Install name` column is the exact value you pass to `--skill`.

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **base-logo-generator** | `base-logo-generator` | Premium, restrained logo design for company, product, app, campaign, event, and cultural/creative marks. Symbol logic comes from brand strategy, metaphor, geometry, negative space, and typography — not from a mascot source. Outputs black/ivory brand-system boards. |
| **mascot-logo-generator** | `mascot-logo-generator` | Mascot-derived logo marks. Starts from an animal, character, object, or celestial form, extracts one recognizable feature (paw, antler, crescent, tusk, etc.), and reduces it into a flat, scalable, trademarkable silhouette. Same board layout as base. |
| **logo-colorway-generator** | `logo-colorway-generator` | Post-processing: adds scenario-based color systems to any existing logo or board. Preserves the original symbol, wordmark, and silhouette. Creates 2-4 palette routes with hex values, a signature brand color, and real-world application mockups. |

### Which skill should I use?

- Start with **base-logo-generator** for foundational company and product logos — clean, premium, restrained.
- Use **mascot-logo-generator** when the mark should come from a recognizable animal, character, or celestial feature.
- Use **logo-colorway-generator** after a logo already exists and needs memorable colors, scenario applications, or a signature brand color that grabs attention.
- Chain **base → colorway** or **mascot → colorway** for a full brand identity pipeline.

## Codex & Image Generation

All three skills work with **Codex** out of the box. When an image-generation tool is available (e.g. Codex `imagegen`, ChatGPT Images), the skill prepares the full creative direction first, then calls the tool to generate a polished board.

**No image tool?** The skills return the final prompt ready to paste into GPT Image, Midjourney, Flux, or Ideogram.

**Image-first tip:** State the pipeline in your prompt — e.g. *"Generate a logo board, then add a colorway"* — and the agent will follow the skills in sequence.

## Workflow

```
   Step 1 — generate logo (choose one)        Step 2 — post-process (optional)
 ┌─────────────────────────────────┐        ┌───────────────────────────────┐
 │  base-logo-generator             │        │                               │
 │    OR                            │  ───▶  │  logo-colorway-generator      │
 │  mascot-logo-generator           │        │                               │
 └─────────────────────────────────┘        └───────────────────────────────┘
   Brief → Logo + Brand-System Board           Existing Logo → Palette + Scenarios
```

Each skill works standalone. Use the colorway skill after either logo skill to add a signature color system.

---

## `base-logo-generator`

Premium, restrained logo design — the foundation of any brand identity. The symbol comes from brand strategy, metaphor, geometry, negative space, or product meaning — not from a mascot source. The result should feel sophisticated, durable, and distinctly ownable.

**Outputs:**

| Section | What You Get |
| --- | --- |
| Logo Direction | Positioning, visual mood, palette, type direction, composition |
| Symbol Concept | Core metaphor, icon form, negative space, 2-4 alternate routes |
| Visual System Notes | Lockups, one-color behavior, small-size legibility, usage surfaces |
| Brand System Board | Numbered modules: main logo, favicon, seal, lockup, applications, mockups, symbol meaning |
| Final Image Prompts | Universal, GPT Image, Midjourney, Flux, Ideogram variants |
| Generated Logo | Direct image when an image tool is available |

<details>
<summary>Example input</summary>

```json
{
  "brand_name": "SanBaoTech",
  "logo_type": "company",
  "brief": "A premium AI company focused on AI communities, AI applications, and practical product ecosystems.",
  "preferred_style": "minimal, premium, abstract",
  "output_layout": "brand-system-board",
  "target_platform": "all"
}
```
</details>

> Generate a logo creative package using the base-logo-generator skill.

---

## `mascot-logo-generator`

Mascot-derived marks with the same premium board layout. Different symbol logic: extract one recognizable feature from an animal, character, object, or celestial form, then compress it into a flat, scalable, trademarkable silhouette.

**Good feature sources:** paws, head profiles, antlers, ears, tusks, eye shapes, masks, wings, tail curves, crescents, helmets, fruit cutouts.

Must not copy famous mascot silhouettes or trademark-specific proportions. Existing brands are method references only.

<details>
<summary>Example input</summary>

```json
{
  "brand_name": "Moonshade",
  "logo_type": "brand",
  "brief": "A quiet fantasy technology brand that needs a mysterious but premium symbol.",
  "preferred_style": "minimal, premium, mysterious",
  "mascot_source": "half moon",
  "mascot_feature_focus": "crescent edge and shadow cutout",
  "output_layout": "brand-system-board"
}
```
</details>

> Generate a mascot-derived logo using the mascot-logo-generator skill.

---

## `logo-colorway-generator`

Post-processing skill for scenario-based color systems. Use after a logo concept, image, or full board already exists. Preserves the original symbol, wordmark, silhouette, and one-color usability — only adds memorable color and real-world application rules.

Creates a **signature brand color** that grabs attention at first glance, validated across app icons, packaging, signage, social, and merch.

**Outputs:**

| Section | What You Get |
| --- | --- |
| Existing Logo Read | What the source mark is and what must be preserved |
| Palette Routes | 2-4 color routes with impact level and hex values |
| Chosen Color System | Signature color, primary, secondary, accent, neutral, dark, one-color fallback |
| First-Glance Impact | Why the colorway is more memorable in app, shelf, merch, or social |
| Scenario Layout | How background, layout, and modules make the colorway broadly usable |
| Color Application Rules | Where each color appears across logo modules and mockups |
| Colorway Board Layout | How to render the scenario-based recolored board |
| Final Recolor Prompts | Platform-ready recolor prompts |

<details>
<summary>Example input</summary>

```json
{
  "brand_name": "Aster Koi",
  "source_logo_description": "Existing mascot-derived brand-system board with koi tail split and water ripple symbol.",
  "brand_context": "Premium tea and botanical lifestyle brand.",
  "palette_direction": "warm ivory base with persimmon signature color, pond green support, ink black",
  "color_impact": "memorable",
  "layout_mode": "adaptive-scenario-board",
  "colorway_count": 3,
  "output_layout": "colorway-board"
}
```
</details>

> Add a colorway system using the logo-colorway-generator skill.

---

## Input Schemas

**Base & Mascot** (shared core fields):

| Field | Required | Description |
| --- | --- | --- |
| `brand_name` | **Yes** | Company, product, campaign, event, IP, or brand name |
| `brief` | **Yes** | What's being branded, audience, value proposition, personality |
| `logo_type` | No | `company` `brand` `product` `cultural-creative` `campaign` `advertising` `event` `app` `sub-brand` `personal-brand` `other` |
| `preferred_style` | No | minimal, modern, playful, corporate, tech, luxury, bold, organic, etc. |
| `output_layout` | No | `brand-system-board` (default), `identity-board`, `standalone-logo`, `square-avatar`, `transparent-asset` |
| `target_platform` | No | `gpt-image` `midjourney` `flux` `ideogram` `all` (default) |
| `render_image` | No | Generate an image when an image tool is available |
| `reference_style` | No | Written description of a visual reference (method only, not for copying) |
| `revision_notes` | No | Iteration feedback when refining a previous concept |
| `output_language` | No | `zh-CN` (default) or `en` |

**Mascot-only additional fields:**

| Field | Required | Description |
| --- | --- | --- |
| `mascot_source` | No | Source entity: deer, bear paw, mammoth head, crescent moon, etc. |
| `mascot_feature_focus` | No | Feature to extract: antlers, paw pads, tusks, ears, crescent edge, etc. |

**Colorway** core fields:

| Field | Required | Description |
| --- | --- | --- |
| `brand_name` | **Yes** | Exact brand name in the existing logo |
| `source_logo_description` | **Yes** | Description of existing logo/board and what must be preserved |
| `brand_context` | No | Category, audience, personality, usage surfaces |
| `palette_direction` | No | Desired mood, specific colors, or colors to avoid |
| `color_impact` | No | `restrained` `memorable` (default) `high-impact` `experimental` |
| `layout_mode` | No | `adaptive-scenario-board` (default), `preserve-original-board`, `campaign-colorway-board`, `application-mockup-board` |
| `audience_scope` | No | `broad-mainstream` (default), `premium-niche`, `youthful-pop`, `enterprise`, `cultural-collectible` |
| `background_direction` | No | Board background or scene direction |
| `colorway_count` | No | Palette routes to propose, 1-4 (default 3) |

Full schemas: [`base`](skills/base-logo-generator/input-schema.json) · [`mascot`](skills/mascot-logo-generator/input-schema.json) · [`colorway`](skills/logo-colorway-generator/input-schema.json)

---

## Project Layout

```text
logo-generator-skill/
├── skill.sh                          # Skill path resolver
├── skills/
│   ├── llms.txt                      # Machine-readable skill index
│   ├── base-logo-generator/
│   │   ├── SKILL.md                  # Skill entry point
│   │   ├── prompt.md                 # Detailed style & output rules
│   │   ├── input-schema.json
│   │   └── assets/                   # Example boards & keyframes
│   ├── mascot-logo-generator/
│   │   ├── SKILL.md · prompt.md · input-schema.json · assets/
│   └── logo-colorway-generator/
│       ├── SKILL.md · prompt.md · input-schema.json · assets/
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## FAQ

**Does it only generate prompts?**

No. For example, when using Codex, the skill can generate suitable images directly.

**Why a brand-system board instead of one centered logo?**

The board validates the mark across real identity surfaces: favicon, seal, lockup, monochrome, mockup, and meaning diagram. One logo on white doesn't tell you if it survives at 16×16 or in one-color print.

**Can mascot logos only use animals?**

No. Whether the source is an animal, plant, celestial body, food, or anything else, the skill extracts its signature feature and generates a more suitable logo.

## License

[MIT](LICENSE) · Copyright (c) 2026 SanbaoAI
