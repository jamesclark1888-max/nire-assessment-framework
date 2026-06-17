# Dimension 4: Product & Traction

**The VC underwriting question this answers:** *"Is it working? Is the product solving the problem and gaining adoption?"*

**Status:** 🟢 Drafted (v0.1.0)

---

## Why this dimension exists

At pre-seed, this dimension is light — often pre-product. At seed, it starts to matter materially. At Series A, it is the centre of gravity of the assessment. The framework handles all three stages through showIf conditions that gate revenue and retention questions on the founder's stated product status, so pre-revenue founders are not penalised for metrics they cannot yet provide.

This dimension assesses:

1. **Product status** — where the product is on the idea-to-scaling spectrum
2. **Quantitative traction** — customers, MRR, growth rate, NRR
3. **Qualitative traction** — the quality of customer relationships and documented outcomes
4. **Retention** — whether users and customers are staying
5. **Product discipline** — whether the team builds from evidence or assumption

---

## What this dimension assesses

### Required tier (5 questions)

- **q4.1** — Product status (single-select, informational-only): routes subsequent questions to the right benchmarks
- **q4.2** — Active paying customers or users (number, quantitative-threshold): primary adoption signal
- **q4.3** — Current MRR in GBP (number, quantitative-threshold): gated by showIf on live/scaling status
- **q4.4** — Month-over-month growth rate (number, quantitative-threshold): gated by showIf on mvp/live/scaling
- **q4.5** — Strongest traction evidence (long-text, ai-qualitative): highest-weight question in dimension

### Recommended tier (4 questions)

- **q4.6** — Primary retention metric (long-text, ai-qualitative): gated by showIf on live/scaling
- **q4.8** — 12-month product roadmap (long-text, ai-qualitative)
- **q4.9** — Net revenue retention / NRR (number, quantitative-threshold): gated by showIf on live/scaling; applies to SaaS/fintech/healthtech
- **q4.10** — Recent product iteration evidence (long-text, ai-qualitative)

### Optional deep-dive (3 questions)

- **q4.11** — Cohort retention analysis (long-text, ai-qualitative): gated by showIf on scaling status
- **q4.12** — Top 3-5 customers detail (long-text, ai-qualitative)
- **q4.13** — Product analytics evidence (long-text, ai-qualitative)

---

## Stage adaptation

This dimension has the heaviest stage variation of any dimension:

- **Pre-seed**: product status and qualitative signals are primary. MRR and NRR questions are hidden. Customer count benchmarks are low. The main question is whether there is any external evidence of value creation.
- **Seed**: paying customers, MRR, and growth rate become primary. Retention is expected. The main question is whether there is a repeatable pattern, not just individual success.
- **Series A**: cohort retention, NRR, and growth trajectory are primary. The main question is whether the economics scale and whether the product is building a compounding position.

showIf conditions implement this adaptation at the question level. The benchmark file (`benchmarks/global.yaml`) implements it at the scoring threshold level.

---

## Recommendation triggers

| Template ID | Trigger | Priority |
|---|---|---|
| `weak-traction-evidence` | q4.5 low | Critical (free-tier) |
| `no-early-traction` | q4.2 low | Critical (free-tier) |
| `improvable-traction-evidence` | q4.5 medium | High |
| `low-growth` | q4.4 low | High |
| `no-retention-data` | q4.6 low | Critical |
| `low-mrr` | q4.3 low | High |
| `unclear-roadmap` | q4.8 low | Medium |
| `weak-nrr` | q4.9 low | Medium |
| `no-product-iteration-signal` | q4.10 low | Medium |

---

## Weight distribution

Total scored weight: 0.87 across 11 scored questions (q4.1 is informational at 0.02).

| Question | Weight | Notes |
|---|---|---|
| q4.5 | 0.17 | Highest weight — primary traction signal |
| q4.2 | 0.13 | Customer/user count |
| q4.3 | 0.12 | MRR (showIf: live/scaling) |
| q4.4 | 0.11 | MoM growth (showIf: mvp/live/scaling) |
| q4.6 | 0.10 | Retention (showIf: live/scaling) |
| q4.8 | 0.07 | Product roadmap |
| q4.9 | 0.05 | NRR (showIf: live/scaling; SaaS only) |
| q4.10 | 0.04 | Product iteration |
| q4.11 | 0.04 | Cohort analysis (showIf: scaling) |
| q4.12 | 0.02 | Top customers |
| q4.13 | 0.02 | Product analytics |

---

## Files

- `questions.yaml` — all 13 questions with showIf conditions and scoring metadata
- `scoring.yaml` — 11 scoring rules (4 threshold, 7 rubric)
- `recommendations.yaml` — 8 recommendation templates
- `benchmarks/global.yaml` — stage-specific thresholds for customer count, MRR, growth rate, and NRR
