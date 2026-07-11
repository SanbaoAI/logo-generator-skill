# AI Corporate Website Generator

*Brand-led corporate front-door website generation*

This project is a **full brand design system for companies**: brand positioning, logo, color, typography, visual assets, and scenario-specific brand expression. It helps companies systematize how they explain who they are, what they do, what they feel like, and what users can get from them.

This branch focuses specifically on generating a company's **front-door official website**. It is for teams that do not want to write code from scratch or settle for generic templates: provide company information, brand assets, and business direction, then generate a premium website template that explains the business and expresses the brand in minutes.

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Supported agents](https://img.shields.io/badge/Tools-Codex%20%C2%B7%20Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20ChatGPT-blue.svg)](#installing) [![Skills](https://img.shields.io/badge/Skills-10-green.svg)](#skills) [![Website generation](https://img.shields.io/badge/Website-Brand%20Card%20System-orange.svg)](#codex--website-generation)

**[中文](README.zh-CN.md)** &nbsp;·&nbsp; **English**

[Install](#installing) · [Website Workflow](#corporate-brand-card-website-workflow) · [Runtime](#design-skill-runtime-v2) · [Skills](#skills) · [Schemas](#input-schemas) · [FAQ](#faq)

---

## Why This Exists

A corporate official website is not a pretty long image or a stack of marketing cards. It is the first entrance for users to understand the company: the first glance should explain who the company is, the second glance should explain what problem it solves, and the rest should build enough trust for action.

This branch treats website generation as a brand design workflow, not a page assembly workflow:

```text
Company information / brand assets / business direction
-> product-manager intake and value clarification
-> copy and terminology validation
-> brand, color, typography, and visual system design
-> corporate website template and separated asset output
-> design-director final review
```

The website is the primary deliverable. Brand DNA, logo, color, copy, typography, visual assets, and UI are supporting systems that make the website clearer, more premium, and more recognizable.

Core capabilities:

1. **No coding required**: describe the company, business, and brand preferences in natural language to get a website design plan and static template.
2. **Minutes to a website draft**: quickly create a premium, discussable, previewable website foundation instead of staying at abstract advice.
3. **Brand-led visual system**: the site is not a generic template; its visual language comes from brand assets, industry category, and business value.
4. **Enterprise brand-card first viewport**: communicate company name, category, core value, target users, trust tone, and action path.
5. **Separated delivery**: product brief, copy validation, design direction, brand design, color system, typography system, visual assets, UI, and website template are output separately.

## Installing

The [`npx skills add`](https://github.com/vercel-labs/agent-skills) CLI scans the `skills/` folder, so all ten skills install the same way.

Install all skills:

```bash
npx skills add https://github.com/SanbaoAI/logo-generator-skill
```

Install a single skill by its **install name**:

```bash
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "brand-orchestrator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "brand-agent-roles"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "brand-architect"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "base-logo-generator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "mascot-logo-generator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "logo-colorway-generator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "content-copy-validator"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "typography-system-designer"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "japanese-typography-consultant"
npx skills add https://github.com/SanbaoAI/logo-generator-skill --skill "corporate-website-generator"
```

You can also copy any `SKILL.md` into your project or paste it into Codex / Claude Code / Cursor conversations:

```bash
cp -r skills/brand-orchestrator ~/.codex/skills/
```

## Skills

Each skill does one job; you do not need all of them at once. The `Install name` column is the exact value you pass to `--skill`.

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **corporate-website-generator** | `corporate-website-generator` | Core skill: corporate official website generator. Uses PM intake, copy validation, design director strategy, brand design, color design, typography system design, typography consultant review, visual asset design, and UI design to create an enterprise brand-card website template with separated output directories. |
| **brand-orchestrator** | `brand-orchestrator` | Complete workflow controller for the AI Brand Architect system. Plans the project, spawns or simulates specialist subagents, assigns research and creative work, runs phase gates, resolves conflicts, routes to visual skills, and assembles the final deliverable. |
| **brand-agent-roles** | `brand-agent-roles` | Division-of-labor skill for subagent teams. Defines specialist roles, prompts, output contracts, handoff rules, overlap boundaries, and QA responsibilities for brand archaeology, human insight, myth, civilization, symbols, audits, visual identity, prompts, and guidelines. |
| **brand-architect** | `brand-architect` | Complete AI Brand Architect workflow. Builds Brand DNA before visuals: historical context, human narrative, Jungian archetypes, brand myth, brand civilization, symbol discovery, distinctiveness scoring, restraint scoring, timelessness testing, visual identity, and brand guidelines. Logo becomes the final expression, not the starting point. |
| **base-logo-generator** | `base-logo-generator` | Premium, restrained logo design for company, product, app, campaign, event, and cultural/creative marks. Symbol logic comes from brand strategy, metaphor, geometry, negative space, and typography — not from a mascot source. Outputs black/ivory brand-system boards. |
| **mascot-logo-generator** | `mascot-logo-generator` | Mascot-derived logo marks. Starts from an animal, character, object, or celestial form, extracts one recognizable feature (paw, antler, crescent, tusk, etc.), and reduces it into a flat, scalable, trademarkable silhouette. Same board layout as base. |
| **logo-colorway-generator** | `logo-colorway-generator` | Post-processing: adds scenario-based color systems to any existing logo or board. Preserves the original symbol, wordmark, and silhouette. Creates 2-4 palette routes with hex values, a signature brand color, and real-world application mockups. |
| **content-copy-validator** | `content-copy-validator` | Copy validation for terminology, acronyms, factual claims, naming consistency, Chinese wording, mixed-language expression, CTA clarity, and unsupported claims before design or publication. |
| **typography-system-designer** | `typography-system-designer` | Typography system designer for websites, AI/technology pages, dashboards, mixed Chinese-English layouts, type scales, hero line breaks, CTA hierarchy, and responsive typography QA. |
| **japanese-typography-consultant** | `japanese-typography-consultant` | Senior typography consultant pass for Chinese and East Asian layouts using Japanese-inspired whitespace, semantic line breaks, grid discipline, quiet body copy, and mixed-script hierarchy. |

### Which skill should I use?

- Start with **corporate-website-generator** when the goal is a corporate official website or next-generation enterprise brand-card homepage.
- Use **brand-orchestrator** when you want a full end-to-end system, subagent delegation, phase gates, synthesis, QA, and final delivery.
- Use **brand-agent-roles** when you need to define the expert team, role prompts, output contracts, and handoff rules.
- Use **brand-architect** when you want Brand DNA, cultural roots, strategy, symbol validation, timelessness, and guidelines before any logo is drawn.
- Use **base-logo-generator** for foundational company and product logos — clean, premium, restrained.
- Use **mascot-logo-generator** when the mark should come from a recognizable animal, character, or celestial feature.
- Use **logo-colorway-generator** after a logo already exists and needs memorable colors, scenario applications, or a signature brand color that grabs attention.
- Use **content-copy-validator** before design when terminology, acronyms, claims, naming, Chinese copy, mixed-language wording, or CTA clarity needs validation.
- Use **typography-system-designer** when text hierarchy, Chinese/English mixed typesetting, headline rhythm, responsive type scale, or CTA/label readability needs a dedicated pass.
- Use **japanese-typography-consultant** after typography design when Chinese line breaks, East Asian rhythm, ma spacing, quiet body copy, or mixed-script hierarchy needs a senior consultant review.
- Use **base-logo-generator**, **mascot-logo-generator**, or **logo-colorway-generator** when an existing brand mark needs stronger website-ready identity assets.
- Recommended website pipeline: **corporate website → copy validation → typography → typography consultant → visual assets → UI → review**.

## Codex & Website Generation

All ten skills work with **Codex** out of the box. When subagents are available, the orchestrator can delegate specialist work in parallel; when image-generation tools are available (e.g. Codex `imagegen`, ChatGPT Images), the visual skills can generate brand assets; when the target is a website, `corporate-website-generator` outputs page structure, visual systems, asset folders, and a reviewable static website template.

**No frontend or image tool?** The skills still return a structured website design plan, page narrative, asset list, copy validation, and prompts that a designer or developer can continue from.

**System tip:** State the target clearly — e.g. *"Use our logo and brand information to generate an enterprise brand-card official website"* — and the agent will prioritize the website workflow instead of stopping at a logo or brand board.

## Workflow

```
   Step 1 — clarify company       Step 2 — content + brand system   Step 3 — website design      Step 4 — separated delivery
 ┌─────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────┐     ┌──────────────────────────┐
 │ PM intake                │ ──▶ │ Copy + Brand + Typography │ ──▶ │ Visual assets + UI    │ ──▶ │ Website template + QA    │
 └─────────────────────────┘     └──────────────────────────┘     └──────────────────────┘     └──────────────────────────┘
   who, what, for whom             terms, logo, color, type          layout, assets, states       files, folders, review
```

Each skill works standalone, but this branch defaults to the website as the main scenario. Logo, colorway, and Brand DNA are upstream materials for the corporate website, not the final promotional focus.

## Corporate Brand-Card Website Workflow

`corporate-website-generator` is not a generic landing-page maker. Its job is to make the first viewport behave like an enterprise brand card: within 3-5 seconds, visitors should know who the company is, what it does, what it feels like, what they can get, and what to do next.

```text
Product Manager
-> Content Copy Validator
-> Design Director
-> Brand Designer
-> Color Designer
-> Typography System Designer
-> Japanese Typography Consultant
-> Visual Asset Designer
-> UI Designer
-> Design Director Final Review
```

Quality gates:

| Gate | Check |
| --- | --- |
| First-viewport recognition | Company name, category, core business, target users, main benefit, and representative visual must be visible. |
| Content validation | Terminology, acronyms, factual claims, naming consistency, Chinese wording, mixed-language copy, and CTAs are checked before design. FDE is validated as `Forward Deployed Engineer / Forward Deployed Engineering`; avoid `Field Deployment Engineering`. |
| Visual tone | Color, typography, icons, illustrations, backgrounds, and UI must express the company's character instead of relying on generic AI gradients. |
| Chinese typography | Headlines need semantic line breaks, body copy needs restrained whitespace, and mixed Chinese-English hierarchy should pass the Japanese-inspired typography consultant review. |
| Separated delivery | Product brief, content validation, design direction, brand design, color system, typography system, typography consultant, visual assets, UI, website template, and final review are separated. |

The repository includes a SanBao AI official-site example:

| File | Purpose |
| --- | --- |
| `outputs/sanbao-ai-official-site/index.html` | Static website template entry |
| `outputs/sanbao-ai-official-site/styles.css` | Advanced AI/technology visual system and responsive layout |
| `outputs/sanbao-ai-official-site/script.js` | Lightweight interactions |
| `outputs/sanbao-ai-official-site/design-brief.md` | Design brief, content validation notes, and FDE terminology rule |

## Design Skill Runtime v2

The repository now includes a lightweight Python runtime for multi-scene brand visual generation:

```text
User Input
-> Skill Router
-> Selected Skill
-> Prompt Compiler
-> Generation Engine
-> Critic Agent
-> Memory Writer
```

Runtime modules:

| Module | Purpose |
| --- | --- |
| `core/prompt_compiler.py` | Builds structured prompts from brand memory, last design, scene context, and task. |
| `skills/skill_router.py` | Routes requests to `corporate_website_skill`, `social_media_skill`, `ppt_skill`, `poster_skill`, or `logo_skill`. |
| `skills/corporate_website_skill.py` | Converts a company brief into a role-based corporate website design package with separated output folders. |
| `skills/social_media_skill.py` | Converts brand DNA and content input into a publishable social media carousel plan. |
| `core/critic_agent.py` | Scores clarity, brand consistency, visual balance, and issues. |
| `core/memory_writer.py` | Appends asset history and updates visual DNA. |
| `core/runtime.py` | Runs the complete route -> compile -> skill -> critic -> memory loop. |

Example test case:

```bash
python3 -m unittest discover -s tests
```

The included tests validate both social media output and: "帮我做一个企业品牌名片型官网" -> `corporate_website_skill` -> PM brief, design director strategy, brand/color/asset/UI plans, separated directories, critic scores, and memory history.

---

## `brand-orchestrator`

The workflow controller for the full AI Brand Architect system. It decides which specialist work should run in parallel, what each subagent must return, when to synthesize, and when to move through phase gates.

**Outputs:**

| Section | What You Get |
| --- | --- |
| Orchestration Plan | Scope, assumptions, selected lanes, subagent roster, and phase gates |
| Delegation Briefs | Copy-ready tasks for specialist subagents |
| Integration Matrix | How archaeology, human meaning, symbols, audits, and visuals connect |
| Gate Decisions | Continue, revise, or stop decisions after strategy, symbol, and visual phases |
| Final Assembly | Brand DNA, visual identity direction, prompts, guidelines, and QA notes |

---

## `brand-agent-roles`

The division-of-labor layer for specialist subagents. Use it to define the expert team before or during orchestration.

**Core roles:**

| Role | Responsibility |
| --- | --- |
| Brand Archaeologist | Cultural roots, historical context, design traditions |
| Human Insight Strategist | Human need, emotional meaning, audience tension |
| Archetype and Myth Strategist | Jungian archetypes, brand myth, enemy belief |
| Civilization Builder | Values, taboos, tribe, rituals, totems |
| Semiotic Symbol Scout | Symbol candidates, metaphors, cultural risk |
| Distinctiveness Auditor | Memory, silhouette, tiny-size, competitor distance |
| Restraint and Time Auditor | Subtraction, production readiness, timelessness |
| Visual Identity Director | Logo direction, typography, color, system design |
| Prompt Producer | Image-generation prompts for selected platforms |
| Guidelines Editor | Final brand rules, usage, extension principles |

---

## `brand-architect`

The complete AI Brand Architect workflow. It first answers the deeper question: if this brand lives for 100 years, what will people remember it for?

**Outputs:**

| Section | What You Get |
| --- | --- |
| Brand DNA Summary | What the brand is, who it serves, and what it should be remembered for |
| Historical Context | Cultural roots, industry origins, design traditions, and source stack |
| Human Narrative | Functional, emotional, and deeper human needs behind the product |
| Archetype System | Primary and secondary Jungian archetypes, behavior, voice, risks |
| Brand Myth | Reason for existence, enemy belief, transformation, one-line myth |
| Brand Civilization | Values, taboos, tribe, rituals, totems, language, symbolic materials |
| Symbol System | Top 20 symbols derived from geometry, history, culture, and product meaning |
| Distinctiveness Engine | Memory, silhouette, tiny-size, competitor distance, ownership scores |
| Restraint Engine | Subtraction rules, one-color behavior, production readiness |
| Time Machine | 5-years-ago, today, 10-year, and 30-year durability tests |
| Visual Identity | Logo, wordmark, color, typography, illustration, motion, design language |
| Brand Guidelines | Practical use rules and extension principles |

<details>
<summary>Example input</summary>

```json
{
  "brand_name": "Leios",
  "industry": "AI design tools",
  "product": "A thinking-first AI design platform that helps creators turn ideas into visual identity systems.",
  "target_users": "Independent creators, product founders, and small teams who need design judgment before visual execution.",
  "founder_story": "The brand was created from the belief that design should return to thinking, not visual noise.",
  "research_depth": "deep",
  "output_mode": "full-system"
}
```
</details>

> Build Brand DNA using the brand-architect skill, then generate the visual identity.

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

## `corporate-website-generator`

Next-generation corporate official website generator. Use it when the website should act as an enterprise brand card: the visitor should understand the company, category, tone, and benefit in the first viewport.

It runs a role-based workflow instead of jumping straight into a page mockup: Product Manager intake, Content Copy Validation, Design Director strategy, Brand Design, Color Design, Typography System Design, Japanese Typography Consultant review, Visual Asset Design, UI Design, and final director review.

**Outputs:**

| Section | What You Get |
| --- | --- |
| Product Manager Brief | Company profile, business category, target users, core value, goals, preferences, dislikes, and intake questions |
| Content Copy Validation | Terminology, acronym expansion, factual claims, naming consistency, Chinese wording, mixed-language copy, and CTA clarity |
| Design Director Strategy | First-viewport thesis, visual language, page narrative, role assignments, and checkpoints |
| Brand Design | Logo direction, wordmark rules, favicon/app icon, brand symbols, and homepage identity rules |
| Color Design | Primary/accent/neutral tokens, usage rules, accessibility checks, and tone alignment |
| Typography Design | Font roles, type scale, mixed Chinese-English rules, hero line breaks, labels, metrics, CTAs, and responsive QA |
| Japanese Typography Consultant Review | Spacing, semantic Chinese line breaks, East Asian rhythm, quiet body copy, and mixed-script hierarchy critique |
| Visual Assets | Icons, illustrations, backgrounds, textures, mockups, and asset naming rules |
| UI Design | Layout system, navigation, CTA behavior, responsive rules, components, and interaction notes |
| Separated Output Directories | Product brief, design direction, brand design, color system, visual assets, UI design, website template, and final review folders |
| Design Director Review | Final quality gate ensuring the website reads as a corporate brand card, not a generic landing page |

<details>
<summary>Example input</summary>

```json
{
  "company_name": "Sanbao Design AI",
  "industry": "AI brand design",
  "business": "enterprise brand identity and website generation",
  "target_users": "founders and product teams",
  "core_value": "a clear official website and reusable brand system",
  "brand_tone": "professional, modern, design-led",
  "goals": ["brand introduction", "lead conversion", "trust building"]
}
```
</details>

> Generate a corporate official website brand-card system using the corporate-website-generator skill.

---

## Input Schemas

**Brand Architect** core fields:

| Field | Required | Description |
| --- | --- | --- |
| `brand_name` | **Yes** | Company, product, campaign, event, IP, or brand name |
| `industry` | No | Industry or category used for brand archaeology |
| `product` | No | What the brand makes, sells, enables, or changes |
| `target_users` | No | Primary audience, buyer, user, tribe, or community |
| `founder_story` | No | Origin story, founding belief, or reason the brand exists |
| `brief` | No | Additional market context, personality, constraints, surfaces, or competitors |
| `competitors` | No | Competitor or adjacent brand names for distance checks |
| `research_depth` | No | `lean` `standard` (default) `deep` |
| `output_mode` | No | `brand-dna` `visual-identity` `brand-guidelines` `full-system` (default) |
| `visual_identity_scope` | No | `strategy-only` `logo-only` `identity-board` `brand-system-board` (default) |
| `target_platform` | No | `gpt-image` `midjourney` `flux` `ideogram` `all` (default) |
| `render_image` | No | Generate an image when an image tool is available |
| `output_language` | No | `zh-CN` (default) or `en` |

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

**Corporate Website** core fields:

| Field | Required | Description |
| --- | --- | --- |
| `company_name` | No | Company name shown as the first-viewport signal |
| `industry` | No | Business category or market |
| `business` | No | Plain-language description of what the company does |
| `target_users` | No | Visitors, buyers, users, or decision makers |
| `core_value` | No | What users can get from the company |
| `brand_tone` | No | Desired corporate tone |
| `preferences` | No | Visual or content preferences |
| `dislikes` | No | Styles, phrases, or patterns to avoid |
| `goals` | No | Website goals such as trust, leads, hiring, sales, or investor credibility |

Full schemas: [`orchestrator`](skills/brand-orchestrator/input-schema.json) · [`roles`](skills/brand-agent-roles/input-schema.json) · [`architect`](skills/brand-architect/input-schema.json) · [`base`](skills/base-logo-generator/input-schema.json) · [`mascot`](skills/mascot-logo-generator/input-schema.json) · [`colorway`](skills/logo-colorway-generator/input-schema.json) · [`copy`](skills/content-copy-validator/input-schema.json) · [`typography`](skills/typography-system-designer/input-schema.json) · [`typography-consultant`](skills/japanese-typography-consultant/input-schema.json) · [`website`](skills/corporate-website-generator/input-schema.json)

---

## Project Layout

```text
logo-generator-skill/
├── skill.sh                          # Skill path resolver
├── skills/
│   ├── llms.txt                      # Machine-readable skill index
│   ├── brand-orchestrator/
│   │   ├── SKILL.md                  # Multi-agent workflow controller
│   │   ├── prompt.md                 # Delegation, gates, synthesis, QA
│   │   └── input-schema.json
│   ├── brand-agent-roles/
│   │   ├── SKILL.md                  # Subagent role system entry point
│   │   ├── prompt.md                 # Role cards and output contracts
│   │   └── input-schema.json
│   ├── brand-architect/
│   │   ├── SKILL.md                  # Brand DNA workflow entry point
│   │   ├── prompt.md                 # Detailed phase rules & scoring engines
│   │   └── input-schema.json
│   ├── base-logo-generator/
│   │   ├── SKILL.md                  # Skill entry point
│   │   ├── prompt.md                 # Detailed style & output rules
│   │   ├── input-schema.json
│   │   └── assets/                   # Example boards & keyframes
│   ├── mascot-logo-generator/
│   │   ├── SKILL.md · prompt.md · input-schema.json · assets/
│   ├── logo-colorway-generator/
│   │   ├── SKILL.md · prompt.md · input-schema.json · assets/
│   ├── content-copy-validator/
│   │   ├── SKILL.md · prompt.md · input-schema.json
│   ├── typography-system-designer/
│   │   ├── SKILL.md · prompt.md · input-schema.json
│   ├── japanese-typography-consultant/
│   │   ├── SKILL.md · prompt.md · input-schema.json
│   ├── corporate-website-generator/
│   │   ├── SKILL.md · prompt.md · input-schema.json
│   ├── corporate_website_skill.py  # Runtime implementation
│   ├── social_media_skill.py       # Runtime implementation
│   └── skill_router.py             # Runtime router
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## FAQ

**Does it only generate prompts?**

No. This branch can output website structure, design briefs, asset directories, static HTML/CSS templates, and preview images. Prompts are only supporting artifacts for visual asset generation.

**Why not a generic landing page?**

Because the goal is not to stack marketing components. The website must explain the company's brand, business, tone, and benefit in the first viewport, then turn that recognition into trust and conversion.

**Are the logo skills still useful?**

Yes, but they are no longer the promotional focus. Logo, colorway, and Brand DNA are upstream brand assets that support website identity, first-screen recognition, and visual extension.

## License

[MIT](LICENSE) · Copyright (c) 2026 SanbaoAI
