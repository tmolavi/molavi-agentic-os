"""Antigravity Platform Adapter."""

from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class AntigravityAdapter(PlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "antigravity"

    def export_agent(self, agent: AgentDefinition) -> str:
        return f"""# Antigravity Subagent Configuration: {agent.metadata.name}
Role: {agent.metadata.role}
Category: {agent.metadata.category}
Permission: {agent.permission_level.value}

## System Prompt
{agent.system_instructions}

## Required Skills
{', '.join(agent.required_skills)}
"""

    def export_skill(self, skill: SkillDefinition) -> str:
        return skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        return team.to_json()
