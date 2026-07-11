# Corporate Website Generator Prompt Guide

Use this guide when writing the final website prompt or implementation brief.

## Prompt Shape

```text
Design a next-generation corporate official website for <company>.
It must work as an enterprise brand card, not a generic SaaS landing page.

First viewport:
- company name: <company>
- industry descriptor: <industry>
- business: <business>
- target users: <target_users>
- core value: <core_value>
- primary CTA: <cta>
- representative visual: <business-specific visual>

Design roles:
- PM brief: <summary>
- Content copy validation: <terminology, claims, naming, CTA review>
- Design director thesis: <thesis>
- Brand design: <logo/icon/symbol rules>
- Color design: <tokens and usage>
- Typography design: <font roles, type scale, mixed-language rules, line breaks>
- Japanese typography consultant: <spacing, Chinese line breaks, mixed-script critique>
- Visual assets: <icons, illustrations, backgrounds, mockups>
- UI design: <layout, responsive, interactions>

Output separate folders for product brief, content validation, design direction, brand design,
color system, typography system, typography consultant review, visual assets, UI design, website template, and final review.
```

## Copy Rules

- Use direct business language.
- Put value propositions in supporting copy, not vague hero slogans.
- Avoid unsupported claims such as "redefine the future".
- Prefer "what the company does + who it helps + what result users get".

## Visual Rules

- Use a real product, service, system, or outcome as the hero visual.
- Make the company name a first-viewport signal.
- Keep UI controls familiar and compact.
- Use 8px radius or less unless an existing design system says otherwise.
- Keep icons, illustrations, and backgrounds separable as assets.

## Reference-Grade AI Homepage Pattern

For advanced AI companies, build the page around a visible operating system:

1. **Hero as product surface**: show a command bar, deployment console, model/workflow map, or live agent orchestration panel near the headline.
2. **Validated terminology**: expand acronyms on first use. Use Forward Deployed Engineer for the FDE role/person and Forward Deployed Engineering for the practice/system.
3. **Immediate capability proof**: place 3-5 named AI business lines or use cases directly under the hero.
4. **Large contrast band**: use one strong dark or full-bleed section to communicate scale, engineering seriousness, and deployment depth.
5. **Trust and control layer**: include governance, evaluation, human-in-the-loop, permissions, logs, or observability so enterprise users feel safe.
6. **Final action**: make the CTA a concrete business motion such as "map one workflow", "audit AI opportunities", or "deploy the first agent".
7. **Typography system**: define headline line breaks, Chinese/English hierarchy, section heading rhythm, console labels, metric styles, and mobile text behavior before final UI.
8. **Typography consultant pass**: apply Japanese-inspired spacing discipline, semantic Chinese line breaks, quiet body copy, and controlled asymmetry before final UI.

Do not imitate any reference brand's logo, layout exactly, copy, product names, or assets. Translate the benchmark into the client's own brand system.
