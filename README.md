# Molavi Agentic OS

<p align="center">
  <strong>An Open Ecosystem of Agents, Skills, Teams, Workflows & Tools.</strong><br>
  <em>Build Smarter Agents. Create Better Teams. Automate Real Work.</em>
</p>

<p align="center">
  <a href="https://github.com/tmolavi/molavi-agentic-os/actions"><img src="https://img.shields.io/badge/CI-Passing-brightgreen?style=flat-square" alt="CI Status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"></a>
  <a href="AUDIT_REPORT.md"><img src="https://img.shields.io/badge/Audit-20%20Repos%20Verified-success?style=flat-square" alt="Audit"></a>
  <a href="https://molavi.pro"><img src="https://img.shields.io/badge/Brand-Molavi.pro-orange?style=flat-square" alt="Molavi Brand"></a>
</p>

---

## 🌍 Multilingual Documentation
- [English](README.md)
- [فارسی (Persian)](docs/fa/README.md)
- [Türkçe (Turkish)](docs/tr/README.md)
- [Azərbaycan dili (Azerbaijani)](docs/az/README.md)
- [العربية (Arabic)](docs/ar/README.md)

---

## 1. Overview

**Molavi Agentic OS** is an open-source, modular, model-agnostic AI agent operating framework developed under the **Molavi brand** by **Taqi Molavi** (AI Systems Architect, SEO & GEO Strategist).

Unlike marketing hype lists or unstructured prompt collections, Molavi Agentic OS consolidates real, tested architectural patterns into a zero-dependency, production-ready system:
- **Free-First Model Strategy:** Run out-of-the-box on local open-weight models (Ollama: Llama 3, Mistral) and zero-cost cloud tiers (Groq, Gemini Free Tier) before escalating to paid models.
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

## 3. Audited Source Repositories

This project was built following a comprehensive technical audit of 20 viral AI agent repositories. Full evaluations, license provenance, and security risk analyses are published in [AUDIT_REPORT.md](AUDIT_REPORT.md).

| Category | Studied Projects | Molavi Agentic OS Action |
|---|---|---|
| **Catalogs & Profiles** | `awesome-grok-bot`, `grok-bot-templates` | Extracted taxonomy, rewritten into 100/100 Bot-Ready schemas |
| **Org Charts & Teams** | `serenakeyitan/agent-org-chart` | Adopted hierarchical delegation protocols natively |
| **Human Approval** | `supersuit-tech/permission-slip`, `hypergrok` | Adopted HMAC approval ticket engine into core security |
| **Verification Gate** | `Archive228/foreman` | Adopted the "No-Guessing" artifact verification gate |
| **Queue & Runtime** | `grokbot-queue`, `OpenGrokBot` | Rewritten into pure-Python, zero-dependency `TaskQueue` |
| **Dangerous Root Daemons** | `head77x/grokbotos` | **STRICTLY REJECTED** due to excessive root permissions |

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
