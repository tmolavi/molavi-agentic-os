"""TM Autoresearch Evaluation Engine — Metric-driven autonomous experiment loops.

Inspired by Andrej Karpathy's Autoresearch:
- Metric-based evaluation and hypothesis verification.
- Automated baseline comparison.
- Keep / revert decision engine for agent prompts, skills, and workflows.
- Structured experiment ledger with reproducible telemetry.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Callable
import time


@dataclass
class ResearchHypothesis:
    """Hypothesis governing an autonomous optimization experiment."""
    id: str
    target_component: str  # e.g., 'seo_audit_prompt', 'retrieval_strategy'
    hypothesis_statement: str
    baseline_metric: float
    target_metric_key: str
    min_improvement_threshold: float = 0.05  # 5% improvement required to keep


@dataclass
class ExperimentTrial:
    """Single trial in an autonomous research loop."""
    trial_number: int
    parameters: Dict[str, Any]
    metric_results: Dict[str, float]
    output_artifact: Any
    elapsed_time_seconds: float
    status: str = "completed"  # completed, failed, reverted


@dataclass
class KeepRevertDecision:
    """Decision indicating whether an experiment trial is kept or reverted."""
    hypothesis_id: str
    trial_number: int
    action: str  # KEEP, REVERT
    previous_best_metric: float
    trial_metric: float
    relative_delta: float
    rationale: str


class AutoresearchLoop:
    """Autonomous experiment loop tracking agent performance metrics and managing keep/revert decisions."""

    def __init__(self, hypothesis: ResearchHypothesis):
        self.hypothesis = hypothesis
        self.trials: List[ExperimentTrial] = []
        self.current_best_metric = hypothesis.baseline_metric
        self.best_parameters: Dict[str, Any] = {}
        self.decisions: List[KeepRevertDecision] = []

    def run_trial(
        self,
        trial_number: int,
        parameters: Dict[str, Any],
        eval_fn: Callable[[Dict[str, Any]], Dict[str, float]],
        artifact_generator: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> KeepRevertDecision:
        """Executes a single trial and computes keep/revert decision against the running baseline."""
        start_time = time.perf_counter()

        try:
            metrics = eval_fn(parameters)
            artifact = artifact_generator(parameters) if artifact_generator else None
            elapsed = time.perf_counter() - start_time

            trial = ExperimentTrial(
                trial_number=trial_number,
                parameters=parameters,
                metric_results=metrics,
                output_artifact=artifact,
                elapsed_time_seconds=elapsed,
                status="completed"
            )
            self.trials.append(trial)

            # Evaluate against target metric
            target_metric = metrics.get(self.hypothesis.target_metric_key, 0.0)
            baseline = self.current_best_metric

            delta = (target_metric - baseline) / max(baseline, 0.0001)

            if delta >= self.hypothesis.min_improvement_threshold:
                # Keep improvement
                decision = KeepRevertDecision(
                    hypothesis_id=self.hypothesis.id,
                    trial_number=trial_number,
                    action="KEEP",
                    previous_best_metric=baseline,
                    trial_metric=target_metric,
                    relative_delta=delta,
                    rationale=f"Metric improved by {delta * 100:.2f}% (exceeds threshold of {self.hypothesis.min_improvement_threshold * 100:.1f}%)."
                )
                self.current_best_metric = target_metric
                self.best_parameters = parameters
            else:
                # Revert
                decision = KeepRevertDecision(
                    hypothesis_id=self.hypothesis.id,
                    trial_number=trial_number,
                    action="REVERT",
                    previous_best_metric=baseline,
                    trial_metric=target_metric,
                    relative_delta=delta,
                    rationale=f"Insufficient gain ({delta * 100:.2f}%). Reverting back to baseline {baseline:.4f}."
                )
                trial.status = "reverted"

            self.decisions.append(decision)
            return decision

        except Exception as e:
            elapsed = time.perf_counter() - start_time
            trial = ExperimentTrial(
                trial_number=trial_number,
                parameters=parameters,
                metric_results={},
                output_artifact=None,
                elapsed_time_seconds=elapsed,
                status="failed"
            )
            self.trials.append(trial)
            decision = KeepRevertDecision(
                hypothesis_id=self.hypothesis.id,
                trial_number=trial_number,
                action="REVERT",
                previous_best_metric=self.current_best_metric,
                trial_metric=0.0,
                relative_delta=-1.0,
                rationale=f"Trial failed with exception: {str(e)}"
            )
            self.decisions.append(decision)
            return decision

    def summary(self) -> Dict[str, Any]:
        """Returns structured research ledger summary."""
        return {
            "hypothesis_id": self.hypothesis.id,
            "target_component": self.hypothesis.target_component,
            "total_trials": len(self.trials),
            "kept_trials": sum(1 for d in self.decisions if d.action == "KEEP"),
            "reverted_trials": sum(1 for d in self.decisions if d.action == "REVERT"),
            "initial_baseline": self.hypothesis.baseline_metric,
            "final_best_metric": self.current_best_metric,
            "best_parameters": self.best_parameters
        }
