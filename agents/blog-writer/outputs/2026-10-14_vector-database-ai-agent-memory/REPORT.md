# Report — 2026-10-14

## Yayın
- **Başlık:** Vector Database for AI Agent Memory: Qdrant vs Chroma vs pgvector
- **Durum:** Yayında (`publish`, `gate_failures: []`, ilk denemede geçti)
- **Canlı link:** https://www.firstevolvenextscale.com/vector-database-ai-agent-memory/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1692&action=edit
- **WP ID:** 1692
- **Odak anahtar kelime:** vector database for ai agent memory
- **Kelime sayısı:** ~2.626
- **Kategori:** AI
- **Etiketler (10):** AI Agent Memory, Vector Database, Vector Search, Vector Store Setup, Self-Hosted Vector Database, AI Agent Multi-Tenancy, Qdrant, Chroma, pgvector, Vector Database Comparison

## Kalite
- **SEO checklist:** 12/12 (odak kelime başlıkta + ilk 100 kelimede [kelime 98] + bir H2'de; SEO title 53 karakter; meta description 141 karakter; slug 5 kelime yılsız; 5 iç link farklı hedeflere; 3 dış resmi link utm'siz; 4 görsel hepsi ≤125 karakter farklı alt text; FAQ 5 soru; H2→H3 hiyerarşi atlamasız, 10 etiket hazır)
- **voice_check.py:** PASS (sentences=78, mean_len≈23.8, short(<=6w)=8, flat_triplets=2, em_dash=0)
- **İnsan Sesi Testi:** 8/8 (yasak kalıp taraması temiz; ritim kırıldı — kısa cümleler eklendi; ≥4 uzmanlık sinyali: maintenance_work_mem NOTICE'ı bizzat tetikleme, client.search() kaldırılma gotcha'sı, is_tenant flag versiyon notu, 3 farklı dimension-mismatch hata mesajı; ≥2 açık görüş — "I'd reach for Chroma...", "I'd go straight to Qdrant..."; açılış gerçek bir durumla başlıyor; conclusion özet değil tavsiye)
- **Görseller:** 1 JPEG (featured, 138 KB) + 3 WebP (51–79 KB), 4/4 ilk denemede kabul edildi, yeniden üretim yok. Her görsel Read ile açılıp tüm etiketler tek tek okundu: "pgvector", "Qdrant", "Chroma", "Scale" (featured); "Filter", "Agent-1/2/3" (inline-1); "pgvector", "HNSW", "Memory", "Build Time" (inline-2); "Qdrant Collection", "Tenant A/B" (inline-3) — hepsi doğru yazılmış, uydurma/bozuk etiket yok.

## Teknik Doğrulama (canlı test, sources.md'de detay)
- Postgres 16 + pgvector 0.6.0 (apt paketi) kuruldu; `psycopg[binary]`, `pgvector`, `qdrant-client`, `chromadb` güncel sürümleriyle (PyPI'deki en güncel sürümlerle eşleştiği `pip index versions` ile doğrulandı) temiz bir venv'e kuruldu.
- pgvector: HNSW index oluşturuldu, filtrelenmiş benzerlik sorgusu çalıştırıldı; `maintenance_work_mem` bilerek 1MB'a düşürülüp 20.000 satırlık bir HNSW build'i gerçek Postgres NOTICE'ını ("Building will take significantly more time.") bizzat tetikledi; `hnsw.iterative_scan` parametresinin bu (0.6.0) sürümde var olmadığı doğrulandı (0.8.0'da eklendiği resmi GitHub release notlarından teyit edildi, canlı test edilmedi çünkü apt'ta sadece 0.6.0 var).
- Qdrant: `:memory:` local modda collection oluşturuldu, `is_tenant` payload index + `query_points()` ile filtrelenmiş arama çalıştırıldı; `client.search()` metodunun kaldırıldığı (`AttributeError`, deprecation warning değil) bizzat `qdrant-client==1.19.1` ile doğrulandı.
- Chroma: `PersistentClient` ile yerel, sunucusuz bir collection oluşturuldu, metadata filtreli sorgu çalıştırıldı.
- Her üç sistemde de embedding boyutu uyuşmazlığı hatası gerçek kodla tetiklenip tam hata mesajı makaleye alındı (üçü de farklı, gerçek metin).
- Doküman-doğrulamalı (canlı test edilmedi) iddialar sources.md'de ayrıca işaretlendi: pgvector HNSW varsayılan `m`/`ef_construction` ve Docker `--shm-size` notu, Qdrant çok-kiracılık rehberi detayları (1.11.0, payload_m, ~20.000 nokta eşiği), Chroma'nın tek-node/bellek sınırı dokümantasyonu.

## Mevcut Yazılara Önerilen Ters İç Linkler (insan uygulayacak)
- `langgraph-long-term-memory`: "Picking a vector store" bölümüne bu yazıya link eklenebilir ("if you're choosing between pgvector, Qdrant, and Chroma before committing to this setup, see our full comparison").
- `crewai-unified-memory-system`: Memory sisteminin arkasındaki vektör deposu tartışmasına bu yazıya link eklenebilir.
- `langgraph-checkpointing`: Postgres'i zaten checkpoint için kullanan okurlara "aynı veritabanını agent memory için de kullanabilirsin" notu + link.

## Notlar
- Kuyrukta bu konu son kalan maddeydi; kuyruk artık boş. HEARTBEAT kuralı gereği yarın TOPIC_SELECTION tetiklenecek (5 yeni konu üretilecek).
- Ortam: `pip install -q Pillow` yine yanlış Python'a kurdu (8. değil, bugün tekrar fark edildi — toplamda art arda kaçıncı gün olduğu MEMORY/journal'da takip ediliyor), `python3 -m pip install -q Pillow` ile düzeltildi. Detached HEAD bu sefer **yoktu** (branch zaten `main`, origin ile güncel).
- Teknik doğrulama için ek olarak gerçek bir Postgres 16 + pgvector apt paketi kuruldu (bu ortamda kalıcı değil, bulut oturumu sıfırlanınca gidecek).
