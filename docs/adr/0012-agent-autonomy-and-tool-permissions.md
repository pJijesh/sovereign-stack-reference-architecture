---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: accountable executive, security lead, use case owner, data protection lead"
---

# ADR-0012: Agent autonomy and tool permissions

## Context and Problem Statement

Software agents that plan and take actions through tools can save effort, and they can also take wrong or harmful actions quickly, be misled by untrusted content, and act with more access than any person intended. How much autonomy should agents have, and how should their permissions be controlled?

## Decision Drivers

* Impact of a wrong action (financial, legal, reputational, safety, data exposure)
* Reversibility of actions
* Prompt injection and other manipulation through untrusted content
* Least privilege and accountability: every action attributable to an identity and an owner
* Human oversight duties where AI Act or data protection rules apply (for example rules on solely automated decisions)
* Auditability and the ability to stop an agent immediately
* Interoperability: standards for tool interfaces are emerging and still changing

## Considered Options

* **A. No agents**: assistive AI only, a person performs every action
* **B. Assistive agents**: agents prepare actions, a person executes them
* **C. Bounded autonomy**: agents execute within a tool gateway with allow-lists, scopes, spend or volume limits and approval thresholds
* **D. Broad autonomy**: agents act with wide access and minimal approvals

## Decision Outcome

**Recommended default for a mid-size UK company: Option B generally, moving to C for specific, low-impact, reversible tasks that pass the AI governance gate (ADR-0010). Do not adopt D.**

Define autonomy levels and record them per use case:

| Level | Description | Typical controls |
|---|---|---|
| L0 | Suggests only | Read-only access; output reviewed by a person |
| L1 | Prepares actions | Drafts changes; a person approves and executes |
| L2 | Executes low-impact, reversible actions | Tool gateway, per-agent identity, volume and spend caps, full audit log |
| L3 | Executes higher-impact actions | Human approval step above threshold, dual control for the highest-impact actions, kill switch tested |

**Tool permissions.** All tools are accessed through a tool gateway with an allow-list, scoped credentials and schema validation of inputs and outputs. Read tools and write tools are separated. Each agent has its own identity with short-lived credentials. External tool servers and plug-ins (including those using open interface standards such as the Model Context Protocol) are treated as untrusted supply chain components: reviewed, pinned to versions and monitored.

**Untrusted content.** Content retrieved from emails, documents and web pages is treated as data, not instructions. Design assumes the agent may be manipulated and limits what a manipulated agent can do.

**Stop controls.** A kill switch and rate limits exist, are tested and do not depend on the agent's cooperation.

### Consequences

* Good: benefits of automation for appropriate tasks, with bounded downside.
* Good: audit trail and clear accountability.
* Bad: more engineering work than giving an agent a broad API key; some tasks will be slower because of approvals.
* Bad: guardrails reduce but do not eliminate risk; residual risk must be accepted by a named owner.

### Confirmation

* Red-team exercise per quarter for L2 and L3 agents, including injection attempts via retrieved content.
* Review of tool allow-lists and permissions after any change.
* Kill-switch test results.

## Pros and Cons of the Options

### A. No agents

* Good: lowest risk.
* Bad: forgoes benefits; shadow use may emerge anyway.

### B. Assistive agents

* Good: human in control; good starting point.
* Bad: approval fatigue; human review can become nominal.

### C. Bounded autonomy

* Good: efficient with proportionate control.
* Bad: demands engineering of gateways and monitoring.

### D. Broad autonomy

* Good: maximum speed.
* Bad: unacceptable exposure for a mid-size organisation with limited security capacity.

## More Information

**When to adjust.** Higher levels of autonomy suit tasks that are reversible, low value per action and well monitored. Lower levels suit anything touching money, employment, customer commitments or regulated data.

**Related:** [ADR-0001](0001-identity-provider-approach.md), [ADR-0004](0004-model-hosting-options.md), [ADR-0008](0008-logging-and-retention.md), [ADR-0010](0010-ai-governance-gate.md).

Review date: every six months, because tooling and threat knowledge change quickly.
