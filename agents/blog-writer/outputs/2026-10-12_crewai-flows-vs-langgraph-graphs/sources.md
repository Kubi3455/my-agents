# Sources — CrewAI Flows vs LangGraph Graphs

## Official documentation (fetched today via WebFetch)
- CrewAI Flow decorators (`@start`, `@listen`, `@router`, `and_`, `or_`), state management (unstructured dict vs Pydantic `Flow[State]`), persistence (`@persist`, `restore_from_state_id`), plotting: https://docs.crewai.com/en/concepts/flows
- CrewAI → LangGraph migration guide (source of the classify/route example shape used in the article): https://docs.crewai.com/en/guides/migration/migrating-from-langgraph
- LangGraph `StateGraph.add_conditional_edges` signature and parameter docs (`source`, `path`, `path_map`): https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_conditional_edges
- LangGraph `Command` class fields (`graph`, `update`, `resume`, `goto`, `PARENT`): https://reference.langchain.com/python/langgraph/types/Command
- LangGraph `StateGraph` constructor and usage pattern (`.compile()` required before execution): https://reference.langchain.com/python/langgraph/graph/state/StateGraph

Third-party comparison blogs turned up by web search (metavert.io, morphllm.com, spheron.network, leanware.co, alicelabs.ai, etc.) were read for orientation only, cited nothing directly, and were cross-checked against the official docs/source above wherever used — several of those blogs disagreed with each other on version numbers, which is why none of them is cited as a source.

## End-to-end runtime verification (today, two local venvs)

**LangGraph** — installed `langgraph==1.2.14` cleanly (`pip install langgraph`, no issues). Verified with `inspect.signature`:
- `StateGraph.add_conditional_edges(self, source, path, path_map=None)`
- `StateGraph.add_node(...)`, `StateGraph.add_edge(start_key, end_key)`
- `Command` dataclass fields: `graph`, `update`, `resume`, `goto`, `PARENT`

Ran the article's exact LangGraph triage example end-to-end (`app.invoke(...)`) for both the billing and technical branches — both returned the correct result. Then built a second graph with a routing function that returns a label absent from `path_map` and invoked it: it raised `KeyError: 'unknown_label'` at `invoke()` time (i.e., the first time that specific edge is actually traversed), not at `add_conditional_edges()` or `.compile()` time. **This corrected a factual error in an earlier draft of the article**, which had described the check as happening at "construction time" / "build time" — the draft was rewritten throughout to say "run time" / "the first time that edge is hit" instead, which is what the test actually showed.

**CrewAI** — `pip install crewai` alone never finished in a reasonable window; its dependency resolver backtracks heavily across a large, tightly-pinned tree (chromadb, opentelemetry exporters, lancedb, litellm, etc.) looking for a mutually compatible set, and the plain install was killed after ~20 minutes with no package yet installed. Worked around this by installing `crewai` with `--no-deps` and then walking its actual `ModuleNotFoundError` chain one package at a time (also `--no-deps`), fixing a few PyPI/import name mismatches along the way (`python-dotenv` not `dotenv`, `rpds-py` not `rpds`, `PyJWT` not `jwt`, `python-dateutil` not `dateutil`) and installing the two `opentelemetry-exporter-otlp-proto-*` packages together (with deps) once their mismatched `--no-deps` versions broke each other. This resolved to a working install of **`crewai==1.15.27`**, the actual current PyPI release.

With `crewai` actually importable, two things were verified directly against the installed source and runtime, not secondhand:
1. **Read the real dispatch code** in `crewai/flow/runtime/__init__.py` (`_execute_listeners` → `_find_triggered_methods` → `_condition_met` → `_condition_satisfied`). The router's return value is coerced to `str()` and checked with plain Python `in` against the set of already-seen trigger names (`crewai/flow/runtime/__init__.py:184-189`: `return condition in events` for a string condition). No normalization, no case-insensitivity, no validation step, and `_find_triggered_methods` returns an empty list with zero errors/warnings/logs when nothing matches.
2. **Ran it.** Built the article's exact `TriageFlow` and called `flow.kickoff(...)` — worked correctly, printed `routed to billing queue`. Then built the same Flow with `@listen("Billing")` (capital B) against a router that still returns lowercase `"billing"`, redirected stdout/stderr, and called `kickoff()` again: it completed normally, printed CrewAI's own Flow-execution panels for `classify` and `route` as "Completed", and simply never executed `handle_billing` at all. No exception, no warning, no log line matching `error|warn|fail|exception|traceback` anywhere in the captured output. `flow.state.result` stayed at its Pydantic default (`""`). This is the exact scenario described in the article's opening anecdote and the "Silent String-Matching Trap" section, confirmed against the real, current library rather than assumed from memory or from secondary blog posts.

All code examples in the article (both the working CrewAI/LangGraph triage flows and the typo'd CrewAI variant) are the literal code that was executed in these two venvs, not simplified or reconstructed afterward.
