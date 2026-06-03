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

### Added
- CLAUDE.md with engineering standards, definition of done, pre-commit rule, spec-first discipline, git hygiene, and common task guides
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
