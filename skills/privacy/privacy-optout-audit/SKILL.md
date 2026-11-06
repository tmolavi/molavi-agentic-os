---
name: Digital Footprint & Privacy Opt-Out Auditor
description: Identify personal or company exposure across public data-broker sites and generate removal requests.
category: privacy
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Digital Footprint & Privacy Opt-Out Auditor

Identify personal or company exposure across public data-broker sites and generate removal requests.

## Trigger Conditions
- Activated when task requires capability: `privacy-optout-audit`
- Invoked by specialist agents in category `privacy`

## Required Inputs
```json
{
  "entity_name": "string",
  "domains_to_check": "list"
}
```

## Execution Instructions
Scan standard directory templates (Whitepages, Spokeo, Radaris). Generate standardized opt-out and GDPR removal requests.

## Expected Outputs
```json
{
  "exposed_records": "list",
  "optout_procedures": "list"
}
```

## Limitations & Security
- **Limitation:** Audit and template generation; user reviews before dispatch
- **Security:** Never store user personal identification numbers or passwords
