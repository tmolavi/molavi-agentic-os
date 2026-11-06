"""Tests for core schemas and BotReadyValidator."""

import pytest
import os
import json
from molavi_agentic_os.core.agent import AgentDefinition, AgentMetadata, PermissionLevel
from molavi_agentic_os.core.skill import SkillDefinition, SkillMetadata
from molavi_agentic_os.core.team import TeamDefinition, TeamRole
from molavi_agentic_os.core.workflow import WorkflowDefinition, WorkflowStep
from molavi_agentic_os.core.validator import BotReadyValidator

def test_agent_serialization():
    agent = AgentDefinition(
        metadata=AgentMetadata(
            id="test-agent",
            name="Test Agent",
            purpose="A test agent designed to verify unit testing behavior and criteria.",
            role="Tester",
            category="development"
        ),
        system_instructions="Execute test steps deterministically and report results with evidence.",
        execution_boundaries=["Do not mutate production", "Verify tests"],
        permission_level=PermissionLevel.L1_DRAFT_RECOMMEND,
        input_schema={"test_id": "string"},
        output_schema={"passed": "boolean"},
        test_cases=[{"test": "smoke"}]
    )
    val = BotReadyValidator.validate_agent(agent)
    assert val.is_valid is True
    assert val.score >= 80

    # Test JSON round-trip
    d = agent.to_dict()
    agent_restored = AgentDefinition.from_dict(d)
    assert agent_restored.metadata.id == "test-agent"
    assert agent_restored.permission_level == PermissionLevel.L1_DRAFT_RECOMMEND

def test_skill_markdown():
    skill = SkillDefinition(
        metadata=SkillMetadata(id="test-skill", name="Test Skill", description="Performs unit test operations", category="testing"),
        trigger_conditions=["When testing is invoked"],
        required_inputs={"arg": "string"},
        execution_instructions="Run test runner and verify output status code is 0.",
        expected_outputs={"status": "PASS"},
        limitations=["Only runs in sandbox"],
        security_considerations=["No eval execution"]
    )
    val = BotReadyValidator.validate_skill(skill)
    assert val.is_valid is True
    assert val.score == 100
    md = skill.to_markdown()
    assert "# Test Skill" in md
    assert "Trigger Conditions" in md
