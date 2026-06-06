# Brand System Board Generator

[中文](README.zh-CN.md)

Not just a logo — a complete **brand specification board**. Turn a short brand brief into a polished, editorial-grade brand-system page with numbered modules for the main logo, favicon, seal, wordmark lockup, applications, mockups, symbol meaning, and footer values.

## Showcase

These samples demonstrate the skill's core output: a premium brand-system specification board that evaluates whether a mark can become a real identity system.

### Moss Lab

![Moss Lab brand system board](assets/moss-lab-brand-system-board.png)

Moss Lab is treated as a calm research/creative lab identity. The direction blends moss micro-ecology with laboratory precision: a compact petri-dish or microscope-slide symbol, deep forest green, fresh moss green, warm off-white, and a clean modern sans wordmark.

Final prompt summary: generate a square black-and-ivory brand-system board reading exactly "Moss Lab", with numbered modules for the main logo, favicon, seal, lockup, applications, mockups, symbol meaning, and footer values. Keep it editorial, restrained, scalable, and free of generic AI symbols.

### LOW ENERGY

![LOW ENERGY brand system board](assets/low-energy-brand-system-board.png)

LOW ENERGY is treated as a low-effort, relaxed apparel identity for understated daily outfits. The direction combines a soft fabric fold with a subtle low-battery negative-space idea, using charcoal, muted sage, washed sky blue, and warm off-white.

Final prompt summary: generate a square black-and-ivory brand-system board reading exactly "LOW ENERGY", with numbered modules for the main logo, favicon, seal, lockup, label applications, garment or editorial mockups, symbol meaning, and footer values. Keep it quiet, apparel-ready, memorable, and premium.

### SanBaoTech

![SanBaoTech brand system board](assets/sanbaotech-brand-system-board.png)

SanBaoTech is treated as a premium AI company focused on AI communities, AI applications, and practical product ecosystems. The direction uses an abstract, editorial, black-and-ivory system with a memorable symbol and a refined English wordmark.

Final prompt summary: generate a square brand-system board reading exactly "SanBaoTech", with numbered modules for main logo, favicon, seal version, wordmark lockup, black/ivory applications, product or editorial mockups, symbol meaning, and footer values. Keep it mostly monochrome, premium, instantly recognizable, one-color friendly, and free of generic AI cliches.

## Overview

This skill goes beyond simple logo image generation. It produces a **brand specification board** — a complete creative package that includes strategic thinking, symbol concept, visual system notes, and a polished brand-system page layout. It supports company logos, brand logos, cultural/creative merchandise logos, product logos, campaign and advertising logos, event logos, app logos, and sub-brand marks. Outputs are optimized for **GPT Image**, **Midjourney**, **Flux**, and **Ideogram**.

The default output is not a single centered logo on a blank canvas, but a **brand-system board**: a square ivory guideline page with numbered sections for `MAIN LOGO`, `FAVICON`, `SEAL VERSION`, `WORDMARK LOCKUP`, applications, mockups, symbol meaning, and footer values. This format is designed to evaluate whether a logo can work as a real identity system — testing scalability, one-color behavior, lockup flexibility, and contextual application — rather than just looking attractive as a standalone graphic.

## Input

| Field | Required | Description |
|-------|----------|-------------|
| `brand_name` | Yes | Company, product, campaign, event, IP, or brand name |
| `brief` | Yes | What is being branded, audience, value proposition, personality, and usage context |
| `logo_type` | No | `company` · `brand` · `product` · `cultural-creative` · `campaign` · `advertising` · `event` · `app` · `sub-brand` · `personal-brand` · `other` |
| `preferred_style` | No | Visual style preference, such as `minimal`, `modern`, `heritage modern`, `playful`, `corporate`, `tech`, `luxury`, or `bold` |
| `reference_style` | No | Written description of a visual reference's layout, spacing, typography, color restraint, and mood |
| `output_layout` | No | `brand-system-board` · `identity-board` · `standalone-logo` · `square-avatar` · `transparent-asset`; default is `brand-system-board` for direct renders |
| `target_platform` | No | `gpt-image` · `midjourney` · `flux` · `ideogram` · `all` |
| `render_image` | No | `true` to generate an actual logo image after creating the final prompt, when image generation is available |

## Output

| Section | Description |
|---------|-------------|
| **Logo Direction** | Brand positioning, visual mood, color palette, typography, composition |
| **Symbol Concept** | Core metaphor, icon form, and rationale |
| **Visual System Notes** | Lockups, one-color behavior, small-size behavior, and usage notes |
| **Brand System Board Layout** | Direct-render board layout with numbered modules for main logo, favicon, seal, lockup, applications, mockups, symbol meaning, and footer values |
| **Final Image Prompt** | Paste-ready prompts: Universal, GPT Image, Midjourney, Flux, Ideogram |
| **Generated Logo** | Optional direct image output when `render_image: true` or the user asks to generate/render the logo |

## Quick Start

```json
{
  "brand_name": "Nebula",
  "logo_type": "company",
  "brief": "A cloud infrastructure platform that helps startups deploy and scale applications with zero DevOps overhead.",
  "preferred_style": "tech",
  "output_layout": "brand-system-board"
}
```

Paste the JSON (or describe the company in plain text) and ask:

> Generate logo concepts using the logo-generator skill.

The agent returns the complete output sections. Copy the platform-specific prompt into your image tool of choice.

To generate an image directly, ask:

> Generate a Moss Lab logo image using the logo-generator skill.

Or set:

```json
{
  "brand_name": "Moss Lab",
  "brief": "An AI tools brand for independent developers and designers...",
  "render_image": true
}
```

When direct generation is requested, the agent prepares the creative direction and uses the strongest GPT Image or Universal prompt to create one polished brand-system board by default: a square guideline page with numbered sections for `MAIN LOGO`, `FAVICON`, `SEAL VERSION`, `WORDMARK LOCKUP`, applications, mockups, symbol meaning, and footer values. Ask for `identity-board`, `standalone-logo`, `square-avatar`, or `transparent-asset` when you need a simpler output.

## Brand System Board Style

The default direct-render layout follows a complete premium brand-spec board:

- Square ivory canvas with a thin outer border and fine internal grid lines.
- Numbered modules for `MAIN LOGO`, `FAVICON`, `SEAL VERSION`, `WORDMARK LOCKUP`, applications, mockups, and `SYMBOL MEANING`.
- Mostly black and ivory, with a tiny deep-red accent line or dot when useful.
- A footer strip with compact values such as `OUR MISSION`, `OUR VIEW`, `OUR STANDARD`, and `OUR PROMISE`.
- Consistent symbol reuse across favicon, seal, lockup, applications, and mockups.

This style is useful for evaluating whether a logo can become a real identity system rather than only an attractive single graphic.

## Worked Example: Moss Lab

### Example Input

```json
{
  "brand_name": "Moss Lab",
  "logo_type": "brand",
  "brief": "An AI tools brand for independent developers and designers. The logo should feel intelligent, calm, and laboratory-like, without robot heads, brains, circuit boards, or generic AI symbols. Main uses include website branding, app icon, and open-source project avatar.",
  "preferred_style": "minimal, quiet, experimental",
  "target_platform": "all",
  "render_image": true
}
```

### Generated Result

#### Logo Direction

Position Moss Lab as a calm AI workshop: precise, useful, and quietly inventive. The visual mood should combine the softness of moss with the discipline of a lab mark, using a compact symbol that feels organic but engineered.

Use a restrained palette of deep moss green, graphite, warm off-white, and a small pale mint accent. Typography should be a clean geometric sans with subtle humanist warmth, such as a softened grotesk or rounded technical sans. The composition should support a horizontal wordmark for the website, a stacked lockup for documentation, and a square icon for GitHub or app surfaces.

This direction fits an AI tools brand because it avoids loud futurism and instead signals thoughtful utility, craft, and reliability for makers.

#### Symbol Concept

The primary symbol is a rounded lab tile containing a small negative-space monogram: an `M` suggested by two moss-like arcs and a central vertical stem, also reading as a quiet test sample under observation. The mark should be simple enough to work as a favicon and distinct enough to avoid common AI cliches.

Alternative symbolic routes:

- A minimal petri-dish circle with an `M` formed from growing negative space.
- A lab flask silhouette reduced into a leaf-like `M`, without becoming botanical decoration.
- A square terminal cursor combined with a soft moss patch, suggesting code plus organic experimentation.

#### Visual System Notes

Use three lockups: symbol plus wordmark, symbol above wordmark, and standalone app/avatar icon. The one-color version should preserve the negative-space `M` clearly in black, white, or moss green. At small sizes, remove secondary detail and keep only the rounded tile, the `M` cutout, and one clean accent shape.

For open-source avatars, use the standalone symbol on a warm off-white or graphite background. For website headers, pair the icon with a quiet wordmark and generous spacing. Avoid gradients, glowing AI effects, molecule diagrams, and overly literal lab equipment.

#### Final Image Prompt

##### Universal

Create a premium minimalist logo for "Moss Lab", an AI tools brand for independent developers and designers. Design a compact symbol that combines the feeling of soft moss growth with a precise laboratory sample tile. Use a rounded square or circular lab-tile icon with a negative-space `M` formed from two organic arcs and a central stem. Pair it with a clean geometric sans wordmark reading "Moss Lab". Mood: intelligent, calm, experimental, trustworthy. Palette: deep moss green, graphite, warm off-white, pale mint accent. Vector-like, scalable, one-color friendly, favicon-ready. No robot heads, brains, circuit boards, globes, wifi icons, generic AI symbols, light bulbs, shields, or swooshes.

##### GPT Image

Design a clean vector-style logo on a plain warm off-white background for the brand "Moss Lab". The logo should include a compact icon and readable wordmark. The icon is a rounded lab sample tile in deep moss green, with a simple negative-space `M` shaped from two soft moss-like arcs and one precise central stem. The wordmark says exactly "Moss Lab" in a quiet geometric sans typeface with subtle warmth. The overall feeling is intelligent, calm, experimental, and useful for AI tools made for independent developers and designers. Keep the logo flat, premium, balanced, and usable at small app-icon size. Avoid robot heads, brains, circuit boards, generic AI imagery, glowing effects, complex lab equipment, and decorative swooshes.

##### Midjourney

premium minimalist vector logo for "Moss Lab", AI tools brand for indie developers and designers, rounded lab sample tile icon, negative space M made from soft moss arcs and precise central stem, calm intelligent experimental mood, deep moss green graphite warm off-white pale mint accent, clean geometric sans wordmark, flat scalable favicon friendly, no robot head no brain no circuit board no generic AI symbol no glow --ar 1:1 --v 6 --style raw

##### Flux

Moss Lab logo, premium minimalist vector mark, AI tools brand, independent developers and designers, rounded lab sample tile, negative-space M, soft moss arcs, precise central stem, calm intelligent experimental, deep moss green, graphite, warm off-white, pale mint accent, clean geometric sans wordmark, flat design, scalable, one-color friendly, favicon-ready, no robot, no brain, no circuit board, no generic AI icon, no glow

##### Ideogram

Create a clean vector-like logo with exact readable text: "Moss Lab". Use a compact rounded lab-tile icon beside the wordmark. The icon should show a negative-space capital `M` formed by two soft moss-like arcs and a precise central stem. Style: premium minimalist, calm, intelligent, experimental, made for an AI tools brand serving independent developers and designers. Colors: deep moss green, graphite, warm off-white, small pale mint accent. Make the wordmark crisp and correctly spelled. Avoid robot heads, brains, circuit boards, generic AI symbols, glow effects, and clutter.

## Directory Structure

```
logo-generator-skill/
├── SKILL.md            # Skill definition and workflow
├── prompt.md           # Output templates and platform notes
├── input-schema.json   # Input JSON Schema
├── README.md           # English documentation (this file)
└── README.zh-CN.md     # Chinese documentation
```

## Supported Image Models

| Platform | Prompt variant | Notes |
|----------|---------------|-------|
| GPT Image | `### GPT Image` | Natural language; strong layout control |
| Midjourney | `### Midjourney` | Includes `--ar 1:1 --v 6 --style raw` |
| Flux | `### Flux` | Concise keyword-style prompt |
| Ideogram | `### Ideogram` | Emphasizes legible wordmark text |

Set `"target_platform": "midjourney"` in input to focus on one platform; default is `"all"`.

## Install as Cursor Skill

```bash
# Project-level (shared with team)
cp -r logo-generator-skill .cursor/skills/logo-generator

# Personal (all projects)
cp -r logo-generator-skill ~/.cursor/skills/logo-generator
```

The skill entry file is already named `SKILL.md`.

## Iteration

Add `revision_notes` to refine a concept without restarting:

```json
{
  "brand_name": "Nebula",
  "brief": "...",
  "preferred_style": "tech",
  "revision_notes": "Simpler icon, no gradients, bolder wordmark"
}
```

## License

MIT
