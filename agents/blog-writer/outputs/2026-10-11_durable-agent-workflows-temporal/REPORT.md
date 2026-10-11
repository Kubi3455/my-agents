# Report — 2026-10-11

## Yayın
- **Başlık:** Durable Agent Workflows with Temporal: Surviving Crashes Without Checkpointing Hacks
- **Odak kelime:** durable agent workflows with temporal
- **Durum:** Yayında (post 1674) — https://www.firstevolvenextscale.com/durable-agent-workflows-temporal/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1674&action=edit
- **Kalite kapısı:** `gate_failures: []` (ilk `--live` denemesinde geçti, taslakta kalmadı)
- **Kelime sayısı:** ~2.650

## Checklist (12/12)
1. Odak kelime başlıkta ✅
2. Odak kelime ilk 100 kelimede ✅ (kelime 68 civarı, 2. paragrafın başında)
3. Odak kelime bir H2'de ✅ ("Durable Agent Workflows with Temporal: A Minimal Step in Python")
4. SEO title ≤60 karakter ✅ (53)
5. Meta description 140–158 karakter ✅ (153)
6. Slug kısa, yılsız, odak kelimeli ✅ (`durable-agent-workflows-temporal`), envanterde boşta
7. 6 iç link, farklı ve açıklayıcı anchor'lar ✅ (ilk 300 kelimede ≥1 — ai-agent-rate-limits linki kelime ~115'te)
8. 4 dış link, resmi Temporal dokümantasyonu (docs.temporal.io), utm'siz ✅
9. Tüm görsellerde odak/ilgili kelimeli, ≤125 karakter, birbirinden farklı alt text ✅
10. Featured (JPEG) + 3 inline (WebP) ✅
11. FAQ bölümü (5 soru) ✅
12. H1 yok, H2→H3 hiyerarşisi atlamasız (Pros/Cons H3'leri Pros and Cons H2 altında, FAQ soruları H3), 10 etiket hazır, odak kelime etikette (`Durable Agent Workflows`) ✅

## voice_check.py
`sentences=114 mean_len=20.1 stdev=12.5 short(<=6w)=15 flat_triplets=4 em_dash=1` → **PASS**

## İnsan Sesi Testi: 8/8
1. Yasak kalıp/kelime taraması temiz — voice_check + elle tarandı, bulgu yok (ilk taslakta 1 "it's not X, it's Y" karşıtlık deseni ve 18 em dash vardı, ikisi de düzeltildi)
2. Art arda 3 aynı uzunlukta cümle — flat_triplets=4/114 (~3.5%, eşik %15'in çok altında)
3. ≥4 uzmanlık sinyali — Postgres `agent_progress` tablosu + Slack mesajının iki kez gitmesi anekdotu, RetryPolicy alanlarının pratik anlamı, `random.choice()` buried-helper determinism bug'ı (gerçek hata deneyimi), `temporalio-openai-agents` ayrı paket olduğu bulgusu (bugün kendi testimde keşfedildi)
4. ≥2 açık görüş/tavsiye — "I'd stop hand-rolling a status column the moment…", "I'll say the quiet thing out loud: … LangGraph's checkpointer is simpler to run and genuinely enough", "last I checked, there's no equivalent drop-in plugin [for Claude Agent SDK]"
5. Conclusion tavsiye (özet değil) — kişisel eşik kuralı + "Start there, get one Workflow running end to end… before worrying about Continue-As-New and versioning"
6. Açılış gerçek durumla başlıyor — "Last month I shipped a 'crash-safe' agent loop that was really just a Postgres table…"
7–8. Sesli okuma / meslektaş testi — subjektif, teknik detay ve kod boyunca destekli

## Teknik Doğrulama (uçtan uca)
Bu yazının riskli kısmı: Temporal'ın Python SDK'sında determinism kuralları ve OpenAI Agents SDK entegrasyonunun paket yolu hızlı değişiyor (dokümantasyon "1.0.0 moved the integration out of `temporalio.contrib.openai_agents` into `temporalio.openai_agents`" diyor). İkincil kaynaklara güvenmek yerine:
- Temiz bir venv'e `temporalio==1.34.0`, `temporalio-openai-agents==1.1.0`, `openai-agents==0.23.1` kuruldu.
- `inspect.signature` ile `RetryPolicy.__init__`, `OpenAIAgentsPlugin.__init__`, `ModelActivityParameters.__init__` imzaları makaledeki kodla birebir doğrulandı; `workflow.random/now/uuid4/signal/update/wait_condition` varlığı kontrol edildi.
- Makaledeki **üç** Python örneği de gerçek bir yerel Temporal dev server'a karşı (`temporalio.testing.WorkflowEnvironment.start_local()`, gerçek Temporal CLI 1.9.1 / Server 1.32.0 indirip çalıştırıyor) uçtan uca çalıştırıldı: (1) minimal Workflow+Activity+RetryPolicy, (2) Signal tabanlı onay akışı, (3) OpenAIAgentsPlugin üzerinden gerçek bir OpenAI model çağrısı yapan agent workflow'u. Üçü de beklenen sonucu döndürdü.
- Bu test sırasında gerçek bir bulgu çıktı: `temporalio.openai_agents` modülü yalnızca ayrı `temporalio-openai-agents` paketi kurulunca çalışıyor, taban `temporalio` paketine dahil değil. Bu pratik detay makaleye eklendi (dokümanda açıkça yazmıyor).
- Kaynaklar: `sources.md`

## Görseller
4/4 görsel ilk denemede kabul edildi (yeniden üretim yok). Etiketler ("Crash"/"Resume", "Workflow"/"Activity"/"History", "workflow.random()"/"workflow.now()"/"Replay", "Signal"/"Resume") birebir doğru yazılmış, kod paneli yok, 4 görsel aynı lacivert/mavi/mor paletinde.

## İç Link Ağı (bu yazıdan)
- ai-agent-rate-limits
- prevent-ai-agents-stuck-in-loops
- claude-agent-sdk-vs-openai-agents-sdk
- human-in-the-loop-for-ai-workflows
- langgraph-checkpointing
- debugging-multi-agent-workflows

## Ters İç Link Önerisi (insan uygulayabilir)
- `langgraph-checkpointing` yazısına, "for crashes across multiple machines or long human waits, see durable agent workflows with Temporal" tarzı bir cümleyle bu yazıya link eklenebilir.
- `ai-agent-rate-limits` yazısına, RetryPolicy'nin sıra/sequencing sorununu da çözdüğünü belirten bir cümle eklenebilir.
- `claude-agent-sdk-vs-openai-agents-sdk` yazısına, OpenAI Agents SDK tarafı için Temporal entegrasyonuna işaret eden bir not eklenebilir.

## Ortam Notu
- Oturum başında HEAD yine **detached** idi (origin/main ile aynı commit — veri kaybı yok, 8. kez: 2026-10-02, 03, 04, 07, 08, 09, 10, 11). `git checkout main && git fetch origin main && git merge --ff-only origin/main` ile düzeltildi.
- `pip install -q Pillow` (HEARTBEAT.md adım 0'daki komut birebir) yine yanlış Python'a kurdu; `python -m pip install -q Pillow` ile düzeltildi. Bu **6. kez** tekrarlıyor (2026-10-06, 07, 08, 09, 10, 11).
- Bugün Pazar, haftalık review günü değil (Pazartesi). Ama bu iki bulgu artık 6-8 gündür tekrarlıyor ve her ikisi de insan onayı bekliyor; bir sonraki Pazartesi review'da kalıcı düzeltme olarak HEARTBEAT.md'ye işlenmesini tekrar öneriyorum.
