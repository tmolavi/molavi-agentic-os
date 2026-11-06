# TM Open Source Standard

> **Document Type:** Canonical Repository Governance & Engineering Policy  
> **Brand Authority:** TM / Molavi Open Source Ecosystem  
> **Maintainer & Brand Owner:** Taqi Molavi (`tmolavi`)  
> **Applicability:** Mandatory for all existing, current, and future open-source repositories under `tmolavi`  
> **Effective Date:** November 2026 (Permanent Governance Policy)  

---

## 1. Prime Directive & Purpose

The **TM Open Source Standard** defines the mandatory governance, branding, technical, documentation, and security standards for all open-source projects published under the **TM (Taqi Molavi) ecosystem**.

The objective of this standard is to guarantee that every repository published under `tmolavi`:
1. Is **immediately recognizable**, trustworthy, and professionally maintained.
2. Is **search-optimized (SEO/AEO/GEO)** and easily discoverable across GitHub, Google, and AI answer engines.
3. Provides **five-language documentation** (English, Persian, Turkish, Azerbaijani, and Arabic) to support international and regional developers.
4. Discloses **model requirements, token consumption, and API costs** transparently, prioritizing free and open-source models (Ollama, Groq, Gemini Free Tier).
5. Enforces **strict license compliance, zero-secret exposure, and clean provenance**.
6. Maintains **direct interoperability** with AI coding environments (Codex, Claude Code, Antigravity, Hermes) and the Hamzad ecosystem.

---

## 2. Repository Naming & Identity Convention

### 2.1 The `tm-*` Canonical Prefix
All new repositories must use the standardized `tm-` prefix to establish brand coherence, unless granted a documented policy exemption:
* **Format:** `tm-<domain>-<capability>`
* **Examples:**
  * `tm-agentic-os` (Core agent framework)
  * `tm-geo-scope` (Generative Engine Optimization benchmark suite)
  * `tm-news-engine` (Autonomous newsroom and syndication engine)
  * `tm-sage-audit` (Unified 3-pillar SEO/AEO/GEO audit CLI)
  * `tm-bale-skills` (Agent skills for Bale messenger)

### 2.2 Recognized Exemptions
1. **GitHub Profile Repository:** `tmolavi` (Reserved special repository for user profile overview).
2. **Upstream Direct Forks:** Where preserving the exact upstream repository name is legally or technically required for pull requests (e.g., `awesome-skills`).
3. **Established Core Systems during Planned Migration:** Repositories undergoing staged migration windows must define redirect aliases and deprecation notices before renaming.

---

## 3. Mandatory Five-Language Documentation Standard

Every TM repository must provide comprehensive documentation across five languages:

```text
docs/
├── fa/README.md    # فارسی (Persian)
├── tr/README.md    # Türkçe (Turkish)
├── az/README.md    # Azərbaycan dili (Azerbaijani)
├── ar/README.md    # العربية (Arabic)
└── en/README.md    # English (Optional mirror; root README.md serves as primary English)
```

### Language Coverage Rules:
1. **Root `README.md`:** Written in idiomatic, professional English with international open-source styling, architecture diagrams, quickstart guides, badges, and language switcher links.
2. **Localized `README.md` files:**
   - Must contain a complete project overview, key value propositions, local installation steps, CLI examples, and brand philosophy.
   - Identifiers, code snippets, and CLI commands must remain in English; explanations and narrative descriptions must be fully localized.
   - Machine translation must be reviewed for technical accuracy and natural phrasing.

---

## 4. Model, API & Cost Transparency Standard

Every repository utilizing Artificial Intelligence or Large Language Models must include a **`MODEL-REQUIREMENTS.md`** file disclosing:
1. **Supported Model Classes:**
   - Free/Local Open-Weight Models (e.g., Ollama Llama 3, Mistral, Qwen).
   - Zero-Cost Cloud Tiers (e.g., Groq Free Tier, Google Gemini 1.5/2.0 Flash Free Tier).
   - Paid Cloud APIs (e.g., Anthropic Claude 3.5 Sonnet, OpenAI GPT-4o).
2. **Token Consumption & Rate Limits:**
   - Estimated input/output tokens per standard run.
   - Recommended context-window size.
   - Handling of rate limits and backoff policies.
3. **Cost Profile:**
   - Default execution cost must be **$0.00** using local or free-tier providers.
   - Paid models must require explicit configuration and consent; silent switching to paid APIs is strictly prohibited.

---

## 5. Security & Human-in-the-Loop Governance

### 5.1 Permission Hierarchy (L0 to L3)
Every tool, skill, and agent must adhere to the four-tier permission model:
* **L0 (Read-Only):** Data extraction, log inspection, read-only analysis.
* **L1 (Draft & Recommend):** Local draft creation, code diff proposals, content drafting without external side effects.
* **L2 (Human Approval Required):** **Default for all sensitive actions.** Sending emails, publishing live articles, executing financial transactions, mutating server configurations, and executing destructive shell commands require a cryptographically signed `ApprovalTicket`.
* **L3 (Pre-Authorized Automation):** Sandboxed, pre-authorized executions with verified audit logs.

### 5.2 Foreman Verification Rule
* *"It is not allowed to guess."* Agents must not declare tasks completed without verifiable evidence artifacts (test outputs, diffs, URLs, citation hashes).

### 5.3 Secret Redaction & Supply Chain
* No credentials, private tokens (`ghp_*`, `sk-*`), or personal passwords may ever be committed to Git history.
* Every repository must configure automated secret scanning and pass `check_governance.py`.

---

## 6. Open-Source Provenance & Licensing

1. **Default License:** **MIT License** for all original software authored under TM Open Source.
2. **Third-Party Attribution:**
   - Repositories adapting or referencing external work must maintain a `THIRD_PARTY_NOTICES.md` preserving original copyrights and licenses.
   - Repositories studying or synthesizing concepts must maintain a `SOURCES.md`.
3. **No License Incompatibility:** GPL-incompatible code must never be mixed into permissive MIT modules without strict architectural separation.

---

## 7. Mandatory Repository Layout Checklist

Every standard TM repository must feature the following structure:

```text
├── README.md                  # Comprehensive English documentation with language switcher
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contribution guidelines & Bot-Ready standards
├── SECURITY.md                # Security policy & L0-L3 permission matrix
├── MODEL-REQUIREMENTS.md      # Model transparency, token estimates & free alternatives
├── THIRD_PARTY_NOTICES.md     # Third-party notices and licenses
├── CHANGELOG.md               # Semantic version changelog
├── ROADMAP.md                 # Development roadmap
├── docs/                      # Multi-language documentation
│   ├── fa/README.md
│   ├── tr/README.md
│   ├── az/README.md
│   └── ar/README.md
├── tests/                     # Deterministic, reproducible unit & integration tests
├── .github/
│   └── workflows/ci.yml       # Automated CI with lint, test & governance checks
```

---

## 8. Pre-Publication Gate

Before any repository is made public under `tmolavi`, it must pass the **TM Pre-Publication Checklist**:
- [ ] Name conforms to `tm-*` convention (or has documented exemption).
- [ ] Description is clear, concise, and SEO-optimized.
- [ ] Root `README.md` and all 4 regional languages (`fa`, `tr`, `az`, `ar`) exist.
- [ ] `MODEL-REQUIREMENTS.md` is present and details free-first alternatives.
- [ ] `LICENSE` is valid MIT.
- [ ] Zero secrets or API keys are present in Git history.
- [ ] Automated tests pass with 100% success rate.
- [ ] Relevance to the TM ecosystem and Hamzad is documented.

*If any item is missing, the repository status must be marked `EXPERIMENTAL` or `NEEDS_DOCUMENTATION` and must not be promoted as production-ready.*

---

## 9. Single Source of Truth Instruction

All AI coding assistants (including **Google Antigravity**, **OpenAI Codex**, **Claude Code**, **Hermes Agent**, and **Hamzad AI**) must consult this document (`TM-OPEN-SOURCE-STANDARD.md`) before creating, refactoring, or publishing any repository under `tmolavi`.
