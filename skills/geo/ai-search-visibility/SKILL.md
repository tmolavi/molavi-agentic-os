---
name: AI Search Visibility & GEO Analysis
description: Analyzes content citability, semantic extractability, and recommendation rates across AI answer engines.
category: geo
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# AI Search Visibility & GEO Analysis

Analyzes content citability, semantic extractability, and recommendation rates across AI answer engines (Perplexity, Gemini, ChatGPT).

## Trigger Conditions
- Activated when evaluating how generative engines cite, index, and summarize brand content.
- Invoked by GEO auditors and AI visibility specialists.

## Required Inputs
```json
{
  "target_url": "string",
  "brand_entities": "list",
  "query_clusters": "list"
}
```

## Execution Instructions
1. Inspect passage-level citability and TL;DR block placement.
2. Evaluate entity definition clarity and JSON-LD schema depth.
3. Compute semantic extractability score and LLM citation readiness.
4. Provide structured fixes for improving LLM search engine visibility.

## Expected Outputs
```json
{
  "citability_score": "float",
  "entity_clarity_score": "float",
  "actionable_recommendations": "list"
}
```

## Limitations & Security
- **Limitation:** Focuses on structural extractability; live model querying requires API credentials or headless browser.
- **Security:** Zero token leakage; executes locally without third-party data tracking.
