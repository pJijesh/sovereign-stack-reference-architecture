#!/usr/bin/env python3
"""Check links in the repository's Markdown files. Standard library only.

Internal checks (always on): relative file links and #anchors must resolve.
External checks (--external): http(s) links are requested. Only definite
failures (404, 410, DNS or connection errors) fail the run. Responses such as
403, 429 and 5xx are reported as warnings, because many sites block automated
requests or are briefly unavailable.

Usage:
    python tools/check_links.py [--external] [--root PATH]
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
USER_AGENT = "Mozilla/5.0 (compatible; repo-link-check/1.0)"


def slugify(heading):
    """GitHub-style heading anchor."""
    text = re.sub(r"`|\*|_", "", heading.strip().lower())
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def strip_code(text):
    """Remove fenced code blocks and inline code so links inside are ignored."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors_in(path, cache):
    if path not in cache:
        found, counts = set(), {}
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = HEADING_RE.match(line)
            if match:
                slug = slugify(match.group(2))
                n = counts.get(slug, 0)
                counts[slug] = n + 1
                found.add(slug if n == 0 else f"{slug}-{n}")
        cache[path] = found
    return cache[path]


def markdown_files(root):
    return sorted(
        p for p in root.rglob("*.md")
        if not (set(p.relative_to(root).parts) & SKIP_DIRS)
    )


def collect_links(path):
    text = strip_code(path.read_text(encoding="utf-8"))
    return LINK_RE.findall(text) + AUTOLINK_RE.findall(text)


def check_internal(root):
    errors, cache = [], {}
    for md in markdown_files(root):
        for target in collect_links(md):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            file_part, _, anchor = target.partition("#")
            dest = md if file_part == "" else (md.parent / file_part).resolve()
            where = md.relative_to(root)
            if not dest.exists():
                errors.append(f"{where}: broken link target {target}")
                continue
            if anchor and dest.suffix == ".md":
                if anchor.lower() not in anchors_in(dest, cache):
                    errors.append(f"{where}: missing anchor #{anchor} in {target}")
    return errors


def fetch_status(url, timeout):
    """Return (status, detail). status is an int HTTP code or None for network errors."""
    last = (None, "no attempt")
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(
            url, method=method, headers={"User-Agent": USER_AGENT}
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, "ok"
        except urllib.error.HTTPError as exc:
            last = (exc.code, exc.reason)
            if method == "HEAD" and exc.code in (403, 404, 405, 429, 501):
                continue  # some servers mishandle HEAD, retry with GET
            return last
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return None, str(getattr(exc, "reason", exc))
    return last


def check_external(root, timeout=20):
    errors, warnings, seen = [], [], {}
    for md in markdown_files(root):
        for target in collect_links(md):
            if not target.startswith(("http://", "https://")):
                continue
            url = target.split("#")[0]
            if url not in seen:
                seen[url] = fetch_status(url, timeout)
            status, detail = seen[url]
            where = md.relative_to(root)
            if status is None or status in (404, 410):
                errors.append(f"{where}: {url} -> {status or 'connection error'} ({detail})")
            elif status >= 400:
                warnings.append(f"{where}: {url} -> {status} ({detail})")
    return errors, warnings, len(seen)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--external", action="store_true", help="also check http(s) links")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    errors = check_internal(root)
    print(f"Internal links checked in {len(markdown_files(root))} Markdown files: "
          f"{len(errors)} problem(s)")
    warnings = []
    if args.external:
        ext_errors, warnings, count = check_external(root, args.timeout)
        errors += ext_errors
        print(f"External URLs checked: {count}; failures: {len(ext_errors)}; "
              f"warnings: {len(warnings)}")
    for line in errors:
        print("ERROR  " + line)
    for line in warnings:
        print("WARN   " + line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
