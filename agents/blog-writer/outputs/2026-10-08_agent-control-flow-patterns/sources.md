# Sources — Agent Control Flow Patterns

- `create_react_agent` deprecation notice (verbatim: "This function is deprecated in favor of `create_agent` from the `langchain` package"): https://reference.langchain.com/python/langgraph.prebuilt/prebuilt/chat_agent_executor/create_react_agent
- `create_agent` full signature (model, tools, system_prompt, middleware, response_format, state_schema, context_schema, checkpointer, store, interrupt_before, interrupt_after, debug, name, cache, transformers): https://reference.langchain.com/python/langchain/agents/factory/create_agent
- Middleware hooks (`before_model`, `after_model`, `wrap_model_call`, `wrap_tool_call`, async `a`-prefixed variants) and the `ModelCallLimitMiddleware` step-limit example (adapted, same hook names/signatures): https://docs.langchain.com/oss/python/langchain/middleware/custom
- `Send` API for dynamic fan-out / map-reduce in LangGraph's graph API (adapted example, same import and pattern as the official map-reduce walkthrough): https://docs.langchain.com/oss/python/langgraph/use-graph-api
- Middleware overview (hook placement before/after model and tool steps, registration via `middleware=[...]` on `create_agent`): https://docs.langchain.com/oss/python/langchain/middleware/overview
