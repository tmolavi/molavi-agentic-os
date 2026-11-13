<div align="center" dir="rtl">

# سیستم عامل ایجنت‌های هوش مصنوعی مولوی (TM Molavi Agentic OS)

### اکوسیستم متن‌باز، تولیدمحور و مستقل از مدل برای ایجنت‌های خودمختار، مهارت‌ها، تیم‌های چند ایجنتی، حافظه محلی و اجرای چند پلتفرمی

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![Bot-Ready Score](https://img.shields.io/badge/Bot--Ready-100%2F100-purple?style=for-the-badge)](https://github.com/tmolavi/molavi-agentic-os)
[![Marginal Cost](https://img.shields.io/badge/Cost-%240.00%20(Free--First)-brightgreen?style=for-the-badge)](MODEL-REQUIREMENTS.md)

**معماری و توسعه توسط [تقی مولوی (Taghi Molavi)](https://molavi.pro)** · *معمار سیستم‌های هوش مصنوعی و پژوهشگر دیده‌پذیری مدل‌های مولد*  
*یاد بگیر، یاد بده و اثری ماندگار خلق کن — Learn. Share. Create a lasting impact.*

```bash
pip install molavi-agentic-os
```

<div dir="ltr">

[English](README.md) · [فارسی (Persian)](README.fa.md) · [Türkçe (Turkish)](README.tr.md) · [Azərbaycan dili](README.az.md) · [العربية (Arabic)](README.ar.md)

</div>

<br/>

> ⭐ **اگر این پروژه شما را از دیمون‌های سنگین سرور و توهم ایجنت‌ها نجات داد، لطفاً با دادن یک ستاره (Star) به مخزن در گیت‌هاب از توسعه این اکوسیستم متن‌باز حمایت کنید!**

</div>

---

<div dir="rtl">

## ⚡ معضل فریم‌ورک‌های فعلی ایجنت‌ها در محیط‌های واقعی

اکثر فریم‌ورک‌های مرسوم هوش مصنوعی هنگام ورود به محیط عملیاتی و پروداکشن با ۳ چالش مهلک مواجه می‌شوند:

۱. **انباشت زیرساخت و وابستگی اجباری (Infrastructure Sprawl):** برای یک پایپ‌لاین ۳ مرحله‌ای ساده، شما را وادار به راه‌اندازی دیمون‌های Redis، Celery، داکر و پایگاه‌های برداری سنگین می‌کنند و گلوگاه هزینه‌های هنگفت کلیدهای API تجاری را به سیستم تحمیل می‌نمایند.
۲. **وضعیت‌های اتمام ساختگی و توهم ایجنت (Hallucinated Done States):** ایجنت‌ها بدون اینکه تست فیزیکی اجرا کرده باشند یا خروجی واقعی تولید کنند، خود را «پایان‌یافته» گزارش می‌کنند.
۳. **نبود مرزبندی امنیتی در اجرای ابزارها:** اجرای دستورات خطرناک ترمینال بدون تایید انسانی کریپتوگرافیک و بدون بازرسی امنیتی ابزارهای MCP.

**TM Molavi Agentic OS** یک سیستم‌عامل مستقل، ماژولار و فاقد وابستگی خارجی است؛ بدون نیاز به ردیس یا سلری، با اولویت مدل‌های رایگان محلی و تپ‌های ابری رایگان، با گیت راستی‌آزمایی فورمن (قانون طلایی: حدس زدن ممنوع)، و با تایید انسانی مبتنی بر توکن‌های امضاشده HMAC.

---

## 📊 جدول مقایسه فنی: چرا مهندسان سیستم مولوی را ترجیح می‌دهند؟

| شاخص / ویژگی معماری | TM Molavi Agentic OS | CrewAI | LangGraph | AutoGPT |
|---|---|---|---|---|
| **وابستگی‌های ران‌تایم** | **صفر (فقط کتابخانه استاندارد پایتون)** | سنگین (Pydantic, Chroma و ...) | وابسته به اکوسیستم LangChain | سنگین (داکر، ردیس و ...) |
| **استراتژی مصرف مدل** | **اولویت رایگان ($0.00 Ollama/Groq/Gemini)** | پیش‌فرض کلیدهای ابری پولی | پیش‌فرض کلیدهای ابری پولی | پیش‌فرض OpenAI |
| **گیت راستی‌آزمایی فورمن** | **تاییدیه دقیق شواهد فیزیکی و آرتیفکت** | تایید وضعیت اعلامی خود ایجنت | بررسی‌های دستی کاربر | غیرکنترل‌شده |
| **تاییدیه انسانی (Human-in-the-Loop)** | **تیکت‌های امضاشده HMAC کریپتوگرافیک (L0-L3)** | کال‌بک‌های ساده کلاینت | الگوی Interrupt | تایید متنی در ترمینال |
| **پروتکل ابزارها** | **درگاه بومی MCP + ممیزی امنیتی بامبل‌بی** | رپرهای اختصاصی ابزار | LangChain Tools | پلاگین‌های کاستوم |
| **مدیریت حافظه** | **حافظه محلی SQLite + مغز دوم ابسیدین/مارک‌داون** | دیتابیس برداری اجباری | Checkpointer State | حافظه برداری و فایل |
| **آداپتورهای چندپلتفرمی** | **Hermes Main, Hermes Desktop, Antigravity, Codex** | CLI اختصاصی | LangGraph Cloud | فقط وب اینترفیس |
| **بهینه‌سازی خودکار** | **حلقه آزمون و خطای Autoresearch با Keep/Revert** | ندارد | سرویس پولی LangSmith | ندارد |

---

## 🏛️ معماری کلان سیستم

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  آداپتورهای پلتفرم و ران‌تایم:                                         │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  تیم‌های چند ایجنتی و پایپ‌لاین‌های عملیاتی:                           │
│  • تیم پژوهش سئو و GEO             • حلقه پژوهش و بهینه‌سازی خودکار   │
│  • تیم تحلیل دیده‌شدن در چت‌بات‌ها • خط لوله هنداوف رسمی چند ایجنتی   │
│  • تیم تولید محتوای بدون اسلوپ     • مدیریت خطا، بک‌آف و فال‌بک خودکار │
│  • تیم سرنخ‌های B2B با تایید رسمی  • اشکال‌زدایی و پچ سیستماتیک کد     │
├────────────────────────────────────────────────────────────────────────┤
│  ۱۲ ایجنت تخصصی با امتیاز ۱۰۰/۱۰۰ اعتبارسنجی:                          │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  ۲۴ مهارت استاندارد ایجنت‌ها (SKILL.md) و رجیستری ابزارها:             │
│  • مهندسی ایجنت و قراردادها        • ممیزی امنیتی بامبل‌بی برای MCP    │
│  • تحلیل عمیق ریپوزیتوری           • ارزیابی کمی و متریک‌های Autoresearch│
│  • هوش اسناد و پارس اسکیما         • جمع‌آوری وب بدون هزینه توکن       │
│  • سنجش دیده‌پذیری هوش مصنوعی و GEO • اتصال به حافظه مغز دوم ابسیدین     │
├────────────────────────────────────────────────────────────────────────┤
│  زیرسیستم‌های هسته، امنیت و ارکستریشن:                                  │
│  • دیمون تایید انسانی با امضای HMAC دیجیتال (L2_HUMAN_APPROVAL)         │
│  • گیت اعتبارسنجی آرتیفکت‌های تجربی فورمن (قانون: حدس زدن ممنوع)        │
│  • صف وظایف Thread-Safe و اجراکننده گراف DAG بدون نیاز به ردیس یا سلری  │
│  • روتر هوشمند مدل‌های رایگان (اولویت اولاما و لاما ۳.۲، گروک و جمینای) │
│  • آداپتور مغز دوم مارک‌داون با نگه‌داری تغییرات غیرمخرب               │
│  • درگاه استاندارد MCP با فیلتر تزریق پرامپت و فرار از مسیر             │
│  • لجر تجربی پژوهش الهام‌گرفته از آندری کارپاتی با تصمیم Keep / Revert  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 شروع سریع در ۶۰ ثانیه

### ۱. نصب پکیج از PyPI
```bash
pip install molavi-agentic-os
```

یا کلون سورس کد مخزن برای توسعه محلی:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### ۲. اعتبارسنجی ۱۰۰/۱۰۰ با استاندارد Bot-Ready
```bash
molavi-agentic-os validate
```
خروجی ترمینال:
```text
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] fact-checker (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### ۳. اجرای پایپ‌لاین کامل اند-تو-اند
```bash
python examples/end_to_end_agent_workflow.py
```

---

## 💡 نمونه کدهای اجرایی

### ۱. مسیریابی مدل‌های رایگان محلی و ابری (هزینه ۰.۰۰ دلار)
```python
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider

router = ModelRouter()
local_model = MockProvider(fixed_response="معماری سیستم به صورت کاملاً آفلاین راستی‌آزمایی شد.")
router.register_provider("ollama-llama-3.2", local_model, ModelTier.FREE_LOCAL)

response = router.route_and_generate(
    prompt="بررسی معماری امنیتی و مرزبندی ایجنت‌ها",
    preferred_tier=ModelTier.FREE_LOCAL
)
print(f"مدل استفاده‌شده: {response.model_name} | هزینه: ${response.estimated_cost_usd:.2f}")
```

### ۲. گیت راستی‌آزمایی شواهد فورمن («حدس زدن ممنوع»)
```python
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

agent_output = {
    "status": "completed",
    "target_url": "https://molavi.pro/research",
    "evidence": ["HTTP 200 OK", "هدینگ‌های فنی با موفقیت استخراج شدند"]
}

artifacts = [
    VerificationArtifact("url_crawled", "string", agent_output["target_url"]),
    VerificationArtifact("evidence_ledger", "list", agent_output["evidence"])
]

result = ForemanVerificationGate.verify(agent_output, artifacts)
if result.is_verified:
    print(f"✅ تاییدیه فورمن صادر شد: {result.verified_artifacts}")
else:
    print(f"❌ رد شد: {result.failure_reason}")
```

### ۳. تایید انسانی با تیکت‌های امضاشده HMAC
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key-min-32-chars")
ticket = mgr.create_ticket(
    action="deploy_production_code",
    reason="انتشار رسمی نسخه v0.2.0 سیستم عامل",
    target="prod-cluster-01",
    impact="اعمال تغییرات روی کلاستر پروداکشن",
    risk="HIGH"
)
print(f"شناسه تیکت: {ticket.ticket_id} | نیازمند تایید انسانی: {ticket.requires_human_approval}")
```

### ۴. ممیزی امنیتی ابزارهای MCP با الهام از پروژه بامبل‌بی
```python
from molavi_agentic_os.mcp import BumblebeeMCPSecurityAuditor

audit = BumblebeeMCPSecurityAuditor.audit_invocation_arguments({
    "file_path": "../../etc/shadow",
    "command": "rm -rf /"
})
if not audit.is_safe:
    print(f"🚨 هشدار امنیتی: دستور پرخطر مسدود شد -> {audit.issues}")
```

### ۵. حلقه آزمایش و بهینه‌سازی اتونوموس (Autoresearch)
```python
from molavi_agentic_os.evaluation import AutoresearchLoop, ResearchHypothesis

hypothesis = ResearchHypothesis(
    id="EXP-OPT-01",
    target_component="پرامپت ایجنت ممیزی سئو",
    hypothesis_statement="کاهش تمپرچر به ۰.۲ دقت خروجی را بیش از ۵ درصد بهبود می‌دهد",
    baseline_metric=0.60,
    target_metric_key="accuracy"
)
loop = AutoresearchLoop(hypothesis)
decision = loop.run_trial(
    trial_number=1,
    parameters={"temperature": 0.2},
    eval_fn=lambda p: {"accuracy": 0.72}
)
print(f"نتیجه آزمایش ۱: {decision.action} ({decision.rationale})")
```

---

## 🌐 آداپتورهای خروجی برای محیط‌های اجرایی مختلف

```bash
# خروجی برای ران‌تایم اصلی هرمس (Hermes Main)
molavi-agentic-os install --platform hermes --agent research-agent

# خروجی برای هرمس دسکتاپ شخصی (فایل‌های محلی و محیط امن ایزوله)
molavi-agentic-os install --platform hermes-desktop --agent developer-agent

# خروجی برای محیط آی‌دی‌ای آنتی‌گرویتی (Antigravity IDE)
molavi-agentic-os install --platform antigravity --agent content-writer

# خروجی برای قوانین OpenAI Codex و Cursor
molavi-agentic-os install --platform codex --agent seo-auditor

# خروجی برای Claude Code (فایل CLAUDE.md)
molavi-agentic-os install --platform claude-code --agent project-manager
```

---

## 🔗 اکوسیستم پیوسته و مخازن همکار در گیت‌هاب

سیستم عامل مولوی به عنوان هسته اجرایی مرکزی در هماهنگی با سایر پروژه‌های تخصصی فعالیت می‌کند:

| مخزن همکار | تخصص | نقطه اتصال با TM Agentic OS |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | زیرساخت حافظه محلی مارک‌داون و ابسیدین برای ایجنت‌ها | لایه حافظه پایدار بین‌سشنی با لجر تغییرات غیرمخرب. |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | فریم‌ورک تجربی ارزیابی دیده‌شدن در چت‌بات‌های AI (Perplexity, Gemini, ChatGPT) | تأمین داده‌های واقعی استناد برای `geo-auditor`. |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | موتور ممیزی ۳ ستونه سئو، AEO و اسکیما | تغذیه کدهای بررسی فنی به `seo-auditor`. |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | خزنده و ابزار اتونوموس پایش و اصلاح کد و کانفیگ وب‌سایت | اعمال خودکار پچ‌های فنی بر اساس گزارش‌های ایجنت‌ها. |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | خزش و جمع‌آوری دترمینستیک وب بدون هزینه توکن | لایه استخراج داده بدون هزینه برای ایجنت‌های پژوهش. |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | کپی‌رایتینگ انسانی با آنتروپی صفر ($H \to 0$) و عبور از دتکتورها | هسته اصلی مهارت `unslop-humanizer` و نویسنده محتوا. |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | سرور FastMCP برای ارزیابی سئو و GEO | ارائه ابزارهای MCP استاندارد به ایجنت‌ها. |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | پلتفرم اتونوموس انتشار و ترافیک خبری در گوگل نیوز | اتصال به تیم تولید محتوا جهت اتوماسیون رسانه‌ای. |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | لجر شواهد علمی و مقالات بدون ارجاع ساختگی | استانداردسازی استنادها برای فکت‌چکر و پژوهشگر. |
| [`mcp-agent-skills-hub`](https://github.com/tmolavi/mcp-agent-skills-hub) | هاب توزیع اسکیل‌های کاربردی و کانفیگ‌های ابری ایجنت‌ها | کاتالوگ مهارت‌های گسترده برای محیط‌های کدنویسی. |
| [`tmolavi`](https://github.com/tmolavi/tmolavi) | پروفایل رسمی گیت‌هاب تقی مولوی | پایگاه مرکزی معرفی اکوسیستم و معماری پروژه‌ها. |

---

## 🛡️ پروژه‌های بالادستی و انطباق کامل لایسنس‌ها

این سیستم‌عامل با احترام کامل به جامعه متن‌باز و با بازپیاده‌سازی کاملاً مستقل (Clean-Room Implementation) از ۶ پروژه الهام گرفته است:
۱. **Andrej Karpathy — [Autoresearch](https://github.com/karpathy/autoresearch)** (لایسنس MIT)
۲. **Andrej Karpathy — [Nanochat](https://github.com/karpathy/nanochat)** (لایسنس MIT)
۳. **Sebastian Raschka — [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** (لایسنس Apache 2.0)
۴. **Forrest Chang — [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** (لایسنس MIT)
۵. **ComposioHQ — [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** (لایسنس Apache 2.0)
۶. **Perplexity AI — [Bumblebee](https://github.com/perplexityai/bumblebee)** (لایسنس Apache 2.0)

برای مشاهده تحلیل حقوقی عدم تعارض، به سند [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md) و [`SOURCES.md`](SOURCES.md) مراجعه فرمایید.

---

## ❓ پرسش‌های متداول (FAQ / AEO)

<details>
<summary><strong>سؤال: آیا اجرای سیستم‌عامل مولوی نیاز به نصب ردیس، سلری یا داکر دارد؟</strong></summary>

**خیر.** سیستم‌عامل مولوی با تکیه بر همروندی استاندارد پایتون (Thread-Safe Priority Queue و گراف حل وابستگی‌های DAG) پیاده‌سازی شده است. می‌توانید سارم‌های چند ایجنتی را روی لپ‌تاپ خود بدون نیاز به سرویس‌های پس‌زمینه اجرا کنید.
</details>

<details>
<summary><strong>سؤال: استراتژی مدل رایگان (Free-First) چگونه کار می‌کند؟</strong></summary>

روتر سیستم به صورت پیش‌فرض کارهای محلی را به اولاما (Ollama Llama 3.2 یا Mistral) هدایت می‌کند و کارهای وب را به تپ‌های ابری رایگان با سرعت بالا (Groq یا Google Gemini Free Tier) می‌فرستد. مدل‌های گران‌قیمت تجاری تنها با تایید مستقیم کاربر فعال می‌شوند.
</details>

<details>
<summary><strong>سؤال: گیت راستی‌آزمایی فورمن چگونه جلوی توهم ایجنت را می‌گیرد؟</strong></summary>

در این گیت، پرچم‌های متنی اعلامی ایجنت نادیده گرفته می‌شوند و سیستم وجود آرتیفکت‌های فیزیکی (فایل ذخیره‌شده، پاسخ کد HTTP، انطباق اسکیمای JSON، غیرخالی بودن خروجی) را بازرسی می‌کند. در صورت نبود شواهد، تسک رد می‌شود.
</details>

---

## 📈 تاریخچه ستاره‌های گیت‌هاب (Star History)

<div align="center" dir="ltr">

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

**⭐ این پروژه را دوست داشتید؟ ثبت یک ستاره در بالای صفحه گیت‌هاب تنها ۱ ثانیه زمان می‌برد اما حامی بزرگ این اکوسیستم متن‌باز است.**

</div>

---

## 📜 لایسنس و حاکمیت

تحت مجوز بین‌المللی **MIT License** منتشر شده است. حق نشر (c) ۲۰۲۶ متعلق به **تقی مولوی (Taghi Molavi)** است.  
مطابق با استاندارد حاکمیت متن‌باز TM در سند [`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md).

</div>
