# License Compatibility & Upstream Provenance Matrix

This document provides a comprehensive intellectual property, licensing, and architectural compatibility analysis for **TM Molavi Agentic OS** (`molavi-agentic-os`).

All core engines, agent contracts, skill architectures, team topologies, and adapters in TM Molavi Agentic OS are original implementations authored by **Taghi Molavi**, distributed under the permissive **MIT License**.

---

## 1. Upstream Reference Repositories & Compatibility Matrix

TM Molavi Agentic OS draws inspiration from six foundational open-source engineering paradigms. Rather than copying proprietary source files or unverified packages, TM Molavi Agentic OS adopts clean-room architectural adaptations conforming to permissive open-source license standards.

| Reference Repository | Upstream Author / Org | Upstream License | Incorporated Concepts | TM Clean-Room Implementation | Compatibility Verdict |
|---|---|---|---|---|---|
| [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) | Andrej Karpathy | MIT License | • Metric-driven autonomous research loops<br>• Hypothesis evaluation<br>• Keep / Revert rollback decisions<br>• Experiment tracking ledgers | `molavi_agentic_os.evaluation.autoresearch`<br>`skills/evaluation/autonomous-experiment-eval`<br>`skills/research/autonomous-research-loop` | **100% Compatible (MIT to MIT)**<br>Zero GPU training code imported; pure agent evaluation logic. |
| [`karpathy/nanochat`](https://github.com/karpathy/nanochat) | Andrej Karpathy | MIT License | • Minimal, understandable modular design<br>• Zero unnecessary dependencies<br>• Reproducible execution primitives | `molavi_agentic_os.core`<br>`molavi_agentic_os.providers.router` | **100% Compatible (MIT to MIT)**<br>Architectural simplicity principles applied to zero-dependency agent OS. |
| [`rasbt/LLMs-from-scratch`](https://github.com/rasbt/LLMs-from-scratch) | Sebastian Raschka | Apache 2.0 | • Transparent model fundamentals<br>• Tokenization and context management<br>• Educational & verifiable documentation | `MODEL-REQUIREMENTS.md`<br>`molavi_agentic_os.providers.base`<br>Multilingual technical architecture docs | **100% Compatible (Apache 2.0 to MIT)**<br>No direct code copied; architectural pedagogy and context boundaries adapted. |
| [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) | Forrest Chang | MIT License | • "Think before coding" discipline<br>• Surgical atomic diffs<br>• Goal-oriented execution<br>• Coding agent behavioral standards | `skills/development/code-review-standards`<br>`skills/orchestration/agent-engineering`<br>`AGENTS.md` & contributor rules | **100% Compatible (MIT to MIT)**<br>Original behavioral directives codified into machine-enforceable Bot-Ready schemas. |
| [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) | ComposioHQ | Apache 2.0 | • Standardized `SKILL.md` structure<br>• Capability discovery metadata<br>• Reusable tool integration patterns | `molavi_agentic_os.core.skill`<br>`molavi_agentic_os.tools.registry`<br>Curated 24-skill ecosystem | **100% Compatible (Apache 2.0 to MIT)**<br>Clean-room specification using standard YAML frontmatter and JSON Schemas. |
| [`perplexityai/bumblebee`](https://github.com/perplexityai/bumblebee) | Perplexity AI | Apache 2.0 | • MCP server security auditing<br>• Supply-chain risk detection<br>• Injection prevention & path jail enforcement<br>• Least-privilege tool allowlists | `molavi_agentic_os.mcp.security_auditor`<br>`skills/security/bumblebee-mcp-audit`<br>`molavi_agentic_os.security.guardrails` | **100% Compatible (Apache 2.0 to MIT)**<br>Independent Python static analysis engine protecting tool boundaries. |

---

## 2. Redistribution & Copyright Notice

1. **Original TM Components:** Copyright (c) 2026 Taghi Molavi. Licensed under the MIT License.
2. **Third-Party Patents & Trademarks:** All trademarks, logos, and brand names mentioned (OpenAI, Claude, Perplexity, Gemini, Ollama, GitHub, Obsidian) are the property of their respective owners. Their mention in this repository denotes interoperability and compatibility analysis only.
3. **Redistribution Rights:** Because all upstream reference works are licensed under either the **MIT License** or **Apache License 2.0**, their architectural patterns and interfaces are fully compatible with TM Molavi Agentic OS's MIT distribution.
