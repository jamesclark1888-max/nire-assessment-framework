# Routing

This directory contains the logic that determines which questions a founder sees based on their context.

The full question bank is large (~150 questions across all dimensions, regional layers, and business model variants). Any individual founder typically sees 30-45 questions, selected by these routing rules.

---

## Routing files

- [`stage-routing.yaml`](stage-routing.yaml): adjusts question relevance by stage (pre-seed, seed, Series A)
- [`business-model-routing.yaml`](business-model-routing.yaml): hides or shows questions based on business model (SaaS, marketplace, hardware, deeptech, etc.)
- [`regional-routing.yaml`](regional-routing.yaml): adds regional regulatory and ecosystem questions based on country of incorporation

---

## How routing works

For each question in the framework:

1. The question's `applies-to` field defines its baseline applicability (e.g. "stages: all, business-models: all, regions: all")
2. Routing rules apply overrides (e.g. "hide q4.7 for pre-seed founders" or "show q5.fr1 only for French-incorporated founders")
3. The result is the founder-specific question set

Routing also affects **question weighting**, not just visibility. A question may be visible at all stages but weighted differently at each.

---

## Dimension weight overrides by stage

This is also defined here, because stage-based weighting is the most important routing decision.

| Dimension | Pre-seed | Seed | Series A |
|-----------|----------|------|----------|
| Founder & Team | 25% | 20% | 12% |
| Problem & Insight | 20% | 12% | 5% |
| Market | 15% | 12% | 10% |
| Product & Traction | 5% | 18% | 22% |
| Business Model | 5% | 12% | 18% |
| Go-to-Market | 10% | 10% | 15% |
| Competition & Moat | 10% | 8% | 10% |
| Round & Capital | 10% | 8% | 8% |

These are working values; calibration will refine them.
