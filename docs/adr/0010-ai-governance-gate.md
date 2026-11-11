---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: accountable executive, data protection lead, security lead, legal or compliance adviser"
---

# ADR-0010: AI governance gate

## Context and Problem Statement

AI use cases are being proposed from every part of the business, often using external tools. Without a consistent way to review them, the organisation cannot say what AI it uses, on which data, with what oversight, or who is accountable. How should new AI use cases be assessed before they reach production?

## Decision Drivers

* Data protection duties, including assessment of risk and, where required, a data protection impact assessment
* EU AI Act obligations where they apply (prohibited practices, transparency, high-risk requirements, general-purpose AI model duties), with dates summarised in [UK and EU considerations](../uk-eu-considerations.md)
* Proportionality: a drafting assistant and a system that screens job applicants are not the same risk
* Speed: a gate that is too slow pushes use into the shadows
* Evidence for customers, auditors and boards
* Alignment with recognised frameworks (NIST AI Risk Management Framework; ISO/IEC 42001)

## Considered Options

* **A. No formal gate**: rely on general policies
* **B. Ad hoc review by IT or security on request**
* **C. Risk-tiered gate** with intake, tiering, named approvers, minimum evidence per tier and a register
* **D. Full AI management system certified to ISO/IEC 42001**

## Decision Outcome

**Recommended default for a mid-size UK company: Option C, designed so it can grow into D if customers or regulators require certification.**

**Intake.** One short form: purpose, users, data used, whether personal or special category data is involved, model and hosting route (ADR-0004), decisions affected, human oversight, owner.

**Tiering (adjust to your context).**

| Tier | Examples | Minimum evidence | Approver |
|---|---|---|---|
| 1 Low | Internal drafting or summarising with no personal or confidential data | Acceptable use confirmation, registered use case | Line manager and IT |
| 2 Medium | Customer-facing content, internal decision support, personal data involved | Data protection assessment, evaluation results, human review design, supplier terms | Use case owner, data protection lead, security lead |
| 3 High | Affects employment, access to services, credit, safety, or falls into an EU AI Act high-risk category; or any use that might be a prohibited practice | Full impact assessment, bias and robustness testing, human oversight design, logging design, legal review, board-level or equivalent sign-off | Accountable executive with legal advice |

**Gate questions** include: Is this use permitted at all? What is the lawful basis and is a DPIA needed? What is the worst plausible failure and who is harmed? How is human oversight real rather than nominal? How will we monitor drift and incidents? How do we switch the system off? What is the exit route for the model or supplier?

**Register.** Every use case, its tier, approver, evaluation evidence and review date is recorded. Review periodically and on material change.

### Consequences

* Good: proportionate and quick for low-risk uses; rigorous where it counts; provides an inventory.
* Good: produces the artefacts that later certification or regulatory requests will ask for.
* Bad: needs people with time to review. Without capacity the gate becomes a bottleneck.
* Bad: tiering involves judgement; borderline classification under EU AI Act categories needs legal input.

### Confirmation

* Register completeness check: spot-scan expense claims, SaaS discovery and network logs for unregistered AI tools.
* Time-to-decision measure per tier.
* Annual sample review of approved use cases against their original evidence.

## Pros and Cons of the Options

### A. No formal gate

* Good: no overhead.
* Bad: no visibility, accountability or evidence.

### B. Ad hoc review

* Good: low overhead.
* Bad: inconsistent and person-dependent.

### C. Risk-tiered gate

* Good: proportionate, scalable.
* Bad: requires upkeep and training.

### D. Certified management system

* Good: externally assured, recognised.
* Bad: significant effort and cost; may be premature.

## More Information

**When to adjust.** Organisations that sell AI-enabled services, or that serve customers who require certification, should plan for D. Organisations with very little AI activity can run a one-page version of C.

**Standards and law.** See [references](../references.md) for the NIST AI RMF, ISO/IEC 42001 and the EU AI Act text. The AI literacy duty in Article 4 of the EU AI Act was amended by the 2026 Digital Omnibus; check its current wording. This is not legal advice.

**Related:** [ADR-0004](0004-model-hosting-options.md), [ADR-0008](0008-logging-and-retention.md), [ADR-0012](0012-agent-autonomy-and-tool-permissions.md).

Review date: six months after adoption, then annually.
