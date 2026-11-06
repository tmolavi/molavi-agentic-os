---
name: Second Brain Local Memory Vault
description: Store and retrieve episodic memories, project context, and key-value state locally via SQLite.
category: orchestration
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Second Brain Local Memory Vault

Store and retrieve episodic memories, project context, and key-value state locally via SQLite.

## Trigger Conditions
- Activated when task requires capability: `second-brain-memory`
- Invoked by specialist agents in category `orchestration`

## Required Inputs
```json
{
  "operation": "store | retrieve",
  "session_id": "string",
  "data": "object"
}
```

## Execution Instructions
Connect to local SQLite database. Store interaction episodes with timestamp and agent ID. Query recent context on demand.

## Expected Outputs
```json
{
  "success": "boolean",
  "data": "object"
}
```

## Limitations & Security
- **Limitation:** Local file access required
- **Security:** Database remains strictly on local machine; zero external cloud sync by default
