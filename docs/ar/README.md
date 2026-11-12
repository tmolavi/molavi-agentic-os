# حزمة وكلاء الذكاء الاصطناعي TM (نظام تشغيل مولوي للوكلاء الذاتيين)

<div align="center">

**نظام تشغيل مفتوح المصدر ونمطي ومستقل عن النماذج للوكلاء الذاتيين، والمهارات، والفرق متعددة الوكلاء، والذاكرة المحلية، والتنفيذ عبر منصات متعددة**  
*ابنِ وكلاء أكثر ذكاءً. شكّل فرق عمل أكثر كفاءة. أتمت مهامك الحقيقية بأدلة تجريبية قابلة للتحقق وبدون أي تخمين.*

[![إصدار PyPI](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=flat-square)](https://pypi.org/project/molavi-agentic-os/)
[![حالة CI](https://img.shields.io/github/actions/workflow/status/tmolavi/molavi-agentic-os/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![ترخيص MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](../../LICENSE)
[![تكلفة صفرية](https://img.shields.io/badge/التكلفة-0.00%24%20(النماذج%20المجانية%20أولاً)-brightgreen?style=flat-square)](../../MODEL-REQUIREMENTS.md)
[![مهندس النظام](https://img.shields.io/badge/تقي%20مولوي-Molavi.pro-orange?style=flat-square)](https://molavi.pro)

[English (Root)](../../README.md) · [English (Docs)](../en/README.md) · [فارسی](../fa/README.md) · [Türkçe](../tr/README.md) · [Azərbaycan dili](../az/README.md) · [العربية](README.md)

</div>

---

## 🏛️ وثائق الحوكمة ومصفوفة التوافق
* **معيار حوكمة المصادر المفتوحة TM:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **شفافية متطلبات النماذج والتكلفة:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **مصفوفة توافق التراخيص:** [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md)
* **المصادر والأصل التقني:** [`SOURCES.md`](../../SOURCES.md)

---

## 1. نظرة عامة وفلسفة النظام

**TM Molavi Agentic OS** هو إطار عمل مفتوح المصدر ونمطي ومستقل عن أي نموذج محدد، طوره المهندس **تقي مولوي (Taghi Molavi)** كبديل للأنظمة الهشة والمعتمدة على بنى تحتية معقدة.

يقوم النظام على خمس ركائز هندسية:
1. **استراتيجية النماذج المجانية أولاً (Free-First):** التنفيذ المباشر على النماذج المحلية خفيفة الوزن (Ollama: Llama 3.2, Mistral) والطبقات السحابية المجانية (Groq, Gemini Free Tier) بتكلفة هامشية قدرها **0.00$**.
2. **أمان الموافقة البشرية (Permission-Slip):** تخضع العمليات الحساسة (إرسال البريد الإلكتروني، تعديل قواعد البيانات، نشر الكود البرمجي) لبروتوكول `L2_HUMAN_APPROVAL` وتتطلب تذكرة موافقة رقمية موقعة بـ HMAC.
3. **بوابة التحقق الصارم فورمن (ممنوع التخمين):** لا يحق لأي وكيل اعتبار المهمة منتهية دون تقديم دليل مادي وملموس يمكن التحقق منه برمجياً.
4. **أمان بروتوكول سياق النموذج (Bumblebee MCP Security):** فحص أمني دقيق يمنع الأوامر الطرفية الخطيرة (`rm -rf`، `curl | bash`) وهجمات اختراق المسار وحقن التوجيهات.
5. **محولات بيئات التشغيل المتعددة:** تصدير مباشر ومتوافق مع **Hermes Main**، و **Hermes Personal Desktop**، و **Antigravity IDE**، و **OpenAI Codex / Cursor**، و **Claude Code**.

---

## 2. التثبيت والبدء السريع

### التثبيت عبر PyPI:
```bash
pip install molavi-agentic-os
```

### التثبيت من المصدر:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### أوامر سطر الأوامر (CLI):
```bash
# التحقق من جاهزية الوكلاء (100/100)
molavi-agentic-os validate

# عرض جميع مكونات النظام
molavi-agentic-os list all

# تصدير التكوينات للمنصات المستهدفة
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform hermes-desktop --agent developer-agent
molavi-agentic-os install --platform antigravity --agent content-writer
molavi-agentic-os install --platform codex --agent seo-auditor
```

---

## 3. التكامل مع منظومة TM

- [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): نظام الذاكرة المحلية الدائمة للوكلاء بتنسيق Markdown و Obsidian.
- [`geo-scope`](https://github.com/tmolavi/geo-scope): إطار قياس الظهور الميداني في إجابات الذكاء الاصطناعي (Perplexity, ChatGPT, Gemini).
- [`sage-audit`](https://github.com/tmolavi/sage-audit): محرك التدقيق الفني الشامل لـ SEO و AEO.
- [`siteprobe`](https://github.com/tmolavi/siteprobe): الزاحف الذاتي لفحص وإصلاح مواقع الويب تلقائياً.
- [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): محرك الصياغة البشرية خالية من حشو الذكاء الاصطناعي.

---

## 4. الاختبارات والتحقق البرمجي

```bash
pytest -v
python scripts/check_governance.py
```

---

## 5. الترخيص وحقوق الملكية

مرخص تحت رخصة **MIT License**. حقوق النشر (c) 2026 **تقي مولوي (Taghi Molavi)**.
