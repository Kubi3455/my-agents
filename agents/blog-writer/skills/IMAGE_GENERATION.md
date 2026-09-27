# Skill: Image Generation

## Purpose
Her yazı için tutarlı görsel kimlikte 1 featured image ve 2–3 yazı içi görsel üretmek, SEO dostu dosya adı ve alt text ile paketlemek.

## Serves Goals
- SEO kalitesi

## Inputs
- `content.html` içindeki `{{IMG:inline-N}}` yer tutucuları ve çevresindeki bölüm
- Odak kelime
- `MEMORY.md` → "Görsel"

## Görsel Kimlik (her prompt'un sonuna eklenir)
> Detailed modern tech editorial infographic illustration, dark navy (#0B1220) background with electric blue and soft violet accents, isometric 3D style with depth and soft glow, rich layered composition with multiple meaningful components (servers, databases, code windows, terminal panels, clocks, warning icons, data cards, arrows showing flow), crisp clean lines, high detail, balanced layout, no logos, no human faces.

## Detay Kuralı (kullanıcı geri bildirimi 2026-09-28: "görseller çok basit")
Görsel **konuyu anlatmalı**, sadece süs olmamalı. Okur, yazıyı okumadan görsele bakınca konunun ne olduğunu anlamalı.
- **Sahne = mini hikâye:** Soyut noktalar/çizgiler yerine konunun gerçek bileşenleri. Örnek (checkpointing): kod editörü penceresi → agent düğümleri → çatlamış/kırmızı "timeout" düğümü → kaydedilmiş durum kartlarını tutan veritabanı silindiri → oradan devam eden parlak ok.
- **En az 5 anlamlı öğe** (pipeline adımları, veri kartları, sunucu/DB, uyarı ikonu, saat, terminal vb.) ve bir **okuma yönü** (soldan sağa akış, önce/sonra, iki yol karşılaştırması).
- **Kısa etiketler serbest:** 2–4 adet, her biri 1–2 İngilizce kelime. Prompt'ta tırnakla birebir yaz: `labeled "Checkpoint"`, `"Resume"`, `"Timeout"`. Cümle, paragraf, kod metni yok.
- **Kontrol:** Üretimden sonra görseli aç ve **görseldeki her yazıyı** oku. Model prompt'ta olmayan ek etiketler/açıklama kutuları ekleyebilir; bunlar kabul edilir **ancak** her kelime doğru yazılmış ve teknik olarak doğru olmalı (yanlış terim, bozuk harf, anlamsız kelime = yeniden üret, en fazla 2 deneme; yine bozuksa etiketsiz versiyon).
- **Kalite:** featured `--quality high`, inline `--quality medium`.

## Process
1. **Featured (1536x1024, high):** Yazının ana problem → çözüm hikâyesini tek sahnede, bileşenleriyle anlat.
2. **Inline (1536x1024, medium, 2–3 adet):** Her yer tutucu için o bölümün mekanizmasını göster: akış/pipeline, karşılaştırma (iki yan yana panel), mimari (bileşenler + oklar), zaman çizelgesi.
3. `python scripts/generate_image.py --prompt "<sahne> <görsel kimlik>" --out outputs/YYYY-MM-DD_[slug]/[dosya-adi].png`
4. **Sıkıştır (zorunlu, kasma önleme):** `python scripts/optimize_image.py x.png x.webp` → 1200px genişlik, WebP q75 (Squoosh ile aynı libwebp motoru; Squoosh PWA'sının CLI'ı yok). Hedef ≤150 KB. `post.json`'a **.webp** dosyası yazılır. **İstisna: featured → `.jpg`** (Instagram/Jetpack WebP kabul etmez; hedef ≤150 KB).
5. Oluşan görseli **aç ve kontrol et** (Read ile): etiket yazımı birebir mi, bozuk şekil/logo var mı, en az 5 anlamlı öğe var mı? Değilse yeniden üret (en fazla 2 deneme).
6. Her görsel için:
   - Dosya adı: `[odak-kelime]-[kavram].png`
   - Alt text: 1 cümle, ne gösterdiğini anlatır + odak/ilgili kelime (STYLE_GUIDE örneği gibi)
   - Title: SEO'lu, okunur başlık (medya kütüphanesi)
   - Caption: inline görseller için 1 cümle (featured için boş)
   - Description: 1–2 cümle, görselin yazıdaki rolü + anahtar kelime
7. `post.json` → `images` dizisine ekle.

## Outputs
- `outputs/YYYY-MM-DD_[slug]/*.png`
- `post.json` → `images: [{key, file, title, alt, caption, description}]` (`key`: `featured` veya `inline-N`)

## Quality Bar
- Etiketler birebir doğru yazılmış; prompt'ta olmayan metin yok
- Görsel, yazıyı okumadan konuyu anlatıyor (en az 5 anlamlı öğe)
- 4 görsel de aynı renk paletinde (seri gibi görünür)
- Her alt text farklı ve ≤ 125 karakter

## Tools
- `scripts/generate_image.py` (OpenAI Images API, `gpt-image-2`, `OPENAI_API_KEY`)
- `scripts/optimize_image.py` (Pillow/libwebp, Squoosh eşdeğeri)

## Integration
- WP_PUBLISH görselleri media library'ye yükler, yer tutucuları `wp:image` bloklarıyla değiştirir
