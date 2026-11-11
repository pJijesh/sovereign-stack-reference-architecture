#!/usr/bin/env python3
"""Check that Mermaid diagram sources, embedded blocks and PNG renders agree.

Rules:
  1. Every docs/diagrams/*.mmd has a non-empty PNG with the same name.
  2. Every ```mermaid block in the Markdown files matches exactly one .mmd source
     (whitespace-normalised), so the diagram on GitHub equals the rendered PNG.
  3. Every .mmd source is embedded somewhere in the documentation.

This does not render anything; run tools/render_diagrams.sh for that.
Standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
BLOCK_RE = re.compile(r"```mermaid\n(.*?)```", re.S)


def normalise(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def check(root):
    problems = []
    diagrams = root / "docs" / "diagrams"
    sources = {p.stem: normalise(p.read_text(encoding="utf-8"))
               for p in sorted(diagrams.glob("*.mmd"))}
    if not sources:
        problems.append("no .mmd sources found in docs/diagrams")

    for name in sources:
        png = diagrams / f"{name}.png"
        if not png.exists() or png.stat().st_size == 0:
            problems.append(f"{name}: missing or empty PNG")
        elif png.read_bytes()[:8] != PNG_SIGNATURE:
            problems.append(f"{name}: PNG has an invalid signature")

    embedded = set()
    by_text = {text: name for name, text in sources.items()}
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for block in BLOCK_RE.findall(md.read_text(encoding="utf-8")):
            text = normalise(block)
            if text in by_text:
                embedded.add(by_text[text])
            else:
                problems.append(
                    f"{md.relative_to(root)}: mermaid block does not match any docs/diagrams/*.mmd"
                )
    for name in sources:
        if name not in embedded:
            problems.append(f"{name}: source is not embedded in any Markdown file")
    return sources, problems


def main():
    root = Path(__file__).resolve().parent.parent
    sources, problems = check(root)
    print(f"Diagram sources: {len(sources)}; problems: {len(problems)}")
    for problem in problems:
        print("ERROR  " + problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
