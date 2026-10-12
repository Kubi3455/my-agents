# 2026-10-12 · blog-writer · CrewAI Flows vs LangGraph Graphs

- Yayında: "CrewAI Flows vs LangGraph Graphs: Picking the Right Control Flow" — https://www.firstevolvenextscale.com/crewai-flows-vs-langgraph-graphs/ (WP ID 1680), kalite kapısından ilk denemede geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8.
- Kuyruktaki ilk konu alındı. 5 iç link, 4 dış resmi link (docs.crewai.com, reference.langchain.com), 10 etiket, 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul, yeniden üretim yok).

## Teknik doğrulama: önemli bir düzeltme + yeni bir doğrulama tekniği
- `langgraph==1.2.14` sorunsuz kuruldu, makaledeki örnek uçtan uca çalıştırıldı (billing/technical dalları + path_map'te olmayan bir route değeriyle bozuk bir graph). Bu test taslağın bir hatasını yakaladı: `path_map`'te olmayan bir değer `add_conditional_edges()`/`.compile()` anında değil, **o kenar ilk çalıştığında** `KeyError` fırlatıyor. Taslak "construction-time kontrol" diye yazmıştı (üçüncü parti karşılaştırma bloglarının ifadesine dayanarak); makale yayından önce "run time" olarak düzeltildi. Bu, gerçek kod çalıştırmanın ikincil kaynaklardan daha güvenilir olduğunun somut bir örneği.
- `crewai`'nin düz `pip install`'ı ~20 dakika boyunca tek paket kurmadan (bağımlılık çözücü backtracking'de) iptal edildi. Bunun yerine `--no-deps` ile kurup gerçek `ModuleNotFoundError` zincirini tek tek takip ederek (birkaç PyPI adı/import adı uyuşmazlığını düzelterek) güncel `crewai==1.15.27`'yi çalışır hâle getirdim. Bu teknik `MEMORY.md` → "Teknik Doğrulama"ya eklendi, gelecekte crewai içeren yazılarda zaman kazandırır.
- Çalışan kurulumla hem gerçek kaynak kodu (`crewai/flow/runtime/__init__.py`) okudum hem de makalenin açılış anekdotunu birebir yeniden ürettim: `@listen("Billing")` (büyük B) + router'ın küçük harf `"billing"` döndürdüğü bir Flow, `kickoff()`'u hatasız tamamlıyor, CrewAI'nin kendi "Completed" panellerini basıyor, ama ilgili adım hiç çalışmıyor — stdout/stderr'de error/warn/fail/exception geçen tek satır yok. Makalenin ana iddiası artık varsayımdan değil gerçek çalıştırmadan geliyor.

## Tekrarlayan ortam sorunları (insan onayı hâlâ bekliyor)
- **Detached HEAD — 9. kez art arda** (2026-10-02'den beri her gün). Yine `git checkout main && git fetch origin main && git merge --ff-only origin/main` ile düzeltildi, veri kaybı yok.
- **`pip install -q Pillow` yanlış Python'a kuruyor — 7. kez art arda**. `python3 -m pip install -q Pillow` ile düzeltildi.
- Yarın Pazartesi (haftalık review günü): bu ikisinin HEARTBEAT.md adım 0'a kalıcı düzeltme olarak işlenmesini üçüncü kez öneriyorum (en son 2026-10-11'de de önerilmişti).

## Sonraki
- Kuyrukta 2 konu kaldı (parallel tool calling, vector database showdown). 5'in altında ama boş değil; HEARTBEAT kuralı gereği TOPIC_SELECTION'ı bugün tetiklemedim, yarınki döngü muhtemelen tetikleyecek.
