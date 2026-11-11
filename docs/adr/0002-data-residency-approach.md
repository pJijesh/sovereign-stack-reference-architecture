---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: data protection lead, accountable owner, security lead"
---

# ADR-0002: Data residency approach

## Context and Problem Statement

Customers, regulators and contracts increasingly ask where data is stored and processed. Data also moves in less visible ways: backups, logs, support access, analytics, and now AI prompts and retrieval indexes. How should the organisation decide where each class of data may live, and how should it enforce that decision?

## Decision Drivers

* Legal and contractual requirements about location and transfers (see [UK and EU considerations](../uk-eu-considerations.md))
* Data classification and impact of exposure
* Latency and availability needs
* Provider capabilities: region choice, sub-processor transparency, support-access controls
* Cost and complexity of running more than one location
* The difference between **residency** (where data is) and **jurisdiction exposure** (which legal systems may reach it)

## Considered Options

* **A. Classification-driven regional pinning** on a major cloud or SaaS provider, to a UK or EU region, with contractual and technical controls
* **B. Provider established and operated in the UK or EU** for the most sensitive classes
* **C. Self-operated or co-located infrastructure** for the most sensitive classes
* **D. No explicit residency policy**: accept each provider's global default

## Decision Outcome

**Recommended default for a mid-size UK company: a classification-driven approach combining A with B or C only where a class justifies it.**

1. Define four classes (public, internal, confidential, restricted) and record the permitted locations for each.
2. Public and internal data may use any region the supplier contract allows. Confidential data is pinned to the UK or EU, including backups, logs and AI processing. Restricted data is pinned to the UK, or to a named location, and also gets the strongest key and access controls (ADR-0003).
3. Every system records its data locations in the catalogue, including sub-processors and support-access paths. "Region" settings are checked by automated policy, not by one-off review.
4. Residency decisions for personal data are made alongside a transfer assessment. Storing data in a UK or EU region does not by itself resolve onward access or jurisdiction questions, and the record says so.

### Consequences

* Good: effort goes where impact is highest; the policy is explainable to customers and auditors.
* Bad: classification takes real effort and must be kept current.
* Bad: not every SaaS product offers regional choice for all components (support tooling, analytics, AI features may differ). Some exceptions will need risk acceptance with a named owner.
* Bad: a UK region from a non-UK supplier reduces some exposures but not all.

### Confirmation

* A data-location register, reviewed quarterly, with automated checks for non-compliant regions.
* Supplier sub-processor change notices are reviewed within an agreed time.
* A sample of systems is traced end to end each year, including backups and logs.

## Pros and Cons of the Options

### A. Classification-driven regional pinning

* Good: practical, proportionate, uses capabilities most providers already offer.
* Bad: relies on provider assurances for what happens behind the region setting; exposure to the provider's home-country legal reach remains.

### B. UK or EU established provider

* Good: reduces some forms of foreign legal exposure; may suit contracts that require it.
* Bad: narrower product range, possible capability or scale gaps; supplier concentration and viability still need assessment. Establishment in the UK or EU does not by itself prevent every foreign legal claim, for example through corporate ownership.

### C. Self-operated or co-located

* Good: maximum control over placement and access.
* Bad: highest cost and skills demand; security and resilience become your responsibility entirely.

### D. No explicit policy

* Good: zero effort now.
* Bad: you cannot answer a customer, regulator or board question with evidence; accidental non-compliant placement is likely.

## More Information

**When to adjust.** Tighten if a customer contract, regulator or sector rule demands specific locations or operators. Loosen for data that is genuinely public. Revisit after any change to the UK-EU or UK-US transfer position (see [UK and EU considerations](../uk-eu-considerations.md)).

**Related:** [ADR-0003](0003-bring-your-own-key-and-key-custody.md), [ADR-0004](0004-model-hosting-options.md), [ADR-0008](0008-logging-and-retention.md). Not legal advice.

Review date: 12 months after adoption.
