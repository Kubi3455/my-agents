# Skill: Component Selection

## Purpose
Örnek kaynağındaki (varsayılan: 21st.dev community components) onlarca bileşen arasından verilen firmaya en uygun olanları seçmek. Her firma projesinde bu seçim yeniden yapılır.

## Serves Goals
- Benzer kalitede site üretmek
- Referans havuzunu büyütmek (incelenen her bileşen havuza girer)

## Inputs
- Aktif firma dosyası: `data/imports/firmalar/[firma-adi].md`
- Örnek kaynağı: firma dosyasındaki `Örnek kaynağı` alanı, yoksa `data/imports/ORNEK_KAYNAGI.md`
- Firma analizi sonucu belirlenen konsept (HEARTBEAT 3A, adım 1)
- Tasarım planı (DESIGN_DIRECTION çıktısı): renk token'ları, fontlar ve hero'nun rolü. Adaylar bu plana uyarlanabilirliklerine göre değerlendirilir.
- `MEMORY.md` → "21st.dev Bileşen Notları" ve "Sektör → Konsept Eşleşmeleri"

## Kaynak Yapısı (21st.dev)
- Kategori sayfaları: `https://21st.dev/community/components/s/[kategori]`
  - Marketing blokları: `hero`, `background`, `shader`, `call-to-action`, `pricing-section`, `testimonials`, `navigation-menu`, `announcement`, `border`, `features`, `footer`...
  - UI bileşenleri: `button`, `card`, `accordion`, `form`, `input`, `dialog`, `table`...
- Bileşen sayfası: `https://21st.dev/@[kullanici]/components/[bilesen-adi]` (canlı önizleme, kod, bağımlılıklar, lisans)
- Kurulum: `npx shadcn@latest add "https://21st.dev/r/[kullanici]/[bilesen-adi]?api_key=$API_KEY_21ST"`
- Kategori slug'ları değişebilir; bulunamazsa ana sayfadaki kategori listesinden doğrula.

## Process
1. **Sitenin bölüm planını çıkar.** Firma dosyasındaki `Sayfalar` alanından bölümleri belirle (ör. hero, hizmetler, referanslar, iletişim).
2. **İmza bileşenini ara (asıl görev).** Sitenin karakterini belirleyecek tek bileşen budur: genelde `hero`, `background` veya `shader` kategorisinden hareketli, görsel olarak güçlü bir parça.
   - İlgili kategori sayfalarını tara, konsepte uyan 5-10 adayı kısa listeye al.
   - Her adayın canlı önizlemesini aç (Playwright / tarayıcı), masaüstü + mobil ekran görüntüsü al.
3. **Adayları puanla (1-10):**
   - **Wow** — ilk 3 saniyedeki görsel etki
   - **Firma Uyumu** — konsept, sektör, hedef kitle ve marka renklerine uyarlanabilirlik
   - **Uyarlanabilirlik** — renk, metin ve görselin prop/Tailwind ile kolay değişip değişmediği
   - **Teknik Sağlık** — bağımlılık sayısı ve ağırlığı (ör. Spline/Three.js ağır), mobil performans, reduced-motion desteği
4. **Tek imza bileşenini seç.** En yüksek toplam kazanır. Eşitlikte Firma Uyumu yüksek olan seçilir. Firma Uyumu <6 olan seçilemez.
5. **Lisans kontrolü.** Bileşen sayfasındaki lisansı oku. MIT, Apache-2.0, ISC gibi izin veren lisanslar kabul edilir. Lisans yoksa veya kısıtlayıcıysa sıradaki adaya geç.
6. **Destekleyici bileşenler (opsiyonel, en fazla 4).** Diğer bölümler için imza bileşeniyle aynı görsel dili taşıyan bileşenleri seç (ör. CTA, pricing, testimonials). Aynı puanlama ve lisans kontrolü uygulanır. Uygun bileşen yoksa o bölüm elle yazılır.
7. **Seçimi kaydet.** Bileşen URL'leri, kurulum komutları, bağımlılıklar ve lisansları rapora yaz. Seçim projeye sabitlenir, insan istemedikçe değişmez.

## Outputs
Firma döngü raporunun "Bileşen Seçimi" bölümü (`outputs/YYYY-MM-DD_web-builder_firma-[firma-adi].md`):

| Rol | Bileşen | URL | Wow | Firma Uyumu | Uyarlanabilirlik | Teknik Sağlık | Toplam | Lisans |
|-----|---------|-----|-----|-------------|------------------|---------------|--------|--------|

Ayrıca elenen adaylar ve elenme nedenleri, imza bileşeninin neden seçildiği (2-3 cümle) ve kurulum komutları listesi.

## Quality Bar
- Tam olarak 1 imza bileşeni seçilmiş olmalı.
- Seçilen her bileşenin lisansı belgelenmiş ve izin verici olmalı.
- Her seçimin "bu firmaya neden uygun?" sorusuna tek cümlelik cevabı olmalı.
- Seçilen bileşen gerçekten önizlemede açılıp denenmiş olmalı; sadece isim veya küçük resimden seçim yapılmaz.

## Tools
- WebFetch / firecrawl (kategori listeleri), Playwright / Chrome DevTools (canlı önizleme, ekran görüntüsü)
- shadcn CLI (kurulum; `API_KEY_21ST` ortam değişkeni gerekir)

## Integration
- Seçilen bileşenler → SITE_BUILD'e (kurulum + firmaya uyarlama)
- Ağır bağımlılıklı bileşenler → QUALITY_AUDIT'te performans açısından özellikle izlenir
- Onaylanan seçimler → MEMORY.md "21st.dev Bileşen Notları" ve "Sektör → Konsept Eşleşmeleri"
