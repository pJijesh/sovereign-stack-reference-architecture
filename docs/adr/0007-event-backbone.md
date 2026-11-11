---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: platform owner, integration lead, data engineering lead"
---

# ADR-0007: Event backbone

## Context and Problem Statement

Events and message queues decouple systems, support replay and enable near-real-time data flow. They also introduce a platform that must be run, secured and governed, and whose protocol shapes how hard it is to move. Should a mid-size organisation adopt an event backbone, and on what terms?

## Decision Drivers

* Real business need for asynchronous flow, replay or fan-out (not fashion)
* Protocol openness and availability of compatible alternatives
* Operational skills and appetite for running stateful infrastructure
* Throughput, ordering and retention needs
* Schema governance (versioned contracts)
* Cost and total effort
* Region, encryption and access control

## Considered Options

* **A. Managed queue or topic service with a proprietary API** from a cloud provider
* **B. Managed service exposing an open protocol** (for example Kafka-compatible or AMQP-compatible services)
* **C. Self-hosted streaming platform** (example: Apache Kafka)
* **D. Lightweight broker** (examples: RabbitMQ, NATS)
* **E. No backbone yet**: use webhooks, scheduled jobs and a transactional outbox until a need is proven

## Decision Outcome

**Recommended default for a mid-size UK company: E until a demonstrated need exists, then B (an open-protocol managed service) or D for simpler workloads.** Avoid C unless you have a team able to run it and a need that justifies it.

Whatever the product, apply four rules: version every event schema in a registry; keep producers and consumers on the open protocol rather than provider-specific client features; set retention deliberately by topic with personal data minimised in payloads; and write an adapter-level replacement plan for any proprietary component.

### Consequences

* Good: avoids operating streaming infrastructure that is not yet needed; the open protocol rule keeps a move feasible.
* Good: schema governance reduces integration breakage.
* Bad: delaying a backbone can mean rework when needs arrive; the outbox pattern and clear contracts reduce that cost.
* Bad: managed open-protocol services may not support every feature of the original software.

### Confirmation

* An event catalogue lists every topic with owner, schema, retention and data classification.
* A portability test replays a sample topic into an alternative broker using the same client library.
* Payload review shows personal data is minimised.

## Pros and Cons of the Options

### A. Managed service with proprietary API

* Good: lowest effort, tight integration.
* Bad: client code and semantics tie you to the provider.

### B. Managed open protocol

* Good: reduced operations, protocol-level portability.
* Bad: compatibility is rarely perfect; still depends on a provider for operation.

### C. Self-hosted streaming platform

* Good: control, rich ecosystem.
* Bad: demanding to operate well; overkill for modest volumes.

### D. Lightweight broker

* Good: simple, quick to adopt, adequate for many task and notification workloads.
* Bad: weaker replay and long-retention features than streaming platforms.

### E. No backbone yet

* Good: minimal complexity.
* Bad: harder to scale integration patterns later without planning.

## More Information

**When to adjust.** Move to B or C earlier if you have multiple consumers needing the same data stream, regulatory replay requirements, or high-volume operational events.

**Related:** [ADR-0006](0006-api-gateway.md), [ADR-0008](0008-logging-and-retention.md), [ADR-0009](0009-exit-strategy-and-portability-tests.md). Product names are examples only.

Review date: 12 months after adoption.
