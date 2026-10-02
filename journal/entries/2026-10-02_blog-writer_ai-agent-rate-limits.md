# 2026-10-02 · blog-writer · AI Agent Rate Limits

- Yayında: "AI Agent Rate Limits: A Practical Retry Strategy for 429 Errors" — https://www.firstevolvenextscale.com/ai-agent-rate-limits/ (WP ID 1625), kalite kapısından ilk denemede geçti (SEO 12/12, voice_check PASS, İnsan Sesi 8/8).
- Jetpack Facebook + LinkedIn'e paylaştı (Instagram bağlı değil, bilinen kısıt).
- Teknik kaynaklar: Anthropic/OpenAI resmi rate-limit ve hata kodu dokümanları + tenacity dokümantasyonu; üç kod örneği (`tenacity` retry, token bucket, idempotent fingerprint cache) bir venv'de çalıştırılarak doğrulandı.
- Görsel notu: jitter karşılaştırma görseli ilk üretimde kod panelinde bozuk bir etiket içeriyordu ("COITH JITTER)"); basitleştirilmiş prompt ile 1 kez yeniden üretildi, ikincisi temizdi.

## Bulgu: 2026-09-29 ve 2026-10-01 kayıtları eksikti
Bugün 06:00 rutinine başlamadan önce envanteri tazeleyince, sitede 2026-09-29 (CrewAI Unified Memory, WP 1613) ve 2026-10-01 (MCP Context Bloat, WP 1619) tarihli iki yazının zaten **yayında** olduğu görüldü, ama repoda bu günlere ait TOPIC_LOG satırı, journal kaydı, `outputs/` klasörü ya da git commit'i yoktu (git log'da son commit hâlâ 2026-09-28'den). Yani bulut rutini o iki günde çalışıp yazıyı WordPress'e yayınlamış, ama HEARTBEAT adım 5'teki `git add/commit/push` ya hiç tamamlanmamış ya da konteyner commit'ten önce geri dönüştürülmüş — HEARTBEAT.md'nin kendi uyardığı risk ("bulut ortamı her gün sıfırdan başlar, kaydedilmeyen her şey kaybolur") tam olarak gerçekleşmiş.
- Bugün TOPIC_LOG'a bu iki yazı geriye dönük "yayında" olarak eklendi, envanterden gerçek başlık/etiket/slug alındı.
- Kayıp olan: o iki günün REPORT.md'si, görselleri, sources.md'si, sosyal paylaşım metninin tam kaydı — bunlar WordPress'te (medya kütüphanesi, yayınlanmış içerik) hâlâ duruyor, sadece ajanın kendi repo geçmişinde yok.
- **Kullanıcıya not:** Adım 5'in başarıyla tamamlandığını doğrulayan bir kontrol yok (ör. push sonrası `git log` ile commit'in gerçekten uzak repoda olduğunu teyit etmek). Önerilen iyileştirme: HEARTBEAT adım 5'e "push sonrası doğrula" adımı eklemek; yine de bu çalıştırmada riski azaltmak dışında bir aksiyon alınmadı, sadece boşluk kayıt altına alındı.

### Kök neden bulundu ve bugün düzeltildi
Bugünkü commit'i yaparken reponun **detached HEAD** durumunda açıldığı görüldü (`HEAD detached from refs/heads/main`), `main` dalında değil. Bu durumda `git commit` detached HEAD üzerinde yeni bir commit oluşturuyor, `main` dalı ise eski commit'te sabit kalıyor. `git push origin main` komutu, local `main` referansını (hâlâ eski commit) uzak `main`'e gönderiyor — yani "Everything up-to-date" gibi davranıp **hiçbir şey push etmiyor**, hata da vermiyor. Muhtemelen 2026-09-29 ve 2026-10-01 çalıştırmalarında tam olarak bu oldu: yazı yayınlandı, commit detached HEAD'de oluşturuldu, push sessizce no-op geçti, konteyner kapanınca commit kayboldu.
- **Bugün uygulanan düzeltme:** `git checkout main && git merge --ff-only <detached-commit>` ile commit `main`'e taşındı, `git push -u origin main` ile push edildi, ardından `git fetch` + `git rev-parse HEAD` / `origin/main` karşılaştırmasıyla push'un gerçekten uzak repoya ulaştığı doğrulandı.
- **Kalıcı öneri:** HEARTBEAT.md adım 5'e, commit öncesi `git symbolic-ref -q HEAD` ile dal üzerinde olunduğunu kontrol eden (detached ise önce `git checkout main` yapan) ve push sonrası `git fetch` ile uzak repoyu doğrulayan bir adım eklenmeli. Bu çalıştırmada sadece bu oturum için manuel düzeltildi; HEARTBEAT.md dosyası henüz güncellenmedi (insan onayı için bırakıldı).

## Sonraki
- Kuyrukta 5 konu var (sırada ilk: multi-agent tracing/observability — Langfuse/AgentOps).
- Haftalık review (Pazartesi) bu boşluk bulgusunu ve taslak/stil düzeltme oranını değerlendirmeli.
