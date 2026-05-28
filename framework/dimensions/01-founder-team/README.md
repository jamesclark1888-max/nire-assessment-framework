# Dimension 1: Founder & Team

**The VC underwriting question this answers:** *"Are these the right people to build this, and can they attract the talent they'll need?"*

---

## Why this dimension exists

At pre-seed and seed stage, this is the single most important factor in a VC's decision. The product will change. The market will shift. The strategy will evolve. The people, more often than not, are the constant the VC is betting on.

Even at Series A, team quality remains a primary determinant of execution risk. Strong teams with mediocre traction often get funded; mediocre teams with strong traction often don't.

This dimension assesses:

1. **Who the founders are** (background, experience, prior outcomes)
2. **How they fit together** (working history, role coverage, equity dynamics)
3. **What they're missing** (gaps that need to be filled by hires or advisors)
4. **How they think about themselves** (self-awareness, coachability, ambition)

---

## What this dimension does not assess

- The quality of the problem they're working on (Dimension 2)
- The size of the market (Dimension 3)
- Their go-to-market capability as a function (Dimension 6)
- Their fundraising terms (Dimension 8)

We avoid scope creep into other dimensions. A founder's commercial talent is assessed here in terms of team coverage; their actual GTM strategy is assessed in Dimension 6.

---

## Question structure

### Required tier (5 questions)
Minimum for a meaningful score. Targets ~5 minutes to complete.

### Recommended tier (5 questions)
Improves confidence and unlocks sharper recommendations. Adds ~5 minutes.

### Optional deep-dive (4 questions)
For founders who want maximum precision. Adds ~5-10 minutes depending on uploads.

### Regional layers
Added based on country of incorporation:

- **UK**: 2 questions (EMI, SEIS/EIS structuring)
- **France**: 2 questions (BSPCE, JEI status)
- **Germany**: 2 questions (entity type, VSOP)
- **Other tier 2 regions**: TBD as added
- **Generic EU**: 0 additional questions

---

## How it's scored

The dimension score is the weighted sum of question scores. Weights vary by stage (see `scoring.yaml`).

Key signals the engine surfaces:

- **Solo founder flag**: at seed and beyond, raises probability that the founder needs to articulate why they can attract talent
- **Working relationship strength**: longer prior collaboration → higher score
- **Function coverage**: missing critical functions create gaps reflected in score and recommendations
- **Prior exit signal**: repeat founders score higher with most archetypes
- **Founder-market fit quality**: AI-evaluated against rubric

---

## Files in this directory

- [`questions.yaml`](questions.yaml) - the question definitions
- [`scoring.yaml`](scoring.yaml) - scoring rules and rubrics
- [`recommendations.yaml`](recommendations.yaml) - AI recommendation templates
- [`benchmarks/`](benchmarks/) - regional benchmark data

---

## Archetype interactions

Different VC archetypes weight this dimension differently:

| Archetype | Dimension weight | Notes |
|-----------|------------------|-------|
| Seed Generalist | High | Team is the bet at seed |
| Sector Specialist | Very high | Domain expertise is decisive |
| Growth / Series A | Medium-high | Still matters but traction matters more |
| Angel Syndicate | Very high | Often a pure team bet |
| Strategic / Corporate | Medium | Care about ability to navigate enterprise |

---

## Open questions / future work

- Calibration of the founder-market fit rubric with 3+ working VCs
- Whether to add a "founder mental health / sustainability" question (sensitive, but increasingly relevant)
- Whether to add a "diversity composition" question (data only, no scoring impact, for VC-side filtering only with consent)
- Whether to include LinkedIn URL parsing for automated background scoring (privacy implications)
