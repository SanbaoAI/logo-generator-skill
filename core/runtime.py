"""Executable Design Skill Runtime pipeline."""

from __future__ import annotations

from typing import Any

from core.critic_agent import CriticAgent
from core.memory_writer import save_memory
from core.prompt_compiler import PromptContext, build_prompt
from skills.skill_router import create_skill, route


class DesignSkillRuntime:
    """Route a request, compile prompt context, run the skill, critique, then save memory."""

    def __init__(self, critic: CriticAgent | None = None) -> None:
        self.critic = critic or CriticAgent()

    def run(
        self,
        request: str,
        input_data: dict[str, Any] | None = None,
        memory: dict[str, Any] | None = None,
        last_design: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        input_data = dict(input_data or {})
        input_data.setdefault("request", request)
        memory = memory or {}

        selected_skill = route(request)
        prompt_context = build_prompt(
            PromptContext(
                brand_memory=memory,
                last_design=last_design,
                scene=input_data.get("scene", {}),
                task={"request": request, **input_data},
            )
        )

        skill = create_skill(selected_skill)
        output = skill.run(input_data=prompt_context["task"], memory=memory)
        output["skill"] = selected_skill
        output["prompt_context"] = prompt_context

        critique = self.critic.evaluate(output, memory)
        asset = {
            "asset_id": output.get("asset_id", f"{selected_skill}_draft"),
            "type": output.get("type", selected_skill),
            "summary": output.get("summary", request),
            "styled_plan": output.get("styled_plan", {}),
        }

        return {
            "skill": selected_skill,
            "prompt": prompt_context,
            "output": output,
            "critique": critique,
            "memory": save_memory(asset, memory),
        }
