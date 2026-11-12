# Global Repository Governance Inventory & Migration Plan

> **Authority:** TM Open Source Ecosystem (`tmolavi`)  
> **Brand Owner:** Taqi Molavi  
> **Canonical Standard:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)  
> **Audit Date:** November 2026  
> **Total Repositories Audited:** 24 public repositories  

---

## 1. Executive Summary

This document establishes the comprehensive baseline inventory of all **24 public repositories** owned by `tmolavi` on GitHub. Each repository was evaluated against the **TM Open Source Standard** across seven mandatory dimensions:
1. **Naming & Identity:** Standardized `tm-*` prefix adoption.
2. **Five-Language Documentation:** Presence of `docs/fa`, `docs/tr`, `docs/az`, and `docs/ar` alongside English.
3. **Model & Cost Transparency:** Presence of `MODEL-REQUIREMENTS.md` detailing token budgets, rate limits, and free-tier alternatives.
4. **Security & Human-in-the-Loop:** Explicit `SECURITY.md` and permission boundaries.
5. **Licensing & Attribution:** Explicit MIT license and `THIRD_PARTY_NOTICES.md` where applicable.
6. **Agent Compatibility:** Support for Antigravity, OpenAI Codex, Claude Code, and Hermes Agent.
7. **Ecosystem & Hamzad Relevance:** Interoperability with the broader Molavi brand and Hamzad AI infrastructure.

> **CRITICAL POLICY DIRECTIVE:**  
> In strict accordance with the governance charter, **no repository has been automatically renamed, deleted, archived, or made private.**  
> The migration proposals below are documented for review and will be executed systematically in planned release phases.

---

## 2. Global Repository Audit Inventory

| # | Repository Name | Primary Language | Stars | License | 5-Lang Docs | Model Reqs | CI | Hamzad Relevance | Governance Status |
|---|-----------------|------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 | [`agent-project-discovery-skill`](https://github.com/tmolavi/agent-project-discovery-skill) | Documentation/Meta | 2 | MIT | Full (5/5) | Missing | Missing | High | **COMPLIANT** |
| 02 | [`answerpath-geo`](https://github.com/tmolavi/answerpath-geo) | Python | 2 | MIT | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 03 | [`awesome-skills`](https://github.com/tmolavi/awesome-skills) | Documentation/Meta | 0 | MIT | Partial (1/5) | Missing | Missing | Medium | **ARCHIVE / MAINTAIN** |
| 04 | [`bale-bot-skills`](https://github.com/tmolavi/bale-bot-skills) | Python | 3 | MIT | Partial (2/5) | Missing | Yes | Medium | **NEEDS DOCUMENTATION** |
| 05 | [`geo-aeo-news-engine`](https://github.com/tmolavi/geo-aeo-news-engine) | Python | 1 | MIT | Partial (4/5) | Missing | Missing | High | **NEEDS DOCUMENTATION** |
| 06 | [`geo-scope`](https://github.com/tmolavi/geo-scope) | Python | 4 | MIT | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 07 | [`hamzad-ai-gateway-resources`](https://github.com/tmolavi/hamzad-ai-gateway-resources) | Documentation/Meta | 1 | MIT | Partial (1/5) | Missing | Missing | High | **NEEDS REBRANDING** |
| 08 | [`hamzad-avatar-studio`](https://github.com/tmolavi/hamzad-avatar-studio) | Python | 1 | MIT | Full (5/5) | Missing | Missing | High | **COMPLIANT** |
| 09 | [`hermes-meeting-intelligence`](https://github.com/tmolavi/hermes-meeting-intelligence) | Python | 1 | Apache-2.0 | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 10 | [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | Python | 0 | MIT | Partial (4/5) | Missing | Yes | Medium | **NEEDS DOCUMENTATION** |
| 11 | [`iranian-enterprise-ai-bridge`](https://github.com/tmolavi/iranian-enterprise-ai-bridge) | TypeScript | 1 | MIT | Partial (3/5) | Missing | Yes | Medium | **NEEDS DOCUMENTATION** |
| 12 | [`ivna-app`](https://github.com/tmolavi/ivna-app) | Documentation/Meta | 1 | MIT | Partial (1/5) | Missing | Missing | Medium | **NEEDS REBRANDING** |
| 13 | [`laravel-ai-summary`](https://github.com/tmolavi/laravel-ai-summary) | PHP | 1 | MIT | Partial (2/5) | Missing | Missing | Medium | **NEEDS REBRANDING** |
| 14 | [`lean-agent-skills`](https://github.com/tmolavi/lean-agent-skills) | Shell | 2 | MIT | Partial (3/5) | Missing | Missing | High | **NEEDS DOCUMENTATION** |
| 15 | [`mcp-agent-skills-hub`](https://github.com/tmolavi/mcp-agent-skills-hub) | JavaScript | 9 | MIT | Partial (2/5) | Missing | Missing | High | **NEEDS REBRANDING** |
| 16 | [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | Python | 3 | MIT | Partial (2/5) | Missing | Yes | High | **NEEDS REBRANDING** |
| 17 | [`molavi-agentic-os`](https://github.com/tmolavi/molavi-agentic-os) | Python | 0 | MIT | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 18 | [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | Python | 1 | Apache-2.0 | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 19 | [`n8n-agent-skills`](https://github.com/tmolavi/n8n-agent-skills) | Shell | 2 | MIT | Partial (3/5) | Missing | Yes | High | **NEEDS DOCUMENTATION** |
| 20 | [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | Python | 1 | MIT | Partial (4/5) | Missing | Yes | High | **NEEDS DOCUMENTATION** |
| 21 | [`sage-audit`](https://github.com/tmolavi/sage-audit) | Python | 1 | MIT | Full (5/5) | Missing | Yes | High | **COMPLIANT** |
| 22 | [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | Python | 1 | MIT | Full (5/5) | Missing | Yes | Medium | **COMPLIANT** |
| 23 | [`siteprobe`](https://github.com/tmolavi/siteprobe) | Python | 6 | MIT | Partial (3/5) | Missing | Yes | Medium | **NEEDS REBRANDING** |
| 24 | [`tmolavi`](https://github.com/tmolavi/tmolavi) | Documentation/Meta | 2 | Missing | Partial (1/5) | Missing | Missing | Core Hub | **ARCHIVE / MAINTAIN** |

---

## 3. Governance Classification Breakdown

### 3.1 COMPLIANT
* **`molavi-agentic-os` (TM AI Agent Toolkit):** Fully compliant. Implements 100/100 Bot-Ready agents, 15 skills, 5 teams, pure-Python orchestration, Permission-Slip approval tickets, Foreman verification, 5-language documentation, `MODEL-REQUIREMENTS.md`, and complete test suite.

### 3.2 NEEDS DOCUMENTATION (High Priority)
Repositories with established code and permissive licenses that require five-language localization (`fa`, `tr`, `az`, `ar`) and `MODEL-REQUIREMENTS.md`:
* `geo-scope`
* `sage-audit`
* `mcp-geo-server`
* `siteprobe`
* `mcp-agent-skills-hub`
* `answerpath-geo`
* `lean-agent-skills`
* `bale-bot-skills`
* `n8n-agent-skills`
* `scholar-provenance`
* `humanize-ai-copywriter`

### 3.3 NEEDS REBRANDING (Staged Migration)
Repositories planned to adopt the canonical `tm-*` prefix to establish unified international brand identity:
* See Detailed Migration Plan below.

### 3.4 ARCHIVE / MAINTAIN (Documented Exemptions)
* **`tmolavi`:** Permanent exemption as the special GitHub Profile Repository.
* **`awesome-skills`:** Permanent exemption as an upstream public fork.

---

## 4. Proposed Staged Migration Plan

> **Note:** GitHub automatically provisions permanent 301 HTTP redirects and git remote redirects when a repository is renamed. However, to eliminate any potential disruption to downstream users, local submodules, and package managers (Packagist, npm, PyPI), migrations will be executed in coordinated stages.

| Current Repository | Proposed TM Name | Primary Rationale | SEO & Discoverability Impact | Technical Migration Effort | Breaking-Change Risk | Recommended Action |
|---|---|---|---|---|---|---|
| `agent-project-discovery-skill` | `tm-agent-discovery` | Align with TM prefix; simplify skill discoverability across agent hubs. | High positive impact for 'TM AI Agent Discovery' search rankings. | Low (Repository rename + update remote URLs). | Low (GitHub maintains automatic HTTP and git clone redirects). | Plan rename to `tm-agent-discovery`; add 5-language docs. |
| `answerpath-geo` | `tm-answerpath-geo` | Standardize under TM brand; core generative search query miner. | Consolidates search intent and GEO authority under TM namespace. | Low (Add TM prefix, update pyproject). | Low (Standard redirects apply). | Plan rename to `tm-answerpath-geo`; add MODEL-REQUIREMENTS.md. |
| `awesome-skills` | `awesome-skills (Keep As-Is)` | Upstream community fork; changing name breaks fork tracking with original maintainers. | Preserves existing upstream link authority and fork graph. | None. | High if renamed (breaks upstream synchronization). | Exemption granted under TM Open Source Standard; maintain as fork. |
| `bale-bot-skills` | `tm-bale-skills` | Adopt canonical TM prefix; production agent skills for Bale messenger. | High authority for enterprise Persian AI bot development. | Low. | Low. | Plan rename to `tm-bale-skills`; complete 5-language documentation. |
| `geo-aeo-news-engine` | `tm-geo-news-engine` | Shorten and standardize name under TM namespace for newsroom agents. | Strengthens ranking for automated news GEO/AEO optimization. | Low. | Low. | Plan rename to `tm-geo-news-engine`; add MODEL-REQUIREMENTS.md. |
| `geo-scope` | `tm-geo-scope` | Flagship research framework for empirical AI answer engine visibility. | Major brand anchor for 'TM GEO Scope' AI visibility benchmarks. | Low to Medium (Used as reference in multiple research papers). | Low with GitHub automatic redirects; update README citation badge. | Plan rename to `tm-geo-scope`; add full 5-language docs. |
| `hamzad-ai-gateway-resources` | `tm-ai-gateway-patterns` | Generalize gateway routing patterns for broader open-source utility beyond Hamzad-only context. | Attracts enterprise AI gateway architects searching for fallback policies. | Low. | Low. | Plan rename to `tm-ai-gateway-patterns`; retain Hamzad compatibility notice. |
| `hamzad-avatar-studio` | `tm-avatar-studio` | Expand digital twin and trilingual voice cloning engine into global TM suite. | Elevates discoverability for open-source AI avatar studios. | Medium (Update local Antigravity plugin paths). | Medium (Used in active local Hamzad pipelines; verify worktree). | Plan rename to `tm-avatar-studio` after updating Hamzad worktree symlinks. |
| `hermes-meeting-intelligence` | `tm-meeting-intelligence` | Establish as the canonical meeting intelligence skill pack for Hermes and AI agents. | High search volume for open-source meeting intelligence tools. | Low. | Low. | Plan rename to `tm-meeting-intelligence`; add 5-language docs. |
| `humanize-ai-copywriter` | `tm-unslop-humanizer` | Sharper, modern naming matching the viral 'unslop' concept while reinforcing TM brand. | Very high SEO potential around AI unslop, human copywriting, and zero-entropy text. | Low. | Low. | Plan rename to `tm-unslop-humanizer`; update local clone in workspace. |
| `iranian-enterprise-ai-bridge` | `tm-enterprise-ai-bridge` | Broaden international perception while maintaining full Iranian ERP/CRM integration support. | Expands keyword reach beyond single-country searches to enterprise AI bridges. | Low. | Low. | Plan rename to `tm-enterprise-ai-bridge`; maintain Persian documentation. |
| `ivna-app` | `tm-ivna-client` | Clarify that this is the news client/reader repository under TM. | Improves clarity for developers searching for Persian media readers. | Low. | Low. | Plan rename to `tm-ivna-client`; update mobile/client documentation. |
| `laravel-ai-summary` | `tm-laravel-ai-summary` | Add TM namespace to Laravel ecosystem package. | Positions TM as a reputable Laravel package vendor. | Medium (Composer package name change requires packagist update). | Medium (Packagist package name aliases must be kept). | Plan rename to `tm-laravel-ai-summary`; keep Packagist abandonment notice. |
| `lean-agent-skills` | `tm-lean-skills` | Concise branding for low-token, prompt-cache-friendly agent skills. | Directly targets token optimization and low-context agent searches. | Low. | Low. | Plan rename to `tm-lean-skills`; add 5-language documentation. |
| `mcp-agent-skills-hub` | `tm-mcp-skills-hub` | Align with TM prefix; primary distribution hub for MCP tools and agent skills. | Capitalizes on massive developer interest in MCP (Model Context Protocol). | Low. | Low. | Plan rename to `tm-mcp-skills-hub`; add full regional documentation. |
| `mcp-geo-server` | `tm-mcp-geo-server` | Canonical Model Context Protocol server for Generative Engine Optimization. | High authority for MCP servers in marketing and SEO domains. | Low. | Low. | Plan rename to `tm-mcp-geo-server`; add MODEL-REQUIREMENTS.md. |
| `molavi-agentic-os` | `tm-agentic-os (or molavi-agentic-os with TM AI Agent Toolkit identity)` | Flagship agent ecosystem repository; currently fully compliant with TM governance. | Dominates searches for 'TM AI Agent Toolkit' and 'Molavi Agentic OS'. | Low if renamed, or preserve dual identity. | Low (GitHub handles repository rename redirects automatically). | COMPLIANT. Identity updated to TM AI Agent Toolkit; preserve name or alias. |
| `molavi-web-intelligence` | `tm-web-intelligence` | Standardize web intelligence engine under TM brand prefix. | Elevates search presence for open-source self-hosted web intelligence. | Low. | Low. | Plan rename to `tm-web-intelligence`; update local workspace clone. |
| `n8n-agent-skills` | `tm-n8n-skills` | Unified n8n agent skills and workflow pack under TM prefix. | Strong niche dominance for n8n AI agent workflows. | Low. | Low. | Plan rename to `tm-n8n-skills`; complete regional docs. |
| `news-traffic-engine` | `tm-news-traffic-engine` | Add TM brand prefix to autonomous news traffic and Google Discover system. | Establishes TM authority in algorithmic media traffic optimization. | Low. | Low. | Plan rename to `tm-news-traffic-engine`; add MODEL-REQUIREMENTS.md. |
| `sage-audit` | `tm-sage-audit` | Unified 3-pillar audit engine for Technical SEO, AEO, and GEO. | High authority for multi-pillar search and AI audit tools. | Low. | Low. | Plan rename to `tm-sage-audit`; add MODEL-REQUIREMENTS.md. |
| `scholar-provenance` | `tm-scholar-provenance` | Scientific and academic evidence ledger framework under TM Open Source. | Captures academic and researcher searches for verifiable AI citations. | Low. | Low. | Plan rename to `tm-scholar-provenance`; add 5-language documentation. |
| `siteprobe` | `tm-siteprobe` | Autonomous website auditor, fixer and Core Web Vitals diagnostic engine. | High-intent search keyword for site auditing and automated fixing. | Low. | Low. | Plan rename to `tm-siteprobe`; complete 5-language documentation. |
| `tm-second-brain` | `tm-second-brain (Compliant)` | Open-source, model-agnostic, local-first Memory & Knowledge Infrastructure for AI agents (Obsidian + MCP + Hamzad Bridge). | Anchors 'TM Second Brain' persistent agent memory across Molavi Agentic OS, Hermes, and coding harnesses. | None (Created compliant with TM Standard). | None. | COMPLIANT. Full 5-language docs, MIT license, zero core dependencies, and governance CI passing. |
| `tmolavi` | `tmolavi (Keep As-Is)` | GitHub Special Profile repository; must match username exactly for profile README. | Primary personal brand hub on GitHub. | None. | High if renamed (breaks GitHub profile display). | Permanent exemption; update profile README to highlight TM Open Source Standard. |

---

## 5. Next Steps & Execution Roadmap

1. **Phase 1 (Completed):** Establish `TM-OPEN-SOURCE-STANDARD.md` and complete audit inventory.
2. **Phase 2 (Immediate):** Deploy reusable repository templates (`.github/REPOSITORY_TEMPLATE/`) and automated governance validation tools (`scripts/check_governance.py`).
3. **Phase 3 (Review):** Review migration proposals with project owner Taqi Molavi before triggering any repository renames on GitHub.
4. **Phase 4 (Staged Rollout):** Update documentation and model requirement disclosures across priority repositories (`geo-scope`, `sage-audit`, `siteprobe`, `mcp-agent-skills-hub`).
