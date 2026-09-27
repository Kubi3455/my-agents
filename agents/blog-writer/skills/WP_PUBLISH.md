# Skill: WP Publish

## Purpose
Hazır paketi WordPress'e **taslak** olarak yüklemek: görseller → media library, yazı → draft, featured image, kategori/etiket, Rank Math meta.

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
  "images": [
    {"key": "featured", "file": "x.jpg", "title": "…", "alt": "…", "caption": "", "description": "…"},
    {"key": "inline-1", "file": "y.webp", "title": "…", "alt": "…", "caption": "…", "description": "…"}
  ]
}
```

## Process
1. `python scripts/wp_client.py check` → 200 değilse DUR, insana devret.
2. `python scripts/wp_client.py publish outputs/YYYY-MM-DD_[slug]/post.json`
   - Script: görselleri yükler (alt text dahil), `{{IMG:*}}` yer tutucularını `wp:image` bloklarıyla değiştirir, kategori adını ID'ye çevirir, etiketleri çözer (mevcutları yeniden kullanır), `status: draft` ile yazıyı oluşturur, Rank Math meta'yı yazar ve geri okuyarak doğrular.
3. Script çıktısındaki `post_id` ve `edit_link`'i REPORT.md ve TOPIC_LOG'a yaz.
4. Script "rank math meta yazılamadı" uyarısı verirse: taslak yine de geçerlidir; REPORT.md'ye SEO alanlarını elle girilecek şekilde ekle ve insana kurulum snippet'ini hatırlat.

## Outputs
- WordPress draft (ID + düzenleme linki)
- `outputs/YYYY-MM-DD_[slug]/publish-result.json`

## Quality Bar
- Yazı `draft` statüsünde, featured image atanmış, tüm yer tutucular değiştirilmiş (content'te `{{IMG:` kalmadı)

## Tools
- `scripts/wp_client.py`

## Integration
- Son adım. Sonrası: HEARTBEAT → Raporla
