---
name: Task Queue & Worker Orchestrator
description: Schedule, prioritize, and execute agent tasks in parallel with retry and exponential backoff.
category: orchestration
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Task Queue & Worker Orchestrator

Schedule, prioritize, and execute agent tasks in parallel with retry and exponential backoff.

## Trigger Conditions
- Activated when task requires capability: `task-queue-orchestrator`
- Invoked by specialist agents in category `orchestration`

## Required Inputs
```json
{
  "tasks": "List of task specs",
  "max_concurrency": "integer"
}
```

## Execution Instructions
Queue tasks by priority. Resolve dependencies in topological order. Dispatch across worker pool. Retry on transient failures.

## Expected Outputs
```json
{
  "completed": "list",
  "failed": "list",
  "execution_time": "float"
}
```

## Limitations & Security
- **Limitation:** Local CPU/thread bound
- **Security:** Enforces strict per-task timeouts to prevent resource starvation
