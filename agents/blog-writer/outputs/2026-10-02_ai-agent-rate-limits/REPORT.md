# Report — 2026-10-02

## Yazı
- **Başlık:** AI Agent Rate Limits: A Practical Retry Strategy for 429 Errors
- **Odak anahtar kelime:** ai agent rate limits
- **Kelime sayısı:** 2088
- **Durum:** Yayında — https://www.firstevolvenextscale.com/ai-agent-rate-limits/
- **WP ID:** 1625 (edit: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1625&action=edit)
- **Kategori:** AI
- **Etiketler (10):** AI Agent Rate Limits, 429 Errors, Exponential Backoff, Token Bucket Rate Limiting, Idempotent Retries, Tenacity, Anthropic API, OpenAI API, AI Agent Debugging, Multi-Agent Systems

## Kalite Kapısı
- `quality_gate`: **GEÇTİ** (gate_failures: yok), ilk denemede yayınlandı
- SEO checklist: 12/12
- `voice_check.py`: PASS (sentences=87, stdev=10.3, em_dash=0)
- İnsan Sesi Testi: 8/8
- Görseller: 4/4 Read ile açılıp kontrol edildi

## İç Linkler (5)
- debugging-multi-agent-workflows — "infinite loops in CrewAI and LangGraph"
- mcp-context-bloat — "tool definitions alone can eat a third of your context window"
- prevent-ai-agents-stuck-in-loops — "retry and exit strategies"
- local-llms-ollama-with-web-search — "running models locally through Ollama"
- human-in-the-loop-for-ai-workflows — "keeping a human in the loop"

## Dış Linkler (3, resmî kaynak)
- https://platform.claude.com/docs/en/api/rate-limits
- https://developers.openai.com/api/docs/guides/error-codes
- https://tenacity.readthedocs.io/en/latest/

## Görseller
- Featured (JPEG, 149 KB): 429 wall → backoff → retry gate scene
- 3 inline (WebP, 81–90 KB): fan-out math, same-time vs. jitter comparison, token bucket + idempotency
- Not: jitter görseli ilk denemede kod panelinde bozuk bir etiket ("COITH JITTER)") içeriyordu; basitleştirilmiş prompt'la 1 kez yeniden üretildi, ikinci deneme temiz çıktı

## Teknik Doğrulama
- Kod örnekleri (tenacity retry, token bucket limiter, idempotent fingerprint cache) `/tmp` içinde bir venv'de çalıştırılarak doğrulandı, sadece makul görünüyor diye yazılmadı
- Anthropic/OpenAI hata kodları ve header adları resmi dokümanlardan birebir alındı (bkz. `sources.md`)

## Sosyal Paylaşım
Jetpack Social yayın anında paylaştı (Facebook + LinkedIn; Instagram Jetpack'e bağlı değil — bilinen kısıt, bkz. 2026-09-28 journal). Metin şablonu: kanca + 2-3 cümle + link + "Link in bio" + 6 hashtag (#AIAgentRateLimits #429Errors #ExponentialBackoff #Python #AIAgents #AIEngineering).

## Bulgu: Geçmiş İki Yazı İçin Kayıt Boşluğu
Envanterde 2026-09-29 (crewai-unified-memory-system, WP 1613) ve 2026-10-01 (mcp-context-bloat, WP 1619) yayında görünüyordu, ama repoda bu günlere ait TOPIC_LOG satırı, journal kaydı, `outputs/` klasörü ya da git commit'i yoktu — bulut ortamı o günlerde çalışıp yayınlamış ama adım 5'teki commit/push ya hiç yapılmamış ya da konteyner commit'ten önce geri dönüştürülmüş. Bugün TOPIC_LOG'a geriye dönük iki satır eklendi (bkz. journal). Bu, bulut rutininin günlük push'unun gerçekten tamamlandığını teyit eden bir mekanizma olmadığını gösteriyor; kullanıcıya bildirildi.

## Ters İç Link Önerileri (insan uygular)
- `prevent-ai-agents-stuck-in-loops` yazısına, bu yeni yazının "token bucket ile retry'dan önce concurrency sınırlama" bölümüne bir cümlelik link eklenebilir (retry/exit stratejilerinin doğal devamı)
- `debugging-multi-agent-workflows` yazısına, 429 hatalarının da "agent takılması" gibi göründüğü ama kök nedeninin farklı olduğu bir not eklenebilir
