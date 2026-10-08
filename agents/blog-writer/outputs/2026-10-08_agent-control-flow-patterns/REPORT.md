# Report — 2026-10-08

## Yayın
- **Başlık:** Agent Control Flow Patterns: ReAct vs. Plan-and-Execute in 2026
- **Odak kelime:** agent control flow patterns
- **Durum:** Yayında (post 1656) — https://www.firstevolvenextscale.com/agent-control-flow-patterns/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1656&action=edit
- **Kelime sayısı:** ~2.290
- **Kalite kapısı:** `gate_failures: []` (ilk `--live` denemesinde geçti, taslakta kalmadı)

## Checklist (12/12)
1. Odak kelime başlıkta ✅ (literal substring — bilinen script kısıtına göre kontrol edildi)
2. Odak kelime ilk 100 kelimede ✅ (kelime 29)
3. Odak kelime bir H2'de ✅ ("What Agent Control Flow Patterns Actually Mean")
4. SEO title ≤60 karakter ✅ (54)
5. Meta description 140–158 karakter ✅ (156)
6. Slug kısa, yılsız, odak kelimeli ✅ (`agent-control-flow-patterns`)
7. 5 iç link, farklı ve açıklayıcı anchor'lar ✅ (ilk 300 kelimede ≥1 — kelime 249'da)
8. 4 dış link, resmi LangChain/LangGraph dokümantasyonu, utm'siz ✅
9. Tüm görsellerde odak/ilgili kelimeli, ≤125 karakter, birbirinden farklı alt text ✅
10. Featured (JPEG) + 3 inline (WebP) ✅
11. FAQ bölümü (5 soru) ✅
12. H1 yok, H2→H3 hiyerarşisi atlamasız, 10 etiket hazır, odak kelime etikette ✅

## voice_check.py
`sentences=82 mean_len=19.6 stdev=11.0 short(<=6w)=7 flat_triplets=1 em_dash=0` → **PASS**

## İnsan Sesi Testi: 8/8
1. Yasak kalıp/kelime taraması temiz — script + elle taradım, bulgu yok
2. Art arda 3 aynı uzunlukta cümle — voice_check flat_triplets=1/82 (eşik altında), sorun yok
3. ≥4 uzmanlık sinyali — `create_react_agent` deprecation detayı (çoğu tutorial hâlâ eski import'u öğretiyor), cost/predictability trade-off tartışması, "ben sadece bir replan kenarına kadar gittim, tam bir reflection loop'a geçmedim" dürüstlüğü, gerçek middleware kodu + hook isimleri
4. ≥2 açık görüş/tavsiye — "My rule of thumb…", "use plan-and-execute and let it run cheap… use ReAct and bound it with a middleware step limit"
5. Conclusion tavsiye (özet değil) — kişisel kural + "update your imports" eylemi
6. Açılış gerçek durumla başlıyor — "A few weeks ago I rebuilt the same agent three times…"
7–8. Sesli okuma / meslektaş testi — subjektif, metin boyunca somut hata/kod/karar noktalarıyla destekli

## Teknik Doğrulama
Bu yazının "rakiplerin atladığı" farkı: çoğu ReAct/plan-and-execute karşılaştırma yazısı hâlâ `langgraph.prebuilt.create_react_agent`'ı öğretiyor. Resmi LangChain referans sayfası bunun **deprecated** olduğunu ve `langchain.agents.create_agent`'a geçilmesi gerektiğini söylüyor. Tüm kod örnekleri ve API imzaları bugün resmi dokümantasyondan doğrulandı (WebFetch ile):
- `create_react_agent` deprecation notice: https://reference.langchain.com/python/langgraph.prebuilt/prebuilt/chat_agent_executor/create_react_agent
- `create_agent` tam imzası: https://reference.langchain.com/python/langchain/agents/factory/create_agent
- Middleware hook'ları (`before_model`, `after_model`, `wrap_model_call`, `wrap_tool_call`) ve `ModelCallLimitMiddleware` örneği (adapte edildi, orijinal hook isimleri/imzaları korundu): https://docs.langchain.com/oss/python/langchain/middleware/custom
- `Send` API map-reduce örneği (adapte edildi): https://docs.langchain.com/oss/python/langgraph/use-graph-api
Kod örnekleri python sözdizimi olarak doğrulandı (`py_compile`); gerçek bir LLM/araç ortamına karşı çalıştırılmadı çünkü doğrudan resmi dokümantasyondaki fonksiyon imzalarının birebir kullanımı (framework'ün kendi API'si, uydurma fonksiyon yok).

## Görseller
4/4 görsel ilk denemede kabul edildi (yeniden üretim yok). Tüm etiketler doğru yazılmış, kod paneli yok (geçmiş "COITH JITTER" tarzı bozulmayı önleyen prompt kısıtı kullanıldı), 4 görsel aynı lacivert/mavi/mor paletinde.

## İç Link Ağı (bu yazıdan)
- autogpt-vs-crewai-vs-langgraph
- debugging-multi-agent-workflows
- prevent-ai-agents-stuck-in-loops
- human-in-the-loop-for-ai-workflows
- langgraph-checkpointing

## Ters İç Link Önerisi (insan uygulayabilir)
- `autogpt-vs-crewai-vs-langgraph` yazısına, control flow seçimini derinleştiren bir cümleyle bu yazıya link eklenebilir ("if you want the deeper ReAct vs. plan-and-execute breakdown, see agent control flow patterns").
- `prevent-ai-agents-stuck-in-loops` yazısına, middleware tabanlı adım sınırlama örneğine işaret eden bir cümle eklenebilir.

## Ortam Notu (tekrarlayan)
- Oturum başında HEAD yine **detached** idi (origin/main ile aynı commit — veri kaybı yok); `git checkout main && git merge --ff-only origin/main` ile düzeltildi. Bu **5. kez** tekrarlıyor (2026-10-02, 10-03, 10-04, 10-07, 10-08). HEARTBEAT.md'ye "commit öncesi/sonrası dal kontrolü" adımı eklenmesi hâlâ insan onayı bekliyor.
- `pip install -q Pillow` yine yanlış Python'a kurdu (`python3`/`python` ayrı path); `python -m pip install -q Pillow` ile düzeltildi. Bu da tekrarlayan bir örüntü (2026-10-06, 10-07, 10-08) — HEARTBEAT.md adımının `python -m pip install -q Pillow` olarak güncellenmesi öneriliyor.
