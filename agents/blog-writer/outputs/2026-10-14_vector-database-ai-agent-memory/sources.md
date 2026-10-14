# Sources & Verification — Vector Database for AI Agent Memory

## Live-tested (venv at /tmp/vdb_venv, real local services, 2026-10-14)
- Postgres 16 + `postgresql-16-pgvector` (apt package, pgvector extension v0.6.0) running locally; `psycopg==3.3.6`, `pgvector==0.5.1` Python packages installed via `pip install psycopg[binary] pgvector`.
  - Created `agent_memory` table, HNSW index (`CREATE INDEX ... USING hnsw`), ran a filtered similarity query (`WHERE agent_id = ...`) — only the matching agent's rows returned.
  - Default `hnsw.ef_search` confirmed live via `SHOW hnsw.ef_search` → `40`.
  - Set `maintenance_work_mem = '1MB'`, built an HNSW index on 20,000 rows of 128-dim vectors, captured the real Postgres NOTICE via `conn.add_notice_handler`: `"Building will take significantly more time."`
  - Confirmed `hnsw.iterative_scan` does not exist on this (0.6.0) build — `psycopg.errors.InvalidName: invalid configuration parameter name "hnsw.iterative_scan"` — consistent with that feature being added in pgvector 0.8.0 (per official GitHub release notes, not live-tested since only 0.6.0 was available via apt).
  - Dimension mismatch: inserting a 5-dim vector into a `vector(8)` column raised `psycopg.errors.DataException: expected 8 dimensions, not 5`.
- `qdrant-client==1.19.1` against local in-memory mode (`QdrantClient(":memory:")`).
  - Created collection, upserted points with `agent_id` payload, ran `query_points()` with a `FieldCondition` filter — only the matching tenant's point returned.
  - Confirmed `client.search()` does not exist on this version: `AttributeError: 'QdrantClient' object has no attribute 'search'`.
  - Dimension mismatch: `ValueError: Wrong input: Vector dimension error: expected dim: 8, got 5 for vector ''`.
- `chromadb==1.5.9` via `PersistentClient` (local on-disk, no server).
  - Created collection, added points with `agent_id` metadata, ran `collection.query(..., where={"agent_id": ...})` — only the matching tenant's document returned.
  - Dimension mismatch: `chromadb.errors.InvalidArgumentError: Collection expecting embedding with dimension of 8, got 5`.
- Installed package versions cross-checked against PyPI (`pip index versions qdrant-client/chromadb/pgvector/psycopg`) to confirm they match the current releases cited below.

## Doc-verified only (not independently live-tested on this run)
- pgvector HNSW default build params (`m=16`, `ef_construction=64`) and `maintenance_work_mem` / Docker `--shm-size` guidance: https://github.com/pgvector/pgvector#hnsw
- pgvector current release v0.8.7 (Oct 1, 2026) and the 0.8.0 changelog item adding `hnsw.iterative_scan`: https://github.com/pgvector/pgvector/tags and https://github.com/pgvector/pgvector/releases
- Qdrant multi-tenancy guidance (payload partitioning, `is_tenant: true` since v1.11.0, `payload_m`, dedicated/tiered shards, ~20,000-point promotion threshold, 1,000-collection Cloud cap): https://qdrant.tech/documentation/guides/multiple-partitions/
- Qdrant current release v1.19.2 (Oct 5, 2026): https://github.com/qdrant/qdrant/releases
- Chroma single-node deployment model, no built-in replication/clustering, HNSW segment loaded into process memory: https://cookbook.chromadb.dev/core/system_constraints/
- Chroma current release v1.5.9 (May 5, 2026): https://github.com/chroma-core/chroma/releases

## Internal link targets (confirmed in data/post-inventory.json, 2026-10-14 refresh)
- langgraph-long-term-memory (WP 1650)
- crewai-unified-memory-system (WP 1613)
- semantic-caching-llm-agents (WP 1637) — note: actual slug is `semantic-caching-llm-agents`, title uses "for"; used slug-accurate URL in content.
- mcp-context-bloat (WP 1619)
- ai-agent-rate-limits (WP 1625)
