---
name: base-logo-generator
description: Generate logo creative directions, image-generation prompts, and optionally direct logo images for company logos, brand logos, cultural/creative merchandise logos, product logos, campaign and advertising logos, event logos, app logos, sub-brand logos, and related visual identity marks. Use when the user asks for logo concepts, logo prompt writing, logo direction, brand symbol ideas, direct logo image generation, or revisions to an existing logo concept.
---

# Logo Generator

Use this skill to turn a business, product, campaign, or cultural/creative brief into a practical logo creative package, and to generate a logo image when the user explicitly asks to create or render one.

## Workflow

1. Identify the logo type: company/brand, product, cultural/creative merchandise, campaign/advertising, event, app, sub-brand, personal brand, or other.
2. Understand the object being branded: name, audience, offering, brand values, usage surfaces, market context, and any style constraints.
3. If the user provides a visual reference, extract its transferable design system: layout, spacing, color restraint, typography mood, scale hierarchy, presentation format, and production constraints. Do not copy the reference mark, wordmark, or trademark-specific silhouette.
4. Extract 2-4 symbolic routes that are specific to the brief and avoid generic category cliches.
5. Choose the strongest direction and explain why it fits the logo type and use case.
6. Generate platform-ready prompts. If the user specifies `target_platform`, focus on that platform; otherwise include Universal, GPT Image, Midjourney, Flux, and Ideogram variants.
7. For direct image generation, default to a brand-system-board presentation unless the user asks for a standalone logo, transparent asset, app icon, or another format. The board should use a square brand guideline grid with numbered modules: main logo, favicon, seal version, wordmark lockup, black/ivory applications, mockup, embossed application, symbol meaning, and a footer value strip.
8. If the user asks to "generate", "render", "create an image", "出图", "直接生成", or sets `render_image: true`, use the strongest GPT Image or Universal prompt to call the `imagegen` skill/tool or another available image-generation tool after preparing the creative direction. Generate one polished primary image unless the user asks for variants.
9. If image generation is requested but no image-generation tool is available, return the creative package and clearly identify the final prompt to paste into an image model.
10. If `revision_notes` are provided, preserve the useful parts of the prior direction and revise only the requested aspects.

## Output

Return these sections:

- Logo Direction
- Symbol Concept
- Visual System Notes
- Brand System Board Layout
- Final Image Prompts
- Generated Logo, only when direct image generation is requested and available

Read `prompt.md` for detailed style constraints, anti-patterns, and output templates.
