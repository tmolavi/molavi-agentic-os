---
name: Autonomous Experiment Evaluation & Reliability
description: Quantitative evaluation, benchmark execution, and automated keep/revert decisions for agent workflows.
category: evaluation
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Autonomous Experiment Evaluation & Reliability

Quantitative evaluation, benchmark execution, and automated keep/revert decisions for agent workflows.

Inspired by Andrej Karpathy's Autoresearch principles.

## Trigger Conditions
- Activated when evaluating agent prompt variations, routing configurations, or workflow optimizations.
- Invoked by reliability engineers and autonomous research agents.

## Required Inputs
```json
{
  "hypothesis_statement": "string",
  "baseline_metrics": "object",
  "target_metric_key": "string",
  "min_improvement_threshold": "float"
}
```

## Execution Instructions
1. Run reproducible evaluation benchmark over defined test dataset.
2. Measure primary target metrics (e.g. latency, accuracy, token cost, citability).
3. Compare trial score against baseline.
4. Execute Keep decision if delta exceeds threshold; execute Revert if regression occurs.
5. Record trial results in persistent research ledger.

## Expected Outputs
```json
{
  "decision": "string",
  "baseline_metric": "float",
  "trial_metric": "float",
  "relative_delta": "float",
  "rationale": "string"
}
```

## Limitations & Security
- **Limitation:** Requires measurable, reproducible metric evaluation function.
- **Security:** Reverts unverified changes automatically to prevent performance degradation.
