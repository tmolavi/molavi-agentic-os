# TM AI Agent Toolkit

<p align="center">
  <strong>Molavi Agentic OS: An Open Ecosystem of Agents, Skills, Teams, Workflows & Tools.</strong><br>
  <em>Build Smarter Agents. Create Better Teams. Automate Real Work.</em>
</p>

<p align="center">
  <a href="https://github.com/tmolavi/molavi-agentic-os/actions"><img src="https://img.shields.io/badge/CI-Passing-brightgreen?style=flat-square" alt="CI Status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"></a>
  <a href="TM-OPEN-SOURCE-STANDARD.md"><img src="https://img.shields.io/badge/Governance-TM%20Standard-purple?style=flat-square" alt="Governance Standard"></a>
  <a href="MODEL-REQUIREMENTS.md"><img src="https://img.shields.io/badge/Model-Free--First-brightgreen?style=flat-square" alt="Model Requirements"></a>
  <a href="SYSTEM_ARCHITECTURE.md"><img src="https://img.shields.io/badge/Architecture-Verified-success?style=flat-square" alt="Architecture"></a>
  <a href="https://molavi.pro"><img src="https://img.shields.io/badge/Brand-Molavi.pro-orange?style=flat-square" alt="Molavi Brand"></a>
</p>

---

## 🏛️ Ecosystem & Governance
* **Canonical Governance Policy:** [`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md)
* **Model & Cost Transparency:** [`MODEL-REQUIREMENTS.md`](MODEL-REQUIREMENTS.md)
* **Global Ecosystem Inventory:** [`docs/repository-governance/EXISTING-REPOSITORIES.md`](docs/repository-governance/EXISTING-REPOSITORIES.md)
* **Reusable Repository Template:** [`.github/REPOSITORY_TEMPLATE/`](.github/REPOSITORY_TEMPLATE/)

---

## 🌍 Multilingual Documentation
- [English](README.md)
- [فارسی (Persian)](docs/fa/README.md)
- [Türkçe (Turkish)](docs/tr/README.md)
- [Azərbaycan dili (Azerbaijani)](docs/az/README.md)
- [العربية (Arabic)](docs/ar/README.md)

---

## 1. Overview

**TM AI Agent Toolkit** (Molavi Agentic OS) is an open-source, modular, model-agnostic AI agent operating framework developed under the **TM (Taqi Molavi) Open Source ecosystem**.

Unlike marketing hype lists or unstructured prompt collections, TM AI Agent Toolkit consolidates real, tested architectural patterns into a zero-dependency, production-ready system:
- **Free-First Model Strategy:** Run out-of-the-box on local open-weight models (Ollama: Llama 3.2, Mistral) and zero-cost cloud tiers (Groq, Gemini Free Tier) before escalating to paid models (see [`MODEL-REQUIREMENTS.md`](MODEL-REQUIREMENTS.md)).
- **Permission-Slip Security:** Default Human-in-the-Loop (`L2_HUMAN_APPROVAL`) with cryptographically signed approval tickets for any sensitive actions (emails, trades, code deployments).
- **Foreman Verification Gate:** Strict enforcement of the golden rule: *"It is not allowed to guess."* Tasks cannot be declared complete without verifiable evidence artifacts.
- **Model-Agnostic & Cross-Platform:** Native export adapters for OpenAI Codex / Cursor, Claude Code, Hermes Agent, Antigravity, and Generic CLI runtimes.

---

## 2. Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                          MOLAVI AGENTIC OS                             │
├────────────────────────────────────────────────────────────────────────┤
│  CLI & Platform Adapters:                                              │
│  [Antigravity]  [Claude Code]  [OpenAI Codex]  [Hermes]  [Generic CLI] │
├────────────────────────────────────────────────────────────────────────┤
│  Teams & Workflows:                                                    │
│  • SEO & GEO Research Team          • Research → Analysis → Report     │
│  • AI Visibility Audit Team         • Keyword → Brief → Humanized QA   │
│  • Content Production Team          • GEO Audit & Citability Flow      │
│  • Lead Generation & Outreach Team  • Lead Discovery → Approval Gate   │
│  • Software Development Team        • Parallel Task Queue DAG          │
├────────────────────────────────────────────────────────────────────────┤
│  Specialist Agents (100/100 Bot-Ready Score):                          │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  Security & Orchestration Engine:                                      │
│  • Permission-Slip Daemon (L0 to L3 HMAC Approval Tickets)             │
│  • Foreman 'No-Guessing' Artifact Verification Gate                    │
│  • Zero-Dependency Thread-Safe TaskQueue & DAG Runner                  │
│  • Local Durable SQLite Memory & Working Memory Buffer                 │
│  • Free-First Model Router (Ollama → Groq → Gemini → Paid Fallback)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Architectural Pillars

TM AI Agent Toolkit is engineered as an end-to-end, zero-dependency platform based on five foundational pillars:

| Pillar | Technical Mechanism | Production Benefit |
|---|---|---|
| **Hierarchical Team Topologies** | Formal `TeamDefinition` with coordinator, specialist roles, and delegation rules | Eliminates confusion and context pollution in multi-agent workflows |
| **Permission-Slip Human Approval** | Cryptographic HMAC-signed `ApprovalTicket` system for all L2 sensitive actions | Prevents unauthorized emails, deployments, trades, or server mutations |
| **Foreman Verification Gate** | Anti-hallucination verification requiring verifiable evidence artifacts | Eliminates fake completion claims; agents cannot declare done without proof |
| **Zero-Dependency TaskQueue** | Pure Python thread-safe priority queue and DAG execution engine | Runs anywhere without requiring Redis, Celery, Docker, or external daemon setups |
| **Free-First Model Router** | Provider-agnostic routing prioritizing local Ollama and zero-cost cloud tiers | Enables complete local offline execution at $0.00 marginal cost |

---

## 4. Quickstart

### Installation
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .
```

### Validate Ecosystem Artifacts
```bash
molavi-agentic-os validate
```
Output:
```
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### List Ecosystem Components
```bash
molavi-agentic-os list all
```

### Export for Target Platforms
```bash
# Export for OpenAI Codex / Cursor rules
molavi-agentic-os install --platform codex --agent seo-auditor

# Export for Hermes Agent
molavi-agentic-os install --platform hermes --agent research-agent

# Export for Claude Code
molavi-agentic-os install --platform claude-code --agent developer-agent

# Export for Antigravity
molavi-agentic-os install --platform antigravity --agent content-writer
```

---

## 5. Security & Human Approval Model

All sensitive actions default to **L2_HUMAN_APPROVAL**:
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secret-key")
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

## 6. Brand Positioning

**Molavi Ecosystem**  
- **Brand Owner:** Taqi Molavi  
- **Specialization:** AI Systems Architecture | SEO & GEO Strategy  
- **Brand Philosophy:** *Be Visible. Sell Better. Build Authority.*  
- **Website:** [molavi.pro](https://molavi.pro)

---

## 7. License & Attribution

- **Core Framework:** Licensed under the [MIT License](LICENSE).
- **Third-Party Attribution:** Documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [SOURCES.md](SOURCES.md).
