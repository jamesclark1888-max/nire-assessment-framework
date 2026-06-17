# Dimension 6: Go-to-Market

**The VC underwriting question this answers:** *"Can they reach customers efficiently and repeatably?"*

**Status:** 🟢 Drafted. Shipped in v0.1.0 of the assessment framework.

---

## Why this dimension exists

A great product without distribution is a hobby. VCs weight GTM capability heavily at pre-seed because product-market fit is often achievable, but distribution is harder to build and harder to fake. A founder who can name a specific buyer, a specific purchase trigger, and a channel that is already producing customers is demonstrably further along than one who describes a plan.

This dimension assesses the specificity of the ICP, the evidence of working channels, and the ability to describe acquisition economics — not the scale of current traction, which D4 (Product & Traction) handles.

---

## What this dimension assesses

1. **ICP and sales motion** (q6.4, required, ai-qualitative, weight 0.22): specificity of buyer definition, named purchase trigger, and coherence of the sales motion
2. **Channel evidence** (q6.5, required, ai-qualitative, weight 0.20): observed evidence of channel traction, rationale for channel selection, and next validation step
3. **Sales cycle length** (q6.3, required, quantitative-threshold, weight 0.12): ascending scoring; 0 = no sale yet; 1–30 days = highest signal
4. **Pipeline value** (q6.6, recommended, quantitative-threshold, weight 0.12): qualified pipeline in GBP as a forward revenue signal
5. **Conversion rate** (q6.7, recommended, quantitative-threshold, weight 0.10): discovery-to-close rate; non-monotonic above 60% (small-sample noise)
6. **Channel economics** (q6.10, recommended, ai-qualitative, weight 0.10): CAC estimate and repeatability case
7. **Channel concentration** (q6.9, recommended, categorical, weight 0.07): all-one-channel is structurally fragile even when the channel works
8. **GTM roadmap** (q6.11, optional, ai-qualitative, weight 0.05): milestone-based plan with resource coherence

Informational questions (q6.1 GTM motion type, q6.2 current channels, q6.8 sales team composition, q6.12 CRM upload) carry weight 0.02 or 0.00 and do not affect scoring.

---

## Question structure

### Required tier (5 questions, 2 AI-qualitative)
- `q6.1` — Primary GTM motion (single-select, informational)
- `q6.2` — Current acquisition channels (multi-select, informational)
- `q6.3` — Sales cycle length in days (number, quantitative-threshold)
- `q6.4` — ICP definition and sales motion (long-text, ai-qualitative, min-chars 80)
- `q6.5` — Channel strategy and traction evidence (long-text, ai-qualitative, min-chars 60)

### Recommended tier (5 questions)
- `q6.6` — Qualified pipeline value in GBP thousands (number, quantitative-threshold)
- `q6.7` — Discovery-to-close conversion rate % (number, quantitative-threshold)
- `q6.8` — Sales team composition (single-select, informational)
- `q6.9` — Channel concentration (single-select, categorical)
- `q6.10` — Channel economics and repeatability (long-text, ai-qualitative)

### Optional tier (2 questions)
- `q6.11` — 12-month GTM roadmap (long-text, ai-qualitative)
- `q6.12` — CRM or pipeline data upload (file-upload, informational)

---

## Scoring notes

- `q6.3` is ascending: shorter sales cycles generate evidence faster at pre-seed. Score 0 as 30 to distinguish "no sale yet" from a genuine fast cycle.
- `q6.7` is non-monotonic above 60%: very high conversion rates at small pre-seed sample sizes may reflect non-representative pipeline rather than exceptional execution.
- `q6.4` and `q6.5` are the **multi-faceted signal exception**: two required prose anchors were justified because ICP/sales-motion and channel-evidence are genuinely independent signals — neither can substitute for the other — analogous to D7's q7.2/q7.5 split.
- No `showIf` gates in v0.1: all GTM motion types can answer all questions. Deferred to avoid penalty-bug surface area.

---

## Recommendation templates (11)

| ID | Priority | Trigger | Free |
|---|---|---|---|
| `gtm-sales-cycle-long` | high | q6.3 low | yes |
| `gtm-icp-undefined` | critical | q6.4 low | yes |
| `gtm-channel-no-evidence` | critical | q6.5 low | yes |
| `gtm-sales-cycle-moderate` | medium | q6.3 medium | no |
| `gtm-icp-partial` | high | q6.4 medium | yes |
| `gtm-channel-untested` | high | q6.5 medium | yes |
| `gtm-pipeline-thin` | high | q6.6 low | no |
| `gtm-conversion-low` | medium | q6.7 low | no |
| `gtm-channel-concentrated` | medium | q6.9 low | no |
| `gtm-cac-unknown` | medium | q6.10 low | no |
| `gtm-cac-partial` | low | q6.10 medium | no |

---

## Benchmarks

See `benchmarks/uk.yaml` for UK pre-seed B2B SaaS thresholds. US benchmarks are a v0.2 workstream.
