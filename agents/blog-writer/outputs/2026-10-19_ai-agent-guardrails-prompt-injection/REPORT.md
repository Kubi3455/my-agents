# Report — 2026-10-19

## Post
- **Title:** AI Agent Guardrails for Prompt Injection: A Practical Playbook
- **Slug:** ai-agent-guardrails-prompt-injection
- **Focus keyword:** ai agent guardrails for prompt injection
- **Category:** AI
- **Word count:** ~2,430 words
- **WP post ID:** 1701 (draft)
- **Edit link:** https://www.firstevolvenextscale.com/wp-admin/post.php?post=1701&action=edit
- **Preview:** https://www.firstevolvenextscale.com/?p=1701

## Quality gate result: FAILED (kept as draft)
```
gate_failures:
- seo_checklist 10/12
- images not visually reviewed
- featured image missing or not JPEG (Instagram needs JPEG)
- fewer than 2 inline images
```
Root cause: `OPENAI_API_KEY` has no remaining credits. Confirmed today with a live
`chat.completions` call and by running `scripts/generate_image.py` directly — both returned
`429 insufficient_quota / credit_balance_exhausted`. This is the **5th consecutive day**
(2026-10-15, 16, 17, 18, 19) this exact blocker has prevented IMAGE_GENERATION. Posts 1694, 1696,
1698, 1699 are all stuck in draft for the same reason; this is now post 1701 on the same list.

Everything else is ready:
- `voice_check.py` → PASS (sentences=92, mean_len=20.2, stdev=10.3, em_dash=0)
- Human Voice Test: 8/8 (self-assessed against the STYLE_GUIDE checklist)
- SEO checklist: 10/12 — only the two image-related items fail
- 5 internal links (agent-control-flow-patterns, parallel-tool-calling-llm-agents,
  langgraph-long-term-memory, a2a-protocol-explained, claude-agent-sdk-vs-openai-agents-sdk)
- 4 external official links (Anthropic, OpenAI Agents SDK docs, OWASP GenAI, NVIDIA-NeMo/Guardrails)
- 10 tags prepared and resolved (tag_ids saved in publish-result.json)
- FAQ with 5 questions
- `content.html` has 3 `<!-- TODO (human): ... -->` comments in place of the unreplaced image
  placeholders, each with a concrete suggested scene, so a human can generate the images and
  update this draft directly in WordPress without touching the rest of the content.

## Technical verification
- Anthropic's indirect-injection pattern (tool_result isolation, JSON-encoding untrusted content,
  screening tool output with a cheap model) verified against the live `platform.claude.com` docs
  page via WebFetch, not a secondary source.
- OpenAI Agents SDK guardrail API verified two ways: against the official docs page AND against
  the actual installed `openai-agents` package in a clean venv (`inspect.signature` on
  `GuardrailFunctionOutput` and `ToolGuardrailFunctionOutput`, and reading
  `agents/tool_guardrails.py` source directly).
- Wrote and ran a real `tool_output_guardrail` (regex injection scan) against a poisoned and a
  clean fake tool output. Observed real output: `reject_content` for the poisoned case, `allow`
  for the clean one. No OpenAI API call was needed for this, since the guardrail function is
  pure Python called directly — this worked despite the credit exhaustion blocking image gen.
- Found and flagged a discrepancy: several 2026 security blogs describe a "2026 edition" of the
  OWASP LLM Top 10 with Excessive Agency moved to #3, but OWASP's own `genai.owasp.org/llm-top-10/`
  page still shows the 2025 edition at fetch time. The article states this explicitly rather than
  repeating the unverified "2026 edition" claim as fact. See `sources.md`.

## Suggested backlinks for older posts (not applied — agent doesn't edit published posts)
- `agent-control-flow-patterns` (1656) could link forward to this post when discussing how a
  ReAct loop re-feeds tool output into the next reasoning step — that's exactly the entry point
  indirect injection uses.
- `parallel-tool-calling-llm-agents` (1686) could reference this post's point about screening
  being harder once several tool calls return results simultaneously.

## Social
Caption prepared in `post.json` → `social_message` (526 chars, 6 hashtags, link + "Link in bio"
line). Will not be posted by Jetpack since the post stayed a draft.

## Operational note (same as the last 4 days)
Nothing left for the agent to do here — this is an OpenAI billing issue, not a content or code
issue. A human needs to add credits at
https://platform.openai.com/settings/organization/billing/. Once that happens, IMAGE_GENERATION
can run against this same draft (1701) without redoing the writing, SEO, or linking work.
