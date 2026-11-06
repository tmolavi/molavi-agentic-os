---
name: Permission-Slip Human Approval Gatekeeper
description: Generate HMAC-signed approval tickets for sensitive actions (email, trade, deployment, deletion).
category: security
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Permission-Slip Human Approval Gatekeeper

Generate HMAC-signed approval tickets for sensitive actions (email, trade, deployment, deletion).

## Trigger Conditions
- Activated when task requires capability: `permission-slip`
- Invoked by specialist agents in category `security`

## Required Inputs
```json
{
  "action": "Action name",
  "impact": "Description of impact",
  "risk_level": "LOW|MEDIUM|HIGH|CRITICAL"
}
```

## Execution Instructions
When an agent attempts a sensitive action classified under L2, halt execution, generate an ApprovalTicket, and notify the human operator.

## Expected Outputs
```json
{
  "ticket_id": "string",
  "status": "PENDING",
  "signature": "string"
}
```

## Limitations & Security
- **Limitation:** Requires human decision; will auto-expire if unattended
- **Security:** Cryptographically signs tickets to prevent tampering
