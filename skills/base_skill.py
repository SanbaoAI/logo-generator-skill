"""Base class for Design Skill Runtime skills."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseSkill(ABC):
    @abstractmethod
    def run(self, input_data: dict[str, Any], memory: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
