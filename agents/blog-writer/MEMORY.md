# Blog Writer Memory

> Yalnızca **onaylanmış** örüntüler. Hipotezler "Denenecek" bölümüne. Haftalık review'da güncellenir.

## Ses (insan düzeltmelerinden öğrenilen)
- 2026-09-27 (kullanıcı kuralı): Yazılar gerçek, samimi bir AI uzmanı yazmış gibi olmalı; yapay zekâ kokusu kabul edilmez. Detaylar: STYLE_GUIDE → "İnsan Sesi". Her yazıda ayrı bir insan sesi revizyon turu zorunlu.

## Konu Seçimi
- 2026-09-27: Son 2 ayın en tutarlı kümesi "agent loops / debugging multi-agent / local LLM". Bu kümede iç link ağı kurmak kolay.

## Yayın
- 2026-09-28 (kullanıcı kararı): Taslak değil otomatik yayın. Güvenlik: script içindeki quality_gate; önce draft, sonra ayrı istekle publish (Jetpack paylaşımı son meta+görselle tetiklensin).
- 2026-09-28: Jetpack REST meta anahtarları doğrulandı: jetpack_publicize_message, jetpack_publicize_feature_enabled, jetpack_social_options, jetpack_social_post_already_shared.

## SEO
- 2026-09-28 (kullanıcı kuralı): Her yazıya SEO ile birlikte yazıya özel 10 etiket. `wp_client.py` → `MAX_TAGS = 10`.
- 2026-09-28: Rank Math tag arşivlerini `noindex, follow` yapıyor; sitemap_index.xml Rank Math'ten geliyor.
- 2026-09-27: Rank Math meta alanları varsayılan olarak REST'te yazılamaz; `data/imports/HOW_TO_SETUP.md` snippet'i şart.
- 2026-09-27: API'ye her zaman `www.` ile istek at; www'suz adres 301 yönlendiriyor ve POST'ta Authorization düşüyor.

## Görsel
- 2026-09-28: Detaylı prompt + featured `high` ile v2 kapak: numaralı adım başlıkları, lejant kutusu, tüm yazılar doğru. Hedef standart bu seviye (kullanıcı yayınladı = onaylandı). PNG 1.9 MB → JPEG 127 KB.
- 2026-09-28 (kullanıcı geri bildirimi): İlk seri "çok basit" bulundu. Artık detaylı, konuyu anlatan infografik sahneler + 2–4 kısa etiket; featured high kalite.
- 2026-09-28: gpt-image-2 (1536x1024, medium) prompt'taki "no text, no letters, no numbers" ile temiz çıktı verdi; 3/3 ilk denemede kabul.
- 2026-09-28: optimize_image.py ile PNG 1.5–1.7 MB → WebP 16–27 KB, gözle kayıp yok.

- 2026-10-02: İki panelli "karşılaştırma" sahnelerinde (ör. A vs B) model bazen sahte/bozuk kod panelleri ekliyor ("COITH JITTER)" gibi anlamsız başlıklar). Prompt'a "no embedded code panels" eklemek ve sahneyi ikona/metrik kartlarına yönlendirmek temiz sonuç verdi (1 yeniden üretimde düzeldi).

## Denenecek (Hipotezler)
- FAQ bölümü olan yazılar daha fazla gösterim alıyor mu? (Search Console verisi gelince test et)
- Başlıkta yıl ("2026") CTR'yi artırıyor mu?
