---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: platform owner, data protection lead, AI use case owner"
---

# ADR-0005: Vector store selection criteria

## Context and Problem Statement

Retrieval-augmented generation and semantic search need a store for embeddings. The market includes databases with vector extensions, dedicated vector databases, search engines with vector support and managed proprietary services. Rather than name a winner, how should the organisation decide, and what must any choice support to keep control, portability and auditability?

## Decision Drivers

* Corpus size and query volume, now and in a realistic planning horizon
* Permission-aware retrieval: results must respect the caller's entitlements on the source documents
* Deletion: ability to remove vectors and metadata when source data is erased or expires
* Filtering and hybrid search (keyword plus vector)
* Operational fit: can your team already run it?
* Region, encryption and key control
* Export: vectors, metadata and the embedding model identity can be extracted
* Licence and governance of the software

## Considered Options

* **A. Vector extension in an existing governed relational database** (example: PostgreSQL with pgvector)
* **B. Dedicated open-source vector database** (example: Qdrant)
* **C. Search engine with vector capability** (example: OpenSearch)
* **D. Managed proprietary vector service**

## Decision Outcome

**Recommended default for a mid-size UK company: start with A where the corpus and query load are modest; move to B or C when measured needs (scale, latency, filtering, hybrid search) exceed what A delivers.** Treat D as acceptable only if it meets the mandatory criteria below.

**Mandatory criteria for any option:**

1. Metadata filtering that enforces document-level access control at query time, tested with a deliberate cross-user leakage test.
2. Deletion that removes vectors and metadata and can be evidenced.
3. Encryption at rest with keys under the organisation's key policy (ADR-0003) and regional placement per ADR-0002.
4. Export of vectors, metadata and the identity and version of the embedding model, in a documented format.
5. Audit logging of administrative actions and, where needed, queries.

**Weighted criteria** (use the [decision matrix template](../decision-matrix-template.md)): operational fit, scale headroom, hybrid search quality, cost, community and vendor health, licence terms.

### Consequences

* Good: starting with A reduces the number of systems to secure and back up, and lets you reuse existing controls.
* Good: the mandatory criteria stop retrieval from becoming an unmanaged copy of confidential data.
* Bad: A may not scale or filter as well as dedicated systems under heavy load; migration later requires re-indexing, which is manageable if the source documents and embedding configuration are kept.
* Bad: embeddings derived from personal data should be treated as potentially personal data in your risk assessment. Take advice for your circumstances.

### Confirmation

* Leakage test passes before launch and after each major change.
* Erasure test: delete a source record and show it can no longer be retrieved.
* Re-index drill: rebuild the index in an alternative store from source documents.

## Pros and Cons of the Options

### A. Extension in an existing relational database

* Good: one system to run, consistent backup and access control, familiar skills.
* Bad: performance ceilings at higher scale; fewer specialised features.

### B. Dedicated open-source vector database

* Good: purpose-built performance and filtering; open code allows self-hosting.
* Bad: another system to operate and secure; maturity varies by product.

### C. Search engine with vector support

* Good: strong hybrid keyword and vector search; may already exist in the estate.
* Bad: resource heavy; operational complexity.

### D. Managed proprietary service

* Good: least operational effort.
* Bad: export, deletion evidence and region controls vary; highest lock-in risk.

## More Information

**When to adjust.** If your corpus is large from the outset, or latency requirements are strict, begin with B or C. If you have no capacity to run additional data services, a managed option that meets the mandatory criteria may be the right answer.

**Related:** [ADR-0002](0002-data-residency-approach.md), [ADR-0004](0004-model-hosting-options.md), [ADR-0011](0011-open-data-formats-and-storage-abstraction.md). Product names are examples only.

Review date: 12 months after adoption.
