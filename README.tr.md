<div align="center">

# TM Molavi Agentic OS

### Otonom Yapay Zekâ Ajanları, Beceriler, Çoklu Ajan Ekipleri, İş Akışları ve Yerel Bellek için Açık Kaynaklı, Modüler İşletim Ekosistemi

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?color=blue&style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Stdlib)-success?style=for-the-badge)](pyproject.toml)
[![Bot-Ready Score](https://img.shields.io/badge/Bot--Ready-100%2F100-purple?style=for-the-badge)](https://github.com/tmolavi/molavi-agentic-os)
[![Marginal Cost](https://img.shields.io/badge/Cost-%240.00%20(Free--First)-brightgreen?style=for-the-badge)](MODEL-REQUIREMENTS.md)

**Mimar ve Geliştirici: [Taghi Molavi (تقی مولوی)](https://molavi.pro)** · *Yapay Zekâ Sistemleri Mimarı ve Üretken Arama Görünürlüğü (GEO) Araştırmacısı*  
*یاد بگیر، یاد بده و اثری ماندگار خلق کن — Öğren. Paylaş. Kalıcı bir etki yarat.*

```bash
pip install molavi-agentic-os
```

[English](README.md) · [فارسی (Persian)](README.fa.md) · [Türkçe (Turkish)](README.tr.md) · [Azərbaycan dili](README.az.md) · [العربية (Arabic)](README.ar.md)

<br/>

> ⭐ **Bu proje sizi ağır sunucu altyapılarından ve hayali ajan çıktılarından kurtardıysa, lütfen GitHub'da depoya bir yıldız (Star) vererek ekosistemi destekleyin!**

</div>

---

## ⚡ Üretim Ortamında Ajan Sistemlerinin Temel Sorunları

Mevcut yapay zekâ ajan kütüphanelerinin çoğu kurumsal üretim ortamlarında 3 kritik darboğaza takılır:

1. **Aşırı Altyapı Bağımlılığı (Infrastructure Sprawl):** Basit bir 3 adımlı iş akışı için bile arka planda Redis, Celery, Docker veya pahalı ticari API modelleri zorunlu kılınır.
2. **Hayali "Tamamlandı" Yanılsaması (Hallucinated Done States):** Ajanlar, gerçekte hiçbir fiziksel test veya çıktı üretmedikleri halde görevleri "tamamlandı" olarak raporlar.
3. **Güvenlik Sınırlarının Olmayışı:** Kritik terminal komutları (`rm -rf`, kontrolsüz kabuk komutları) kriptografik insan onayı ve MCP güvenlik denetimi olmaksızın çalıştırılır.

**TM Molavi Agentic OS**, bağımlılık yükünü sıfıra indiren saf Python mimarisiyle bu sorunları çözer: Redis veya Celery gerektirmez, yerel açık kaynaklı modelleri (Ollama: Llama 3.2, Mistral) ve ücretsiz bulut katmanlarını (Groq, Gemini Free Tier) önceliklendirerek **0.00$** marjinal maliyet sunar, Foreman doğrulama kapısı ("tahmin yasaktır") ile somut artefakt kanıtı arar ve hassas işlemleri HMAC imzalı izin biletleriyle insan onayına bağlar.

---

## 📊 Karşılaştırma Matrisi: Mühendisler Neden Molavi Agentic OS'i Seçiyor?

| Özellik / Mimari Boyut | TM Molavi Agentic OS | CrewAI | LangGraph | AutoGPT |
|---|---|---|---|---|
| **Çalışma Zamanı Bağımlılıkları** | **Sıfır (Yalnızca Python Standart Kütüphanesi)** | Ağır (Pydantic, Chroma vb.) | Ağır (LangChain ekosistemi) | Ağır (Docker, Redis vb.) |
| **Model Maliyet Stratejisi** | **Önce Ücretsiz (0.00$ Ollama/Groq/Gemini)** | Ücretli bulut API'leri | Ücretli bulut API'leri | Varsayılan OpenAI |
| **Foreman Doğrulama Kapısı** | **Katı Somut Artefakt Denetimi ("No-Guessing")** | Ajanın kendi beyanı | Manuel kullanıcı kontrolleri | Kontrolsüz |
| **İnsan Onay Mekanizması** | **HMAC İmzalı `ApprovalTicket` (L0-L3)** | Basit geri çağırma | Interrupt deseni | CLI onay metni |
| **Araç Protokolü** | **Yerel MCP Ağ Geçidi + Bumblebee Güvenliği** | Özel araç sarıcıları | LangChain Araçları | Özel eklentiler |
| **Bellek Mimarisi** | **SQLite + `tm-second-brain` (Markdown/Obsidian)** | Vektör veritabanı şart | Checkpointer State | Vektör deposu |
| **Platform Adaptörleri** | **Hermes Main, Hermes Desktop, Antigravity, Codex** | Özel CLI | LangGraph Cloud | Yalnızca web arayüzü |
| **Otonom Optimizasyon** | **Karpathy Autoresearch Keep/Revert Döngüsü** | Yok | Ücretli LangSmith | Yok |

---

## 🏛️ Sistem Mimarisi

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        TM MOLAVI AGENTIC OS                            │
├────────────────────────────────────────────────────────────────────────┤
│  Platform ve Çalışma Zamanı Adaptörleri:                               │
│  [Hermes Main]  [Hermes Desktop]  [Antigravity IDE]  [Codex / Cursor]  │
├────────────────────────────────────────────────────────────────────────┤
│  Çoklu Ajan Ekipleri ve Üretim İş Akışları:                            │
│  • SEO & GEO Araştırma Ekibi       • Otonom Araştırma Döngüsü          │
│  • Yapay Zekâ Görünürlük Ekibi     • Çoklu Ajan Devir Hattı            │
│  • Katkısız İçerik Üretim Ekibi    • Hata Yönetimi ve Otomatik Geri Çekilme │
│  • B2B Müşteri Adayı & İletişim    • Sistematik Hata Ayıklama ve Yama  │
├────────────────────────────────────────────────────────────────────────┤
│  12 Uzman Ajan (100/100 Bot-Ready Skoru):                              │
│  [Research Agent] [SEO Auditor] [GEO Auditor] [AI Visibility Analyst]  │
│  [Content Strategist] [Content Writer] [Fact Checker] [Code Reviewer]  │
│  [Developer Agent] [Marketing Analyst] [Lead Researcher] [PM Agent]    │
├────────────────────────────────────────────────────────────────────────┤
│  24 Standart Ajan Becerisi (SKILL.md) ve Araç Kataloğu:                │
│  • Ajan Mühendisliği ve Sözleşmeler • Bumblebee MCP Güvenlik Denetimi  │
│  • Derin Depo Analizi               • Nicel Autoresearch Metrikleri    │
│  • Belge Zekâsı ve Şema Çıkarımı    • Sıfır Jeton Maliyetli Ağ Taraması│
│  • GEO ve Arama Görünürlüğü Analizi • İkinci Beyin Obsidian Belleği    │
├────────────────────────────────────────────────────────────────────────┤
│  Çekirdek Orkestrasyon ve Güvenlik Alt Sistemleri:                     │
│  • HMAC İmzalı İnsan Onay Koruyucusu (L2_HUMAN_APPROVAL)               │
│  • Foreman 'Tahmin Yasaktır' Artefakt Doğrulama Kapısı                 │
│  • Sıfır Bağımlılıklı Thread-Safe TaskQueue ve DAG Koşucusu            │
│  • Ücretsiz Model Yönlendiricisi (Ollama Llama-3.2, Groq, Gemini)      │
│  • Değişiklik Geçmişini Saklayan Markdown İkinci Beyin Belleği         │
│  • İstek Enjeksiyonunu Engelleyen Standart MCP Ağ Geçidi               │
│  • Karpathy'den İlham Alan Keep/Revert Kararlı Deney Defteri           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 60 Saniyede Başlangıç

### 1. PyPI Üzerinden Kurulum
```bash
pip install molavi-agentic-os
```

Veya geliştirme için yerel repoyu klonlayın:
```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e ".[dev]"
```

### 2. Bot-Ready Doğrulaması (100/100 Puan)
```bash
molavi-agentic-os validate
```
Çıktı:
```text
Running Bot-Ready Validation across '.'...
  [PASS] research-agent (Score: 100/100)
  [PASS] fact-checker (Score: 100/100)
  [PASS] seo-auditor (Score: 100/100)
  [PASS] geo-auditor (Score: 100/100)
  ...
Validation Summary: 12/12 Passed Bot-Ready Score threshold (>=70/100)
```

### 3. Uçtan Uca İş Akışını Çalıştırın
```bash
python examples/end_to_end_agent_workflow.py
```

---

## 💡 Çalıştırılabilir Kod Örnekleri

### 1. Sıfır Maliyetli Yerel ve Bulut Model Yönlendirmesi ($0.00)
```python
from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider

router = ModelRouter()
local_model = MockProvider(fixed_response="Sistem mimarisi tamamen çevrimdışı doğrulandı.")
router.register_provider("ollama-llama-3.2", local_model, ModelTier.FREE_LOCAL)

response = router.route_and_generate(
    prompt="Güvenlik mimarisini ve ajan sınırlarını denetle",
    preferred_tier=ModelTier.FREE_LOCAL
)
print(f"Kullanılan Model: {response.model_name} | Maliyet: ${response.estimated_cost_usd:.2f}")
```

### 2. Foreman Doğrulama Kapısı ("Tahmin Yasaktır")
```python
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

agent_output = {
    "status": "completed",
    "target_url": "https://molavi.pro/research",
    "evidence": ["HTTP 200 OK", "Başlıklar başarıyla çıkarıldı"]
}

artifacts = [
    VerificationArtifact("url_crawled", "string", agent_output["target_url"]),
    VerificationArtifact("evidence_ledger", "list", agent_output["evidence"])
]

result = ForemanVerificationGate.verify(agent_output, artifacts)
if result.is_verified:
    print(f"✅ Foreman Onayı Verildi: {result.verified_artifacts}")
else:
    print(f"❌ Reddedildi: {result.failure_reason}")
```

### 3. HMAC İmzalı İnsan Onay Mekanizması
```python
from molavi_agentic_os.security import ApprovalManager

mgr = ApprovalManager(secret_key="your-secure-secret-key-min-32-chars")
ticket = mgr.create_ticket(
    action="deploy_production_code",
    reason="İşletim sistemi v0.2.0 resmi sürüm dağıtımı",
    target="prod-cluster-01",
    impact="Üretim kümesinde canlı kod güncellemesi",
    risk="HIGH"
)
print(f"Bilet ID: {ticket.ticket_id} | İnsan Onayı Gerekli mi: {ticket.requires_human_approval}")
```

---

## 🌐 Çalışma Zamanı Adaptörleri

```bash
# Hermes Main (Ana Ajan Ortamı) için dışa aktar
molavi-agentic-os install --platform hermes --agent research-agent

# Hermes Desktop (Kişisel Dosyalar ve İzolasyon) için dışa aktar
molavi-agentic-os install --platform hermes-desktop --agent developer-agent

# Antigravity IDE için dışa aktar
molavi-agentic-os install --platform antigravity --agent content-writer

# OpenAI Codex ve Cursor için dışa aktar
molavi-agentic-os install --platform codex --agent seo-auditor

# Claude Code (CLAUDE.md) için dışa aktar
molavi-agentic-os install --platform claude-code --agent project-manager
```

---

## 🔗 Ekosistem ve Bağlantılı GitHub Depoları

| Depo | Uzmanlık Alanı | TM Agentic OS ile Entegrasyonu |
|---|---|---|
| [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain) | Ajanlar için Yerel Markdown ve Obsidian Bellek Altyapısı | Oturumlar arası kalıcı hafıza ve denetim günlüğü katmanı. |
| [`geo-scope`](https://github.com/tmolavi/geo-scope) | Yapay Zekâ Cevap Motorlarında (Perplexity, ChatGPT) Görünürlük Çerçevesi | `geo-auditor` için gerçek atıf verisi sağlar. |
| [`sage-audit`](https://github.com/tmolavi/sage-audit) | 3 Sütunlu Teknik SEO, AEO ve Şema Denetim Motoru | `seo-auditor` içine teknik denetim rutinlerini besler. |
| [`siteprobe`](https://github.com/tmolavi/siteprobe) | Otonom Web Sitesi Tarayıcısı ve Kod/Yapılandırma Onarıcısı | Teşhis raporlarına göre otomatik düzeltme yamalarını uygular. |
| [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence) | Sıfır Jeton Maliyetli Deterministik Web Tarayıcısı | Ajanların internetten bilgi toplaması için ücretsiz altyapı. |
| [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter) | Sıfır Entropili İnsani Metin Yazarlığı ve Slop Temizleme | `unslop-humanizer` ve içerik yazarının çekirdek motoru. |
| [`mcp-geo-server`](https://github.com/tmolavi/mcp-geo-server) | GEO ve Yapay Zekâ Görünürlüğü için FastMCP Sunucusu | Ajanlar için standart MCP araç uç noktaları sunar. |
| [`news-traffic-engine`](https://github.com/tmolavi/news-traffic-engine) | Otonom Haber Odası Yayıncılığı ve Google News Trafik Motoru | Medya otomasyonu için içerik ekibine bağlanır. |
| [`scholar-provenance`](https://github.com/tmolavi/scholar-provenance) | Akademik Kanıt Defterleri ve Doğrulanabilir Makaleler | `fact-checker` için doğrulanabilir atıf şemaları sağlar. |
| [`tmolavi`](https://github.com/tmolavi/tmolavi) | Taghi Molavi Resmi GitHub Profil Deposu | Tüm ekosistem mimarisinin merkez tanıtım üssü. |

---

## 🛡️ Açık Kaynak Referans Projeler ve Lisans Uyumluluğu

Bu proje, açık kaynak topluluğuna derin bir saygıyla ve 6 öncü projenin ilkelerinden bağımsız olarak temiz oda (clean-room) yaklaşımıyla geliştirilmiştir:
1. **Andrej Karpathy — [Autoresearch](https://github.com/karpathy/autoresearch)** (MIT)
2. **Andrej Karpathy — [Nanochat](https://github.com/karpathy/nanochat)** (MIT)
3. **Sebastian Raschka — [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)** (Apache 2.0)
4. **Forrest Chang — [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills)** (MIT)
5. **ComposioHQ — [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** (Apache 2.0)
6. **Perplexity AI — [Bumblebee](https://github.com/perplexityai/bumblebee)** (Apache 2.0)

Ayrıntılı yasal analizler için [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md) ve [`SOURCES.md`](SOURCES.md) dosyalarını inceleyebilirsiniz.

---

## ❓ Sıkça Sorulan Sorular (SSS / AEO)

<details>
<summary><strong>S: TM Molavi Agentic OS çalıştırmak için Docker, Redis veya Celery şart mı?</strong></summary>

**Hayır.** Sistem tamamen standart Python kütüphaneleriyle (Thread-Safe TaskQueue ve DAG bağımlılık çözücüsü) yazılmıştır. Harici servisler çalıştırmadan doğrudan dizüstü bilgisayarınızda çoklu ajan sürülerini koşturabilirsiniz.
</details>

<details>
<summary><strong>S: Önce Ücretsiz Model (Free-First) stratejisi nasıl çalışır?</strong></summary>

Yönlendirici varsayılan olarak yerel Ollama modellerini veya ücretsiz yüksek hızlı bulut katmanlarını (Groq ve Google Gemini Free Tier) kullanır. Ücretli modeller yalnızca özel bir onay verildiğinde devreye girer.
</details>

<details>
<summary><strong>S: Foreman Doğrulama Kapısı hayal görmeyi (hallucination) nasıl engeller?</strong></summary>

Ajanın "görev bitti" beyanını dikkate almaz. Fiziksel dosya yolları, HTTP durum kodları, JSON şema eşleşmesi ve çıktıların doluluğu gibi somut kanıtları denetler. Kanıt yoksa görev onaylanmaz.
</details>

---

## 📈 Yıldız Geçmişi (Star History)

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=tmolavi/molavi-agentic-os&type=Date)](https://star-history.com/#tmolavi/molavi-agentic-os&Date)

**⭐ Bu projeyi beğendiniz mi? GitHub'da depoya bir yıldız vererek ekosistemi büyütebilirsiniz!**

</div>

---

## 📜 Lisans ve Yönetişim

**MIT Lisansı** altında yayımlanmıştır. Telif hakkı (c) 2026 **Taghi Molavi**.  
[`TM-OPEN-SOURCE-STANDARD.md`](TM-OPEN-SOURCE-STANDARD.md) standartlarına %100 uygundur.
