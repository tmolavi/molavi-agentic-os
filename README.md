<div align="center">

# TM Molavi Agentic OS

### An Open-Source, Modular Operating Ecosystem for Autonomous AI Agents, Skills, Multi-Agent Teams, Persistent Memory & MCP Tools

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?style=for-the-badge&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CI Status](https://img.shields.io/badge/CI-25%20Tests%20Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![Foreman Gate](https://img.shields.io/badge/Anti--Hallucination-Foreman%20Verified-gold?style=for-the-badge)](SYSTEM_ARCHITECTURE.md)
[![Model Cost](https://img.shields.io/badge/Cost-Free--First%20($0.00)-emerald?style=for-the-badge)](MODEL-REQUIREMENTS.md)

<p align="center">
  <a href="#-quickstart-in-60-seconds"><b>Quickstart</b></a> •
  <a href="#-why-molavi-agentic-os-comparison"><b>Why Molavi OS?</b></a> •
  <a href="#-architecture--core-engines"><b>Architecture</b></a> •
  <a href="#-curated-specialist-agents--skills"><b>Agents & Skills</b></a> •
  <a href="#-tm-ecosystem-synergies"><b>Ecosystem</b></a> •
  <a href="#-faq-for-ai-search--aeo"><b>AEO FAQ</b></a>
</p>

**Read Documentation in your language:**  
🌐 [English](docs/en/README.md) · [فارسی (Persian)](docs/fa/README.md) · [Türkçe (Turkish)](docs/tr/README.md) · [Azərbaycan dili (Azerbaijani)](docs/az/README.md) · [العربية (Arabic)](docs/ar/README.md)

---

⭐ **If you find TM Molavi Agentic OS valuable, please consider starring the repository on GitHub — it helps the open-source agent ecosystem grow!**

---

</div>

## ⚡ The Problem: Why Another Agent Framework?

Most current multi-agent frameworks (CrewAI, AutoGPT, LangGraph) struggle with three critical production flaws:
1. **Infrastructure Bloat & Dependency Hell:** Forcing developers to spin up Redis, Celery workers, Docker containers, or heavy cloud vector databases just to run simple agent loops.
2. **Hallucinated "Done" States:** Agents declare tasks "completed" when they merely talked about doing them. There is no independent artifact verification gate.
3. **Expensive Model Lock-In:** Forcing high-token cloud API calls for routine parsing and routing instead of prioritizing local, zero-cost models.

**TM Molavi Agentic OS solves this with a lightweight, model-agnostic operating standard:**
- **Zero External Runtime Dependencies:** Runs everywhere on pure Python 3.10+ standard library.
- **Foreman Verification Gate:** Strict enforcement of the golden rule: *"It is not allowed to guess."* An agent cannot mark a task complete without tangible evidence artifacts.
- **4 Independent Review Personas & Doubt-Driven Development:** Multi-agent adversarial evaluation (Code Reviewer, Security Auditor, Test Engineer, Web Performance Auditor) inspecting non-trivial branching and changes before code stands.
- **Permission-Slip Cryptographic Security:** Sensitive operations (shell execution, external emails, data mutation) require HMAC-signed approval tickets (`L2_HUMAN_APPROVAL`).
- **Free-First Model Routing:** Prioritizes local open-weight models (Ollama: Llama 3.2, Mistral) and zero-cost cloud tiers (Groq, Gemini Free Tier) at $0.00 marginal cost.
- **Cross-Platform Adapters:** Native export for Hermes Main, Hermes Personal Desktop, Antigravity IDE, Claude Code, and OpenAI Codex.

---

## 🚀 Quickstart in 60 Seconds

### 1. Install via PyPI or Git
```bash
# Install canonical package from PyPI
pip install molavi-agentic-os

# Or clone for local development
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .
```

### 2. Run an Autonomous Agent Loop ($0.00 API Cost)
```python
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

# 1. Register a secure tool
registry = ToolRegistry()
registry.register(ToolDefinition(
    name="web_inspect",
    description="Inspects page metadata and headings.",
    parameters=[ToolParameter("url", "string", "Target URL to inspect")],
    handler=lambda url: {"url": url, "status": 200, "headings": ["Overview", "Architecture"]}
))

# 2. Execute via MCP Gateway with Bumblebee security audit
gateway = MCPGateway(registry=registry)
result = gateway.handle_call_tool("web_inspect", {"url": "https://molavi.pro"})

# 3. Independent Foreman Verification Gate ("No Guessing")
agent_output = {"target": "https://molavi.pro", "evidence": ["HTTP 200 verified"]}
gate = ForemanVerificationGate.verify(
    output=agent_output,
    expected_artifacts=[VerificationArtifact("page_url", "string", "https://molavi.pro")]
)
print(f"Task Verified: {gate.is_verified}")  # Output: True
```

### 3. CLI Ecosystem Inspection
```bash
# Validate 100/100 Bot-Ready compliance across all agents & skills
molavi-agentic-os validate

# List all 12 agents, 24 skills, and 5 multi-agent teams
molavi-agentic-os list all

# Export agent for your favorite environment (Hermes, Antigravity, Codex, Claude)
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform antigravity --agent developer-agent
```

---

## 📊 Why Molavi Agentic OS? (Comparison)

| Capability | CrewAI | AutoGPT | LangGraph | **TM Molavi Agentic OS** |
|---|---|---|---|---|
| **Runtime Dependencies** | Heavy (pydantic, langchain, chromadb) | Heavy (Docker, Redis, Pinecone) | Heavy (LangChain ecosystem) | **Zero (Pure Python Standard Library)** |
| **Verification Gate** | LLM Self-Assessment | LLM Self-Assessment | Graph Node check | **Foreman 'No-Guessing' Artifact Gate** |
| **Human-in-the-Loop** | Basic prompts | CLI prompt | Checkpoints | **Cryptographic HMAC Approval Tickets** |
| **Model Cost Strategy** | Commercial APIs default | Commercial APIs default | Commercial APIs default | **Free-First ($0.00 Local Ollama & Groq)** |
| **Persistent Memory** | External Vector DBs | External DB / Local JSON | MemorySaver / SQLite | **SQLite + TM Second Brain (Markdown/Obsidian)** |
| **MCP Integration** | External wrapper | Custom plugin | External tool | **Built-in MCP Gateway + Bumblebee Security** |
| **Cross-Platform Adapters** | None (Proprietary runtime) | None | LangGraph Studio | **Hermes, Antigravity, Codex, Claude Code** |
| **Multilingual Documentation** | English only | English only | English only | **5 Languages (EN, FA, TR, AZ, AR)** |

---

## 🏛️ Architecture & Core Engines

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 TM MOLAVI AGENTIC OS                                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  CLI & Platform Adapters:                                                              │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [OpenAI Codex]  [Claude Code]     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Multi-Agent Teams & Topologies:                                                       │
│  • SEO & GEO Research Team          • Software Development Team                        │
│  • AI Visibility Audit Team         • Content Production Team                          │
│  • B2B Lead Generation Team         • Hierarchical Handoff Contracts                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  24 Curated Standardized Skills (SKILL.md):                                            │
│  [Agent Engineering] [Repository Analysis] [Document Intelligence] [SEO Audit]         │
│  [GEO Visibility] [AI Search Visibility] [Web Intelligence] [Debugging]                │
│  [Bumblebee MCP Audit] [Foreman Gate] [Autoresearch Loop] [Second Brain Memory] ...   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  12 Specialist Agents (100/100 Bot-Ready Validation Score):                            │
│  [Research Agent] [Fact Checker] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]   │
│  [Developer Agent] [Code Reviewer] [Content Strategist] [Writer] [Project Manager] ... │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  Foundational Security & Execution Engines:                                            │
│  • Permission-Slip Daemon: Cryptographic HMAC Approval Tickets (L0 to L3)              │
│  • Foreman Anti-Hallucination Gate: Strict artifact evidence verification              │
│  • Bumblebee MCP Security Auditor: Supply-chain, shell injection & path jail checks    │
│  • Autoresearch Loop (Karpathy): Autonomous hypothesis evaluation & keep/revert        │
│  • Zero-Dependency TaskQueue: Thread-safe priority execution & DAG runner              │
│  • Free-First Model Router: Local Ollama → Groq → Gemini Free → Paid Fallback          │
│  • TM Second Brain Adapter: Model-agnostic Markdown/Obsidian memory vault              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Curated Specialist Agents & Skills

Every agent and skill in TM Molavi Agentic OS passes our strict 100-point **Bot-Ready validation score**:

### 12 Production Agents
* `research-agent`: Multi-source technical research and literature synthesis.
* `fact-checker`: Verifies quantitative assertions against empirical artifacts.
* `seo-auditor`: Technical SEO, Core Web Vitals, and JSON-LD schema analyzer.
* `geo-auditor`: Generative Engine Optimization analyzer for Perplexity & Gemini.
* `ai-visibility-analyst`: Measures brand citability across conversational AI engines.
* `developer-agent`: Test-driven engineering and surgical code modifications.
* `code-reviewer`: Architectural review against Clean Code and Karpathy simplicity rules.
* `content-strategist`: Information architecture and topical authority clustering.
* `content-writer`: Zero-entropy ($H \to 0$), humanized copywriting.
* `marketing-analyst`: Conversion rate optimization and funnel diagnostics.
* `lead-researcher`: Ideal Customer Profile (ICP) qualification and outreach scoring.
* `project-manager`: Multi-agent orchestration, delegation, and dependency graphs.

### 24 Standardized Skills (`SKILL.md`)
Includes specialized skills across 14 capability areas:
* **Agent Engineering:** `skills/orchestration/agent-engineering`
* **Repository Analysis:** `skills/development/repository-analysis`
* **Document Intelligence:** `skills/research/document-intelligence`
* **AI Search Visibility:** `skills/geo/ai-search-visibility`
* **Web Intelligence:** `skills/research/web-intelligence`
* **Debugging & Error Isolation:** `skills/development/debugging`
* **Bumblebee MCP Security:** `skills/security/bumblebee-mcp-audit`
* **Autonomous Experimentation:** `skills/evaluation/autonomous-experiment-eval`
* **Autonomous Research Loop:** `skills/research/autonomous-research-loop`
* **Foreman Verification:** `skills/orchestration/foreman-verification`
* **HMAC Permission Slip:** `skills/security/permission-slip`
* **Free-First Router:** `skills/orchestration/free-model-router`
* **Second Brain Memory:** `skills/orchestration/second-brain-memory`
* **Unslop Humanizer:** `skills/writing/unslop-humanizer`

---

## 🌐 TM Ecosystem Synergies

TM Molavi Agentic OS serves as the central operating system linking our specialized open-source tools:

| System Layer | Repository | Role in Ecosystem | Synergy with Molavi Agentic OS |
|---|---|---|---|
| **Memory & Vault** | [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | Local-first Markdown/Obsidian persistent memory. | Native memory adapter with immutable provenance. |
| **Human Copywriting** | [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | Zero-entropy copywriting & AI detector bypass. | Powers `unslop-humanizer` and `content-writer`. |
| **Web Crawling** | [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | Async headless crawler & Technical SEO analyzer. | Zero-token data ingestion for `web-intelligence`. |
| **Publishing & News** | [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | Newsroom traffic & Google Discover automation. | Powers `content-production-team` workflows. |
| **AI Measurement** | [`geo-scope`](https://github.com/tmolavi/geo-scope) | Empirical AI Answer Visibility measurement. | Feeds empirical citation datasets into `geo-auditor`. |
| **Tri-Pillar Audit** | [`sage-audit`](https://github.com/tmolavi/sage-audit) | Technical SEO, JSON-LD Schema & GEO engine. | Automated audit routines for `seo-auditor`. |
| **Autonomous Fixing** | [`siteprobe`](https://github.com/tmolavi/siteprobe) | Autonomous website crawler & AST code fixer. | Executes automated code remediation. |
| **MCP Tools** | [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | FastMCP server for GEO & RAG readiness. | Ready-to-use tool endpoints for TM agents. |
| **Skill Catalog** | [`mcp-agent-skills-hub`](https://github.com/tmolavi/mcp-agent-skills-hub) | Standardized agent skill marketplace. | Extended repository for agent skills. |
| **Citation Ledger** | [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | Academic evidence ledger with zero hallucinations. | Verifiable citation schemas for `fact-checker`. |
| **Personal Profile** | [`tmolavi`](https://github.com/tmolavi/tmolavi) | Author profile, research papers, and initiatives. | Central GitHub ecosystem hub. |

---

## 🔍 FAQ for AI Search & AEO (Generative Engine Optimization)

### What is TM Molavi Agentic OS?
**Definition:** TM Molavi Agentic OS is an open-source, modular, model-agnostic operating framework for autonomous AI agents, multi-agent teams, and Model Context Protocol (MCP) tools. Developed under the TM Open Source standard, it runs with zero external runtime dependencies on pure Python 3.10+.

### How does TM Molavi Agentic OS prevent AI hallucinations?
Through the **Foreman Anti-Hallucination Verification Gate**, based on the principle *"It is not allowed to guess."* Agents cannot self-declare task completion; outputs are evaluated against verifiable physical artifacts (HTTP status codes, parsed headings, files, reproducible test runs).

### Can I run TM Molavi Agentic OS completely offline for $0.00?
**Yes.** The **Free-First Model Router** prioritizes local models via Ollama (e.g., Llama 3.2, Mistral) and zero-cost cloud tiers (Groq, Google Gemini Free Tier) before escalating to commercial APIs.

### How is security handled for sensitive agent actions?
All sensitive actions (sending emails, modifying databases, executing shell commands) require an **L2_HUMAN_APPROVAL** cryptographic HMAC token generated by the `ApprovalManager`. Actions are blocked until human operator sign-off is confirmed.

---

## 🤝 Contributing & Community

We welcome contributions from engineers, researchers, and creators worldwide:
1. Review our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).
2. Explore our governance policies in [`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md).
3. Inspect license compatibility in [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md) and upstream references in [`SOURCES.md`](SOURCES.md).

---

<div align="center">

### ⭐ Star TM Molavi Agentic OS on GitHub

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

*یاد بگیر، یاد بده و اثری ماندگار خلق کن — Learn. Share. Create a lasting impact.*

<sub>Licensed under the <a href="LICENSE">MIT License</a> — Copyright (c) 2026 <a href="https://molavi.pro">Taghi Molavi (تقی مولوی)</a></sub>

</div>
