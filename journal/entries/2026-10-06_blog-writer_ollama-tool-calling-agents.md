# 2026-10-06 · blog-writer · Ollama Tool Calling Agents

- Yayında: "Ollama Tool Calling Agents: No LangChain Required" — https://www.firstevolvenextscale.com/ollama-tool-calling-agents/ (WP ID 1644), kalite kapısından ilk denemede geçti (SEO 12/12, voice_check PASS, İnsan Sesi 8/8).
- İçerik, Ollama'nın yerel `/api/chat` tool-calling API'sini LangChain olmadan kullanmayı anlatıyor: minimal bir ajan döngüsü, OpenAI-uyumlu endpoint'in `num_ctx`'i sessizce düşürüp tool şemalarını context'ten kırpması (gerçek bir gotcha, kişisel anekdotla açılışta kullanıldı), dün (2026-10-05) yayınlanan Ollama v0.40.0'ın streaming tool-call parser iyileştirmesi, ve model boyutuna göre tool-calling güvenilirliği.
- Konu doğrulaması için ayrı bir araştırma ajanı kullanıldı (web search): Ollama'nın güncel API şeklini, v0.40.0'ın tam değişikliklerini ve gerçek bir GitHub issue'dan (#12064) alıntı hata mesajını doğruladı. Araştırma, yayından 1 gün önce çıkan v0.40.0'ı bulduğu için makaleye tazelik kattı.
- Agent-loop kod örneği (`requests.post` ile `/api/chat`, tool dispatch, `role: tool` ile ikinci istek) gerçek bir Ollama kurulumu bu ortamda mevcut olmadığı için, dokümantasyondaki yanıt şekline birebir uyan yerel bir mock HTTP sunucusuna (`http.server`) karşı uçtan uca çalıştırılarak doğrulandı. `arguments` alanının zaten parse edilmiş dict olduğu (JSON string değil) bu testle doğrulandı.
- 6 iç link (local-llms-ollama-with-web-search, mcp-context-bloat, prevent-ai-agents-stuck-in-loops, structured-outputs-in-local-llm, debugging-multi-agent-workflows, autogpt-vs-crewai-vs-langgraph), 4 dış resmi link (docs.ollama.com, ollama.com/search, 2x github.com/ollama/ollama), 10 etiket (6'sı mevcut etiketlerle eşleşti).
- 4 görsel (1 JPEG featured + 3 WebP inline) ilk denemede kabul edildi, yeniden üretim gerekmedi.

## Ortam notu (bulut)
`pip`/`python` komutu bu bulut oturumunda Python 3.11'e gidiyor, ama bazı önceden kurulu paketler Python 3.13'ün kullanıcı sitesinde. `pip install Pillow` (sade) paketi 3.13'e kurdu, `optimize_image.py` ise `python` (3.11) ile çalıştığı için `ModuleNotFoundError: No module named 'PIL'` verdi. Çözüm: `python -m pip install -q Pillow` kullanmak (doğru yorumlayıcıya kurar). HEARTBEAT.md'deki "pip install -q Pillow" adımını `python -m pip install -q Pillow` olarak güncellemek, gelecekte bu adımın tekrar aynı hataya düşmesini önler — insan onayı bekliyor.

## Sonraki
- Kuyrukta 2 konu kaldı (sırada ilk: LangGraph long-term memory / vector store setup).
- Git durumu: oturum başında `main`, origin ile senkronize, detached HEAD yoktu (3 gündür tekrarlayan sorun bu kez görülmedi).
