# Report — 2026-10-18

## Yazı
- **Başlık:** AI Agent Code Execution Sandboxes: E2B vs Modal vs Daytona in 2026
- **Odak anahtar kelime:** ai agent code execution sandboxes
- **Kelime sayısı:** 2.495
- **Durum:** Taslak (kapıdan geçemedi) — WP ID **1699**
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1699&action=edit

## Kalite Kapısı
- `voice_check.py`: **PASS** (sentences=86, mean_len=21.2, stdev=14.1, short=12, flat_triplets=0, em_dash=0)
- İnsan Sesi Testi: **8/8** (yasak kalıp yok, ritim kırık, 5+ uzmanlık sinyali — pratik detay/nftables, trade-off/Firecracker-gVisor, başarısızlık anısı/rmtree, yaygın tavsiyeye itiraz/Daytona, kenar durum/idle-timeout — 2 açık görüş "I'd start with E2B" / "Skip Daytona", conclusion tavsiye niteliğinde, açılış gerçek bir olayla başlıyor)
- **SEO checklist: 10/12** — yalnızca #9 (görsellerde alt text) ve #10 (featured + ≥2 inline görsel) eksik, diğer 10 madde geçti:
  1. ✅ Odak kelime başlıkta
  2. ✅ Odak kelime ilk 100 kelimede
  3. ✅ Odak kelime en az 1 H2'de (2 H2)
  4. ✅ SEO title 58/60 karakter
  5. ✅ Meta description 146/158 karakter, odak kelimeli
  6. ✅ Slug kısa, odak kelimeli (`ai-agent-code-execution-sandboxes`)
  7. ✅ 6 iç link, farklı/açıklayıcı anchor
  8. ✅ 4 dış link, resmî kaynak, utm'siz
  9. ❌ Görsel alt text — görsel yok
  10. ❌ Featured + ≥2 inline görsel — görsel yok
  11. ✅ FAQ, 5 soru
  12. ✅ H1 yok, H2→H3 hiyerarşi düzgün, 10 etiket hazır (odak kelime etiketlerde)

## Engel (4. gün üst üste): OPENAI_API_KEY kredisi tükendi
Bugün de aynı blokaj — hem canlı bir `gpt-4o-mini` chat completion çağrısıyla hem de bizzat `scripts/generate_image.py` çalıştırılarak doğrulandı: `429 insufficient_quota / credit_balance_exhausted`. 2026-10-15, 10-16, 10-17, ve şimdi 10-18 — dört gün, dört yazı, hepsi aynı nedenle sadece görsel yüzünden taslakta kaldı; SEO/ses/link tarafı dördünde de tam hazır. `content.html` içinde 3 `<!-- TODO (human) -->` yorumu, her biri için somut sahne önerisiyle hazır (sandbox/Firecracker-gVisor şeması, gVisor-vs-VM/GPU karşılaştırması, E2B/Modal/Daytona durum şeması). Bu operasyonel engel kullanıcıya **PushNotification ile bildirilecek** (bu artık 2 gün önce de bildirilmiş sürekli bir blokaj).

## İç Linkler (6)
- `agent-control-flow-patterns` — ReAct-style control loop
- `durable-agent-workflows-temporal` — durable agent workflows
- `claude-agent-sdk-vs-openai-agents-sdk` — tool-calling agent framework
- `parallel-tool-calling-llm-agents` — parallel tool calling
- `ai-agent-rate-limits` — retry strategy for 429 errors
- `mcp-context-bloat` — context bloat problem

## Dış Linkler (4, resmî/birincil kaynak, utm'siz)
- https://github.com/e2b-dev/infra (E2B'nin kendi açık kaynak runtime deposu — Firecracker detayının birincil kaynağı)
- https://modal.com/docs/guide/sandbox (Modal resmî Sandbox dokümantasyonu)
- https://github.com/daytonaio/daytona (Daytona'nın kendi deposu — arşivlenmiş/read-only olduğu birebir buradan doğrulandı)
- https://fly.io/learn/firecracker-vs-gvisor.md (Fly.io'nun Firecracker vs gVisor teknik karşılaştırması)

## Teknik Doğrulama (özet)
- E2B: `docs.e2b.dev` (genel SDK kullanımı, `Sandbox.create()`, `commands.run()`) ve `github.com/e2b-dev/infra` (Firecracker microVM + cgroup/network namespace + nftables egress firewall iddiası, repo README'sinden birebir) ile doğrulandı. `docs.e2b.dev/sandbox/lifecycle` sayfasından: varsayılan timeout sayısı yayınlanmamış, sadece maksimumlar (Hobby 1 saat / Pro 24 saat) var — makalede bu fark açıkça "no published default" olarak yazıldı, uydurma bir sayı kullanılmadı.
- Modal: `modal.com/docs/guide/sandbox` resmî sayfasından `runtime="gvisor"|"vm"`, varsayılan 5 dakika ömür, `timeout`/`idle_timeout` parametreleri, GPU'nun sadece gVisor runtime'da desteklendiği birebir doğrulandı.
- Daytona: iddia (2026'da kapalı kaynağa geçiş) üçüncü parti bir blog yazısından (helix.ml) geldi; **kendi GitHub deposuna bakılarak birincil kaynaktan doğrulandı** — repo arşivlenmiş/read-only, README "core development moved to a private codebase" diyor. Üçüncü parti iddia bu şekilde teyit edilmeden makaleye alınmadı.
- Firecracker vs gVisor genel mekanik farkı fly.io'nun kendi teknik yazısından doğrulandı (hardware-virtualized microVM + ayrı guest kernel vs userspace syscall interception).
- **Canlı çağrı yapılamayan kısım:** E2B ve Modal'ın gerçek API'lerine karşı kod örnekleri çalıştırılamadı — bu ajanın E2B_API_KEY veya Modal token'ı yok (yalnızca OPENAI_API_KEY ve WP kimlik bilgileri mevcut, bkz. HEARTBEAT adım 0). Kod örnekleri resmî dokümandaki örneklerle birebir uyumlu yazıldı ve `py_compile` ile sözdizimi doğrulandı (4/4 OK); REPORT'ta bu fark açıkça ayrıştırıldı (2026-10-13 ile aynı yöntem: doküman-doğrulamalı, çalıştırma-doğrulamalı değil).
- Üçüncü parti karşılaştırma bloglarındaki gecikme/cold-start rakamları (ör. "E2B 150ms") makaleye **alınmadı** çünkü kaynaklar birbiriyle çelişiyordu ve resmi dokümanlarda karşılaştırılabilir tek bir sayı yok.

## Ters İç Link Önerisi (insan uygular)
- `agent-control-flow-patterns`: "tool-calling bir ReAct döngüsü çalıştırıyorsanız, kodu nerede çalıştırdığınız da aynı derecede önemli" cümlesiyle bu yeni yazıya link eklenebilir.
- `claude-agent-sdk-vs-openai-agents-sdk`: kod yürütme araçlarından bahsedilen bölüme bu yazıya link eklenebilir.

## Sosyal Paylaşım Metni
Hazır, `post.json` → `social_message` (515 karakter, link + "Link in bio" + tam 6 hashtag). Taslak olduğu için Jetpack paylaşımı **tetiklenmedi**.

## Etiketler (10)
AI Agent Code Execution Sandboxes, E2B, Modal, Daytona, Firecracker MicroVM, AI Agent Security*, Prompt Injection, AI Agent Tools*, Sandbox Isolation, gVisor (*: mevcut etiket yeniden kullanıldı)

## publish-result.json özeti
- `post_id: 1699`, `status: draft`, `rank_math_meta_saved: true`
- `gate_failures`: seo_checklist 10/12; images not visually reviewed; featured image missing; fewer than 2 inline images
- Komut **tek sefer** çalıştırıldı (MEMORY.md kuralı), çıktı `tee` ile `publish-stdout.txt`'e kaydedildi.
