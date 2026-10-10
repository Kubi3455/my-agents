# Report — 2026-10-10

## Yayın
- **Başlık:** A2A Protocol Explained: How AI Agents Talk to Each Other
- **Odak kelime:** a2a protocol
- **Durum:** yayında (ilk `--live` denemesinde geçti, `gate_failures: []`)
- **WP ID:** 1668
- **Canlı link:** https://www.firstevolvenextscale.com/a2a-protocol-explained/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1668&action=edit
- **Kelime sayısı:** ~2.185

## Kalite Kapısı
- SEO checklist: 12/12 (detay aşağıda)
- voice_check.py: PASS (em_dash=0, flat_triplets=0/75, stdev=10.8)
- İnsan Sesi Testi: 8/8 (self-assessment, detay aşağıda)
- Görseller: 4/4 Read ile açılıp kontrol edildi, 0 yeniden üretim (4/4 ilk denemede kabul, tüm etiketler birebir doğru)

## SEO Checklist (12/12)
1. Odak kelime başlıkta ✓ ("A2A Protocol Explained: How AI Agents Talk to Each Other")
2. Odak kelime ilk 100 kelimede ✓ (açılış paragrafında "the A2A protocol")
3. Odak kelime en az bir H2'de ✓ ("What the A2A Protocol Actually Solves")
4. SEO title ≤60 karakter ✓ (56)
5. Meta description 140-158 karakter ve odak kelimeli ✓ (150)
6. Slug kısa ve odak kelimeli ✓ (`a2a-protocol-explained`)
7. 5 iç link, farklı ve açıklayıcı anchor'lar ✓ (aşağıda liste; 4-6 hedefi içinde)
8. 3 dış resmi link, utm'siz ✓ (a2a-protocol.org spec, github a2a-python, aaif.io duyurusu)
9. Tüm görsellerde odak/ilgili kelimeli, ≤125 karakter, farklı alt text ✓
10. Featured (JPEG) + 3 inline (WebP) ✓
11. FAQ bölümü, 5 soru ✓
12. H1 yok, H2→H3 hiyerarşisi atlamasız, 10 etiket hazır, odak kelime terimi etiketlerde (`A2A Protocol`) ✓

## İç Linkler (5)
- `/mcp-context-bloat/` — "what MCP actually does to your agent's context window" (intro, ilk 100 kelime içinde)
- `/debugging-multi-agent-workflows/` — "same infinite-loop and handoff headaches"
- `/agent-tracing-observability/` — "real tracing across the whole multi-agent call chain"
- `/human-in-the-loop-for-ai-workflows/` — "human-in-the-loop gate"
- `/claude-agent-sdk-vs-openai-agents-sdk/` — "a different comparison entirely"

## Dış Linkler (3, resmi kaynak)
- https://a2a-protocol.org/latest/specification/ — A2A 1.0 resmi spesifikasyonu
- https://github.com/a2aproject/a2a-python — `a2a-sdk` resmi kaynak kodu
- https://aaif.io/blog/a2a-joins-aaif — Agentic AI Foundation'ın resmi duyurusu (2026-08-17)

## Ters İç Link Önerisi (eski yazılara, insan uygular)
- `mcp-context-bloat` yazısına, "diğer protokoller" bahsi geçen bir yere "see how A2A compares, a different layer entirely" gibi bir cümleyle bu yazıya link eklenebilir
- `autogpt-vs-crewai-vs-langgraph` yazısına, framework'lerin birbirleriyle konuşması bahsi geçen bir yere bu yazıya link verilebilir
- `claude-agent-sdk-vs-openai-agents-sdk` yazısına, in-process delegation ile cross-vendor protokol farkına değinen bir cümleyle bu yazıya link eklenebilir

## Teknik Doğrulama
Konu, kuyruktaki ilk sıradaydı (bkz. TOPIC_LOG.md #1). Web aramasıyla güncelliği doğrulandı: A2A, Ağustos 2026'da (17 Ağustos) Agentic AI Foundation'a (AAIF) taşındı ve v1.0.0'a ulaştı — konu kuyruğa eklendiği tarihten (2026-10-09) sonra da hâlâ güncel ve şimdi daha da güçlü bir "neden şimdi" kancası var.

Tüm teknik iddialar bugün doğrulandı, ikinci kaynaklardan değil birincil kaynaklardan:
- Resmi A2A 1.0 spesifikasyonu (`a2a-protocol.org`): AgentCard/Task/Message/Part alan adları, TaskState enum değerleri, versiyon pazarlığı davranışı (`A2A-Version` header, header yoksa varsayılan 0.3)
- Kurulu `a2a-sdk` 1.2.2 paketinin **gerçek kaynak kodu**, Python `inspect`/`DESCRIPTOR.fields` ile doğrudan incelendi (ikincil blog kaynaklarına güvenilmedi, çünkü MEMORY'de not edildiği gibi API hızlı değişiyor)
- Agentic AI Foundation'ın resmi duyuru yazısı (`aaif.io`, 2026-08-17 tarihli) — ikincil haber kaynaklarının "Linux Foundation" dediği yerde resmi kaynak "Agentic AI Foundation (AAIF), Linux Foundation'ın barındırdığı" diyor; makalede yalnızca resmi ifade kullanıldı
- **Tüm kod örnekleri yerel bir venv'de uçtan uca çalıştırıldı**: FastAPI `TestClient` ile gerçek bir `a2a-sdk` sunucusuna (AgentExecutor + DefaultRequestHandler + InMemoryTaskStore) karşı hem agent card endpoint'i hem `message:send` REST endpoint'i test edildi. İki gerçek hata makalede birebir kullanıldı çünkü kendi ortamımda yeniden üretildi: (1) `A2A-Version` header'ı olmadan gönderilen istek `"A2A version '0.3' is not supported..."` ile reddedildi, (2) eski `url=` kwarg'ı `AgentCard`'a verilince `ValueError: Protocol message AgentCard has no "url" field.` hatası alındı
- `A2AStarletteApplication` sınıfının güncel `a2a-sdk` sürümünde artık var olmadığı, paket içeriği taranarak (`pkgutil.walk_packages`) doğrulandı; yerine geçen `add_a2a_routes_to_fastapi` + `create_agent_card_routes`/`create_jsonrpc_routes`/`create_rest_routes` fonksiyonlarının imzaları `inspect.signature` ile teyit edildi

## Görsel Notu
4/4 görsel ilk denemede kabul edildi, yeniden üretim gerekmedi. Üçü de MEMORY.md'deki önceki sapma örüntülerinden kaçınmak için spesifik, somut sahne tarifleriyle (gerçek adım/alan isimleri, "bundan başka terim ekleme" kısıtlaması, ikili karşılaştırmalarda ikon/kart tabanlı sahne — kod paneli yok) üretildi.

## Sosyal Paylaşım Metni
Şablona uygun (499 karakter, ilk satır 87 karakter, link + "On Instagram? Link in bio." + tam 6 hashtag: #A2AProtocol #AgentToAgent #MultiAgentSystems #Python #AIAgents #AgenticAI).

## Ortam Kontrolü (bu oturumda düzeltildi)
- **Detached HEAD — 7. kez** (2026-10-02, 03, 04, 07, 08, 09, 10). Oturum yine detached açıldı; bu kez local `main` origin'in 5 commit gerisindeydi. `git checkout main && git fetch origin main && git merge --ff-only origin/main` ile düzeltildi, veri kaybı yok. Bu artık 7 gündür insan onayı bekleyen bir öneri (HEARTBEAT.md'ye commit öncesi/sonrası dal kontrolü eklenmesi).
- **`pip install` yanlış Python'a kuruyor — 5. kez** (2026-10-06, 07, 08, 09, 10). `python -m pip install -q Pillow` ile düzeltildi (PIL ilk `pip install` sonrası hâlâ import edilemiyordu, ikinci komuttan sonra çalıştı).

## Sonraki
- Kuyrukta 4 konu kaldı (Temporal durable workflows, CrewAI Flows vs LangGraph, parallel tool calling, vector database showdown) — bkz. TOPIC_LOG.md.
- Haftalık review bugüne denk gelmiyor (Pazartesi değil); ancak detached HEAD ve pip bulguları artık 7/5 gündür tekrarlıyor, bir sonraki Pazartesi review'da kalıcı HEARTBEAT.md düzeltmesi olarak karara bağlanması gerekiyor.
