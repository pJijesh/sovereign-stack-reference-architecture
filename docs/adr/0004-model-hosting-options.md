---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: accountable owner, data protection lead, security lead, AI use case owners"
---

# ADR-0004: Model hosting options

## Context and Problem Statement

Language and other AI models can be consumed as a managed service or run on infrastructure the organisation controls. The choice affects data exposure, cost, quality, skills needs and exit options. Which hosting approach should a mid-size UK organisation use, and how should it avoid being locked to one model or provider?

## Decision Drivers

* Data classification of prompts, retrieved content and outputs
* Contractual terms on data use, retention, training, sub-processors and region
* Capability required: the best available managed models may outperform models you can self-host for some tasks
* Cost profile: per-use pricing against fixed infrastructure cost at realistic utilisation
* Skills: operating GPU infrastructure and model serving is specialised
* Licence terms of any model you host
* Ability to swap models as the market and providers' terms change
* Legal duties, including transparency and risk obligations under the EU AI Act where applicable

## Considered Options

* **A. Managed API, public endpoint**: the provider hosts and operates the model; you call it over the internet. Examples of the category: hosted APIs from model developers, or models offered through a cloud provider's AI service
* **B. Managed service with regional or private endpoint and negotiated terms**: as A, with a chosen region, private connectivity, and contractual commitments on retention and training use
* **C. Self-hosted open-weight model** on infrastructure you operate or rent (serving software examples: vLLM, Ollama for development use)
* **D. Hybrid with a routing gateway**: a mix of B and C selected by data classification and use case, behind an internal AI gateway

## Decision Outcome

**Recommended default for a mid-size UK company: Option D, starting with B and adding C only for workloads that need it.**

1. Put an internal **AI gateway** in front of every model. Applications call the gateway, never a provider directly. This is the main anti-lock-in control.
2. Route by classification. Public and internal data may go to B. Confidential data goes to B only if contract terms and region meet policy, otherwise to C. Restricted data stays on C or on an approved private endpoint.
3. Do not stand up self-hosted serving until a use case demonstrates the need (sensitivity, cost at volume, or capability fit). Many organisations will find B sufficient for a long time.
4. Record each model's licence, version, owner, evaluation results and deprecation date in a model registry.
5. Keep prompts, evaluation sets and tool definitions in your repository in provider-neutral form so that a model swap is a test exercise, not a rewrite.

### Consequences

* Good: sensitive data has a path that keeps inference under your control; the gateway gives central logging, quotas, redaction and a swap point.
* Good: avoids premature investment in GPU operations.
* Bad: you must maintain a gateway and a routing policy, and keep them current.
* Bad: results differ between models, so each swap needs regression evaluation.
* Bad: "open-weight" models vary widely in licence conditions and are not necessarily open source. Legal review of the licence is part of adoption.

### Confirmation

* No application has direct provider credentials (checked through secrets scanning and egress rules).
* A swap exercise each year: replace the model for one use case and compare evaluation results.
* Contract terms on retention and training use are filed for every managed model service.

## Pros and Cons of the Options

### A. Managed API, public endpoint

* Good: fastest start, strongest models available, no infrastructure to run.
* Bad: data leaves your environment; terms and regions may be limited; provider changes can affect you at short notice.

### B. Managed with regional or private endpoint and negotiated terms

* Good: keeps managed quality with better placement and contractual protection.
* Bad: still a third-party operator and possibly foreign legal exposure; availability of regional capacity and models varies.

### C. Self-hosted open-weight

* Good: control over where inference runs, what is logged and when models change.
* Bad: skills, capacity planning and security burden; model quality gap for some tasks; unit cost can be higher at low utilisation.

### D. Hybrid with gateway

* Good: proportionate; keeps options open.
* Bad: more moving parts; needs disciplined routing policy and testing.

## More Information

**When to adjust.** Go further towards C if regulation or contract forbids external processing of the relevant data, or if sustained volume makes fixed-cost hosting cheaper (check this with your own numbers, not with assumptions). Stay with A or B if you lack the skills to run C safely.

**Related:** [ADR-0005](0005-vector-store-selection-criteria.md), [ADR-0010](0010-ai-governance-gate.md), [ADR-0012](0012-agent-autonomy-and-tool-permissions.md). Product names are examples only.

Review date: every six months, because the model market changes quickly.
