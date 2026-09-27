# Skill: Site Build

## Purpose
Analiz edilen referanslardan ve efekt kütüphanesinden yararlanarak, görsel olarak aynı ligde ama özgün bir yeni nesil web sitesi / landing page inşa etmek.

## Serves Goals
- Benzer kalitede site üretmek

## Inputs
- `data/imports/BRIEF.md` (varsa) — proje adı, sektör, içerik, istenen his
- Teardown çıktıları ve `outputs/sites/patterns/`
- `knowledge/BRAND.md` — marka tonu ve görsel kimlik
- `MEMORY.md` — işe yarayan kompozisyonlar ve stack tercihleri

## Process
1. Brief'i oku; yoksa en güçlü referanstan yola çıkan kurgusal bir konsept belirle ve bunu çıktıda açıkça belirt.
2. Moodboard: 2-3 referans + kullanılacak 1-3 pattern seç; "referanstan ne alıyoruz / neyi farklı yapıyoruz" tablosu yaz.
3. Stack seç. Firma Modu'nda varsayılan: Next.js (veya Vite) + React + Tailwind + shadcn, çünkü 21st.dev bileşenleri bunu gerektirir. Keşif Modu'nda Vite + vanilla/React, GSAP + ScrollTrigger, Lenis veya Three.js/OGL da seçilebilir. Seçimi gerekçelendir.
   - Firma Modu'nda COMPONENT_SELECTION'da seçilen bileşenleri resmi kurulum komutuyla ekle, sonra renk, tipografi, metin ve animasyon hızını firmaya göre özelleştir.
4. Önce statik iskelet: semantik HTML, tipografi, grid, responsive kırılımlar.
5. Hareketli arka planı ve animasyonları katman katman ekle; her birine `prefers-reduced-motion` fallback'i yaz.
6. İçerik ve görseller: özgün, lisanslı (Unsplash/Pexels vb.) veya üretilmiş asset kullan; kaynaklarını `CREDITS.md`'ye yaz.
7. Lokal olarak çalıştır, masaüstü + mobil ekran görüntüsü al.
8. QUALITY_AUDIT'e devret.

## Outputs
- `outputs/sites/YYYY-MM-DD_[proje-adi]/` — kaynak kod, `README.md` (nasıl çalıştırılır), `CREDITS.md`, ekran görüntüleri

## Quality Bar
- İlk ekranda (hero) belirgin, akıcı (60fps hedefi) bir hareketli öğe var.
- Referans sitesiyle yan yana konduğunda "aynı ligde" ama açıkça farklı bir site.
- Mobilde bozulmayan, JS kapalıyken bile okunabilir içerik.
- Tüm asset'lerin lisansı `CREDITS.md`'de belgelenmiş.

## Tools
- Node.js, Next.js/Vite, Tailwind, shadcn CLI (21st.dev bileşenleri için `API_KEY_21ST`), GSAP, Three.js/OGL, Lenis; `frontend-design` skill (tasarım planı, elle yazılan bölümler, öz eleştiri); Playwright (ekran görüntüsü)

## Integration
- Çıktı → QUALITY_AUDIT
- Deploy isteniyorsa → insana handoff (onay olmadan yayın yok)
