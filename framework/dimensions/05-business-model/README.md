# Dimension 5: Business Model & Unit Economics

**The VC underwriting question this answers:** *"Can this make money? Do the economics work at scale?"*

**Status:** 🟢 Drafted (v0.1.0)

---

## Why this dimension exists

A growing user base with unworkable unit economics is the most expensive kind of failure. This dimension assesses whether the path from customer to profit is plausible — and whether the founder has stress-tested the numbers or is projecting an optimistic case.

At pre-seed, unit economics are often modelled. At seed, they should be measurable in early cohorts. At Series A, they are expected to be evidenced and improving.

This dimension assesses:

1. **Revenue model** — how the business makes money and what model-appropriate benchmarks apply
2. **Pricing** — how pricing was derived, tested, and whether evidence of pricing power exists
3. **Gross margin** — the structural ceiling on long-run profitability
4. **Unit economics** — the complete picture of CAC, delivery cost, LTV, and payback
5. **Path to viable economics** — at what scale the model becomes self-sustaining and what assumptions it depends on
6. **Scalability** — how each cost category behaves at 5-10x current revenue

---

## What this dimension assesses

### Required tier (5 questions)

- **q5.1** — Revenue model type (single-select, informational-only): routes the assessment to model-appropriate benchmarks; does not re-ask q4.3
- **q5.2** — Pricing rationale and evidence (long-text, ai-qualitative): the highest-weight qualitative question; evidence of price changes accepted by customers scores highest
- **q5.3** — Gross margin percentage (number, quantitative-threshold): flat thresholds, no stage variation — structural ceiling applies at all stages
- **q5.4** — Full unit economics walkthrough (long-text, ai-qualitative): highest weight in dimension; requires all three components (acquisition cost, delivery cost, lifetime value)
- **q5.5** — Scale inflection and assumptions (long-text, ai-qualitative): path from current economics to viability with named assumptions

### Recommended tier (4 questions)

- **q5.6** — LTV:CAC ratio (number, quantitative-threshold): gated by showIf on live/scaling status; stage-specific thresholds
- **q5.7** — CAC payback period in months (number, quantitative-threshold): gated by showIf on live/scaling status; inverted scale (lower = better); stage-specific thresholds
- **q5.8** — Pricing power evidence (long-text, ai-qualitative): evidence of accepted price increases or premium competitive wins
- **q5.9** — Model scalability analysis (long-text, ai-qualitative): how each major cost category behaves at scale

### Optional deep-dive (2 questions)

- **q5.10** — Unit economics sensitivity analysis (long-text, ai-qualitative): which assumptions matter most and how far they can shift
- **q5.11** — Cost structure breakdown (long-text, ai-qualitative): three to five largest cost categories and their scale behaviour

---

## Stage adaptation

- **Pre-seed**: pricing rationale, gross margin, and the unit economics walkthrough are primary. LTV:CAC and payback (q5.6, q5.7) are hidden until the product is live. The main question is whether the founder has thought through the economics, not whether they are proven.
- **Seed**: quantitative benchmarks for LTV:CAC and payback become primary. Pricing power evidence is expected from at least one documented test. Gross margin should reflect actual delivery, not estimates.
- **Series A**: all questions are in scope. LTV:CAC benchmarks tighten at Series A level (≥7× target). CAC payback stricter (≤6 months target). Pricing power evidence is expected from multiple data points.

showIf conditions on q5.6 and q5.7 gate them on `q4.1 in [live, scaling]`. Pre-revenue founders are not penalised for metrics they cannot yet provide. The scoring engine does not currently evaluate showIf conditions — unanswered recommended questions receive the penalty score of 15 regardless of product status. This is a known backlog item and pre-launch blocker.

---

## Recommendation triggers

| Template ID | Question | Trigger | Priority |
|---|---|---|---|
| `weak-unit-economics` | q5.4 | low | Critical (free-tier) |
| `low-gross-margin` | q5.3 | low | Critical (free-tier) |
| `weak-pricing-rationale` | q5.2 | low | High |
| `improvable-unit-economics` | q5.4 | medium | High |
| `unclear-profitability-path` | q5.5 | low | High |
| `low-ltv-cac` | q5.6 | low | High |
| `long-cac-payback` | q5.7 | low | High |
| `improvable-pricing-rationale` | q5.2 | medium | Medium |
| `no-pricing-power-evidence` | q5.8 | low | Medium |
| `unclear-model-scalability` | q5.9 | low | Medium |

---

## Weight distribution

Total scored weight: 1.11 across 10 scored questions (q5.1 is informational at 0.02).

| Question | Weight | Notes |
|---|---|---|
| q5.4 | 0.19 | Highest weight — complete unit economics walkthrough |
| q5.2 | 0.16 | Pricing rationale and evidence |
| q5.3 | 0.15 | Gross margin (flat thresholds, all stages) |
| q5.5 | 0.14 | Scale inflection and assumptions |
| q5.6 | 0.12 | LTV:CAC (showIf: live/scaling; stage-thresholds) |
| q5.7 | 0.11 | CAC payback inverted (showIf: live/scaling; stage-thresholds) |
| q5.8 | 0.08 | Pricing power evidence |
| q5.9 | 0.07 | Model scalability |
| q5.10 | 0.04 | Sensitivity analysis (optional) |
| q5.11 | 0.03 | Cost structure (optional) |

---

## Scoring notes

- **q5.3 gross margin**: flat thresholds — ≥80%→95, 65–79%→78, 40–64%→55, 20–39%→30, <20%→15. No stage variation because the structural ceiling on profitability is model-dependent, not stage-dependent.
- **q5.6 LTV:CAC**: stage-thresholds. Pre-seed and seed share the same bands (≥7→95, 4.0–6.9→78, 2.0–3.9→55, 0.5–1.9→30, ≤0.4→15). Series A tightens at the top (only ≥10 hits 95).
- **q5.7 CAC payback**: inverted threshold (lower is better). Pre-seed: ≤6 months→95, 7–12→78, 13–24→55, 25–48→30, ≥49→15. Series A stricter: ≤6→95, 7–12→78, 13–18→55, 19–24→30, ≥25→15.
- **Rubric questions** (q5.2, q5.4, q5.5, q5.8, q5.9, q5.10, q5.11): scored by HeuristicScorer at min=15, max=88–90. AnthropicScorer is stubbed and not yet wired; swap is controlled by `SCORING_STRATEGY` env var.

---

## Files

- `questions.yaml` — 11 questions with showIf conditions and scoring metadata
- `scoring.yaml` — 10 scoring rules (3 threshold, 7 rubric)
- `recommendations.yaml` — 10 recommendation templates
- `benchmarks/global.yaml` — stage-specific thresholds for gross margin, LTV:CAC, and CAC payback
