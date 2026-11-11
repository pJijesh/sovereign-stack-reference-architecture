"""Tests for the link and diagram checkers, and for repository hygiene rules."""

import base64
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import check_diagrams  # noqa: E402
import check_links  # noqa: E402


class SlugTests(unittest.TestCase):
    def test_slugify_matches_github_style(self):
        self.assertEqual(check_links.slugify("Where to go next"), "where-to-go-next")
        self.assertEqual(check_links.slugify("1. Identity and access"), "1-identity-and-access")
        self.assertEqual(check_links.slugify("Use `code` here!"), "use-code-here")


class LinkCheckerTests(unittest.TestCase):
    def make_tree(self, files):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def test_good_links_pass(self):
        root = self.make_tree({
            "a.md": "# A\n[b](b.md) [anchor](b.md#second-part) [self](#a)\n",
            "b.md": "# B\n\n## Second part\n",
        })
        self.assertEqual(check_links.check_internal(root), [])

    def test_broken_file_and_anchor_are_reported(self):
        root = self.make_tree({
            "a.md": "[x](missing.md) [y](b.md#nope)\n",
            "b.md": "# B\n",
        })
        errors = check_links.check_internal(root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("missing.md" in e for e in errors))
        self.assertTrue(any("#nope" in e for e in errors))

    def test_links_in_code_are_ignored(self):
        root = self.make_tree({"a.md": "```\n[x](missing.md)\n```\nand `[y](gone.md)`\n"})
        self.assertEqual(check_links.check_internal(root), [])

    def test_repository_internal_links_resolve(self):
        self.assertEqual(check_links.check_internal(ROOT), [])


class DiagramCheckerTests(unittest.TestCase):
    def test_repository_diagrams_are_consistent(self):
        sources, problems = check_diagrams.check(ROOT)
        self.assertGreaterEqual(len(sources), 9)
        self.assertEqual(problems, [])

    def test_detects_mismatched_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs" / "diagrams").mkdir(parents=True)
            (root / "docs" / "diagrams" / "x.mmd").write_text("flowchart LR\n A-->B\n")
            (root / "docs" / "diagrams" / "x.png").write_bytes(check_diagrams.PNG_SIGNATURE + b"data")
            (root / "docs" / "a.md").write_text("```mermaid\nflowchart LR\n A-->C\n```\n")
            _, problems = check_diagrams.check(root)
        text = " | ".join(problems)
        self.assertIn("does not match", text)
        self.assertIn("not embedded", text)

    def test_detects_missing_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs" / "diagrams").mkdir(parents=True)
            (root / "docs" / "diagrams" / "x.mmd").write_text("flowchart LR\n A-->B\n")
            (root / "docs" / "a.md").write_text("```mermaid\nflowchart LR\n A-->B\n```\n")
            _, problems = check_diagrams.check(root)
        self.assertTrue(any("missing or empty PNG" in p for p in problems))


DASHES = "[" + chr(0x2013) + chr(0x2014) + "]"


class HygieneTests(unittest.TestCase):
    """Guard the editorial rules in the brief: no em-dashes, no employer names."""

    # Stored encoded so that this public file does not itself name the terms it guards against.
    _ENCODED_TERMS = [
        "aW50ZXJuYXRpb25hbCBjYXJnbyBsb2dpc3RpY3M=",
        "bWVudGZpZWxk",
        "YXNjb20=",
        "Y2FyZ293aXNl",
        "dHJhbnMgZGF0YSBtYW5hZ2VtZW50",
    ]
    FORBIDDEN_TERMS = [base64.b64decode(t).decode() for t in _ENCODED_TERMS]

    def text_files(self):
        for path in ROOT.rglob("*"):
            if path.is_file() and ".git" not in path.parts and path.suffix in {
                ".md", ".py", ".csv", ".yml", ".yaml", ".mmd", ".sh", ".json", ""
            }:
                yield path

    def test_no_em_or_en_dashes(self):
        offenders = [
            str(p.relative_to(ROOT)) for p in self.text_files()
            if re.search(DASHES, p.read_text(encoding="utf-8", errors="ignore"))
        ]
        self.assertEqual(offenders, [])

    def test_no_employer_or_client_terms(self):
        offenders = []
        for path in self.text_files():
            if path.name == "test_repo_checks.py":
                continue  # this file holds the terms it checks for (encoded)
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            for term in self.FORBIDDEN_TERMS:
                if term in text:
                    offenders.append(f"{path.relative_to(ROOT)}: {term}")
            if re.search(r"\b" + base64.b64decode("aWNs").decode() + r"\b", text):
                offenders.append(f"{path.relative_to(ROOT)}: short-name")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
