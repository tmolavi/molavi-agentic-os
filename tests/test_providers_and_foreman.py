"""Tests for Free-first model router and Foreman verification gate."""

import pytest
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider
from molavi_agentic_os.evaluation.foreman_gate import ForemanVerificationGate
from molavi_agentic_os.evaluation.evaluator import AgentOutputEvaluator

def test_model_router_free_first():
    router = ModelRouter()
    local_p = MockProvider('{"tier": "free_local", "answer": "42"}')
    router.register_provider("ollama-local", local_p, ModelTier.FREE_LOCAL)

    resp = router.route_and_generate("What is the meaning of life?")
    assert "free_local" in resp.content
    assert resp.estimated_cost_usd == 0.0

def test_foreman_gate():
    # Fails when missing evidence
    bad_output = {"summary": "Completed successfully"}
    assert ForemanVerificationGate.verify_output(bad_output, required_keys=["summary"], min_evidence_items=1) is False

    # Passes when evidence exists
    good_output = {
        "summary": "Completed successfully",
        "evidence": ["https://example.com/source1", "https://example.com/source2"]
    }
    assert ForemanVerificationGate.verify_output(good_output, required_keys=["summary"], min_evidence_items=2) is True

def test_evaluator():
    output = {"status": "success", "summary": "SEO audit complete", "evidence": ["url1", "url2"]}
    expected = {"summary": "string", "evidence": "list"}
    score = AgentOutputEvaluator.evaluate(output, expected)
    assert score.is_passed is True
    assert score.total_score >= 80.0
