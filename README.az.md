<div align="center">

# TM Molavi Agentic OS

### Avtonom Süni İntellekt Agentləri, Bacarıqlar, Çoxagentli Komandalar, İş Axınları və Yerli Yaddaş üçün Açıq Mənbəli Əməliyyat Ekosistemi

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![Bot-Ready Score](https://img.shields.io/badge/Bot--Ready-100%2F100-purple?style=for-the-badge)](https://github.com/tmolavi/molavi-agentic-os)
[![Marginal Cost](https://img.shields.io/badge/Cost-%240.00%20(Free--First)-brightgreen?style=for-the-badge)](MODEL-REQUIREMENTS.md)

**Memar və Tərtibatçı: [Tağı Mövləvi (Taghi Molavi)](https://molavi.pro)** · *Süni İntellekt Sistemləri Memarı və Generativ Axtarış Görünürlüyü (GEO) Tədqiqatçısı*  
*یاد بگیر، یاد بده و اثری ماندگار خلق کن — Öyrən. Paylaş. Qalıcı təsir yarat.*

```bash
pip install molavi-agentic-os
```

[English](README.md) · [فارسی (Persian)](README.fa.md) · [Türkçe (Turkish)](README.tr.md) · [Azərbaycan dili](README.az.md) · [العربية (Arabic)](README.ar.md)

<br/>

> ⭐ **Əgər bu layihə sizi ağır server infrastrukturlarından və yalançı agent hesabatlarından xilas etdisə, zəhmət olmasa GitHub-da depoya bir ulduz (Star) verərək açıq mənbəli ekosistemi dəstəkləyin!**

</div>

---

## ⚡ İstehsalat Mühitində Agent Sistemlərinin Əsas Problemləri

Mövcud süni intellekt agent kitabxanaları real istehsalat mühitində 3 kritik problemlə üzləşir:

1. **Həddindən Artıq İnfrastruktur Asılılığı (Infrastructure Sprawl):** Sadə 3 mərhələli agent axını üçün belə arxa fonda Redis, Celery, Docker və bahalı kommersiya API modelləri tələb edilir.
2. **Uydurma "Tamamlandı" İllüziyası (Hallucinated Done States):** Agentlər fiziki olaraq heç bir test icra etmədən və real çıxış istehsal etmədən tapşırıqları "bitmiş" kimi təqdim edirlər.
3. **Təhlükəsizlik Sərhədlərinin Olmaması:** Təhlükəli terminal əmrləri (`rm -rf`, nəzarətsiz şell skriptləri) kriptoqrafik insan təsdiqi və MCP təhlükəsizlik auditi olmadan işə salınır.

**TM Molavi Agentic OS** təmiz Python standart kitabxanası ilə bu problemləri aradan qaldırır: Redis və ya Celery tələb etmir, yerli açıq çəkili modelləri (Ollama: Llama 3.2, Mistral) və pulsuz bulud laylarını (Groq, Gemini Free Tier) önə çəkərək **0.00$** marjinal xərclə işləyir, Foreman doğrulama qapısı ("ehtimal etmək qadağandır") ilə maddi artefakt sübutu tələb edir və həssas əməliyyatları HMAC imzalı icazə biletləri ilə insan təsdiqinə bağlayır.

---

## 📊 Müqayisə Cədvəli: Niyə Mühəndislər Molavi Agentic OS Seçir?

| Göstərici / Memarlıq | TM Molavi Agentic OS | CrewAI | LangGraph | AutoGPT |
|---|---|---|---|---|
| **İcra Asılılıqları** | **Sıfır (Yalnız Python Standart Kitabxanası)** | Ağır (Pydantic, Chroma və s.) | Ağır (LangChain ekosistemi) | Ağır (Docker, Redis və s.) |
| **Model Xərc Strategiyası** | **Əvvəlcə Pulsuz (0.00$ Ollama/Groq/Gemini)** | Ödənişli bulud API-ləri | Ödənişli bulud API-ləri | Standart OpenAI |
| **Foreman Doğrulama Qapısı** | **Dəqiq Maddi Artefakt Yoxlaması ("No-Guessing")** | Agentin öz bəyanı | Əllə istifadəçi yoxlaması | Nəzarətsiz |
| **İnsan Təsdiqi Sistemi** | **HMAC İmzalı `ApprovalTicket` (L0-L3)** | Sadə callback | Interrupt modeli | Terminal təsdiqi |
| **Alət Protokolu** | **Yerli MCP Şlüzü + Bumblebee Təhlükəsizliyi** | Xüsusi örtüklər | LangChain Tools | Fərdi plaqinlər |
| **Yaddaş Memarlığı** | **SQLite + `tm-second-brain` (Markdown/Obsidian)** | Vektor bazası məcburi | Checkpointer State | Vektor yaddaşı |
| **Platforma Adapterləri** | **Hermes Main, Hermes Desktop, Antigravity, Codex** | Xüsusi CLI | LangGraph Cloud | Yalnız veb interfeysi |
| **Avtonom Optimizasiya** | **Karpathy Autoresearch Keep/Revert Dövrəsi** | Yoxdur | Ödənişli LangSmith | Yoxdur |

---

## 🏛️ Sistem Memarlığı

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  Platforma və İcra Zamanı Adapterləri:                                 │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  Çoxagentli Komandalar və İstehsalat İş Axınları:                      │
│  • SEO və GEO Tədqiqat Komandası   • Avtonom Tədqiqat Dövrəsi          │
│  • Süni İntellekt Görünürlük Qrupu • Rəsmi Çoxagentli Təhvil Xətti     │
│  • Təmiz Məzmun İstehsal Komandası • Xəta İdarəetməsi və Geri Çəkilmə  │
│  • B2B Müştəri Axtarış Komandası   • Sistematik Sazlama və Yamaq       │
├────────────────────────────────────────────────────────────────────────┤
│  12 Mütəxəssis Agent (100/100 Bot-Ready Xalı):                         │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  24 Standart Agent Bacarığı (SKILL.md) və Alət Kataloqu:               │
│  • Agent Mühəndisliyi və Müqavilələr • Bumblebee MCP Təhlükəsizlik Yoxlaması │
│  • Dərin Depo Təhlili                • Kəmiyyət Autoresearch Metrikləri│
│  • Sənəd Zəkası və Sxem Çıxarışı     • Sıfır Token Xərcli Şəbəkə İntellekti │
│  • GEO və Süni İntellekt Görünürlüyü • İkinci Beyin Obsidian Yaddaşı   │
├────────────────────────────────────────────────────────────────────────┤
│  Əsas İdarəetmə və Təhlükəsizlik Alt Sistemləri:                       │
│  • HMAC İmzalı İnsan Təsdiq Nəzarətçisi (L2_HUMAN_APPROVAL)            │
│  • Foreman 'Ehtimal Qadağandır' Artefakt Doğrulama Qapısı              │
│  • Sıfır Asılılıqlı Thread-Safe TaskQueue və DAG İcraçısı              │
│  • Pulsuz Model Yönləndiricisi (Ollama Llama-3.2, Groq, Gemini)        │
│  • Dəyişiklik Tarixçəsini Saxlayan Markdown İkinci Beyin Yaddaşı       │
│  • Təlimat İnseksiyasını Əngəlləyən Standart MCP Şlüzü                 │
│  • Karpathy-dən İlham Alan Keep/Revert Qərarlı Tədqiqat Dəftəri        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 60 Saniyədə Başlanğıc

### 1. PyPI vasitəsilə quraşdırma
```bash
pip install molavi-agentic-os
```

Və ya inkişaf üçün mənbə kodunu klonlayın:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### 2. Bot-Ready Doğrulaması (100/100 Xal)
```bash
molavi-agentic-os validate
```
Çıxış:
```text
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] fact-checker (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### 3. Ucdan-Uca İş Axınını İcra Edin
```bash
python examples/end_to_end_agent_workflow.py
```

---

## 💡 İcraolunan Kod Nümunələri

### 1. Sıfır Xərcli Yerli və Bulud Model Yönləndirilməsi (0.00$)
```python
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider

router = ModelRouter()
local_model = MockProvider(fixed_response="Sistem memarlığı tamamilə oflayn doğrulandı.")
router.register_provider("ollama-llama-3.2", local_model, ModelTier.FREE_LOCAL)

response = router.route_and_generate(
    prompt="Təhlükəsizlik memarlığını və agent sərhədlərini yoxla",
    preferred_tier=ModelTier.FREE_LOCAL
)
print(f"İstifadə edilən Model: {response.model_name} | Xərc: ${response.estimated_cost_usd:.2f}")
```

### 2. Foreman Doğrulama Qapısı ("Ehtimal etmək qadağandır")
```python
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

agent_output = {
    "status": "completed",
    "target_url": "https://molavi.pro/research",
    "evidence": ["HTTP 200 OK", "Başlıqlar uğurla çıxarıldı"]
}

artifacts = [
    VerificationArtifact("url_crawled", "string", agent_output["target_url"]),
    VerificationArtifact("evidence_ledger", "list", agent_output["evidence"])
]

result = ForemanVerificationGate.verify(agent_output, artifacts)
if result.is_verified:
    print(f"✅ Foreman Təsdiqi Verildi: {result.verified_artifacts}")
else:
    print(f"❌ İmtina Edildi: {result.failure_reason}")
```

### 3. HMAC İmzalı İnsan Təsdiq Sistemi
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key-min-32-chars")
ticket = mgr.create_ticket(
    action="deploy_production_code",
    reason="Əməliyyat sistemi v0.2.0 rəsmi buraxılışı",
    target="prod-cluster-01",
    impact="İstehsalat klasterində canlı kod yenilənməsi",
    risk="HIGH"
)
print(f"Bilet ID: {ticket.ticket_id} | İnsan Təsdiqi Tələb Olunurmu: {ticket.requires_human_approval}")
```

---

## 🌐 Platforma İxrac Adapterləri

```bash
# Hermes Main üçün ixrac et
molavi-agentic-os install --platform hermes --agent research-agent

# Hermes Desktop üçün ixrac et
molavi-agentic-os install --platform hermes-desktop --agent developer-agent

# Antigravity IDE üçün ixrac et
molavi-agentic-os install --platform antigravity --agent content-writer

# OpenAI Codex və Cursor üçün ixrac et
molavi-agentic-os install --platform codex --agent seo-auditor

# Claude Code (CLAUDE.md) üçün ixrac et
molavi-agentic-os install --platform claude-code --agent project-manager
```

---

## 🔗 Ekosistem və Əlaqəli GitHub Depoları

| Depo | Sahə | TM Agentic OS ilə Əlaqəsi |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | Agentlər üçün Yerli Markdown və Obsidian Yaddaş İnfrastrukturu | Seanslararası davamlı yaddaş və audit jurnalı layı. |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | Süni İntellekt Cavab Sistemlərində Görünürlük Çərçivəsi | `geo-auditor` üçün real istinad məlumatlarını təmin edir. |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | 3 Sütunlu Texniki SEO, AEO və Sxem Auditi Mühərriki | `seo-auditor` daxilinə texniki audit rutinlərini ötürür. |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | Avtonom Veb Sayt Təmiri və Diaqnostikası | Diaqnostika hesabatlarına əsasən avtomatik təmir edir. |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | Sıfır Token Xərcli Deterministik Şəbəkə Təhlili | Agentlərin internetdən məlumat toplaması üçün pulsuz baza. |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | Sıfır Entropiyalı İnsani Mətn Yazarlığı Mühərriki | `unslop-humanizer` və məzmun yazarının əsas mühərriki. |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | GEO və Süni İntellekt Görünürlüyü üçün FastMCP Serveri | Agentlər üçün standart MCP alət nöqtələri təqdim edir. |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | Xəbər Otağı Yayımı və Google News Trafik Mühərriki | Media avtomatlaşdırılması üçün məzmun qrupuna qoşulur. |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | Elmi Sübut Dəftərləri və Doğrulanabilən Məqalələr | `fact-checker` üçün doğrulanabilən istinad sxemləri verir. |
| [`tmolavi`](https://github.com/tmolavi/tmolavi) | Tağı Mövləvi Rəsmi GitHub Profil Deposu | Bütün ekosistem memarlığının mərkəzi təqdimat bazası. |

---

## 🛡️ Açıq Mənbə Referans Layihələri və Lisenziya Uyğunluğu

1. **Andrej Karpathy — [Autoresearch](https://github.com/karpathy/autoresearch)** (MIT)
2. **Andrej Karpathy — [Nanochat](https://github.com/karpathy/nanochat)** (MIT)
3. **Sebastian Raschka — [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** (Apache 2.0)
4. **Forrest Chang — [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** (MIT)
5. **ComposioHQ — [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** (Apache 2.0)
6. **Perplexity AI — [Bumblebee](https://github.com/perplexityai/bumblebee)** (Apache 2.0)

Geniş hüquqi analiz üçün [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md) və [`SOURCES.md`](SOURCES.md) fayllarını oxuya bilərsiniz.

---

## ❓ Tez-tez Verilən Suallar (FAQ / AEO)

<details>
<summary><strong>Sual: TM Molavi Agentic OS işlətmək üçün Docker və ya Redis vacibdirmi?</strong></summary>

**Xeyr.** Sistem yalnız standart Python kitabxanaları ilə (Thread-Safe TaskQueue və DAG həll edicisi) yazılmışdır. Noutbukunuzda heç bir xarici xidmət qurmadan çoxagentli komandaları işə sala bilərsiniz.
</details>

<details>
<summary><strong>Sual: Əvvəlcə Pulsuz Model strategiyası necə işləyir?</strong></summary>

Yönləndirici ilkin olaraq yerli Ollama modellərini və ya pulsuz yüksəksürətli bulud sistemlərini (Groq və Google Gemini Free Tier) seçir. Ödənişli modellər yalnız birbaşa insan təsdiqi verildikdə aktivləşir.
</details>

---

## 📈 Ulduz Tarixçəsi (Star History)

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

**⭐ Bu layihəni bəyəndinizsə, GitHub-da depoya bir ulduz verərək ekosistemi böyüdə bilərsiniz!**

</div>

---

## 📜 Lisenziya və İdarəetmə

**MIT Lisenziyası** altında təqdim olunur. Müəllif hüququ (c) 2026 **Tağı Mövləvi**.  
[`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md) standartlarına 100% cavab verir.
