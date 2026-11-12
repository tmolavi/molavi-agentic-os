# Changelog

All notable changes to **Molavi Agentic OS** are documented in this file.

## [0.2.0] - 2026-11-12

### Added
- **PyPI Package Integration (`molavi-agentic-os`):** Standardized packaging with `pyproject.toml`, console scripts (`molavi-agentic-os`, `tm-agentic-os`), automated build, and GitHub Actions Trusted Publishing workflow (`.github/workflows/publish-pypi.yml`).
- **TM Tool Registry & MCP Gateway (`molavi_agentic_os/tools/` & `molavi_agentic_os/mcp/`):**
  - Schema-validated tool registry with JSON Schema input/output checking and execution telemetry.
  - Model Context Protocol (MCP) gateway compliant with protocol version `2024-11-05`.
  - Perplexity Bumblebee-inspired `BumblebeeMCPSecurityAuditor` for static tool analysis, command injection blocks (`rm -rf`, `curl | bash`), and path traversal sanitization.
- **Autoresearch Experiment Loop (`molavi_agentic_os/evaluation/autoresearch.py`):**
  - Inspired by Andrej Karpathy's Autoresearch: automated metric tracking, hypothesis evaluation, keep/revert decision engine, and reproducible research ledgers.
- **Hermes Personal Desktop Adapter (`molavi_agentic_os/adapters/hermes_desktop.py`):**
  - Dedicated adapter for local desktop file isolation, sandboxing, and personal workflow boundaries across macOS local and Finland server runtimes.
- **TM Second Brain Memory Bridge (`molavi_agentic_os/memory/second_brain.py`):**
  - Native integration with `tm-second-brain` for local-first Markdown/Obsidian memory with YAML frontmatter, conflict-free state, and `.audit_log.jsonl` provenance.
- **Expanded Curated Skills Collection (24 Skills total):**
  - Added Agent Engineering (`agent-engineering`), Repository Analysis (`repository-analysis`), Document Intelligence (`document-intelligence`), AI Search Visibility (`ai-search-visibility`), Web Intelligence (`web-intelligence`), Systematic Debugging (`debugging`), Bumblebee MCP Audit (`bumblebee-mcp-audit`), Autonomous Experiment Evaluation (`autonomous-experiment-eval`), and Autonomous Research Loop (`autonomous-research-loop`).
- **End-to-End Runnable Examples:**
  - `examples/end_to_end_agent_workflow.py`: Canonical user prompt → agent selection → skill discovery → MCP execution → structured output → Foreman verification → evaluation score.
  - `examples/multi_agent_handoff_team.py`: Multi-agent team with explicit JSON Schema handoff contracts.
  - `examples/failure_recovery_workflow.py`: Resilient workflow execution with exponential backoff and Free-First fallback routing.
  - `examples/autoresearch_experiment_eval.py`: Autoresearch experiment loop with keep/revert decisions.
- **Intellectual Property & Provenance Governance:**
  - Added `LICENSE_COMPATIBILITY.md` detailing the 6 reference upstream repositories (Karpathy Autoresearch, Nanochat, Raschka LLMs from scratch, Forrest Chang Karpathy skills, Composio Awesome Claude Skills, Perplexity Bumblebee).
  - Enhanced `SOURCES.md` and `THIRD_PARTY_NOTICES.md`.
  - Added `.env.example` with zero-leak configuration guidelines.
- **Multilingual Documentation Suite v2:**
  - Complete 5-language documentation in English (`docs/en/README.md`), Persian (`docs/fa/README.md`), Turkish (`docs/tr/README.md`), Azerbaijani (`docs/az/README.md`), and Arabic (`docs/ar/README.md`).

## [0.1.0] - 2026-11-06

### Initial Production MVP Release
- **Comprehensive System Design:** Complete ground-up architecture of 12 specialist agents, 15 skills, and zero-dependency orchestration documented in `SYSTEM_ARCHITECTURE.md`.
- **12 Production-Ready Specialist Agents:**
  - `research-agent`, `seo-auditor`, `geo-auditor`, `ai-visibility-analyst`, `content-strategist`, `content-writer`, `fact-checker`, `code-reviewer`, `developer-agent`, `marketing-analyst`, `lead-researcher`, `project-manager`.
  - All 12 agents achieve a 100/100 Bot-Ready validation score.
- **15 Standardized Agent Skills (`SKILL.md`):**
  - Web research, Technical SEO, GEO Visibility, Content Briefs, Unslop Humanizer, Fact Checking, Code Review, Permission-Slip, Foreman Verification, Task Queue, Lead Qualification, Outreach Drafting, Second Brain Memory, Free Model Router, and Privacy Opt-Out.
- **5 Multi-Agent Team Topologies:**
  - SEO & GEO Research Team, AI Visibility Audit Team, Content Production Team, Software Development Team, Lead Generation & Outreach Team.
- **5 Canonical Workflows:**
  - Research to Report, Keyword to Content, GEO Audit Flow, Lead to Outreach, Task Parallel Execution.
- **Pure-Python Orchestration Layer:**
  - Zero-dependency thread-safe `TaskQueue` and `OrchestrationEngine` with DAG resolution, timeout controls, and backoff retries.
- **Permission-Slip Security Daemon:**
  - HMAC-signed approval tickets for L2 sensitive operations.
- **Foreman Verification Gate:**
  - "No-guessing" anti-hallucination artifact validator.
- **Free-First Model Router:**
  - Task-based routing prioritizing local Ollama, Groq free-tier, and Gemini free-tier.
- **Multi-Platform Adapters:**
  - Full export support for Antigravity, OpenAI Codex / Cursor, Claude Code, Hermes Agent, and Generic CLI.
- **Multilingual Documentation:**
  - Complete documentation in English, Persian (فارسی), Turkish (Türkçe), Azerbaijani (Azərbaycan), and Arabic (العربية).
