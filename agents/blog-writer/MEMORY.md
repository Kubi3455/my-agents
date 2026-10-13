# Blog Writer Memory

> Yalnızca **onaylanmış** örüntüler. Hipotezler "Denenecek" bölümüne. Haftalık review'da güncellenir.

## Ses (insan düzeltmelerinden öğrenilen)
- 2026-09-27 (kullanıcı kuralı): Yazılar gerçek, samimi bir AI uzmanı yazmış gibi olmalı; yapay zekâ kokusu kabul edilmez. Detaylar: STYLE_GUIDE → "İnsan Sesi". Her yazıda ayrı bir insan sesi revizyon turu zorunlu.

## Konu Seçimi
- 2026-09-27: Son 2 ayın en tutarlı kümesi "agent loops / debugging multi-agent / local LLM". Bu kümede iç link ağı kurmak kolay.

## Yayın
- 2026-09-28 (kullanıcı kararı): Taslak değil otomatik yayın. Güvenlik: script içindeki quality_gate; önce draft, sonra ayrı istekle publish (Jetpack paylaşımı son meta+görselle tetiklensin).
- 2026-09-28: Jetpack REST meta anahtarları doğrulandı: jetpack_publicize_message, jetpack_publicize_feature_enabled, jetpack_social_options, jetpack_social_post_already_shared.

## SEO
- 2026-09-28 (kullanıcı kuralı): Her yazıya SEO ile birlikte yazıya özel 10 etiket. `wp_client.py` → `MAX_TAGS = 10`.
- 2026-09-28: Rank Math tag arşivlerini `noindex, follow` yapıyor; sitemap_index.xml Rank Math'ten geliyor.
- 2026-09-27: Rank Math meta alanları varsayılan olarak REST'te yazılamaz; `data/imports/HOW_TO_SETUP.md` snippet'i şart.
- 2026-09-27: API'ye her zaman `www.` ile istek at; www'suz adres 301 yönlendiriyor ve POST'ta Authorization düşüyor.
- 2026-10-07: `wp_client.py`'nin `quality_gate`'i odak kelime/başlık eşleşmesini literal substring ile kontrol ediyor (tire/boşluk normalize etmiyor). Odak kelimeyi kuyruğa boşluklu değil, başlıkta kullanılacak gerçek yazımla (örn. "long-term memory" tireli) kaydetmek veya yazarken başlığın tam yazımına göre revize etmek gerekiyor; aksi halde `--live` kapıdan "focus keyword missing from title" ile döner ve bir taslak post + kullanılmayan etiket yaratıp bırakır (script var olan taslağı güncelleyen bir komut sunmuyor, bkz. 2026-10-07 REPORT.md/journal — insan onayı bekleyen script iyileştirme önerisi).

## Görsel
- 2026-09-28: Detaylı prompt + featured `high` ile v2 kapak: numaralı adım başlıkları, lejant kutusu, tüm yazılar doğru. Hedef standart bu seviye (kullanıcı yayınladı = onaylandı). PNG 1.9 MB → JPEG 127 KB.
- 2026-09-28 (kullanıcı geri bildirimi): İlk seri "çok basit" bulundu. Artık detaylı, konuyu anlatan infografik sahneler + 2–4 kısa etiket; featured high kalite.
- 2026-09-28: gpt-image-2 (1536x1024, medium) prompt'taki "no text, no letters, no numbers" ile temiz çıktı verdi; 3/3 ilk denemede kabul.
- 2026-09-28: optimize_image.py ile PNG 1.5–1.7 MB → WebP 16–27 KB, gözle kayıp yok.

- 2026-10-02: İki panelli "karşılaştırma" sahnelerinde (ör. A vs B) model bazen sahte/bozuk kod panelleri ekliyor ("COITH JITTER)" gibi anlamsız başlıklar). Prompt'a "no embedded code panels" eklemek ve sahneyi ikona/metrik kartlarına yönlendirmek temiz sonuç verdi (1 yeniden üretimde düzeldi).
- 2026-10-04: "Threshold/risk tuning" gibi soyut kavram sahnelerinde model bazen konuyu tamamen başka bir alana kaydırıyor (ör. "semantic caching" isteği "kullanıcı kimlik/fraud eşleştirme" sahnesine dönüştü: User ID/Email/Device/Location kartları). Metin kendi içinde doğru yazılmış olsa da makalenin konusunu yansıtmıyor. Prompt'a konuyla ilgili somut negatif kısıtlar eklemek ("NOT about X, no user profiles/emails/device fields, only Y") sapmayı 1 denemede düzeltti. Soyut/çok genel sahne tarifleri (sadece "risk tuning", "comparison" gibi) bu sapmaya daha yatkın; sahneyi makalenin asıl nesneleriyle (burada: soru-cevap balonları) açıkça sınırlamak gerekiyor.
- 2026-10-09: Belirli, isimlendirilmiş bir süreç/pipeline'ı (ör. "6 adımlı izin değerlendirme sırası: hooks, deny rules, ask rules, permission mode, allow rules, callback") görselleştirirken prompt'ta sadece "altı adımlı bir pipeline çiz" gibi genel bir tarif yeterli olmuyor — model kulağa makul gelen ama makale metnindeki gerçek adım isimleriyle çelişen uydurma etiketler üretiyor (ör. "Intent Check", "Policy Check", "Rate Limit Check", "Audit Check" — hiçbiri gerçek API/doküman terimi değil). Bu, "yanlış yazım" değil "yanlış ama akıcı okunan teknik terim" sınıfı bir hata; IMAGE_GENERATION kontrolünde sadece yazım değil, makale metniyle birebir terim eşleşmesi de kontrol edilmeli. Düzeltme: prompt'a adım isimlerini tam ve sırayla, "bundan başka adım/terim ekleme" talimatıyla birlikte yazmak 1 denemede düzeltti.

## Teknik Doğrulama
- 2026-10-12: `pip install crewai` (bağımlılıksız değil, tam) bağımlılık çözücüde ağır backtracking'e giriyor (chromadb/opentelemetry/lancedb gibi sıkı sürümlenmiş büyük bir ağaç); ~20 dakikada tek paket kurmadan iptal edildi. Çözüm: `pip install --no-deps crewai`, sonra gerçek `ModuleNotFoundError` zincirini tek tek `pip install --no-deps <modül>` ile takip et (crewai + LangGraph gibi iki ağır paketi aynı venv'de birlikte kurmaya çalışmak yerine). Bilinen PyPI paket adı ≠ import adı uyuşmazlıkları bu süreçte çıktı: `python-dotenv` (dotenv değil), `rpds-py` (rpds değil), `PyJWT` (jwt değil, "jwt" adlı ayrı/yanlış bir paket var), `python-dateutil` (dateutil değil). `opentelemetry-exporter-otlp-proto-http` ve `...-common` gibi birbirine sıkı bağımlı kardeş paketleri `--no-deps` ile ayrı ayrı kurmak sürüm uyuşmazlığı yaratıyor; bu ikisini birlikte (depslı) kurmak gerekti. Sonuç: güncel `crewai==1.15.27` çalışır hâle geldi ve gerçek `Flow.kickoff()` çalıştırılabildi.
- 2026-10-12: LangGraph'ta `add_conditional_edges()`'in `path_map`'inde olmayan bir route değeri, grafiği kurarken (`add_conditional_edges()`/`.compile()`) değil, **o kenar ilk çalıştığında** (`invoke()` sırasında) `KeyError` fırlatıyor. "Build-time/construction-time kontrol" gibi ifadeler kullanmadan önce bunu gerçek bir `invoke()` çağrısıyla doğrula; üçüncü parti karşılaştırma bloglarının "graph construction'da kontrol edilir" ifadesi yanlış çıktı.
- 2026-10-12: CrewAI Flow'da `@router()`'ın döndürdüğü string ile `@listen("...")`'in beklediği string birebir (case-sensitive, normalize edilmeyen) eşleşmezse hiçbir hata/uyarı/log olmadan o dal sessizce hiç çalışmıyor (`crewai/flow/runtime/__init__.py` → `_condition_satisfied`: düz `in` operatörü). Gerçek `kickoff()` çalıştırmasıyla doğrulandı (stdout/stderr'de error/warn/fail/exception geçen tek satır yok).
- 2026-10-13: Anthropic API anahtarı ortamda olmayan bir oturumda Claude'a özgü bir API alanını (ör. `disable_parallel_tool_use`) doğrulamanın güvenilir yolu: canlı çağrı yapamasan bile `pip install anthropic` ile kurulu SDK'nın kendi tip tanımlarına (`from anthropic.types.X import Y; Y.__annotations__`) bakmak, sadece resmi dokümana güvenmemek. OpenAI tarafında ise gerçek anahtar varsa (`OPENAI_API_KEY`), iddiayı doğrudan küçük/ucuz bir modelle (`gpt-4o-mini`) canlı çağırıp davranışı bizzat gözlemlemek dokümana atıftan daha güçlü bir doğrulama — bu makalede ikisi birden yapıldı (OpenAI canlı test, Claude SDK tip doğrulaması), REPORT.md'de hangisinin hangi yöntemle doğrulandığı açıkça ayrıştırıldı.
- 2026-10-13: Paylaşılan durumda (shared state) race condition içeren bir teknik iddiayı ("parallel tool calls birbirini ezebilir") kanıtlamanın en güçlü yolu üçüncü parti kaynak alıntılamak değil, minimal bir Python `threading` scriptiyle hatayı bizzat yeniden üretmek (okuma ile yazma arasına yapay bir `time.sleep` koyarak yarışı güvenilir şekilde tetikleyip beklenenden farklı bir sonuç gözlemlemek), sonra aynı senaryoyu `threading.Lock` + idempotency-key seti ile düzeltilmiş haliyle tekrar çalıştırıp doğru sonucu doğrulamak. İki script de makaleye gerçekten çalıştırılmış haliyle kondu.

## Denenecek (Hipotezler)
- FAQ bölümü olan yazılar daha fazla gösterim alıyor mu? (Search Console verisi gelince test et)
- Başlıkta yıl ("2026") CTR'yi artırıyor mu?
