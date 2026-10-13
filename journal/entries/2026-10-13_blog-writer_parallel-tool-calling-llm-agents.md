# 2026-10-13 · blog-writer · Parallel Tool Calling in LLM Agents

- Yayında: "Parallel Tool Calling in LLM Agents: When It Helps and When It Breaks" — https://www.firstevolvenextscale.com/parallel-tool-calling-llm-agents/ (WP ID 1686), kalite kapısından ilk denemede geçti (`gate_failures: []`): SEO 12/12, voice_check PASS, İnsan Sesi 8/8.
- Kuyruktaki ilk konu alındı (kuyrukta 2 konu vardı). Konu, CrewAI/LangGraph gibi bir framework değil, doğrudan Claude ve OpenAI'ın ham tool-calling API'lerinin mekaniği olduğu için araştırma `platform.claude.com` ve `developers.openai.com`'un resmi dokümanlarına odaklandı. 6 iç link, 4 dış resmi link, 10 etiket (6'sı mevcut etiketlerle eşleşti: LLM Agents, Python, Claude API, OpenAI API, Idempotent Retries, AI Agent Reliability), 1 JPEG + 3 WebP görsel (4/4 ilk denemede kabul, yeniden üretim yok).

## Teknik doğrulama: canlı API çağrısı + bizzat yeniden üretilmiş race condition
Bu yazı özellikle iki katmanlı doğrulama içeriyordu:
- `anthropic` 1.13.0 ve `openai` 3.29.0 temiz bir venv'e kuruldu. `disable_parallel_tool_use` alanının gerçekten `ToolChoiceAutoParam`/`ToolChoiceAnyParam`'da var olduğu `__annotations__` ile doğrulandı (Anthropic API anahtarı ortamda olmadığı için bu alan canlı çağrı yerine SDK'nın kendi tip tanımlarından doğrulandı — bu sınırlama REPORT.md'de açıkça belirtildi).
- OpenAI tarafı için gerçek bir `gpt-4o-mini` çağrısı yapıldı (OPENAI_API_KEY canlı): varsayılan ayarla 2 tool call, `parallel_tool_calls=False` ile tam olarak 1 tool call döndü — dokümanın iddiasını doğrudan kendi ortamımda gördüm, sadece dokümana güvenmedim.
- Makalenin ana örneği (paylaşılan envanter durumunda race condition) iki Python thread'iyle bizzat kodlandı ve çalıştırıldı: kilitsiz versiyon beklenen 3 yerine 6 verdi (lost update), lock + idempotency-key seti eklenince her çalıştırmada doğru 3'ü verdi. Makaledeki iki kod bloğu da bu gerçekten çalıştırılmış scriptler.

## Tekrarlayan ortam sorunları (insan onayı hâlâ bekliyor — bugün Pazartesi, haftalık review günü)
- **Detached HEAD — 10. kez art arda** (2026-10-02'den beri her gün). Yine `git checkout main && git merge --ff-only origin/main` ile düzeltildi (local main origin'in 8 commit gerisindeydi), veri kaybı yok.
- **`pip install -q Pillow` yanlış Python'a kuruyor — 8. kez art arda.** Bugün `optimize_image.py` gerçekten `ModuleNotFoundError: No module named 'PIL'` ile patladı (önceki günlerde sorunu fark edip önceden düzeltiyordum; bugün sırayı takip ederken aynı hataya düştüm çünkü bugünkü zamanlanmış görev metni `pip install -q Pillow` komutunu birebir içeriyordu). `python3 -m pip install -q Pillow` ile düzeltildi.
- **Bugün haftalık review günü (Pazartesi).** Bu iki bulgu artık 10 ve 8 gündür art arda tekrarlıyor ve her ikisi de HEARTBEAT.md'ye kalıcı düzeltme olarak işlenmeyi bekliyor (adım 0: `pip install` → `python3 -m pip install`; adım 5: commit öncesi/sonrası `git branch`/`git status` kontrolü). İnsan onayı olmadan HEARTBEAT.md'yi kendi başıma değiştirmedim (önceki günlerin kararıyla tutarlı); ancak bu kadar uzun süredir tekrar eden, düşük riskli, agent'ın kendi klasöründeki mekanik bir komut düzeltmesi olduğu için, bir sonraki fırsatta insan onayı verilirse hemen uygulanabilir.

## Sonraki
- Kuyrukta 1 konu kaldı (vector database showdown for AI agent memory). 5'in altında ama boş değil; HEARTBEAT kuralı gereği TOPIC_SELECTION bugün tetiklenmedi, muhtemelen yarın tetiklenecek.
- Haftalık review maddeleri (bugün için): (1) detached HEAD + pip bulgularının HEARTBEAT.md'ye kalıcı düzeltme olarak işlenmesi — 10/8 gündür bekliyor; (2) REPORT.md'de biriken ters iç link önerilerinin insan tarafından eski yazılara uygulanıp uygulanmadığının kontrolü.
