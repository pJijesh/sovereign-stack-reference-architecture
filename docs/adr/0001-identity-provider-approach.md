---
status: "proposed (reference default, adjustable)"
date: 2026-11-04
decision-makers: "To be completed by the adopting organisation: accountable owner, security lead, data protection lead"
---

# ADR-0001: Identity provider approach

## Context and Problem Statement

Every other layer relies on the identity provider (IdP) to say who or what is acting. Choosing it also decides where the directory lives, who operates it, and how hard it is to leave. How should a mid-size UK organisation provide workforce identity and single sign-on while keeping control and a credible exit path?

## Decision Drivers

* Security capability: phishing-resistant multi-factor authentication, conditional access, privileged access controls, admin audit logs
* Operational burden and available skills in a small team
* Availability: an IdP outage stops almost everything
* Open protocol support (OpenID Connect, SAML 2.0, SCIM) for federation and provisioning
* Location of directory data and support-access paths
* Ability to export users, groups, roles and assignments in a usable form
* Total cost, including licences, operation and migration

## Considered Options

* **A. Managed cloud IdP as the primary provider**, configured for exit (examples of this category: Microsoft Entra ID, Okta)
* **B. Self-hosted open-source IdP** (example: Keycloak)
* **C. Managed IdP plus a self-operated secondary IdP** kept in sync for continuity and as a ready exit target

## Decision Outcome

**Recommended default for a mid-size UK company: Option A, with exit-ready design rules.** The rules are: federate applications over open protocols rather than proprietary connectors where a choice exists; provision over SCIM; avoid depending on features with no equivalent elsewhere without recording the dependency; keep at least two offline, monitored break-glass accounts; export users, groups, roles and application assignments on a schedule into an open format; and rehearse the exit path for the highest-criticality applications.

This is a default, not a rule. Adjust it using the criteria above and the "When to adjust" notes below.

### Consequences

* Good: strong, maintained security controls without a dedicated identity engineering team; lower operational risk than self-hosting for most teams.
* Good: the exit-ready rules turn "we could leave" into something that can be tested.
* Bad: the directory and authentication service sit with a supplier. Supplier outage, policy change and jurisdiction exposure remain residual risks that must be recorded.
* Bad: the exit-ready rules cost some convenience, because native single-vendor features may be simpler to use.

### Confirmation

* Annual restore-and-rebuild drill: reconstruct a sample of 10 applications' access in the alternative IdP or a test instance from the exported data.
* Quarterly review that break-glass accounts work and alert when used.
* Dependency register lists every feature used that has no standards-based equivalent.

## Pros and Cons of the Options

### A. Managed cloud IdP (primary)

* Good: mature security features, high availability engineering, rapid integration with common SaaS.
* Good: low skills overhead.
* Bad: highest concentration of dependency on one supplier; directory data location and support access need contractual and configuration checks.
* Bad: proprietary extensions can quietly increase switching cost.

### B. Self-hosted open-source IdP

* Good: full operational control and data location; open code; no per-user licence for the software itself.
* Bad: you own patching, high availability, backup, and security hardening. For a small team this can make the organisation less secure and less available, not more.
* Bad: advanced features such as device-based conditional access or risk-based sign-in may need additional components.

### C. Managed primary plus self-operated secondary

* Good: continuity if the primary is unavailable, and a rehearsed exit target.
* Bad: double the operating effort, synchronisation complexity, and a risk of configuration drift. Rarely justified below a high criticality or regulatory threshold.

## More Information

**When to adjust.** Move towards B or C if a regulator, contract or data classification requires operation by a party in a specific jurisdiction, if you already have the skills to run it well, or if you need very large numbers of external identities with custom flows (consider a separate customer identity platform in that case). Move away from A if you cannot meet the export and drill rules in practice.

**Related:** [ADR-0003 Bring your own key](0003-bring-your-own-key-and-key-custody.md), [ADR-0009 Exit strategy](0009-exit-strategy-and-portability-tests.md). Product names are examples of a category only and are not endorsements.

Review date: 12 months after adoption, or on a material supplier change.
