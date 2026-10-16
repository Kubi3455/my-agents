# Report — 2026-10-16

## Yazı
- **Başlık:** Evaluating AI Agents Before Production: What Catches Real Failures
- **Odak kelime:** evaluating ai agents before production
- **Kelime sayısı:** 2.656 (kod blokları hariç)
- **Durum:** TASLAK (kalite kapısı geçmedi — bkz. aşağı)
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1696&action=edit (canonical taslak, post_id 1696)

## ⚠️ Script hatası: kazara ikinci bir taslak oluştu (post_id 1697)
`wp_client.py publish` komutunu ilk kez çalıştırdım (post 1696 oluştu, kapı beklenen şekilde reddetti). Çıktıyı dosyaya kaydetmek için komutu **ikinci kez** çalıştırdım — script'in var olan taslağı güncelleyen bir komutu olmadığı için (bkz. MEMORY.md 2026-10-07 notu, aynı sorun) bu ikinci çalıştırma **yeni bir taslak (post_id 1697)** ve 10 **kullanılmayan etiket** daha yarattı; 1697'nin kendi kapı hatası listesine de "slug already used by post 1696" eklendi. Bu benim hatam (komutu tekrar çalıştırmak), script eksikliği değil bu kez — ama sonucu aynı: iki taslak + fazladan etiketler oluştu.
- **İnsan aksiyonu gerekiyor:** WP admin'den **post 1697'yi çöpe taşıyın** (1696 canonical olan, tüm metaveri ve içerik orada). Bu ajan mevcut/kendi oluşturduğu yazıları silme yetkisine sahip değil (RULES.md).
- **Öğrenilen ders (MEMORY.md'ye eklendi):** `wp_client.py publish --live` komutunu *asla* ikinci kez çalıştırma, komut çıktısını kaybetsen bile. Çıktı kayboldu ise WP admin'den post'u elle kontrol et, tekrar publish deneme.

## Kalite Kapısı Sonucu
`gate_failures`:
1. `seo_checklist 10/12` — eksik olan 2 madde: #9 (görsellerde odak kelimeli alt text — görsel yok) ve #10 (featured + ≥2 inline görsel — hiç görsel yok)
2. `images not visually reviewed`
3. `featured image missing or not JPEG`
4. `fewer than 2 inline images`

**Neden görsel yok:** `OPENAI_API_KEY` ortam değişkeni set ama **kredisi tükenmiş** — hem düz bir `chat.completions` çağrısı hem de `generate_image.py` (gpt-image-2) aynı `429 insufficient_quota / credit_balance_exhausted` hatasını verdi (canlı olarak doğrulandı, bkz. aşağı). Bu, 2026-10-15'teki aynı sorunun devamı — **iki gündür** kredi yok. `sources.md` ve `content.html` içindeki `<!-- TODO (human): ... -->` yorumları, her görsel için önerilen sahne tarifini içeriyor; insan kredi ekleyip `generate_image.py` + `optimize_image.py` çalıştırıp görselleri ekledikten sonra taslağı (post 1696) tamamlayabilir.

**Diğer 10/12 madde hazır:**
- Odak kelime başlıkta, ilk 100 kelimede, 1 H2'de ✓
- SEO title 51 karakter, meta description 157 karakter (odak kelimeli) ✓
- Slug boşta, odak kelimeli, 5 kelime ✓
- 5 iç link (agent-tracing-observability, agent-control-flow-patterns, durable-agent-workflows-temporal, parallel-tool-calling-llm-agents, mcp-context-bloat), her biri açıklayıcı farklı anchor ✓
- 4 dış resmi link (anthropic.com, github.com/langchain-ai/agentevals, docs.langchain.com, developers.openai.com), utm'siz ✓
- FAQ bölümü (5 soru) ✓
- H2/H3 hiyerarşisi atlamasız (11 H2, 8 H3), H1 yok ✓
- 10 etiket hazır ✓

## voice_check.py
`PASS` — `sentences=96 mean_len=23.2 stdev=14.6 short(<=6w)=9 flat_triplets=2 em_dash=0`

## İnsan Sesi Testi: 8/8
1. Yasak kalıp/kelime: temiz (voice_check PASS) ✓
2. Art arda 3 eş uzunlukta cümle: flat_triplets=2/96 (%2, eşik %15) ✓
3. Uzmanlık sinyalleri (≥4): "superset" modunun tekrarlı çağrıyı yakalamadığı keşfi (dokümanda yok), trade-off (exact match vs LLM judge maliyeti), başarısızlık anlatısı (çift refund), gerçek komut çıktısı (`0.95 ** 8`, gerçek `agentevals` çıktıları), yaygın tavsiyeye itiraz (superset'i güvenlik-kritik testlerde kullanma) — 5 sinyal ✓
4. Açık görüş/tavsiye (≥2): "I'd skip the instinct…", "I'd default to trajectory matching…", "Reach for unordered or strict…" — 3+ ✓
5. Conclusion tavsiye (özet değil): evet, somut aksiyon öneriyor ✓
6. Açılış gerçek durumla başlıyor: evet (çift refund anekdotu) ✓
7/8. Sesli okuma / meslektaş testi: evet, kişisel ses ve dürüst caveat'lar (OpenAI kredisi, LLM judge canlı test edilmedi) var ✓

## Teknik Doğrulama
- `agentevals` 0.0.9 temiz bir venv'e (`/tmp/evalcheck_venv`) kurulup gerçek kodlar çalıştırıldı (bkz. `sources.md`).
- **Gerçek bulgu (dokümanda yazmıyor):** `create_trajectory_match_evaluator(trajectory_match_mode="superset")`, referans çağrıların üstüne eklenen tekrarlı/güvensiz bir `issue_refund` çağrısını **yakalamıyor** (`score: True`), aynı senaryoda `"unordered"` modu doğru şekilde yakalıyor (`score: False`). Bu makalenin ana pratik bulgusu, bizzat her iki modu da çalıştırarak doğrulandı.
- `0.95 ** 8 = 0.6633956609125211` bizzat hesaplandı.
- Anthropic'in resmi "Demystifying evals for AI agents" makalesi WebFetch ile birincil kaynaktan okundu (ikincil özetlere güvenilmedi); transcript tanımı, outcome/transcript grading ayrımı, 20-50 vaka önerisi, pass@k/pass^k tanımları ve git-history "haksız avantaj" anekdotu birebir doğrulandı.
- OpenAI'nin "Trace grading" sayfası da WebFetch ile birincil kaynaktan okundu; "legacy API" iddiası doğrulanamadığı için makaleye **alınmadı**.
- `create_trajectory_llm_as_judge` canlı çağrılmadı (OpenAI kredisi yok); imza ve rubric metni kurulu paketin kaynağından doğrulandı, makalede bu açıkça belirtildi (dürüstlük).

## Ters İç Link Önerisi (eski yazılara eklenebilir, insan uygular)
- `agent-tracing-observability` yazısına: "...and once you have that trace, you can grade it — see [evaluating AI agents before production](https://www.firstevolvenextscale.com/evaluating-ai-agents-before-production/) for how." cümlesi eklenebilir.
- `agent-control-flow-patterns` yazısına: ReAct/Plan-and-Execute karşılaştırmasının sonunda, her iki control flow'un da trajectory testi gerektirdiğine dair bir not + link eklenebilir.

## TOPIC_LOG
Konu `taslak` olarak işaretlendi (post_id 1696, 1697 kazara duplicate — bkz. yukarı).
