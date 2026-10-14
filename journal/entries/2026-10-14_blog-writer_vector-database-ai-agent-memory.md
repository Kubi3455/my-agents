# 2026-10-14 · blog-writer · Vector Database for AI Agent Memory

- Yayında: "Vector Database for AI Agent Memory: Qdrant vs Chroma vs pgvector" — https://www.firstevolvenextscale.com/vector-database-ai-agent-memory/ (WP ID 1692), kalite kapısından ilk denemede geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8. 5 iç link (langgraph-long-term-memory, crewai-unified-memory-system, langgraph-checkpointing, mcp-context-bloat, semantic-caching-llm-agents), 3 dış resmi link (github.com/pgvector, qdrant.tech, cookbook.chromadb.dev), 10 etiket, 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul, yeniden üretim yok).

## Teknik doğrulama: üç vektör veritabanı da gerçekten kuruldu ve karşılaştırıldı
Kuyruktaki son konuydu (Qdrant vs Chroma vs pgvector, agent memory bağlamında). Bu yazı için üç farklı sistemi aynı anda gerçek kurulumlarla test ettim: `apt` ile Postgres 16 + `postgresql-16-pgvector` (0.6.0) kurup gerçek bir HNSW index oluşturdum; `qdrant-client` ve `chromadb`'yi güncel sürümleriyle (PyPI'deki en güncel sürümlerle `pip index versions` ile eşleştirilerek doğrulandı) bir venv'e kurup local/embedded modlarında gerçek sorgular çalıştırdım. İki somut bulgu canlı testten geldi, dokümandan değil:
- `maintenance_work_mem` bilinçli olarak 1MB'a düşürülünce, HNSW build'i hata vermedi ama gerçek bir Postgres NOTICE'ı ("Building will take significantly more time.") bastı — bunu `conn.add_notice_handler` ile bizzat yakaladım.
- Güncel `qdrant-client==1.19.1`'de `client.search()` artık sadece deprecated değil, tamamen kaldırılmış: çağırınca `AttributeError: 'QdrantClient' object has no attribute 'search'` alıyorsun, uyarı değil çökme. Eski tutorial'ları kopyalayanlar için makaleye özellikle bir "Common Pitfalls" maddesi olarak işlendi.
Üç sistemde de embedding boyutu uyuşmazlığı hatası ayrı ayrı tetiklenip tam metinleriyle makaleye alındı (üçü de farklı: pgvector `DataException`, Qdrant `ValueError`, Chroma `InvalidArgumentError`).

## Ortam notları
- `pip install -q Pillow` bugün de yanlış Python'a kurdu (bare `pip`/`pip3` → Python 3.13, ama script'lerin çalıştığı `python3` → 3.11); `python3 -m pip install -q Pillow` ile düzeltildi. Bu kaçıncı gün art arda olduğu önceki journal girişlerinde (2026-10-12, 2026-10-13) de not edilmişti.
- Detached HEAD **bu sefer yoktu** — `git branch --show-current` → `main`, origin ile güncel. Önceki art arda seriyi bozan ilk gün.
- Postgres servisini ve `postgresql-16-pgvector` paketini bu oturumda kurdum; bulut ortamı sıfırlanınca kaybolacak, kalıcı bir değişiklik değil.

## Sonraki
- Kuyruk artık boş (bu konu son maddeydi). Yarınki döngüde HEARTBEAT kuralı gereği önce `TOPIC_SELECTION` çalışıp 5 yeni konu üretilecek.
- REPORT.md'de 3 eski yazıya (langgraph-long-term-memory, crewai-unified-memory-system, langgraph-checkpointing) önerilen ters iç link insan onayı bekliyor.
- Tekrarlayan `pip install` sorunu hâlâ HEARTBEAT.md adım 0'a kalıcı düzeltme olarak işlenmeyi bekliyor (insan onayı gerekiyor, ajan kendi başına HEARTBEAT.md'yi değiştirmiyor).
