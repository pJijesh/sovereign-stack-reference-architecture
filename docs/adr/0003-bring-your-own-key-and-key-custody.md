---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: security lead, data protection lead, accountable owner"
---

# ADR-0003: Bring your own key and key custody

## Context and Problem Statement

Encryption protects data only as well as the control of the keys. Who creates, holds and can use the keys decides what a provider can read at rest and whether the organisation can revoke that ability. How much key custody should a mid-size organisation take on?

## Decision Drivers

* Data classification and the impact of unauthorised access by a provider, a third party or a legal process
* Availability risk: key loss or key-service outage can make data unreadable
* Skills and operational maturity
* Provider support for customer-managed keys across all the services in use
* Ability to revoke access and to destroy data credibly at exit ("crypto-shredding")
* Cost

## Considered Options

* **A. Provider-managed keys** (default encryption at rest; the provider controls the keys)
* **B. Customer-managed keys in the provider's key management service** (often called "bring your own key" or customer-managed keys). Examples: AWS KMS, Azure Key Vault, Google Cloud KMS
* **C. Customer-held keys in an external key manager** where the provider calls out to a key service you operate or an independent supplier operates ("hold your own key"). Example of the self-run category: OpenBao
* **D. Client-side encryption** before data reaches the provider

## Decision Outcome

**Recommended default for a mid-size UK company: B for confidential and restricted data; A for internal and public data; C or D only for a narrow set of restricted data where the added risk and effort are justified.**

Additional rules: key rotation on a defined schedule; separation of duties between key administrators and data administrators; key-use logging sent to the log pipeline (ADR-0008); and an annual **revocation test** on a non-production dataset to prove what happens when access to a key is removed. Backups and replicas must use keys covered by the same policy.

### Consequences

* Good: gives a real lever to restrict provider access at rest and a documented route to render data unreadable at exit.
* Good: modest operational cost with mainstream providers.
* Bad: the key service is usually still operated by the same provider as the data under option B. It limits access at rest but does not remove the provider's operational position or its legal exposure.
* Bad: key loss means data loss. Recovery procedures and dual control are essential.
* Bad: options C and D can break provider features (search, indexing, managed analytics) and add latency and availability dependencies.

### Confirmation

* Inventory showing which datasets use which key option and why.
* Revocation test results, dated and signed off.
* Evidence of key rotation and separation of duties from the key service logs.

## Pros and Cons of the Options

### A. Provider-managed keys

* Good: simplest, no key-loss risk on your side.
* Bad: no customer lever over provider access at rest.

### B. Customer-managed keys in provider KMS

* Good: meaningful control and audit, broad support across services, manageable effort.
* Bad: coverage varies by service; the provider still operates the infrastructure.

### C. External key manager

* Good: strongest separation of key custody from the data host.
* Bad: availability coupling, latency, limited service support, and more to run. If the external key service is down, so is access to the data.

### D. Client-side encryption

* Good: the provider never sees plaintext.
* Bad: the provider cannot search, index or process the data; application complexity rises sharply.

## More Information

**What this does not do.** Customer-managed keys protect data at rest. Data in use is normally processed in plaintext by the host. Confidential computing can narrow that gap but has its own assumptions and limits. Do not describe key custody to customers as protection against all provider or legal access.

**When to adjust.** Move more datasets to B where contracts demand it; use C or D only when you can name the specific threat they address and have the skills to run them.

**Related:** [ADR-0002](0002-data-residency-approach.md), [ADR-0009](0009-exit-strategy-and-portability-tests.md). Product names are examples of a category only.

Review date: 12 months after adoption.
