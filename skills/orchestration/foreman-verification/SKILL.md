---
name: Foreman 'No-Guessing' Task Verification
description: Enforces that tasks can only be completed when tangible, verifiable artifact evidence exists.
category: orchestration
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Foreman 'No-Guessing' Task Verification

Enforces that tasks can only be completed when tangible, verifiable artifact evidence exists.

## Trigger Conditions
- Activated when task requires capability: `foreman-verification`
- Invoked by specialist agents in category `orchestration`

## Required Inputs
```json
{
  "task_output": "Dictionary of execution results",
  "required_artifacts": "list"
}
```

## Execution Instructions
Inspect agent output. Ensure required artifacts (files, URLs, test outputs) physically exist and are non-empty. Reject guesses.

## Expected Outputs
```json
{
  "verified": "boolean",
  "missing_artifacts": "list",
  "status": "string"
}
```

## Limitations & Security
- **Limitation:** Requires deterministic criteria
- **Security:** Stops hallucinated success claims
