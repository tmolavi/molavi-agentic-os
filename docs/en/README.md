# TM Molavi Agentic OS — Complete Documentation (English)

Welcome to the comprehensive technical documentation for **TM Molavi Agentic OS** (`molavi-agentic-os`).

---

## Table of Contents
1. [Project Overview & Philosophy](#1-project-overview--philosophy)
2. [System Architecture & Engines](#2-system-architecture--engines)
3. [Installation & Requirements](#3-installation--requirements)
4. [Configuration (.env & Model Tiers)](#4-configuration-env--model-tiers)
5. [Quick Start & Basic Usage](#5-quick-start--basic-usage)
6. [Runtime Platform Adapters](#6-runtime-platform-adapters)
7. [Skill Development Guide](#7-skill-development-guide)
8. [Agent Development Guide](#8-agent-development-guide)
9. [Team & Workflow Topologies](#9-team--workflow-topologies)
10. [Security & Human Approval (Permission Slip)](#10-security--human-approval-permission-slip)
11. [Evaluation & Autoresearch Loops](#11-evaluation--autoresearch-loops)
12. [Troubleshooting & FAQ](#12-troubleshooting--faq)
13. [License & Third-Party Notices](#13-license--third-party-notices)

---

## 1. Project Overview & Philosophy

**TM Molavi Agentic OS** is an open-source, modular, model-agnostic operating framework for autonomous AI agents, multi-agent teams, persistent memory, and Model Context Protocol (MCP) tools.

### Core Principles
1. **Zero External Runtime Dependencies:** Runs on pure Python 3.10+ standard library.
2. **Free-First Model Routing:** Local open-weight models (Ollama: Llama 3.2, Mistral) and zero-cost cloud tiers (Groq, Gemini Free Tier) at $0.00 marginal cost.
3. **Foreman Anti-Hallucination Gate:** *"It is not allowed to guess."* Agents must provide verifiable artifact evidence.
4. **Cryptographic HMAC Security:** Sensitive operations require `L2_HUMAN_APPROVAL` tokens.
5. **Universal Portability:** Native adapters for Hermes Main, Hermes Personal Desktop, Antigravity IDE, Claude Code, and OpenAI Codex.

---

## 2. System Architecture & Engines

The ecosystem is organized into decoupled, independently testable modules:
* `core/`: Agent definitions, skill specifications, team topologies, and validation contracts.
* `tools/` & `mcp/`: JSON-Schema tool registry, stdio MCP gateway, and Bumblebee security auditor.
* `memory/`: SQLite episodic store, fast working scratchpad, and TM Second Brain Markdown vault bridge.
* `security/`: Permission-slip HMAC approval tickets and prompt injection guardrails.
* `providers/`: Free-first model router with quota management and graceful fallback.
* `evaluation/`: Output evaluator, Foreman artifact gate, and Karpathy-inspired Autoresearch loop.
* `adapters/`: Runtime export adapters for Hermes, Antigravity, Claude Code, and Codex.

---

## 3. Installation & Requirements

### Requirements
* Python 3.10 or higher
* No mandatory cloud infrastructure, external databases, or Docker daemons.

### Installation via PyPI
```bash
pip install molavi-agentic-os
```

### Installation from Source
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .
```

---

## 4. Configuration (.env & Model Tiers)

Copy the configuration template:
```bash
cp .env.example .env
```

Configure your preferred parameters:
* `TM_APPROVAL_HMAC_SECRET`: 32+ character key for cryptographic approval tokens.
* `OLLAMA_HOST`: Local Ollama URL (default: `http://localhost:11434`).
* `TM_BRAIN_VAULT_PATH`: Local path to Markdown/Obsidian memory vault.

---

## 5. Quick Start & Basic Usage

```python
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

registry = ToolRegistry()
registry.register(ToolDefinition(
    name="system_summary",
    description="Returns system metrics.",
    parameters=[ToolParameter("target", "string", "System target name")],
    handler=lambda target: {"target": target, "status": "active", "load": 0.12}
))

gateway = MCPGateway(registry=registry)
call_res = gateway.handle_call_tool("system_summary", {"target": "agent-cluster"})
print(call_res)
```

---

## 6. Runtime Platform Adapters

Export agents, skills, and teams to your development environment:
```bash
# Export for Hermes Agent
molavi-agentic-os install --platform hermes --agent research-agent

# Export for Antigravity IDE
molavi-agentic-os install --platform antigravity --agent developer-agent

# Export for OpenAI Codex / Cursor
molavi-agentic-os install --platform codex --agent seo-auditor

# Export for Claude Code
molavi-agentic-os install --platform claude-code --agent content-writer
```

---

## 7. Skill Development Guide

Every skill is defined as a `SKILL.md` document with structured YAML frontmatter:
```markdown
---
name: Skill Name
description: Clear, action-oriented description.
category: orchestration | development | research | seo | geo | security
version: 1.0.0
author: Author Name
license: MIT
---

# Skill Title
...
```

Run validation:
```bash
molavi-agentic-os validate
```

---

## 8. Agent Development Guide

Agents are defined in YAML or Python using `AgentDefinition`:
* Explicit role and purpose (>15 characters).
* Deterministic JSON input/output schemas.
* Minimum of 2 execution boundaries.
* Permission level (`L0_READ_ONLY`, `L1_DRAFT_RECOMMEND`, `L2_HUMAN_APPROVAL`, `L3_PRE_AUTHORIZED`).

---

## 9. Team & Workflow Topologies

Support for 5 multi-agent team configurations:
1. **SEO & GEO Research Team:** Coordinator, SEO Auditor, GEO Auditor, Fact-Checker.
2. **AI Visibility Audit Team:** Analyst, Prompt Researcher, Citability Scorer.
3. **Software Development Team:** PM Agent, Developer Agent, Code Reviewer.
4. **Content Production Team:** Strategist, Humanized Writer, Fact-Checker.
5. **B2B Lead Generation Team:** ICP Researcher, Marketing Analyst, Human Approval Gatekeeper.

---

## 10. Security & Human Approval (Permission Slip)

All sensitive actions require HMAC-signed approval tickets:
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="secure-key")
ticket = mgr.create_ticket(
    action="send_email",
    reason="Outreach to partner",
    target="partner@example.com",
    impact="External email communication",
    risk="HIGH"
)
```

---

## 11. Evaluation & Autoresearch Loops

Inspired by Andrej Karpathy's Autoresearch:
```python
from molavi_agentic_os.evaluation import AutoresearchLoop, ResearchHypothesis

hypothesis = ResearchHypothesis(
    id="EXP-01",
    target_component="prompt_engineering",
    hypothesis_statement="Lower temperature to 0.2",
    baseline_metric=0.65,
    target_metric_key="accuracy"
)
loop = AutoresearchLoop(hypothesis)
```

---

## 12. Troubleshooting & FAQ

* **ModuleNotFoundError:** Ensure package is installed via `pip install -e .`.
* **Tests Failing:** Run `python3 -m pytest tests/ -v`.
* **Missing Secrets:** TM Molavi Agentic OS defaults to local models and mock providers. No secrets required for tests.

---

## 13. License & Third-Party Notices

Licensed under the **MIT License**. For complete provenance, upstream references, and license compatibility, see:
* [`LICENSE`](../../LICENSE)
* [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md)
* [`SOURCES.md`](../../SOURCES.md)
* [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md)
