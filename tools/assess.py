#!/usr/bin/env python3
"""Score a self-assessment CSV and print a text summary with a radar-style chart.

Standard library only. Python 3.10 or later.

Usage:
    python tools/assess.py assessment/self-assessment-template.csv
    python tools/assess.py my-scores.csv --target 3 --json
    python tools/assess.py my-scores.csv --fail-below 2

Input CSV columns: id, layer, question, score, evidence, notes
    id        unique question id, for example IAM-01
    layer     one of IAM, DATA, INT, AI, ORCH, SEC, OBS, GOV
    score     integer 1 to 5, or blank if not yet answered
Other columns are free text and are carried through unchanged.

Exit codes:
    0  success
    1  input could not be read or failed validation
    2  --fail-below was given and at least one scored layer is below it
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

# Layer code -> display name. The order defines the order of the radar spokes.
LAYERS = {
    "IAM": "Identity and access",
    "DATA": "Data and storage",
    "INT": "Integration and APIs",
    "AI": "AI and ML platform",
    "ORCH": "Orchestration and agents",
    "SEC": "Security and key management",
    "OBS": "Observability",
    "GOV": "Governance and compliance",
}

LEVEL_NAMES = {1: "Ad hoc", 2: "Defined", 3: "Managed", 4: "Tested", 5: "Adaptive"}
REQUIRED_COLUMNS = ("id", "layer", "question", "score")
MAX_SCORE = 5
MIN_SCORE = 1


class AssessmentError(Exception):
    """Raised when the input file is unreadable or invalid."""

    def __init__(self, problems):
        self.problems = list(problems)
        super().__init__("; ".join(self.problems))


def load_rows(path):
    """Read the CSV into a list of dicts. Raises AssessmentError if unreadable."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames or []
            missing = [c for c in REQUIRED_COLUMNS if c not in fields]
            if missing:
                raise AssessmentError(
                    ["missing required column(s): " + ", ".join(missing)]
                )
            return [dict(row) for row in reader]
    except OSError as exc:
        raise AssessmentError([f"cannot read {path}: {exc.strerror or exc}"]) from exc
    except csv.Error as exc:
        raise AssessmentError([f"malformed CSV: {exc}"]) from exc


def parse_score(raw):
    """Return an int 1..5, or None for blank. Raises ValueError for anything else."""
    text = (raw or "").strip()
    if text == "":
        return None
    try:
        value = int(text)
    except ValueError:
        raise ValueError(f"score {text!r} is not a whole number") from None
    if not MIN_SCORE <= value <= MAX_SCORE:
        raise ValueError(f"score {value} is outside {MIN_SCORE} to {MAX_SCORE}")
    return value


def validate(rows):
    """Return a list of problems (empty if the rows are valid)."""
    problems = []
    seen = set()
    if not rows:
        problems.append("no data rows found")
    for number, row in enumerate(rows, start=2):  # header is line 1
        qid = (row.get("id") or "").strip()
        layer = (row.get("layer") or "").strip()
        if not qid:
            problems.append(f"line {number}: empty id")
        elif qid in seen:
            problems.append(f"line {number}: duplicate id {qid}")
        seen.add(qid)
        if layer not in LAYERS:
            problems.append(
                f"line {number}: unknown layer {layer!r} (expected one of "
                + ", ".join(LAYERS)
                + ")"
            )
        try:
            parse_score(row.get("score"))
        except ValueError as exc:
            problems.append(f"line {number}: {exc}")
    return problems


def score_rows(rows):
    """Compute per-layer and overall scores. Rows must already be valid.

    Layer score is the mean of answered questions in that layer. Overall score is
    the mean of the layer scores for layers that have at least one answer, so a
    layer with many questions does not outweigh one with few.
    """
    per_layer = {}
    for code in LAYERS:
        scores = [
            parse_score(r.get("score"))
            for r in rows
            if (r.get("layer") or "").strip() == code
        ]
        total = len(scores)
        answered = [s for s in scores if s is not None]
        mean = sum(answered) / len(answered) if answered else None
        per_layer[code] = {
            "name": LAYERS[code],
            "questions": total,
            "answered": len(answered),
            "mean": mean,
            "lowest": min(answered) if answered else None,
        }
    scored = [v["mean"] for v in per_layer.values() if v["mean"] is not None]
    overall = sum(scored) / len(scored) if scored else None
    total_q = sum(v["questions"] for v in per_layer.values())
    total_a = sum(v["answered"] for v in per_layer.values())
    return {
        "layers": per_layer,
        "overall": overall,
        "answered": total_a,
        "questions": total_q,
    }


def level_name(mean):
    """Name of the nearest maturity level (half rounds up)."""
    if mean is None:
        return "Not scored"
    level = min(MAX_SCORE, max(MIN_SCORE, int(math.floor(mean + 0.5))))
    return f"{level} {LEVEL_NAMES[level]}"


def bar(mean, width=25):
    """Horizontal bar scaled 0..5, for example '#########----'."""
    if mean is None:
        return "." * width
    filled = int(round(mean / MAX_SCORE * width))
    return "#" * filled + "-" * (width - filled)


def _line_points(x0, y0, x1, y1):
    """Bresenham line between two grid points, inclusive."""
    points = []
    dx, dy = abs(x1 - x0), -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    return points


def render_radar(layer_means, radius=10):
    """Return a list of text lines drawing a polar (radar) plot.

    One spoke per layer, starting at the top and going clockwise. The outer ring
    is a score of 5. Unscored layers sit at the centre. Spoke ends carry the
    layer number 1..8, matching the legend printed below the chart.
    """
    codes = list(LAYERS)
    n = len(codes)
    height = 2 * (radius + 1) + 1
    width = 4 * (radius + 1) + 1  # characters are about twice as tall as wide
    cx, cy = width // 2, height // 2
    grid = [[" "] * width for _ in range(height)]

    def to_xy(angle, r):
        x = cx + int(round(2 * r * math.cos(angle)))
        y = cy - int(round(r * math.sin(angle)))
        return x, y

    angles = [math.pi / 2 - 2 * math.pi * i / n for i in range(n)]

    # Spokes and ring ticks
    for angle in angles:
        for step in range(1, radius + 1):
            x, y = to_xy(angle, step)
            if grid[y][x] == " ":
                grid[y][x] = "."
    for ring in range(1, MAX_SCORE + 1):
        r = ring / MAX_SCORE * radius
        for angle in angles:
            x, y = to_xy(angle, r)
            grid[y][x] = "+" if ring < MAX_SCORE else "o"

    # Score polygon
    vertices = []
    for angle, code in zip(angles, codes):
        mean = layer_means.get(code)
        r = 0.0 if mean is None else mean / MAX_SCORE * radius
        vertices.append(to_xy(angle, r))
    for i in range(n):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % n]
        for x, y in _line_points(x0, y0, x1, y1):
            if grid[y][x] in (" ", ".", "+"):
                grid[y][x] = "*"
    for x, y in vertices:
        grid[y][x] = "@"

    # Spoke labels just outside the outer ring
    for index, angle in enumerate(angles, start=1):
        x, y = to_xy(angle, radius + 1)
        grid[y][x] = str(index)

    grid[cy][cx] = grid[cy][cx] if grid[cy][cx] in ("@", "*") else "x"
    return ["".join(row).rstrip() for row in grid]


def build_report(result, target=None, radar_radius=10):
    """Return the full text report as a string."""
    lines = []
    layers = result["layers"]
    lines.append("SOVEREIGN STACK SELF-ASSESSMENT")
    lines.append("=" * 31)
    lines.append(
        f"Questions answered: {result['answered']} of {result['questions']}"
    )
    if result["overall"] is None:
        lines.append("No scored questions yet. Fill in the score column (1 to 5).")
        return "\n".join(lines)

    lines.append(
        f"Overall (mean of layer scores): {result['overall']:.2f} "
        f"({level_name(result['overall'])})"
    )
    lines.append("")
    lines.append("Layer scores (0 to 5 scale, 25 characters = 5.0)")
    lines.append("-" * 72)
    for index, (code, info) in enumerate(layers.items(), start=1):
        mean = info["mean"]
        value = "  n/a" if mean is None else f"{mean:5.2f}"
        lines.append(
            f"{index}  {info['name']:<28} {value}  {bar(mean)}  "
            f"{info['answered']}/{info['questions']}"
        )
    lines.append("")
    lines.append("Radar (outer ring o = 5, rings + = 1 to 4, @ = layer score)")
    lines.extend(render_radar({c: v["mean"] for c, v in layers.items()}, radar_radius))
    lines.append("")
    for index, info in enumerate(layers.values(), start=1):
        lines.append(f"  {index} = {info['name']}")

    scored = [(c, v) for c, v in layers.items() if v["mean"] is not None]
    weakest = sorted(scored, key=lambda item: (item[1]["mean"], item[0]))[:3]
    lines.append("")
    lines.append("Weakest layers (focus first):")
    for code, info in weakest:
        lines.append(f"  - {info['name']}: {info['mean']:.2f} ({level_name(info['mean'])})")

    unanswered = [v["name"] for v in layers.values() if v["answered"] == 0]
    if unanswered:
        lines.append("")
        lines.append("Not yet scored: " + ", ".join(unanswered))

    if target is not None:
        gaps = [(c, v) for c, v in scored if v["mean"] < target]
        lines.append("")
        lines.append(f"Gap to target level {target:g}:")
        if not gaps:
            lines.append("  All scored layers meet the target.")
        for code, info in sorted(gaps, key=lambda item: item[1]["mean"]):
            lines.append(
                f"  - {info['name']}: {info['mean']:.2f}, short by {target - info['mean']:.2f}"
            )

    lines.append("")
    lines.append(
        "Self-assessment only: scores show your own judgement, not independent assurance."
    )
    return "\n".join(lines)


def to_json(result, target=None):
    payload = {
        "overall": result["overall"],
        "answered": result["answered"],
        "questions": result["questions"],
        "layers": result["layers"],
    }
    if target is not None:
        payload["target"] = target
    return json.dumps(payload, indent=2)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Score a Sovereign Stack self-assessment CSV."
    )
    parser.add_argument("csv_path", help="path to the filled-in assessment CSV")
    parser.add_argument(
        "--target", type=float, default=None,
        help="optional target level (1 to 5); layers below it are listed as gaps",
    )
    parser.add_argument(
        "--fail-below", type=float, default=None, metavar="LEVEL",
        help="exit with status 2 if any scored layer is below LEVEL",
    )
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    for name in ("target", "fail_below"):
        value = getattr(args, name)
        if value is not None and not MIN_SCORE <= value <= MAX_SCORE:
            print(f"error: --{name.replace('_', '-')} must be 1 to 5", file=sys.stderr)
            return 1
    try:
        rows = load_rows(Path(args.csv_path))
        problems = validate(rows)
        if problems:
            raise AssessmentError(problems)
    except AssessmentError as exc:
        print("Input problems:", file=sys.stderr)
        for problem in exc.problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    result = score_rows(rows)
    if args.json:
        print(to_json(result, args.target))
    else:
        print(build_report(result, args.target))

    if args.fail_below is not None:
        below = [
            v for v in result["layers"].values()
            if v["mean"] is not None and v["mean"] < args.fail_below
        ]
        if below:
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
