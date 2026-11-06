---
name: B2B Lead Qualification & ICP Scoring
description: Evaluate prospective business accounts against ICP parameters and score qualification likelihood.
category: business
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# B2B Lead Qualification & ICP Scoring

Evaluate prospective business accounts against ICP parameters and score qualification likelihood.

## Trigger Conditions
- Activated when task requires capability: `lead-qualification`
- Invoked by specialist agents in category `business`

## Required Inputs
```json
{
  "company_profile": "object",
  "icp_rules": "object"
}
```

## Execution Instructions
Assess company revenue, employee count, tech stack, and pain points against ICP rules. Assign points per category.

## Expected Outputs
```json
{
  "score": "integer (0-100)",
  "qualified": "boolean",
  "qualification_reasons": "list"
}
```

## Limitations & Security
- **Limitation:** Based on public business information
- **Security:** Filter out protected personal private details
