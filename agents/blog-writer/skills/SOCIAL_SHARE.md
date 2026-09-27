# Skill: Social Share

## Purpose
Her taslak için yazının sosyal medya özetini yazmak ve taslağa gömmek. Yazı yayınlandığı anda Jetpack Social bu metni kapak görseliyle birlikte Facebook Sayfası, Instagram Business ve LinkedIn profiline otomatik paylaşır.

## Serves Goals
- Organik büyüme (sosyal trafik)
- Düzenli yayın

## Nasıl Çalışır (iş bölümü)
- **Ajan:** paylaşım metnini yazar → `post.json` → `social_message` → WP_PUBLISH bunu `jetpack_publicize_message` meta alanına yazar.
- **Jetpack Social (eklenti):** insan yazıyı **yayınladığında** metni, kapak görselini ve linki bağlı 3 hesaba gönderir.
- Taslak aşamasında **hiçbir şey paylaşılmaz**: taslak linki herkese kapalıdır, erken paylaşım 404'e götürür (kullanıcı kararı 2026-09-28).
- Ücretsiz Jetpack planında 3 platforma **aynı metin** gider (kullanıcı bunu seçti). Metin üçüne de uymalı; Facebook/LinkedIn ayrıca otomatik link önizlemesi ekler.

## Inputs
- Son hâli `content.html`, başlık, odak kelime, 10 etiket
- `data/STYLE_GUIDE.md` → "İnsan Sesi" (sosyal metin de aynı sesle yazılır)

## Process
1. Yazının **tek bir somut vaadini** bul (okur ne kazanacak?).
2. Metni aşağıdaki **sabit şablonla** yaz (İngilizce, toplam 450–750 karakter). Kullanıcı kararı 2026-09-28: tek ortak metin, her yazıda rutin.

```
[KANCA: kişisel ya da acı noktası odaklı, ≤ 120 karakter]

[2–3 kısa cümle: yazıda ne öğrenilecek + 1 somut detay (hata, parametre, karşılaştırma)]

Read the full guide 👉 https://www.firstevolvenextscale.com/[slug]/
📌 On Instagram? Link in bio.

#[Niş1] #[Niş2] #[Niş3] #[Araç] #[Geniş1] #[Geniş2]
```

   - **Link:** her zaman `https://www.firstevolvenextscale.com/[slug]/` (site kalıcı link yapısı `/%postname%/`; slug taslakta belli olduğu için link önceden doğru yazılır)
   - **"📌 On Instagram? Link in bio."** satırı her yazıda aynen kalır
   - **Hashtag (tam 6, üç platforma uyumlu orta yol):**
     - 3 niş: yazının 10 etiketinden türet, boşluksuz CamelCase (`LangGraph Checkpointing` → `#LangGraphCheckpointing`)
     - 1 araç/dil: yazıda kullanılan (`#Python`, `#Ollama`, `#LangGraph`)
     - 2 geniş ama ilgili: `#AIAgents`, `#MachineLearning`, `#GenerativeAI`, `#LLM`, `#AIEngineering`, `#DevCommunity` havuzundan konuya en yakın 2 tanesi
     - Yasak: `#AI` tek başına, `#tech`, `#viral`, `#follow`, `#instagood` gibi spam etiketler; Türkçe hashtag yok
3. İnsan Sesi yasak listesini bu metne de uygula; emoji yalnızca şablondaki 👉 ve 📌.
4. `post.json` → `"social_message": "..."`

## Outputs
- `post.json` → `social_message`
- REPORT.md → "Sosyal paylaşım metni" bölümü (insan yayından önce görsün/düzenleyebilsin)

## Quality Bar
- 450–750 karakter, ilk satır ≤ 120 karakter
- Link doğru slug ile, "📌 On Instagram? Link in bio." satırı var, tam 6 hashtag
- Yazıda olmayan bir iddia yok

## Tools
- `scripts/wp_client.py publish` (meta yazımı), `scripts/wp_client.py check` (Jetpack alanı erişilebilir mi)

## Integration
- SEO_LINKING'den sonra, WP_PUBLISH'ten önce çalışır
- Kapak görseli JPEG olmalı (Instagram WebP kabul etmez) → IMAGE_GENERATION
