---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: data platform owner, architecture lead, data protection lead"
---

# ADR-0011: Open data formats and storage abstraction

## Context and Problem Statement

Where analytical and archival data is stored in a vendor's proprietary format, leaving means conversion at best and loss at worst. Open file and table formats let different engines read the same data. How far should the organisation go in adopting open formats and a storage abstraction?

## Decision Drivers

* Ability to change compute and analytics engines without bulk conversion
* Performance and feature needs (transactions, schema evolution, time travel)
* Skills and tooling maturity
* Cost, including storage and egress
* Governance: catalogue, lineage, classification, deletion
* Compatibility claims often differ from reality, so tests matter more than labels

## Considered Options

* **A. Proprietary warehouse storage** (data lives in the vendor's internal format)
* **B. Open file format in object storage** (for example Apache Parquet) with a catalogue
* **C. Open table format over object storage** (examples: Apache Iceberg, Delta Lake) with a catalogue
* **D. A vendor lakehouse that can export or expose open formats on request**

## Decision Outcome

**Recommended default for a mid-size UK company: Option C for analytical and archival data that matters, with B for simple cases. Treat A and D as acceptable only where an export and read-back test is passed.**

Operational databases stay on standard SQL engines. Their portability comes from logical dumps, schema in version control and restore tests (see ADR-0009), not from open table formats.

Rules: object storage access through a thin abstraction layer in code; no dependence on vendor-specific features without recording the dependency; data catalogue with owner, classification, residency tag and retention; storage region per ADR-0002.

### Consequences

* Good: engines can be replaced or added; data remains readable for the life of the format.
* Good: aligns with deletion and retention governance through the catalogue.
* Bad: more assembly than a single proprietary service; needs data engineering skill.
* Bad: "S3-compatible" and "Iceberg-compatible" are partial claims in practice. Test the features you use.
* Bad: table-format row-level deletes and compaction need care to meet erasure and retention duties, because deleted data may persist in older files until cleaned up.

### Confirmation

* Quarterly read test of a curated table with a second engine.
* Erasure test: delete a record and show physical removal after compaction and expiry processes.
* Catalogue completeness report.

## Pros and Cons of the Options

### A. Proprietary storage

* Good: simplest, tightly optimised.
* Bad: export may be slow, costly or lossy; strongest lock-in.

### B. Open files with catalogue

* Good: very portable, simple.
* Bad: no transactions or schema evolution features.

### C. Open table format

* Good: transactions, schema evolution, multi-engine access, portability.
* Bad: operational complexity; catalogue choice becomes a dependency.

### D. Vendor lakehouse with open export

* Good: convenience with some portability.
* Bad: portability depends on contract and testing, not on design.

## More Information

**When to adjust.** If the analytical estate is small and a managed warehouse meets all needs, option D with a tested export may be proportionate. Large or long-lived archives justify C earlier.

**Related:** [ADR-0002](0002-data-residency-approach.md), [ADR-0005](0005-vector-store-selection-criteria.md), [ADR-0009](0009-exit-strategy-and-portability-tests.md). Product names are examples only.

Review date: 12 months after adoption.
