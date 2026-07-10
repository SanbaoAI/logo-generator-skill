---
name: brand-orchestrator
description: Orchestrate the full AI Brand Architect workflow. Use when the user wants end-to-end brand strategy, subagent delegation, phase gates, synthesis, QA, routing to specialist skills, or final delivery from brand input to visual identity and website outputs.
---

# Brand Orchestrator

Use this skill as the workflow controller for a complete brand project. It does not replace the specialist skills; it decides which specialists should run, what each one must return, how conflicts are resolved, and when the project can move to the next phase.

## Workflow

1. Collect the brand input: name, industry, product, audience, founder story, goals, constraints, deliverables, and preferred output language.
2. Decide the project lane: Brand DNA, logo system, mascot system, colorway, corporate website, copy validation, typography, or full system.
3. Build a specialist roster using `brand-agent-roles` when the project requires subagent-style division of labor.
4. Run phase gates:
   - Strategy gate: the brand meaning and audience are clear.
   - Symbol gate: the identity direction is ownable, simple, and durable.
   - Visual gate: logo, color, type, and assets share one logic.
   - Delivery gate: output files, prompts, QA, and handoff notes are complete.
5. Route work to specialist skills:
   - Use `brand-architect` for Brand DNA and symbolic strategy.
   - Use `base-logo-generator` or `mascot-logo-generator` for logo execution.
   - Use `logo-colorway-generator` for scenario color systems.
   - Use `content-copy-validator` for terminology, claims, naming, Chinese copy, and CTA QA.
   - Use `typography-system-designer` and `japanese-typography-consultant` for mixed Chinese-English typography.
   - Use `corporate-website-generator` for enterprise brand-card official websites.
6. Synthesize specialist outputs into one final delivery with assumptions, decisions, risks, and next steps.

## Output

Return these sections:

- Orchestration Plan
- Specialist Roster
- Delegation Briefs
- Phase Gates
- Routing Decisions
- Integration Matrix
- Final Assembly Checklist
- QA Notes

Read `prompt.md` for detailed templates and decision rules.
