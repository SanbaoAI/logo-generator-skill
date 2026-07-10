"""Corporate website brand card generation skill."""

from __future__ import annotations

from typing import Any

from skills.base_skill import BaseSkill


ROLE_SEQUENCE = [
    "product_manager",
    "content_copy_validator",
    "design_director",
    "brand_designer",
    "color_designer",
    "typography_designer",
    "japanese_typography_consultant",
    "visual_asset_designer",
    "ui_designer",
]


class CorporateWebsiteSkill(BaseSkill):
    """Turn a company brief into a role-based corporate website design package."""

    def run(self, input_data: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
        brief = self.build_product_brief(input_data)
        content_validation = self.validate_content_copy(input_data, brief)
        strategy = self.plan_design_direction(brief, content_validation)
        brand_system = self.plan_brand_design(brief, strategy)
        color_system = self.plan_color_system(input_data, memory, strategy)
        typography_system = self.plan_typography_system(input_data, brief, strategy)
        typography_consultant = self.consult_japanese_typography(input_data, brief, strategy, typography_system)
        visual_assets = self.plan_visual_assets(brief, strategy, color_system)
        ui_design = self.plan_ui_design(
            brief, strategy, brand_system, color_system, typography_system, typography_consultant
        )
        delivery = self.plan_delivery_tree(brief)
        review = self.design_director_review(
            brief, strategy, brand_system, color_system, typography_system, typography_consultant, ui_design
        )

        styled_plan = {
            "geometry": strategy["visual_language"]["geometry"],
            "emotion": strategy["visual_language"]["tone"],
            "colors": {
                "primary": color_system["tokens"]["primary"],
                "secondary": color_system["tokens"]["accent"],
            },
            "keywords": strategy["brand_impression"][:6],
            "layout_preference": ui_design["layout_system"]["composition"],
            "typography": typography_system["type_scale"]["desktop"],
        }

        return {
            "asset_id": f"{self._slug(brief['company_name'])}_corporate_website_v1",
            "type": "corporate_website_brand_card",
            "summary": f"{brief['company_name']} corporate website design package",
            "content": {
                "core_message": strategy["first_viewport"]["one_sentence_value"],
                "cta": strategy["first_viewport"]["primary_cta"],
                "company_name": brief["company_name"],
            },
            "roles": ROLE_SEQUENCE,
            "product_manager": brief,
            "content_validation": content_validation,
            "design_director": strategy,
            "brand_design": brand_system,
            "color_design": color_system,
            "typography_design": typography_system,
            "typography_consultant": typography_consultant,
            "visual_assets": visual_assets,
            "ui_design": ui_design,
            "layout": ui_design["page_structure"],
            "styled_plan": styled_plan,
            "output_directories": delivery,
            "quality_gates": review,
            "final_output": {
                "delivery_ready": True,
                "directory_separated": True,
                "website_template_ready": True,
            },
        }

    def build_product_brief(self, input_data: dict[str, Any]) -> dict[str, Any]:
        request = str(input_data.get("request", ""))
        company_name = input_data.get("company_name") or input_data.get("brand_name") or "Example Company"
        industry = input_data.get("industry") or self._infer_industry(request)
        business = input_data.get("business") or input_data.get("product") or self._infer_business(industry)
        audience = input_data.get("audience") or input_data.get("target_users") or self._infer_audience(industry)
        core_value = input_data.get("core_value") or self._infer_core_value(industry, business)
        tone = input_data.get("tone") or input_data.get("brand_tone") or self._infer_tone(industry)
        preferences = input_data.get("preferences") or input_data.get("visual_preferences") or [
            "clear first-screen positioning",
            "premium but direct corporate credibility",
            "business-relevant visuals instead of generic decoration",
        ]
        dislikes = input_data.get("dislikes") or ["empty slogans", "generic AI gradients", "unclear business category"]
        goals = input_data.get("goals") or ["brand introduction", "lead conversion", "trust building"]

        return {
            "role": "Product Manager",
            "company_name": str(company_name),
            "industry": str(industry),
            "business": str(business),
            "target_users": str(audience),
            "core_value": str(core_value),
            "brand_tone": str(tone),
            "preferences": preferences,
            "dislikes": dislikes,
            "website_goals": goals,
            "intake_questions": [
                "What does the company sell or deliver in one plain sentence?",
                "Who must understand and trust the company in the first 5 seconds?",
                "What proof, result, or capability should the hero section make visible?",
                "Which visual styles feel wrong for this company?",
                "What should the visitor do after understanding the company?",
            ],
            "pm_summary": (
                f"{company_name} needs a corporate brand-card website that immediately communicates "
                f"{business}, serves {audience}, and turns {core_value} into a visible promise."
            ),
        }

    def validate_content_copy(self, input_data: dict[str, Any], brief: dict[str, Any]) -> dict[str, Any]:
        requested_terms = input_data.get("terms") or ["AI", "FDE", "AIGC", "Hermes Agent"]
        corrections = []
        if "FDE" in requested_terms or "FDE" in str(input_data.get("request", "")) or "FDE" in brief["business"]:
            corrections.append(
                {
                    "term": "FDE",
                    "approved": "Forward Deployed Engineer / Forward Deployed Engineering",
                    "avoid": "Field Deployment Engineering",
                    "rule": "Use Engineer for the role/person and Engineering for the practice.",
                }
            )

        return {
            "role": "Content Copy Validator",
            "terminology_review": {
                "approved_terms": {
                    "FDE": "Forward Deployed Engineer / Forward Deployed Engineering",
                    "AIGC": "AI-generated content",
                    "Hermes Agent": "task orchestration agent system",
                },
                "corrections": corrections,
            },
            "fact_and_claim_review": [
                "Avoid unsupported superlatives or absolute claims.",
                "Tie AI capability claims to deployable workflows, governance, observability, and operating metrics.",
            ],
            "naming_consistency": [
                "Use SanBaoTech for the English brand name and 三宝国 for the Chinese name.",
                "Use Hermes Agent consistently for the agent engineering line.",
            ],
            "chinese_copy_review": [
                "Keep primary value propositions in direct Chinese.",
                "Use precise business verbs: 部署, 运营, 评估, 监控, 迭代.",
            ],
            "mixed_language_review": [
                "Expand acronyms on first use when space allows.",
                "Use English labels for technical surfaces, not as decorative filler.",
            ],
            "cta_review": "Prefer concrete CTA language such as 从一个流程开始 or 部署第一条流程.",
            "approved_copy_rules": [
                "FDE first-use expansion should be Forward Deployed Engineer or Forward Deployed Engineering.",
                "Do not describe FDE as Field Deployment Engineering.",
                "Do not imply fully autonomous operation without human approval or governance.",
            ],
            "corrections_required": bool(corrections),
        }

    def plan_design_direction(self, brief: dict[str, Any], content_validation: dict[str, Any]) -> dict[str, Any]:
        one_sentence_value = (
            f"{brief['company_name']} helps {brief['target_users']} get {brief['core_value']} through {brief['business']}."
        )
        return {
            "role": "Design Director",
            "design_thesis": (
                "Build the official website as a digital corporate name card: company identity, business category, "
                "tone, benefit, and proof must be understood before the visitor scrolls."
            ),
            "first_viewport": {
                "must_show": [
                    "company name",
                    "industry category",
                    "core business",
                    "target user",
                    "main benefit",
                    "representative brand visual",
                ],
                "one_sentence_value": one_sentence_value,
                "primary_cta": "Start a brand conversation",
                "secondary_cta": "View capabilities",
            },
            "brand_impression": [
                "clear",
                "credible",
                "specific",
                "modern",
                brief["brand_tone"],
                brief["industry"],
            ],
            "visual_language": {
                "geometry": "structured editorial grid",
                "tone": brief["brand_tone"],
                "density": "medium-high information clarity",
                "imagery_rule": "show business-specific systems, products, or service outcomes",
            },
            "page_narrative": [
                "Who we are",
                "What we do",
                "What you get",
                "How the system works",
                "Proof and scenarios",
                "Contact or start",
            ],
            "checkpoints": [
                "Can a first-time visitor name the industry within 3 seconds?",
                "Does the hero show a concrete benefit instead of an abstract slogan?",
                "Do brand, color, assets, and UI share one visual logic?",
                "Did content validation approve terminology, claims, and CTA wording?",
                "Are icons, illustrations, and backgrounds stored as separate deliverables?",
                "Is the page useful as a reusable corporate website template?",
            ],
            "content_dependencies": content_validation["approved_copy_rules"],
        }

    def plan_brand_design(self, brief: dict[str, Any], strategy: dict[str, Any]) -> dict[str, Any]:
        symbol_anchor = self._symbol_anchor(brief["industry"])
        return {
            "role": "Brand Designer",
            "identity_goal": "Make the company recognizable as a business before the visitor reads long copy.",
            "logo_direction": {
                "mark": f"abstract {symbol_anchor} symbol tied to {brief['business']}",
                "wordmark": "clean corporate wordmark with strong small-size readability",
                "lockups": ["horizontal", "stacked", "icon-only", "favicon"],
            },
            "brand_assets": [
                "primary logo",
                "secondary logo",
                "favicon",
                "app icon",
                "social avatar",
                "brand pattern",
                "business capability icons",
            ],
            "homepage_identity_rules": [
                "Place the company name as the first viewport signal, not only in nav.",
                "Pair the logo with an industry descriptor.",
                "Use one strong representative brand visual near the value proposition.",
            ],
            "asset_prompts": [
                f"Create a premium corporate logo for {brief['company_name']}, {brief['industry']}, using {symbol_anchor} as the symbolic base.",
                f"Create favicon and app icon variants preserving the {symbol_anchor} silhouette.",
            ],
        }

    def plan_color_system(
        self,
        input_data: dict[str, Any],
        memory: dict[str, Any],
        strategy: dict[str, Any],
    ) -> dict[str, Any]:
        dna = memory.get("visual_dna", {})
        preferred = input_data.get("colors") or {}
        primary = preferred.get("primary") if isinstance(preferred, dict) else None
        accent = preferred.get("accent") if isinstance(preferred, dict) else None
        primary = primary or dna.get("primary_color") or "#2563EB"
        accent = accent or dna.get("secondary_color") or "#F97316"

        return {
            "role": "Color Designer",
            "color_strategy": "Use color as a business signal: category recognition first, decorative expression second.",
            "tokens": {
                "primary": primary,
                "accent": accent,
                "background": "#F8FAFC",
                "surface": "#FFFFFF",
                "text": "#111827",
                "muted_text": "#64748B",
                "border": "#CBD5E1",
            },
            "usage": {
                "primary": "logo, hero proof visual, primary CTA, active states",
                "accent": "important metrics, conversion highlights, small visual hooks",
                "background": "large page bands and calm reading areas",
                "text": "headlines and business-critical statements",
            },
            "accessibility_rules": [
                "Do not place low-contrast text over illustration backgrounds.",
                "Reserve accent color for one decision point per section.",
                "Check light and dark theme token contrast before final delivery.",
            ],
            "director_alignment": f"Palette supports a {strategy['visual_language']['tone']} but business-readable website.",
        }

    def plan_visual_assets(
        self,
        brief: dict[str, Any],
        strategy: dict[str, Any],
        color_system: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "role": "Visual Asset Designer",
            "asset_principle": "Every visual asset must help users understand the company, not decorate the page.",
            "icons": [
                {"name": "business-category", "purpose": "show what the company does"},
                {"name": "core-value", "purpose": "show the promised user benefit"},
                {"name": "process", "purpose": "show how the service works"},
                {"name": "delivery", "purpose": "show what the user receives"},
            ],
            "illustrations": [
                {
                    "name": "hero-capability-scene",
                    "brief": f"{brief['company_name']} delivering {brief['core_value']} for {brief['target_users']}",
                },
                {
                    "name": "system-output-board",
                    "brief": "modular overview of logo, color, UI, and business touchpoints",
                },
            ],
            "backgrounds": [
                {
                    "name": "hero-background",
                    "style": f"quiet {strategy['visual_language']['geometry']} using {color_system['tokens']['primary']} as signal color",
                },
                {"name": "section-grid", "style": "subtle structured grid for capability sections"},
            ],
            "mockups": ["homepage first viewport", "mobile hero", "business card", "social profile", "capability page"],
            "file_rules": [
                "Store icons separately from illustrations.",
                "Store backgrounds separately from page screenshots.",
                "Name assets by role and usage surface.",
            ],
        }

    def plan_typography_system(
        self,
        input_data: dict[str, Any],
        brief: dict[str, Any],
        strategy: dict[str, Any],
    ) -> dict[str, Any]:
        language = input_data.get("language") or "mixed"
        density = input_data.get("body_copy_density") or "medium"
        return {
            "role": "Typography Designer",
            "typography_strategy": (
                "Use a deliberate mixed Chinese-English system: strong sans-serif headlines for technology credibility, "
                "short English system labels for AI surfaces, and readable Chinese body copy for business clarity."
            ),
            "font_roles": {
                "display": "system sans, heavy weight, tight but non-overlapping line breaks",
                "heading": "system sans, semibold to bold, clear section rhythm",
                "body": "system sans, regular, controlled line length",
                "label": "compact uppercase or short bilingual labels, no extra letter spacing",
                "numeric": "tabular-style metrics when available",
                "console": "monospace only for real system states, logs, and command-like text",
            },
            "type_scale": {
                "desktop": {
                    "hero": "72-128px with planned line breaks",
                    "hero_statement": "30-48px",
                    "section_heading": "44-92px",
                    "body": "16-18px",
                    "label": "11-13px",
                },
                "mobile": {
                    "hero": "48-70px",
                    "hero_statement": "24-28px",
                    "section_heading": "34-48px",
                    "body": "15-17px",
                    "label": "11-12px",
                },
            },
            "mixed_language_rules": [
                "Do not force long Chinese and English brand names onto one line when a hero visual sits beside them.",
                "Use English for product/system labels only when the surrounding Chinese copy explains the business value.",
                "Keep Chinese paragraphs within comfortable line lengths and avoid dense multi-clause blocks in cards.",
                "Use 0 letter spacing by default for implementation safety.",
            ],
            "hero_typography": {
                "headline": brief["company_name"],
                "supporting_statement": strategy["first_viewport"]["one_sentence_value"],
                "line_break_rule": "break brand name, category statement, and value proposition into separate typographic roles",
            },
            "density": density,
            "language": language,
            "qa": [
                "Hero headline does not overlap the product visual.",
                "Mobile headline breaks remain intentional.",
                "Console labels are legible and not decorative filler.",
                "CTA hierarchy is visible within 5 seconds.",
                "Chinese and English text feel like one system.",
            ],
        }

    def consult_japanese_typography(
        self,
        input_data: dict[str, Any],
        brief: dict[str, Any],
        strategy: dict[str, Any],
        typography_system: dict[str, Any],
    ) -> dict[str, Any]:
        density = input_data.get("layout_density") or "balanced"
        return {
            "role": "Japanese Typography Consultant",
            "consultant_diagnosis": (
                "Treat Chinese headlines as composed visual blocks, not just text strings. "
                "Use Japanese-inspired spacing discipline, semantic line breaks, and quiet body copy to reduce noise."
            ),
            "principles_applied": [
                "ma: preserve meaningful empty space around the key value statement",
                "kata: align labels, titles, and body copy to a visible grid",
                "headline-as-object: split long mixed-script headlines into controlled blocks",
                "quiet-body: reduce dense paragraphs inside cards and dark panels",
                "mixed-script hierarchy: English labels support Chinese meaning, not compete with it",
            ],
            "headline_line_break_advice": {
                "hero": "separate brand name, core statement, and explanatory body into three typographic layers",
                "section": "prefer 2-3 short semantic lines over one long headline",
                "avoid": "long Chinese-English headline strings beside large visuals",
            },
            "spacing_and_grid_advice": [
                "Increase space before major section titles so headings feel intentional.",
                "Use tighter internal card rhythm but larger section-to-section breathing room.",
                "Align short labels to the same left edge as the headline or content column.",
            ],
            "mixed_script_advice": [
                "Keep English labels short: AI Stack, FDE, Hermes, Trust.",
                "Use Chinese for primary business value and user benefit.",
                "Avoid uppercase labels with extra letter spacing in compact UI.",
            ],
            "component_text_advice": [
                "Console text should look operational: short labels, fixed rhythm, readable contrast.",
                "Capability cards should use short body copy and strong section numbers.",
                "CTA text should be action-specific, not generic consultation language.",
            ],
            "mobile_typography_advice": [
                "Preserve semantic line breaks on mobile.",
                "Avoid stacking too many tiny English labels before the Chinese value statement.",
                "Keep body paragraphs under 4 lines where possible.",
            ],
            "density": density,
            "qa": typography_system["qa"]
            + [
                "Japanese-inspired spacing creates calm rather than emptiness.",
                "Section titles have visible rhythm and do not feel randomly oversized.",
            ],
        }

    def plan_ui_design(
        self,
        brief: dict[str, Any],
        strategy: dict[str, Any],
        brand_system: dict[str, Any],
        color_system: dict[str, Any],
        typography_system: dict[str, Any],
        typography_consultant: dict[str, Any],
    ) -> dict[str, Any]:
        sections = strategy["page_narrative"]
        return {
            "role": "UI Designer",
            "layout_system": {
                "composition": "left identity statement, right representative visual, below-the-fold capability preview",
                "grid": "12-column desktop, 4-column mobile",
                "spacing": "compact corporate rhythm with generous section breaks",
                "component_radius": "8px or less",
            },
            "page_structure": {
                "format": "corporate official website",
                "sections": len(sections),
                "structure": sections,
                "hero": {
                    "headline": brief["company_name"],
                    "descriptor": f"{brief['industry']} / {brief['business']}",
                    "value": strategy["first_viewport"]["one_sentence_value"],
                    "proof_visual": "hero-capability-scene",
                    "cta": strategy["first_viewport"]["primary_cta"],
                },
            },
            "components": [
                "navigation",
                "hero identity block",
                "capability strip",
                "deliverables grid",
                "process timeline",
                "proof metrics",
                "contact CTA",
            ],
            "interaction_notes": [
                "Use tabs or segmented controls for industry/capability variants.",
                "Keep CTA labels action-based and business-specific.",
                "On mobile, show company name, descriptor, value, and CTA before any decorative visual.",
            ],
            "brand_asset_dependencies": brand_system["brand_assets"],
            "color_dependencies": color_system["tokens"],
            "typography_dependencies": typography_system["font_roles"],
            "typography_consultant_dependencies": typography_consultant["headline_line_break_advice"],
        }

    def plan_delivery_tree(self, brief: dict[str, Any]) -> dict[str, Any]:
        slug = self._slug(brief["company_name"])
        base = f"outputs/{slug}/"
        return {
            "base": base,
            "directories": [
                f"{base}01-product-brief/",
                f"{base}02-content-validation/",
                f"{base}03-design-direction/",
                f"{base}04-brand-design/logo/",
                f"{base}04-brand-design/icons/",
                f"{base}05-color-system/",
                f"{base}06-typography-system/",
                f"{base}07-typography-consultant/",
                f"{base}08-visual-assets/icons/",
                f"{base}08-visual-assets/illustrations/",
                f"{base}08-visual-assets/backgrounds/",
                f"{base}08-visual-assets/mockups/",
                f"{base}09-ui-design/wireframes/",
                f"{base}09-ui-design/high-fidelity/",
                f"{base}09-ui-design/components/",
                f"{base}10-website-template/assets/",
                f"{base}11-final-review/",
            ],
            "expected_files": [
                "01-product-brief/company-profile.md",
                "01-product-brief/pm-summary.json",
                "02-content-validation/copy-review.md",
                "03-design-direction/design-strategy.md",
                "04-brand-design/logo-directions.md",
                "05-color-system/color-tokens.json",
                "06-typography-system/type-system.md",
                "07-typography-consultant/consultant-review.md",
                "08-visual-assets/asset-manifest.json",
                "09-ui-design/page-structure.md",
                "10-website-template/index.html",
                "11-final-review/design-director-review.md",
            ],
        }

    def design_director_review(
        self,
        brief: dict[str, Any],
        strategy: dict[str, Any],
        brand_system: dict[str, Any],
        color_system: dict[str, Any],
        typography_system: dict[str, Any],
        typography_consultant: dict[str, Any],
        ui_design: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "role": "Design Director",
            "decision": "approved_for_template_production",
            "checks": [
                {"item": "company identity visible in first viewport", "status": "pass"},
                {"item": "business category stated plainly", "status": "pass"},
                {"item": "user benefit is explicit", "status": "pass"},
                {"item": "brand, color, assets, and UI have separated deliverables", "status": "pass"},
                {"item": "typography system is defined before UI production", "status": "pass"},
                {"item": "typography consultant reviewed spacing and Chinese line breaks", "status": "pass"},
                {"item": "visual assets are tied to business meaning", "status": "pass"},
            ],
            "revision_notes": [
                f"Keep {brief['company_name']} as the main first-screen signal.",
                f"Use {color_system['tokens']['primary']} consistently for identity and conversion.",
                f"Use typography rule: {typography_system['hero_typography']['line_break_rule']}.",
                f"Apply consultant advice: {typography_consultant['headline_line_break_advice']['section']}.",
                f"Do not allow {brand_system['logo_direction']['mark']} to become a generic decorative mark.",
                f"Validate that {ui_design['page_structure']['hero']['descriptor']} remains readable on mobile.",
            ],
            "next_step": "Generate high-fidelity website design and separated asset folders.",
            "director_summary": strategy["design_thesis"],
        }

    def _infer_industry(self, request: str) -> str:
        if "品牌" in request or "logo" in request.lower() or "设计" in request:
            return "AI brand design"
        if "健身" in request or "fitness" in request.lower():
            return "fitness technology"
        if "教育" in request or "education" in request.lower():
            return "education technology"
        return "professional service technology"

    def _infer_business(self, industry: str) -> str:
        if "brand" in industry.lower() or "品牌" in industry:
            return "AI-assisted brand identity and official website design"
        return "specialized digital service delivery"

    def _infer_audience(self, industry: str) -> str:
        if "brand" in industry.lower() or "品牌" in industry:
            return "founders, product teams, and growing companies"
        return "business decision makers"

    def _infer_core_value(self, industry: str, business: str) -> str:
        if "brand" in industry.lower() or "品牌" in industry:
            return "a clear, credible, and reusable company identity"
        return f"trusted results from {business}"

    def _infer_tone(self, industry: str) -> str:
        if "brand" in industry.lower() or "设计" in industry:
            return "professional, modern, design-led"
        return "credible, modern, direct"

    def _symbol_anchor(self, industry: str) -> str:
        normalized = industry.lower()
        if "brand" in normalized or "设计" in industry:
            return "modular identity frame"
        if "fitness" in normalized or "健身" in industry:
            return "movement signal"
        if "education" in normalized or "教育" in industry:
            return "learning pathway"
        return "precision system mark"

    def _slug(self, value: str) -> str:
        slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
        while "--" in slug:
            slug = slug.replace("--", "-")
        return slug or "company"
