---
name: Personalized B2B Outreach Drafter
description: Draft concise, highly relevant, value-focused outreach emails with zero spam tactics.
category: writing
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Personalized B2B Outreach Drafter

Draft concise, highly relevant, value-focused outreach emails with zero spam tactics.

## Trigger Conditions
- Activated when task requires capability: `outreach-drafter`
- Invoked by specialist agents in category `writing`

## Required Inputs
```json
{
  "lead_context": "object",
  "value_proposition": "string"
}
```

## Execution Instructions
Draft 3 subject line options. Draft body under 120 words focusing on a specific problem and demonstrated solution. Avoid pushy sales pitches.

## Expected Outputs
```json
{
  "subject_lines": "list",
  "body_markdown": "string",
  "cta": "string"
}
```

## Limitations & Security
- **Limitation:** Drafting only; sending requires permission-slip ticket approval
- **Security:** Strictly adhere to CAN-SPAM and GDPR guidelines
