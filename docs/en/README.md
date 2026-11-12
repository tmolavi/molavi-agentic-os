# TM Molavi Agentic OS — English Documentation

<p align="center">
  <strong>An Open-Source, Modular Operating Ecosystem for Autonomous AI Agents, Skills, Multi-Agent Teams, Workflows, Memory & Cross-Runtime Execution.</strong><br>
  <em>Build Smarter Agents. Orchestrate Better Teams. Automate Production Systems with Verifiable Proof.</em>
</p>

<p align="center">
  <a href="https://pypi.org/project/molavi-agentic-os/"><img src="https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=flat-square" alt="PyPI Version"></a>
  <a href="https://github.com/tmolavi/molavi-agentic-os/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/tmolavi/molavi-agentic-os/ci.yml?branch=main&label=CI&style=flat-square" alt="CI Status"></a>
  <a href="../../LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License: MIT"></a>
  <a href="../../MODEL-REQUIREMENTS.md"><img src="https://img.shields.io/badge/Cost-$0.00%20Marginal%20(Free--First)-brightgreen?style=flat-square" alt="Cost: $0.00"></a>
  <a href="https://molavi.pro"><img src="https://img.shields.io/badge/Architect-Taghi%20Molavi-orange?style=flat-square" alt="Taghi Molavi"></a>
</p>

---

## 🌍 Language Navigation
- [English (Root)](../../README.md)
- [English (Full Docs)](README.md)
- [فارسی (Persian)](../fa/README.md)
- [Türkçe (Turkish)](../tr/README.md)
- [Azərbaycan dili (Azerbaijani)](../az/README.md)
- [العربية (Arabic)](../ar/README.md)

---

## 1. Project Overview & Philosophy

**TM Molavi Agentic OS** is an open-source, model-agnostic operating framework developed under the **TM (Taghi Molavi) Open Source ecosystem**.

Unlike fragile prompt libraries or heavy monolithic agent runtimes that depend on massive infrastructure (Redis, Celery, Docker daemons, or mandatory cloud subscriptions), TM Molavi Agentic OS provides a **zero-dependency, local-first architecture**:

1. **Free-First Model Routing:** Runs natively on local open-weight models (Ollama: Llama 3.2, Mistral) and zero-cost cloud tiers (Groq, Gemini Free Tier) before escalating to paid commercial APIs.
2. **Permission-Slip Security (`L2_HUMAN_APPROVAL`):** All sensitive operations (sending emails, database mutations, code deployments, trade executions) require cryptographically signed HMAC approval tickets.
3. **Foreman Anti-Hallucination Gate:** Golden Rule: *"It is not allowed to guess."* Agents cannot declare a task complete without tangible, verifiable artifact evidence.
4. **Bumblebee MCP Security:** Static analysis of tool definitions and dynamic inspection of invocation arguments to eliminate prompt injections, unsafe shell executions (`rm -rf`, `curl | bash`), and path traversals.
5. **Cross-Runtime Adapters:** Native export and bidirectional interoperability with **Hermes Main**, **Hermes Personal Desktop**, **Antigravity IDE**, **OpenAI Codex / Cursor**, and **Claude Code**.

---

## 2. Core System Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  Runtime Adapters:                                                     │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  Multi-Agent Teams & Canonical Workflows:                              │
│  • SEO & GEO Research Team         • Autonomous Research Loop          │
│  • AI Search Visibility Team       • Multi-Agent Handoff Pipeline      │
│  • Content Production Team         • Failure Recovery & Retries        │
│  • Lead Generation & Outreach      • Security & Audit Verification     │
├────────────────────────────────────────────────────────────────────────┤
│  Specialist Agents (100/100 Bot-Ready Score):                          │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  Orchestration & Verification Subsystems:                              │
│  • Permission-Slip HMAC Human Approval Gatekeeper                      │
│  • Foreman 'No-Guessing' Artifact Verification Gate                    │
│  • Thread-Safe TaskQueue & DAG Runner (Zero Celery / Redis required)   │
│  • TM Second Brain Adapter (Markdown/Obsidian Vault Memory)            │
│  • Bumblebee MCP Gateway & Tool Security Auditor                       │
│  • Autoresearch Experiment Loop & Metric Ledger                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Installation & Packaging

### Option A: Install from PyPI
```bash
pip install molavi-agentic-os
```

### Option B: Local Editable Installation
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### Build Distributions Locally
```bash
python setup.py sdist bdist_wheel
```

---

## 4. Configuration (`.env.example`)

Copy the configuration template to `.env`:
```bash
cp .env.example .env
```
Key configuration parameters:
- `TM_HMAC_SECRET_KEY`: Minimum 32-character secret key for signing approval tickets.
- `OLLAMA_BASE_URL`: Local Ollama daemon URL (default: `http://localhost:11434`).
- `GROQ_API_KEY`: Optional free-tier Groq API key.
- `GEMINI_API_KEY`: Optional free-tier Google Gemini key.
- `TM_SECOND_BRAIN_VAULT_PATH`: Path to your local Markdown/Obsidian memory vault.

---

## 5. Quickstart & CLI Commands

### 1. Validate All Agents & Skills (100/100 Bot-Ready Score)
```bash
molavi-agentic-os validate
```

### 2. List Ecosystem Components
```bash
molavi-agentic-os list all
```

### 3. Export Agent for Target Runtimes
```bash
# Export for Hermes Main
molavi-agentic-os install --platform hermes --agent research-agent

# Export for Antigravity IDE
molavi-agentic-os install --platform antigravity --agent developer-agent

# Export for Codex / Cursor
molavi-agentic-os install --platform codex --agent seo-auditor
```

---

## 6. Runtime Integrations

### A. Hermes Main & Hermes Desktop
- **Hermes Main:** Distributed agent orchestration, remote tool invocation over WebSocket / stdio.
- **Hermes Desktop:** Local process sandboxing, personal file access boundaries, and local `.tm-brain` Obsidian memory integration.

### B. Antigravity IDE
- Surgical coding agent behaviors, automated test verification, and project-level `.gemini/` instruction export.

### C. Codex & Claude Code
- Strict schema adherence, `.cursorrules` and `CLAUDE.md` compatibility, and least-privilege tool execution.

---

## 7. Memory & Knowledge Infrastructure (`tm-second-brain`)

TM Molavi Agentic OS natively connects to [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain):
- Local-first Markdown files with YAML frontmatter.
- Non-destructive conflict resolution with append-only `.audit_log.jsonl`.
- Environment isolation across namespaces (`hamzad-core`, `hermes-main`, `hermes-desktop`).

---

## 8. Security & Human Approval Model

All high-privilege actions default to **L2_HUMAN_APPROVAL**:
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key")
ticket = mgr.create_ticket(
    action="send_email",
    reason="Outreach to prospective enterprise partner",
    target="partner@enterprise.com",
    impact="External email communication",
    risk="HIGH"
)
print(f"Ticket ID: {ticket.ticket_id} | Status: {ticket.status.value}")
```

---

## 9. Troubleshooting & Governance

Run the automated governance suite to verify 100% compliance:
```bash
python scripts/check_governance.py
```
Run the full test suite:
```bash
pytest -v
```

---

## 10. Upstream Sources & License

Distributed under the **MIT License**. For complete provenance regarding Karpathy Autoresearch, Nanochat, Sebastian Raschka's LLMs from Scratch, Composio Awesome Claude Skills, and Perplexity Bumblebee, consult [`SOURCES.md`](../../SOURCES.md) and [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md).
