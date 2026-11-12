"""Hermes Personal Desktop Platform Adapter.

Specialized adapter for local desktop agent execution, local file access boundaries,
and safe desktop workflow encapsulation.
"""

import json
from typing import Dict, Any, List
from .base import PlatformAdapter
from ..core.agent import AgentDefinition
from ..core.skill import SkillDefinition
from ..core.team import TeamDefinition


class HermesDesktopAdapter(PlatformAdapter):
    """Adapter for Hermes Personal Desktop runtime (macOS local and Finland headless server)."""

    def __init__(self, allowed_directories: List[str] = None):
        self.allowed_directories = allowed_directories or ["~/workspace", "~/Documents", "/opt/hermes"]

    @property
    def platform_name(self) -> str:
        return "hermes-desktop"

    def export_agent(self, agent: AgentDefinition) -> str:
        data = {
            "hermes_desktop_runtime_version": "2.0",
            "agent_id": agent.metadata.id,
            "display_name": agent.metadata.name,
            "role": agent.metadata.role,
            "security_boundary": {
                "jail_enabled": True,
                "allowed_directories": self.allowed_directories,
                "allow_network": True,
                "require_human_approval_for_write": True
            },
            "system_prompt": agent.system_instructions,
            "skills": agent.required_skills,
            "desktop_actions": [
                "read_local_file",
                "list_directory",
                "search_notes",
                "query_second_brain"
            ]
        }
        return json.dumps(data, indent=2)

    def export_skill(self, skill: SkillDefinition) -> str:
        # Skills in Hermes desktop format preserve markdown with desktop runtime headers
        header = f"<!-- Hermes Desktop Skill: {skill.metadata.name} | Sandbox: Local -->\n"
        return header + skill.to_markdown()

    def export_team(self, team: TeamDefinition) -> str:
        team_data = json.loads(team.to_json())
        team_data["runtime_target"] = "hermes-desktop"
        team_data["isolation_mode"] = "process_sandbox"
        return json.dumps(team_data, indent=2)
