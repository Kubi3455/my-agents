# Sources & Verification — Prompt Caching for AI Agents

## Primary technical sources
- **Anthropic prompt caching docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  Fetched directly (WebFetch) on 2026-10-15. Used for: write cost multipliers (1.25x/5min, 2x/1h), read cost multiplier (0.1x, with 0.05x/0.025x exceptions on some newer models), minimum cacheable token thresholds (512–4,096 depending on model), max 4 explicit breakpoints, default 5-minute lifetime, cache scope order (tools → system → messages), usage field names (`input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `cache_creation.ephemeral_5m_input_tokens`/`ephemeral_1h_input_tokens`).
- **Anthropic Python SDK (local, offline verification)** — `pip install anthropic` (installed version 1.14.0). Verified `anthropic.types.CacheControlEphemeralParam` directly via `inspect.getsource()`: confirms `type: "ephemeral"` (required) and `ttl: "5m"|"1h"` (default `"5m"`), matching the docs. No live Anthropic API key is available in this environment, so no live call was made — this is a type-definition check, not a live-call verification (same method used in the 2026-10-13 article for the same reason).
- **OpenAI prompt caching docs** — https://developers.openai.com/api/docs/guides/prompt-caching (note: `platform.openai.com/docs/guides/prompt-caching` 301-redirects here as of this writing). Fetched directly (WebFetch) on 2026-10-15. Used for: automatic/implicit caching by default, minimum ~1,024 tokens on current models, discount language ("up to 95%"), 1.25x write / 0.1x read on current-generation models, retention windows, and response field names (`usage.input_tokens_details.cached_tokens`, `cache_write_tokens`).
- **Live OpenAI API check** — attempted a real `chat.completions.create` call (`gpt-4o-mini`) with a long static system prompt, the exact request shape implicit caching applies to. The call reached the API and returned a structurally valid error: `HTTP 429 insufficient_quota / credit_balance_exhausted` — the OPENAI_API_KEY in this environment has no remaining billing credit (confirmed on two separate attempts, a few seconds apart, ruling out a transient blip). This confirms the request itself is well-formed and reaches billing, but means the `cached_tokens` usage field could **not** be observed live this run. The article's OpenAI numbers are doc-sourced only, and the code example says so explicitly in its comments. **Action needed from a human:** add credit to the OpenAI account at platform.openai.com/settings/organization/billing — this also blocked IMAGE_GENERATION today (see REPORT.md / journal).

## Research paper
- **"Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks"**, Lumer, Nizar, Jangiti, Frank, Gulati, Phadate, Subbiah. arXiv:2601.06007 (v1/v2), January 2026. https://arxiv.org/abs/2601.06007
  Fetched the abstract/metadata page directly (WebFetch) on 2026-10-15; the full paper body was not accessed, only what the abstract page itself reports. Numbers used in the article: 41–80% cost reduction, 13–31% TTFT improvement, >500 agent sessions on DeepResearch Bench, 10,000-token system prompts in the main experiment, ablation over 500–50,000 token prompts and 3–50 tool calls, full-context caching sometimes increasing latency, and the "what breaks the cache" findings (dynamic content placement, dynamic tool results in the cached prefix, naive full-context caching).

## Internal link targets (verified against data/post-inventory.json, refreshed 2026-10-15)
- /semantic-caching-llm-agents/
- /ai-agent-rate-limits/
- /durable-agent-workflows-temporal/
- /parallel-tool-calling-llm-agents/
- /agent-tracing-observability/
- /mcp-context-bloat/

## Not independently verified / excluded from the article
- Secondary blog claims about exact OpenAI per-model pricing history (e.g. "older models write for free, read at up to 90% off") were seen in search results but not confirmed against official docs, so they were left out. Only the current-generation numbers confirmed directly on `developers.openai.com` are used.
- Google's caching behavior (also tested in the arXiv paper) is mentioned only in the aggregate "across OpenAI, Anthropic, and Google" framing — no Google-specific numbers are claimed, since the abstract page didn't break those out and no official Google doc was checked.
