# NIRE Assessment Framework

> The single source of truth for NIRE's founder investment readiness assessment.

**Owner:** NIRE HQ LIMITED
**Status:** Active development
**Version:** 0.1.0

---

## What this is

This repository defines the complete intellectual framework behind NIRE's founder assessment product. It contains:

- The strategic philosophy behind our approach
- The full question bank, structured for machine consumption
- The scoring methodology and weightings
- Regional adaptation layers (UK, France, Germany, etc.)
- VC archetype scoring lenses
- AI recommendation templates
- Routing logic for adaptive questionnaires

This framework is the source of truth. The founder-side questionnaire app and the VC-side dashboard both consume from here. When the framework changes, the products change.

---

## Why this exists as a separate repo

1. **Product spec evolves separately from code.** The framework is updated based on VC feedback, market changes, and product learnings, independent of any code release cycle.
2. **It is the core IP.** As a potential acquisition target, this framework is one of the most valuable assets of the company. It deserves its own home, its own version history, and its own governance.
3. **Multiple consumers.** The founder app, the VC dashboard, AI pipelines, and marketing content all reference this framework. A single source of truth prevents drift.
4. **Auditability.** Version control on every question change, scoring tweak, and benchmark update is essential for trust on both sides of the marketplace.

---

## Repository structure

```
nire-assessment-framework/
├── docs/              # Strategic thinking, methodology, decisions
├── framework/         # The assessment itself (questions, scoring, archetypes)
├── schema/            # JSON Schema validation for all framework files
├── tooling/           # Scripts for validation, analysis, reporting
└── examples/          # Worked examples of founder journeys and outputs
```

See [`docs/00-overview.md`](docs/00-overview.md) for a full guided tour.

---

## Navigating this repo

**If you want to understand the philosophy:** Start with [`docs/01-philosophy.md`](docs/01-philosophy.md).

**If you want to see how scoring works:** Read [`docs/02-scoring-methodology.md`](docs/02-scoring-methodology.md).

**If you want to see a worked dimension:** Look at [`framework/dimensions/01-founder-team/`](framework/dimensions/01-founder-team/).

**If you want to know how a founder journey plays out:** Browse [`examples/`](examples/).

**If you're contributing changes:** Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

---

## Status of dimensions

| # | Dimension | Status |
|---|-----------|--------|
| 1 | Founder & Team | ✅ Drafted |
| 2 | Problem & Insight | ✅ Drafted |
| 3 | Market | ✅ Drafted |
| 4 | Product & Traction | 🟡 Skeleton |
| 5 | Business Model & Unit Economics | 🟡 Skeleton |
| 6 | Go-to-Market | 🟡 Skeleton |
| 7 | Competition & Moat | 🟡 Skeleton |
| 8 | Round & Capital Strategy | 🟡 Skeleton |

---

## Licence

Proprietary. See [`LICENSE`](LICENSE). All contributions are subject to the terms in [`CONTRIBUTING.md`](CONTRIBUTING.md).

© 2026 NIRE HQ LIMITED. All rights reserved.
