# Sources

- https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use — execution semantics (no prescribed order), disable via `tool_choice.disable_parallel_tool_use`, effect under `auto` vs `any`/`tool`, troubleshooting (result formatting, "only batch independent calls" prompt line), computer/browser use batch actions must run sequentially.
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls — `tool_use`/`tool_result` formatting rules, `tool_use_id` matching, tool_result blocks must precede text, `is_error` pattern.
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools — `tool_choice` types (`auto`/`any`/`tool`/`none`), forced tool use model support table.
- https://developers.openai.com/api/docs/guides/function-calling — default parallel behavior, `parallel_tool_calls=False` effect ("exactly zero or one tool"), built-in tools excluded from parallel function-call batch on GPT-5-class models, `gpt-4.1-nano-2025-04-14` duplicate-call note.
- https://developers.openai.com/api/docs/api-reference/chat/create — `parallel_tool_calls` parameter description ("Whether to enable parallel function calling during tool use").

## Verified by direct execution (this session, 2026-10-13)
- `anthropic` Python SDK 1.13.0 installed in a clean venv; `inspect`/`__annotations__` on `ToolChoiceAutoParam` and `ToolChoiceAnyParam` confirmed the `disable_parallel_tool_use` field name matches the docs exactly.
- `openai` Python SDK 3.29.0 installed in the same venv; ran a real `chat.completions.create` call against `gpt-4o-mini` with two independent tool-eligible requests in one prompt — default run returned 2 `tool_calls`, a second run with `parallel_tool_calls=False` returned exactly 1.
- Reproduced the read-modify-write race with two Python threads simulating "parallel tool calls" writing to a shared in-memory inventory dict with an artificial delay between read and write: final value was 6 instead of the expected 3 (lost update).
- Verified the fix (a `threading.Lock` around the mutation plus a `seen_requests` idempotency set keyed by request ID): same scenario produced the correct value of 3 every run.
