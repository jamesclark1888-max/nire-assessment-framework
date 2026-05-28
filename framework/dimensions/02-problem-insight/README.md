# Dimension 2: Problem & Insight

**The VC underwriting question this answers:** *"What non-obvious truth does this team know about this problem?"*

**Status:** ✅ Drafted (v0.1.0)

---

## Why this dimension exists

The best startups are built on an insight that is not yet widely understood. They see a problem clearly that most people see blurrily, or they see something true that the market hasn't yet priced in.

This dimension assesses the quality of the founder's insight, the depth of their problem understanding, and the customer evidence behind it. At pre-seed and seed, this is the second-most important dimension after Founder & Team — because before there is traction, there is only insight.

This dimension assesses:

1. **Problem articulation**: how clearly the founder describes the problem in customer language
2. **Customer evidence**: how many real customers they've spoken to and what they learned
3. **Insight depth**: the non-obvious truth that makes this company defensible
4. **Problem urgency**: why this needs solving now (timing thesis)
5. **Evidence breadth**: what independent signals validate that the problem is real
6. **Alternatives understanding**: what customers currently use and why it fails
7. **Counter-intuitive beliefs**: what the founder knows that others don't

---

## What this dimension does not assess

- The size of the addressable market (Dimension 3)
- Whether the product solves the problem (Dimension 4)
- Whether there is a commercial model to capture the value (Dimension 5)
- Competitive positioning and moat (Dimension 7)

Competitive alternatives are referenced here only as evidence of the problem; positioning strategy and moat belong in Dimension 7.

---

## Question structure

### Required tier (5 questions)
Minimum for a meaningful score. Targets approximately 5-7 minutes to complete.

| ID | Type | Signal |
|----|------|--------|
| q2.1 | Long-text | Problem articulation quality |
| q2.2 | Number | Customer discovery depth |
| q2.3 | Long-text | Core insight strength (highest weight) |
| q2.4 | Long-text | Timing thesis |
| q2.5 | Multi-select | Evidence signal breadth |

### Recommended tier (5 questions)
Improves confidence and unlocks sharper recommendations. Adds approximately 5 minutes.

| ID | Type | Signal |
|----|------|--------|
| q2.6 | Long-text | Best customer story / direct quote |
| q2.7 | Single-select | Problem severity |
| q2.8 | Long-text | Alternatives analysis depth |
| q2.9 | Long-text | Knowledge of prior failed attempts |
| q2.10 | Long-text | Contrarian belief |

### Optional deep-dive (3 questions)
For founders seeking maximum precision. Adds approximately 5-10 minutes.

| ID | Type | Signal |
|----|------|--------|
| q2.11 | File upload | Discovery artefacts (increases confidence rating) |
| q2.12 | Structured input | Customer profile breakdown |
| q2.13 | Long-text | Hypothesis evolution narrative |

### Regional layers
This dimension has no region-specific questions. Problem insight is assessed universally. Regional context surfaces in Dimensions 3 (Market) and 8 (Round & Capital).

---

## How it's scored

The dimension score is the weighted sum of question scores. Key weights:

| Question | Weight | Rationale |
|----------|--------|-----------|
| q2.3 (core insight) | 20% | Primary differentiator; most predictive of long-term defensibility |
| q2.1 (problem articulation) | 15% | Foundational: must be in customer language |
| q2.2 (customer interviews) | 15% | Quantitative proxy for discovery rigour |
| q2.4 (timing thesis) | 15% | Critical signal for pre-seed and seed |
| q2.5 (evidence breadth) | 10% | Multi-signal validation |

Most scoring in this dimension is AI-evaluated qualitative (rubric-based). The only
quantitative signal is customer interview count (q2.2), benchmarked by stage.

---

## Files in this directory

- [`questions.yaml`](questions.yaml) — question definitions
- [`scoring.yaml`](scoring.yaml) — scoring rules and rubrics
- [`recommendations.yaml`](recommendations.yaml) — AI recommendation templates
- [`benchmarks/global.yaml`](benchmarks/global.yaml) — global benchmark data

---

## Archetype interactions

Different VC archetypes weight this dimension differently:

| Archetype | Dimension weight | Notes |
|-----------|-----------------|-------|
| Seed Generalist | High (12% of overall score) | Strong insight compensates for early traction |
| Sector Specialist | Very high | Domain insight is the primary filter |
| Growth / Series A | Low (5% of overall score) | Largely displaced by traction data |
| Angel Syndicate | High | Often betting on insight before product |
| Strategic / Corporate | Medium | Cares about insight relevance to their sector |

---

## Open questions / future work

- Calibration of the core-insight rubric with 3+ working VCs — the non-obviousness criterion is the hardest to score consistently
- Whether to add a structured "customer interview log" repeating-block to replace or supplement q2.2 (count alone is a weak signal)
- Whether to add a cross-dimension consistency check between q2.3 (insight) and q1.5 (founder-market fit) — the two answers should be mutually reinforcing
- Whether q2.10 (contrarian insight) should be moved to required tier at pre-seed given its predictive weight
