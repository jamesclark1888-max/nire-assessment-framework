#!/usr/bin/env python3
"""
NIRE Assessment Framework — question count utility

Reports how many questions a founder with a given profile would see.
Useful for keeping assessment length sane.

Usage:
    python tooling/question-count.py --stage seed --business-model saas --region uk
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Missing dependencies. Install with: pip install pyyaml")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = ROOT / "framework"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def question_applies(
    question: dict[str, Any],
    stage: str,
    business_model: str,
    region: str,
) -> bool:
    applies_to = question.get("applies-to", {})

    stages = applies_to.get("stages", "all")
    if stages != "all" and stage not in stages:
        return False

    models = applies_to.get("business-models", "all")
    if models != "all" and business_model not in models:
        return False

    regions = applies_to.get("regions", "all")
    if regions != "all" and region not in regions:
        return False

    return True


def count_questions(stage: str, business_model: str, region: str) -> dict[str, Any]:
    counts = {
        "required": 0,
        "recommended": 0,
        "optional": 0,
        "total": 0,
        "by-dimension": {},
    }

    dimensions_dir = FRAMEWORK_DIR / "dimensions"
    for dim_dir in sorted(dimensions_dir.iterdir()):
        if not dim_dir.is_dir():
            continue
        questions_file = dim_dir / "questions.yaml"
        if not questions_file.exists():
            continue
        data = load_yaml(questions_file)
        if not data or "questions" not in data:
            continue
        dim_counts = {"required": 0, "recommended": 0, "optional": 0}
        for q in data["questions"]:
            if not question_applies(q, stage, business_model, region):
                continue
            tier = q.get("tier", "optional")
            if tier in dim_counts:
                dim_counts[tier] += 1
                counts[tier] += 1
                counts["total"] += 1
        counts["by-dimension"][dim_dir.name] = dim_counts

    return counts


def estimate_time(counts: dict[str, int]) -> tuple[int, int]:
    # Rough heuristic: required ~45s avg, recommended ~60s, optional ~75s
    min_sec = counts["required"] * 45 + counts["recommended"] * 60 + counts["optional"] * 75
    max_sec = counts["required"] * 90 + counts["recommended"] * 120 + counts["optional"] * 180
    return min_sec // 60, max_sec // 60


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", default="seed", choices=["pre-seed", "seed", "series-a", "series-b"])
    parser.add_argument("--business-model", default="saas")
    parser.add_argument("--region", default="uk")
    parser.add_argument("--tier", choices=["required", "recommended", "optional", "all"], default="all")
    args = parser.parse_args()

    counts = count_questions(args.stage, args.business_model, args.region)

    print(f"\nProfile: stage={args.stage}, model={args.business_model}, region={args.region}")
    print("=" * 60)
    print(f"Required:    {counts['required']:>3}")
    print(f"Recommended: {counts['recommended']:>3}")
    print(f"Optional:    {counts['optional']:>3}")
    print(f"Total:       {counts['total']:>3}")
    min_min, max_min = estimate_time(counts)
    print(f"\nEstimated time to complete all: {min_min}-{max_min} minutes")
    print(f"Required tier only: ~{counts['required'] * 45 // 60}-{counts['required'] * 90 // 60} minutes")

    print("\nPer dimension:")
    for dim, dc in counts["by-dimension"].items():
        total = dc["required"] + dc["recommended"] + dc["optional"]
        print(f"  {dim}: {total} total ({dc['required']}/{dc['recommended']}/{dc['optional']})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
