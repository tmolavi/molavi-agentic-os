"""Autonomous Research & Optimization Loop Example.

Inspired by Andrej Karpathy's Autoresearch:
1. Defines Research Hypothesis and target baseline metric.
2. Iterates over prompt / workflow hyperparameter trials.
3. Evaluates quantitative metrics per trial.
4. Executes Keep / Revert decisions against previous best score.
5. Emits verifiable experiment ledger.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.evaluation import AutoresearchLoop, ResearchHypothesis


def simulate_eval_agent(params: dict) -> dict:
    """Mock evaluation function measuring prompt effectiveness and latency."""
    temperature = params.get("temperature", 0.7)
    use_few_shot = params.get("use_few_shot", False)
    rag_k = params.get("rag_k", 3)

    # Simulated metric formula
    score = 0.60
    if use_few_shot:
        score += 0.18
    if temperature <= 0.3:
        score += 0.12
    if rag_k == 5:
        score += 0.08
    elif rag_k > 5:
        score -= 0.05  # Context dilution penalty

    return {
        "accuracy": round(score, 4),
        "latency_ms": 120.0 + (rag_k * 15.0),
        "cost_usd": 0.00
    }


def main():
    print("=" * 75)
    print("TM MOLAVI AGENTIC OS — AUTORESEARCH EXPERIMENT EVALUATION")
    print("=" * 75)

    # 1. Formulate Hypothesis
    hypothesis = ResearchHypothesis(
        id="EXP-OPT-PROMPT-01",
        target_component="SEO Audit Agent Prompt & Context Strategy",
        hypothesis_statement="Adding 2 few-shot exemplars and lowering temperature to 0.2 will improve audit accuracy > 5%.",
        baseline_metric=0.60,
        target_metric_key="accuracy",
        min_improvement_threshold=0.05
    )

    print(f"\n[HYPOTHESIS] {hypothesis.id}:")
    print(f"  Target:    {hypothesis.target_component}")
    print(f"  Statement: {hypothesis.hypothesis_statement}")
    print(f"  Baseline:  {hypothesis.baseline_metric * 100:.1f}%")

    loop = AutoresearchLoop(hypothesis)

    # 2. Run Trial 1: Just lowering temperature
    print("\n[TRIAL 1] Testing temperature reduction (0.2)...")
    dec1 = loop.run_trial(
        trial_number=1,
        parameters={"temperature": 0.2, "use_few_shot": False, "rag_k": 3},
        eval_fn=simulate_eval_agent
    )
    print(f"  Decision: {dec1.action} | Trial Metric: {dec1.trial_metric * 100:.1f}% | Delta: +{dec1.relative_delta * 100:.1f}%")
    print(f"  Rationale: {dec1.rationale}")

    # 3. Run Trial 2: Increasing RAG k to 10 (dilution failure)
    print("\n[TRIAL 2] Testing excessive context window (rag_k = 10)...")
    dec2 = loop.run_trial(
        trial_number=2,
        parameters={"temperature": 0.2, "use_few_shot": False, "rag_k": 10},
        eval_fn=simulate_eval_agent
    )
    print(f"  Decision: {dec2.action} | Trial Metric: {dec2.trial_metric * 100:.1f}% | Delta: {dec2.relative_delta * 100:.1f}%")
    print(f"  Rationale: {dec2.rationale}")

    # 4. Run Trial 3: Adding few-shot exemplars + optimal rag_k
    print("\n[TRIAL 3] Testing few-shot exemplars + optimal rag_k = 5...")
    dec3 = loop.run_trial(
        trial_number=3,
        parameters={"temperature": 0.2, "use_few_shot": True, "rag_k": 5},
        eval_fn=simulate_eval_agent
    )
    print(f"  Decision: {dec3.action} | Trial Metric: {dec3.trial_metric * 100:.1f}% | Delta: +{dec3.relative_delta * 100:.1f}%")
    print(f"  Rationale: {dec3.rationale}")

    # 5. Summary & Ledger
    summary = loop.summary()
    print("\n[EXPERIMENT LEDGER SUMMARY]")
    print(f"  Total Trials:   {summary['total_trials']}")
    print(f"  Kept Trials:    {summary['kept_trials']}")
    print(f"  Reverted:       {summary['reverted_trials']}")
    print(f"  Start Baseline: {summary['initial_baseline'] * 100:.1f}%")
    print(f"  Final Best:     {summary['final_best_metric'] * 100:.1f}%")
    print(f"  Best Parameters: {json.dumps(summary['best_parameters'])}")
    print("\nAutoresearch loop completed with verifiable metric tracking.\n")


if __name__ == "__main__":
    main()
