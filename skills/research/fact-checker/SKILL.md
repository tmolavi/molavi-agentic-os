---
name: Fact & Claim Verification
description: Cross-reference text statements against primary sources and compute confidence scores.
category: research
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Fact & Claim Verification

Cross-reference text statements against primary sources and compute confidence scores.

## Trigger Conditions
- Activated when task requires capability: `fact-checker`
- Invoked by specialist agents in category `research`

## Required Inputs
```json
{
  "statements": "List of claims to verify"
}
```

## Execution Instructions
Extract atomic claims from text. For each claim, query authoritative repositories. Assign True, False, or Unverified.

## Expected Outputs
```json
{
  "verdicts": "List of {claim, status, source_url, confidence}"
}
```

## Limitations & Security
- **Limitation:** Cannot verify private or non-public events
- **Security:** Flag conflicting historical records neutrally
