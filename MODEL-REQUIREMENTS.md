# Model Requirements & Cost Transparency

> **Repository:** TM AI Agent Toolkit (`molavi-agentic-os`)  
> **Brand:** TM Open Source / Molavi Brand  
> **Strategy:** Free-First, Provider-Agnostic, Zero Hidden Costs  

---

## 1. Free-First Strategy Overview

TM AI Agent Toolkit is engineered to run out-of-the-box with **zero software or API costs**.

All agents, workflows, and skills are decoupled from proprietary infrastructure. You are never forced to pay for an API subscription to run, evaluate, or deploy these agents.

```
Execution Priority Tier:
┌────────────────────────────────────────────────────────┐
│  Tier 1: FREE LOCAL (Ollama: Llama 3.2, Mistral, Qwen)  │  --> $0.00 / run
├────────────────────────────────────────────────────────┤
│  Tier 2: FREE CLOUD (Groq Free, Gemini 2.0 Flash Free)  │  --> $0.00 / run
├────────────────────────────────────────────────────────┤
│  Tier 3: LOW-COST CLOUD (Claude 3.5 Haiku, GPT-4o-mini) │  --> Minimal cost
├────────────────────────────────────────────────────────┤
│  Tier 4: HIGH-CAPABILITY (Claude 3.5 Sonnet, GPT-4o)   │  --> Explicit user consent only
└────────────────────────────────────────────────────────┘
```

---

## 2. Supported Providers & Model Compatibility

| Provider | Supported Models | Recommended Tier | Free Tier Available? | Offline Capable? |
|---|---|---|:---:|:---:|
| **Ollama (Local)** | `llama3.2`, `mistral`, `qwen2.5`, `phi-3` | `FREE_LOCAL` | **Yes (100% Free)** | **Yes** |
| **Google Gemini** | `gemini-2.0-flash`, `gemini-1.5-flash` | `FREE_CLOUD` | **Yes (15 RPM free)** | No |
| **Groq** | `llama-3.3-70b-versatile`, `mixtral-8x7b-32768` | `FREE_CLOUD` | **Yes (Generous free tier)** | No |
| **OpenRouter** | Free endpoints (`:free` tags) | `FREE_CLOUD` | **Yes** | No |
| **Anthropic** | `claude-3-5-haiku-latest`, `claude-3-5-sonnet` | `CHEAP_CLOUD` / `PREMIUM` | Paid API | No |
| **OpenAI** | `gpt-4o-mini`, `gpt-4o` | `CHEAP_CLOUD` / `PREMIUM` | Paid API | No |

---

## 3. Token Consumption & Cost Profiles

Estimated resource consumption across standard tasks:

| Workflow / Task | Avg. Prompt Tokens | Avg. Completion Tokens | Total Tokens | Estimated Cost (Local / Free Tier) | Estimated Cost (Commercial API) |
|---|:---:|:---:|:---:|:---:|:---:|
| **SEO Technical Audit** | 1,200 | 800 | 2,000 | **$0.00** | < $0.005 |
| **GEO Visibility Benchmark** | 1,800 | 1,200 | 3,000 | **$0.00** | < $0.008 |
| **Unslop Content Humanization**| 2,000 | 1,500 | 3,500 | **$0.00** | < $0.009 |
| **Lead Qualification & Drafter**| 1,500 | 600 | 2,100 | **$0.00** | < $0.006 |
| **Code Review & Clean Code** | 3,000 | 1,800 | 4,800 | **$0.00** | < $0.012 |

---

## 4. Minimum Hardware Requirements for Local Inference

To run Tier 1 (`FREE_LOCAL`) completely offline without external cloud requests:
* **Minimum CPU:** 4-core modern x86_64 or Apple Silicon (M1/M2/M3/M4) / ARM64.
* **Minimum RAM:** 8 GB RAM (for running 3B quantized parameter models like `llama3.2:3b`).
* **Recommended RAM:** 16 GB+ RAM (for running 7B-8B parameter models like `llama3.1:8b` or `qwen2.5:7b`).
* **Optional GPU:** NVIDIA RTX 3060+ (6GB+ VRAM) or Apple Silicon Unified Memory for sub-second response times.

---

## 5. Cost Protection & Rate Limiting Guarantees

1. **No Silent Upgrades:** The `ModelRouter` will never automatically escalate to a paid model tier unless explicitly requested via configuration flags (`allow_paid_fallback=True`).
2. **Quota Tracking:** Built-in token counters monitor cumulative session consumption.
3. **Graceful Degradation:** If cloud free tiers hit rate limits (e.g., HTTP 429), the router automatically backs off exponentially and falls back to local Ollama inference.
