# Sources — Durable Agent Workflows with Temporal

- Workflow/Activity basics, `@workflow.defn`, `@workflow.run`, `@activity.defn`, `workflow.execute_activity`, deterministic replay model: https://docs.temporal.io/develop/python/workflows/basics and https://docs.temporal.io/develop/python/activities/basics
- Worker setup (`Client.connect`, `Worker(...)`, `worker.run()`): https://docs.temporal.io/develop/python/workers/run-worker-process
- `RetryPolicy` (import path `temporalio.common.RetryPolicy`, fields `initial_interval`, `backoff_coefficient`, `maximum_interval`, `maximum_attempts`, `non_retryable_error_types`) and usage via `retry_policy=` on `workflow.execute_activity`: https://docs.temporal.io/develop/python/failure-detection
- Determinism constraints (no local clock/random branching inline, non-deterministic work belongs in Activities, versioning/patching for workflow code changes): https://docs.temporal.io/workflow-definition
- Replay-safe helpers `workflow.random()`, `workflow.now()`, `workflow.uuid4()` replacing `random.random()`, `datetime.now()`, `uuid.uuid4()`: https://docs.temporal.io/develop/python/workflows/basics
- OpenAI Agents SDK integration (`temporalio.openai_agents`, formerly `temporalio.contrib.openai_agents`; `OpenAIAgentsPlugin`, `ModelActivityParameters`, `activity_as_tool`, `@function_tool`, requires Temporal Python SDK 1.33.0+): https://docs.temporal.io/develop/python/integrations/openai-agents
- Joint Temporal/OpenAI public-preview announcement (July 2025): https://temporal.io/blog/announcing-openai-agents-sdk-integration
- Signals and Updates (`@workflow.signal`, `@workflow.update`, `WorkflowHandle.signal`, `WorkflowHandle.execute_update`): https://docs.temporal.io/develop/python/message-passing
- `temporalio` PyPI package, current version 1.34.0: https://pypi.org/project/temporalio/
- Real-world Thread-to-Workflow mapping for a LangGraph agent (checkpoints as Workflow state via the Update primitive, crash rehydration on another worker) — cited as one documented deployment pattern, not a core Temporal API: https://temporal.io/blog/manetu-the-thread-is-the-workflow

All code in the article is adapted from the official Temporal Python SDK docs and samples (`temporalio/samples-python`) with API names, decorators, and class/field names kept identical to the sources above; narrative examples (the agent, the tool names) are original. Verified today via WebFetch against the live docs pages, not from secondary blog posts.

## End-to-end runtime verification (today, local venv)
- Installed `temporalio==1.34.0`, `temporalio-openai-agents==1.1.0`, `openai-agents==0.23.1` in a clean venv (`pip install temporalio temporalio-openai-agents openai-agents`).
- Confirmed by direct introspection (`inspect.signature`) that `RetryPolicy.__init__`, `OpenAIAgentsPlugin.__init__`, and `ModelActivityParameters.__init__` match the fields used in the article exactly, and that `workflow.random`, `workflow.now`, `workflow.uuid4`, `workflow.signal`, `workflow.update`, `workflow.wait_condition` all exist on `temporalio.workflow`.
- Ran all three Python examples from the article end-to-end against a real local Temporal dev server (`temporalio.testing.WorkflowEnvironment.start_local()`, which downloads and runs the actual Temporal CLI dev server, here CLI 1.9.1 / Server 1.32.0):
  1. The minimal `AgentStepWorkflow` + `call_model` Activity + `RetryPolicy` — executed, returned the expected result.
  2. The `ApprovalAgentWorkflow` with `@workflow.signal` / `wait_condition` — started, signaled, resolved correctly.
  3. The `SupportAgentWorkflow` wired through `OpenAIAgentsPlugin` + `ModelActivityParameters`, with `Runner.run` making a real OpenAI model call inside a Temporal Activity — executed successfully end-to-end against a live OpenAI API call.
- One real finding from this testing: `temporalio.openai_agents` (the path named in the docs as the "1.0.0" location) only resolves after installing the separate `temporalio-openai-agents` package — it is not bundled in the base `temporalio` package. The article doesn't currently call this out explicitly; noted here in case a human editor wants to add a one-line install note.
