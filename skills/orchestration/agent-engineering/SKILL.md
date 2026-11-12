---
name: Agent Engineering & Architecture Standards
description: Engineering principles for defining deterministic, model-agnostic, and safe AI agents.
category: orchestration
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Agent Engineering & Architecture Standards

Engineering principles for defining deterministic, model-agnostic, and safe AI agents.

## Trigger Conditions
- Activated when designing, refactoring, or validating autonomous agent contracts.
- Invoked by system architects and multi-agent team coordinators.

## Required Inputs
```json
{
  "agent_role": "string",
  "system_instructions": "string",
  "permission_level": "string",
  "input_schema": "object",
  "output_schema": "object"
}
```

## Execution Instructions
1. Inspect role boundaries and prevent multi-purpose prompt sprawl.
2. Verify that input and output schemas enforce strict typing (JSON Schema / PEP 557).
3. Ensure sensitive operations are gated behind HMAC permission tickets.
4. Validate that completion criteria require verifiable evidence artifacts rather than self-reported success.

## Expected Outputs
```json
{
  "validation_score": "integer",
  "bot_ready_status": "string",
  "architectural_recommendations": "list"
}
```

## Limitations & Security
- **Limitation:** Does not generate model weights; focuses on orchestration contracts.
- **Security:** Enforces least-privilege boundaries and prohibits unconstrained tool access.
