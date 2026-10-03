# Sources — Agent Tracing Observability

- Langfuse × CrewAI integration guide — https://langfuse.com/integrations/frameworks/crewai
  - `pip install langfuse crewai openinference-instrumentation-crewai`
  - Env vars: `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_BASE_URL` (regional: cloud.langfuse.com / us.cloud.langfuse.com / jp.cloud.langfuse.com / hipaa.cloud.langfuse.com)
  - Code: `get_client()`, `langfuse.auth_check()`, `CrewAIInstrumentor().instrument(skip_dep_check=True)`, `langfuse.start_as_current_observation(as_type="span", name=...)`, `langfuse.flush()`
- CrewAI's own Langfuse observability doc (alternate OpenLit path) — https://docs.crewai.com/en/observability/langfuse
  - `pip install langfuse openlit crewai crewai_tools`; `openlit.init()` as the one-line instrumentation call
- AgentOps × LangGraph integration guide — https://docs.agentops.ai/v2/integrations/langgraph
  - `pip install agentops langgraph langchain-openai python-dotenv`
  - Env var: `AGENTOPS_API_KEY`
  - Code: single `agentops.init()` call, auto-captures graph structure, node executions, LLM calls, tool usage, state changes, timing
- LangSmith LangGraph tracing guide — https://docs.langchain.com/langsmith/trace-with-langgraph
  - Env vars: `LANGSMITH_TRACING=true`, `LANGSMITH_API_KEY`, optional `LANGSMITH_ENDPOINT` (non-US regions)
  - LangChain-based graphs: env vars only, no code changes. Non-LangChain code inside the graph needs `@traceable` / `wrap_openai`.
- Langfuse OpenTelemetry native endpoint changelog (context on OTel support breadth) — https://langfuse.com/changelog/2025-02-14-opentelemetry-tracing
- Background on current agent observability landscape (used only for framing, not as a factual citation) — https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse

## Verified claims used in the article
- Langfuse ingests traces over an OTLP endpoint and supports CrewAI, AutoGen, Semantic Kernel, Pydantic AI, smolagents among others via OpenTelemetry.
- AgentOps treats the *agent session* (not the individual LLM call) as its primary trace unit and supports session replay.
- LangSmith's zero-code-change path only applies when the graph's own nodes call LangChain/LangGraph primitives; raw OpenAI SDK calls inside a node still need manual wrapping.
- All three tools require an API key tied to a hosted (or self-hosted, for Langfuse) backend — none of this is "free forever" at scale, which is why the cost section exists.
