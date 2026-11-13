<div dir="rtl" align="center">

# نظام تشغيل مولوي للوكلاء الذاتيين (TM Molavi Agentic OS)

### نظام تشغيل مفتوح المصدر ونمطي للوكلاء الذاتيين، والمهارات، والفرق متعددة الوكلاء، والذاكرة الدائمة، وأدوات بروتوكول MCP

[![إصدار PyPI](https://img.shields.io/pypi/v/molavi-agentic-os.svg?style=for-the-badge&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/molavi-agentic-os/)
[![بايثون 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![الاختبارات الآلية](https://img.shields.io/badge/CI-21%20Tests%20Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![ترخيص MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](../../LICENSE)
[![بدون تبعيات خارجية](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](../../pyproject.toml)

**لغات أخرى:**  
🌐 [English](../../docs/en/README.md) · [فارسی (الفارسية)](../../docs/fa/README.md) · [Türkçe (التركية)](../../docs/tr/README.md) · [Azərbaycan dili (الأذربيجانية)](../../docs/az/README.md)

---

⭐ **إذا كان TM Molavi Agentic OS مفيداً لمشاريعك، يرجى دعمنا بوضع نجمة (Star) للمستودع على GitHub للمساهمة في نمو هذا النظام المفتوح المصدر!**

---

</div>

<div dir="rtl">

## 1. نظرة عامة وفلسفة النظام

**TM Molavi Agentic OS** هو نظام تشغيل مفتوح المصدر ومستقل عن مزودي النماذج، مصمم لبناء وتشغيل وكلاء الذكاء الاصطناعي الذاتيين وفرق العمل متعددة الوكلاء بأعلى درجات الموثوقية.

### المزايا الهندسية الجوهرية:
- **صفر تبعيات خارجية عند التشغيل (Zero Runtime Dependencies):** يعمل بالكامل وبسرعة فائقة عبر مكتبة بايثون القياسية 3.10+ دون الحاجة إلى Redis أو Celery أو خوادم Docker معقدة.
- **بوابة التحقق الصارمة فورمن (Foreman Gate):** تعتمد المبدأ الذهبي *"ممنوع التخمين"*. لا يحق لأي وكيل اعتبار المهمة منجزة دون تقديم أدلة مادية ملموسة (بيانات فحص حقيقية، ملفات، نتائج اختبارات قابلة للتكرار).
- **أذونات الأمان المشفرة (HMAC Permission Slip):** تتطلب العمليات الحساسة (تنفيذ أوامر النظام، إرسال البريد، تعديل قواعد البيانات) موافقة بشرية مسبقة عبر تذاكر مشفرة (`L2_HUMAN_APPROVAL`).
- **توجيه النماذج المجانية أولاً (Free-First Router):** يمنح الأولوية للنماذج المحلية مفتوحة الأوزان (Ollama: Llama 3.2, Mistral) والخيارات السحابية المجانية (Groq, Gemini Free Tier) بتكلفة استدعاء تساوي 0.00 دولار.
- **محولات متعددة البيئات:** يدعم التصدير المباشر لبيئات Hermes Main، وHermes Desktop، وAntigravity IDE، وClaude Code، وOpenAI Codex.

---

## 2. البدء السريع خلال 60 ثانية

```bash
# تثبيت الحزمة الرسمية عبر مستودع PyPI
pip install molavi-agentic-os

# التحقق من جودة وجاهزية الوكلاء وفق معيار 100/100 Bot-Ready
molavi-agentic-os validate

# عرض جميع الوكلاء والمهارات والفرق المسجلة
molavi-agentic-os list all
```

### كود بايثون تفاعلي ($0.00 تكلفة)
```python
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

registry = ToolRegistry()
registry.register(ToolDefinition(
    name="inspect_page",
    description="فحص عناوين وبيانات الصفحة",
    parameters=[ToolParameter("url", "string", "رابط الموقع")],
    handler=lambda url: {"url": url, "status": 200, "headings": ["المقدمة", "الهيكل"]}
))

gateway = MCPGateway(registry=registry)
result = gateway.handle_call_tool("inspect_page", {"url": "https://molavi.pro"})

gate = ForemanVerificationGate.verify(
    output={"target": "https://molavi.pro", "evidence": ["HTTP 200 verified"]},
    expected_artifacts=[VerificationArtifact("target", "string", "https://molavi.pro")]
)
print("هل تم التحقق بنجاح؟:", gate.is_verified)
```

---

## 3. التكامل مع بيئة أدوات TM

* [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): نظام الذاكرة الدائمة المحلية القائم على Obsidian وMarkdown.
* [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): محرك الصياغة الإنسانية المتطورة الخالية من القوالب الاصطناعية.
* [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence): بنية استخراج وتتبع بيانات الويب بدون تكلفة توكنات.
* [`geo-scope`](https://github.com/tmolavi/geo-scope): قياس مدى ظهور العلامات التجارية في إجابات محركات الذكاء الاصطناعي التوليدية.

---

</div>

<div dir="rtl" align="center">
<sub>مرخص بموجب <a href="../../LICENSE">ترخيص MIT</a> — حقوق النشر (c) 2026 <a href="https://molavi.pro">تقي مولوي (Taghi Molavi)</a></sub>
</div>
