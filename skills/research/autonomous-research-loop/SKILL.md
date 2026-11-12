---
name: Autonomous Research Loop & Evidence Synthesis
description: End-to-end autonomous research iteration, literature synthesis, and factual verification.
category: research
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Autonomous Research Loop & Evidence Synthesis

End-to-end autonomous research iteration, literature synthesis, and factual verification.

## Trigger Conditions
- Activated when conducting deep multi-turn research, state-of-the-art literature review, or market studies.
- Invoked by lead research agents and project managers.

## Required Inputs
```json
{
  "research_objective": "string",
  "seed_queries": "list",
  "max_iterations": "integer"
}
```

## Execution Instructions
1. Formulate testable research questions from high-level objective.
2. Query documentation, academic repositories, and web indices.
3. Cross-validate facts across multiple independent sources.
4. Synthesize findings into structured Markdown briefs with verifiable citation hashes.
5. Identify knowledge gaps and trigger next iteration until completion criteria are met.

## Expected Outputs
```json
{
  "research_brief": "string",
  "citations": "list",
  "iterations_completed": "integer",
  "foreman_verified": "boolean"
}
```

## Limitations & Security
- **Limitation:** Does not generate speculative claims; enforces strict factual attribution.
- **Security:** Secret tokens are scrubbed from all research query logs.
