# Changelog

All notable changes to the NIRE Assessment Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Future work / Open questions

- **Conditional question visibility based on prior answers.** For example, q1.3
  (co-founder working relationship) should be hidden when q1.1 = "1 (solo founder)"
  because the question is not applicable. The current `applies-to` schema only supports
  static filtering by stage, business-model, and region — it has no mechanism for
  answer-dependent visibility. Implementing this requires either: (a) a new
  `show-if` / `hide-if` field in the question schema referencing another question ID
  and a set of trigger values, or (b) keeping the logic in the rendering layer as a
  hardcoded mapping. Either approach needs schema design and validator support before
  it can be built. Deferring to a future framework schema revision.

### Added (continued)
- Dimension 5 (Business Model & Unit Economics) fully drafted: 11 questions across 3 tiers (5 required, 4 recommended, 2 optional), 10 scoring rules (3 threshold-based for gross margin, LTV:CAC, and CAC payback; 7 rubric-based for qualitative signals), 10 recommendation templates, and global benchmarks for gross margin, LTV:CAC, and CAC payback across pre-seed, seed, and Series A. LTV:CAC (q5.6) and CAC payback (q5.7) use stage-thresholds; gross margin (q5.3) uses flat thresholds (model-dependent, not stage-dependent). showIf conditions gate q5.6 and q5.7 on `q4.1 in [live, scaling]` so pre-revenue founders are not assessed on metrics they cannot provide. D5 README updated from skeleton to full specification.

### Changed
- D4 quantitative scoring rules (q4.2 customer count, q4.3 MRR, q4.9 NRR) now carry per-stage threshold tables under a `stage-thresholds` block alongside the fallback `thresholds` table. The scoring engine selects the table matching `profile_stage` at runtime; unknown stages fall back to the flat table. q4.4 (MoM growth rate) uses a single flat table across all stages — bands revised to `≤2%→15, 3-7%→30, 8-14%→55, 15-29%→78, ≥30%→95` to align with the global benchmark band scores used by all other threshold questions.
- `schema/scoring-rule.schema.json`: `stage-thresholds` added to `logic.properties` as an optional object whose keys are stage names and values are threshold arrays matching the existing threshold item schema.

### Added
- Dimension 4 (Product & Traction) fully drafted: 13 questions across 3 tiers (5 required, 5 recommended, 3 optional), 12 scoring rules (4 threshold-based for quantitative signals, 8 rubric-based for qualitative), 10 recommendation templates, and global benchmarks for customer count, MRR, month-over-month growth, and NRR across pre-seed, seed, and Series A. showIf conditions gate revenue and retention questions on product status (q4.1), so pre-revenue founders are not penalised for metrics they cannot provide. D4 README updated from skeleton to full specification.
- `show-if` conditional display: q1.5 (founder-market-fit narrative) now gates on `preq.stage in [pre-seed, seed]`; Series-A+ founders skip the open-text narrative because their track record substitutes it. Schema updated: `show-if` now requires a `conditions` array with `field`, `operator`, and `value`/`values` fields, replacing the earlier placeholder `{question, values}` format. Validator updated accordingly.
- Dimension 7 (Competition & Moat) fully populated: 12 questions across 3 tiers (5 required, 5 recommended, 2 optional), 11 scoring rules (all rubric-based), 11 recommendation templates covering competitive awareness, differentiation, incumbent threat, moat evidence, compounding mechanisms, switching costs, network effects, competitive deal evidence, and IP/regulatory barriers. q7.3 (moat type multi-select) is informational-only with weight 0.
- Dimension 7 README updated from skeleton to full specification
- CLAUDE.md with engineering standards, definition of done, pre-commit rule, spec-first discipline, git hygiene, and common task guides
- Dimension 3 (Market) fully populated: 14 questions across 3 tiers (6 required, 6 recommended, 2 optional), 14 scoring rules, 17 recommendation templates, and global benchmarks for TAM/SAM/SOM/CAGR signals across pre-seed, seed, and Series A stages
- Dimension 3 README updated from skeleton to full specification
- Dimension 2 (Problem & Insight) fully populated: 13 questions across 3 tiers, 11 scoring rules and rubrics, 17 recommendation templates, and global benchmarks for customer discovery interview counts
- Dimension 2 README updated from skeleton to full specification
- `count-question` field added to `schema/question.schema.json` validation block — allows a repeating-block question to declare a sibling single-select question whose answer is parsed as the minimum required row count
- q1.2 annotated with `count-question: q1.1` so the co-founder detail block enforces that the number of filled rows matches the co-founder count selected in q1.1
- `show-if` field added to `schema/question.schema.json` as a peer of `validation` — schema slot for future conditional question visibility (enforcement in the rendering layer); shape: `{ question: string, values: string[] }`
- ID pattern in `schema/question.schema.json` updated to allow `preq.[a-z-]+` style identifiers for pre-qualifying questions
- `framework/pre-qualifying/questions.yaml` created with two informational-only required questions: `preq.stage` (funding stage, 5 options) and `preq.region` (primary market region, 5 options)

## [0.1.1] - 2026-05-28

### Added
- Initial repository scaffolding
- Strategic documentation: philosophy, scoring methodology, regional strategy, VC archetypes, data flow, paywall strategy, glossary
- Architecture Decision Record 0001: YAML chosen as the structured data format for questions
- JSON Schemas for questions, scoring rules, benchmarks, archetypes, and recommendations
- Dimension 1 (Founder & Team) fully populated with questions, scoring, recommendations, and UK + global benchmarks
- Skeleton READMEs for Dimensions 2 through 8
- Five VC archetype skeleton definitions: Seed Generalist, Sector Specialist, Growth/Series A, Angel Syndicate, Strategic/Corporate
- Routing logic skeletons for stage, business model, and regional adaptation
- Regional skeleton files for UK, France, Germany, Netherlands, Nordics, and generic EU
- Validation tooling (`tooling/validate.py`)
- Example founder journey for a UK pre-seed SaaS founder
- GitHub issue templates and PR template
- CI workflow for schema validation

## [0.1.0] - 2026-05-28

Initial version. Repository created.
