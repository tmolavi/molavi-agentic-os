<div align="center" dir="rtl">

# نظام تشغيل مولوي للوكلاء الذاتيين (TM Molavi Agentic OS)

### بيئة تشغيل مفتوحة المصدر ونمطية ومستقلة عن النماذج للوكلاء الأذكياء، والمهارات، والفرق متعددة الوكلاء، والذاكرة المحلية، والتنفيذ عبر منصات متعددة

[![إصدار PyPI](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ترخيص MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![صفر تبعيات](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![نقاط الجاهزية](https://img.shields.io/badge/Bot--Ready-100%2F100-purple?style=for-the-badge)](https://github.com/tmolavi/molavi-agentic-os)
[![تكلفة صفرية](https://img.shields.io/badge/Cost-%240.00%20(Free--First)-brightgreen?style=for-the-badge)](MODEL-REQUIREMENTS.md)

**تصميم وهندسة: [تقي مولوي (Taghi Molavi)](https://molavi.pro)** · *مهندس نظم الذكاء الاصطناعي وباحث في ظهور محركات الإجابة (GEO)*  
*یاد بگیر، یاد بده و اثری ماندگار خلق کن — تعلّم. شارك. اترك أثراً دائماً.*

```bash
pip install molavi-agentic-os
```

<div dir="ltr">

[English](README.md) · [فارسی (Persian)](README.fa.md) · [Türkçe (Turkish)](README.tr.md) · [Azərbaycan dili](README.az.md) · [العربية (Arabic)](README.ar.md)

</div>

<br/>

> ⭐ **إذا ساعدك هذا النظام في التخلص من تعقيدات البنية التحتية المرهقة وتفادي أوهام الوكلاء، يرجى التكرم بدعم المشروع بوضع نجمة (Star) على مستودع GitHub!**

</div>

---

<div dir="rtl">

## ⚡ معضلات أطر عمل الوكلاء في البيئات الإنتاجية الحقيقية

تواجه معظم أطر عمل وكلاء الذكاء الاصطناعي الحالية ثلاث عقبات تقنية حرجة عند نشرها في بيئات العمل الحقيقية:

١. **تضخم البنية التحتية والارتباط القسري (Infrastructure Sprawl):** تفرض عليك تشغيل خدمات خلفية معقدة مثل Redis و Celery و Docker وقواعد بيانات متجهات ضخمة حتى لتنفيذ تدفق بسيط من ۳ خطوات، مما يوقعك في فخ الفواتير الباهظة للنماذج السحابية.
٢. **حالات الإنجاز الوهمية (Hallucinated Done States):** يصرّح الوكيل بأن المهمة قد اكتملت بنجاح دون تنفيذ أي اختبار فعلي أو تقديم دليل مادي قابل للتحقق برمجياً.
٣. **انعدام الحدود الأمنية الصارمة:** تشغيل أوامر طرفية حساسة دون موافقة بشرية موقعة تشفيرياً ودون تدقيق أمني لأدوات بروتوكول سياق النموذج (MCP).

يقدم **TM Molavi Agentic OS** حلاً هندسياً جذرياً يعتمد بالكامل على مكتبة بايثون القياسية: لا حاجة لخوادم ردیس أو سيليري، مع إعطاء الأولوية القصوى للنماذج المحلية المفتوحة (Ollama: Llama 3.2, Mistral) والطبقات السحابية المجانية عالية السرعة (Groq, Gemini Free Tier) بتكلفة هامشية **0.00$**، بالإضافة إلى بوابة فورمن للتحقق الصارم ("ممنوع التخمين") ونظام تذاكر الموافقة البشرية المشفرة بـ HMAC.

---

## 📊 مصفوفة المقارنة الهندسية: لماذا يفضل المهندسون نظام مولوي؟

| المعيار / الخاصية الهندسية | TM Molavi Agentic OS | CrewAI | LangGraph | AutoGPT |
|---|---|---|---|---|
| **تبعيات بيئة التشغيل** | **صفر (مكتبة بايثون القياسية فقط)** | ثقيلة (Pydantic, Chroma وغيرها) | معتمدة على منظومة LangChain | ثقيلة (Docker, Redis وغيرها) |
| **استراتيجية استهلاك النماذج** | **المجاني أولاً (0.00$ Ollama/Groq/Gemini)** | نماذج سحابية مدفوعة افتراضياً | نماذج سحابية مدفوعة افتراضياً | نماذج OpenAI الافتراضية |
| **بوابة التحقق الصارم فورمن** | **فحص صارم للأدلة المادية والأثر الفعلي** | اعتماد تقرير الوكيل الذاتي | فحوصات يدوية يحددها المستخدم | غير مقيد |
| **نظام الموافقة البشرية** | **تذاكر HMAC مشفرة رقمياً (L0-L3)** | استدعاءات برمجية بسيطة | نمط المقاطعة (Interrupt) | تأكيد نصي في الطرفية |
| **بروتوكول الأدوات** | **شبه بوابة MCP مدمجة + تدقيق أمان بامبل‌بي** | مغلفات أدوات مخصصة | LangChain Tools | ملحقات مخصصة |
| **معمارية الذاكرة** | **ذاكرة SQLite محلية + العقل الثاني بـ Markdown/Obsidian** | قواعد بيانات متجهات إجبارية | Checkpointer State | مخزن متجهات |
| **محولات المنصات المتعددة** | **Hermes Main, Hermes Desktop, Antigravity, Codex** | واجهة أوامر خاصة | LangGraph Cloud | واجهة ويب فقط |
| **التحسين والتقييم الذاتي** | **حلقة تجارب Autoresearch مع قرارات Keep/Revert** | غير متوفر | خدمة مدفوعة (LangSmith) | غير متوفر |

---

## 🏛️ المعمارية العامة للنظام

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  محولات بيئات التشغيل والمنصات:                                        │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  فرق العمل متعددة الوكلاء والتدفقات المعتمدة:                          │
│  • فريق أبحاث SEO و GEO            • حلقة البحث والتحسين الذاتي        │
│  • فريق ظهور الذكاء الاصطناعي      • خط أنابيب التسليم الرسمي بين الفرق│
│  • فريق إنتاج المحتوى عالي الجودة  • إدارة الفشل والاسترجاع التلقائي   │
│  • فريق اكتساب العملاء المحتملين   • تصحيح الأخطاء البرمجية الممنهج    │
├────────────────────────────────────────────────────────────────────────┤
│  ١٢ وكيلاً متخصصاً (بدرجة جاهزية كاملة 100/100):                       │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  ٢٤ مهارة قياسية للوكلاء (SKILL.md) وسجل الأدوات:                      │
│  • هندسة الوكلاء والعقود البرمجية   • تدقيق أمان بامبل‌بي لأدوات MCP   │
│  • الفحص العميق لمستودعات الأكواد  • مقاييس Autoresearch الكمية        │
│  • استخراج المخططات وهندسة الوثائق • استخراج بيانات الويب بدون توكنات │
│  • تحليل الظهور في محركات التوليد  • ذاكرة العقل الثاني المتوافقة      │
├────────────────────────────────────────────────────────────────────────┤
│  الأنظمة الفرعية للأمان والأوركسترا:                                   │
│  • خادم الموافقة البشرية المشفر بـ HMAC (مستوى L2_HUMAN_APPROVAL)      │
│  • بوابة فورمن للتحقق من الأدلة المادية (قانون: ممنوع التخمين)         │
│  • طابور مهام آمن للخيوط ومحرك رسوم بيانية DAG دون الحاجة لـ Redis     │
│  • موجه النماذج المجانية أولاً (Ollama Llama-3.2، Groq، Gemini Free)   │
│  • ذاكرة العقل الثاني المحلية غير المدمرة لتاريخ التعديلات             │
│  • بوابة MCP القياسية مع فلترة حقن التوجيهات واختراق المسار            │
│  • دفتر تجارب الأبحاث المستوحى من أندريه كارباثي (Keep / Revert)       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 البدء السريع في ٦٠ ثانية

### ١. التثبيت عبر مستودع حزم PyPI الرسمي
```bash
pip install molavi-agentic-os
```

أو استنساخ المستودع للتطوير المحلي:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### ٢. التحقق من جاهزية الوكلاء والمهارات (درجة 100/100)
```bash
molavi-agentic-os validate
```
المخرجات:
```text
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] fact-checker (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### ٣. تشغيل تدفق العمل الشامل من البداية حتى النهاية
```bash
python examples/end_to_end_agent_workflow.py
```

---

## 💡 أمثلة برمجية قابلة للتنفيذ المباشر

### ١. توجيه النماذج الذكي (تكلفة هامشية 0.00$)
```python
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider

router = ModelRouter()
local_model = MockProvider(fixed_response="تم التحقق من معمارية النظام محلياً دون أي اتصال خارجي.")
router.register_provider("ollama-llama-3.2", local_model, ModelTier.FREE_LOCAL)

response = router.route_and_generate(
    prompt="تدقيق المعمارية الأمنية وحدود الوكلاء",
    preferred_tier=ModelTier.FREE_LOCAL
)
print(f"النموذج المستخدم: {response.model_name} | التكلفة: ${response.estimated_cost_usd:.2f}")
```

### ٢. بوابة فورمن للتحقق من الأدلة ("ممنوع التخمين")
```python
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

agent_output = {
    "status": "completed",
    "target_url": "https://molavi.pro/research",
    "evidence": ["HTTP 200 OK", "تم استخراج العناوين التقنية بنجاح"]
}

artifacts = [
    VerificationArtifact("url_crawled", "string", agent_output["target_url"]),
    VerificationArtifact("evidence_ledger", "list", agent_output["evidence"])
]

result = ForemanVerificationGate.verify(agent_output, artifacts)
if result.is_verified:
    print(f"✅ تمت موافقة فورمن الرسمية: {result.verified_artifacts}")
else:
    print(f"❌ تم الرفض لغياب الأدلة: {result.failure_reason}")
```

### ٣. الموافقة البشرية بتذاكر HMAC المشفرة
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key-min-32-chars")
ticket = mgr.create_ticket(
    action="deploy_production_code",
    reason="إطلاق الإصدار الرسمي v0.2.0 لنظام التشغيل",
    target="prod-cluster-01",
    impact="تحديث مباشر في بيئة الإنتاج الحية",
    risk="HIGH"
)
print(f"معرف التذكرة: {ticket.ticket_id} | يتطلب موافقة بشرية: {ticket.requires_human_approval}")
```

---

## 🌐 محولات التصدير لمنصات العمل المختلفة

```bash
# التصدير لمنصة هرمس الرئيسية (Hermes Main)
molavi-agentic-os install --platform hermes --agent research-agent

# التصدير لبيئة هرمس ديسكتوب الشخصية المعزولة
molavi-agentic-os install --platform hermes-desktop --agent developer-agent

# التصدير لبيئة Antigravity IDE البرمجية
molavi-agentic-os install --platform antigravity --agent content-writer

# التصدير لمنصة OpenAI Codex وقواعد Cursor
molavi-agentic-os install --platform codex --agent seo-auditor

# التصدير لمنصة Claude Code (ملف CLAUDE.md)
molavi-agentic-os install --platform claude-code --agent project-manager
```

---

## 🔗 التكامل المترابط مع مستودعات منظومة TM على GitHub

يعمل هذا النظام كمركز ثقل تشغيلي متكامل مع مستودعات تقی مولوی المفتوحة المصدر:

| المستودع | التخصص الدقيق | آلية التكامل مع TM Agentic OS |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | بنية الذاكرة الدائمة للوكلاء بـ Markdown و Obsidian | طبقة الذاكرة الدائمة بين الجلسات مع سجل تدقيق غير مدمر. |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | إطار قياس الظهور الميداني في إجابات محركات الذكاء الاصطناعي | يزود وكيل `geo-auditor` بسجلات الاستشهاد الحقيقية. |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | محرك التدقيق الفني الشامل لـ SEO و AEO والمخططات | يغذي الوكلاء بقواعد الفحص الفني للويب. |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | الزاحف الذاتي لفحص وإصلاح مواقع الويب تلقائياً | ينفذ التعديلات والإصلاحات البرمجية بناءً على التقارير. |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | الزاحف المحدد لاستخراج بيانات الويب بدون توكنات | طبقة تزويد الوكلاء بالبيانات المجانية من الإنترنت. |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | الصياغة البشرية بصفر إنتروبيا وتجاوز كواشف الذكاء الاصطناعي | المحرك الأساسي لمهارة صياغة المحتوى عالي الجودة. |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | خادم FastMCP لتدقيق الظهور ومحركات الإجابة | يوفر أدوات MCP قياسية لوكلاء النظام. |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | منصة النشر الذاتي وأتمتة غرف الأخبار في Google News | يرتبط بفريق إنتاج المحتوى لأتمتة الصحافة الرقمية. |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | سجلات الأدلة العلمية والأبحاث بدون مراجع وهمية | يزود فاحص الحقائق بمخططات إثبات موثوقة. |
| [`tmolavi`](https://github.com/tmolavi/tmolavi) | المستودع التعريفي الرسمي لتقي مولوي | المركز التعريفي الأول لربط معمارية المنظومة كاملة. |

---

## 🛡️ المشاريع المرجعية وتوافق التراخيص مفتوحة المصدر

تم بناء هذا النظام باحترام عميق للمجتمع التقني المفتوح مع إعادة كتابة معمارية مستقلة ونظيفة (Clean-Room Implementation) مستوحاة من ٦ مشاريع رائدة:
١. **Andrej Karpathy — [Autoresearch](https://github.com/karpathy/autoresearch)** (ترخيص MIT)
٢. **Andrej Karpathy — [Nanochat](https://github.com/karpathy/nanochat)** (ترخيص MIT)
٣. **Sebastian Raschka — [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** (ترخيص Apache 2.0)
٤. **Forrest Chang — [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** (ترخيص MIT)
٥. **ComposioHQ — [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** (ترخيص Apache 2.0)
٦. **Perplexity AI — [Bumblebee](https://github.com/perplexityai/bumblebee)** (ترخيص Apache 2.0)

للاطلاع على التحليل القانوني الكامل لعدم التعارض، يرجى مراجعة وثيقة [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md) و [`SOURCES.md`](SOURCES.md).

---

## ❓ الأسئلة الشائعة (FAQ / AEO)

<details>
<summary><strong>سؤال: هل يتطلب تشغيل النظام تثبيت Docker أو Redis أو Celery؟</strong></summary>

**لا.** تم بناء النظام بالكامل باستخدام مكتبات بايثون القياسية المتزامنة (Thread-Safe TaskQueue وحل رسوم الاعتمادية DAG). يمكنك تشغيل أسراب كاملة من الوكلاء محلياً على جهازك المحمول دون الحاجة لأي خدمات خلفية إضافية.
</details>

<details>
<summary><strong>سؤال: كيف تعمل استراتيجية النماذج المجانية أولاً (Free-First)؟</strong></summary>

يقوم الموجه الذكي افتراضياً بتشغيل النماذج المحلية عبر Ollama أو استخدام الطبقات السحابية المجانية فائقة السرعة مثل Groq و Google Gemini Free Tier. النماذج التجارية المدفوعة لا تُستخدم إلا بموافقة صريحة للمهام المعقدة.
</details>

---

## 📈 سجل النجوم على GitHub (Star History)

<div align="center" dir="ltr">

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

**⭐ هل نال هذا المشروع إعجابك؟ منح نجمة للمستودع في أعلى الصفحة يستغرق ثانية واحدة فقط لكنه يقدم دعماً هائلاً لهذه المنظومة مفتوحة المصدر!**

</div>

---

## 📜 الترخيص والحوكمة

منشور تحت رخصة **MIT License** الدولية. حقوق النشر (c) 2026 محفوظة للمهندس **تقي مولوي (Taghi Molavi)**.  
متوافق بنسبة 100% مع معيار حوكمة المصادر المفتوحة في وثيقة [`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md).

</div>
