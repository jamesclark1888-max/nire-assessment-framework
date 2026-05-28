# Tooling

Scripts for validating and analysing the NIRE Assessment Framework.

---

## Scripts

### `validate.py`

Validates all YAML files against their corresponding JSON Schemas, plus runs cross-file consistency checks.

```bash
python tooling/validate.py
```

Output: validation report to stdout, plus optional `validation-report.json` for CI consumption.

Checks performed:

- Every `questions.yaml` validates against `schema/question.schema.json`
- Every `scoring.yaml` validates against `schema/scoring-rule.schema.json`
- Every `benchmark.yaml` validates against `schema/benchmark.schema.json`
- Every `archetype.yaml` validates against `schema/archetype.schema.json`
- Every `recommendations.yaml` validates against `schema/recommendation.schema.json`
- Question weights within each dimension sum to 1.0 (±0.01 tolerance)
- Archetype dimension weights sum to 1.0 (±0.01)
- Stage dimension weights in `stage-routing.yaml` sum to 1.0 per stage (±0.01)
- Every `rubric-ref` and `benchmark-ref` in questions resolves to a defined rule
- Every `recommendation-trigger` ID resolves to a defined recommendation
- Question IDs are unique across the framework
- Benchmark `expires` dates are in the future

### `question-count.py`

Reports how many questions a founder would see for various profiles. Useful for keeping the assessment to a reasonable length.

```bash
python tooling/question-count.py --stage seed --business-model saas --region uk
```

Output: count of required, recommended, and optional questions for that profile, plus estimated completion time.

---

## Dependencies

Both scripts use:

- `pyyaml` for YAML parsing
- `jsonschema` for schema validation

Install:

```bash
pip install pyyaml jsonschema
```

---

## CI integration

GitHub Actions runs `validate.py` on every pull request. The workflow is defined in `.github/workflows/validate.yml`. PRs cannot be merged unless validation passes.
