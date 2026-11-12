# Sources, Technical Standards & Upstream Provenance

This document catalogs the open specifications, architectural standards, upstream reference repositories, and technical protocols upon which **TM Molavi Agentic OS** is built.

---

## 1. Upstream Reference Repositories

| Repository | Author / Organization | URL | License | Key Concept Extracted & Adapted | TM Implementation Module |
|---|---|---|---|---|---|
| **Autoresearch** | Andrej Karpathy | [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch) | MIT | Autonomous experiment loops, hypothesis evaluation, keep/revert decisions, reproducibility ledgers. | `molavi_agentic_os.evaluation.autoresearch` |
| **Nanochat** | Andrej Karpathy | [github.com/karpathy/nanochat](https://github.com/karpathy/nanochat) | MIT | Minimal, zero-dependency, modular, reproducible systems architecture. | `molavi_agentic_os.core` & providers |
| **LLMs from Scratch** | Sebastian Raschka | [github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Apache-2.0 | Transparent model fundamentals, tokenization, context bounds, educational documentation. | `MODEL-REQUIREMENTS.md` |
| **Andrej Karpathy Skills** | Forrest Chang | [github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | MIT | "Think before coding", surgical diffs, agent behavioral boundaries, goal-driven execution. | `skills/development/code-review-standards` |
| **Awesome Claude Skills** | ComposioHQ | [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Apache-2.0 | Standardized `SKILL.md` format, capability discovery, structured tool contracts. | `molavi_agentic_os.core.skill` & registry |
| **Bumblebee** | Perplexity AI | [github.com/perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | Apache-2.0 | MCP server security checks, supply-chain auditing, path jail boundaries, injection defenses. | `molavi_agentic_os.mcp.security_auditor` |

---

## 2. Open Technical Specifications & Standards

| Standard / Protocol | Governing Body | Applied Concept in TM Agentic OS |
|---|---|---|
| **Agent Skills Standard** | Open Agent Community | Standardized `SKILL.md` metadata, trigger conditions, and schemas |
| **Model Context Protocol (MCP)** | Anthropic & Open Source Community | Standardized tool execution, JSON-RPC stdio protocol, schema validation |
| **RFC 2104 (HMAC Authentication)** | IETF | Cryptographically signed `ApprovalTicket` system for human verification |
| **JSON-LD & Schema.org** | W3C Semantic Web | Knowledge graph entity resolution for SEO & GEO auditors |
| **Core Web Vitals Metric Suite** | Chromium / Google | LCP, INP, and CLS diagnostic thresholds in SEO auditing skills |
| **PEP 557 & PEP 621** | Python Software Foundation | Strict typed schema validation for canonical agents and workflows |
| **Clean Architecture & SOLID** | Robert C. Martin | Minimal diffs, decoupled engine abstractions, and zero external runtime dependencies |

---

## 3. Licensing Statement

All source code, agent schemas, skill implementations, and team topologies in TM Molavi Agentic OS are original works authored by **Taghi Molavi**, licensed under the **MIT License**. For complete cross-project licensing details, see [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md).
