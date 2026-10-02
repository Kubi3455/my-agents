# Topic Log

Durumlar: `sırada` → `taslak` → `yayında` (veya `reddedildi`)
Kural: Aynı **odak anahtar kelime** tabloda iki kez olamaz.

## Sıradaki (kuyruk)

| # | Konu (çalışma başlığı) | Odak anahtar kelime | Küme | Kategori | Neden şimdi | Eklendi |
|---|------------------------|---------------------|------|----------|-------------|---------|
| 1 (yarın) | Tracing multi-agent systems: Langfuse/AgentOps for CrewAI & LangGraph debugging | agent tracing observability | agent loops / debugging | AI | Debugging kümesinde 3 yazı var ama hiçbiri gözlemlenebilirlik araçlarını kapsamıyor; CrewAI'nin yeni OTel/Langfuse entegrasyonu güncel | 2026-10-02 |
| 2 | Semantic caching for LLM agents: cutting redundant API calls and cost | semantic caching llm agents | cost/ops | AI Software | 2026'da token maliyeti ve agent fan-out'u artan bir ağrı noktası; sitede hiç ele alınmamış | 2026-10-02 |
| 3 | Tool-calling agents with Ollama without LangChain | ollama tool calling agents | local LLM | AI | Ollama'nın native tool calling desteği (Qwen3, Llama3.1) local LLM kümesini güçlendirir | 2026-10-02 |
| 4 | Long-term memory for LangGraph agents: a practical vector store setup | langgraph long term memory | agent loops / memory | AI | CrewAI unified memory yazısına doğal karşılık; MongoDB Atlas + LangGraph entegrasyonu güncel | 2026-10-02 |
| 5 | AutoGPT-style planning vs ReAct loops: picking an agent control flow | agent control flow patterns | agent loops | AI | Mimari karar noktası, forumlarda sık soru; mevcut karşılaştırma yazılarını tamamlar | 2026-10-02 |

## Taslak / Yayında

| Tarih | Başlık | Odak anahtar kelime | Durum | WP ID | Not |
|-------|--------|---------------------|-------|-------|-----|
| 2026-09-28 | LangGraph Checkpointing: How to Resume an AI Agent After a Crash | langgraph checkpointing | yayında | 1606 | İlk uçtan uca test; kapak v2 (detaylı infografik) ile değiştirildi |
| 2026-09-29 | CrewAI Unified Memory System: What Actually Changed in 2026 | crewai unified memory | yayında | 1613 | Bulut rutini önceki günlerde yayınladı ancak TOPIC_LOG/journal/outputs commit edilmemiş; envanterden geriye dönük kaydedildi (bkz. journal 2026-10-02 bulgu) |
| 2026-10-01 | MCP Context Bloat: How to Reclaim Your Agent's Context Window | mcp context bloat | yayında | 1619 | Aynı nedenle geriye dönük kaydedildi |
| 2026-10-02 | AI Agent Rate Limits: A Practical Retry Strategy for 429 Errors | ai agent rate limits | yayında | 1625 | SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 3 dış link, 10 etiket, 1 JPEG + 3 WebP görsel (jitter görseli 1 kez yeniden üretildi: ilk denemede kod panelinde bozuk etiket çıktı) |

## Reddedilenler

| Tarih | Konu | Neden |
|-------|------|-------|
