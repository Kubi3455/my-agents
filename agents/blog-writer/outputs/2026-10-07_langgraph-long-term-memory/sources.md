# Sources & Verification — LangGraph Long-Term Memory

## Official documentation
- https://docs.langchain.com/oss/python/langchain/long-term-memory — Store API overview, InMemoryStore/PostgresStore creation, IndexConfig shape
- https://docs.langchain.com/oss/python/langgraph/stores — Store class list (InMemoryStore, PostgresStore, MongoDBStore, RedisStore, UpstashStore), namespace/method signatures, index config with embed/dims/fields
- https://pypi.org/project/langgraph-checkpoint-postgres/ — pip install command, psycopg dependency, `.setup()` requirement, `autocommit=True` / `row_factory=dict_row` requirement for manual connections
- https://github.com/pgvector/pgvector — pgvector Postgres extension (server-side package, not a Python package)

## Claims verified by running real code (not taken on faith)
Environment: Python 3.11 venv (`langgraph==1.2.14`, `langgraph-checkpoint-postgres==3.1.2`, `psycopg[binary]==3.3.6`, `langchain`/`langchain-openai`), against a real local PostgreSQL 16 instance.

1. **InMemoryStore + real OpenAI embeddings (`text-embedding-3-small`, 1536 dims)**: `put`/`get`/`search` all work as documented; a semantic query ("what language does this user code in") correctly ranked the memory about the user's favorite language above an unrelated one (score 0.6522 vs 0.309).
2. **NumPy warning**: Running InMemoryStore with semantic search but without NumPy installed prints: "NumPy not found in the current Python environment. The InMemoryStore will use a pure Python implementation for vector operations..." — reproduced verbatim.
3. **PostgresStore without pgvector installed on the server**: `store.setup()` raises `psycopg.errors.FeatureNotSupported: extension "vector" is not available` with a DETAIL/HINT about the missing extension control file. Reproduced on a stock PostgreSQL 16 install before adding the `postgresql-16-pgvector` package.
4. **PostgresStore with pgvector installed**: After `apt-get install postgresql-16-pgvector`, `setup()` succeeds, and real OpenAI-embedded `put`/`search` return correctly ranked results, matching the InMemoryStore behavior.
5. **Dimension lock-in**: After writing to a PostgresStore table with a 1536-dim embedding, reopening a store against the *same database* with a 384-dim embedding function raises `psycopg.errors.DataException: expected 1536 dimensions, not 384` on the next `put()`. Reproduced exactly as shown in the article (own test, not copied from a forum).
6. **384 dims as a real embedding size**: all-MiniLM-L6-v2 (a widely used sentence-transformers model) outputs 384-dimensional vectors; OpenAI's text-embedding-3-small outputs 1536. Both are standard, documented model specs, not invented numbers.

## Not independently re-verified (secondary/background context only, not used as a specific claim in the article)
- MongoDB's LangGraph.js long-term memory store (mentioned only as "other backends exist," not detailed)
