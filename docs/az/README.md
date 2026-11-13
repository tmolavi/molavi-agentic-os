<div align="center">

# TM Molavi Agentic OS (Azərbaycan dilində Sənədlər)

### Avtonom Süni İntellekt Agentləri, Bacarıqlar, Çoxagentli Komandalar, Davamlı Yaddaş və MCP Alətləri üçün Açıq Mənbəli Əməliyyat Ekosistemi

[![PyPI Version](https://img.shields.io/pypi/v/molavi-agentic-os.svg?style=for-the-badge&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/molavi-agentic-os/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CI Status](https://img.shields.io/badge/CI-21%20Tests%20Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/tmolavi/molavi-agentic-os/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](../../LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Runtime%20Deps-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](../../pyproject.toml)

**Digər Dillər:**  
🌐 [English](../../docs/en/README.md) · [فارسی (Fars dili)](../../docs/fa/README.md) · [Türkçe (Türkiyə türkcəsi)](../../docs/tr/README.md) · [العربية (Ərəb dili)](../../docs/ar/README.md)

---

⭐ **Əgər TM Molavi Agentic OS sizin üçün faydalıdırsa, GitHub-da repozitoriyanı ulduzlamaqla (Star) açıq mənbəli ekosistemin inkişafına dəstək olun!**

---

</div>

## 1. Ümumi Baxış və Memarlıq Əsasları

**TM Molavi Agentic OS** avtonom süni intellekt agentləri, çoxagentli komandalar və Model Context Protocol (MCP) alətləri üçün hazırlanmış, modeldən asılı olmayan açıq mənbəli əməliyyat ekosistemidir.

Əsas üstünlüklər:
- **Sıfır Xarici Asılılıq:** Redis, Celery və ya Docker tələb etmədən təmiz Python 3.10+ standart kitabxanası üzərində işləyir.
- **Foreman Doğrulama Qapısı:** *"Təxmin etmək qadağandır"* prinsipi əsasında heç bir agent maddi sübut və artefakt təqdim etmədən tapşırığı tamamlanmış elan edə bilməz.
- **Kriptoqrafik HMAC İcazə Biletləri:** Həssas əməliyyatlar (kod icrası, e-poçt göndərilməsi, verilənlər bazası dəyişiklikləri) `L2_HUMAN_APPROVAL` səviyyəsində insan təsdiqinə bağlanır.
- **Prioritet Pulsuz Model Yönləndiricisi:** Yerli açıq çəkili modelləri (Ollama: Llama 3.2, Mistral) və pulsuz bulud qatlarını (Groq, Gemini Free Tier) $0.00 xərclə prioritetləşdirir.
- **Çoxplatformalı Uyğunluq:** Hermes Main, Hermes Personal Desktop, Antigravity IDE, Claude Code və OpenAI Codex üçün hazır adaptörlər təqdim edir.

---

## 2. 60 Saniyədə Sürətli Başlanğıc

```bash
# PyPI vasitəsilə rəsmi paketin quraşdırılması
pip install molavi-agentic-os

# CLI ilə Bot-Ready 100 ballıq yoxlama
molavi-agentic-os validate

# Bütün komponentlərin siyahısı
molavi-agentic-os list all
```

### Python Nümunəsi
```python
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact

registry = ToolRegistry()
registry.register(ToolDefinition(
    name="sayt_yoxla",
    description="Səhifə başlıqlarını yoxlayır.",
    parameters=[ToolParameter("url", "string", "Hədəf URL")],
    handler=lambda url: {"url": url, "status": 200, "headings": ["Giris", "Memarliq"]}
))

gateway = MCPGateway(registry=registry)
cavab = gateway.handle_call_tool("sayt_yoxla", {"url": "https://molavi.pro"})

gate = ForemanVerificationGate.verify(
    output={"url": "https://molavi.pro", "evidence": ["HTTP 200"]},
    expected_artifacts=[VerificationArtifact("url", "string", "https://molavi.pro")]
)
print("Təsdiqləndi:", gate.is_verified)
```

---

## 3. Ekosistem Əlaqələri

* [`tm-second-brain`](https://github.com/tmolavi/tm-second-brain): Markdown və Obsidian əsaslı lokal davamlı yaddaş.
* [`humanize-ai-copywriter`](https://github.com/tmolavi/humanize-ai-copywriter): İnsani və yüksək konversiyalı kopiraytinq mühərriki.
* [`molavi-web-intelligence`](https://github.com/tmolavi/molavi-web-intelligence): $0.00 xərclə veb məlumatlarının toplanması.
* [`geo-scope`](https://github.com/tmolavi/geo-scope): Süni intellekt axtarış sistemlərində görünürlüyün ölçülməsi.

---

<div align="center">
<sub>MIT Lisenziyası ilə yayımlanır — Müəllif hüququ (c) 2026 <a href="https://molavi.pro">Tağı Mövləvi</a></sub>
</div>
