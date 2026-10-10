# Sources — A2A Protocol Explained

All technical claims in this article were verified on 2026-10-10 against the official A2A specification, the current `a2a-sdk` (v1.2.2) Python package installed in a local venv, and the Agentic AI Foundation's own announcement. Every code example was executed end-to-end locally (FastAPI `TestClient` against a real `a2a-sdk` server built with `DefaultRequestHandler` + `InMemoryTaskStore`) before being used in the article.

- A2A protocol specification, v1.0.0 (AgentCard/Task/Message/Part fields, TaskState enum, versioning rules, `A2A-Version` header behavior, security schemes) — https://a2a-protocol.org/latest/specification/
- `a2a-sdk` Python package source, installed version 1.2.2, inspected directly via `inspect`/`DESCRIPTOR.fields` for `a2a.types.AgentCard/AgentSkill/AgentCapabilities/Message/Task/Part`, `a2a.server.agent_execution.AgentExecutor`, `a2a.server.request_handlers.DefaultRequestHandler`, `a2a.server.routes.*` (`create_agent_card_routes`, `create_jsonrpc_routes`, `create_rest_routes`, `add_a2a_routes_to_fastapi`) — https://github.com/a2aproject/a2a-python and https://pypi.org/project/a2a-sdk/
- Agentic AI Foundation announcement, "Agent2Agent (A2A) is joining the Agentic AI Foundation (AAIF) as a hosted project," dated 2026-08-17 (governance move, 150+ backing organizations, MCP/A2A layering, production users in mobile/cloud/commerce) — https://aaif.io/blog/a2a-joins-aaif

Local verification performed, not published as a separate claim but used to confirm article accuracy:
- Reproduced "A2A version '0.3' is not supported by this handler. Expected version '1.0'." by sending a request without the `A2A-Version` header, confirming the spec's default-to-0.3 behavior.
- Reproduced `ValueError: Protocol message AgentCard has no "url" field.` by passing a legacy top-level `url=` kwarg to `AgentCard(...)`, confirming the v1.0 schema change away from v0.3 tutorials.
- Confirmed `a2a.server.routes.fastapi_routes` / `agent_card_routes` / `jsonrpc_routes` / `rest_routes` replaced the removed `A2AStarletteApplication` class that older (v0.2.x/v0.3.x) tutorials still reference.
