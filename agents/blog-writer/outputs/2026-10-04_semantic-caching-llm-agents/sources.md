# Sources — Semantic Caching for LLM Agents

## Official / primary sources
- GPTCache GitHub repo (API, adapter behavior, lazy-install mechanism): https://github.com/zilliztech/GPTCache
- Redis LangCache concepts docs (cacheId, Attributes, embedding provider, search strategy, default similarity threshold 0.85, recommended range 0.8–0.9): https://redis.io/docs/latest/develop/ai/context-engine/langcache/concepts/
- Redis blog, "Prompt caching vs semantic caching" (cost reduction up to 73–90%, ~15x latency improvement on hits, double-caching concept): https://redis.io/blog/prompt-caching-vs-semantic-caching/
- arXiv:2411.05276, "GPT Semantic Cache: Reducing LLM Costs and Latency via Semantic Embedding Caching" (cache hit rate 61.6–68.8%): https://arxiv.org/abs/2411.05276

## Personally verified (this session, not an external citation)
Ran in a clean Python 3.11 venv (`/tmp/venv_gptcache`), gptcache 0.1.44:
- `pip install gptcache` alone does NOT install onnxruntime, transformers, sqlalchemy, or faiss-cpu; GPTCache's lazy-install (`subprocess.check_call("pip install ...")`) does not reliably land packages in the active venv — confirmed by reproducing the `PipInstallError` / `ModuleNotFoundError` chain, then installing each dependency manually.
- Latest `transformers` (5.18.0 at test time) breaks GPTCache's bundled `Onnx` embedding wrapper: `AlbertTokenizer has no attribute encode_plus` (fast tokenizer no longer exposes that method). Pinning `transformers==4.36.2` + `tokenizers<0.20` resolved it.
- `put()`/`get()` with plain string prompts requires `cache.init(..., pre_embedding_func=get_prompt)`; without it, `put()` raises `TypeError: 'NoneType' object is not subscriptable` because the default pre-processor expects an OpenAI-style `messages` list.
- Confirmed working end-to-end: `put("How do I reset my password?", "...")` → `get("How do I change my password?")` returns the cached answer; `get("What's the weather in Tokyo?")` returns `None` (correct miss).

## Internal links used
- https://www.firstevolvenextscale.com/ai-agent-rate-limits/
- https://www.firstevolvenextscale.com/mcp-context-bloat/
- https://www.firstevolvenextscale.com/crewai-unified-memory-system/
- https://www.firstevolvenextscale.com/agent-tracing-observability/
(4 internal links in prose; see SEO_LINKING pass for final count/placement)
