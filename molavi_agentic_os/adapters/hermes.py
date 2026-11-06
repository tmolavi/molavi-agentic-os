"""Hermes Agent Skill Adapter."""

import json
from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class HermesAdapter(PlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "hermes"

    def export_agent(self, agent: AgentDefinition) -> str:
        data = {
            "hermes_agent_version": "1.0",
            "id": agent.metadata.id,
            "name": agent.metadata.name,
            "role": agent.metadata.role,
            "system_prompt": agent.system_instructions,
            "skills": agent.required_skills
        }
        return json.dumps(data, indent=2)

    def export_skill(self, skill: SkillDefinition) -> str:
        return skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        return team.to_json()
