# Skill: Inspiration Hunt

## Purpose
Piyasadaki hareketli arka planlı ve görsel olarak üst düzey web sitelerini bulup puanlayarak bir referans havuzu oluşturmak.

## Serves Goals
- Referans havuzunu büyütmek

## Inputs
- `knowledge/AUDIENCE.md` ve `knowledge/BRAND.md` — hangi sektör/estetik önemli
- `data/imports/` — insanın eklediği referans URL'ler (`REFERENCES.md`)
- `MEMORY.md` — daha önce işe yarayan/yaramayan referans tipleri
- Web: Awwwards (SOTD/SOTM), Godly, SiteInspire, Lapa Ninja, One Page Love, CSS Design Awards, Codrops

## Modlar
- **Firma Modu'nda bu skill çalışmaz.** Firma projelerinde seçim işini `COMPONENT_SELECTION` yapar.
- **Keşif modu:** Aşağıdaki sürecin tamamı uygulanır.

## Process
1. `data/imports/REFERENCES.md` içinde insanın verdiği URL'leri öncelikle al.
2. Galeri sitelerinden son 30 günün öne çıkan sitelerini tara (web search / firecrawl / tarayıcı).
3. Her aday için bir ekran görüntüsü veya kısa not al; hareketli öğeyi tanımla (ör. "WebGL akışkan gradient arka plan", "scroll ile dönen 3D model").
4. Her siteyi 1-10 arası puanla:
   - **Wow** — ilk 3 saniyedeki görsel etki
   - **Teknik** — kullanılan tekniğin öğrenme değeri
   - **Uygulanabilirlik** — bizim stack'imizle makul sürede yeniden üretilebilir mi
   - **Firma Uyumu** — *(sadece Firma Modu'nda)* konsept, hedef kitle ve içerik yapısı aktif firmaya ne kadar oturuyor. Bu puanı 6'nın altında olan site seçilemez.
5. Teknik etiketleri ekle: `webgl`, `three.js`, `gsap`, `scroll-driven`, `shader`, `canvas`, `lottie`, `css-only`, `video-bg`, `cursor-fx`, `lenis`.
6. Toplam puana göre sırala; en iyi 2'yi DESIGN_TEARDOWN için işaretle.

## Outputs
- `outputs/YYYY-MM-DD_web-builder_inspiration.md` — tablo: URL | Kaynak | Hareketli öğe | Etiketler | Wow | Teknik | Uygulanabilirlik | Toplam

## Quality Bar
- Haftada en az 5 site; en az 3 farklı teknik etiket temsil edilmeli.
- Her satırda "neyi öğreneceğiz?" sorusunun tek cümlelik cevabı var.
- Sadece statik güzel site değil: listenin ≥%60'ı hareketli/animasyonlu öğe içermeli.

## Tools
- Web search, firecrawl (scrape/screenshot), Playwright / Chrome DevTools (canlı inceleme)

## Integration
- En yüksek puanlı siteler → DESIGN_TEARDOWN
- Sektör/estetik trendleri → journal
