"""Brand memory update helpers."""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any


def save_memory(asset: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
    """Return updated brand memory with asset history and refined visual DNA."""

    updated = deepcopy(memory)
    updated.setdefault("history", [])
    updated["history"].append(
        {
            "asset_id": asset.get("asset_id", "asset_unknown"),
            "type": asset.get("type", "unknown"),
            "summary": asset.get("summary", ""),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    updated["visual_dna"] = update_dna(asset, updated)
    return updated


def update_dna(asset: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
    dna = deepcopy(memory.get("visual_dna", {}))
    styled_plan = asset.get("styled_plan", {})
    colors = styled_plan.get("colors", {})

    if colors.get("primary"):
        dna["primary_color"] = colors["primary"]
    if colors.get("secondary"):
        dna["secondary_color"] = colors["secondary"]
    if styled_plan.get("geometry"):
        dna["geometry"] = styled_plan["geometry"]
    if styled_plan.get("emotion"):
        dna["emotion"] = styled_plan["emotion"]

    keywords = list(dict.fromkeys(dna.get("keywords", []) + styled_plan.get("keywords", [])))
    if keywords:
        dna["keywords"] = keywords[:12]

    return dna
