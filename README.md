# Sovereign Stack Reference Architecture

[![CI](https://github.com/pJijesh/sovereign-stack-reference-architecture/actions/workflows/ci.yml/badge.svg)](https://github.com/pJijesh/sovereign-stack-reference-architecture/actions/workflows/ci.yml) [![Licence: MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg) [![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.txt)

**Problem:** organisations depend on external platforms for identity, data, integration and AI, often without knowing where their data sits, who can reach it, or how they would leave.

**For:** technology leaders, architects and risk colleagues in UK and EU mid-size organisations, and anyone reviewing how the author approaches architecture and technology leadership.

**Demonstrates:** how to turn "keeping control" into layered design, recorded decisions, sourced legal context, a maturity model and a working scoring tool, while staying vendor-neutral and honest about limits.

![Overview of the reference architecture: consumers reach identity and access, then integration and APIs, then orchestration and agents, the AI and ML platform and data and storage. Security and key management, observability, and governance and compliance apply across all layers.](docs/diagrams/01-overview.png)

## What this is

A documentation-first, vendor-neutral reference architecture for an organisation that wants to keep practical control of its **identity, data, AI and integration layers**: where data lives, who operates the system, which legal systems can reach it, and whether it can be moved out again.

"Sovereignty" here is used in a narrow, practical sense (data location, operational control, legal jurisdiction exposure, portability and exit), not a political one. See the [overview](docs/overview.md) for the definition and for what the repository does **not** claim.

## Map of the repository

```text
.
├── README.md                          you are here
├── docs/
│   ├── overview.md                    problem, principles, scope, definition of sovereignty
│   ├── architecture.md                eight layers, one Mermaid diagram each, plus an overview
│   ├── uk-eu-considerations.md        UK GDPR, EU GDPR, transfers, Data Act, EU AI Act dates (with sources)
│   ├── maturity-model.md              five levels across the layers
│   ├── exit-readiness-checklist.md    sovereignty and exit-readiness checklist
│   ├── decision-matrix-template.md    weighted decision matrix, with a worked fictional example
│   ├── how-to-adopt.md                six-month roadmap for a mid-size organisation
│   ├── glossary.md
│   ├── references.md                  every source, with its type (primary or secondary)
│   ├── adr/                           12 decision records in MADR format, plus a template
│   └── diagrams/                      Mermaid sources (.mmd) and rendered PNGs
├── assessment/
│   ├── self-assessment-template.csv   24 questions, blank scores
│   └── example-filled.csv             fictional sample scores for demonstration
├── tools/
│   ├── assess.py                      scores a filled-in CSV, prints a text radar summary
│   ├── check_links.py                 internal and (optional) external link check
│   ├── check_diagrams.py              diagram sources, embedded blocks and PNGs agree
│   ├── render_diagrams.sh             renders Mermaid sources with mmdc (--check to verify only)
│   └── puppeteer-config.json          browser settings for mmdc in containers and CI
├── tests/                             unit tests (standard library only)
├── .github/workflows/ci.yml           tests, link check, diagram check
├── LICENSE                            MIT (code)
├── LICENSE-DOCS.txt                   CC BY 4.0 (documentation)
└── CONTRIBUTING.md
```

## Where to start

| If you want to... | Go to |
|---|---|
| Understand the idea and its limits | [Overview](docs/overview.md) |
| See the architecture | [Layered architecture](docs/architecture.md) |
| See how decisions are reasoned | [Decision records](docs/adr/README.md) |
| Check the UK and EU legal context | [UK and EU considerations](docs/uk-eu-considerations.md) |
| Score your own position | [Maturity model](docs/maturity-model.md) and the tool below |
| Test whether you could leave a platform | [Exit-readiness checklist](docs/exit-readiness-checklist.md) |
| Plan the work | [Six-month roadmap](docs/how-to-adopt.md) |

## Quick start: score your own position

Python 3.9 or later; no packages to install.

```bash
cp assessment/self-assessment-template.csv my-scores.csv
# fill in the score column (1 to 5) and the evidence column, then:
python tools/assess.py my-scores.csv --target 3
```

Try it on the fictional sample:

```bash
python tools/assess.py assessment/example-filled.csv --target 3
python -m unittest discover -s tests -v
```

The tool prints per-layer scores, the three weakest layers, gaps against a target level and a text radar chart. It validates input and exits with a non-zero status on errors. Use `--json` for machine-readable output.

## Honest limitations

- **Not legal advice.** The UK and EU material summarises public sources as at 4 November 2026. Some points rest on secondary sources, and some could not be verified. The document says which. Law and guidance change, so re-check before relying on it.
- **Not validated in a live organisation.** The recommended defaults are reasoned starting points, written for a mid-size UK organisation. They have not been tested in production by independent parties, and no case studies are offered.
- **No architecture guarantees sovereignty, compliance or security.** Controls reduce specific exposures. Residual risk remains and should be recorded and owned.
- **Vendor-neutral, not exhaustive.** Product names appear only as examples of a category, with no endorsement, ranking or supplier review. Capabilities change quickly, so check current product facts yourself.
- **Self-assessment is self-assessment.** The maturity scores reflect your own judgement. They are not independent assurance, and the level names are not benchmarked against other organisations.
- **Documentation-first.** There are no deployable infrastructure templates or cost models. The Python tools are small and exist to support the assessment and the repository's own checks.
- **Out of scope:** sector-specific regimes (for example financial services or health), cyber security legislation, and detailed implementation guides.
- **Regulatory dates move.** The EU AI Act timeline was amended in 2026 by the Digital Omnibus. The operative text of that amending regulation was not read in full by the author. Dates were checked against the European Commission's AI Act Service Desk and several law-firm commentaries.

## Roadmap

Planned, not promised. Order and timing change with other work.

- **Next:** Add decision record on AI hosting; Add decision record on identity
- **Then:** Add a second worked scoring example; Recheck UK data transfer guidance
- **Later:** Add updated reference diagrams; Release v1.1

## Licensing

This repository uses two licences, because code and documentation have different needs:

- **Code is licensed under the [MIT licence](LICENSE).** This covers the Python scripts and tests in `tools/` and `tests/`, the shell script, configuration files and the CI workflow.
- **Documentation is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-DOCS.txt).** This covers the Markdown documents, diagrams and the assessment CSV templates. You may share and adapt them, including commercially, provided you give appropriate credit, link to the licence and indicate if changes were made.

Suggested attribution: "Based on the Sovereign Stack Reference Architecture by Puliyappottammal Jijesh, https://github.com/pJijesh/sovereign-stack-reference-architecture, CC BY 4.0."

## About the author

Puliyappottammal Jijesh is an IT manager and author. Find him on [GitHub (pJijesh)](https://github.com/pJijesh) and [LinkedIn](https://www.linkedin.com/in/pjijesh). His forthcoming book, *The Sovereign Stack*, is related work; this repository is a standalone resource.

The views here are the author's own and do not represent any employer or client. No employer or client data, systems or examples are used.

Contributions and corrections are welcome. See [CONTRIBUTING](CONTRIBUTING.md).
