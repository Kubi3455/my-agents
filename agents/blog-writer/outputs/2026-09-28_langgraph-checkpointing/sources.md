# Kaynaklar
- https://docs.langchain.com/oss/python/langgraph/persistence (checkpointer'lar, thread_id, PostgresSaver.setup)
- https://docs.langchain.com/oss/python/langgraph/durable-execution (durability: sync/async/exit anlamları)
- https://docs.langchain.com/oss/python/langgraph/use-time-travel
- https://pypi.org/project/langgraph-checkpoint-sqlite/ , https://pypi.org/project/langgraph-checkpoint-postgres/
- github.com/langchain-ai/langgraph issue #7094 (varsayılan durability="async")
- Yerel test: langgraph 1.2.12, langgraph-checkpoint 4.2.0, langgraph-checkpoint-sqlite 3.1.1. Çökme/devam, durability sayımları, time travel çatallama, eksik thread_id ValueError, SQLite thread ProgrammingError, AsyncSqliteSaver import
