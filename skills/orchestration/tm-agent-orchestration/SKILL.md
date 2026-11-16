---
name: tm-agent-orchestration
description: Multi-agent coordination, structured task delegation, parallel DAG execution, session recovery, approval checkpoints, and result aggregation across Antigravity, Hermes, Hamzad, and coding harnesses.
---

# TM Agent Orchestration (`tm-agent-orchestration`)

> **Standard Agent Skill for Molavi Agentic OS & TM Second Brain Ecosystem.**  
> Inspired by **HKUDS/AutoSwarm** principles, built on zero-external-dependency standard Python.

## Core Capabilities
- **Multi-Agent Delegation:** Maps subtasks to best-fit agent roles with explicit inputs and handover acceptance criteria.
- **Parallel DAG Execution:** Runs independent subtasks concurrently while strictly enforcing topological dependencies.
- **Structured Inter-Agent Communication:** Passes secret-redacted `TaskEnvelope` payloads between agents.
- **Durable Session Recovery:** Checkpoints execution progress to allow resumption of interrupted sessions without duplicate side effects.
- **Approval Checkpoints:** Pauses sensitive or high-risk tasks until an explicit human operator ticket is approved.
- **Result Aggregation & Conflict Detection:** Verifies Foreman evidence artifacts and catches contradictory outputs across agents.

## Usage
```python
from tm_second_brain.orchestration import AgentOrchestrator, TaskUnit, RiskLevel
# or via molavi-agentic-os
```
