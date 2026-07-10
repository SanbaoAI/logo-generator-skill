"""Task router for Design Skill Runtime."""

from __future__ import annotations

from typing import Any

from skills.base_skill import BaseSkill
from skills.corporate_website_skill import CorporateWebsiteSkill
from skills.social_media_skill import SocialMediaSkill


class PlaceholderSkill(BaseSkill):
    """Lightweight adapter for skills that still live as prompt-only Agent Skills."""

    def __init__(self, skill_name: str) -> None:
        self.skill_name = skill_name

    def run(self, input_data: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
        return {
            "asset_id": f"{self.skill_name}_draft",
            "type": self.skill_name,
            "summary": input_data.get("request", ""),
            "status": "routed",
            "message": f"Request routed to {self.skill_name}.",
        }


def route(request: str) -> str:
    normalized = request.lower()
    if (
        "website" in normalized
        or "official site" in normalized
        or "homepage" in normalized
        or "官网" in request
        or "企业名片" in request
        or "品牌名片" in request
    ):
        return "corporate_website_skill"
    if "ppt" in normalized or "powerpoint" in normalized or "slides" in normalized:
        return "ppt_skill"
    if "poster" in normalized or "海报" in request:
        return "poster_skill"
    if (
        "social" in normalized
        or "instagram" in normalized
        or "twitter" in normalized
        or "xiaohongshu" in normalized
        or "小红书" in request
        or "宣传图" in request
    ):
        return "social_media_skill"
    return "logo_skill"


def create_skill(skill_name: str) -> BaseSkill:
    if skill_name == "corporate_website_skill":
        return CorporateWebsiteSkill()
    if skill_name == "social_media_skill":
        return SocialMediaSkill()
    return PlaceholderSkill(skill_name)
