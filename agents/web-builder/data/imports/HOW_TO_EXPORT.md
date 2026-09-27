# Web Builder — Veri Bırakma Rehberi

Agent'a bu klasöre dosya bırakarak yön verebilirsin. Hepsi opsiyonel.

| Dosya | Ne içerir | Agent ne yapar |
|-------|-----------|----------------|
| `FIRMA_SORU_FORMU.md` | Firmaya gönderilecek hazır soru listesi (iletişim + SSS) | Gelen cevaplar sohbete yapıştırılınca firma dosyasına ve chatbot SSS'sine işlenir |
| `ORNEK_KAYNAGI.md` | Örnek sitelerin bulunduğu galeri sitesinin URL'si (tüm projelerde varsayılan kaynak) | Firma Modu'nda örnekleri **sadece** buradan seçer |
| `firmalar/[firma-adi].md` | Firma bilgileri (aşağıdaki şablon) | **Firma Modu**: galeriden firmaya en uygun tek örneği seçer ve firmaya uyarlar (tek site) |
| `REFERENCES.md` | Beğendiğin site URL'leri (satır başına bir URL + kısa not) | INSPIRATION_HUNT bunları öncelikle puanlar |
| `BRIEF.md` | Proje adı, sektör, sayfalar, içerik, istenen his, referans URL'ler | SITE_BUILD bu brief'e göre site yapar |
| `FEEDBACK.md` | Üretilen sitelere yorumların (beğendin / beğenmedin, neden) | Haftalık review'da MEMORY.md'ye işlenir |
| `lighthouse/*.json` | Dışarıda çalıştırdığın Lighthouse raporları | QUALITY_AUDIT karşılaştırma için kullanır |

## BRIEF.md örneği
```
Proje: kahve-dukkani
Sektör: Butik kahve
His: Sıcak, premium, yavaş akan hareket
Sayfalar: Tek sayfa landing (hero, menü, hikaye, iletişim)
Referanslar: https://..., https://...
Olmazsa olmaz: Hero'da hareketli arka plan
```

## ORNEK_KAYNAGI.md örneği
```
Galeri: https://ornek-galeri-sitesi.com
Not: Kategori/etiket filtreleri varsa agent konsepte göre bunları kullanır.
```

## Firma dosyası şablonu (`firmalar/[firma-adi].md`)
Dosya adı küçük harf ve tire ile yazılır, ör. `firmalar/yildiz-mimarlik.md`. Aynı anda sadece bir firma `Durum: aktif` olmalı.

```
Durum: aktif            # aktif | beklemede | onay-bekliyor | tamamlandı
Firma adı:
Sektör:
Ne yapıyor (1-2 cümle):
Hedef kitle:
Marka tonu / istenen his:   # ör. premium, sakin, cesur, eğlenceli
Renkler (varsa hex):
Logo / görseller:           # dosya yolu veya "yok"
Slogan:
Hizmetler / ürünler:
Sayfalar:                   # ör. tek sayfa landing / anasayfa + hakkımızda + iletişim
Telefon:
WhatsApp:                   # ülke koduyla, ör. 905321234567 (boşsa telefon numarası kullanılır)
E-posta:
Adres:
Harita konumu (opsiyonel):  # Google Maps linki veya enlem,boylam; boşsa adres kullanılır
Çalışma saatleri:
SSS (opsiyonel):            # "Soru? - Cevap" satırları; boşsa agent bilinen bilgilerden türetir
Chatbot (opsiyonel):        # kural-tabanlı (varsayılan) | yapay-zeka | yok
Rakipler / beğendiği siteler (opsiyonel):
Konsept (opsiyonel):        # boşsa agent kendisi belirler
Örnek kaynağı (opsiyonel):  # boşsa ORNEK_KAYNAGI.md kullanılır; doluysa sadece bu proje için geçerli
Kaçınılacaklar (opsiyonel):
```
