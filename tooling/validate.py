#!/usr/bin/env python3
"""
NIRE Assessment Framework — validator

Validates all YAML files against their JSON Schemas and runs cross-file
consistency checks. Exit code 0 on success, 1 on any failure.

Usage:
    python tooling/validate.py
    python tooling/validate.py --json  # outputs JSON report as well
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("Missing dependencies. Install with: pip install pyyaml jsonschema")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
FRAMEWORK_DIR = ROOT / "framework"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks_run: int = 0

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def ok(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok(),
            "checks-run": self.checks_run,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text(encoding="utf-8"))


def validate_against_schema(
    data: Any, schema: dict[str, Any], context: str, report: Report
) -> None:
    report.checks_run += 1
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    for err in errors:
        path_str = ".".join(str(p) for p in err.path) or "<root>"
        report.error(f"[{context}] schema error at {path_str}: {err.message}")


def validate_question_file(path: Path, schema: dict[str, Any], report: Report) -> None:
    data = load_yaml(path)
    if not data or "questions" not in data:
        report.error(f"[{path}] missing 'questions' key")
        return
    for q in data["questions"]:
        validate_against_schema(q, schema, f"{path}::{q.get('id', '<no-id>')}", report)


def validate_dimension_files(report: Report) -> None:
    question_schema = load_schema("question")
    scoring_schema = load_schema("scoring-rule")
    benchmark_schema = load_schema("benchmark")
    recommendation_schema = load_schema("recommendation")

    dimensions_dir = FRAMEWORK_DIR / "dimensions"
    if not dimensions_dir.exists():
        report.error("framework/dimensions/ does not exist")
        return

    for dim_dir in sorted(dimensions_dir.iterdir()):
        if not dim_dir.is_dir():
            continue

        questions_file = dim_dir / "questions.yaml"
        if questions_file.exists():
            validate_question_file(questions_file, question_schema, report)
            check_question_weights_sum_to_one(questions_file, report)
        else:
            report.warn(f"[{dim_dir.name}] no questions.yaml yet (skeleton)")

        scoring_file = dim_dir / "scoring.yaml"
        if scoring_file.exists():
            data = load_yaml(scoring_file)
            validate_against_schema(data, scoring_schema, str(scoring_file), report)

        rec_file = dim_dir / "recommendations.yaml"
        if rec_file.exists():
            data = load_yaml(rec_file)
            validate_against_schema(
                data, recommendation_schema, str(rec_file), report
            )

        benchmarks_dir = dim_dir / "benchmarks"
        if benchmarks_dir.exists():
            for bench_file in sorted(benchmarks_dir.glob("*.yaml")):
                data = load_yaml(bench_file)
                validate_against_schema(
                    data, benchmark_schema, str(bench_file), report
                )


def validate_archetype_files(report: Report) -> None:
    schema = load_schema("archetype")
    archetypes_dir = FRAMEWORK_DIR / "archetypes"
    if not archetypes_dir.exists():
        report.warn("framework/archetypes/ does not exist (skeleton)")
        return
    for f in sorted(archetypes_dir.glob("*.yaml")):
        data = load_yaml(f)
        validate_against_schema(data, schema, str(f), report)
        check_archetype_dimension_weights(f, data, report)


def check_question_weights_sum_to_one(path: Path, report: Report) -> None:
    data = load_yaml(path)
    if not data or "questions" not in data:
        return
    total = sum(q.get("scoring", {}).get("weight", 0) for q in data["questions"])
    # Note: weights are within a dimension; informational-only questions
    # have weight 0. Some leeway because of regional/optional questions.
    # Strict check would require excluding regional and optional from the
    # required-tier weight check. Soft warning only for now.
    if total < 0.5 or total > 1.5:
        report.warn(
            f"[{path}] question weights sum to {total:.2f} (expected ~1.0 across the dimension)"
        )


def check_archetype_dimension_weights(
    path: Path, data: dict[str, Any], report: Report
) -> None:
    weights = data.get("dimension-weights", {})
    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        report.error(
            f"[{path}] dimension-weights sum to {total:.3f}, must equal 1.0"
        )


def validate_routing_files(report: Report) -> None:
    routing_dir = FRAMEWORK_DIR / "routing"
    if not routing_dir.exists():
        report.warn("framework/routing/ does not exist")
        return
    stage_file = routing_dir / "stage-routing.yaml"
    if stage_file.exists():
        data = load_yaml(stage_file)
        dim_weights = data.get("dimension-weights", {})
        for stage, weights in dim_weights.items():
            total = sum(weights.values())
            if abs(total - 1.0) > 0.01:
                report.error(
                    f"[stage-routing.yaml::{stage}] dimension weights sum to "
                    f"{total:.3f}, must equal 1.0"
                )
            report.checks_run += 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate NIRE framework")
    parser.add_argument("--json", action="store_true", help="Output JSON report to file")
    args = parser.parse_args()

    report = Report()

    print("Running NIRE Framework validation...\n")
    validate_dimension_files(report)
    validate_archetype_files(report)
    validate_routing_files(report)

    print(f"Checks run: {report.checks_run}")
    print(f"Errors:     {len(report.errors)}")
    print(f"Warnings:   {len(report.warnings)}")

    if report.warnings:
        print("\nWarnings:")
        for w in report.warnings:
            print(f"  - {w}")

    if report.errors:
        print("\nErrors:")
        for e in report.errors:
            print(f"  - {e}")

    if args.json:
        out_path = ROOT / "validation-report.json"
        out_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
        print(f"\nWrote {out_path}")

    if report.ok():
        print("\n✅ Validation passed.")
        return 0
    print("\n❌ Validation failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
