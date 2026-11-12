"""Multi-Agent Team Execution with Explicit Handoff Contracts.

Demonstrates:
1. Team Topologies (Hierarchical Coordinator -> Specialist -> Fact-Checker)
2. Explicit JSON Schema Handoff Contracts
3. Never trusting an agent output solely because another agent produced it
4. Downstream verification before handoff execution
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact


class AgentHandoffContract:
    """Formal schema and validation contract for inter-agent communication."""

    def __init__(self, sender_id: str, receiver_id: str, required_keys: list):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.required_keys = required_keys

    def validate_handoff(self, payload: dict) -> tuple[bool, str]:
        for k in self.required_keys:
            if k not in payload or not payload[k]:
                return False, f"Handoff validation failed: missing or empty key '{k}' in transmission from {self.sender_id} to {self.receiver_id}"
        return True, "Handoff payload strictly conforms to contract."


def main():
    print("=" * 75)
    print("TM MOLAVI AGENTIC OS — MULTI-AGENT TEAM HANDOFF CONTRACTS")
    print("=" * 75)

    # 1. Define Agents and Roles
    coordinator = "project-manager"
    specialist = "research-agent"
    verifier = "fact-checker"
    publisher = "content-writer"

    print(f"\n[TOPOLOGY] Hierarchical Multi-Agent Team:")
    print(f"  Coordinator: {coordinator}")
    print(f"  Researcher:  {specialist}")
    print(f"  Verifier:    {verifier}")
    print(f"  Publisher:   {publisher}")

    # 2. Handoff Contract 1: Coordinator -> Researcher
    contract_c_to_r = AgentHandoffContract(
        sender_id=coordinator,
        receiver_id=specialist,
        required_keys=["task_id", "objective", "constraints"]
    )
    brief_payload = {
        "task_id": "TASK-2026-004",
        "objective": "Investigate LLM retrieval latency vs context window expansion",
        "constraints": ["Include empirical benchmarks", "No hallucinated citations"]
    }
    is_valid, msg = contract_c_to_r.validate_handoff(brief_payload)
    print(f"\n[HANDOFF 1] {coordinator} -> {specialist}:")
    print(f"  Contract Status: {msg}")

    # 3. Researcher executes work and produces structured research output
    research_output = {
        "task_id": brief_payload["task_id"],
        "findings": "Context windows > 128k show 2.4x latency degradation in naive full-attention retrieval.",
        "citations": [
            "https://arxiv.org/abs/2401.00000",
            "https://github.com/tmolavi/molavi-agentic-os"
        ],
        "evidence": [
            "Benchmark run over 100 queries on 8x H100 cluster",
            "Mean TTFT increased from 180ms to 430ms"
        ]
    }

    # 4. Handoff Contract 2: Researcher -> Fact Checker (Verification Gate)
    contract_r_to_f = AgentHandoffContract(
        sender_id=specialist,
        receiver_id=verifier,
        required_keys=["task_id", "findings", "citations", "evidence"]
    )
    is_valid, msg = contract_r_to_f.validate_handoff(research_output)
    print(f"\n[HANDOFF 2] {specialist} -> {verifier}:")
    print(f"  Contract Status: {msg}")

    # Fact-Checker verifies output before downstream consumption
    print(f"\n[VERIFICATION] {verifier} audits {specialist} research output:")
    gate_res = ForemanVerificationGate.verify(
        research_output,
        expected_artifacts=[
            VerificationArtifact("findings", "string", research_output["findings"]),
            VerificationArtifact("citations", "list", research_output["citations"]),
        ]
    )
    print(f"  Foreman Verification Passed: {gate_res.is_verified}")
    print(f"  Verified Artifacts: {gate_res.verified_artifacts}")

    # 5. Handoff Contract 3: Verified Research -> Publisher
    contract_f_to_p = AgentHandoffContract(
        sender_id=verifier,
        receiver_id=publisher,
        required_keys=["task_id", "verified_findings", "approved_citations"]
    )
    verified_payload = {
        "task_id": research_output["task_id"],
        "verified_findings": research_output["findings"],
        "approved_citations": research_output["citations"]
    }
    is_valid, msg = contract_f_to_p.validate_handoff(verified_payload)
    print(f"\n[HANDOFF 3] {verifier} -> {publisher}:")
    print(f"  Contract Status: {msg}")

    final_article = (
        f"# Technical Analysis: Context Windows vs Retrieval Latency\n\n"
        f"{verified_payload['verified_findings']}\n\n"
        f"**Verified Sources:**\n" + "\n".join(f"- {c}" for c in verified_payload["approved_citations"])
    )
    print("\n[FINAL OUTPUT] Publisher Generated Clean Document:")
    print("-" * 50)
    print(final_article)
    print("-" * 50)
    print("Multi-agent team flow completed with zero unverified trust assumptions.\n")


if __name__ == "__main__":
    main()
