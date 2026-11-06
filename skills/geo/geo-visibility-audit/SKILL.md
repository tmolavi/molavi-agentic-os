---
name: Generative Engine Optimization (GEO) Audit
description: Measure entity citability and answer visibility across AI engines (Perplexity, Gemini, ChatGPT).
category: geo
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Generative Engine Optimization (GEO) Audit

Measure entity citability and answer visibility across AI engines (Perplexity, Gemini, ChatGPT).

## Trigger Conditions
- Activated when task requires capability: `geo-visibility-audit`
- Invoked by specialist agents in category `geo`

## Required Inputs
```json
{
  "brand": "Brand or entity name",
  "queries": "List of prompt queries"
}
```

## Execution Instructions
Query benchmark AI models with representative user prompts. Record whether target entity is cited, mentioned positively, or omitted.

## Expected Outputs
```json
{
  "visibility_ratio": "float",
  "cited_sources": "list",
  "missing_entity_signals": "list"
}
```

## Limitations & Security
- **Limitation:** Dependent on search engine rate limits
- **Security:** Never send synthetic spam or automated review manipulation
