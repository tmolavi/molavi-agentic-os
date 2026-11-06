"""Foreman Anti-Hallucination Gate.

Rule: "It is not allowed to guess."
An agent cannot mark a task completed unless it produces verifiable artifact evidence.
"""

from typing import Dict, Any, List

class ForemanVerificationGate:
    """Validates that agent execution results contain concrete artifacts and verifiable evidence."""

    @classmethod
    def verify_output(cls, output: Dict[str, Any], required_keys: List[str], min_evidence_items: int = 1) -> bool:
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
