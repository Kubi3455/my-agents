# Topic Log

Durumlar: `sırada` → `taslak` → `yayında` (veya `reddedildi`)
Kural: Aynı **odak anahtar kelime** tabloda iki kez olamaz.

## Sıradaki (kuyruk)

| # | Konu (çalışma başlığı) | Odak anahtar kelime | Küme | Kategori | Neden şimdi | Eklendi |
|---|------------------------|---------------------|------|----------|-------------|---------|
| 1 | AutoGPT-style planning vs ReAct loops: picking an agent control flow | agent control flow patterns | agent loops | AI | Mimari karar noktası, forumlarda sık soru; mevcut karşılaştırma yazılarını tamamlar | 2026-10-02 |

## Taslak / Yayında

| Tarih | Başlık | Odak anahtar kelime | Durum | WP ID | Not |
|-------|--------|---------------------|-------|-------|-----|
| 2026-09-28 | LangGraph Checkpointing: How to Resume an AI Agent After a Crash | langgraph checkpointing | yayında | 1606 | İlk uçtan uca test; kapak v2 (detaylı infografik) ile değiştirildi |
| 2026-09-29 | CrewAI Unified Memory System: What Actually Changed in 2026 | crewai unified memory | yayında | 1613 | Bulut rutini önceki günlerde yayınladı ancak TOPIC_LOG/journal/outputs commit edilmemiş; envanterden geriye dönük kaydedildi (bkz. journal 2026-10-02 bulgu) |
| 2026-10-01 | MCP Context Bloat: How to Reclaim Your Agent's Context Window | mcp context bloat | yayında | 1619 | Aynı nedenle geriye dönük kaydedildi |
| 2026-10-02 | AI Agent Rate Limits: A Practical Retry Strategy for 429 Errors | ai agent rate limits | yayında | 1625 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 3 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (jitter görseli 1 kez yeniden üretildi: ilk denemede kod panelinde bozuk etiket çıktı) |
| 2026-10-03 | Agent Tracing Observability: Langfuse vs AgentOps vs LangSmith | agent tracing observability | yayında | 1631 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 4 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (ilk denemede kabul, yeniden üretim yok). İlk publish denemesi geçici Imunify360 403'üne takıldı, ~5sn sonra retry ile geçti (bkz. journal) |
| 2026-10-04 | Semantic Caching for LLM Agents: Cut Redundant API Calls | semantic caching for llm agents | yayında | 1637 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 3 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (3. inline görsel 1 kez yeniden üretildi: ilk denemede konudan sapıp kullanıcı kimlik/fraud eşleştirme sahnesi üretti). GPTCache kodu venv'de uçtan uca doğrulandı; odak kelime kuyruktaki "semantic caching llm agents"tan "semantic caching for llm agents"a küçük revize edildi (daha doğal ifade) |
| 2026-10-06 | Ollama Tool Calling Agents: No LangChain Required | ollama tool calling agents | yayında | 1644 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 6 iç + 4 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul, yeniden üretim yok). Araştırma ajanı yayından 1 gün önce çıkan Ollama v0.40.0'ı (streaming tool-call parser iyileştirmesi) buldu ve makaleye işlendi. Agent-loop kod örneği gerçek Ollama kurulumu olmadığı için dokümantasyon şekline uyan yerel bir mock HTTP sunucusuna karşı uçtan uca çalıştırılarak doğrulandı |
| 2026-10-07 | LangGraph Long-Term Memory: A Practical Vector Store Setup | langgraph long-term memory | yayında | 1650 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 4 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul). InMemoryStore + PostgresStore (pgvector) uçtan uca gerçek bir Postgres 16 kurulumuna (apt ile pgvector eklendi) ve gerçek OpenAI embeddings'e karşı test edildi; dims uyuşmazlığı hatası (`DataException: expected 1536 dimensions, not 384`) kendi ortamımda yeniden üretildi. İlk `publish --live` denemesi kapıdan "focus keyword missing from title" ile döndü (kuyruktaki odak kelime boşluklu "long term", başlık ise doğru biçimde tireli "Long-Term"; script literal substring kontrolü yapıyor) — odak kelimeyi tireli biçime düzelttim (bkz. MEMORY.md). Bu deneme zaten bir taslak (post 1650) oluşturmuştu; script'te var olan taslağı güncelleyen bir komut olmadığından, aynı taslağı REST API ile elle güncelleyip (meta + etiketler) yayınladım, ikinci bir yazı oluşturmadım. Kalite kapısının tüm diğer 12 maddesini manuel doğruladım (publish öncesi) |

## Reddedilenler

| Tarih | Konu | Neden |
|-------|------|-------|
