# Report — 2026-10-09

## Yayın
- **Başlık:** Claude Agent SDK vs OpenAI Agents SDK: A 2026 Comparison
- **Odak kelime:** claude agent sdk vs openai agents sdk
- **Durum:** yayında (ilk `--live` denemesinde geçti, `gate_failures: []`)
- **WP ID:** 1662
- **Canlı link:** https://www.firstevolvenextscale.com/claude-agent-sdk-vs-openai-agents-sdk/
- **Düzenleme linki:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1662&action=edit
- **Kelime sayısı:** ~2.162

## Kalite Kapısı
- SEO checklist: 12/12 (detay aşağıda)
- voice_check.py: PASS (em_dash=0, flat_triplets=1/79, stdev=11.1)
- İnsan Sesi Testi: 8/8 (self-assessment, detay aşağıda)
- Görseller: 4/4 Read ile açılıp kontrol edildi, 1 yeniden üretim (inline-2, aşağıda)

## SEO Checklist (12/12)
1. Odak kelime başlıkta ✓ ("Claude Agent SDK vs OpenAI Agents SDK: A 2026 Comparison")
2. Odak kelime ilk 100 kelimede ✓ (doğrulandı, python ile kontrol edildi)
3. Odak kelime en az bir H2'de ✓ (2 H2'de: "Two Different Mental Models" ve "Side-by-Side")
4. SEO title ≤60 karakter ✓ (56)
5. Meta description 140-158 karakter ve odak kelimeli ✓ (142, kelime içeriyor)
6. Slug kısa ve odak kelimeli ✓ (`claude-agent-sdk-vs-openai-agents-sdk`)
7. 6 iç link, farklı ve açıklayıcı anchor'lar ✓ (aşağıda liste; hedef 4-6'nın üst sınırında)
8. 4 dış resmi link, utm'siz ✓ (code.claude.com x2, openai.github.io x2)
9. Tüm görsellerde odak/ilgili kelimeli alt text ✓
10. Featured (JPEG) + 3 inline (WebP) ✓
11. FAQ bölümü, 5 soru ✓
12. H1 yok, H2→H3 hiyerarşisi atlamasız, 10 etiket hazır, odak kelime terimleri etiketlerde (`Claude Agent SDK`, `OpenAI Agents SDK`) ✓

## İç Linkler (6)
- `/agent-control-flow-patterns/` — "plan its own steps" (intro, ilk 100 kelime içinde)
- `/autogpt-vs-crewai-vs-langgraph/` — "comparing AutoGPT, CrewAI, and LangGraph"
- `/mcp-context-bloat/` — "bloating your agent's context window"
- `/agent-tracing-observability/` — "tracing gives you a visual run-through"
- `/debugging-multi-agent-workflows/` — "handoff chain starts looping"
- `/human-in-the-loop-for-ai-workflows/` — "human-in-the-loop check"

## Dış Linkler (4, resmi dokümantasyon)
- https://code.claude.com/docs/en/agent-sdk/subagents
- https://code.claude.com/docs/en/agent-sdk/permissions
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/

## Ters İç Link Önerisi (eski yazılara, insan uygular)
- `agent-control-flow-patterns` yazısına, "delegation patterns" bahsi geçen yerde bu yeni yazıya link eklenebilir ("see how Claude's subagents and OpenAI's handoffs compare" gibi bir cümleyle)
- `debugging-multi-agent-workflows` yazısına, framework seçimi bahsi geçen bir yere bu karşılaştırmaya link verilebilir
- `mcp-context-bloat` yazısına, subagent context isolation bahsi varsa bu yazıya link eklenebilir

## Teknik Doğrulama
Tüm SDK iddiaları (`sources.md`'de linkler) resmi dokümantasyondan WebFetch ile bugün doğrulandı:
- Claude Agent SDK: `query()`, `ClaudeAgentOptions`, `AgentDefinition`, `Agent` tool adı (eski `Task`), varsayılan concurrency 20 / depth 3, `max_budget_usd`, 6 adımlı izin pipeline'ı (hooks → deny → ask → mode → allow → callback), permission modları (`default`, `dontAsk`, `acceptEdits`, `bypassPermissions`, `plan`, `auto`)
- OpenAI Agents SDK: `Agent`, `Runner.run_sync`, `handoff()` parametreleri (`tool_name_override`, `on_handoff`, `input_type`, vb.), varsayılan tool adı `transfer_to_<agent_name>`, `@input_guardrail`/`@output_guardrail`, `GuardrailFunctionOutput`, `InputGuardrailTripwireTriggered`
- Kod örnekleri resmi quickstart/handoffs/guardrails sayfalarından birebir uyarlandı, uydurma fonksiyon/parametre yok
- Belirsiz/çelişkili bilgiler (SDK'ların kesin yayın tarihleri, rakip blog kaynaklarında tutarsızdı) makaleye **dahil edilmedi** — yalnızca resmi dokümanlardan doğrulanabilen teknik içerik kullanıldı

## Görsel Notu
İlk üretimde `permissions-guardrails` inline görseli, Claude'un gerçek 6 adımlı izin pipeline'ını (hooks/deny/ask/mode/allow/callback) yanlış/uydurma adım isimleriyle ("Intent Check", "Policy Check", "Rate Limit Check" vb.) göstermişti — makale metnindeki gerçek adımlarla çelişiyordu. Prompt'a adımların birebir listesi eklenerek 1 denemede düzeltildi (bkz. MEMORY.md "Görsel", yeni bir örüntü olarak eklendi).

## Sosyal Paylaşım Metni
Şablona uygun (611 karakter, link + "On Instagram? Link in bio." + tam 6 hashtag: #ClaudeAgentSDK #OpenAIAgentsSDK #MultiAgentSystems #Python #AIAgents #AIEngineering). Yayın anında Jetpack Social FB/IG/LinkedIn'e paylaştı.

## Tekrarlayan Ortam Sorunları (bu oturumda da görüldü)
- **Detached HEAD — 6. kez.** Oturum HEAD'i yine detached açıldı, ancak bu kez `origin/main`'in **kendisi** zaten 10-05/10-06/10-07/10-08 commit'lerini taşıyordu (local `main` dalı geride kalmıştı, veri kaybı yoktu). `git checkout main && git merge --ff-only` + push ile doğrulandı. HEARTBEAT.md'ye önerilen "commit öncesi/sonrası dal kontrolü" adımı **6 gündür** (2026-10-02, 03, 04, 07, 08, 09) insan onayı bekliyor.
- **`pip install` yanlış Python'a kuruyor — 4. kez** (2026-10-06, 07, 08, 09). `python -m pip install -q Pillow` ile düzeltildi.

## Sonraki
- Kuyrukta 5 yeni konu var (A2A protocol, Temporal durable workflows, CrewAI Flows vs LangGraph, parallel tool calling, vector database showdown) — bkz. TOPIC_LOG.md.
