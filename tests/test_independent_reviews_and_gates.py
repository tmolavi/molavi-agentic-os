"""Tests for Independent Review Personas, Doubt-Driven Workflow, and Engineering Quality Gates."""

import json
import os
import glob
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_independent_review_personas_load_and_validate():
    agents_dir = os.path.join(REPO_ROOT, "agents", "development")
    expected_agents = [
        "code-reviewer.json",
        "security-auditor.json",
        "test-engineer.json",
        "web-performance-auditor.json",
    ]

    for agent_file in expected_agents:
        path = os.path.join(agents_dir, agent_file)
        assert os.path.exists(path), f"Missing expected agent persona file: {agent_file}"
        with open(path, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            assert "metadata" in data
            assert data["metadata"]["category"] == "development"
            assert "system_instructions" in data
            assert "required_skills" in data
            assert "required_tools" in data
            assert "output_schema" in data
            assert data["permission_level"] in ["L1_DRAFT_RECOMMEND", "L2_EXECUTE_WITH_APPROVAL"]

def test_independent_engineering_review_team_schema():
    team_path = os.path.join(REPO_ROOT, "teams", "independent-engineering-review-team.json")
    assert os.path.exists(team_path), "Missing independent-engineering-review-team.json"
    with open(team_path, "r", encoding="utf-8") as fp:
        team = json.load(fp)
        assert team["id"] == "independent-engineering-review-team"
        roles = {r["role_id"]: r["agent_id"] for r in team["roles"]}
        assert "coordinator" in roles
        assert roles["code_reviewer"] == "code-reviewer"
        assert roles["security_auditor"] == "security-auditor"
        assert roles["test_engineer"] == "test-engineer"
        assert roles["perf_auditor"] == "web-performance-auditor"

def test_workflows_integrity():
    workflows_dir = os.path.join(REPO_ROOT, "workflows")
    expected_workflows = [
        "doubt-driven-adversarial-review.json",
        "spec-driven-development-flow.json",
    ]

    for wf_file in expected_workflows:
        wf_path = os.path.join(workflows_dir, wf_file)
        assert os.path.exists(wf_path), f"Missing expected workflow: {wf_file}"
        with open(wf_path, "r", encoding="utf-8") as fp:
            wf = json.load(fp)
            assert "id" in wf
            assert "steps" in wf
            assert len(wf["steps"]) >= 4
            assert "quality_gate" in wf

def test_skills_frontmatter_and_content():
    skills_dir = os.path.join(REPO_ROOT, "skills", "development")
    expected_skills = [
        "spec-driven-development",
        "doubt-driven-development",
        "constraint-driven-development",
        "anti-rationalization-rules",
    ]

    for skill_name in expected_skills:
        skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
        assert os.path.exists(skill_path), f"Missing skill file: {skill_name}/SKILL.md"
        with open(skill_path, "r", encoding="utf-8") as fp:
            content = fp.read()
            assert content.startswith("---")
            assert "name:" in content
            assert "description:" in content
            assert "category: development" in content
