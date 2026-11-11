---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: accountable owner, procurement lead, security lead, business owner of each critical platform"
---

# ADR-0009: Exit strategy and portability tests

## Context and Problem Statement

Most organisations have an exit clause somewhere in a contract and few have ever tested leaving. An untested exit plan is an assumption. How much exit planning and testing is proportionate for a mid-size organisation, and how should it be organised?

## Decision Drivers

* Business criticality of each platform and the cost of disruption
* Contractual rights on data return, assistance, notice and deletion
* Statutory switching rights, where they apply (for example the EU Data Act's rules on switching between data processing services, which the [UK and EU considerations](../uk-eu-considerations.md) summarise)
* Availability of open export formats and alternative suppliers
* Effort and cost of testing
* Evidence demanded by customers, auditors and boards

## Considered Options

* **A. Contractual exit terms only**
* **B. Documented exit plan for each critical platform, not tested**
* **C. Tiered approach: documented plans for all critical platforms plus scheduled, scoped portability tests**
* **D. Active multi-provider operation** for critical services, so that exit is continuous

## Decision Outcome

**Recommended default for a mid-size UK company: Option C.**

1. **Tier the platforms.** Tier 1 are platforms whose loss would stop core operations or expose restricted data. Tier 2 are important but replaceable within an agreed time. Tier 3 are low impact.
2. **Tier 1:** a written exit plan (data inventory, export method and format, target options, dependencies, estimated time and cost, decision owner) and an annual **portability test**: export a representative dataset, load it into an alternative environment, verify record counts and integrity, and record elapsed time and gaps.
3. **Tier 2:** exit plan summary and a portability test every two years.
4. **Tier 3:** contract review at renewal; note the data-return clause.
5. **Contract hygiene for Tiers 1 and 2:** data return in a documented open format, assistance period, termination notice, deletion confirmation and a statement of sub-processors. Seek these at procurement, when negotiating leverage is highest.
6. The target **time to exit** is a business decision recorded per platform. This repository does not prescribe numbers.

### Consequences

* Good: turns "we could leave" into evidence; exposes hidden dependencies early; strengthens procurement leverage.
* Bad: tests take time and sometimes cost money (for example egress or duplicate environments).
* Bad: a passed test shows that a sample can be moved, not that every workflow could be recreated quickly. State the limit when reporting results.

### Confirmation

* Exit register listing tiers, plans, last test date, result and open gaps.
* Board or leadership report each year summarising results and residual risk.
* Contract clauses checked at every renewal.

## Pros and Cons of the Options

### A. Contract terms only

* Good: no effort beyond negotiation.
* Bad: no evidence that data and configuration can actually be used elsewhere.

### B. Documented, untested plan

* Good: clarifies dependencies.
* Bad: documents drift and untested steps usually fail under pressure.

### C. Tiered with tests

* Good: proportionate, evidence-based.
* Bad: needs ownership and a calendar.

### D. Active multi-provider

* Good: strongest resilience and bargaining position.
* Bad: costly and complex; usually only justified for a few critical services.

## More Information

**When to adjust.** Increase test frequency for platforms with unstable supplier positions or contract renewals approaching. Reduce scope for platforms with standard exports and low switching complexity.

**Related:** [exit-readiness checklist](../exit-readiness-checklist.md), [ADR-0001](0001-identity-provider-approach.md), [ADR-0003](0003-bring-your-own-key-and-key-custody.md), [ADR-0011](0011-open-data-formats-and-storage-abstraction.md).

Review date: annually.
