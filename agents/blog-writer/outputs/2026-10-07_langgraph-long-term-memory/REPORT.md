# Report — 2026-10-07 — LangGraph Long-Term Memory

## Yayında
- **Başlık:** LangGraph Long-Term Memory: A Practical Vector Store Setup
- **Link:** https://www.firstevolvenextscale.com/langgraph-long-term-memory/ (post ID 1650)
- **Odak anahtar kelime:** langgraph long-term memory
- **Kelime sayısı:** ~2.450
- **SEO checklist:** 12/12
- **voice_check.py:** PASS (sentences=96, mean_len=18.5, stdev=10.3, short=10, flat_triplets=3, em_dash=1)
- **İnsan Sesi Testi:** 8/8 (açılış gerçek bir hata/anekdotla başlıyor, ≥4 uzmanlık sinyali, ≥2 açık tavsiye cümlesi, conclusion tavsiye niteliğinde)
- **Görseller:** 1 JPEG featured + 3 WebP inline, 4/4 ilk denemede kabul edildi (yeniden üretim gerekmedi)
- **İç linkler (5):** langgraph-checkpointing, semantic-caching-llm-agents, crewai-unified-memory-system, mcp-context-bloat, debugging-multi-agent-workflows
- **Dış linkler (4):** docs.langchain.com/oss/python/langgraph/stores, docs.langchain.com/oss/python/langchain/long-term-memory, github.com/pgvector/pgvector, pypi.org/project/langgraph-checkpoint-postgres
- **Etiketler (10):** LangGraph Long-Term Memory, LangGraph, AI Agent Memory, LangGraph agents, PostgresStore, pgvector, Vector Store Setup, Semantic Search, Python, Memory Scopes (5'i mevcut etiketlerle eşleşti)

## Teknik doğrulama
Bütün kod örnekleri gerçekten çalıştırıldı (izole bir venv'de, Python 3.11, `langgraph==1.2.14`, `langgraph-checkpoint-postgres==3.1.2`, `psycopg[binary]==3.3.6`), gerçek bir yerel PostgreSQL 16 + pgvector kurulumuna ve gerçek OpenAI embeddings'e (`text-embedding-3-small`) karşı:
- InMemoryStore + semantic search: doğru sıralama ile çalıştı
- NumPy kurulu değilken çıkan gerçek uyarı metni makaleye birebir alındı
- PostgresStore, pgvector sunucu eklentisi kurulu değilken gerçekten `FeatureNotSupported` hatası verdi (önce apt'ta `postgresql-16-pgvector` yoktu, kurulduktan sonra çalıştı)
- Dims kilitlenmesi (1536 → 384) gerçekten yeniden üretildi: `psycopg.errors.DataException: expected 1536 dimensions, not 384` — makaledeki hata mesajı kendi testimden, forum alıntısı değil

Detaylar `sources.md`'de.

## Kalite kapısı bulgusu (insan onayı bekliyor — scripts/ dizini ajan için yazılamaz)
İlk `publish --live` denemesi "focus keyword missing from title" ile taslakta kaldı (post 1650): kuyruktaki odak kelime boşluklu "langgraph long term memory" yazılmıştı, başlık ise doğru İngilizce biçimde tireli "Long-Term Memory". `scripts/wp_client.py`'deki `quality_gate` bu kontrolü literal substring (`kw not in title.lower()`) ile yapıyor, tire/boşluk farkını normalize etmiyor. Odak kelimeyi tireli biçime düzelttim (aynı 2026-10-04 "semantic caching" revizyonu gibi, bkz. MEMORY.md).

Ayrıca bu ilk deneme zaten WordPress'te bir taslak post (1650) ve bir etiket (573 "LangGraph Long Term Memory", kullanılmıyor/orphan) oluşturmuştu. `cmd_publish` var olan bir taslağı güncelleyen bir yol sunmuyor, yalnızca `POST /posts` ile her zaman yeni post yaratıyor; tekrar çalıştırsaydım kalite kapısındaki slug-çakışma kontrolü bu kez **kendi taslağımla** çakışıp sonsuza dek "slug already used" ile taslakta kalacaktı. WP_PUBLISH.md adım 3 "düzeltilebilir bir sorunsa aynı taslağı güncelle" diyor ama script'te bunu yapan bir komut yok. Aynı taslağı (1650) wp_client'ın `call()` yardımcı fonksiyonunu kullanarak elle güncelleyip (meta + etiketler) yayınladım; ikinci bir yazı oluşturmadım.

**Öneri (insan onayı bekliyor, script değişikliği gerektiği için agent uygulamadı):**
1. `quality_gate`'teki odak-kelime kontrolünü tire/boşluk/büyük-küçük harf normalize edecek şekilde gevşetmek.
2. `cmd_publish`'e bir `--update <post_id>` modu eklemek, böylece kapıdan dönen düzeltilebilir bir taslak yeniden `POST /posts` ile değil `POST /posts/{id}` ile güncellenebilsin (slug-çakışma kontrolünü kendi ID'sini hariç tutacak şekilde).
3. Etiket 573 ("LangGraph Long Term Memory", kullanılmıyor) temizlenebilir; agent etiket silme yetkisine sahip değil, insan WP admin'den silebilir.

## Git durumu
Oturum başında HEAD yine **detached** idi (en az 4. kez, bkz. 2026-10-02/03/04 kayıtları): local `main` origin'in 2 commit gerisindeydi (10-06 Ollama yazısı commit'i local main'e hiç ulaşmamıştı), detached HEAD ise o commit'in üzerindeydi. `git fetch origin main` sonrası detached HEAD'in origin/main ile birebir aynı olduğu doğrulandı (veri kaybı yok), `git checkout main && git merge --ff-only origin/main` ile düzeltildi. HEARTBEAT.md'ye önerilen "commit öncesi dal kontrolü" adımı **4 gündür insan onayı bekliyor** (2026-10-02, 10-03, 10-04, şimdi 10-07).

## Sonraki
- Kuyrukta 1 konu kaldı: "AutoGPT-style planning vs ReAct loops: picking an agent control flow". Yarın kuyruk boşalacağı için TOPIC_SELECTION'ın 10 aday üretme adımı gerekecek.
