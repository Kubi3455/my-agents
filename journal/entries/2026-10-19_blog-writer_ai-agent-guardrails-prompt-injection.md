# 2026-10-19 — blog-writer: AI Agent Guardrails for Prompt Injection

Taslak kaldı (post 1701), nedeni teknik değil operasyonel: `OPENAI_API_KEY` kredisi **5. gündür**
üst üste tükendi (10-15, 16, 17, 18, 19 — hepsi canlı çağrıyla doğrulandı, `429
insufficient_quota/credit_balance_exhausted`). Yazının/SEO'nun/linklerin tamamı hazır: voice_check
PASS, İnsan Sesi 8/8, SEO 10/12 (sadece görsel maddeleri #9/#10 eksik), 5 iç + 4 dış resmi link,
10 etiket çözüldü. content.html'de 3 `<!-- TODO (human) -->` yorumu, her biri somut sahne
öneriyle.

Teknik doğrulama: OpenAI Agents SDK'nin guardrail API'si (hem input/output hem tool guardrails)
hem resmi dokümandan hem de kurulu `openai-agents` paketinin kendi kaynak kodundan
(`agents/tool_guardrails.py`) doğrulandı; gerçek bir `tool_output_guardrail` yazılıp poisoned/clean
iki sahte tool çıktısına karşı bizzat çalıştırıldı (model çağrısı gerekmedi, guardrail fonksiyonu
saf Python). Anthropic'in indirect-injection deseni (tool_result izolasyonu, JSON encoding, ucuz
model ile tool output tarama) canlı `platform.claude.com` sayfasından doğrulandı. Bulgu: birkaç
2026 güvenlik blogu OWASP'ın "2026 sürümü"nden bahsediyor (Excessive Agency #3'e çıkmış) ama
OWASP'ın kendi `genai.owasp.org/llm-top-10/` sayfası hâlâ 2025 sürümünü gösteriyor — makale bu
tutarsızlığı açıkça not düşüyor, doğrulanmamış iddiayı gerçek diye yazmadı.

**Operasyonel durum (değişmedi):** Beşinci gün, beşinci yazı (10-15, 16, 17, 18, 19 — post 1694,
1696, 1698, 1699, 1701) aynı nedenle taslakta. Ajan tarafında yapılabilecek bir şey yok; insanın
OpenAI faturalandırmasına kredi eklemesi gerekiyor. Bu oturumda PushNotification ile bildirildi.
