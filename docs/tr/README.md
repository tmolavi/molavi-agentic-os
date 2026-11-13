# TM Molavi Agentic OS — Türkçe Kapsamlı Dokümantasyon

<div align="center">

**Otonom Yapay Zekâ Ajanları, Beceriler, Ekipler ve Yerel Bellek için Açık Kaynaklı Modüler İşletim Ekosistemi**

[![PyPI Sürümü](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=flat-square)](https://pypi.org/project/molavi-agentic-os/)
[![CI Durumu](https://img.shields.io/github/actions/workflow/status/tmolavi/molavi-agentic-os/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![MIT Lisansı](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](../../LICENSE)
[![Sıfır Maliyet](https://img.shields.io/badge/Maliyet-0.00%24%20(Free--First)-brightgreen?style=flat-square)](../../MODEL-REQUIREMENTS.md)

[English](../../README.md) · [English Docs](../en/README.md) · [فارسی](../fa/README.md) · [Türkçe (Kök Sayfa)](../../README.tr.md) · [Azərbaycan dili](../az/README.md) · [العربية](../ar/README.md)

</div>

---

## 🏛️ Yönetişim Belgeleri ve Şeffaflık
* **TM Açık Kaynak Yönetişim Standardı:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **Model Gereksinimleri ve Maliyet Şeffaflığı:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **Lisans Uyumluluk Matrisi:** [`LICENSE_COMPATIBILITY.md`](../../LICENSE_COMPATIBILITY.md)
* **Kaynaklar ve Provenans:** [`SOURCES.md`](../../SOURCES.md)

---

## 1. Genel Bakış ve Mimari Felsefesi

**TM Molavi Agentic OS**, bağımlılık yükü yüksek ve kırılgan çerçevelere alternatif olarak **Taghi Molavi** tarafından geliştirilmiş açık kaynaklı, modelden bağımsız bir yapay zekâ ajanı işletim sistemidir.

Sistem beş temel mühendislik ilkesine dayanır:
1. **Önce Ücretsiz Model Stratejisi (Free-First):** Yerel açık ağırlıklı modelleri (Ollama: Llama 3.2, Mistral) ve sıfır maliyetli bulut katmanlarını (Groq, Gemini Free Tier) önceliklendirerek **0.00$** marjinal maliyetle çalışır.
2. **Permission-Slip İnsan Onay Mekanizması:** E-posta gönderimi, veritabanı değişiklikleri veya kod dağıtımı gibi hassas işlemler `L2_HUMAN_APPROVAL` düzeyinde durdurulur ve kriptografik HMAC imzalı onay bileti üretilir.
3. **Foreman Doğrulama Kapısı (Tahmin Yasaktır):** Hiçbir ajan, somut ve doğrulanabilir bir kanıt çıktısı üretmeden bir görevi "tamamlandı" olarak işaretleyemez.
4. **Bumblebee MCP Güvenliği:** Tehlikeli kabuk komutlarını (`rm -rf`, `curl | bash`), dizin geçiş açıklarını ve istem enjeksiyonlarını (Prompt Injection) engelleyen statik ve dinamik denetim motoru.
5. **Çoklu Çalışma Zamanı Adaptörleri:** **Hermes Main**, **Hermes Personal Desktop**, **Antigravity IDE**, **OpenAI Codex / Cursor** ve **Claude Code** için doğrudan dışa aktarım desteği.

---

## 2. v0.2.0 Sürüm Özellikleri

* **12 Uzman Ajan (100/100 Bot-Ready Puanı):**
  - `research-agent`, `seo-auditor`, `geo-auditor`, `ai-visibility-analyst`, `content-strategist`, `content-writer`, `fact-checker`, `code-reviewer`, `developer-agent`, `marketing-analyst`, `lead-researcher`, `project-manager`.
* **24 Standart Ajan Becerisi (SKILL.md):**
  - Ajan mühendisliği, kod inceleme, depo analizi, web taraması, belge analizi, SEO, GEO, arama görünürlüğü, sistematik hata ayıklama, Bumblebee MCP denetimi, otonom deney değerlendirmesi ve araştırma döngüsü.
* **MCP Ağ Geçidi ve Güvenlik Denetçisi:**
  - JSON Şeması doğrulaması ve güvenli yürütme sınırları.
* **Autoresearch Deney Defteri:**
  - Otomatik Keep/Revert kararları ile metrik optimizasyonu.
* **İkinci Beyin Bellek Köprüsü (`tm-second-brain`):**
  - YAML başlıklı yerel Markdown hafızası.

---

## 3. Kurulum ve Başlangıç

### PyPI Üzerinden Kurulum:
```bash
pip install molavi-agentic-os
```

### Kaynak Koddan Geliştirici Kurulumu:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### CLI ile Doğrulama ve Listeleme:
```bash
# Bot-Ready Doğrulaması (100/100 Puan)
molavi-agentic-os validate

# Ekosistem Bileşenlerini Listele
molavi-agentic-os list all

# Platformlara Dışa Aktar
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform hermes-desktop --agent developer-agent
molavi-agentic-os install --platform antigravity --agent content-writer
molavi-agentic-os install --platform codex --agent seo-auditor
```

---

## 4. Ekosistem Entegrasyonu

Bu sistem, tmolavi ekosistemindeki diğer açık kaynaklı araçlarla doğrudan entegredir:
- [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): Yerel Markdown ve Obsidian tabanlı kalıcı ajan hafızası.
- [`geo-scope`](https://github.com/tmolavi/geo-scope): Yapay zekâ cevap motorlarında görünürlük ve atıf benchmarkı.
- [`sage-audit`](https://github.com/tmolavi/sage-audit): Teknik SEO, AEO ve şema denetim motoru.
- [`siteprobe`](https://github.com/tmolavi/siteprobe): Otomatik web sitesi tarayıcısı ve kod düzeltici.
- [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence): Sıfır jeton maliyetli ağ tarayıcısı.
- [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): Sıfır entropili insani metin yazarlığı motoru.
- [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine): Otonom haber odası yayıncılığı ve trafik motoru.

---

## 5. Testler ve Doğrulama

```bash
pytest -v
python scripts/check_governance.py
```

---

## 6. Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Telif Hakkı (c) 2026 **Taghi Molavi**.
