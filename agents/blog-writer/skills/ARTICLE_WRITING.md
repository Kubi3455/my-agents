# Skill: Article Writing

## Purpose
Seçilen konu için sitenin sesinde, Gutenberg blok formatında, teknik olarak doğrulanmış İngilizce yazıyı üretmek.

## Serves Goals
- Ses tutarlılığı
- Düzenli yayın

## Inputs
- TOPIC_SELECTION çıktısı (konu, odak kelime, ikincil kelimeler, niyet)
- `data/STYLE_GUIDE.md` (**tamamını oku**)
- `MEMORY.md` → "Ses" (insan düzeltmeleri, STYLE_GUIDE'dan önceliklidir)
- Referans: envanterdeki en yakın 2 yazının `content.rendered` alanı (ses kalibrasyonu)
- Resmî dokümantasyon (araştırma)

## Process
1. **Araştır:** Konunun resmî dokümanlarını ve ilk sayfadaki 3–5 sonucu oku. Onların **atladığı** şeyi bul (kenar durum, gerçek hata, performans notu). Yazının farkı bu olacak.
2. **Doğrula:** Kullanılacak her API/parametre/sürüm bilgisini resmî kaynaktan teyit et; kaynak URL'lerini not al (SEO_LINKING dış link olarak kullanır).
3. **Taslak iskelet (outline):** H2/H3 listesi. STYLE_GUIDE yapısına uy: açılış (3 paragraf) → problem → nasıl çalışır → uygulama (kod) → karşılaştırma tablosu → sınırlar/pros-cons → common pitfalls → conclusion → FAQ.
4. **Yaz:**
   - Açılış: yaşanmış, spesifik, hafif kendini tiye alan bir geliştirici anısı (uydurma rakam/şirket adı yok; genel ama somut bir durum)
   - Odak kelime: ilk 100 kelimede, en az bir H2'de, conclusion'da; doğal yoğunluk (~%0.8–1.2), zorlama yok
   - Paragraf ≤ 4 cümle; her 250–350 kelimede bir görsel, kod, tablo, liste veya alıntı ile ritim kır
   - Kod: tam import'lu, çalıştırılabilir, kısa; yorum satırları açıklayıcı
   - Görsel yerleri için yer tutucu bırak: `{{IMG:inline-1}}`, `{{IMG:inline-2}}`, `{{IMG:inline-3}}` (her biri ayrı satırda, blok dışında)
   - İç link yerleri için şimdilik düz metin bırak; SEO_LINKING ekler
5. **Gutenberg'e çevir:** STYLE_GUIDE'daki blok yorumlarıyla sar.
6. **İnsan Sesi geçişi (ayrı bir revizyon turu, atlanmaz):** STYLE_GUIDE → "İnsan Sesi" bölümünü baştan oku. Metni o gözle **yeniden yaz**: yasak kalıpları ve kelimeleri ayıkla, cümle ve paragraf ritmini boz, görüş ve uzmanlık sinyallerini ekle, conclusion'ı tavsiyeye çevir. Sonra 8 maddelik İnsan Sesi Testi'ni uygula; skoru REPORT.md'ye yaz.
7. **Teknik öz-denetim:** Kod çalışır mı? Her iddianın kaynağı var mı?

## Outputs
- `outputs/YYYY-MM-DD_[slug]/content.html` (Gutenberg bloklu, yer tutuculu)
- `outputs/YYYY-MM-DD_[slug]/sources.md` (doğrulama kaynakları)

## Quality Bar
- 1.800–2.800 kelime
- STYLE_GUIDE "Kaçınılacaklar" ve "Yasak kalıplar" listelerinden sıfır ifade
- İnsan Sesi Testi 8/8 (değilse WP_PUBLISH'e geçilmez)
- Her teknik iddianın `sources.md`'de kaynağı var
- En az 1 tablo, 1 FAQ bölümü (3–5 soru); teknik konuda en az 2 kod bloğu
- Rakip bir yazıdan 8+ kelimelik aynı dizi yok

## Tools
- `python scripts/voice_check.py outputs/.../content.html`: yasak kalıp, em dash ve cümle ritmi kontrolü. PASS olmadan İnsan Sesi Testi tamamlanmış sayılmaz
- WebSearch / WebFetch
- Opsiyonel: `searchfit-seo:content-brief` skill'i (brief zenginleştirme)

## Integration
- content.html → SEO_LINKING (link + meta) → IMAGE_GENERATION (yer tutucular için prompt) → WP_PUBLISH
