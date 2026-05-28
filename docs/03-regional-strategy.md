# 03. Regional strategy

This document explains how the NIRE framework adapts to different geographies, why we made the trade-offs we did, and how to extend support to new regions.

---

## Core principle

**Geography is detected at the founder level, not the domain level.**

NIRE operates from a single primary domain (`nirehq.com`) regardless of the founder's location. We detect geography from:

1. The founder's country of incorporation (definitive, asked early)
2. IP geolocation (used to pre-populate dropdowns)
3. Browser locale (fallback hint)

We deliberately avoid splitting the product across multiple domains. Founders don't think in terms of domains; they think in terms of relevance to their context.

---

## Three layers of regional adaptation

### Layer 1: Core questions (~70% of the framework)

Universal. Founder backgrounds, problem insight, market logic, traction metrics, unit economics. Every founder sees these regardless of geography.

VCs everywhere care about these things even if they apply different thresholds.

### Layer 2: Regional questions (~20% of the framework)

Geography-specific. Examples:

- **UK**: EIS / SEIS status, EMI option schemes, R&D tax credits, Innovate UK grants
- **France**: BSPCE, JEI status, BPI France support, CIR (Crédit d'Impôt Recherche)
- **Germany**: GmbH/UG/AG structure, VSOP plans, EXIST grants, KfW programmes
- **Netherlands**: BV structure, WBSO, Innovation Box
- **Nordics**: Vinnova (SE), Tekes/Business Finland (FI), Innovation Norway (NO)

These questions are not asked of founders incorporated outside the relevant jurisdiction.

### Layer 3: Regional benchmarks (invisible to founders)

Same answers, scored against regional norms. A UK seed round of £1.2m is at the median; a US seed round of $1.2m is well below the median. The scoring engine uses the founder's country of incorporation to pick the right benchmarks.

---

## Three classification questions

We ask three separate geography questions early in the assessment because they often differ:

1. **Country of incorporation** → drives regulatory questions and benchmark selection
2. **Primary market** → drives market size benchmarks and competition analysis
3. **Founder location** → drives ecosystem-specific recommendations (e.g. "consider applying to Seedcamp" for UK-based founders)

This handles tricky cases like a Delaware C-corp run by UK founders selling primarily into Germany.

---

## Tiered regional support at launch

We support different depth levels for different regions to avoid promising precision we can't deliver.

### Tier 1: Deep support (launch)

- **United Kingdom**
- **Ireland**

Full regional question layer, full benchmark set, all VC archetypes available, UK-specific recommendation templates. The maintainer team has the deepest knowledge here.

### Tier 2: Strong support (launch)

- **France**
- **Germany**
- **Netherlands**
- **Nordics** (Sweden, Norway, Finland, Denmark)

Localised terminology and benchmarks, region-specific regulatory questions, VC archetype variants. Recommendations are tailored but may be lighter on local nuance than Tier 1.

### Tier 3: Generic EU support (launch)

All other EU/EEA countries. Generic EU benchmarks, no localised regulatory questions, EU-wide VC archetype averages. Honest about the lower precision.

### Tier 4: Acknowledged limitations

Countries outside Europe. We allow registration with a clear banner: "NIRE currently optimises for UK and EU founders. Your assessment will use generic benchmarks and may be less precise for your region." We capture the founder's data and ecosystem, which informs future expansion.

---

## How to add a new region

Adding a new region (e.g. Spain, Portugal, US) requires:

1. **Regulatory question layer** in `framework/regional/{country}.yaml`
2. **Benchmark file** in each dimension folder: `benchmarks/{country}.yaml`
3. **VC archetype regional variants** if the local market behaves differently
4. **Recommendation templates** with country-specific guidance (programmes, accelerators, tax schemes)
5. **Routing rules** updated in `framework/routing/regional-routing.yaml`
6. **Documentation** of the regulatory and ecosystem context
7. **Calibration** with at least 3 local VCs before promoting to Tier 1 or Tier 2

A region starts in Tier 4, progresses to Tier 3 once benchmarks exist, and is promoted to Tier 2/1 only after VC calibration confirms quality.

---

## The benchmark data problem

Benchmarks are the hardest part of regional adaptation. Sources we use:

- **Public reports**: Atomico State of European Tech, Dealroom, PitchBook, Beauhurst (UK), France Digitale
- **Government and trade body data**: BVA, Tech Nation, France Invest, BVK (Germany)
- **Direct VC partnerships**: VCs on the platform contribute calibrated thresholds
- **Founder data on NIRE itself**: as the platform scales, our own dataset becomes the most accurate benchmark

Benchmarks are versioned. Every benchmark file lists its source, the date it was last reviewed, and the date it expires (typically annually).

---

## What we don't do

- **We don't redirect users between domains based on location.** Confusing and bad SEO.
- **We don't translate the assessment.** English only for now. This is a deliberate trade-off; we'd rather be excellent in English than mediocre in five languages.
- **We don't auto-detect region without confirmation.** IP detection is for convenience, not authority. The founder always confirms.
- **We don't promise precision we don't have.** Where benchmarks are weak, we say so in the report.
