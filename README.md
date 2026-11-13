<div align="center">

# TM Molavi Agentic OS

### Production-Grade, Model-Agnostic Operating Ecosystem for Autonomous AI Agents, Skills, Multi-Agent Teams, Workflows & Local Memory

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![Bot-Ready Score](https://img.shields.io/badge/Bot--Ready-100%2F100-purple?style=for-the-badge)](https://github.com/tmolavi/molavi-agentic-os)
[![Marginal Cost](https://img.shields.io/badge/Cost-%240.00%20(Free--First)-brightgreen?style=for-the-badge)](MODEL-REQUIREMENTS.md)

**Architected by [Taghi Molavi (تقی مولوی)](https://molavi.pro)** · *AI Systems Architect & AI Visibility Researcher*  
*یاد بگیر، یاد بده و اثری ماندگار خلق کن — Learn. Share. Create a lasting impact.*

```bash
pip install molavi-agentic-os
```

[English](README.md) · [فارسی (Persian)](README.fa.md) · [Türkçe (Turkish)](README.tr.md) · [Azərbaycan dili](README.az.md) · [العربية (Arabic)](README.ar.md) · [Detailed Docs](docs/en/README.md)

<br/>

> ⭐ **If this project saves you from heavy infrastructure sprawl or hallucinated agent outputs, please consider starring this repository! It helps the open-source ecosystem grow.**

</div>

---

## ⚡ The Production Agent Problem

Most modern AI agent frameworks suffer from three severe architectural bottlenecks when deployed in real-world systems:

1. **Infrastructure Bloat & Vendor Lock-in:** Requiring heavy background daemons (Redis, Celery, Vector DBs, Docker containers) just to run a 3-step agent pipeline, while binding workflows to expensive proprietary API models.
2. **Hallucinated "Done" States:** Agents declaring tasks "completed" without verifiable physical artifacts or reproducible proof (e.g. self-reporting that code was tested when no test command was ever executed).
3. **Security Vulnerabilities & Uncontrolled Execution:** Dangerous tool execution (`rm -rf`, uncontrolled shell commands, path traversals) without cryptographic human approval gates or MCP supply-chain audits.

**TM Molavi Agentic OS** solves this by delivering a **zero-dependency, local-first operating ecosystem** where every action is verified, every sensitive operation is human-approved via cryptographic HMAC tickets, and local open-weight models run at **$0.00 marginal cost**.

---

## 📊 Framework Comparison: Why Engineers Choose Molavi Agentic OS

| Feature / Architecture | TM Molavi Agentic OS | CrewAI | LangGraph | AutoGPT |
|---|---|---|---|---|
| **Runtime Dependencies** | **Zero (Python stdlib only)** | Heavy (Pydantic, Chroma, etc.) | Heavy (LangChain ecosystem) | Heavy (Docker, Redis, etc.) |
| **Model Cost Strategy** | **Free-First ($0.00 Ollama/Groq/Gemini)** | Default Cloud API keys | Default Cloud API keys | Default OpenAI keys |
| **Foreman Verification Gate** | **Strict "No-Guessing" Artifact Gate** | Self-reported status | User-defined checks | Unconstrained |
| **Human Approval System** | **HMAC-Signed `ApprovalTicket` (L0-L3)** | Basic callback | Interrupt pattern | CLI confirm |
| **Tool Protocol** | **Native MCP Gateway + Bumblebee Security** | Custom tool wrappers | LangChain Tools | Custom plugins |
| **Memory Engine** | **SQLite + `tm-second-brain` (Markdown/Obsidian)** | Vector DB mandatory | Checkpointer state | Memory vector store |
| **Runtime Adapters** | **Hermes, Hermes Desktop, Antigravity, Codex** | Proprietary CLI | LangGraph Cloud | Web UI only |
| **Autonomous Evaluation** | **Karpathy Autoresearch Keep/Revert Loop** | None | LangSmith (Paid SaaS) | None |

---

## 🏛️ System Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  Cross-Platform Runtime Adapters:                                      │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  Multi-Agent Teams & Production Topologies:                            │
│  • SEO & GEO Research Team         • Autonomous Research Loop          │
│  • AI Search Visibility Team       • Multi-Agent Handoff Pipeline      │
│  • Content Production Team         • Failure Recovery & Backoff        │
│  • Lead Generation & Outreach      • Systematic Debugging & Fixes      │
├────────────────────────────────────────────────────────────────────────┤
│  12 Specialist Agents (100/100 Bot-Ready Score):                       │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  24 Standardized Agent Skills (SKILL.md) & Tools Registry:             │
│  • Agent Engineering               • Bumblebee MCP Security Audit      │
│  • Repository Analysis             • Autonomous Experiment Evaluation  │
│  • Document Intelligence           • Deterministic Web Intelligence    │
│  • AI Search Visibility & GEO      • Second Brain Obsidian Memory      │
├────────────────────────────────────────────────────────────────────────┤
│  Core Orchestration & Security Subsystems:                             │
│  • Permission-Slip HMAC Human Approval Gatekeeper (L2_HUMAN_APPROVAL)  │
│  • Foreman 'No-Guessing' Artifact Verification Gate (Golden Rule)      │
│  • Zero-Dependency Thread-Safe TaskQueue & DAG Runner                  │
│  • Free-First Model Router (Ollama Llama-3.2 → Groq → Gemini Free Tier)│
│  • TM Second Brain Adapter (Local-first Markdown Vault Memory)         │
│  • Bumblebee MCP Gateway & Injection Filter                            │
│  • Karpathy-Inspired Autoresearch Keep/Revert Metric Ledger            │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quickstart in 60 Seconds

### 1. Installation
Install directly from PyPI:
```bash
pip install molavi-agentic-os
```

Or clone the repository for development:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### 2. Validate Bot-Ready Compliance (100/100 Score)
Verify all 12 agents, 24 skills, and 5 teams against the strict TM Bot-Ready scoring benchmark:
```bash
molavi-agentic-os validate
```
Output:
```text
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] fact-checker (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### 3. Run the End-to-End Pipeline
Execute the canonical user request → tool execution → Foreman verification flow:
```bash
python examples/end_to_end_agent_workflow.py
```

---

## 💡 Code Walkthroughs

### 1. Zero-Cost Free-First Model Routing
Run your agents on local Ollama models (Llama 3.2, Mistral) or zero-cost cloud tiers (Groq, Gemini Free Tier) without paying a cent:
```python
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider

router = ModelRouter()
local_model = MockProvider(fixed_response="System architecture verified offline.")
router.register_provider("ollama-llama-3.2", local_model, ModelTier.FREE_LOCAL)

response = router.route_and_generate(
    prompt="Audit system security architecture",
    preferred_tier=ModelTier.FREE_LOCAL
)
print(f"Model: {response.model_name} | Cost: ${response.estimated_cost_usd:.2f}")
```

### 2. Foreman Verification Gate ("No Guessing")
Prevent hallucinated success claims by requiring verifiable evidence artifacts:
```python
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

agent_output = {
    "status": "completed",
    "target_url": "https://molavi.pro/research",
    "evidence": ["HTTP 200 OK", "Headings extracted successfully"]
}

artifacts = [
    VerificationArtifact("url_crawled", "string", agent_output["target_url"]),
    VerificationArtifact("evidence_ledger", "list", agent_output["evidence"])
]

result = ForemanVerificationGate.verify(agent_output, artifacts)
if result.is_verified:
    print(f"✅ Foreman Approved: {result.verified_artifacts}")
else:
    print(f"❌ Rejected: {result.failure_reason}")
```

### 3. Cryptographic Human Approval (`Permission-Slip`)
Gate all sensitive external operations (emails, deployments, database writes) behind HMAC-signed approval tickets:
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key-min-32-chars")
ticket = mgr.create_ticket(
    action="deploy_production_code",
    reason="Release v0.2.0 update",
    target="prod-cluster-01",
    impact="Live service modification",
    risk="HIGH"
)
print(f"Ticket ID: {ticket.ticket_id} | Requires Human Approval: {ticket.requires_human_approval}")
```

### 4. Bumblebee MCP Tool Security Audit
Inspect tool manifests and dynamic arguments to block command injections and path traversals:
```python
from molavi_agentic_os.mcp import BumblebeeMCPSecurityAuditor

audit = BumblebeeMCPSecurityAuditor.audit_invocation_arguments({
    "file_path": "../../etc/shadow",
    "command": "rm -rf /"
})
if not audit.is_safe:
    print(f"🚨 Security Alert: Blocked unsafe execution -> {audit.issues}")
```

### 5. Karpathy Autoresearch Experiment Loop
Iteratively optimize agent prompts and context parameters with automatic keep/revert decisions:
```python
from molavi_agentic_os.evaluation import AutoresearchLoop, ResearchHypothesis

hypothesis = ResearchHypothesis(
    id="EXP-OPT-01",
    target_component="SEO Audit Prompt",
    hypothesis_statement="Lowering temperature to 0.2 improves accuracy > 5%",
    baseline_metric=0.60,
    target_metric_key="accuracy"
)
loop = AutoresearchLoop(hypothesis)
decision = loop.run_trial(
    trial_number=1,
    parameters={"temperature": 0.2},
    eval_fn=lambda p: {"accuracy": 0.72}
)
print(f"Trial 1: {decision.action} ({decision.rationale})")
```

---

## 🌐 Cross-Runtime Export Adapters

Export your agents, skills, and teams to your preferred development environment with one command:

```bash
# Export for Hermes Main (Personal AI Runtime)
molavi-agentic-os install --platform hermes --agent research-agent

# Export for Hermes Personal Desktop (Local Files & Sandbox)
molavi-agentic-os install --platform hermes-desktop --agent developer-agent

# Export for Antigravity IDE (Coding Harness)
molavi-agentic-os install --platform antigravity --agent content-writer

# Export for OpenAI Codex / Cursor (.cursorrules)
molavi-agentic-os install --platform codex --agent seo-auditor

# Export for Claude Code (CLAUDE.md)
molavi-agentic-os install --platform claude-code --agent project-manager
```

---

## 🔗 TM Ecosystem & Interconnected Repositories

TM Molavi Agentic OS serves as the central operating engine for our specialized open-source initiatives:

| Ecosystem Repository | Specialization | Synergy with Molavi Agentic OS |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | Local-First Obsidian & Markdown Memory Infrastructure | Native persistent cross-session memory adapter with immutable audit logs. |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | Empirical AI Answer Visibility Framework (Perplexity, Gemini, ChatGPT) | Supplies citation ledgers and extractability metrics to `geo-auditor`. |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | 3-Pillar Technical SEO, AEO & JSON-LD Schema Auditor | Powers technical diagnostics inside `seo-auditor`. |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | Autonomous Website Crawler & AST Code/Config Fixer | Executes automated remediation based on Agentic OS diagnostic reports. |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | Deterministic Headless Web Crawler ($0.00 Token Cost) | Zero-token data ingestion backend for research and crawling skills. |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | Zero-Entropy ($H \to 0$) Human Copywriting & Anti-Slop Engine | Native engine powering `unslop-humanizer` and technical writing agents. |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | FastMCP Server for GEO & AI Visibility Diagnostics | Standard MCP tool endpoints consumable by TM agents. |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | Autonomous Newsroom Publishing & Google News Traffic Engine | Integrates with `content-production-team` for media automation. |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | Academic Evidence Ledgers & Verifiable Manuscripts | Provides citation schemas to `fact-checker` and research agents. |
| [`mcp-agent-skills-hub`](https://github.com/tmolavi/mcp-agent-skills-hub) | Standardized Agent Skills Catalog for Coding Harnesses | Extended marketplace for portable `SKILL.md` definitions. |
| [`tmolavi`](https://github.com/tmolavi/tmolavi) | Taghi Molavi GitHub Special Profile & Architecture Map | Central brand and project portfolio hub. |

---

## 🛡️ Upstream Reference Repositories & License Compatibility

TM Molavi Agentic OS was built with deep respect for the open-source community, adopting clean-room architectural adaptations from six foundational upstream projects:

1. **Andrej Karpathy — [Autoresearch](https://github.com/karpathy/autoresearch)** (MIT): Inspired our metric-based experiment tracking, hypothesis evaluation, and keep/revert decision engine.
2. **Andrej Karpathy — [Nanochat](https://github.com/karpathy/nanochat)** (MIT): Inspired our zero-dependency, modular, understandable architecture.
3. **Sebastian Raschka — [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** (Apache 2.0): Inspired our transparent model requirements and context boundary engineering.
4. **Forrest Chang — [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** (MIT): Inspired our surgical agent diffs and "think before coding" behavioral standards.
5. **ComposioHQ — [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** (Apache 2.0): Inspired our portable `SKILL.md` schema and capability discovery registry.
6. **Perplexity AI — [Bumblebee](https://github.com/perplexityai/bumblebee)** (Apache 2.0): Inspired our MCP security auditor, supply-chain checks, and prompt-injection filters.

For full license audits and provenance, see [`SOURCES.md`](SOURCES.md), [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), and [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md).

---

## ❓ Frequently Asked Questions (FAQ / AEO)

<details>
<summary><strong>Q: Does TM Molavi Agentic OS require Docker, Redis, or Celery?</strong></summary>

**No.** TM Molavi Agentic OS is engineered with pure Python 3.10+ standard library concurrency (thread-safe `TaskQueue` and topological DAG execution). You can run complete multi-agent swarms locally on your laptop without spinning up external daemon processes.
</details>

<details>
<summary><strong>Q: How does the Free-First Model Strategy work?</strong></summary>

By default, the `ModelRouter` prioritizes local open-weight models running on Ollama (such as Llama 3.2 3B or Mistral) or zero-cost cloud tiers (Groq and Google Gemini Free Tier). Commercial API calls (OpenAI, Anthropic) are only escalated when a complex reasoning task explicitly demands them.
</details>

<details>
<summary><strong>Q: How does the Foreman Verification Gate prevent hallucinations?</strong></summary>

Under the Foreman Gate, self-reported success flags are ignored. The gate evaluates physical evidence artifacts (status codes, JSON schema matches, physical file paths, non-empty outputs) against explicit verification contracts. If artifacts are missing, the task is marked as failed or queued for retry.
</details>

<details>
<summary><strong>Q: Is this system compatible with Model Context Protocol (MCP)?</strong></summary>

**Yes.** The system includes a built-in `MCPGateway` that translates tool definitions into standard MCP schemas (`2024-11-05` protocol version) and subjects incoming arguments to Bumblebee security checks.
</details>

---

## 📈 Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

**⭐ Like this project? Give it a star on GitHub! It takes 1 second and makes a world of difference.**

</div>

---

## 📜 License & Governance

Distributed under the **MIT License**. Copyright (c) 2026 **Taghi Molavi**.  
Compliant with the **TM Open Source Standard** ([`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md)).
