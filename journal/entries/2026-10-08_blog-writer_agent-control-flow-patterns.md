# 2026-10-08 · blog-writer · Agent Control Flow Patterns

- Yayında: "Agent Control Flow Patterns: ReAct vs. Plan-and-Execute in 2026" — https://www.firstevolvenextscale.com/agent-control-flow-patterns/ (WP ID 1656). Kalite kapısı ilk `--live` denemesinde geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8, 5 iç + 4 dış resmi link, 10 etiket, 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul, yeniden üretim yok).
- İçerik ReAct (reason-act-observe) ile plan-and-execute kontrol akışlarını karşılaştırıyor: ne zaman hangisi, LangGraph'ın `Send` API'si ile elle plan-execute grafiği kurma, ve `create_agent` middleware'iyle (`before_model`/`after_model` hook'ları) bir ReAct döngüsünü üretimde adım sınırına bağlama. **Bulgu:** çoğu ReAct tutorial'ının hâlâ öğrettiği `langgraph.prebuilt.create_react_agent` artık **deprecated** — resmi LangChain referansı `langchain.agents.create_agent`'a geçişi istiyor. Bunu ve tüm kod örneklerini (imzalar, middleware hook isimleri, `Send` kullanımı) bugün resmi dokümantasyondan (`reference.langchain.com`, `docs.langchain.com`) WebFetch ile doğruladım; kod `py_compile` ile sözdizimi olarak kontrol edildi.
- Odak kelime "agent control flow patterns" literal substring kontrolüne göre doğrulandı (başlıkta, ilk 100 kelimede kelime 29'da, bir H2'de) — 2026-10-07'deki tire/boşluk uyumsuzluğu hatasını tekrarlamamak için özellikle kontrol edildi.
- Taslak sırasında em dash kullanımı STYLE_GUIDE sınırını (≤3) aştı (ilk taslakta 20); yayından önce tamamı (0'a) düzeltildi, voice_check PASS sonrası.

## Tekrarlayan ortam sorunları
- **Detached HEAD — 5. kez** (2026-10-02, 10-03, 10-04, 10-07, 10-08). Oturum başında yine origin/main ile aynı commit'te detached idi, veri kaybı yok, `git checkout main && git merge --ff-only origin/main` ile düzeltildi. Hâlâ insan onayı bekleyen öneri: HEARTBEAT.md'ye commit öncesi/sonrası dal kontrolü adımı eklenmesi.
- **`pip install` yanlış Python'a kuruyor — 3. kez** (2026-10-06, 10-07, 10-08). `python -m pip install -q Pillow` ile düzeltildi. Öneri: HEARTBEAT.md adım 0'daki komutu `python -m pip install -q Pillow` olarak güncelle.

## Sonraki
- Kuyruk artık boş. Yarın TOPIC_SELECTION'ın 10 aday üretme adımı tetiklenecek (HEARTBEAT karar ağacı).
