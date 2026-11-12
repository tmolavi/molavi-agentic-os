"""Tests for Autoresearch loop, TM Second Brain Adapter, and Hermes Desktop Adapter."""

import os
import shutil
import tempfile
import pytest
from molavi_agentic_os.evaluation import AutoresearchLoop, ResearchHypothesis, ForemanVerificationGate, VerificationArtifact
from molavi_agentic_os.memory.second_brain import TMSecondBrainMemoryAdapter
from molavi_agentic_os.adapters import HermesDesktopAdapter
from molavi_agentic_os.core.agent import AgentDefinition, AgentMetadata, PermissionLevel


def test_autoresearch_keep_revert_decisions():
    hyp = ResearchHypothesis(
        id="HYP-01",
        target_component="eval_prompt",
        hypothesis_statement="Test prompt optimization",
        baseline_metric=50.0,
        target_metric_key="score",
        min_improvement_threshold=0.10  # 10% gain required
    )
    loop = AutoresearchLoop(hyp)

    # Trial 1: 30% improvement -> KEEP
    dec1 = loop.run_trial(1, {"step": 1}, lambda p: {"score": 65.0})
    assert dec1.action == "KEEP"
    assert loop.current_best_metric == 65.0

    # Trial 2: 2% improvement (below 10% threshold) -> REVERT
    dec2 = loop.run_trial(2, {"step": 2}, lambda p: {"score": 66.0})
    assert dec2.action == "REVERT"
    assert loop.current_best_metric == 65.0

    # Trial 3: Regression -> REVERT
    dec3 = loop.run_trial(3, {"step": 3}, lambda p: {"score": 50.0})
    assert dec3.action == "REVERT"
    assert loop.current_best_metric == 65.0

    summary = loop.summary()
    assert summary["total_trials"] == 3
    assert summary["kept_trials"] == 1
    assert summary["reverted_trials"] == 2
    assert summary["final_best_metric"] == 65.0


def test_second_brain_memory_adapter():
    temp_vault = tempfile.mkdtemp(prefix="tm_brain_test_")
    try:
        adapter = TMSecondBrainMemoryAdapter(vault_path=temp_vault, namespace="research")

        # Store episode
        sample_entry = {"query": "Transformer attention", "result_summary": "Quadratic complexity"}
        adapter.store_episode(session_id="sess_101", agent_id="research-agent", entry=sample_entry)

        episodes = adapter.get_episodes(session_id="sess_101")
        assert len(episodes) == 1
        assert episodes[0]["entry"]["query"] == "Transformer attention"

        # Key-Value store
        adapter.set_key(namespace="research", key="model_version", value="v2.4")
        val = adapter.get_key(namespace="research", key="model_version")
        assert val == "v2.4"

        # Verify audit log exists
        audit_file = os.path.join(temp_vault, ".audit_log.jsonl")
        assert os.path.exists(audit_file)
    finally:
        shutil.rmtree(temp_vault)


def test_hermes_desktop_adapter():
    adapter = HermesDesktopAdapter(allowed_directories=["/workspace/safe"])
    assert adapter.platform_name == "hermes-desktop"

    agent = AgentDefinition(
        metadata=AgentMetadata(
            id="desktop-researcher",
            name="Desktop Researcher",
            role="Local File Analyst",
            purpose="Inspects local documentation safely without leaking paths.",
            category="research"
        ),
        permission_level=PermissionLevel.L0_READ_ONLY,
        system_instructions="You are a secure local desktop research agent."
    )

    exported = adapter.export_agent(agent)
    assert "hermes_desktop_runtime_version" in exported
    assert "desktop-researcher" in exported
    assert "/workspace/safe" in exported
