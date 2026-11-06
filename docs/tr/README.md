# TM AI Agent Toolkit (Türkçe Rehber)

<p align="center">
  <strong>Molavi Agentic OS: Ajanlar, Beceriler, Çoklu Ajan Ekipleri ve İş Akışları İçin Açık Ekosistem.</strong><br>
  <em>Daha Akıllı Ajanlar Oluşturun. Daha İyi Ekipler Kurun. Gerçek İşleri Otomatikleştirin.</em>
</p>

---

## 🏛️ Yönetişim ve Model Şeffaflığı
* **Kanonik Yönetişim Standardı:** [`TM-OPEN-SOURCE-STANDARD.md`](../../TM-OPEN-SOURCE-STANDARD.md)
* **Model Gereksinimleri ve Ücretsiz Alternatifler:** [`MODEL-REQUIREMENTS.md`](../../MODEL-REQUIREMENTS.md)
* **Mevcut 24 Deponun Envanteri:** [`docs/repository-governance/EXISTING-REPOSITORIES.md`](../repository-governance/EXISTING-REPOSITORIES.md)

---

## 1. Genel Bakış

**TM AI Agent Toolkit** (Molavi Agentic OS), **Taqi Molavi** (Yapay Zeka Sistemleri Mimarı, SEO & GEO Stratejisti) tarafından TM Açık Kaynak ekosistemi altında geliştirilen açık kaynaklı, modüler ve modelden bağımsız bir yapay zeka ajanı işletim sistemidir.

Sıfırdan modern yapay zeka sistemleri mimarisi standartlarına uygun olarak tasarlanmıştır.

### Temel İlkeler:
1. **Önce Ücretsiz Model Stratejisi (Free-First):** Yerel açık kaynaklı modeller (Ollama) ve ücretsiz bulut katmanları (Groq, Gemini Free Tier) önceliklidir.
2. **Permission-Slip Güvenlik Modeli:** E-posta gönderme, kod dağıtma veya finansal işlemler gibi hassas eylemler insan onayı (`L2_HUMAN_APPROVAL`) gerektirir.
3. **Foreman Doğrulama Kapısı:** *"Tahmin yürütmek yasaktır"* kuralı gereğince, somut kanıt sunulmadan hiçbir görev tamamlandı sayılamaz.

---

## 2. Kurulum ve Çalıştırma

```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
pip install -e .

# Tüm ajanların Bot-Ready skorunu doğrula
molavi-agentic-os validate

# Ekosistem bileşenlerini listele
molavi-agentic-os list all
```

---

## 3. Marka Konumlandırması

* **Proje Sahibi:** Taqi Molavi
* **Uzmanlık:** Yapay Zeka Mimarisi | SEO & GEO Stratejisi
* **Felsefe:** Görünür Ol. Daha İyi Sat. Otorite Kur. (Be Visible. Sell Better. Build Authority.)
* **Web Sitesi:** [molavi.pro](https://molavi.pro)
