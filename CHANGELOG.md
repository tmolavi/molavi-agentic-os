# Changelog

All notable changes to **TM Molavi Agentic OS** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.3.0] — 2026-11-14

### Added
* **4 Independent Review Personas:** Introduced dedicated review specialist agents in `agents/development/`:
  * `code-reviewer`: Principal code quality, SOLID design, readability, and cyclomatic complexity.
  * `security-auditor`: Adversarial threat auditor targeting OWASP Top 10, secret detection, and dependency audits.
  * `test-engineer`: Staff Quality & TDD engineer enforcing boundary value coverage and mock verification.
  * `web-performance-auditor`: Staff Web Performance auditor enforcing Core Web Vitals (LCP, INP, CLS) and token efficiency.
* **Independent Engineering Review Team:** Added `teams/independent-engineering-review-team.json` coordinating non-colluding reviews across all 4 personas before commit sign-off.
* **Doubt-Driven & Spec-Driven Workflows:** Added `workflows/doubt-driven-adversarial-review.json` and `workflows/spec-driven-development-flow.json`.
* **High-Rigor Engineering Skills:** Added `spec-driven-development`, `doubt-driven-development`, `constraint-driven-development`, and `anti-rationalization-rules` to `skills/development/`.
* **Automated Review & Gate Test Suite:** Added `tests/test_independent_reviews_and_gates.py` bringing total passed tests to 25.

---

## [0.2.0] — 2026-11-13

### Added
* **TM Tool & MCP Gateway:** Added `molavi_agentic_os.tools` and `molavi_agentic_os.mcp` with full Model Context Protocol stdio JSON-RPC tool discovery, input validation, and execution isolation.
* **Bumblebee MCP Security Auditor:** Inspired by Perplexity Bumblebee, added static inspection against dangerous shell commands (`rm -rf`, `sudo`, `curl | bash`) and path traversal vulnerabilities (`../../`).
* **Autoresearch Evaluation Loop:** Inspired by Andrej Karpathy's Autoresearch, implemented `molavi_agentic_os.evaluation.autoresearch` supporting `ResearchHypothesis`, `ExperimentTrial`, and automated Keep/Revert decisions.
* **TM Second Brain Memory Bridge:** Added `TMSecondBrainMemoryAdapter` for local-first Markdown/Obsidian persistent memory with immutable `.audit_log.jsonl` provenance.
* **Hermes Personal Desktop Adapter:** Added `HermesDesktopAdapter` with safe directory boundaries and personal desktop action isolation.
* **24 Standardized Skills:** Expanded curated `SKILL.md` library across 14 capability areas including Agent Engineering, Repository Analysis, Document Intelligence, AI Search Visibility, Web Intelligence, Debugging, Bumblebee MCP Security, and Autonomous Research.
* **Five-Language Documentation Suite:** Complete, comprehensive technical documentation published in English (`docs/en`), Persian (`docs/fa`), Turkish (`docs/tr`), Azerbaijani (`docs/az`), and Arabic (`docs/ar`).
* **License & Upstream Provenance:** Published `LICENSE_COMPATIBILITY.md` and updated `SOURCES.md` and `THIRD_PARTY_NOTICES.md` detailing the 6 reference upstream repositories.
* **PyPI Distribution & Trusted Publishing:** Configured `.github/workflows/publish-pypi.yml` and built release packages for `molavi-agentic-os` v0.2.0.

### Changed
* Upgraded `ForemanVerificationGate` with `VerificationArtifact` schema and multi-artifact physical verification.
* Upgraded root `README.md` with high-conversion hero section, PyPI badges, comparison matrix vs CrewAI/LangGraph/AutoGPT, GEO/AEO search snippets, and star CTA.
* Bumped version to `0.2.0` across `pyproject.toml` and `setup.py`.

---

## [0.1.0] — 2026-11-06

### Added
* Initial release of Molavi Agentic OS.
* Core agent, skill, and team definitions.
* Zero-dependency thread-safe `TaskQueue` and DAG orchestration engine.
* Permission-Slip HMAC cryptographic approval tickets (`L2_HUMAN_APPROVAL`).
* Foreman Anti-Hallucination verification gate ("No Guessing").
* Local SQLite memory store and working memory buffer.
* Free-First Model Router with local Ollama and zero-cost cloud tiers.
* Cross-platform adapters for Hermes Agent, Antigravity, Claude Code, and Codex.
* Automated Bot-Ready 100-point validation suite.
