# How to adopt: a six-month roadmap

This roadmap is written for a mid-size organisation with a small in-house technology team, support from external partners, and limited time. It assumes you are starting from a typical position: a mix of SaaS and cloud workloads, a central identity provider, some data and AI experimentation, and little formal exit or AI governance.

It is a plan to adapt, not a promise of results or a statement about how long any specific organisation will take. Dates, effort and owners are yours to set.

## Principles for the programme

- **Start with evidence, not architecture.** Know what you have before deciding what to change.
- **Protect the critical few first.** Focus on the handful of platforms and datasets whose loss or exposure would hurt most.
- **Make small, testable changes.** One drill that works is worth more than a long policy.
- **Keep leadership informed.** A short monthly note with decisions needed and risks.
- **Stop when it is proportionate.** Not every layer needs to reach the highest level.

## Roles

| Role | Responsibility |
|---|---|
| Executive sponsor | Removes blockers, accepts residual risk, owns the budget |
| Programme owner (for example the IT manager or head of technology) | Runs the plan, reports, owns the decision records |
| Data protection lead | Transfers, DPIAs, records of processing, retention |
| Security lead | Keys, secrets, logging, access, testing |
| Platform and business owners | Own each critical platform's exit plan and tests |
| Procurement or commercial lead | Contract terms, renewals, supplier engagement |
| External partners | Implementation help; must not own the decisions |

## Month 1: Baseline

**Goal:** a shared, evidenced picture of where you are.

- Build an inventory of platforms, data stores, AI tools and integrations, with owners.
- Classify data (public, internal, confidential, restricted) at the level of systems, not individual files.
- Record data locations, sub-processors and renewal dates for the top platforms.
- Run the [self-assessment](maturity-model.md) with at least two people scoring independently, and agree the evidence.
- Tier platforms (Tier 1 critical, Tier 2 important, Tier 3 low) per [ADR-0009](adr/0009-exit-strategy-and-portability-tests.md).
- Agree a target maturity level per layer, using proportionality.

**Deliverables:** inventory, data location register (draft), assessment results, tier list, target levels.
**Decision gate:** sponsor confirms scope, tiers and targets.

## Month 2: Foundation decisions

**Goal:** make the cross-cutting decisions that everything else depends on.

- Adapt and adopt decision records for identity ([ADR-0001](adr/0001-identity-provider-approach.md)), data residency ([ADR-0002](adr/0002-data-residency-approach.md)), key custody ([ADR-0003](adr/0003-bring-your-own-key-and-key-custody.md)) and exit ([ADR-0009](adr/0009-exit-strategy-and-portability-tests.md)).
- Review contracts for Tier 1 platforms against section B of the [exit-readiness checklist](exit-readiness-checklist.md). Note renewal dates where terms can be improved.
- Brief the data protection lead on the [UK and EU considerations](uk-eu-considerations.md) and agree which items need professional advice.
- Create the decision register and name an owner for each decision.

**Deliverables:** four adopted or consciously amended decision records, contract findings, advice list.
**Decision gate:** sponsor accepts or amends the decisions.

## Month 3: Identity, keys and logging

**Goal:** harden the foundations that give the most control for the least effort.

- Identity: confirm break-glass accounts, privileged access process, joiner-mover-leaver flow, and set up a scheduled export of users, groups and role assignments.
- Keys: apply the key policy to confidential and restricted data stores; run a revocation test on a non-production dataset.
- Logging: define log classes and retention ([ADR-0008](adr/0008-logging-and-retention.md)); set up redaction for the highest-volume sources; confirm archive location.
- Secrets: remove credentials from code and configuration for Tier 1 systems.

**Deliverables:** export job running, key policy applied, revocation test result, log class policy, secrets clean-up list.
**Decision gate:** security lead confirms residual risks and exceptions.

## Month 4: AI governance and gateway

**Goal:** bring AI use under control without stopping useful work.

- Stand up the AI use case register and the [governance gate](adr/0010-ai-governance-gate.md), starting with a one-page intake form and three tiers.
- Register existing AI use, including tools staff already use. Handle it as discovery, not as enforcement.
- Choose the model hosting approach ([ADR-0004](adr/0004-model-hosting-options.md)) and pilot an AI gateway with one or two use cases.
- Set the agent autonomy policy ([ADR-0012](adr/0012-agent-autonomy-and-tool-permissions.md)): default to assistive agents, define levels.
- Agree what staff training is needed, and check the current wording of the EU AI Act literacy provision with your adviser if it applies.

**Deliverables:** AI register, gate process, gateway pilot, model hosting decision, agent policy.
**Decision gate:** accountable executive approves the gate and the first use cases.

## Month 5: Exit and integration tests

**Goal:** turn exit plans into evidence.

- Write exit plans for Tier 1 platforms (use the checklist).
- Run the first **portability tests** on two or three Tier 1 platforms: export, load elsewhere, verify, record time and gaps.
- Review the API and event landscape ([ADR-0006](adr/0006-api-gateway.md), [ADR-0007](adr/0007-event-backbone.md)): publish specifications for the most important integrations and put them in your repository.
- For data platforms, run a read test with a second engine on one curated dataset ([ADR-0011](adr/0011-open-data-formats-and-storage-abstraction.md)).
- Log gaps and agree remediation owners.

**Deliverables:** exit plans, test reports, gap log, integration specification baseline.
**Decision gate:** business owners confirm target times to exit and accept residual gaps.

## Month 6: Assure and embed

**Goal:** show progress, make it routine and plan the next cycle.

- Re-run the self-assessment with the same scorers and compare to month 1. Challenge scores with someone outside the team.
- Report to the board or leadership: what changed, evidence, residual risks, decisions needed, and the plan for the next 12 months.
- Calendar the recurring activities: portability tests, revocation tests, access reviews, decision record reviews, AI register reviews, contract renewals.
- Decide which layers to take to the next level and which to hold.
- Capture lessons learned and adjust the decision records.

**Deliverables:** reassessment, board report, calendar of recurring tests, next-year plan.
**Decision gate:** sponsor approves continuing scope and budget.

## Measuring progress

Use your own measures, defined in month 1. Examples of useful ones (all counts from your own records, no external benchmark implied):

- Number of Tier 1 platforms with a written exit plan, and with a test in the last 12 months
- Number of AI use cases registered, and with a recorded tier and approver
- Number of datasets with owner, classification and residency recorded
- Number of open gaps from tests, and their age
- Self-assessment scores by layer, month 1 against month 6

## Common risks and responses

| Risk | Response |
|---|---|
| Programme becomes a documentation exercise | Require a test or drill as the output of each month, not only a document |
| Scope creep into every system | Hold to the critical few until month 6 |
| Staff see the AI gate as a block | Keep tier 1 quick; publish decision times; offer approved tools |
| Supplier will not cooperate on exit terms | Record as a risk, use renewal timing and the checklist to build the case, consider alternatives |
| Skills gap for self-hosting | Default to managed services with exit-ready design; buy help for specific tasks |
| Over-reliance on one external partner | Keep decisions and documentation in your own repository |
| Legal position changes mid-programme | Review the [UK and EU considerations](uk-eu-considerations.md) quarterly and after major events |

## What to defer

Unless a clear need exists, defer: self-hosted streaming platforms, running your own identity provider, external key managers, broad agent autonomy, and building a custom AI platform. Revisit in the next planning cycle.
