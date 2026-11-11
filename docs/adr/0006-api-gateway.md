---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: platform owner, security lead, integration lead"
---

# ADR-0006: API gateway

## Context and Problem Statement

As the number of systems and consumers grows, direct point-to-point calls become hard to secure, observe and change. A central API edge can enforce authentication, rate limits and schema checks and give one place to publish and version contracts. Should the organisation use one, and what should it look for?

## Decision Drivers

* Consistent authentication and authorisation using the organisation's IdP (OpenID Connect, OAuth 2.0)
* Observability of API traffic
* Ability to define configuration as code and move between gateways
* Support for open specification formats (OpenAPI, AsyncAPI)
* Operational skills and desired level of control
* Cost and licensing model
* Risk of the gateway becoming a bottleneck or a single point of failure

## Considered Options

* **A. Cloud-provider managed gateway**
* **B. Open-source or open-core gateway that you run** (examples: Kong Gateway, Apache APISIX)
* **C. Ingress controller and service mesh only**, with no central API management layer
* **D. No gateway**, direct calls with per-service controls

## Decision Outcome

**Recommended default for a mid-size UK company: a single gateway layer, A or B chosen on skills and existing platform, with configuration as code and published OpenAPI specifications.**

The portability rule matters more than the product: the API definitions, routing rules, policies and consumer registrations live in the organisation's repository in a documented format, and a migration drill shows that a second gateway can serve a sample API from those definitions. Do not put business logic in gateway plug-ins that cannot be reproduced elsewhere.

### Consequences

* Good: one place to enforce authentication, quotas and logging; clearer ownership of contracts.
* Good: the consistent edge simplifies audit and incident response.
* Bad: another component to run, secure and keep highly available.
* Bad: policy languages differ between gateways, so migration still takes work.

### Confirmation

* Every externally exposed API is registered with an owner, specification and authentication method.
* Gateway configuration is built from the repository, with no manual console changes (drift check).
* An annual drill reproduces a sample API on an alternative gateway.

## Pros and Cons of the Options

### A. Cloud-provider managed gateway

* Good: low operational effort, integrated with the provider's identity and logging.
* Bad: tends to tie definitions to proprietary formats; higher switching cost.

### B. Open-source or open-core gateway

* Good: portable declarative configuration, self-hosting option, active ecosystems.
* Bad: you operate it; some features sit behind paid tiers (check which before committing).

### C. Ingress and mesh only

* Good: fewer products for a purely internal, service-to-service estate.
* Bad: weak external consumer management, quotas and developer-facing catalogue.

### D. No gateway

* Good: simplest at very small scale.
* Bad: inconsistent security and visibility as the estate grows.

## More Information

**When to adjust.** Very small estates with few APIs may defer a gateway and use per-service controls, provided the choice is recorded and revisited as consumers grow.

**Related:** [ADR-0001](0001-identity-provider-approach.md), [ADR-0007](0007-event-backbone.md), [ADR-0008](0008-logging-and-retention.md). Product names are examples only.

Review date: 12 months after adoption.
