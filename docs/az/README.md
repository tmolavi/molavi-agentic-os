# TM Molavi Agentic OS — Azərbaycan dilində Sənədləşmə

<div align="center">

**Avtonom Süni İntellekt Agentləri, Bacarıqlar, Çoxagentli Komandalar, Yerli Yaddaş və Platformalararası İcra üçün Açıq Mənbəli Əməliyyat Ekosistemi**  
*Daha ağıllı agentlər qurun. Daha səriştəli komandalar təşkil edin. İstehsalat sistemlərini real sübutlarla avtomatlaşdırın.*

[![PyPI Versiyası](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=flat-square)](https://pypi.org/project/molavi-agentic-os/)
[![CI Vəziyyəti](https://img.shields.io/github/actions/workflow/status/tmolavi/molavi-agentic-os/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![MIT Lisenziyası](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](../../LICENSE)
[![Sıfır Xərc](https://img.shields.io/badge/X%C9%99rc-0.00%24%20(Free--First)-brightgreen?style=flat-square)](../../MODEL-REQUIREMENTS.md)
[![Memar](https://img.shields.io/badge/Memar-Ta%C4%9F%C4%B1%20M%C3%B6vl%C9%99vi-orange?style=flat-square)](https://molavi.pro)

[English (Root)](../../README.md) · [English (Docs)](../en/README.md) · [فارسی](../fa/README.md) · [Türkçe](../tr/README.md) · [Azərbaycan dili](README.md) · [العربية](../ar/README.md)

</div>

---

## 🏛️ İdarəetmə Sənədləri və Şəffaflıq
* **TM Açıq Mənbə İdarəetmə Standartı:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **Model Tələbləri və Xərc Şəffaflığı:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **Lisenziya Uyğunluq Matrisi:** [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md)
* **Mənbələr və Sübutlar:** [`SOURCES.md`](../../SOURCES.md)

---

## 1. Ümumi Baxış və Memarlıq Fəlsəfəsi

**TM Molavi Agentic OS**, xarici asılılıqları aradan qaldıran və **Tağı Mövləvi** tərəfindən hazırlanmış açıq mənbəli süni intellekt agenti əməliyyat sistemidir.

Sistem 5 mühəndislik prinsipinə əsaslanır:
1. **Əvvəlcə Pulsuz Model Strategiyası (Free-First):** Yerli modelləri (Ollama: Llama 3.2, Mistral) və pulsuz bulud sistemlərini (Groq, Gemini Free Tier) prioritetləşdirərək **0.00$** xərclə işləyir.
2. **Permission-Slip İnsan Təsdiqi:** E-poçt göndərilməsi, verilənlər bazası dəyişiklikləri və kod yerləşdirilməsi kimi həssas əməliyyatlar `L2_HUMAN_APPROVAL` səviyyəsində saxlanılır və HMAC imzalı rəqəmsal bilet tələb olunur.
3. **Foreman Doğrulama Qapısı (Ehtimal etmək qadağandır):** Heç bir agent fiziki sübut və ya artefakt təqdim etmədən tapşırığı tamamlanmış elan edə bilməz.
4. **Bumblebee MCP Təhlükəsizliyi:** Təhlükəli terminal əmrlərini (`rm -rf`, `curl | bash`) və yol aşma cəhdlərini bloklayan təhlükəsizlik auditi.
5. **Çoxplatformalı Uyğunluq:** **Hermes Main**, **Hermes Desktop**, **Antigravity IDE**, **OpenAI Codex / Cursor** və **Claude Code** üçün birbaşa eksport.

---

## 2. Quraşdırma və Tez Başlama

### PyPI vasitəsilə quraşdırma:
```bash
pip install molavi-agentic-os
```

### Mənbə kodundan inkişaf quraşdırması:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### CLI əmrləri:
```bash
# Bot-Ready Doğrulaması (100/100 Xal)
molavi-agentic-os validate

# Ekosistem Komponentlərini Göstər
molavi-agentic-os list all

# Platformalar üçün Eksport
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform hermes-desktop --agent developer-agent
molavi-agentic-os install --platform antigravity --agent content-writer
molavi-agentic-os install --platform codex --agent seo-auditor
```

---

## 3. Ekosistem Əlaqələri

- [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): Yerli Markdown və Obsidian əsaslı davamlı yaddaş.
- [`geo-scope`](https://github.com/tmolavi/geo-scope): Süni intellekt cavab sistemlərində görünürlük meyarları.
- [`sage-audit`](https://github.com/tmolavi/sage-audit): Texniki SEO, AEO və sxem auditi.
- [`siteprobe`](https://github.com/tmolavi/siteprobe): Avtonom sayt təmiri və diaqnostikası.
- [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): İnsani və detektorları keçən mətn yazarlığı.

---

## 4. Testlər

```bash
pytest -v
python scripts/check_governance.py
```

---

## 5. Lisenziya

Bu layihə **MIT Lisenziyası** altında yayımlanmışdır. Müəllif hüquqları (c) 2026 **Tağı Mövləvi**.
