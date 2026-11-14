> Draft (basic) — pending Aviv's review.

# P9 · RAG

Checklist: [the-checklist.md § RAG](../the-checklist.md)

## What this step decides

How retrieved documents reach the model: sources, ingestion, chunking, embeddings, vector storage, who may see which content, retrieval quality, citation, and deletion.

## How to think about it

- RAG is a search system with an access-control problem. The model sees whatever retrieval returns, so retrieval must enforce the same authorization as the rest of the app.
- Start from the data-source inventory and source authorization: why each source is included and who may read it. Then tenant isolation and retrieval authorization: filter by permission before the model sees anything, never after.
- Deletion has to propagate: when a document or user is deleted, the chunks, embeddings and caches go too (P7).
- Measure retrieval quality separately from answer quality, with real questions. Chunking and embedding choices matter only as measured.

## Options and trade-offs

| Decision | Boring default | Heavier option | Pick the heavier one when |
| --- | --- | --- | --- |
| Vector store | Vector extension in the existing database | Dedicated vector service | Scale or latency measured beyond the database |
| Chunking | Simple fixed size with overlap | Structure-aware chunking | Retrieval eval shows boundary failures |
| Embeddings | Provider hosted model | Self-hosted | Privacy or cost demands it |
| Citations | Link to source chunk | Verified quote extraction | Users rely on exactness |

## How to choose: solo founder / pre-revenue defaults

- Keep vectors next to the source rows so permissions and deletes share one transaction boundary.
- Build a small question set with expected sources before tuning anything.
- Treat retrieved text as untrusted content, per the Prompting guide.

## Human in the loop: escalate when

- Ingesting a new data source, especially user-uploaded or third-party content.
- Any retrieval path that could cross tenant or user boundaries.
- Sending source documents to an embedding vendor (new data recipient, P7).
- Choosing a dedicated vector service (new paid vendor), or an irreversible bulk deletion or re-embedding.

## Done means

- Each source has an authorization rule enforced in retrieval, with a test where user A cannot retrieve user B's content.
- Deleting a source removes its chunks and embeddings (tested), and a retrieval-quality score on a fixed question set is recorded.

## Depends on / feeds into

Depends on P2 · Users, Trust and Data Model, P3 · System Architecture, P6 · Security Foundation, P7 · Privacy and Data Governance. Follows P9 · Model layer. Related to P14 · Search / RAG / Indexing (shared index concerns), P8 · Database, P9 · Evaluation.
