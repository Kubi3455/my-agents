# 2026-10-16 · blog-writer · Evaluating AI Agents Before Production

- **Taslak** (kapıdan geçemedi): "Evaluating AI Agents Before Production: What Catches Real Failures" — WP ID 1696 (canonical), edit: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1696&action=edit. SEO 10/12 (odak kelime başlık/ilk100/H2, meta, slug, 5 iç + 4 dış link, FAQ, 10 etiket hepsi geçti; sadece görsel maddeleri #9/#10 eksik), voice_check PASS, İnsan Sesi 8/8.

## Engel: OPENAI_API_KEY kredisi — ikinci gün üst üste
Dün (2026-10-15) tükenen kredi bugün de aynı: canlı bir `gpt-4o-mini` chat completion çağrısıyla doğrulandı, `429 insufficient_quota / credit_balance_exhausted`. IMAGE_GENERATION yine tamamen bloke; akışın geri kalanı (TOPIC_SELECTION → SOCIAL_SHARE) tamamlandı, kapı beklendiği gibi görsel maddeleri yüzünden reddetti. `content.html` içinde 3 `<!-- TODO (human): ... -->` yorumu sahne önerileriyle hazır. **Bu artık tek seferlik bir arıza değil, iki gündür süren bir blokaj — insanın OpenAI faturalandırmasına kredi eklemesi gerekiyor.**

## Operasyonel hata: kazara ikinci taslak (post 1697)
`wp_client.py publish --live` komutunu çıktıyı dosyaya kaydetmek için ikinci kez çalıştırdım. Script var olan taslağı güncelleyen bir komut sunmadığı için (2026-10-07'den bilinen eksiklik) bu, post 1696'dan tamamen bağımsız **yeni bir taslak (post 1697) + 10 fazladan kullanılmayan etiket** yarattı. Post 1696 canonical olan; **insan post 1697'yi WP admin'den çöpe taşımalı**. MEMORY.md'ye "publish --live'ı asla ikinci kez çalıştırma" kuralı eklendi.

## Teknik bulgu: AgentEvals'ın `superset` modu tekrarlı tool-call'ı yakalamıyor
`agentevals` 0.0.9 temiz bir venv'de gerçek çalıştırıldı. Aynı (tekrarlı/güvensiz `issue_refund` çağrısı içeren) trajectory iki modda da test edildi: `trajectory_match_mode="unordered"` doğru şekilde `score: False` veriyor, ama `trajectory_match_mode="superset"` aynı girdide `score: True` döndürüyor — yani referans çağrıların üstüne eklenen fazladan/tekrarlı bir çağrıyı hiç yakalamıyor. Bu, dokümanda yazmayan, bizzat bulunan bir gotcha ve makalenin ana pratik bulgusu oldu (MEMORY.md'ye de eklendi).

## Teknik doğrulama (özet)
Anthropic'in resmi "Demystifying evals for AI agents" makalesi WebFetch ile **birincil kaynaktan** okundu (ikincil blog özetlerine güvenilmedi): transcript tanımı, outcome/transcript grading ayrımı, 20-50 vaka önerisi, pass@k/pass^k tanımları, git-history "haksız avantaj" anekdotu birebir doğrulandı. OpenAI'nin "Trace grading" sayfası da WebFetch ile okundu; ikincil kaynaklardaki "legacy API" iddiası birincil sayfada doğrulanamadığı için makaleye alınmadı. `create_trajectory_llm_as_judge` canlı çağrılmadı (kredi yok); imza/rubric paketin kaynağından doğrulandı, makalede açıkça belirtildi. `0.95 ** 8 ≈ 0.6634` bizzat hesaplandı.

## Ortam notu: detached HEAD tekrar
Bu oturum da `HEAD detached from refs/heads/main` durumunda başladı (2026-10-14/15 girişlerinde de görülen aynı davranış). Bu sefer `origin/main` zaten HEAD ile aynı commit'teydi (önceki 3 commit başarıyla push edilmiş), sadece local `main` dalı HEAD'e bağlı değildi. `git checkout -B main` ile düzeltildi, divergence yoktu. Bu ortamın her oturum başında tekrarlayan bir davranışı gibi görünüyor.
