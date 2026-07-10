"""Social media content generation skill."""

from __future__ import annotations

from typing import Any

from skills.base_skill import BaseSkill


PLATFORM_ADAPTERS: dict[str, dict[str, Any]] = {
    "xiaohongshu": {"title_strength": "high", "emotion": "strong", "ratio": "3:4"},
    "instagram": {"minimalism": True, "emotion": "polished", "ratio": "4:5"},
    "twitter": {"density": "low", "emotion": "direct", "ratio": "16:9"},
}


class SocialMediaSkill(BaseSkill):
    """Convert brand DNA and content input into publishable social visuals."""

    def run(self, input_data: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
        content = self.interpret_content(input_data)
        layout_plan = self.plan_layout(content)
        styled_plan = self.inject_brand_dna(layout_plan, memory)
        assets = self.generate_assets(styled_plan)
        platform = self.detect_platform(input_data)
        final_output = self.platform_adapter(assets, platform)

        return {
            "asset_id": f"{platform}_carousel_v1",
            "type": "social_media_carousel",
            "summary": f"{platform} carousel: {content['core_message']}",
            "platform": platform,
            "content": content,
            "layout": layout_plan,
            "styled_plan": styled_plan,
            "assets": assets,
            "final_output": final_output,
        }

    def interpret_content(self, input_data: dict[str, Any]) -> dict[str, str]:
        request = input_data.get("request") or input_data.get("brief") or ""
        product = input_data.get("product") or "AI tool"
        audience = input_data.get("audience") or input_data.get("target_users") or "creators and product teams"

        emotion = input_data.get("emotion") or ("strong" if "小红书" in request else "confident")
        cta = input_data.get("cta") or "Try it today"

        return {
            "core_message": input_data.get("core_message") or self._core_message(request, product),
            "emotion": emotion,
            "audience": audience,
            "cta": cta,
        }

    def plan_layout(self, content: dict[str, str]) -> dict[str, Any]:
        return {
            "format": "carousel",
            "slides": 5,
            "structure": ["hook", "problem", "solution", "product", "cta"],
            "slide_goals": [
                f"Lead with a sharp hook around {content['core_message']}",
                "Name the current pain or bottleneck",
                "Show the transformation or method",
                "Introduce the product proof and key benefit",
                f"Close with CTA: {content['cta']}",
            ],
        }

    def inject_brand_dna(
        self,
        layout_plan: dict[str, Any],
        memory: dict[str, Any],
    ) -> dict[str, Any]:
        dna = memory.get("visual_dna", {})
        style_rules = memory.get("style_rules", {})

        return {
            **layout_plan,
            "geometry": dna.get("geometry", "rounded"),
            "emotion": dna.get("emotion", "friendly"),
            "colors": {
                "primary": dna.get("primary_color", "#2563EB"),
                "secondary": dna.get("secondary_color", "#F97316"),
            },
            "keywords": dna.get("keywords", ["node", "flow", "minimal"]),
            "complexity": style_rules.get("complexity", 0.4),
            "symmetry": style_rules.get("symmetry", "centered"),
            "layout_preference": style_rules.get("layout_preference", "centered"),
        }

    def generate_assets(self, styled_plan: dict[str, Any]) -> dict[str, Any]:
        slides = []
        for index, section in enumerate(styled_plan["structure"], start=1):
            slides.append(
                {
                    "slide": index,
                    "role": section,
                    "visual_direction": self._visual_direction(section, styled_plan),
                    "prompt_fragment": self._prompt_fragment(section, styled_plan),
                }
            )

        return {
            "format": styled_plan["format"],
            "slides": slides,
            "generation_engine": "image_or_layout",
        }

    def platform_adapter(self, assets: dict[str, Any], platform: str) -> dict[str, Any]:
        adapter = PLATFORM_ADAPTERS.get(platform, PLATFORM_ADAPTERS["instagram"])
        return {
            "platform": platform,
            "adapter": adapter,
            "publish_ready": True,
            "asset_spec": {
                "format": assets["format"],
                "slide_count": len(assets["slides"]),
                "ratio": adapter.get("ratio", "4:5"),
            },
            "slides": assets["slides"],
        }

    def detect_platform(self, input_data: dict[str, Any]) -> str:
        platform = str(input_data.get("platform", "")).lower()
        request = str(input_data.get("request", "")).lower()
        if platform:
            return "xiaohongshu" if platform in {"小红书", "xhs"} else platform
        if "小红书" in input_data.get("request", "") or "xiaohongshu" in request:
            return "xiaohongshu"
        if "twitter" in request or "x.com" in request:
            return "twitter"
        return "instagram"

    def _core_message(self, request: str, product: str) -> str:
        if request:
            return request.replace("帮我做一个", "").strip() or product
        return f"Launch {product} with a clear, memorable story"

    def _visual_direction(self, section: str, styled_plan: dict[str, Any]) -> str:
        return (
            f"{section} slide using {styled_plan['geometry']} geometry, "
            f"{styled_plan['emotion']} emotion, primary {styled_plan['colors']['primary']}"
        )

    def _prompt_fragment(self, section: str, styled_plan: dict[str, Any]) -> str:
        keywords = ", ".join(styled_plan.get("keywords", [])[:4])
        return (
            f"{section} carousel slide, {styled_plan['layout_preference']} layout, "
            f"{keywords}, clean hierarchy, publish-ready social media visual"
        )
