# Agent Workspace

Multi-agent system powered by markdown files and Claude Code.

## Quick Navigation

| Agent | Path | Purpose |
|-------|------|---------|
| Standard Template | `agents/standard-agent/` | Copy this to create any new agent |
| Blog Writer | `agents/blog-writer/` | firstevolvenextscale.com için her gün insan sesinde, SEO'lu, görselli İngilizce AI yazısı üretir, kalite kapısı geçerse yayınlar ve Jetpack ile FB/IG/LinkedIn'e paylaşır |
| Web Builder | `agents/web-builder/` | Üst düzey hareketli/görsel siteleri bulur, analiz eder, benzer kalitede özgün siteler üretir |

## Firma Verildiğinde (web-builder)

Kullanıcı sohbette bir firmanın bilgilerini verirse ("şu firma için site yap" vb.):
1. Bilgileri `agents/web-builder/data/imports/HOW_TO_EXPORT.md` içindeki firma şablonuna göre `agents/web-builder/data/imports/firmalar/[firma-adi].md` dosyasına yaz, `Durum: aktif` yap. Eksik alanları kullanıcıya sor (en az: sektör, hedef kitle, istenen his; chatbot için WhatsApp, adres).
2. `agents/web-builder/HEARTBEAT.md` → Firma Modu akışını çalıştır: tasarım planı `frontend-design` skill'i ile (`skills/DESIGN_DIRECTION.md`), bileşen seçimi 21st.dev'den (`skills/COMPONENT_SELECTION.md`), ikisi harmanlanarak build; her siteye kural tabanlı sohbet asistanı eklenir (`skills/CHATBOT_WIDGET.md`: SSS, WhatsApp, yol tarifi).
3. 21st.dev API anahtarı `API_KEY_21ST` ortam değişkenindedir; değerini hiçbir dosyaya yazma.

## Blog Yazısı (blog-writer)

- Günlük döngü: `agents/blog-writer/HEARTBEAT.md`. Ses kuralları: `agents/blog-writer/data/STYLE_GUIDE.md` → "İnsan Sesi" (öncelikli).
- Yazılar kalite kapısı (`wp_client.py` → `quality_gate`) geçerse otomatik yayınlanır, geçmezse taslak kalır. `WP_USER`, `WP_APP_PASSWORD`, `OPENAI_API_KEY` ortam değişkenlerindedir; değerlerini hiçbir dosyaya yazma.

## Key Directories

- `knowledge/` — Static reference (brand voice, strategy, audience profiles)
- `journal/` — Living memory (events, decisions, learnings)
- `templates/` — Agent creation templates
- `orchestrator/` — Cross-agent coordination
- `examples/` — Example agents to learn from

## Agent Structure

Every agent folder contains:
- `AGENT.md` — Goals, KPIs, skills list, constraints
- `skills/` — One markdown per skill
- `HEARTBEAT.md` — Cron schedule and triggers
- `MEMORY.md` — Agent-local learnings
- `RULES.md` — Boundaries, handoff rules

## Key Files

- `AGENT_REGISTRY.md` — Master list of all agents and their status
- `CONVENTIONS.md` — Naming rules and structure requirements
- `NEW_AGENT_BOOTSTRAP.md` — Steps to create a new agent
- `AGENT_CREATION_CHECKLIST.md` — Verify new agents are complete

## Conventions

- Agent folders: lowercase, hyphen-separated under `agents/`
- Output files: `YYYY-MM-DD_agent-name_description.md`
- Agents read from `knowledge/` and `journal/`, write to `journal/` only
- Knowledge files are static — agents propose changes but never edit directly
