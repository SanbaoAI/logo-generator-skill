---
name: corporate-website-generator
description: Generate next-generation corporate official website brand-card systems from a company conversation or brief. Use when the user wants an official website, homepage, enterprise brand card, corporate website template, role-based design workflow, product-manager intake, design-director review, brand design, color design, UI design, icons, illustrations, backgrounds, separated output directories, or a website that makes visitors understand what the company does, its tone, and what they can get at first glance.
---

# Corporate Website Generator

Use this skill to produce a role-based corporate official website design system. The goal is not a generic landing page. The website must behave like a premium enterprise brand card: in the first viewport, users should understand who the company is, what it does, what tone it has, and what value they can get.

## Core Workflow

Run the work as a design team:

1. **Product Manager**: interview or infer the company profile, business category, target users, core value, goals, preferences, disliked styles, proof points, and first-screen message.
2. **Content Copy Validator**: verify terminology, acronyms, factual claims, naming consistency, Chinese copy, mixed-language expression, and CTA clarity before visual design.
3. **Design Director**: define the official website thesis, first-viewport strategy, visual language, page narrative, role assignments, and design checkpoints.
4. **Brand Designer**: define logo direction, wordmark behavior, favicon/app icon, brand symbols, auxiliary graphics, and homepage identity rules.
5. **Color Designer**: define primary color, accent color, neutral system, accessibility rules, light/dark usage, and where each color may appear.
6. **Typography Designer**: define font roles, Chinese/English mixed typesetting, hero line breaks, type scale, line height, paragraph width, labels, metrics, CTAs, and responsive typography QA.
7. **Japanese Typography Consultant**: review Chinese typography with Japanese-inspired spacing discipline, semantic line breaks, restrained hierarchy, grid logic, and East Asian rhythm.
8. **Visual Asset Designer**: design or prompt the icons, illustrations, backgrounds, textures, mockups, and scene images. Every asset must explain the business or trust signal.
9. **UI Designer**: define layout, navigation, CTA behavior, responsive rules, components, interaction notes, and final page structure.
10. **Design Director Review**: check that copy, brand, color, typography, typography consultant advice, visual assets, and UI all support one clear corporate message.

## First-Viewport Rules

The first viewport must include:

- Company name as a major visual signal.
- Plain industry/category descriptor.
- One sentence that explains the core business and user benefit.
- Representative brand visual, product/state mockup, or business-specific illustration.
- One primary CTA and one secondary CTA.
- A hint of the next section on mobile and desktop.

Avoid abstract slogans that hide the business. Avoid generic AI gradients, decorative blobs, or visuals that could belong to any company.

## Reference-Grade Tech Website Rules

When the user asks for a premium, advanced, AI, frontier-tech, OpenAI-like, Claude-like, Tesla-like, or technology-leader website direction, use benchmark principles without copying any brand:

- **OpenAI principle**: put the product or action surface in the first viewport. Show an input, console, model/workflow surface, API/tool surface, or live system panel so visitors feel the product exists, not just the claim.
- **Claude / Anthropic principle**: pair capability with responsibility, clarity, and trust. Use spacious typography, direct mission language, calm hierarchy, and explicit reliability or governance signals.
- **Tesla principle**: use strong full-viewport moments, high-contrast sections, product-scale metrics, and decisive CTAs. Show engineering scale and deployment reality, not decoration.
- **Enterprise AI principle**: show the bridge between strategy and deployment: business problem -> workflow -> model/tool orchestration -> monitored output -> operating metrics.
- **Content validation principle**: verify terms before designing them. Expand acronyms on first use and keep FDE as Forward Deployed Engineer for role/person or Forward Deployed Engineering for the practice.
- **Visual principle**: avoid flat beige corporate decks, generic blue-purple AI gradients, icon grids without context, and repeated cards as the main experience. Use a distinctive system surface, large type, cinematic section contrast, and restrained signal colors.
- **Typography principle**: do not treat text as default browser styling. Define a deliberate type system before UI: display headlines, section rhythm, mixed Chinese/English rules, body line length, console labels, metrics, CTA hierarchy, and mobile line breaks.
- **Japanese typography consultant principle**: use Japanese-inspired design discipline as critique, not decoration: ma spacing, calm grid, semantic Chinese line breaks, asymmetric balance, quiet body text, and restrained mixed-script hierarchy.

The hero must answer: "What does this AI company actually deploy?" The second viewport must prove it with either a capability matrix, system architecture, workflow cockpit, customer scenario, or measurable operating model.

## Required Outputs

Return these sections:

- `Product Manager Brief`
- `Content Copy Validation`
- `Design Director Strategy`
- `Brand Design`
- `Color Design`
- `Typography Design`
- `Japanese Typography Consultant Review`
- `Visual Assets`
- `UI Design`
- `Separated Output Directories`
- `Design Director Review`
- `Final Website Template Prompt`

When the user asks for files or implementation, create this directory structure under a company slug:

```text
outputs/<company-slug>/
  01-product-brief/
  02-content-validation/
  03-design-direction/
  04-brand-design/
    logo/
    icons/
  05-color-system/
  06-typography-system/
  07-typography-consultant/
  08-visual-assets/
    icons/
    illustrations/
    backgrounds/
    mockups/
  09-ui-design/
    wireframes/
    high-fidelity/
    components/
  10-website-template/
    assets/
  11-final-review/
```

Keep the design-board output separate from source assets. Store icons, illustrations, background images, and website template assets in their own folders.

## Quality Bar

Before final delivery, answer:

- Can a stranger identify the industry within 3 seconds?
- Have terminology, acronyms, claims, and CTAs been validated before design?
- Can they understand what the company does without scrolling?
- Is the visual tone consistent with the stated positioning?
- Is the typography deliberate, readable, responsive, and aligned with the brand tone?
- Has the typography consultant reviewed Chinese line breaks, spacing, and mixed-script hierarchy?
- Are user benefits stated in plain language?
- Are icons, illustrations, and background assets business-specific?
- Are all deliverables separated by role and asset type?
- Does the final website feel like an enterprise brand card, not a generic product landing page?
