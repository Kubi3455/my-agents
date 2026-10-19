# Sources & Verification — AI Agent Guardrails for Prompt Injection

## Primary sources (official docs)

- Anthropic, "Mitigate jailbreaks and prompt injections":
  https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
  Fetched directly (WebFetch). Used for: direct vs indirect injection framing, tool_result isolation,
  JSON-encoding untrusted content, harmlessness-screen pattern for tool output.

- OpenAI Agents SDK, "Guardrails": https://openai.github.io/openai-agents-python/guardrails/
  Fetched directly. Used for: @input_guardrail/@output_guardrail, GuardrailFunctionOutput,
  tripwire exceptions, @tool_input_guardrail/@tool_output_guardrail, ToolGuardrailFunctionOutput.

- OWASP GenAI, "LLM Top 10": https://genai.owasp.org/llm-top-10/
  Fetched directly. As of fetch, the live page shows the **2025** edition (LLM01:2025 Prompt
  Injection, LLM06:2025 Excessive Agency), not a formally published 2026 edition. Several
  third-party security blogs (sdtimes.com, helpnetsecurity.com, infosecurity-magazine.com,
  blog.checkpoint.com) describe a "2026 edition" with Excessive Agency moved to #3, but this could
  not be confirmed on OWASP's own site at fetch time. The article explicitly flags this
  discrepancy instead of stating the 2026 edition as confirmed fact.

- NVIDIA-NeMo/Guardrails repository: https://github.com/NVIDIA-NeMo/Guardrails
  Fetched directly. Used for: 5 rail types (input/dialog/retrieval/execution/output), YAML-based
  input rail config, built-in jailbreak/injection detection claim, Apache-2.0 license, v0.24.1.

## Live code verification (no OpenAI API call required)

- Installed `openai-agents` into a clean venv (`/tmp/guardrails_venv`, Python 3.11) and inspected
  the real package (not just docs):
  - `GuardrailFunctionOutput.__init__` signature confirmed: `(output_info: Any, tripwire_triggered: bool)`.
  - `ToolGuardrailFunctionOutput.allow()` / `.reject_content(message, output_info=None)` /
    `.raise_exception()` confirmed via `inspect.signature` and by reading `agents/tool_guardrails.py`
    source directly.
  - `ToolInputGuardrailData` fields: `context`, `agent`. `ToolOutputGuardrailData` adds `output`.
  - Wrote and ran a standalone `tool_output_guardrail` (regex-based injection scan) against a
    poisoned fake email body and a clean one. Output observed directly:
    `poisoned -> {'type': 'reject_content', 'message': 'Tool output withheld...'}`
    `clean -> {'type': 'allow'}`
  - This did not require a live model call: the guardrail function itself is pure Python, called
    directly rather than through `Runner.run()`. No Anthropic/OpenAI chat completion was made for
    this verification (OPENAI_API_KEY has no credits, see below).

## Known blocker (not a content issue)

- `OPENAI_API_KEY` is set but has no remaining credits: confirmed today via a live
  `chat.completions` call (`429 insufficient_quota / credit_balance_exhausted`) and via running
  `scripts/generate_image.py` directly (same error). This is the **5th consecutive day**
  (2026-10-15 through 2026-10-19) this has blocked IMAGE_GENERATION. See MEMORY.md "Altyapı".
