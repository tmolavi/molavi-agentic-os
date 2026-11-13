<div align="center">

# TM Molavi Agentic OS (Türkçe Dokümantasyon)

### Otonom Yapay Zekâ Ajanları, Beceriler, Çoklu Ajan Takımları, Kalıcı Bellek ve MCP Araçları için Açık Kaynaklı Modüler İşletim Ekosistemi

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?style=for-the-badge&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CI Status](https://img.shields.io/badge/CI-21%20Tests%20Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](../../LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](../../pyproject.toml)

**Diğer Diller:**  
🌐 [English](../../docs/en/README.md) · [فارسی (Farsça)](../../docs/fa/README.md) · [Azərbaycan dili (Azerbaycanca)](../../docs/az/README.md) · [العربية (Arapça)](../../docs/ar/README.md)

---

⭐ **TM Molavi Agentic OS projeleriniz için faydalıysa, lütfen GitHub'da depoyu yıldızlayarak (Star) açık kaynaklı ekosistemin büyümesine destek olun!**

---

</div>

## 1. Genel Bakış ve Mimari Felsefe

**TM Molavi Agentic OS**, üretim ortamlarında çalışan yapay zekâ ajanları ve çoklu ajan iş akışları için geliştirilmiş, modelden bağımsız açık kaynaklı bir işletim ekosistemidir.

CrewAI, AutoGPT ve LangGraph gibi ağır çerçevelerin aksine:
- **Sıfır Dış Çalışma Zamanı Bağımlılığı:** Harici Redis, Celery veya Docker gerektirmeden saf Python 3.10+ standart kütüphanesi üzerinde çalışır.
- **Foreman Doğrulama Kapısı:** *"Tahmin yürütmek yasaktır"* altın kuralını uygular. Ajanlar somut fiziksel kanıtlar (HTTP durum kodları, dosya çıktıları, test sonuçları) sunmadan görevleri tamamlandı olarak işaretleyemez.
- **Kriptografik HMAC Onay Biletleri:** Hassas işlemler (kod çalıştırma, e-posta gönderme, veritabanı yazma) `L2_HUMAN_APPROVAL` seviyesinde insan onayına bağlanır.
- **Öncelikli Ücretsiz Model Yönlendiricisi (Free-First Router):** Yerel açık kaynaklı modelleri (Ollama: Llama 3.2, Mistral) ve ücretsiz bulut katmanlarını (Groq, Gemini Free Tier) 0,00 $ marjinal maliyetle önceliklendirir.
- **Çoklu Çalışma Zamanı Desteği:** Hermes Main, Hermes Personal Desktop, Antigravity IDE, Claude Code ve OpenAI Codex için yerel dışa aktarım adaptörleri sağlar.

---

## 2. 60 Saniyede Hızlı Başlangıç

### PyPI veya Kaynak Koddan Kurulum
```bash
# PyPI üzerinden kararlı paketi kurun
pip install molavi-agentic-os

# Veya kaynak kodu klonlayın
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .
```

### Örnek Çalıştırma ($0.00 Maliyet)
```python
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

registry = ToolRegistry()
registry.register(ToolDefinition(
    name="sayfa_incele",
    description="Web sayfası başlıklarını inceler.",
    parameters=[ToolParameter("url", "string", "Hedef web adresi")],
    handler=lambda url: {"url": url, "durum": 200, "basliklar": ["Genel Bakis", "Mimari"]}
))

gateway = MCPGateway(registry=registry)
sonuc = gateway.handle_call_tool("sayfa_incele", {"url": "https://molavi.pro"})

# Foreman Doğrulama Kapısı
ajan_ciktisi = {"url": "https://molavi.pro", "evidence": ["HTTP 200 basarili"]}
kapı = ForemanVerificationGate.verify(
    output=ajan_ciktisi,
    expected_artifacts=[VerificationArtifact("url", "string", "https://molavi.pro")]
)
print("Dogrulandi mi?:", kapı.is_verified)
```

### CLI Komutları
```bash
# Bot-Ready 100 puanlık uygunluk doğrulaması
molavi-agentic-os validate

# Tüm ajanları, becerileri ve takımları listeleme
molavi-agentic-os list all

# Platform adaptörüyle dışa aktarma (Hermes, Antigravity, Codex)
molavi-agentic-os install --platform hermes --agent research-agent
molavi-agentic-os install --platform antigravity --agent developer-agent
```

---

## 3. Ekosistem Bileşenleri

* **12 Uzman Ajan:** `research-agent`, `fact-checker`, `seo-auditor`, `geo-auditor`, `ai-visibility-analyst`, `developer-agent`, `code-reviewer`, `content-strategist`, `content-writer`, `marketing-analyst`, `lead-researcher`, `project-manager`.
* **24 Standart Beceri:** Ajan mühendisliği, depo analizi, belge zekâsı, SEO/GEO denetimi, Bumblebee MCP güvenlik taraması, otonom araştırma döngüsü, ikinci beyin bellek adaptörü.
* **5 Çoklu Ajan Takımı:** SEO & GEO Araştırma Takımı, Yapay Zekâ Görünürlük Takımı, Yazılım Geliştirme Takımı, İçerik Üretim Takımı, B2B Müşteri Adayı Takımı.

---

## 4. TM Ekosistem Entegrasyonu

* [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): Yerel Markdown/Obsidian kalıcı bellek entegrasyonu.
* [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): Sıfır entropili insani metin yazarlığı motoru.
* [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence): Sıfır maliyetli web tarama ve SEO altyapısı.
* [`geo-scope`](https://github.com/tmolavi/geo-scope): Üretken yapay zekâ arama motorlarında görünürlük ölçümü.

---

<div align="center">
<sub>MIT Lisansı ile lisanslanmıştır — Telif Hakkı (c) 2026 <a href="https://molavi.pro">Taghi Molavi</a></sub>
</div>
