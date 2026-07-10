"""Prompt context compiler for memory-based design skills."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class PromptContext:
    """Context packet shared by runtime skills and generation engines."""

    brand_memory: dict[str, Any] = field(default_factory=dict)
    last_design: dict[str, Any] | None = None
    scene: dict[str, Any] = field(default_factory=dict)
    task: dict[str, Any] = field(default_factory=dict)


def build_prompt(context: PromptContext | dict[str, Any]) -> dict[str, Any]:
    """Merge brand memory, previous design, scene context, and task.

    The return value intentionally stays structured. Downstream engines can
    serialize it to prose, JSON, or model-specific prompt formats without
    losing the boundaries between memory, scene, and current task.
    """

    if isinstance(context, dict):
        context = PromptContext(
            brand_memory=context.get("brand_memory", {}) or {},
            last_design=context.get("last_design"),
            scene=context.get("scene", {}) or {},
            task=context.get("task", {}) or {},
        )

    return {
        "brand_memory": context.brand_memory,
        "last_design": context.last_design,
        "scene": context.scene,
        "task": context.task,
    }
