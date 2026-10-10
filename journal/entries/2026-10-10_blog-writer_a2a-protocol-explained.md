# 2026-10-10 · blog-writer · A2A Protocol Explained

- Yayında: "A2A Protocol Explained: How AI Agents Talk to Each Other" — https://www.firstevolvenextscale.com/a2a-protocol-explained/ (WP ID 1668), kalite kapısından ilk denemede geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8.
- Kuyruktaki ilk konu alındı (A2A protocol). Web aramasıyla güncelliği doğrulandı: A2A, 2026-08-17'de Agentic AI Foundation'a (AAIF) hosted project olarak taşındı ve spesifikasyon v1.0.0'a ulaştı — konu kuyruğa eklendiğinden (2026-10-09) bu yana bile daha güçlü bir "neden şimdi" kancası oluştu. Orijinal kuyruk odak kelimesi "a2a protocol for ai agents" başlıkta birebir geçmeyeceği için (2026-10-07'deki literal substring dersi), odak kelimeyi başlıkla uyumlu "a2a protocol"e revize ettim.
- 5 iç link (mcp-context-bloat, debugging-multi-agent-workflows, agent-tracing-observability, human-in-the-loop-for-ai-workflows, claude-agent-sdk-vs-openai-agents-sdk), 3 dış resmi link (a2a-protocol.org spesifikasyonu, a2a-python GitHub kaynağı, aaif.io resmi duyurusu), 10 etiket, 1 JPEG featured + 3 WebP inline görsel (4/4 ilk denemede kabul, yeniden üretim yok).

## Teknik doğrulama yöntemi: ikincil kaynak yerine birincil kaynak + çalıştırılmış kod
Bu konu özellikle risk taşıyordu çünkü A2A spesifikasyonu ve `a2a-sdk` paketi 2026 içinde hızlı değişti (0.3 → 1.0), ve web aramasındaki ikincil blog/tutorial kaynakları birbiriyle çelişiyordu (sürüm numaraları, "Linux Foundation" vs "Agentic AI Foundation" governance iddiaları, API şekilleri). Bunun yerine:
- Teknik iddialar yalnızca resmi A2A spesifikasyonundan (`a2a-protocol.org`) ve AAIF'in kendi duyurusundan (`aaif.io`, tarihli) alındı.
- `a2a-sdk` API'si bir blog yazısından değil, **kurulu paketin kendisinden** (yerel bir venv'e `pip install a2a-sdk[fastapi]` ile kurulup `inspect`/`DESCRIPTOR.fields` ile) doğrudan okunarak doğrulandı. Bu, 2026-10-08'deki "tutorial deprecated fonksiyon öğretiyor" bulgusunun bir üst seviyesi: burada tutorial'lar sadece eski değil, kullandıkları sınıf (`A2AStarletteApplication`) paketten tamamen kaldırılmıştı.
- Makaledeki kod örneği yerel bir venv'de FastAPI `TestClient` ile gerçek bir A2A sunucusuna karşı uçtan uca çalıştırıldı. İki "gotcha" (A2A-Version header eksikse 400 reddi; eski `url=` kwarg'ının artık `ValueError` vermesi) kendi ortamımda bizzat yeniden üretildi, tahmin edilmedi.

## Tekrarlayan ortam sorunları (insan onayı hâlâ bekliyor)
- **Detached HEAD — 7. kez art arda** (2026-10-02, 03, 04, 07, 08, 09, 10). Bugün yine local `main` origin'in gerisindeydi (5 commit). `git checkout main && git fetch origin main && git merge --ff-only origin/main` ile düzeltildi, veri kaybı yok. Öneri (HEARTBEAT.md'ye commit öncesi/sonrası dal kontrolü eklenmesi) artık **7 gündür** insan onayı bekliyor.
- **`pip install` yanlış Python'a kuruyor — 5. kez** (2026-10-06, 07, 08, 09, 10). `python -m pip install -q Pillow` ile düzeltildi. Bu bulguyu her gün tekrar yazmak yerine bir sonraki Pazartesi haftalık review'da HEARTBEAT.md adım 0'a kalıcı olarak işlenmesini öneriyorum; bugün Cumartesi, review günü değil.

## Sonraki
- Kuyrukta 4 konu kaldı (Temporal durable workflows, CrewAI Flows vs LangGraph, parallel tool calling, vector database showdown).
- Bir sonraki Pazartesi haftalık review'da: (1) detached HEAD ve pip bulgularının HEARTBEAT.md'ye kalıcı düzeltme olarak işlenmesi, 7+5 gündür tekrarlıyor; (2) REPORT.md'de biriken ters iç link önerilerinin insan tarafından eski yazılara uygulanıp uygulanmadığının kontrolü.
