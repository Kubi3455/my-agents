# 2026-10-18 · blog-writer · AI Agent Code Execution Sandboxes

- **Taslak** (kapıdan geçemedi): "AI Agent Code Execution Sandboxes: E2B vs Modal vs Daytona in 2026" — WP ID 1699, edit: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1699&action=edit. SEO 10/12 (odak kelime başlık/ilk100/H2, meta, slug, 6 iç + 4 dış link, FAQ, 10 etiket hepsi geçti; sadece görsel maddeleri #9/#10 eksik), voice_check PASS, İnsan Sesi 8/8.

## Engel: OPENAI_API_KEY kredisi — **dördüncü gün üst üste**
Bugün de aynı: hem bir `gpt-4o-mini` chat completion çağrısıyla hem de bizzat `generate_image.py` çalıştırılarak doğrulandı, ikisi de `429 insufficient_quota/credit_balance_exhausted`. 2026-10-15, 10-16, 10-17, 10-18 — dört gün, dört yazı, hepsi aynı nedenle sadece görsel yüzünden taslakta kaldı; SEO/ses/link tarafı dördünde de tam hazır. `content.html` içinde 3 `<!-- TODO (human): ... -->` yorumu sahne önerileriyle hazır. **PushNotification bu oturumda da gönderildi** (kredi insan tarafından eklenmeden bu blokaj her gün tekrar edecek).

## Teknik doğrulama (özet)
- E2B'nin Firecracker microVM iddiası kendi açık kaynak deposundan (`github.com/e2b-dev/infra` README'si) birebir doğrulandı — genel `docs.e2b.dev` sayfası bu implementasyon detayını vermiyor.
- Modal'ın gVisor/VM runtime seçimi, varsayılan 5 dakikalık ömür ve GPU'nun sadece gVisor runtime'da desteklendiği resmi `modal.com/docs/guide/sandbox` sayfasından doğrulandı.
- Üçüncü parti bir blogun "Daytona 2026'da kapalı kaynağa geçti" iddiası doğrudan Daytona'nın kendi GitHub deposuna bakılarak teyit edildi: repo arşivlenmiş/read-only, README "core development moved to a private codebase" diyor. Doğrulanmadan makaleye alınmadı.
- E2B/Modal'ın gerçek bulut API'lerine karşı kod çalıştırılamadı (bu ajanda o servislere ait API anahtarları yok, yalnızca OPENAI_API_KEY ve WP kimlik bilgileri mevcut). Kod örnekleri resmi dokümanla birebir uyumlu yazıldı ve `py_compile` ile sözdizimi doğrulandı (4/4 OK); REPORT.md'de bu fark açıkça ayrıştırıldı.
- Vendor karşılaştırma bloglarındaki çelişen cold-start/gecikme rakamları (örn. "E2B 150ms") makaleye alınmadı; resmi dokümanlarda karşılaştırılabilir tek bir sayı yok.

## Operasyonel not: detached HEAD tekrar (5. kez)
Oturum yine `HEAD detached from refs/heads/main` ile başladı. `origin/main` ile aynı commit'teydi, divergence yoktu; `git fetch origin main && git checkout -B main origin/main` ile düzeltildi.

## Kuyruk durumu
Bugünün konusu alındıktan sonra kuyrukta 1 konu kaldı ("Guardrails for AI Agents"). Kuyruk boşalmadığı için HEARTBEAT kararına göre yeni TOPIC_SELECTION turu çalıştırılmadı.
