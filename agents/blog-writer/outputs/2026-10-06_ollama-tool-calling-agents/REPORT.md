# Report — 2026-10-06 — Ollama Tool Calling Agents

## Status: Yayında
- Başlık: Ollama Tool Calling Agents: No LangChain Required
- Odak kelime: ollama tool calling agents
- Canlı link: https://www.firstevolvenextscale.com/ollama-tool-calling-agents/
- Düzenleme linki: https://www.firstevolvenextscale.com/wp-admin/post.php?post=1644&action=edit
- WP post ID: 1644
- Kelime sayısı: ~2246
- SEO checklist: 12/12
- İnsan Sesi Testi: 8/8 (`voice_check.py` PASS, em dash 1/3)
- Görseller: 4/4 Read ile açılıp kontrol edildi, hepsi ilk denemede kabul edildi (yeniden üretim yok)
- Kalite kapısı: geçti, `gate_failures: []`

## İçerik Özeti
Konu: Ollama'nın yerel (LangChain'siz) tool-calling API'si ile ajan döngüsü kurmak. Araştırma ajanı önce konunun güncelliğini doğruladı: Ollama v0.40.0 dün (2026-10-05) yayınlandı ve streaming tool-call parser'ını iyileştirdi; bu makaleye tazelik kattı.

Öne çıkan teknik bulgular (hepsi `sources.md`'de kaynaklı):
- `arguments` alanı Ollama'da zaten parse edilmiş dict olarak döner (OpenAI API'nin aksine JSON string değil)
- OpenAI-uyumlu `/v1/chat/completions` endpoint'i `num_ctx`'i sessizce düşürüyor; tool şemaları context'in başında olduğu için önce onlar kırpılıyor (gerçek, kaynaklı bir gotcha — kişisel anekdotla açılışta kullanıldı)
- v0.40.0'daki artımlı tool-call parser'ı, önceki "stream:false zorunlu" kısıtlamasını tamamen kaldırdı
- Gerçek, GitHub issue'dan alıntı hata mesajı: `error parsing tool call: invalid character ']' after object key:value pair` (issue #12064)
- Model boyutuna göre güvenilirlik: sub-7B modeller tek adımdan sonra bozuk JSON üretiyor, 8B-sınıfı modeller uzun zincirlerde döngüye giriyor, tool-tuned orta/büyük modeller (Qwen3, Llama 3.3, Mistral Small 3.5) güvenilir

Kod örneği (minimal tool-calling loop) gerçek bir Ollama kurulumu olmadığı için, dokümantasyondaki yanıt şekline birebir uyan yerel bir mock HTTP sunucusuna karşı uçtan uca çalıştırılarak doğrulandı (bkz. `sources.md`).

## İç Linkler (6)
local-llms-ollama-with-web-search, mcp-context-bloat, prevent-ai-agents-stuck-in-loops, structured-outputs-in-local-llm, debugging-multi-agent-workflows, autogpt-vs-crewai-vs-langgraph

## Dış Linkler (4)
docs.ollama.com/capabilities/tool-calling, ollama.com/search?c=tools, github.com/ollama/ollama/releases/tag/v0.40.0-rc3, github.com/ollama/ollama/issues/12064

## Etiketler (10)
Ollama Tool Calling Agents, Function Calling, Local LLM, AI Agent Loops, AI Agent Tooling, Ollama, LangChain, Python, AI Agent Debugging, Local AI

## Önerilen Ters İç Linkler (eski yazılara, insan uygular)
- `local-llms-ollama-with-web-search` → bu yazıya "tool calling without LangChain" cümlesiyle link eklenebilir (doğal devam yazısı)
- `structured-outputs-in-local-llm` → "if your local model also needs to call tools, not just return structured JSON" gibi bir cümleyle bu yazıya bağlanabilir
- `autogpt-vs-crewai-vs-langgraph` → framework karşılaştırmasına "or skip the framework entirely for a single local agent" notuyla bu yazıya link eklenebilir

## Sosyal Paylaşım Metni
Şablona uygun, 551 karakter, ilk satır 92 karakter, link doğru slug ile, "📌 On Instagram? Link in bio." satırı var, tam 6 hashtag (#OllamaToolCalling #AIAgentTooling #AIAgentLoops #Ollama #AIAgents #AIEngineering). Yayın anında Jetpack Social FB/IG/LinkedIn'e paylaştı.

## Notlar
- Araştırma ajanı (web search), yayınlanmadan bir gün önce çıkan Ollama v0.40.0'ı buldu ve makaleye dahil edildi; bu olmasaydı konu bir gün geride kalacaktı.
- `pip`/`python` komutu bu bulut ortamında Python 3.11'e, varsayılan `pip`'in kurduğu paketler ise bazen Python 3.13 kullanıcı sitesine gidiyor (Pillow bu yüzden `python -m pip install Pillow` ile ayrıca kurulmak zorunda kaldı; `python3.13 -c "import PIL"` çalışıyordu ama `python`/`python3` çalışmıyordu). Gelecek bulut çalışmalarında doğrudan `python -m pip install -q Pillow` kullanmak zaman kazandırır.
