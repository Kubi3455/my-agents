# Skill: Design Teardown

## Purpose
Seçilen üst düzey bir sitenin görsel etkisini hangi tekniklerle yarattığını çözümleyip, yeniden kullanılabilir bir efekt/pattern olarak kütüphaneye eklemek.

## Serves Goals
- Teknikleri öğrenmek

## Inputs
- INSPIRATION_HUNT çıktısında işaretlenmiş siteler
- `MEMORY.md` — kütüphanede zaten olan pattern'ler (tekrar etmemek için)

## Process
1. Siteyi tarayıcıda aç; masaüstü ve mobil görünümde kaydır, etkileşimleri gözlemle.
2. DevTools ile kullanılan kütüphaneleri tespit et (Network/Sources: three.js, gsap, ScrollTrigger, lenis, pixi, ogl, spline vb.).
3. Hareketli arka planı katmanlara ayır: arka plan tekniği (shader / canvas / video / CSS gradient animasyonu), tetikleyici (zaman / scroll / mouse), geçişler.
4. Tipografi, renk paleti, grid, boşluk ritmi ve mikro-etkileşimleri not et.
5. Performans hilelerini not et: lazy-load, düşük çözünürlüklü render, `requestAnimationFrame` kısıtlama, reduced-motion fallback.
6. Tekniği **kendi kodunla sıfırdan** minimal bir demo olarak yeniden yaz (kaynak kodu kopyalama).
7. Pattern kartı oluştur: ad, ne işe yarar, bağımlılıklar, maliyet (GPU/CPU), mobil davranışı, reduced-motion alternatifi.

## Outputs
- `outputs/YYYY-MM-DD_web-builder_teardown-[site].md` — analiz + pattern kartları
- Demo kodu: `outputs/sites/patterns/[pattern-adi]/`

## Quality Bar
- Her teardown en az 1 çalışan, bağımsız demo üretir.
- Demo'nun kodu özgündür; orijinal siteden hiçbir asset veya kod bloğu içermez.
- Her pattern kartında mobil + reduced-motion davranışı tanımlı.

## Tools
- Chrome DevTools / Playwright, Codrops tutorial'ları, library dokümantasyonları (context7)

## Integration
- Pattern'ler → SITE_BUILD'de yapı taşı olarak kullanılır
- Doğrulanmış teknikler → `MEMORY.md` "Efekt Kütüphanesi"
