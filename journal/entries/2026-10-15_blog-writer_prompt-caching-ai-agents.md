# 2026-10-15 · blog-writer · Prompt Caching for AI Agents

- **Taslak** (kapıdan geçemedi): "Prompt Caching for AI Agents: Cutting Long-Horizon Token Costs" — WP ID 1694, edit: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1694&action=edit. SEO 10/12 (odak kelime başlık/ilk100/H2, meta, slug, 6 iç + 3 dış link, FAQ, 10 etiket hepsi geçti; sadece görsel maddeleri #9/#10 eksik), voice_check PASS, İnsan Sesi 8/8.

## Engel: OPENAI_API_KEY kredisi bitti (image generation tamamen bloke)
Kurulum kontrolünde `OPENAI_API_KEY` **set** görünüyordu (eksik değil), ama hesabın kredisi tükenmiş. İki ayrı gerçek API çağrısıyla doğrulandı: `gpt-4o-mini` ile basit bir chat completion ve `generate_image.py` ile gerçek bir `gpt-image-2` görsel üretme denemesi — ikisi de `429 insufficient_quota / credit_balance_exhausted` döndü ("You have no credits remaining. Add credits... at platform.openai.com/settings/organization/billing/"). Bu, bugünkü akışın tek gerçek engeliydi: TOPIC_SELECTION, ARTICLE_WRITING, SEO_LINKING, SOCIAL_SHARE hepsi tamamlandı ama IMAGE_GENERATION hiç çalışamadı, bu da SEO checklist'in 2 maddesini (#9 alt text, #10 featured+inline) ve `images_reviewed`'ı düşürdü, kapı beklendiği gibi `seo_checklist 10/12`, `images not visually reviewed`, `featured image missing`, `fewer than 2 inline images` nedenleriyle reddetti.

**İnsan aksiyonu gerekiyor:** OpenAI hesabına kredi eklenmesi (platform.openai.com/settings/organization/billing). Kredi eklendikten sonra `content.html` içindeki 3 görsel yeri `<!-- TODO (human): ... -->` yorumlarıyla işaretli (her biri önerilen sahneyi tarif ediyor); IMAGE_GENERATION çalıştırılıp `post.json`'a görseller eklenip var olan taslak (1694) WP REST API ile elle güncellenerek `publish --live` tekrar denenebilir — script'in var olan taslağı güncelleyen bir komutu yok (bu, 2026-10-07'den bilinen aynı script eksikliği).

## Konu kuyruğu yeniden dolduruldu
`TOPIC_LOG.md` kuyruğu boştu; 5 yeni konu üretildi (web araştırmasıyla: Ocak 2026 arXiv çalışması "Don't Break the Cache", agent evaluation/trajectory testing, model routing/fallback, agent sandbox karşılaştırmaları, agent güvenliği/prompt injection). Bugünün konusu (prompt caching) en yüksek puanlıydı: taze araştırma + envanterde 6 bağlanabilir yazı + semantic caching yazısından mekanik olarak net ayrışma.

## Teknik doğrulama
- Anthropic `cache_control`: resmi doküman (platform.claude.com) + yerel `anthropic==1.14.0` SDK'sının `CacheControlEphemeralParam` tip tanımı canlı kontrol edildi (Anthropic anahtarı ortamda yok, önceki günlerdeki gibi doküman+tip doğrulaması kullanıldı).
- OpenAI otomatik caching: resmi dokümandan doğrulandı; canlı `cached_tokens` alanı kredi yüzünden gözlemlenemedi, bu açıkça kod yorumlarında ve sources.md'de belirtildi.
- arXiv 2601.06007 ("Don't Break the Cache") rakamları (41-80% maliyet, 13-31% TTFT, 500+ oturum) özet sayfasından alındı, tam metne erişilmedi — sources.md'de not edildi.

## Ortam notu
`pip install -q Pillow` bugün de yanlış Python'a kurdu (bare `pip` → Python 3.13, script'lerin çalıştığı `python3` → 3.11); `python3 -m pip install -q Pillow` ile düzeltildi. Bu, 2026-10-12/13/14 girişlerinde de tekrar eden aynı sorun — HEARTBEAT.md adım 0'a kalıcı düzeltme (`python3 -m pip install` kullanımı) eklenmesi hâlâ insan onayı bekliyor.
