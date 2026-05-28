# VC Archetypes

This directory contains the definitions of VC archetypes used to score founder answers through different investor lenses.

Each archetype is defined in its own YAML file, validated against `schema/archetype.schema.json`.

---

## Current archetypes (v0.1.0)

| ID | Name | Status |
|----|------|--------|
| `seed-generalist` | Seed Generalist | 🟡 Skeleton |
| `sector-specialist` | Sector Specialist | 🟡 Skeleton |
| `growth-series-a` | Growth / Series A | 🟡 Skeleton |
| `angel-syndicate` | Angel Syndicate | 🟡 Skeleton |
| `strategic-corporate` | Strategic / Corporate | 🟡 Skeleton |

Skeleton means weights are set but bonus/penalty rules and question-level adjustments are not yet fully populated.

---

## How archetype scoring works

For each archetype, the same founder answers are re-scored:

1. The base dimension scores are weighted using the archetype's `dimension-weights`
2. Question-level adjustments are applied where this archetype values specific questions differently
3. Bonus and penalty rules are applied based on the founder's profile

The result is an archetype-specific score that tells the founder how each investor type would view them.

---

## Regional variants

Each archetype may have regional variants. A UK Seed Generalist behaves slightly differently from a French Seed Generalist (different reference points, different ecosystem norms). Where significant, these variants are defined in the `regional-variants` section of the archetype file.

---

## How to add an archetype

1. Create a new YAML file in this directory: `your-archetype.yaml`
2. Validate against `schema/archetype.schema.json`
3. Document the rationale in `docs/04-vc-archetypes.md`
4. Add to the table above
5. Calibrate with at least 3 real VCs of this archetype before promoting from skeleton to active

---

## Future archetypes (planned)

- Pre-seed Specialist (distinct from Seed Generalist)
- Crossover / Hedge Fund
- Family Office
- Impact / ESG-focused
- Solo GP / Emerging Manager
