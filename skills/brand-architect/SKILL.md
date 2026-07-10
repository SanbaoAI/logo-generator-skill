---
name: brand-architect
description: Build complete Brand DNA and visual identity systems before logo generation. Use for AI Brand Architect workflows, brand archaeology, cultural roots, human narrative, Jungian archetypes, brand myth, brand civilization, symbol discovery, distinctiveness scoring, restraint scoring, timelessness scoring, brand guidelines, and brand strategy that treats the logo as the final expression rather than the starting point.
---

# AI Brand Architect

Use this skill to turn a brand brief into a durable brand intelligence system. The workflow is:

```text
Input brand
-> understand brand
-> build brand
-> express brand
```

Do not start by drawing a logo. First uncover why the brand should exist, what cultural lineage it belongs to, what human need it serves, what symbols it can own, and whether the final identity can survive time.

If the user asks for a complete operating system, subagent orchestration, parallel specialist delegation, workflow management, or division of labor, use `brand-orchestrator` first. Treat this skill as the core Brand DNA engine inside that larger workflow.

## Workflow

1. Collect or infer the brand inputs: brand name, industry, product, target users, founder story, usage surfaces, market context, and constraints. If details are missing, make reasonable assumptions and label them.
2. Run **Brand Archaeology**: identify industry origins, cultural roots, design traditions, and the historical context that can give the brand depth.
3. Run **Human Meaning**: identify the human need behind the product. Translate "what it sells" into "what it helps people become, feel, do, or believe."
4. Choose **Brand Archetypes**: select one primary and one secondary Jungian archetype, then define the brand's voice, behavior, and visual consequences.
5. Build the **Brand Myth**: write the reason for existence, the long-term enemy, and a one-line myth that can guide future decisions.
6. Define the **Brand Civilization**: values, beliefs, taboos, audience tribe, rituals, symbols, and totems.
7. Run **Symbol Discovery**: derive geometric, historical, cultural, and product-based symbols from the civilization. Produce a ranked candidate set, not a single obvious icon.
8. Run the **Distinctiveness Engine**: score candidate symbols for memory, silhouette, tiny-size clarity, competitor distance, and ownership potential.
9. Run the **Restraint Engine**: remove decorative noise, trend effects, excess elements, and weak details. Prefer one-color, under-three-element, production-ready marks.
10. Run the **Time Machine**: test whether the identity would work 5 years ago, today, 10 years from now, and 30 years from now. Penalize dependency on short-lived trends.
11. Generate the **Visual Identity** only after the strategy is stable: logo direction, wordmark, mascot potential, color system, typography, illustration style, motion style, design language, and brand guidelines.
12. If the user asks to generate, render, create an image, 出图, 直接生成, or sets `render_image: true`, create a focused final image prompt and use the `imagegen` skill/tool when available.

## Output

Return these sections:

- Brand DNA Summary
- Historical Context
- Human Narrative
- Archetype System
- Brand Myth
- Brand Civilization
- Symbol System
- Distinctiveness Engine
- Restraint Engine
- Time Machine
- Visual Identity
- Brand Guidelines
- Final Image Prompts
- Generated Identity, only when direct image generation is requested and available

Read `prompt.md` for detailed phase instructions, scoring rubrics, and output templates.
