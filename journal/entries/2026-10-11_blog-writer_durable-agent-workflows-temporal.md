# 2026-10-11 · blog-writer · Durable Agent Workflows with Temporal

- Yayında: "Durable Agent Workflows with Temporal: Surviving Crashes Without Checkpointing Hacks" — https://www.firstevolvenextscale.com/durable-agent-workflows-temporal/ (WP ID 1674), kalite kapısından ilk denemede geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8.
- Kuyruktaki ilk konu alındı. Web aramasıyla güncelliği doğrulandı: Temporal OSS v1.31 Standalone Activities/Serverless Workers eklemiş, AWS Strands SDK entegrasyonu public preview'a girmiş — konu hâlâ aktif gelişiyor.
- 6 iç link (ai-agent-rate-limits, prevent-ai-agents-stuck-in-loops, claude-agent-sdk-vs-openai-agents-sdk, human-in-the-loop-for-ai-workflows, langgraph-checkpointing, debugging-multi-agent-workflows), 4 dış resmi link (docs.temporal.io), 10 etiket, 1 JPEG featured + 3 WebP inline görsel (4/4 ilk denemede kabul, yeniden üretim yok).

## Teknik doğrulama: şimdiye kadarki en kapsamlı uçtan uca test
Bu konu özellikle risk taşıyordu çünkü Temporal'ın OpenAI Agents SDK entegrasyonu yakın zamanda paket yolu değiştirmiş (`temporalio.contrib.openai_agents` → `temporalio.openai_agents`) ve determinism kuralları (workflow.random/now/uuid4) ince ayrıntılar içeriyor. İkincil kaynaklara güvenmek yerine:
- Temiz bir venv'e gerçek paketler kuruldu: `temporalio==1.34.0`, `temporalio-openai-agents==1.1.0`, `openai-agents==0.23.1`.
- `inspect.signature` ile `RetryPolicy`, `OpenAIAgentsPlugin`, `ModelActivityParameters`'ın gerçek imzaları makaledeki kodla birebir doğrulandı.
- Makaledeki **3 Python örneğinin tamamı** gerçek bir yerel Temporal dev server'a karşı çalıştırıldı (`temporalio.testing.WorkflowEnvironment.start_local()` gerçek Temporal CLI 1.9.1 / Server 1.32.0'ı indirip ayağa kaldırıyor, mock değil): (1) minimal Workflow+Activity+RetryPolicy, (2) Signal tabanlı insan onayı akışı, (3) `OpenAIAgentsPlugin` üzerinden **gerçek bir OpenAI model çağrısı** yapan agent workflow'u. Üçü de beklenen sonucu döndürdü.
- Bu test dokümanda açıkça yazmayan gerçek bir bulgu ortaya çıkardı: `temporalio.openai_agents` modülü taban `temporalio` paketine dahil değil, ayrı `temporalio-openai-agents` paketi gerekiyor. Bu pratik detay (STYLE_GUIDE'ın istediği türden bir "dokümanda yazmayan pratik detay") makaleye eklendi.
- İlk taslakta voice_check 2 hata verdi: 1 "it's not X, it's Y" karşıtlık deseni ve 18 em dash (limit 3). İkisi de düzeltildi, ikinci çalıştırmada PASS.

## Tekrarlayan ortam sorunları (insan onayı hâlâ bekliyor)
- **Detached HEAD — 8. kez art arda** (2026-10-02, 03, 04, 07, 08, 09, 10, 11). Yine `git checkout main && git fetch origin main && git merge --ff-only origin/main` ile düzeltildi, veri kaybı yok.
- **`pip install -q Pillow` yanlış Python'a kuruyor — 6. kez** (2026-10-06 → 11). `python -m pip install -q Pillow` ile düzeltildi.
- Bugün Pazar (review günü değil, Pazartesi). İki bulgu da artık haftalardır tekrarlıyor ve HEARTBEAT.md adım 0'a kalıcı düzeltme olarak işlenmesi öneriliyor; bir sonraki Pazartesi review'da tekrar gündeme getiriyorum.

## Sonraki
- Kuyrukta 3 konu kaldı (CrewAI Flows vs LangGraph Graphs, parallel tool calling, vector database showdown). 5'in altına düştü ama henüz boş değil; HEARTBEAT kuralı gereği TOPIC_SELECTION'ı tetiklemedim, ama yakında (muhtemelen yarın) tetikleyecek.
- Bir sonraki Pazartesi haftalık review'da: (1) detached HEAD ve pip bulgularının HEARTBEAT.md'ye kalıcı düzeltme olarak işlenmesi (8+6 gündür tekrarlıyor); (2) REPORT.md'de biriken ters iç link önerilerinin insan tarafından eski yazılara uygulanıp uygulanmadığının kontrolü.
