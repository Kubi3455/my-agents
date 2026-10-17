# Report — 2026-10-17

## Post
- **Title:** Model Routing for AI Agents: Surviving a Provider Outage
- **Slug:** `model-routing-ai-agents`
- **Focus keyword:** model routing for ai agents
- **WP post ID:** 1698 — **status: draft** (quality gate failed, `--live` kept it as draft, exit code 3)
- **Edit link:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1698&action=edit
- **Word count:** 2,623

## Quality gate result
```
gate_failures:
  - seo_checklist 10/12
  - images not visually reviewed
  - featured image missing or not JPEG (Instagram needs JPEG)
  - fewer than 2 inline images
```
Only the image-related items failed. SEO checklist is 10/12 — the two missing points are exactly checklist items #9 and #10 (alt text on images, featured + ≥2 inline images), because no images exist yet.

## Root cause (not fixable by this agent today)
`OPENAI_API_KEY` has **no remaining credit**. Confirmed live, twice, today (2026-10-17):
- `openai.chat.completions.create(model="gpt-4o-mini", ...)` → `429 insufficient_quota / credit_balance_exhausted`
- This is the **third consecutive day** this exact blocker has appeared (2026-10-15, 2026-10-16, 2026-10-17 — see MEMORY.md "Altyapı"). It is no longer a one-off; it needs a human to add OpenAI billing credit. HEARTBEAT.md step 0 still only checks that the env var is *set*, not that it has balance — this gap has now been flagged for three days running and still needs human sign-off to fix.

## Human-voice test: 8/8
1. Banned-phrase/word scan clean — `voice_check.py` PASS (`sentences=86 mean_len=19.2 stdev=11.9 short=11 flat_triplets=1 em_dash=2`)
2. No long runs of same-length sentences (flat_triplets 1/86)
3. ≥4 expertise signals: a practical gotcha not in the docs (the exception type changes once a circuit breaker opens), a trade-off discussion (proxy vs. no proxy), a real failure narrative (the Tuesday outage), real captured error output, a gentle pushback on common practice (routing rate limits like outages), an edge-case/scale note (fallback-chain latency stacking)
4. ≥2 explicit opinions/recommendations ("I'd start with a circuit breaker... today", "I'd wrap the breaker's own error type...")
5. Conclusion is a recommendation, not a recap
6. Opens on a real, specific incident, not a definition
7/8. Read naturally; practitioner tone throughout

## SEO checklist: 10/12
1. ✅ Focus keyword in title
2. ✅ Focus keyword in first 100 words (91 words in)
3. ✅ Focus keyword in an H2 ("Why model routing for AI agents matters more in 2026")
4. ✅ SEO title 43 chars (≤60)
5. ✅ Meta description 151 chars (140–158), contains focus keyword
6. ✅ Slug short, keyword-derived
7. ✅ 5 internal links, distinct targets, descriptive anchors (within 4–6 target)
8. ✅ 3 external links, official docs only, no utm (LiteLLM docs, OpenRouter docs, pybreaker PyPI page)
9. ❌ Image alt text — no images exist
10. ❌ Featured + ≥2 inline images — none generated
11. ✅ FAQ with 5 questions (H3)
12. ✅ No H1; H2→H3 nesting clean; 10 tags ready, "Model Routing" tag covers the focus keyword

## Technical verification
- **pybreaker**: installed live (`pip install pybreaker`), inspected the real `CircuitBreaker.__init__` signature via `inspect.signature`, and **ran the exact code block in the article** — captured output matches the article word-for-word. This is runtime-verified, not doc-sourced.
- **LiteLLM Router YAML**: field names (`fallbacks`, `context_window_fallbacks`, `content_policy_fallbacks`, `default_fallbacks`, `num_retries`, `request_timeout`, `allowed_fails`, `cooldown_time`, `disable_fallbacks`, `enforce_fallback_model_access`, `enforce_fallback_budget`, spend-log `attempted_fallbacks`/`original_model_group`) verified against the official docs (`docs.litellm.ai/docs/proxy/reliability`) via WebFetch, and the YAML block itself was parsed locally with `yaml.safe_load` to confirm it's syntactically valid. **Not runtime-tested against a live LiteLLM proxy** — `pip install litellm` was attempted but its dependency resolution did not finish inside the research window (same heavy-dependency-tree pattern as crewai/langgraph noted in MEMORY.md 2026-10-12). Flagged here per RULES.md so this is not presented as more verified than it is.
- **OpenRouter routing**: `models` array and the stricter Anthropic-endpoint `fallbacks` parameter (max 3 entries, model-only field, cannot combine with `models`) verified against the official docs (`openrouter.ai/docs/guides/routing`) via WebFetch. The Python code example was `py_compile`-checked for syntax but not run against a live OpenRouter key (none available in this environment).
- Full source list and exact verification method per claim: `sources.md` in this package.

## Images (missing — see TODO comments in content.html)
Two `<!-- TODO (human) -->` comments mark where the featured image and one inline image should go, each with a detailed suggested scene (components, labels, layout) so a human can generate and drop them in without re-reading the whole article. No `{{IMG:...}}` placeholders were left unreplaced — the draft post itself exists cleanly in WordPress.

## Suggested inverse internal links (for a human to add to older posts; this agent does not edit existing posts)
- `ai-agent-rate-limits` → could add a sentence contrasting "retry the same provider" with "route to a different one," linking to this new post
- `durable-agent-workflows-temporal` → could note that crash recovery and provider routing are different failure modes, linking here for the latter
- `agent-tracing-observability` → could mention tracing which model actually answered as a reason to want this post's content

## Next steps for a human
1. Add OpenAI billing credit (3rd day blocked — this is now the priority item).
2. Once credit is restored, generate the featured image (JPEG) + 2 inline images (WebP) using the scenes described in the `TODO (human)` comments in `content.html`, update `post.json` → `images`, set `quality.images_reviewed: true` only after actually opening and checking each image, and republish this exact draft (post 1698) — **do not re-run `wp_client.py publish --live` on a fresh post.json copy; there is no "update draft" command, so editing post 1698 directly via the WP admin or REST API is the only safe path that avoids creating a duplicate post** (see MEMORY.md 2026-10-16 operational note).
