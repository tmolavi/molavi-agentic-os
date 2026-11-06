"""Claude Code Adapter."""

from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class ClaudeCodeAdapter(PlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "claude-code"

    def export_agent(self, agent: AgentDefinition) -> str:
        return f"""// Claude Code Agent Configuration
export const {agent.metadata.id.replace('-', '_')} = {{
    name: "{agent.metadata.name}",
    role: "{agent.metadata.role}",
    instructions: `{agent.system_instructions}`
}};
"""

    def export_skill(self, skill: SkillDefinition) -> str:
        return skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        return team.to_json()
