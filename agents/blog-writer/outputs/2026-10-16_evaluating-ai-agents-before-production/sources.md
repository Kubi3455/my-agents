# Sources & Verification — Evaluating AI Agents Before Production

## Primary sources (fetched directly, not via summary)
- Anthropic engineering guide, "Demystifying evals for AI agents": https://anthropic.com/engineering/demystifying-evals-for-ai-agents
  Fetched directly with WebFetch (not from a secondary summary). Verified claims used in the article:
  - Transcript/trajectory definition: "the complete record of a trial, including outputs, tool calls, reasoning, intermediate results, and any other interactions."
  - Outcome grading vs. transcript grading distinction, and the "often better to grade what the agent produced, not the path it took" guidance, with transcript grading as a complement.
  - Starting dataset size: "20-50 simple tasks drawn from real failures is a great start."
  - pass@k (at least one success in k attempts) vs. pass^k (all k attempts succeed) definitions.
  - Test isolation and the real anecdote: Claude gained an unfair advantage on a coding task by reading leftover git history from an earlier, uncleaned trial.

## Code verified by actually running it (not copied from docs)
- `agentevals` 0.0.9 installed in a clean venv (`/tmp/evalcheck_venv`, Python 3.11) via `pip install agentevals`.
- `create_trajectory_match_evaluator` signature confirmed via `inspect.signature` directly against the installed package: `trajectory_match_mode: Literal["strict","unordered","subset","superset"] = "strict"`, `tool_args_match_mode`, `tool_args_match_overrides`.
- Ran the duplicate-refund trajectory from the article through the evaluator myself:
  - `trajectory_match_mode="unordered"` → `{'key': 'trajectory_unordered_match', 'score': False, 'comment': None, 'metadata': None}` (correctly flags the duplicate `issue_refund` call).
  - `trajectory_match_mode="superset"` on the exact same input → `{'key': 'trajectory_superset_match', 'score': True, ...}` (does NOT flag it). This "superset mode misses duplicate/unsafe extra calls" finding is my own discovery from running both modes side by side, not something stated in the docs — this is the article's main practical gotcha.
- `create_trajectory_llm_as_judge` signature and the exact wording of `TRAJECTORY_ACCURACY_PROMPT` confirmed via `inspect.signature` and reading the string constant directly from the installed `agentevals.trajectory.llm` module.
  - Caveat (disclosed in the article too): I did not make a live model call through this evaluator. `OPENAI_API_KEY` returned `429 insufficient_quota / credit_balance_exhausted` on a direct test call (both a `chat.completions` call and `generate_image.py`) on 2026-10-16, same failure mode as 2026-10-15 (see MEMORY.md "Altyapı"). The code and prompt text shown are accurate to the installed library; the live grading behavior itself is not demonstrated.
- `0.95 ** 8 = 0.6633956609125211` — computed directly in a Python REPL, not quoted from a third party.

## Secondary documentation (used for framing only, not for code)
- LangSmith trajectory evals docs (`docs.langchain.com/langsmith/trajectory-evals`) and the `agentevals` GitHub repo (`github.com/langchain-ai/agentevals`) — used to confirm `pip install agentevals`, the import path `agentevals.trajectory.match`, and the general LangSmith `client.evaluate` integration pattern. Not used for any code claim not separately verified above.
- OpenAI "Trace grading" guide (`developers.openai.com/api/docs/guides/trace-grading`) — fetched directly with WebFetch. Quotes used: trace grading assigns "structured scores or labels" to an agent's trace, described as "the end-to-end log of decisions, tool calls, and reasoning steps"; dashboard workflow is Logs > Traces > select a trace > create/run a grader > "Grade all" for trace evals across examples. I did not find or claim an SDK-level Python call for this flow (dashboard-only, as described).

## Background research (vendor/community blogs, not cited as authoritative in the article)
- Various 2026 vendor blog posts on agent evaluation (futureagi.com, dev.to, shelf.io, etc.) were read for general framing of "trajectory-level testing" as a term, but no specific statistic or claim from them was used in the final article — anything from these sources that made it into the piece was independently re-verified against a primary source (Anthropic's post or a live code run) first.
