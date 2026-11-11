# Sovereignty and exit-readiness checklist

Use this checklist for each critical platform (Tier 1 and Tier 2 in [ADR-0009](adr/0009-exit-strategy-and-portability-tests.md)) before signing, at each renewal, and at least annually. Tick an item only when you can point to evidence. An item that is not applicable should be marked "n/a" with a reason, not ticked.

**Platform:** ____________________  **Tier:** ____  **Business owner:** ____________________  **Date:** ____________

## A. Know what you depend on

- [ ] The platform's purpose, owner, users and business processes it supports are recorded
- [ ] The data held is inventoried and classified (public, internal, confidential, restricted)
- [ ] Data locations are recorded, including backups, logs, support copies, analytics and AI features
- [ ] Sub-processors are listed, with a route to be notified of changes
- [ ] The supplier's corporate structure and the jurisdictions that apply to it are recorded
- [ ] Upstream and downstream integrations are listed with owners
- [ ] Features used that have no standards-based equivalent elsewhere are recorded in a dependency register

## B. Contract and commercial

- [ ] The contract provides for return of data in a documented, open or widely readable format
- [ ] The contract provides for assistance during exit and states its duration and charges
- [ ] Termination rights and notice periods are understood, including termination for a change of control or material change of terms
- [ ] Charges for export and egress are known and budgeted
- [ ] Deletion at end of contract is provided for, with written confirmation
- [ ] Renewal dates and notice windows are in a shared calendar with an owner
- [ ] Statutory switching rights that may apply (for example under the EU Data Act) have been considered. See [UK and EU considerations](uk-eu-considerations.md)
- [ ] The supplier's financial and operational resilience has been considered proportionately

## C. Data portability

- [ ] A full export method exists and is documented (tool, API, bulk file, request process)
- [ ] The export format is documented and readable without the supplier's software
- [ ] The export includes metadata, relationships, history, attachments and audit data, not only the primary records
- [ ] A **portability test** has been run in the last 12 months: representative data exported, loaded into an alternative environment, counts and integrity verified, elapsed time recorded
- [ ] Gaps from the last test are logged with owners and dates
- [ ] Backups are held independently of the supplier where the risk justifies it, and restore has been tested

## D. Configuration, code and logic

- [ ] Configuration, workflows, rules and customisations are exported or recorded in your repository
- [ ] Integrations use documented interfaces and your own specifications, not only the supplier's connectors
- [ ] Business logic embedded in the platform (formulas, automations, scripts) is documented so it can be re-created
- [ ] Infrastructure and platform settings are defined as code where possible

## E. Identity, keys and access

- [ ] Users and roles for the platform come from your identity provider, with provisioning that you can re-point
- [ ] A copy of users, groups, roles and assignments can be exported and rebuilt
- [ ] Encryption keys follow your key policy ([ADR-0003](adr/0003-bring-your-own-key-and-key-custody.md)), and key revocation has been tested where customer-managed keys are used
- [ ] Break-glass access exists that does not depend on the platform being reachable
- [ ] Supplier access to your data (support, engineering) is understood, controlled and logged where possible

## F. Operations and people

- [ ] An exit plan is written: scope, target options, sequence, dependencies, estimated time and cost, decision owner, communication plan
- [ ] The target **time to exit** for this platform is agreed by the business owner and recorded
- [ ] Alternative suppliers or self-hosting options have been identified and, for Tier 1, briefly assessed
- [ ] Staff skills needed to operate the alternative are identified
- [ ] Runbooks exist for continuity if the platform is unavailable for an extended period

## G. AI-specific (where the platform includes or feeds AI features)

- [ ] Models used are identified with versions, hosting location and licence terms
- [ ] Prompts, evaluation sets and tool definitions are held in provider-neutral form in your repository
- [ ] Training or retention of your data by the supplier is addressed in writing
- [ ] Embeddings and indexes can be rebuilt from source documents in another store
- [ ] The AI use case is registered at the [AI governance gate](adr/0010-ai-governance-gate.md)
- [ ] A model swap exercise has been run and results compared

## H. Evidence and decision

- [ ] Results of tests and reviews are filed where an auditor or board member could find them
- [ ] Residual risks are recorded and accepted by a named owner, with a review date
- [ ] The decision to continue, change or exit is recorded as a decision record

## Reading the result

There is no pass mark. A cluster of unticked items in one section shows where to invest. If section C (portability) or section B (contract) is mostly empty for a Tier 1 platform, treat that as a priority finding. Report results with their limits: a passed sample test shows that the sample could be moved, not that every workflow could be recreated in the target time.
