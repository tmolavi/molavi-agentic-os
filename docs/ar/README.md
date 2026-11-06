# حزمة أدوات وكلاء الذكاء الاصطناعي TM (مولوي إيجنتك)

<p align="center">
  <strong>Molavi Agentic OS: منظومة مفتوحة المصدر للوكلاء المستقلين، المهارات، فرق العمل متعددة الوكلاء، وسير العمل التلقائي.</strong><br>
  <em>ابنِ وكلاء أذكى. كوّن فرق عمل أفضل. أتمت الأعمال الحقيقية.</em>
</p>

---

## 🏛️ وثائق الحوكمة وشفافية النماذج
* **معيار حوكمة المصادر المفتوحة TM:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **شفافية النماذج والبدائل المجانية:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **سجل وخطة ترحيل المستودعات الـ ٢٤:** [`docs/repository-governance/EXISTING-REPOSITORIES.md`](../repository-governance/EXISTING-REPOSITORIES.md)

---

## ١. نظرة عامة

**TM AI Agent Toolkit** (نظام مولوي لتشغيل الوكلاء الأذكياء - Molavi Agentic OS) هو إطار عمل هندسي مفتوح المصدر ومستقل عن النماذج المحتكرة، طُوّر تحت مظلة **TM (تقي مولوي - Taqi Molavi)** لنظم الوكلاء الذاتية المتقدمة.

### المبادئ الهندسية الأساسية:
١. **أولوية النماذج المجانية (Free-First):** إمكانية التشغيل محلياً بشكل كامل وبدون تكلفة باستخدام نماذج مفتوحة الأوزان (Ollama) والخدمات السحابية المجانية (Groq, Gemini Free Tier).
٢. **أمان الإجراءات مع الموافقة البشرية (Permission-Slip):** العمليات الحساسة (مثل إرسال البريد، النشر، العمليات المالية) تخضع لمستوى `L2_HUMAN_APPROVAL` وتتطلب تذكرة موافقة موثقة برمجياً.
٣. **بوابة فورمن للتحقق (Foreman Verification):** منع التخمين والهلوسة؛ لا يُعتبر أي عمل منجزاً دون تقديم شواهد وروابط ومخرجات ملموسة.

---

## ٢. التثبيت والبدء السريع

```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .

# التحقق من جاهزية كافة الوكلاء
molavi-agentic-os validate

# استعراض مكونات النظام
molavi-agentic-os list all
```

---

## ٣. فلسفة العلامة التجارية

* **صاحب المشروع:** تقي مولوي (Taqi Molavi)
* **التخصص:** هندسة نظم الذكاء الاصطناعي | استراتيجيات SEO و GEO
* **الشعار:** كن مرئياً. بع بشكل أفضل. ابنِ السلطة والموثوقية. (Be Visible. Sell Better. Build Authority.)
* **الموقع الرسمي:** [molavi.pro](https://molavi.pro)
