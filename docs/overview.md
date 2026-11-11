# Overview

## The problem

Mid-size organisations now run their identity, data, integration and increasingly their AI capabilities on a small number of external platforms. That is usually sensible: the platforms are capable, and building everything in-house is rarely the right use of a small team. The risk is not the dependency itself. The risk is a dependency nobody has examined: where the data actually lives, who can compel or access it, whether it can be taken back out in a usable form, and what happens to the business if a supplier changes price, terms, region, ownership or availability.

AI adds new versions of these questions. Prompts, retrieved documents and model outputs can contain personal or commercial data. Models and agents can be swapped, retrained, deprecated or withdrawn by their providers. Decisions made with AI support need an audit trail.

This repository offers a vendor-neutral reference architecture and a set of working documents (decision records, checklists, a maturity model and a small scoring tool) to help an organisation make those dependencies deliberate, visible and reversible where that matters.

## What "sovereignty" means here

The word carries political weight. This repository uses it in a narrow, practical, organisational sense. It is about **how much control an organisation retains over its own digital capabilities**, broken into four questions that can be answered with evidence:

| Dimension | Practical question | Example evidence |
|---|---|---|
| **Data location** | In which country or region is the data stored and processed, including backups, logs, support copies and AI prompts? | Region configuration, data-flow diagram, sub-processor list |
| **Operational control** | Who operates the system, who holds the keys, and who can change or access it, including supplier staff? | Key custody model, access reviews, support-access terms |
| **Legal jurisdiction exposure** | Which legal systems can compel access to the data or the service, given where the supplier and its parent are established and where the data sits? | Transfer risk assessment, supplier corporate structure, contractual commitments |
| **Portability and exit** | Can the organisation move its data, configuration and workloads elsewhere within an acceptable time and cost? | Tested export, documented runbook, contract exit terms |

Sovereignty in this sense is a **spectrum and a set of trade-offs**, not a state an organisation either has or lacks. A fully self-operated stack maximises operational control and also maximises the operational burden, skills requirement and, for a small team, often the security risk.

## What this repository does not claim

- It does not claim that any architecture "guarantees" sovereignty, compliance, or security. Controls reduce specific exposures. Residual risk remains and should be recorded.
- It is not legal advice. The [UK and EU considerations](uk-eu-considerations.md) summarise public sources at a point in time and name their limits. Take advice from a qualified adviser for your own circumstances.
- It does not argue for or against any supplier, country or cloud model. Where examples of products are given in decision records they are illustrations, with no endorsement.
- It is not a certified framework or a standard, and it does not replace one (for example ISO/IEC 27001 or ISO/IEC 42001).
- It has not been validated in a live organisation by independent parties. The recommended defaults are reasoned starting points.

## Principles

1. **Control.** Know who holds the keys, the credentials and the operational levers for each critical capability, and keep enough of them in-house to act when needed.
2. **Portability.** Prefer open standards, open formats and documented interfaces. Keep the ability to move, and test it, rather than assuming it.
3. **Auditability.** Be able to show who did what, with which data, under whose authority, and why a decision was taken. Design the evidence trail in, not on afterwards.
4. **Least privilege.** Grant people, workloads and agents the minimum access for the shortest time that lets them do the job.
5. **Proportionality.** Match the effort to the risk. Not every system needs customer-managed keys or a tested exit plan. Classify first, then spend where the impact justifies it.

The principles pull against each other. Portability can reduce the benefit of a platform's native features. Auditability increases the volume of personal data held in logs. Control costs people and time. The decision records show these trade-offs openly and state what would change the recommendation.

## Scope

**In scope**

- Eight layers: identity and access; data and storage; integration and APIs; AI and ML platform and model serving; orchestration and agents; security and key management; observability; governance and compliance.
- Decision records with recommended defaults for a mid-size UK organisation.
- UK and EU legal touchpoints at a summary level.
- A maturity model, self-assessment and scoring tool.
- An exit-readiness checklist and a six-month adoption roadmap.

**Out of scope**

- Product selection. The repository names categories and a few illustrative examples only.
- Sector-specific regimes (financial services, health, defence, critical national infrastructure), which add their own requirements.
- Detailed implementation guides, infrastructure code and cost models.
- Physical infrastructure, endpoint management and end-user computing, except where they touch the layers above.

## Who it is for

- **Technology leaders** (IT managers and heads of technology) who need a structured way to discuss dependency, control and exit with a board or leadership team.
- **Architects** looking for a decision-record starting point to adapt.
- **Data protection, risk and compliance colleagues** who need to see how technical choices connect to obligations.
- **Hiring managers and recruiters** who want to see how the author approaches architecture and technology leadership. The repository is a portfolio piece as well as a working reference.

The target organisation is a UK or EU business with roughly 50 to 1,000 staff, a small in-house technology team supported by external partners, a mix of SaaS and cloud workloads, and growing interest in AI. The defaults will need adjustment outside that profile.

## How to use this repository

1. **Read this overview**, then the [layered architecture](architecture.md), starting with the layers that matter most to you.
2. **Run the self-assessment.** Copy [`assessment/self-assessment-template.csv`](../assessment/self-assessment-template.csv), score each question from 1 to 5 using the [maturity model](maturity-model.md), and run `python tools/assess.py your-copy.csv`. The output shows weakest layers and a text radar chart.
3. **Read the decision records** for those layers. Each states options, trade-offs, the decision criteria, a recommended default and when to depart from it. Copy a record, change the status, and record your own decision.
4. **Use the [decision matrix template](decision-matrix-template.md)** when you compare candidates for a layer.
5. **Test exit readiness** with the [checklist](exit-readiness-checklist.md) for your most critical platforms.
6. **Plan the work** with the [six-month roadmap](how-to-adopt.md).
7. **Check the legal position** with your own advisers, using [UK and EU considerations](uk-eu-considerations.md) as a briefing, not as an answer.

Terms are defined in the [glossary](glossary.md). Sources are listed in [references](references.md).

## About the author and related work

This repository is maintained by Puliyappottammal Jijesh ([GitHub: pJijesh](https://github.com/pJijesh), [LinkedIn](https://www.linkedin.com/in/pjijesh)), an IT manager and author. His forthcoming book, *The Sovereign Stack*, is related work. This repository is a standalone resource.

The views here are the author's own and do not represent any employer or client. No employer or client data is used.
