# Skill: SEO & Linking

## Purpose
Yazıya bağlamsal iç/dış linkleri eklemek, Rank Math meta alanlarını hazırlamak ve 12 maddelik SEO checklist'ini geçirmek.

## Serves Goals
- SEO kalitesi
- İç link ağı

## Inputs
- `outputs/YYYY-MM-DD_[slug]/content.html`, `sources.md`
- `data/post-inventory.json`
- Odak + ikincil anahtar kelimeler

## Process
1. **İç linkler (4–6):**
   - Envanterden konu olarak en ilgili yazıları seç (aynı küme > aynı kategori > genel)
   - Anchor, cümlenin içinde doğal bir ifade olmalı; hedef yazının odak konusunu tanımlamalı ("how we debugged infinite loops in CrewAI"). "click here", "this article" yasak
   - Aynı hedefe iki link verme; ilk 300 kelimede en az 1 iç link
   - Link biçimi: `https://www.firstevolvenextscale.com/[slug]/`
2. **Dış linkler (2–4):** `sources.md`'deki **resmî** dokümanlar / orijinal araştırma. `utm_*`/`ref` parametrelerini sil. Rakip bloglara link verme.
3. **Ters iç link önerisi:** Envanterde bu yeni yazıya link vermesi mantıklı 2–3 eski yazıyı ve eklenecek cümleyi REPORT.md'ye yaz (ajan eski yazıyı düzenlemez).
4. **Meta:**
   - SEO title ≤ 60 karakter, odak kelime başa yakın (Rank Math `%title% | First Evolve Next Scale` ekini hesaba kat, yazı başlığı ayrı olabilir)
   - Meta description 140–158 karakter, odak kelime + somut fayda, "Learn how…" / "A practical guide…" tarzı (mevcut örnek: "Learn how Instructor and Pydantic turn messy local LLM output into reliable, validated JSON — with real Python code and Ollama examples.")
   - Slug: 3–6 kelime, yılsız, odak kelimeden türetilmiş
   - Excerpt: 1–2 cümle (meta description'dan farklı)
5. **Taksonomi:** 1 kategori (mevcutlardan). **Tam 10 etiket**, yazıya özel ve SEO ile birlikte hazırlanır:
   - 1: odak anahtar kelime (ör. `Structured Outputs Local LLM`)
   - 1: slug'ın ana ifadesi, odak kelimeden farklıysa
   - 3–4: ikincil anahtar kelimeler
   - 2–3: yazıda gerçekten ele alınan araç/framework adları (`Ollama`, `LangGraph`)
   - 1–2: arama niyeti / konu kümesi (`AI Agent Debugging`)
   - Envanterde aynı adda etiket varsa o yazılır (script eşleştirir), Title Case, 1–4 kelime
6. **Checklist** (her madde 1 puan, hedef 12/12):
   1. Odak kelime başlıkta
   2. Odak kelime ilk 100 kelimede
   3. Odak kelime en az bir H2'de
   4. SEO title ≤ 60 karakter
   5. Meta description 140–158 karakter ve odak kelimeli
   6. Slug kısa ve odak kelimeli
   7. 4–6 iç link, anchor'lar farklı ve açıklayıcı
   8. 2–4 dış link, resmî kaynak, utm'siz
   9. Tüm görsellerde odak/ilgili kelimeli alt text
   10. Featured image + ≥2 inline görsel
   11. FAQ bölümü (3–5 soru)
   12. H1 yok (başlık WP'den gelir), H2→H3 hiyerarşisi atlamasız; 10 etiket hazır ve odak kelime etiketlerde

## Outputs
- Güncellenmiş `content.html` (linkler eklenmiş)
- `post.json` içindeki alanlar: `title`, `slug`, `excerpt`, `seo_title`, `meta_description`, `focus_keyword`, `category`, `tags`
- REPORT.md: checklist skoru + ters iç link önerileri

## Quality Bar
- 12/12. Eksik madde varsa düzeltilmeden WP_PUBLISH'e geçilmez

## Tools
- `data/post-inventory.json`
- Opsiyonel: `searchfit-seo:on-page-seo`, `searchfit-seo:internal-linking` skill'leri

## Integration
- ARTICLE_WRITING'den alır → IMAGE_GENERATION'a alt text anahtar kelimelerini verir → WP_PUBLISH
