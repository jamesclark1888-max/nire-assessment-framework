# NIRE Assessment Framework

The single source of truth for NIRE's founder investment readiness assessment. This repository contains YAML question banks, scoring rubrics, recommendation templates, JSON schemas, and tooling. It is a data and specification repository, not a code application.

Owner: NIRE HQ LIMITED

---

## Before making any changes

Before editing any file, Claude Code MUST:

1. **Read the relevant schema** in `schema/` for the file type being changed (question, scoring-rule, recommendation, benchmark, archetype). Understand every required field and enum before writing YAML.

2. **Read the canonical Dimension 1 files** as the reference pattern before drafting any new dimension:
   - `framework/dimensions/01-founder-team/questions.yaml`
   - `framework/dimensions/01-founder-team/scoring.yaml`
   - `framework/dimensions/01-founder-team/recommendations.yaml`
   - `framework/dimensions/01-founder-team/benchmarks/global.yaml`

3. **Check existing question IDs** in the target `questions.yaml` to avoid collisions. IDs must be unique across the entire file. The pattern is `q{dimension-number}.{sequence}` for universal questions (e.g. `q2.3`) and `q{dimension-number}.{region-code}{sequence}` for regional ones (e.g. `q1.uk2`).

4. **Verify rubric-ref and benchmark-ref alignment** between `questions.yaml` and `scoring.yaml` before writing either. Every non-null `rubric-ref` or `benchmark-ref` in questions must match a rule `id` in scoring.

5. **Read `docs/01-philosophy.md` and `docs/02-scoring-methodology.md`** before drafting a new dimension or adding questions. Every question must earn its place by the standard in those documents.

---

## Spec-first discipline

These invariants must hold after every commit. They are checked manually; the validator does not cross-reference file pairs.

- **No scored question without a scoring rule.** Every question with `scoring.type` other than `informational-only` must have a corresponding rule in `scoring.yaml` whose `id` matches the question's `rubric-ref` or `benchmark-ref`.

- **No non-null recommendation trigger without a template.** Every `recommendation-trigger.low-score` or `recommendation-trigger.medium-score` value that is not `null` must have a matching template `id` in `recommendations.yaml`.

- **No scoring rule without a linked question.** Every rule in `scoring.yaml` must reference a question that exists in `questions.yaml` via `applies-to-question`.

Informational-only questions (weight 0.00, `scoring.type: informational-only`) are exempt from the recommendation trigger requirement.

---

## Definition of done

A change to the framework is NOT complete until all of the following are true:

1. `python3 tooling/validate.py` runs from the repo root and reports **0 errors**.
2. `CHANGELOG.md` has an entry under `[Unreleased]` that describes what changed and why.
3. If a dimension's status changed (e.g. skeleton to drafted), the root `README.md` dimension status table reflects the new status.
4. The commit message clearly describes what changed (not just file names).

---

## Pre-commit rule

**Before every commit, Claude Code MUST run the validator and show the output:**

```bash
python3 tooling/validate.py
```

The only acceptable result is:

```
✅ Validation passed.
```

with 0 errors. Warnings for skeleton dimensions (no `questions.yaml` yet) are expected and acceptable. Any error must be fixed before committing. Do not commit with a failing validator under any circumstances.

If the validator cannot run (missing dependencies), install them first:

```bash
pip3 install pyyaml jsonschema
```

---

## YAML conventions

### Question IDs

| Pattern | Used for |
|---------|----------|
| `q{N}.{n}` | Universal questions (e.g. `q2.3`) |
| `q{N}.{code}{n}` | Regional questions (e.g. `q1.uk2`, `q1.de1`) |

Region codes: `uk`, `fr`, `de`, `nl`, `nordic`, `eu`.

### Weights

Weights within a dimension should sum to approximately 1.0 across all questions. The validator warns when the total falls outside 0.5-1.5. Informational-only questions contribute 0.00 or a small nominal weight (0.02 max). Optional questions carry low weight (0.05 max as a rule of thumb).

### Multi-line strings

Use the YAML block scalar `|` for all multi-line strings (`why-it-matters`, `description`, `diagnostic`, `fix`, etc.). Do not use inline double-quoted strings for multi-line content.

### `why-it-matters`

This field is internal-facing only; it is never shown to founders. It has a 500-character maximum enforced by the schema. Write it from the VC's perspective: what underwriting signal does this question provide?

### Required fields

Every question must have all eight schema-required fields: `id`, `dimension`, `tier`, `type`, `question`, `why-it-matters`, `applies-to`, `scoring`. The validator will report missing fields as errors.

---

## Git hygiene

### Branch discipline

- Always work on `main` unless explicitly asked to create a feature branch.
- Never create or check out a branch without saying so first and getting confirmation.
- Before any commit, verify with `git branch` that we are on `main`. If not, stop and ask before proceeding.

This matches the branch hygiene rule in the Portfolio Tracker. It exists because a parallel-session incident created a `nire-knowledge-base` worktree branch that diverged from main and caused unnecessary cleanup work.

### File moves and deletes

- When moving a file, use `git mv` or follow `mv` immediately with `git rm` on the old path.
- Run `git status` after any file move and confirm no file is listed as both deleted and untracked.
- Never leave a file tracked by git at an old path. Orphaned tracked files are checked out by consumers of the repo and cause confusion.

---

## Common tasks

### Drafting a new dimension

Follow these steps in order. Do not skip steps.

1. Read the dimension's skeleton README at `framework/dimensions/NN-name/README.md` to understand scope.
2. Read the Dimension 1 files (listed above) as the canonical pattern.
3. Read `docs/01-philosophy.md` and `docs/02-scoring-methodology.md`.
4. Read all five schemas in `schema/`.
5. Draft `questions.yaml`:
   - 5 required questions, 4-6 recommended, 3-4 optional.
   - Weights should sum to approximately 1.0 total.
   - Assign `version-added: "0.1.0"` to all questions.
   - Regional questions use the `q{N}.{code}{n}` ID pattern and `applies-to.regions: [code]`.
6. Draft `scoring.yaml`:
   - One rule per scored question.
   - Rule `id` must match the `rubric-ref` or `benchmark-ref` in `questions.yaml` exactly.
   - Use `type: rubric` for qualitative (AI-evaluated) questions; `type: threshold` for quantitative; `type: mapping` for single-select categorical.
7. Draft `recommendations.yaml`:
   - One template per non-null `low-score` or `medium-score` trigger.
   - Every template requires `id`, `trigger`, `priority`, `diagnostic`, and `fix`. Add `gap` and `evidence` wherever the content warrants it.
   - Add `stage-variants` for high-priority templates where the advice differs materially between pre-seed and Series A.
8. Create `benchmarks/global.yaml` if the dimension has any quantitative signals. The benchmark schema requires `region`, `last-reviewed`, `expires`, and `benchmarks`.
9. Update the dimension's README from skeleton to drafted. Mirror the structure of `framework/dimensions/01-founder-team/README.md`.
10. Run `python3 tooling/validate.py` from the repo root. Fix all errors before continuing.
11. Update `CHANGELOG.md` under `[Unreleased]`.
12. Update the dimension status table in the root `README.md`.
13. Commit.

### Adding a question to an existing dimension

1. Decide the tier (required / recommended / optional) and where in the narrative it sits.
2. Assign the next available ID in sequence. Check the highest existing ID in `questions.yaml`.
3. Add the question to `questions.yaml` with all required fields.
4. Add a scoring rule to `scoring.yaml` whose `id` matches the `rubric-ref` or `benchmark-ref`.
5. If `recommendation-trigger.low-score` or `medium-score` is non-null, add the template to `recommendations.yaml`.
6. Check the weight sum: add all question weights and confirm the total remains in the 0.5-1.5 range. Adjust neighbouring weights if needed.
7. Run `python3 tooling/validate.py`. Fix all errors.
8. Update `CHANGELOG.md` under `[Unreleased]`.

### Adding a regional layer

1. Create `framework/regional/{code}.yaml`. Use `framework/regional/_generic-eu.yaml` as a template for structure.
2. Add a routing entry to `framework/routing/regional-routing.yaml`.
3. For each dimension that warrants regional questions:
   - Add questions to the dimension's `questions.yaml` using the `q{N}.{code}{n}` ID pattern.
   - Set `applies-to.regions: [{code}]` and the appropriate `applies-to.stages`.
   - Add a scoring rule to `scoring.yaml` for each regional question.
   - Add recommendation templates for each non-null trigger.
4. If the region has materially different quantitative benchmarks, add `benchmarks/{code}.yaml` to the relevant dimension directories. The benchmark file must pass the benchmark schema.
5. Run `python3 tooling/validate.py`. Fix all errors.
6. Update `CHANGELOG.md` under `[Unreleased]`.

---

## Critical operational rules

None recorded yet. When an incident occurs that requires a standing rule, document it here in the same format as the Portfolio Tracker: what must never happen, what the symptom looks like, and how to fix it.

---

## Repository structure

```
nire-assessment-framework/
├── docs/              # Strategic thinking, methodology, decisions
├── framework/         # The assessment itself
│   ├── dimensions/    # One directory per dimension (01 through 08)
│   ├── archetypes/    # VC archetype scoring lenses
│   ├── routing/       # Stage, business-model, and regional routing logic
│   └── regional/      # Region-level configuration files
├── schema/            # JSON Schema validation for all framework files
├── tooling/           # Validation and analysis scripts
└── examples/          # Worked founder journey examples
```

See `docs/00-overview.md` for a full guided tour.
