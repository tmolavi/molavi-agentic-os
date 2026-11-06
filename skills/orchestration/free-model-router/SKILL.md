---
name: Free-First Model Router
description: Route LLM inference tasks starting with local Ollama and free cloud tiers before escalating to paid models.
category: orchestration
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Free-First Model Router

Route LLM inference tasks starting with local Ollama and free cloud tiers before escalating to paid models.

## Trigger Conditions
- Activated when task requires capability: `free-model-router`
- Invoked by specialist agents in category `orchestration`

## Required Inputs
```json
{
  "prompt": "string",
  "task_type": "string",
  "preferred_tier": "string"
}
```

## Execution Instructions
Inspect task complexity. Try local Ollama (Llama 3, Mistral) first. Fall back to Groq or Gemini Free Tier. Log token usage.

## Expected Outputs
```json
{
  "model_used": "string",
  "response": "string",
  "cost_usd": "float"
}
```

## Limitations & Security
- **Limitation:** Dependent on local hardware or free-tier rate limits
- **Security:** Prevents unexpected billing shocks by rejecting unapproved paid calls
