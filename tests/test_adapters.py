"""Tests for cross-platform adapters."""

import pytest
import json
from molavi_agentic_os.core.agent import AgentDefinition, AgentMetadata, PermissionLevel
from molavi_agentic_os.core.skill import SkillDefinition, SkillMetadata
from molavi_agentic_os.core.team import TeamDefinition
from molavi_agentic_os.adapters import (
    AntigravityAdapter,
    CodexAdapter,
    ClaudeCodeAdapter,
    HermesAdapter,
    GenericAdapter
)

@pytest.fixture
def sample_agent():
    return AgentDefinition(
        metadata=AgentMetadata(
            id="geo-auditor",
            name="GEO Auditor",
            purpose="Generative engine optimization audit specialist.",
            role="GEO Specialist",
            category="geo"
        ),
        system_instructions="Measure brand visibility across AI engines with citation checks.",
        execution_boundaries=["Read-only audits", "No spamming"],
        permission_level=PermissionLevel.L0_READ_ONLY
    )

def test_antigravity_adapter(sample_agent):
    ad = AntigravityAdapter()
    res = ad.export_agent(sample_agent)
    assert "# Antigravity Subagent Configuration" in res
    assert "geo-auditor" in sample_agent.metadata.id

def test_codex_adapter(sample_agent):
    ad = CodexAdapter()
    res = ad.export_agent(sample_agent)
    assert "# Codex / Cursor Instruction Rule" in res
    assert "Execution Boundaries:" in res

def test_claude_code_adapter(sample_agent):
    ad = ClaudeCodeAdapter()
    res = ad.export_agent(sample_agent)
    assert "export const geo_auditor" in res

def test_hermes_adapter(sample_agent):
    ad = HermesAdapter()
    res = ad.export_agent(sample_agent)
    data = json.loads(res)
    assert data["hermes_agent_version"] == "1.0"
    assert data["id"] == "geo-auditor"
