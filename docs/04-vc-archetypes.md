# 04. VC archetypes

This document defines the VC archetypes that score founder answers through different lenses. It is one of the most distinctive parts of the NIRE framework.

---

## Why archetypes matter

A solo technical founder building deeptech receives very different reactions from different VCs:

- A **generalist seed VC** sees a yellow flag (no commercial co-founder)
- A **deeptech specialist** sees a green flag (technical depth is the bet)
- A **growth-stage VC** sees a red flag (no GTM leadership at the maturity they invest in)
- An **angel syndicate** is comfortable backing technical solo founders if the angle is right
- A **strategic corporate VC** cares more about partnership/integration potential than founder shape

If we score everyone with a single "VC view," we hide this nuance. The archetype layer surfaces it.

Founders see their overall NIRE score plus an archetype breakdown: which investor types view them favourably, which would be sceptical, and why.

---

## The five archetypes (launch)

### 1. Seed Generalist

The default mental model. UK examples: Seedcamp, LocalGlobe, Episode 1, Octopus Ventures (early funds), Forward Partners. EU examples: Point Nine (early), Cherry Ventures, Daphni.

**What they weight heavily:**
- Founder & Team (especially founder-market fit and ability to attract talent)
- Problem & Insight (non-obvious truth)
- Market (large or fast-growing)

**What they tolerate:**
- Early-stage traction (or lack thereof)
- Unit economics still being theoretical
- Pivots, if grounded in learning

**What they penalise:**
- Generic founder-market fit answers
- Vague "we'll figure out distribution later"
- Solo founders without a clear plan to add talent

### 2. Sector Specialist

VCs focused on a specific vertical: deeptech, fintech, healthtech, climate, AI, etc.

**What they weight heavily:**
- Domain expertise in the team
- Insight quality (do they know things outsiders don't)
- Regulatory understanding (where relevant)

**What they tolerate:**
- Long product development cycles
- Capital-intensive paths if the prize is large
- Smaller initial TAM if the strategic position is strong

**What they penalise:**
- "Tourist" founders entering a complex space without depth
- Weak technical/scientific moat in a technical/scientific market

### 3. Growth / Series A

VCs deploying larger cheques at the Series A stage. UK examples: Balderton, Index Ventures, Accel London, Atomico (early growth). EU examples: Lakestar, Highland Europe, EQT Ventures.

**What they weight heavily:**
- Product & Traction (real metrics, not vanity)
- Unit Economics (CAC, LTV, payback, gross margin)
- Go-to-Market (proven, repeatable motion)

**What they tolerate:**
- Smaller TAM if growth is exceptional
- Founder gaps that can be filled by experienced hires

**What they penalise:**
- Pre-product-market-fit signal at Series A pricing
- Weak unit economics
- "Spray and pray" GTM with no evidence of a working channel

### 4. Angel Syndicate

Groups of angels investing together, often in pre-seed and seed. Includes platforms like SyndicateRoom, Odin, AngelList syndicates.

**What they weight heavily:**
- Founder quality and personal conviction
- Speed of decision-making (clear ask, clear use of funds)
- Brand-name angels already involved (social proof)

**What they tolerate:**
- Smaller initial TAM
- Less institutional rigour
- Founders without prior exits

**What they penalise:**
- Unclear or shifting fundraising terms
- Disorganised cap tables
- Slow founder responsiveness

### 5. Strategic / Corporate VC

CVCs investing for strategic alignment as well as financial return.

**What they weight heavily:**
- Partnership and integration potential
- Enterprise customer traction
- Regulatory and compliance posture
- Founder ability to navigate corporate procurement

**What they tolerate:**
- Slower growth if strategic value is high
- Lower IRR expectations (offset by strategic value)

**What they penalise:**
- Pure consumer plays with no enterprise angle
- IP positions that conflict with the parent corporation
- Inability to articulate strategic value beyond "we're disruptive"

---

## How archetypes are defined in the framework

Each archetype is a YAML file in `framework/archetypes/` containing:

- A name and description
- A **weighting profile** (how it weighs each of the 8 dimensions)
- **Question-level adjustments** (specific questions that score differently for this archetype)
- **Bonus and penalty rules**
- **Stage applicability** (some archetypes don't apply at certain stages)
- **Regional variants** (a UK Seed Generalist behaves slightly differently from a French one)

---

## What founders see

In the founder report, archetype breakdown shows:

- **Best fit archetype** (highest score)
- **Worst fit archetype** (lowest score)
- **A grid view** showing how each archetype would view each dimension
- **Specific advice per archetype** ("Sector specialists would want to see X; you don't currently signal this")

This is one of the most powerful parts of the founder experience because it makes the invisible visible: founders learn which VCs to target and which to avoid.

---

## What VCs see

On the VC side, each VC user is mapped to one or more archetypes (often a primary plus secondaries). Their dashboard shows founders ranked according to their archetype's specific scoring, not the generic NIRE score.

This is why VCs pay: they get a personalised view of the founder pool, calibrated to their own investment thesis.

---

## Future archetypes (not in v1)

- **Pre-seed Specialist** (distinct from Seed Generalist; smaller cheques, longer time horizons)
- **Crossover / Hedge Fund** (late-stage VC behaviour, different metric weightings)
- **Family Office** (long-term orientation, IRR less central)
- **Impact / ESG-focused** (impact metrics weighted alongside financial)
- **Solo GP / Emerging Manager** (faster decisions, smaller checks, conviction-driven)

These will be added as the platform matures and as we calibrate with real investors of these types.
