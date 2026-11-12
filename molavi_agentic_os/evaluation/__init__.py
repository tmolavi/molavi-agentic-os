"""TM Evaluation Module."""

from .evaluator import AgentOutputEvaluator, EvaluationScore
from .foreman_gate import ForemanVerificationGate, VerificationArtifact, VerificationResult
from .autoresearch import AutoresearchLoop, ResearchHypothesis, ExperimentTrial, KeepRevertDecision

__all__ = [
    "AgentOutputEvaluator",
    "EvaluationScore",
    "ForemanVerificationGate",
    "VerificationArtifact",
    "VerificationResult",
    "AutoresearchLoop",
    "ResearchHypothesis",
    "ExperimentTrial",
    "KeepRevertDecision"
]
