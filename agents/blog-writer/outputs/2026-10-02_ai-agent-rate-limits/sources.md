# Sources — AI Agent Rate Limits / 429 Errors

- Anthropic API rate limits (token bucket algorithm, response headers, spend-cap 429 JSON example, cache-aware ITPM): https://platform.claude.com/docs/en/api/rate-limits — fetched 2026-10-02
- OpenAI API error codes (429 `rate_limit_error`/`slow_down`, 503 `service_unavailable_error`/`server_is_overloaded`): https://developers.openai.com/api/docs/guides/error-codes — fetched 2026-10-02
- OpenAI API rate limits guide (headers, exponential backoff with jitter guidance): https://developers.openai.com/api/docs/guides/rate-limits — fetched 2026-10-02
- tenacity documentation (retry decorator, wait_exponential/wait_random_exponential, stop_after_attempt, retry_if_exception_type signatures): https://tenacity.readthedocs.io/en/latest/ — fetched 2026-10-02; code pattern verified by running against a mock client in a venv (`/tmp/blogvenv`, tenacity installed via pip) before use in the article
- Agent fan-out / concurrency math ("~20 model calls per task", "25 concurrent tasks saturate a 500 RPM quota"): https://59api.com/blog/2026-guide-to-llm-api-rate-limits-and-retries-2493 — fetched 2026-10-02
- Multi-layer retry strategy framing (backoff + jitter + routing fallback + idempotency, differentiate transient vs quota errors): https://www.getmaxim.ai/articles/handle-429-errors-in-production-llm-applications/ — fetched 2026-10-02, used for general framing only, no direct quotes

## Code verified to run (not just plausible)
- `test_retry.py`: tenacity retry differentiating `RateLimitError` (retried, succeeds on 3rd attempt) from `QuotaExceededError` (not retried, raises immediately) — PASSED
- `test_concurrency.py`: `TokenBucket.acquire()` correctly throttles 20 acquires against a 10/sec refill rate (took ~1s, not 0s); `run_tool_once` idempotent fingerprint cache runs a side-effecting function exactly once across two identical calls — PASSED

Both test scripts run in `/tmp/claude-0/.../scratchpad/` under a throwaway venv with `tenacity` installed; not committed to the repo (scratch files).
