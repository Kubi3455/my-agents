# Skill: Quality Audit

## Purpose
Üretilen sitenin görsel etkisini korurken performans, erişilebilirlik ve özgünlük eşiklerini geçtiğini doğrulamak.

## Serves Goals
- Kaliteyi korumak

## Inputs
- `outputs/sites/YYYY-MM-DD_[proje-adi]/`
- İlgili referans siteler (karşılaştırma için)

## Process
1. Lighthouse (mobil + masaüstü) çalıştır: Performance, Accessibility, Best Practices.
2. Core Web Vitals'ı not et: LCP, CLS, INP.
3. `prefers-reduced-motion: reduce` emülasyonu ile tüm animasyonların durduğunu/sadeleştiğini kontrol et.
4. Düşük güçlü cihaz simülasyonu (CPU 4x throttle) ile animasyonların takılıp takılmadığını kontrol et.
5. Klavye navigasyonu, kontrast, alt metinleri kontrol et.
6. Özgünlük ve lisans kontrolü: başka web sitelerinden kopyalanmış kod, asset veya marka öğesi olmadığını doğrula. Örnek kaynağından gelen her bileşenin `CREDITS.md`'de lisansıyla yer aldığını ve firmaya göre özelleştirildiğini kontrol et.
7. Chatbot: WhatsApp (`wa.me`), yol tarifi (Google Maps) ve arama (`tel:`) linklerinin doğru numara/konumu açtığını, widget'ın klavye ile açılıp kapandığını (Esc) ve performansı 3 puandan fazla düşürmediğini kontrol et.
8. Eşik altı her madde için düzeltme öner veya SITE_BUILD'e geri gönder.

## Outputs
- `outputs/YYYY-MM-DD_web-builder_audit-[proje].md` — skor tablosu, ekran görüntüleri, düzeltme listesi, GEÇTİ/KALDI kararı

## Quality Bar
- Perf ≥85, A11y ≥90 (mobil), CLS <0.1.
- Reduced-motion desteği tam.
- Özgünlük kontrolü açıkça "GEÇTİ" olarak işaretli.

## Tools
- Lighthouse / Chrome DevTools MCP, Playwright

## Integration
- GEÇTİ → insana onay için sunulur, sonuçlar `MEMORY.md`'ye (hangi efekt ne kadar performans maliyetli)
- KALDI → SITE_BUILD'e düzeltme listesiyle geri döner
