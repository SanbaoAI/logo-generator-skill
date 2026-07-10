"""Quality critic for generated brand visual assets."""

from __future__ import annotations

from typing import Any


class CriticAgent:
    """Scores clarity, brand consistency, and visual balance."""

    def evaluate(
        self,
        output: dict[str, Any],
        memory: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        memory = memory or {}
        issues: list[str] = []

        clarity = self._score_clarity(output, issues)
        brand_consistency = self._score_brand_consistency(output, memory, issues)
        visual_balance = self._score_visual_balance(output, issues)

        return {
            "clarity": clarity,
            "brand_consistency": brand_consistency,
            "visual_balance": visual_balance,
            "issues": issues,
        }

    def _score_clarity(self, output: dict[str, Any], issues: list[str]) -> float:
        content = output.get("content", {})
        core_message = str(content.get("core_message", "")).strip()
        cta = str(content.get("cta", "")).strip()
        slides = output.get("layout", {}).get("slides", 0)
        sections = output.get("layout", {}).get("sections", 0)

        score = 0.5
        if core_message:
            score += 0.25
        else:
            issues.append("missing core message")
        if cta:
            score += 0.15
        else:
            issues.append("missing CTA")
        if slides or sections:
            score += 0.1

        return round(min(score, 1.0), 2)

    def _score_brand_consistency(
        self,
        output: dict[str, Any],
        memory: dict[str, Any],
        issues: list[str],
    ) -> float:
        dna = memory.get("visual_dna", {})
        styled_plan = output.get("styled_plan", {})
        colors = styled_plan.get("colors", {})
        keywords = set(styled_plan.get("keywords", []))
        memory_keywords = set(dna.get("keywords", []))

        score = 0.45
        if colors.get("primary") == dna.get("primary_color"):
            score += 0.25
        else:
            issues.append("primary color not aligned with brand memory")
        if colors.get("secondary") == dna.get("secondary_color"):
            score += 0.15
        if keywords and memory_keywords and keywords.intersection(memory_keywords):
            score += 0.15
        elif memory_keywords:
            issues.append("brand keywords not reflected")

        return round(min(score, 1.0), 2)

    def _score_visual_balance(
        self,
        output: dict[str, Any],
        issues: list[str],
    ) -> float:
        layout = output.get("layout", {})
        structure = layout.get("structure", [])
        slides = int(layout.get("slides", 0) or 0)
        sections = int(layout.get("sections", 0) or 0)

        score = 0.55
        if (slides and slides == len(structure)) or (sections and sections == len(structure)):
            score += 0.2
        else:
            issues.append("layout count does not match structure length")

        if (slides and slides <= 6) or (sections and sections <= 8):
            score += 0.15
        else:
            issues.append("text too dense")

        if output.get("platform") or output.get("type") == "corporate_website_brand_card":
            score += 0.1

        return round(min(score, 1.0), 2)
