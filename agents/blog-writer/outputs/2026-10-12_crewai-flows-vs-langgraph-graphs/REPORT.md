# Report — 2026-10-12 — CrewAI Flows vs LangGraph Graphs

## Yayın
- **Başlık:** CrewAI Flows vs LangGraph Graphs: Picking the Right Control Flow
- **Durum:** Yayında (WP ID 1680), ilk `publish --live` denemesinde kapıdan geçti, `gate_failures: []`
- **Canlı link:** https://www.firstevolvenextscale.com/crewai-flows-vs-langgraph-graphs/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1680&action=edit
- **Odak anahtar kelime:** crewai flows vs langgraph graphs
- **Kelime sayısı:** ~2254 (kod blokları hariç)

## Kalite
- **SEO checklist:** 12/12 (programatik olarak doğrulandı: odak kelime başlıkta + ilk 100 kelimede (81. kelime) + bir H2'de, seo_title 52 karakter, meta_description 153 karakter, slug kısa/odak kelimeli, 5 iç link, 4 dış resmi link, tüm görsellerde odak/ilgili kelimeli alt text, 1 JPEG + 3 WebP görsel, 5 soruluk FAQ, H1 yok, H2→H3 hiyerarşisi atlamasız, 10 etiket)
- **voice_check.py:** PASS (yasak kalıp yok, em dash 0, stdev 10.9, flat_triplets 1/90)
- **İnsan Sesi Testi:** 8/8 (gerçek bir hata anısıyla açılış, ≥4 uzmanlık sinyali, ≥2 açık tavsiye cümlesi, tavsiye içeren conclusion)
- **Görseller:** 4/4 ilk denemede kabul edildi (featured JPEG 91KB, 3 inline WebP 40-64KB), hepsi Read ile açılıp kontrol edildi — tüm etiketler ("CrewAI Flow", "LangGraph", "Event Chain", "Explicit Graph", "route", "billing", "technical", "BUILD OK", "Crash", "Resume") birebir doğru, bozuk/anlamsız metin yok, yeniden üretim gerekmedi

## Teknik doğrulama (bugünkü en kapsamlı bulgu)
Makalenin can alanı, CrewAI Flow'larda bir router'ın döndürdüğü string ile bir `@listen()` etiketinin birebir eşleşmemesi durumunda **hiçbir hata/uyarı vermeden** o adımın sessizce hiç çalışmaması. Bu iddia hem resmi dokümantasyondan hem de gerçek kod çalıştırmadan doğrulandı:

- `langgraph==1.2.14` sorunsuz kuruldu. Makaledeki LangGraph örneği uçtan uca çalıştırıldı (billing + technical dalları), ardından `path_map`'te olmayan bir etiket döndüren bozuk bir graph kuruldu ve `invoke()` çağrıldığında **gerçekten `KeyError` fırlattığı** doğrulandı — ama bu kontrol `add_conditional_edges()` veya `.compile()` anında değil, **o kenar ilk çalıştığında (run time)** gerçekleşiyor. Taslağın ilk hâli bunu "construction-time" / "build-time" olarak yanlış tanımlamıştı; makale, gerçek testin gösterdiği şekilde "run time" olarak düzeltildi.
- `crewai` paketinin düz `pip install` ile kurulumu makul bir sürede bitmedi (bağımlılık çözücü chromadb/opentelemetry/lancedb gibi ağır, sıkı sürümlenmiş bir ağaçta ~20 dakika sonra hâlâ tek paket kurmamış hâldeydi, iptal edildi). Bunun yerine `--no-deps` ile adım adım gerçek `ModuleNotFoundError` zincirini takip ederek (birkaç PyPI/import adı uyuşmazlığı düzeltilerek: `python-dotenv`, `rpds-py`, `PyJWT`, `python-dateutil`) **gerçek, güncel `crewai==1.15.27`** sürümü çalışır hâle getirildi.
- Çalışan kurulumla hem gerçek kaynak kodu okundu (`crewai/flow/runtime/__init__.py` → `_condition_satisfied`: `return condition in events`, normalize/doğrulama yok) hem de **gerçekten çalıştırıldı**: makaledeki `TriageFlow` doğru çalıştı; `@listen("Billing")` (büyük B) + router'ın küçük `"billing"` döndürdüğü bozuk versiyon ise `kickoff()`'u normal tamamladı, CrewAI'nin kendi "Completed" panellerini bastı, ama `handle_billing` hiç çalışmadı ve `flow.state.result` boş kaldı — stdout/stderr'de error/warn/fail/exception/traceback geçen tek satır yok. Makalenin açılış anekdotu ve "Silent String-Matching Trap" bölümü artık varsayımdan değil gerçek çalıştırmadan geliyor.

Detaylar `sources.md`'de.

## Ters iç link önerisi (insan uygulayabilir)
- `agents/blog-writer/outputs/2026-10-08_agent-control-flow-patterns/content.html`: "control flow" tartışmasının hemen altına, "CrewAI Flows ve LangGraph Graphs'ın kendi routing mekanizmalarını nasıl modellediği" cümlesiyle bu yeni yazıya bağlanabilir.
- `agents/blog-writer/outputs/2026-10-?_autogpt-vs-crewai-vs-langgraph` (envanterdeki eski yazı): framework seçimi tartışmasının sonuna, "routing'in kendisi nerede fark yaratıyor" diye bu yazıya bağlanabilir.

## Sosyal paylaşım metni
```
A router typo in a CrewAI Flow once cost me 20 minutes. No exception, no traceback — one branch just quietly never ran.

CrewAI Flows vs LangGraph Graphs: real code for both, the exact moment each one's "deterministic" routing stops being deterministic, and which one I'd actually reach for.

Read the full guide 👉 https://www.firstevolvenextscale.com/crewai-flows-vs-langgraph-graphs/
📌 On Instagram? Link in bio.

#CrewAIFlows #LangGraphGraphs #AgentControlFlow #Python #AIAgents #AIEngineering
```
(496 karakter, ilk satır 119 karakter, 6 hashtag, Jetpack Social yayın anında FB/IG/LinkedIn'e paylaşacak)

## Ortam notları
- Oturum başında HEAD yine detached'tı (9. kez art arda, 2026-10-02'den beri); `git checkout main && git fetch && git merge --ff-only` ile düzeltildi.
- `pip install -q Pillow` yine yanlış Python'a kurdu (7. kez art arda); `python3 -m pip install -q Pillow` ile düzeltildi.
- Bu ikisi artık haftalardır her gün tekrarlıyor; Pazartesi review'da HEARTBEAT.md adım 0'a kalıcı düzeltme olarak eklenmesini tekrar öneriyorum.
