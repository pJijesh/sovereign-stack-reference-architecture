# Contributing

Thank you for considering a contribution. This is a documentation-first reference, so corrections, sources and clearer wording are as valuable as new content.

## What is welcome

- Corrections to facts, dates or links, **with a source**. Legal and regulatory facts must cite a primary source where one exists, and say when only a secondary source was available.
- New or improved architecture decision records using [the template](docs/adr/0000-template.md).
- Clearer maturity descriptors, checklist items and glossary entries.
- Bug fixes and tests for the Python tools.

## What is not welcome

- Vendor promotion. Product names may appear only as examples of a category (two or three at most per decision), with no endorsement or ranking.
- Invented statistics, market-share figures or case studies. If a number matters, cite its source.
- Content from or about any employer or client, including real systems, names, data or screenshots.
- Legal advice stated as fact. Describe the source and its limits instead.

## Style

- British English. Professional, plain tone. No hype.
- No em-dashes or en-dashes (a test enforces this). Use commas, colons or full stops.
- Say what a control does **not** guarantee, as well as what it does.
- Keep decision records honest about trade-offs. A recommendation with no downside is probably incomplete.

## Working locally

You need Python 3.9 or later. Nothing else is required for the tools and tests.

```bash
python -m unittest discover -s tests -v      # run the tests
python tools/check_links.py                  # internal link check
python tools/check_links.py --external       # also check web links (needs network)
python tools/check_diagrams.py               # diagram sources, embeds and PNGs agree
python tools/assess.py assessment/example-filled.csv --target 3
```

### Changing a diagram

Diagram sources are the `.mmd` files in `docs/diagrams/`. The same text is embedded in `docs/architecture.md` as a Mermaid block so that GitHub renders it, and a PNG copy is stored next to the source.

1. Edit the `.mmd` file and update the matching block in `docs/architecture.md` so they are identical.
2. Install the Mermaid CLI: `npm install -g @mermaid-js/mermaid-cli`.
3. Run `tools/render_diagrams.sh` to regenerate the PNGs.
4. Run `python tools/check_diagrams.py` and look at the PNG.

## Pull requests

- Keep each pull request focused.
- Say which sources you used and when you accessed them.
- Make sure the tests and checks above pass.

## Licensing of contributions

By contributing you agree that code contributions are licensed under the MIT licence and documentation contributions under CC BY 4.0, matching the rest of the repository.
