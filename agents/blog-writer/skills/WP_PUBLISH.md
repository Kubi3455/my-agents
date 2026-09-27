# Skill: WP Publish

## Purpose
Hazır paketi WordPress'e yüklemek ve kalite kapısı geçerse yayınlamak: görseller → media library, yazı → önce draft (meta + featured + Jetpack metni), sonra ayrı istekle `publish`. Yayın anında Jetpack Social FB/IG/LinkedIn'e paylaşır.

## Serves Goals
- Düzenli yayın

## Inputs
- `outputs/YYYY-MM-DD_[slug]/post.json` + `content.html` + görseller
- Ortam değişkenleri: `WP_USER`, `WP_APP_PASSWORD`

## post.json şeması
```json
{
  "title": "…",
  "slug": "…",
  "excerpt": "…",
  "content_file": "content.html",
  "category": "AI",
  "tags": ["AI Agents", "LangGraph"],
  "focus_keyword": "…",
  "seo_title": "…",
  "meta_description": "…",
  "social_message": "…",
  "quality": {"seo_checklist": 12, "human_voice_test": 8, "images_reviewed": true},
  "images": [
    {"key": "featured", "file": "x.jpg", "title": "…", "alt": "…", "caption": "", "description": "…"},
    {"key": "inline-1", "file": "y.webp", "title": "…", "alt": "…", "caption": "…", "description": "…"}
  ]
}
```

## Process
1. `python scripts/wp_client.py check` → 200 değilse DUR, insana devret.
2. `quality` alanını **gerçek** sonuçlarla doldur (SEO checklist puanı, İnsan Sesi Testi puanı, görseller Read ile açılıp kontrol edildi mi). Uydurma puan = kural ihlali.
3. `python scripts/wp_client.py publish outputs/YYYY-MM-DD_[slug]/post.json --live`
   - **quality_gate** (script içinde, atlanamaz): voice_check PASS, SEO 12/12, İnsan Sesi 8/8, görseller kontrol edildi, seo_title ≤60, meta 140–158, odak kelime başlıkta, 10 etiket, featured JPEG + ≥2 inline, tüm alt text'ler, slug boşta, sosyal metin şablonu (link + Link in bio + 6 hashtag), meta kaydedildi
   - Kapı geçerse: draft → `publish` (ayrı istek) → Jetpack paylaşır. Çıkış kodu 0
   - Kapı geçmezse: yazı **taslak** kalır, çıkış kodu 3, nedenler `publish-result.json → gate_failures`. Düzeltilebilir bir sorunsa (ör. meta uzunluğu) düzelt ve yeni pakete geçmeden aynı taslağı güncelle; değilse journal'a yaz
   - Script: görselleri yükler (alt text dahil), `{{IMG:*}}` yer tutucularını `wp:image` bloklarıyla değiştirir, kategori adını ID'ye çevirir, etiketleri çözer (mevcutları yeniden kullanır), `status: draft` ile yazıyı oluşturur, Rank Math meta'yı yazar ve geri okuyarak doğrular.
4. Script çıktısındaki `post_id`, `status`, `public_link` / `edit_link`'i REPORT.md ve TOPIC_LOG'a yaz.
5. Script "post meta was not saved" uyarısı verirse: taslak yine de geçerlidir; REPORT.md'ye SEO alanlarını elle girilecek şekilde ekle ve insana kurulum snippet'ini hatırlat.

## Outputs
- Yayında yazı (canlı link) veya kapıdan kalmış taslak (düzenleme linki + nedenler)
- `outputs/YYYY-MM-DD_[slug]/publish-result.json`

## Quality Bar
- Yazı `publish` (veya kapı nedeniyle `draft`), featured image atanmış, tüm yer tutucular değiştirilmiş (content'te `{{IMG:` kalmadı)

## Tools
- `scripts/wp_client.py`

## Integration
- Son adım. Sonrası: HEARTBEAT → Raporla
