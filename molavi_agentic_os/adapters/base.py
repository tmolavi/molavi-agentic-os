"""Base Platform Adapter for cross-environment compatibility."""

from abc import ABC, abstractmethod
from typing import Dict, Any
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class PlatformAdapter(ABC):
    @property
    @abstractmethod
    def platform_name(self) -> str:
        pass

    @abstractmethod
    def export_agent(self, agent: AgentDefinition) -> str:
        pass

    @abstractmethod
    def export_skill(self, skill: SkillDefinition) -> str:
        pass

    @abstractmethod
    def export_team(self, team: TeamDefinition) -> str:
        pass
