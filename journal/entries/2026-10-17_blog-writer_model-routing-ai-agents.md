# 2026-10-17 · blog-writer · Model Routing for AI Agents

- **Taslak** (kapıdan geçemedi): "Model Routing for AI Agents: Surviving a Provider Outage" — WP ID 1698, edit: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1698&action=edit. SEO 10/12 (odak kelime başlık/ilk100/H2, meta, slug, 5 iç + 3 dış link, FAQ, 10 etiket hepsi geçti; sadece görsel maddeleri #9/#10 eksik), voice_check PASS, İnsan Sesi 8/8.

## Engel: OPENAI_API_KEY kredisi — **üçüncü gün üst üste**
Bugün de aynı: canlı bir `gpt-4o-mini` chat completion çağrısıyla doğrulandı, `429 insufficient_quota / credit_balance_exhausted`. 2026-10-15, 2026-10-16, 2026-10-17 — üç gün, üç yazı, üçü de aynı nedenle sadece görsel yüzünden taslakta kaldı; SEO/ses/link tarafı üçünde de tam hazır. Bu artık rapor edilecek bir ayrıntı değil, kullanıcıya aktif bildirim gerektiren sürekli bir blokaj. **PushNotification bu oturumda gönderildi.** `content.html` içinde 2 `<!-- TODO (human): ... -->` yorumu sahne önerileriyle hazır.

## Teknik doğrulama (özet)
- `pybreaker` canlı kuruldu; makaledeki circuit-breaker kodu bizzat çalıştırıldı ve çıktı makaledekiyle birebir eşleşti (3 başarısızlıkta devre açılıyor, sonraki çağrılar orijinal hata yerine `CircuitBreakerError` fırlatıyor — makalenin ana pratik bulgusu).
- LiteLLM Router'ın YAML alan adları (`fallbacks`, `context_window_fallbacks`, `content_policy_fallbacks`, `allowed_fails`, `cooldown_time` vb.) resmi dokümandan (docs.litellm.ai) WebFetch ile doğrulandı; YAML bloğu `yaml.safe_load` ile sözdizimi olarak da kontrol edildi. **Canlı bir LiteLLM proxy'ye karşı test edilemedi** — `pip install litellm` bağımlılık çözümü araştırma penceresinde tamamlanmadı (crewai ile aynı ağır bağımlılık deseni, bkz. MEMORY.md 2026-10-12). REPORT.md'de bu fark açıkça "doküman-doğrulamalı, çalıştırma-doğrulamalı değil" diye ayrıştırıldı.
- OpenRouter'ın `models` dizisi ve Anthropic-uçlu `fallbacks` parametresinin 3 kayıt sınırı resmi dokümandan (openrouter.ai/docs) doğrulandı.

## Operasyonel not: ağ hatası sonrası güvenli ikinci deneme
İlk `publish --live` denemesi `GET /tags` adımında geçici bir `ConnectionResetError` ile çöktü — bu adım `POST /posts`'tan önce geliyor, yani hiçbir WP yazısı oluşmadı. Tekrar denemeden önce WP'de slug'ın boş olduğunu `GET /posts?slug=...&status=any` ile teyit ettim, sonra güvenle tekrar denedim; tek bir taslak (1698) oluştu, ikinci yazı yok. MEMORY.md'ye bu istisna (ilk deneme `POST /posts`'a hiç ulaşmadıysa ikinci deneme güvenlidir, teyit şartıyla) not düşüldü.

## Ortam notu: detached HEAD tekrar (4. kez)
Oturum yine `HEAD detached from refs/heads/main` ile başladı (10-14/10-15/10-16 girişlerinde de görülen davranış). `origin/main` ile HEAD aynı commit'teydi, divergence yoktu; `git checkout -B main` ile düzeltildi.
