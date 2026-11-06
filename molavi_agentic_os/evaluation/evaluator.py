"""Agent Output Evaluation Framework."""

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class EvaluationScore:
    task_completion: float  # 0.0 to 1.0
    evidence_quality: float  # 0.0 to 1.0
    adherence_to_schema: float  # 0.0 to 1.0
    total_score: float  # 0.0 to 100.0
    is_passed: bool

class AgentOutputEvaluator:
    @classmethod
    def evaluate(cls, result_data: Dict[str, Any], expected_schema: Dict[str, Any]) -> EvaluationScore:
        if not result_data:
            return EvaluationScore(0.0, 0.0, 0.0, 0.0, False)

        # 1. Schema adherence
        matched_keys = sum(1 for k in expected_schema.keys() if k in result_data)
        schema_ratio = matched_keys / max(len(expected_schema), 1)

        # 2. Evidence presence
        evidence = result_data.get("evidence", [])
        evidence_ratio = 1.0 if len(evidence) >= 2 else (0.5 if len(evidence) == 1 else 0.0)

        # 3. Completeness
        completion_ratio = 1.0 if result_data.get("status") in ["success", "completed", "done", "ok"] else 0.7

        total = (schema_ratio * 40.0) + (evidence_ratio * 30.0) + (completion_ratio * 30.0)
        return EvaluationScore(
            task_completion=completion_ratio,
            evidence_quality=evidence_ratio,
            adherence_to_schema=schema_ratio,
            total_score=total,
            is_passed=total >= 70.0
        )
