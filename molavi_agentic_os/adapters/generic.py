"""Generic CLI Platform Adapter."""

from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class GenericAdapter(PlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "generic"

    def export_agent(self, agent: AgentDefinition) -> str:
        return agent.to_json()

    def export_skill(self, skill: SkillDefinition) -> str:
        return skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        return team.to_json()
