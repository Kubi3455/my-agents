# Sources & Verification — Model Routing for AI Agents

## Primary sources (fetched directly, 2026-10-17)

1. **LiteLLM Proxy — Reliability / Fallbacks**
   https://docs.litellm.ai/docs/proxy/reliability
   Verified via WebFetch of the official docs page. Confirmed exact config keys used in this article:
   - `router_settings.fallbacks` / `litellm_settings.fallbacks`: list of `{"model_group": ["backup", ...]}` maps, tried in order
   - `context_window_fallbacks`, `content_policy_fallbacks` as separate fallback types
   - `default_fallbacks` (catch-all under `litellm_settings`)
   - `num_retries`, `request_timeout` (per-model retry/timeout before falling back)
   - `allowed_fails`, `cooldown_time` (cooldown/circuit-breaker-style removal of a failing deployment)
   - `disable_fallbacks` (per-request body field, and per-key via `/key/generate` metadata)
   - `enforce_fallback_model_access`, `enforce_fallback_budget` (general_settings)
   - Spend log metadata: `attempted_fallbacks`, `original_model_group`
   - Deprecation note: `mock_testing_fallbacks` / `mock_testing_context_fallbacks` / `mock_testing_content_policy_fallbacks` stripped from Proxy requests as of Proxy v1.85.0 (still work for direct `litellm.Router` calls)
   - Live `pip install litellm` was attempted in this session but the dependency resolution did not finish within the research window (same heavy-dependency-tree pattern noted in MEMORY.md for crewai/langgraph-adjacent packages); all LiteLLM claims in this article are sourced directly from the official docs page above, not from a local run, and are flagged as doc-verified rather than runtime-verified in REPORT.md.

2. **OpenRouter — Model Routing guide**
   https://openrouter.ai/docs/guides/routing
   Verified via WebFetch of the official docs page. Confirmed:
   - `models` array (priority-ordered list of model IDs) is the main routing/fallback parameter, used when "the primary model's providers are down"
   - A separate `fallbacks` parameter exists only on the Anthropic-shaped Messages endpoint (`/api/v1/messages`), accepts at most 3 entries, each entry has only a `model` field (per-attempt overrides like `max_tokens` return a 400), and `fallbacks` cannot be combined with `models` (sending both returns a 400)
   - Fallback triggers: context length validation errors, moderation flags, rate limiting, downtime — any error by default
   - If the fallback model also fails, the original error from that attempt is returned
   - Billing is based on whichever model actually handled the request (returned in the response's `model` field); the docs do not state whether failed attempts themselves are billed, so this article does not make that claim
   - Example code: `anthropic.beta.messages.create({ model: '...', fallbacks: [{ model: '...' }], ... })` with `baseURL` pointed at OpenRouter

3. **pybreaker** (installed and tested live in this session: `pip install pybreaker`)
   Source: `/usr/local/lib/python3.11/dist-packages/pybreaker/__init__.py` (installed package, inspected directly with `inspect.signature`)
   - `CircuitBreaker.__init__` real signature confirmed: `fail_max: int = 5, reset_timeout: float = 60, success_threshold: int = 1, exclude=None, listeners=None, state_storage=None, name=None, throw_new_error_on_trip: bool = True`
   - States confirmed from source: `pybreaker.STATE_OPEN = "open"`, `STATE_CLOSED = "closed"`, `STATE_HALF_OPEN = "half-open"`
   - **Live-reproduced behavior** (ran in this session, exact output captured): with `fail_max=3`, the 3rd call to a function that always raises trips the breaker; `breaker.call(...)` on that 3rd call raises `pybreaker.CircuitBreakerError` ("Failures threshold reached, circuit breaker opened") instead of propagating the original exception, and every call after that until `reset_timeout` elapses raises `CircuitBreakerError` ("Timeout not elapsed yet, circuit breaker still open") without ever calling the wrapped function again. This is the basis for the "the exception you catch changes" pitfall in the article — it was observed directly, not quoted from a third party.

## Internal link targets (existing posts on the site, verified against `data/post-inventory.json`)
- `/ai-agent-rate-limits/` — 429 retry strategy on a single provider (contrast point: rate limiting vs. a provider being fully down)
- `/agent-tracing-observability/` — needed to actually notice a silent fallback happened
- `/durable-agent-workflows-temporal/` — different failure mode (process/crash recovery vs. provider outage)
- `/parallel-tool-calling-llm-agents/` — tool-call shape differences across providers
- `/claude-agent-sdk-vs-openai-agents-sdk/` — structured-output/tool-schema differences between SDKs

## Note on scope
This article covers API-level model/provider routing (LiteLLM Router, OpenRouter, a hand-rolled circuit breaker). It does not cover intra-cluster GPU load balancing or model-serving infrastructure (vLLM, Triton) — out of scope for the agent-reliability angle this post takes.
