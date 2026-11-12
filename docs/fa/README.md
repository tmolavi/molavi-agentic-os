# تولکیت ایجنت‌های هوش مصنوعی TM (مولوی ایجنتیک او‌اس)

<div align="center">

**اکوسیستم متن‌باز، ماژولار و مستقل از مدل برای ایجنت‌های خودمختار، مهارت‌ها، تیم‌های چند ایجنتی، حافظه محلی و اجرای چند پلتفرمی**  
*ایجنت‌های هوشمندانه‌تر بسازید. تیم‌های کارآمدتر تشکیل دهید. کارهای واقعی را با شواهد تجربی و بدون توهم خودکار کنید.*

[![نسخه PyPI](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=flat-square)](https://pypi.org/project/molavi-agentic-os/)
[![وضعیت CI](https://img.shields.io/github/actions/workflow/status/tmolavi/molavi-agentic-os/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![مجوز MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](../../LICENSE)
[![هزینه صفر مارجینال](https://img.shields.io/badge/هزینه-۰.۰۰%20دلار%20(اولین%20مدل%20رایگان)-brightgreen?style=flat-square)](../../MODEL-REQUIREMENTS.md)
[![معمار سیستم](https://img.shields.io/badge/تقی%20مولوی-Molavi.pro-orange?style=flat-square)](https://molavi.pro)

[English (Root)](../../README.md) · [English (Docs)](../en/README.md) · [فارسی](README.md) · [Türkçe](../tr/README.md) · [Azərbaycan dili](../az/README.md) · [العربية](../ar/README.md)

</div>

---

## 🏛️ اسناد حاکمیتی، سازگاری لایسنس و استانداردها
* **سند استاندارد حاکمیت متن‌باز TM:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **شفافیت مصرف توکن و مدل‌های رایگان:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **ماتریس سازگاری لایسنس و منابع بالادستی:** [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md)
* **موجودی و برنامه مهاجرت مخازن ۲۴گانه:** [`docs/repository-governance/EXISTING-REPOSITORIES.md`](../repository-governance/EXISTING-REPOSITORIES.md)

---

## ۱. معرفی و فلسفه پروژه

**TM Molavi Agentic OS** یک فریم‌ورک متن‌باز، ماژولار و مستقل از مدل است که تحت اکوسیستم متن‌باز **TM (تقی مولوی - Taqi Molavi)** برای سیستم‌های ایجنتیک پیشرفته و توزیع‌شده طراحی شده است.

برخلاف پرامپت‌لیست‌های تبلیغاتی یا فریم‌ورک‌های سنگین و شکننده‌ای که برای کار کردن نیازمند زیرساخت‌های سرسام‌آور (دیمون‌های Redis، Celery، داکر و سرویس‌های ابری پولی) هستند، **مولوی ایجنتیک او‌اس** بر پایه پنج اصل مهندسی استوار است:

۱. **استراتژی اولویت مدل‌های رایگان (Free-First):** اجرای کامل روی مدل‌های سبک محلی (Ollama: Llama 3.2, Mistral) و سرویس‌های پرسرعت رایگان (Groq, Gemini Free Tier) با هزینه حاشیه‌ای **۰.۰۰ دلار**.
۲. **امنیت تضمین‌شده با تایید انسانی (Permission-Slip):** توقف عملیات حساس (ارسال ایمیل، انتشار محتوا، تغییرات دیتابیس، استقرار کد) طبق پروتکل `L2_HUMAN_APPROVAL` و صدور تیکت‌های امضاشده کریپتوگرافیک با کلید HMAC.
۳. **گیت راستی‌آزمایی فورمن (قانون طلایی: حدس زدن ممنوع):** هیچ ایجنتی حق ندارد تسک را «انجام شد» علامت بزند مگر اینکه آرتیفکت و شواهد تجربی و فیزیکی تولید کرده باشد.
۴. **امنیت MCP با الهام از پروژه بامبل‌بی (Bumblebee Security):** بازرسی ایستا و پویای ابزارها و دستورات خطرناک ترمینال (`rm -rf`، `curl | bash`)، مهار نفوذ به مسیرهای حساس و دفاع در برابر تزریق پرامپت (Prompt Injection).
۵. **سازگاری چندپلتفرمی و آداپتورهای اختصاصی:** خروجی مستقیم و سازگاری دوجانبه با **Hermes Main**، **Hermes Personal Desktop**، **Antigravity IDE**، **OpenAI Codex / Cursor** و **Claude Code**.

---

## ۲. مشخصات و امکانات نسخه v0.2.0

* **۱۲ ایجنت تخصصی با امتیاز ۱۰۰/۱۰۰ در ارزیابی Bot-Ready:**
  - `research-agent`: تحلیل‌گر ارشد پژوهش و گردآوری داده با استناد به منابع اولیه
  - `seo-auditor`: آدیتور تکنیکال سئو، ساختار اسکیما و شاخص‌های حیاتی وب (Core Web Vitals)
  - `geo-auditor`: متخصص دیده‌شدن برند در موتورهای هوش مصنوعی (Perplexity, ChatGPT, Gemini)
  - `ai-visibility-analyst`: تحلیل سهم صدای برند (Share of Voice) در چت‌بات‌ها
  - `content-strategist`: استراتژیست کلاستر محتوایی و خوشه‌های اعتبار موضوعی
  - `content-writer`: نویسنده تکنیکال و مقالات انسانی بدون پرتی‌های کلامی هوش مصنوعی (Unslop)
  - `fact-checker`: فکت‌چکر مستقل و سنجش اعتبار گزاره‌ها با شواهد ریاضی و آرتیفکت
  - `code-reviewer`: بازبین ارشد کد، امنیت و استانداردهای Clean Code
  - `developer-agent`: توسعه‌دهنده سیستم‌های ماژولار با تست‌های یونیت پایدار
  - `marketing-analyst`: تحلیل‌گر فانل، شاخص‌های نرخ تبدیل (CRO) و هوش تجاری
  - `lead-researcher`: پژوهشگر اکانت‌های کلیدی B2B و احراز صلاحیت ICP
  - `project-manager`: مدیر عملیات، شکستن پروژه‌ها و مدیریت صف تسک‌ها

* **۲۴ مهارت استاندارد Agent Skills (`SKILL.md`):**
  - پوشش کامل ۱۴ حوزه الزامی: مهندسی ایجنت، استانداردهای کدنویسی، تحلیل ریپوزیتوری، دستیار پژوهش، هوش اسناد، سئو، GEO، دیده‌شدن در چت‌بات‌ها، هوش وب، ارکستریشن چند ایجنتی، اشکال‌زدایی سیستماتیک، ممیزی امنیتی بامبل‌بی، ارزیابی و تست اتونوموس، و حلقه پژوهش خودکار.

* **درگاه MCP و رجیستری ابزارها (Tools Registry & MCP Gateway):**
  - رجیستری ابزارها با اعتبارسنجی اسکیمای JSON، مدیریت تایم‌اوت، مدیریت خطای ایزوله، و ارزیابی امنیتی ورودی‌ها.

* **موتور ارزیابی Autoresearch (الهام‌گرفته از آندری کارپاتی):**
  - حلقه آزمایش‌های اتونوموس برای پرامپت‌ها و ورک‌فلوها با تصمیم‌گیری خودکار نگه داشتن (Keep) یا بازگردانی (Revert) بر اساس متریک‌های کمی.

* **اتصال به حافظه مغز دوم (`tm-second-brain`):**
  - ذخیره‌سازی محلی نوت‌های مارک‌داون با هدرهای YAML و ردیابی غیرمخرب تاریخچه تغییرات.

---

## ۳. نحوه نصب و راه‌اندازی سریع

### نصب مستقیم از طریق PyPI:
```bash
pip install molavi-agentic-os
```

### نصب سورس و حالت توسعه (Editable):
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### اعتبارسنجی و دستورات ترمینال:
```bash
# اعتبارسنجی ۱۰۰/۱۰۰ تمام اجزا
molavi-agentic-os validate

# نمایش لیست اجزای اکوسیستم
molavi-agentic-os list all

# خروجی گرفتن برای ران‌تایم‌های مختلف
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform hermes-desktop --agent developer-agent
molavi-agentic-os install --platform antigravity --agent content-writer
molavi-agentic-os install --platform codex --agent seo-auditor
```

---

## ۴. ارتباط و هم‌افزایی با اکوسیستم TM

این فریم‌ورک هسته عملیاتی متمرکز اکوسیستم ابزارهای متن‌باز تقی مولوی است:

| ریپوزیتوری | نقش تخصصی | هم‌افزایی با Agentic OS |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | سیستم حافظه پایدار مارک‌داون و ابسیدین برای ایجنت‌ها | لایه ذخیره و بازیابی دائمی دانش ایجنت‌ها |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | فریم‌ورک سنجش دیده‌شدن برند در Perplexity و ChatGPT | خوراک داده‌های استناد تجربی برای `geo-auditor` |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | موتور ممیزی سه‌گانه سئو، AEO و اسکیما | تغذیه کدهای بررسی فنی به `seo-auditor` |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | اصلاح‌گر اتونوموس کد و کانفیگ وب‌سایت‌ها | اعمال خودکار پچ‌های فنی حاصل از گزارش‌ها |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | خزنده و پردازشگر دترمینستیک بدون مصرف توکن | زیرساخت استخراج داده برای مهارت‌های وب |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | کپی‌رایتینگ انسانی با آنتروپی صفر و حذف پرتی‌ها | موتور مهارت `unslop-humanizer` و نویسنده محتوا |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | پلتفرم اتونوموس انتشار و ترافیک خبری | اتصال به تیم تولید محتوا جهت اتوماسیون رسانه‌ای |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | سرور FastMCP برای ارزیابی سئو و GEO | درگاه استاندارد ابزارهای MCP برای محیط‌های کدنویسی |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | لجر شواهد علمی و مقالات بدون ارجاع ساختگی | پروتکل فکت‌چکینگ و مستندسازی علمی |

---

## ۵. تست و راستی‌آزمایی کیفیت

```bash
# اجرای کلیه تست‌های یونیت
pytest -v

# راستی‌آزمایی انطباق ۱۰۰ درصدی با حاکمیت TM
python scripts/check_governance.py
```

---

## ۶. لایسنس و حقوق مالکیت فکری

این پروژه تحت مجوز **MIT License** توسط **تقی مولوی (Taghi Molavi)** منتشر شده است. کلیه ایده‌های الهام‌گرفته از مراجع بالادستی با رعایت کامل حقوق معنوی و بر اساس استانداردهای بازطراحی پاکیزه (Clean-Room Adaptation) مستند شده‌اند.
