"""Foreman Anti-Hallucination Gate.

Rule: "It is not allowed to guess."
An agent cannot mark a task completed unless it produces verifiable artifact evidence.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class VerificationArtifact:
    """Represents a tangible, verifiable artifact produced by an agent."""
    name: str
    artifact_type: str  # file, url, metric, schema, test_result
    data: Any
    is_verifiable: bool = True


@dataclass
class VerificationResult:
    """Outcome of Foreman anti-hallucination verification."""
    is_verified: bool
    verified_artifacts: List[str] = field(default_factory=list)
    missing_artifacts: List[str] = field(default_factory=list)
    failure_reason: Optional[str] = None


class ForemanVerificationGate:
    """Validates that agent execution results contain concrete artifacts and verifiable evidence."""

    @classmethod
    def verify(
        cls,
        output: Dict[str, Any],
        expected_artifacts: List[VerificationArtifact],
        min_evidence_items: int = 1
    ) -> VerificationResult:
        """Formal verification of execution output against expected tangible artifacts."""
        if not output:
            return VerificationResult(False, [], [], "Execution output is empty.")

        verified = []
        missing = []

        for art in expected_artifacts:
            if art.data is not None and art.data != "" and art.data != [] and art.data != {}:
                verified.append(art.name)
            else:
                missing.append(art.name)

        # Evidence validation
        evidence = output.get("evidence", [])
        citations = output.get("citations", [])
        has_evidence = (isinstance(evidence, list) and len(evidence) >= min_evidence_items) or \
                       (isinstance(citations, list) and len(citations) >= min_evidence_items)

        if missing:
            return VerificationResult(False, verified, missing, f"Missing required artifacts: {', '.join(missing)}")

        if not has_evidence:
            return VerificationResult(False, verified, ["evidence"], "No verifiable evidence or citations attached.")

        return VerificationResult(True, verified, [])

    @classmethod
    def verify_output(cls, output: Dict[str, Any], required_keys: List[str], min_evidence_items: int = 1) -> bool:
        """Legacy helper for backward compatibility: checks required keys and evidence."""
        # 1. Output cannot be empty
        if not output:
            return False

        # 2. Check all required keys exist and are non-empty
        for key in required_keys:
            if key not in output:
                return False
            val = output[key]
            if val is None or val == "" or val == [] or val == {}:
                return False

        # 3. Evidence check: must have verifiable sources/findings
        evidence = output.get("evidence", [])
        if not isinstance(evidence, list) or len(evidence) < min_evidence_items:
            # Check if structured report contains citations
            if "citations" in output and len(output["citations"]) >= min_evidence_items:
                return True
            return False

        return True
