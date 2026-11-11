"""Tests for tools/assess.py. Run with:  python -m unittest discover -s tests -v"""

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import assess  # noqa: E402

TEMPLATE = ROOT / "assessment" / "self-assessment-template.csv"
EXAMPLE = ROOT / "assessment" / "example-filled.csv"
SCRIPT = ROOT / "tools" / "assess.py"


def write_csv(directory, rows, columns=("id", "layer", "question", "score")):
    path = Path(directory) / "input.csv"
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)
    return path


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, args)],
        capture_output=True, text=True, cwd=ROOT,
    )


class ParseScoreTests(unittest.TestCase):
    def test_blank_is_none(self):
        self.assertIsNone(assess.parse_score(""))
        self.assertIsNone(assess.parse_score("   "))
        self.assertIsNone(assess.parse_score(None))

    def test_valid_range(self):
        for value in range(1, 6):
            self.assertEqual(assess.parse_score(str(value)), value)

    def test_rejects_out_of_range_and_text(self):
        for bad in ("0", "6", "-1", "3.5", "high"):
            with self.assertRaises(ValueError, msg=bad):
                assess.parse_score(bad)


class ValidateTests(unittest.TestCase):
    def test_valid_rows_have_no_problems(self):
        rows = [{"id": "IAM-01", "layer": "IAM", "question": "q", "score": "3"}]
        self.assertEqual(assess.validate(rows), [])

    def test_reports_each_kind_of_problem(self):
        rows = [
            {"id": "A", "layer": "IAM", "question": "q", "score": "9"},
            {"id": "A", "layer": "NOPE", "question": "q", "score": "2"},
            {"id": "", "layer": "DATA", "question": "q", "score": "x"},
        ]
        text = " | ".join(assess.validate(rows))
        self.assertIn("outside 1 to 5", text)
        self.assertIn("duplicate id A", text)
        self.assertIn("unknown layer", text)
        self.assertIn("empty id", text)
        self.assertIn("not a whole number", text)

    def test_empty_file_is_a_problem(self):
        self.assertIn("no data rows found", assess.validate([]))

    def test_missing_column_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_csv(tmp, [["IAM-01", "IAM", "q"]], columns=("id", "layer", "question"))
            with self.assertRaises(assess.AssessmentError) as ctx:
                assess.load_rows(path)
            self.assertIn("score", str(ctx.exception))

    def test_missing_file_is_reported(self):
        with self.assertRaises(assess.AssessmentError):
            assess.load_rows(ROOT / "does-not-exist.csv")


class ScoreTests(unittest.TestCase):
    def rows(self, spec):
        return [
            {"id": f"{layer}-{i}", "layer": layer, "question": "q", "score": score}
            for i, (layer, score) in enumerate(spec)
        ]

    def test_layer_mean_ignores_blanks(self):
        result = assess.score_rows(self.rows([("IAM", "2"), ("IAM", "4"), ("IAM", "")]))
        layer = result["layers"]["IAM"]
        self.assertEqual(layer["questions"], 3)
        self.assertEqual(layer["answered"], 2)
        self.assertAlmostEqual(layer["mean"], 3.0)
        self.assertEqual(layer["lowest"], 2)

    def test_overall_is_mean_of_layer_means_not_of_questions(self):
        # IAM has three questions at 5; DATA has one at 1. Mean of questions would be 4.
        spec = [("IAM", "5")] * 3 + [("DATA", "1")]
        result = assess.score_rows(self.rows(spec))
        self.assertAlmostEqual(result["overall"], 3.0)

    def test_unscored_layers_do_not_affect_overall(self):
        result = assess.score_rows(self.rows([("IAM", "4"), ("DATA", "")]))
        self.assertAlmostEqual(result["overall"], 4.0)
        self.assertIsNone(result["layers"]["DATA"]["mean"])

    def test_nothing_scored(self):
        result = assess.score_rows(self.rows([("IAM", ""), ("GOV", "")]))
        self.assertIsNone(result["overall"])
        self.assertIn("No scored questions", assess.build_report(result))

    def test_level_names_round_half_up(self):
        self.assertEqual(assess.level_name(None), "Not scored")
        self.assertEqual(assess.level_name(1.0), "1 Ad hoc")
        self.assertEqual(assess.level_name(2.5), "3 Managed")
        self.assertEqual(assess.level_name(2.49), "2 Defined")
        self.assertEqual(assess.level_name(5.0), "5 Adaptive")


class RadarTests(unittest.TestCase):
    def means(self, value):
        return {code: value for code in assess.LAYERS}

    def test_every_layer_has_a_numbered_label(self):
        text = "\n".join(assess.render_radar(self.means(3.0)))
        for number in range(1, len(assess.LAYERS) + 1):
            self.assertIn(str(number), text)

    def test_full_scores_reach_the_outer_ring(self):
        radius = 10
        lines = assess.render_radar(self.means(5.0), radius)
        cy = (2 * (radius + 1) + 1) // 2
        top_row = lines[cy - radius]   # spoke 1 points straight up
        self.assertIn("@", top_row)

    def test_low_scores_stay_near_the_centre(self):
        radius = 10
        lines = assess.render_radar(self.means(1.0), radius)
        cy = (2 * (radius + 1) + 1) // 2
        # With a score of 1 the vertices are two cells from the centre, so no '@'
        # can appear in the top or bottom three rows of the plot area.
        outer = lines[: cy - 3] + lines[cy + 4:]
        self.assertFalse(any("@" in row for row in outer))

    def test_output_is_deterministic(self):
        self.assertEqual(assess.render_radar(self.means(3.0)), assess.render_radar(self.means(3.0)))

    def test_unscored_layer_collapses_to_centre(self):
        means = self.means(5.0)
        means["IAM"] = None
        lines = assess.render_radar(means, 10)
        self.assertNotIn("@", lines[1])  # top spoke vertex moved to the centre


class ReportTests(unittest.TestCase):
    def test_report_lists_weakest_layers_and_gaps(self):
        rows = assess.load_rows(EXAMPLE)
        result = assess.score_rows(rows)
        report = assess.build_report(result, target=3)
        self.assertIn("Weakest layers", report)
        self.assertIn("Gap to target level 3", report)
        self.assertIn("AI and ML platform", report)
        self.assertIn("Self-assessment only", report)

    def test_json_round_trips(self):
        result = assess.score_rows(assess.load_rows(EXAMPLE))
        data = json.loads(assess.to_json(result, 3))
        self.assertEqual(data["questions"], 24)
        self.assertEqual(data["target"], 3)
        self.assertEqual(set(data["layers"]), set(assess.LAYERS))


class ShippedFilesTests(unittest.TestCase):
    def test_template_is_valid_and_blank(self):
        rows = assess.load_rows(TEMPLATE)
        self.assertEqual(assess.validate(rows), [])
        self.assertEqual(len(rows), 24)
        self.assertTrue(all((r["score"] or "").strip() == "" for r in rows))

    def test_every_layer_has_three_questions_in_both_files(self):
        for path in (TEMPLATE, EXAMPLE):
            rows = assess.load_rows(path)
            for code in assess.LAYERS:
                count = sum(1 for r in rows if r["layer"] == code)
                self.assertEqual(count, 3, f"{path.name}: {code}")

    def test_example_is_fully_scored(self):
        rows = assess.load_rows(EXAMPLE)
        self.assertEqual(assess.validate(rows), [])
        result = assess.score_rows(rows)
        self.assertEqual(result["answered"], 24)
        self.assertAlmostEqual(result["overall"], 2.0417, places=3)

    def test_template_and_example_have_same_questions(self):
        a = [(r["id"], r["layer"], r["question"]) for r in assess.load_rows(TEMPLATE)]
        b = [(r["id"], r["layer"], r["question"]) for r in assess.load_rows(EXAMPLE)]
        self.assertEqual(a, b)


class CommandLineTests(unittest.TestCase):
    def test_example_runs_and_prints_radar(self):
        proc = run_cli(EXAMPLE, "--target", "3")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Overall (mean of layer scores): 2.04", proc.stdout)
        self.assertIn("Radar", proc.stdout)

    def test_blank_template_is_not_an_error(self):
        proc = run_cli(TEMPLATE)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("0 of 24", proc.stdout)

    def test_json_flag_outputs_json(self):
        proc = run_cli(EXAMPLE, "--json")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)["answered"], 24)

    def test_invalid_input_exits_1_with_messages(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_csv(tmp, [["IAM-01", "IAM", "q", "7"]])
            proc = run_cli(path)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("outside 1 to 5", proc.stderr)

    def test_missing_file_exits_1(self):
        proc = run_cli(ROOT / "nope.csv")
        self.assertEqual(proc.returncode, 1)

    def test_fail_below_exit_code(self):
        self.assertEqual(run_cli(EXAMPLE, "--fail-below", "2.5").returncode, 2)
        self.assertEqual(run_cli(EXAMPLE, "--fail-below", "1").returncode, 0)

    def test_bad_target_is_rejected(self):
        self.assertEqual(run_cli(EXAMPLE, "--target", "9").returncode, 1)


if __name__ == "__main__":
    unittest.main()
