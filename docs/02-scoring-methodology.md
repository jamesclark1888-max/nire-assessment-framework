# 02. Scoring methodology

This document explains how the NIRE assessment translates founder answers into scores, confidence ratings, and recommendations.

---

## The scoring model in plain English

For each of the 8 dimensions, a founder receives:

1. **A dimension score** (0-100)
2. **A confidence rating** (low / medium / high)
3. **A set of gap-based recommendations**
4. **Per-archetype views** of the same data

These are aggregated into:

- **An overall NIRE score** (0-100)
- **An overall confidence rating**
- **An archetype breakdown** (how each VC type would view the founder)
- **A prioritised recommendation list**

---

## How a dimension score is calculated

Each dimension is composed of multiple questions across three tiers. Every question has:

- A **scoring type** (quantitative, categorical, qualitative-AI, multi-select, etc.)
- A **weight** within the dimension (sums to 1.0 across all dimension questions)
- A **scoring rule** that translates the raw answer into a 0-100 score

The dimension score is the weighted sum of question scores.

### Quantitative scoring

For numeric answers (e.g. MoM growth rate, CAC payback period), we use regional benchmark thresholds:

```
0-100 score = piecewise function of (answer, regional benchmark thresholds)
```

Example: MoM revenue growth for UK seed SaaS:
- Above 20%: 100
- 10-20%: linear scale 70-100
- 5-10%: linear scale 40-70
- 0-5%: linear scale 10-40
- Negative: 0

### Categorical scoring

For multi-choice answers, each option is mapped to a score. Example: prior working relationship of founders:
- Never worked together: 30
- Less than 1 year: 50
- 1-3 years: 80
- 3+ years: 100

### Qualitative (AI) scoring

For open-text answers (e.g. founder-market fit paragraph), we use a rubric-based AI evaluation:

- The answer is evaluated against a defined rubric (e.g. specificity, evidence, unfair advantage, clarity)
- The AI returns a score plus a structured critique
- The critique is stored and used both for the recommendation AND for VC-side richness

Qualitative scores are bounded (e.g. 30-95 instead of 0-100) to reflect inherent subjectivity.

### Multi-select scoring

For multi-select questions, scores are calculated against expected coverage. Example: critical functions covered by team:
- Each missing function applies a deduction proportional to its importance at the founder's stage

---

## Confidence ratings

Confidence reflects how complete the data is.

| Tier completion | Confidence rating |
|-----------------|-------------------|
| Required only | Medium |
| Required + 50% of recommended | Medium-High |
| Required + 100% of recommended | High |
| Required + recommended + optional | Very High |

If a founder skips required questions, the dimension is marked as **incomplete** and contributes a "needs data" recommendation rather than a score.

---

## Weightings across dimensions

The 8 dimension scores are aggregated into the overall NIRE score with weights that **vary by stage**:

### Pre-seed weighting (team-heavy)
- Founder & Team: 25%
- Problem & Insight: 20%
- Market: 15%
- Product & Traction: 5%
- Business Model: 5%
- Go-to-Market: 10%
- Competition & Moat: 10%
- Round & Capital: 10%

### Seed weighting (balanced with traction emphasis)
- Founder & Team: 20%
- Problem & Insight: 12%
- Market: 12%
- Product & Traction: 18%
- Business Model: 12%
- Go-to-Market: 10%
- Competition & Moat: 8%
- Round & Capital: 8%

### Series A weighting (metrics-heavy)
- Founder & Team: 12%
- Problem & Insight: 5%
- Market: 10%
- Product & Traction: 22%
- Business Model: 18%
- Go-to-Market: 15%
- Competition & Moat: 10%
- Round & Capital: 8%

These weightings are themselves under review and will be calibrated based on real VC feedback. They are defined in `framework/routing/stage-routing.yaml`.

---

## Archetype scoring

The same answers are scored a second time through each VC archetype's lens. Each archetype has:

- Its own **weighting profile** (Sector Specialists weight Founder & Team's domain expertise higher than generalists do)
- Its own **deduction rules** (Growth/Series A VCs penalise weak unit economics far more than seed generalists)
- Its own **bonus rules** (Strategic/Corporate VCs reward enterprise traction and partnership signal)

Archetypes are defined in `framework/archetypes/`.

---

## How recommendations are generated

Recommendations are not free-form AI output. They are templated and triggered by scoring conditions.

For each question (and for combinations of questions), there are defined **recommendation triggers**:

```yaml
recommendation_trigger:
  low_score: <template-id>
  medium_score: <template-id>
  high_score: null  # No rec needed if scoring well
```

Recommendation templates contain:

- The **diagnostic** (what the founder's answers indicate)
- The **specific gap** (what's missing)
- The **fix** (what to do about it)
- The **evidence** (why VCs care)
- The **stage-appropriate framing** (a pre-seed and Series A founder receive different versions)

AI is used to **personalise** templated recommendations using the founder's specific data, not to generate them from scratch. This keeps quality high and behaviour predictable.

---

## Anti-gaming measures

Sophisticated founders will try to optimise their score. The framework anticipates this:

1. **Cross-question consistency checks**: if claimed MRR doesn't reconcile with claimed customer count and reported pricing, the inconsistency is flagged.
2. **Document verification**: optional uploads (bank statements, Stripe screenshots) increase confidence rating and unlock VC-side visibility.
3. **Time-stamped answers**: founders who change answers dramatically between sessions are flagged for review.
4. **Honest self-assessment questions**: questions like "what are the biggest risks in your team?" reward thoughtful honesty and the AI scores deflective answers lower.

---

## Calibration plan

This methodology is v1. Real-world calibration will happen by:

1. Recruiting 10-20 VC partners to score a sample of founder profiles blind
2. Comparing their scores to NIRE-generated scores
3. Adjusting weights, thresholds, and rubrics where divergence is significant
4. Publishing periodic calibration reports

See [Architecture Decision Record 0002 (TBD)] for the calibration framework.
