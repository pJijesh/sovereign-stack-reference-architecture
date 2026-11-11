# Architecture decision records

Records follow the [MADR](https://adr.github.io/madr/) structure (Markdown Architectural Decision Records), with two additions: a **recommended default** for a mid-size UK organisation, and an explicit **"When to adjust"** note.

Every record is a *proposed reference default*. Copy it, change the status, record your own context and criteria, and name an accountable owner. Product names are examples of a category only. They are not endorsements and no supplier has reviewed or paid for them.

| ADR | Decision | Layer |
|---|---|---|
| [0001](0001-identity-provider-approach.md) | Identity provider approach | Identity and access |
| [0002](0002-data-residency-approach.md) | Data residency approach | Data and storage |
| [0003](0003-bring-your-own-key-and-key-custody.md) | Bring your own key and key custody | Security and key management |
| [0004](0004-model-hosting-options.md) | Model hosting options | AI and ML platform |
| [0005](0005-vector-store-selection-criteria.md) | Vector store selection criteria | AI and ML platform |
| [0006](0006-api-gateway.md) | API gateway | Integration and APIs |
| [0007](0007-event-backbone.md) | Event backbone | Integration and APIs |
| [0008](0008-logging-and-retention.md) | Logging and retention | Observability |
| [0009](0009-exit-strategy-and-portability-tests.md) | Exit strategy and portability tests | Governance and compliance |
| [0010](0010-ai-governance-gate.md) | AI governance gate | Governance and compliance |
| [0011](0011-open-data-formats-and-storage-abstraction.md) | Open data formats and storage abstraction | Data and storage |
| [0012](0012-agent-autonomy-and-tool-permissions.md) | Agent autonomy and tool permissions | Orchestration and agents |

Use [0000-template.md](0000-template.md) to add your own.
