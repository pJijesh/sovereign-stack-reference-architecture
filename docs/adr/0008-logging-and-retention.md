---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: security lead, data protection lead, legal or compliance adviser, platform owner"
---

# ADR-0008: Logging and retention

## Context and Problem Statement

Logs are essential for security, operations and audit, and they also contain personal data and sometimes sensitive content (user identifiers, IP addresses, prompts and model outputs). Keeping too little undermines investigation and accountability; keeping too much conflicts with data minimisation and storage limitation. How should logging and retention be designed?

## Decision Drivers

* Security detection and incident investigation needs
* Accountability and audit evidence, including AI decision trails
* UK GDPR and EU GDPR principles of data minimisation and storage limitation (Article 5)
* Where applicable, EU AI Act logging duties for high-risk systems (for example Article 26(6): deployers keep logs under their control for at least six months, unless other law provides otherwise)
* Cost of storage and search
* Portability of the log archive and independence from a single SIEM or observability supplier

## Considered Options

* **A. One retention period for all logs**
* **B. Tiered retention by log class**, with an open collection pipeline and portable archive
* **C. Rely on the retention defaults of each product**
* **D. Suppliers' SIEM-native storage only**

## Decision Outcome

**Recommended default for a mid-size UK company: Option B.** Use an OpenTelemetry-compatible collection layer, redact at the collector, and apply retention by class.

Starting points (adjustable and not legal requirements; confirm with your legal or compliance adviser and the sector rules that apply to you):

| Log class | Hot (searchable) | Archive | Notes |
|---|---|---|---|
| Authentication and privileged access | 12 months | Per risk and legal advice | Needed for investigations |
| Audit trail of changes and approvals | 12 months | Per risk and legal advice | Include AI use-case approvals |
| AI gateway: prompts, outputs, tool calls | 30 to 90 days | Only where a decision record is needed | Treat as personal data; redact; restrict access |
| Application logs | 30 to 90 days | Optional | Avoid personal data in payloads |
| Debug and verbose logs | 7 days | None | Disabled by default in production |

Deletion is automated and evidenced. Access to logs is role-based and itself logged. The archive is stored in the agreed region in an open format (for example compressed JSON lines or Parquet).

### Consequences

* Good: balances investigative need against minimisation; supports evidence for audits without a standing pile of personal data.
* Good: open pipeline lets you change the analysis tool without losing history.
* Bad: more design work than a single setting; classes must be maintained.
* Bad: redaction can remove detail that investigators later want, so the design needs an agreed break-glass path.

### Confirmation

* Automated report showing the oldest record per log class against policy.
* Quarterly sample check for personal data in application logs.
* Archive export and re-import test to an alternative tool.

## Pros and Cons of the Options

### A. One retention period

* Good: simple.
* Bad: either too short for security or too long for minimisation.

### B. Tiered by class

* Good: proportionate and explainable.
* Bad: requires classification and tooling.

### C. Product defaults

* Good: no effort.
* Bad: inconsistent, unexplained, often unaligned with policy.

### D. SIEM-native only

* Good: convenient.
* Bad: lock-in, and exit means losing history or paying for extraction.

## More Information

**When to adjust.** Sector regulation, contract terms or litigation holds may require longer periods. Systems that make or support high-risk decisions under the EU AI Act need an explicit logging design. The numbers above are illustrative defaults, not sourced requirements.

**Related:** [ADR-0002](0002-data-residency-approach.md), [ADR-0010](0010-ai-governance-gate.md). Product names are examples only.

Review date: 12 months after adoption, or on any regulatory change.
