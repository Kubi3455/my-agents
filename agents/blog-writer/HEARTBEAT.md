# Blog Writer Heartbeat

## Schedule
- **Günlük:** Her gün 06:00 (Europe/Istanbul). Claude Code bulut rutini (scheduled agent) tetikler.
- **Haftalık review:** Pazartesi, günlük döngüden önce.
- Tetikleyici prompt: `agents/blog-writer/HEARTBEAT.md dosyasındaki günlük döngüyü çalıştır.`

## Each Cycle (Günlük)

### 0. Ön Kontrol
- Bulut ortamında: `pip install -q Pillow` (optimize_image.py için)
- `WP_USER`, `WP_APP_PASSWORD`, `OPENAI_API_KEY` ortam değişkenleri var mı? Yoksa DUR, journal'a "kurulum eksik" yaz.
- `python agents/blog-writer/scripts/wp_client.py check` → kimlik doğrulama ve Rank Math meta erişimi OK mi?
- Bugünün tarihli bir `outputs/YYYY-MM-DD_*` klasörü zaten varsa DUR (aynı gün iki yazı yok).

### 1. Bağlamı Oku
- `data/STYLE_GUIDE.md`, `MEMORY.md`, `data/TOPIC_LOG.md`
- Son 7 günün `journal/entries/` kayıtları (insan geri bildirimi var mı?)

### 2. Envanteri Tazele
- `python agents/blog-writer/scripts/wp_client.py inventory` → `data/post-inventory.json`
- Envanterde olup TOPIC_LOG'da "taslak" görünen yazılar yayınlanmış mı? → TOPIC_LOG'da durumunu `yayında` yap.

### 3. Karar Ağacı
- STYLE_GUIDE 30 günden eski mi **veya** envanterde son analizden beri ≥5 yeni insan yazısı var mı? → önce `SITE_ANALYSIS`
- TOPIC_LOG'daki "sıradaki" kuyrukta konu yok mu? → `TOPIC_SELECTION` (5 konuluk kuyruk üretir)
- Sonra her gün sırayla:
  1. `TOPIC_SELECTION` → kuyruktaki ilk konuyu al, güncelliğini doğrula
  2. `ARTICLE_WRITING` → taslak HTML
  3. `SEO_LINKING` → iç/dış link, meta, checklist (12/12 değilse düzelt)
  4. `IMAGE_GENERATION` → featured (JPEG) + 2–3 inline (WebP) görsel
  5. `SOCIAL_SHARE` → FB/IG/LinkedIn özet metni (yayında Jetpack paylaşır)
  6. `WP_PUBLISH` → `publish --live`: kapı geçerse yayın + Jetpack paylaşımı, geçmezse taslak

### 4. Raporla
- `outputs/YYYY-MM-DD_[slug]/REPORT.md`: başlık, odak kelime, kelime sayısı, checklist skoru, WP düzenleme linki, eski yazılara önerilen iç linkler
- `journal/entries/YYYY-MM-DD_blog-writer_[slug].md`: 3–5 satır özet
- `data/TOPIC_LOG.md`: konuyu `yayında` (veya kapıdan kaldıysa `taslak`) durumuna taşı

### 5. Durumu Repoya Kaydet (bulut çalışmasında zorunlu)
Bulut ortamı her gün sıfırdan başlar; kaydedilmeyen TOPIC_LOG/MEMORY/rapor ertesi gün kaybolur.
- `git add agents/blog-writer journal/entries` (ham `.png`'ler .gitignore ile hariç)
- `git commit -m "blog-writer: YYYY-MM-DD [slug] (yayında|taslak)"` → `git push`
- Push başarısızsa journal'a yaz ve raporda belirt

## Weekly Review (Pazartesi)

### 1. Veriyi Topla
- Kapıdan kalan taslaklar: nedenleri tekrar ediyor mu? (ör. hep meta açıklama uzunluğu → SEO_LINKING sürecini düzelt)
- İnsan yayından sonra yazıyı düzenlediyse: `wp_client.py diff [post_id] [pkg_dir]` → benzerlik < %90 ise farkları incele, MEMORY "Ses"e işle
- `data/imports/search-console/` altında yeni CSV varsa: sorgu, tıklama, gösterim, pozisyon

### 2. Hedeflerle Karşılaştır
| Metric | Target | This Week | Status |
|--------|--------|-----------|--------|
| Taslak sayısı | 7 | | |
| Stil düzeltmesi gerekmeyen | ≥ %80 | | |
| Ortalama iç link | 4–6 | | |
| Checklist 12/12 | %100 | | |

### 3. Kazanç ve Kayıplar
- İnsanın **tekrar eden düzeltmeleri** (ör. hep açılışı kısaltıyor) → MEMORY.md "Ses" bölümüne kural olarak ekle
- Search Console'da gösterimi yüksek ama tıklaması düşük yazılar → başlık/meta önerisi raporla
- Pozisyon 8–20 arasındaki sorgular → yeni konu adayı olarak TOPIC_LOG'a ekle

### 4. Hafızayı Güncelle ve Journal'a Haftalık Özet Yaz
