---
name: logo-colorway-generator
description: Add memorable color systems, adaptive layouts, scenario boards, and colorway prompts to existing logos, generated brand-system boards, mascot logos, base logos, app icons, wordmark lockups, seals, and identity sheets without changing the underlying symbol. Use when the user asks to add colors, recolor, create palettes, generate colorways, make color applications, increase first-glance impact, improve broad audience appeal, change the colorway board background/layout, or enhance a previously generated logo with brand colors.
---

# Logo Colorway Generator

Use this skill after a logo or brand-system board already exists. It adds color strategy, adaptive layout, and scenario applications while preserving the original symbol, wordmark, silhouette, and one-color usability. The default color direction should be memorable, broadly appealing, and practical in real use: create a signature color moment, adjust the board background/layout when useful, and show the logo in scenarios that prove it can work beyond a static brand manual.

## Workflow

1. Identify the source logo or board: brand name, existing symbol, wordmark, mascot/base route, current layout, and intended usage surfaces.
2. Preserve logo invariants: do not redraw the mark, change the mascot feature, alter the wordmark spelling, change the core silhouette, or introduce a new concept unless explicitly requested.
3. Extract the existing design system: monochrome behavior, grid style, typography mood, visual density, applications, mockups, and any existing accent color.
4. Create 2-4 palette routes with clear impact levels. Each route should include signature color, primary, secondary, accent or contrast color, neutral background, dark/ink color, and one-color fallback.
5. Choose the strongest palette route for the brand context and explain why it improves first-glance memorability while still fitting the audience, logo shape, mascot/source idea if any, and production surfaces.
6. Choose a colorway layout mode. Prefer an adaptive scenario board unless the user asks to preserve the original board. Use background color, larger color fields, and practical scene modules to make the colorway feel usable and immediately understandable.
7. Define scenario application rules: main logo, favicon/app icon, lockup, social/avatar, packaging or product surface, digital interface or cover, merch/signage, black/ivory fallback, and small-size use.
8. Generate platform-ready recolor prompts. If the user provides an image, treat it as the edit target or reference according to the request. Preserve the logo structure, but allow the surrounding board layout, background color, and scene modules to change for stronger applicability.
9. If the user asks to "generate", "render", "create an image", "出图", "直接生成", "recolor", "改色", or sets `render_image: true`, use the strongest GPT Image or Universal prompt to call the `imagegen` skill/tool or another available image-generation tool. Generate one polished scenario colorway board unless the user asks for variants.
10. If image generation is requested but no image-generation tool is available, return the colorway package and clearly identify the final prompt to paste into an image model.
11. If `revision_notes` are provided, preserve the useful parts of the prior palette/layout and revise only the requested aspects.

## Output

Return these sections:

- Existing Logo Read
- Palette Routes
- Chosen Color System
- First-Glance Impact
- Scenario Layout Strategy
- Color Application Rules
- Colorway Board Layout
- Final Recolor Prompts
- Generated Colorway, only when direct image generation is requested and available

Read `prompt.md` for detailed color constraints, anti-patterns, and output templates.
