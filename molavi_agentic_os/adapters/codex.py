"""OpenAI Codex / Cursor Rules Adapter."""

from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition

class CodexAdapter(PlatformAdapter):
    @property
    def platform_name(self) -> str:
        return "codex"

    def export_agent(self, agent: AgentDefinition) -> str:
        return f"""# Codex / Cursor Instruction Rule: {agent.metadata.name}
<!-- role: {agent.metadata.role} -->
<!-- permission: {agent.permission_level.value} -->

{agent.system_instructions}

## Execution Boundaries:
{chr(10).join(f"- {b}" for b in agent.execution_boundaries)}
"""

    def export_skill(self, skill: SkillDefinition) -> str:
        return skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        return team.to_json()
