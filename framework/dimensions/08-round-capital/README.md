# Dimension 8: Round & Capital Strategy

**The VC underwriting question this answers:** *"Is this fundable now at sensible terms, with clear use of funds?"*

**Status:** 🟢 Authored v0.1.0. UK (GBP) benchmarks live. US benchmarks and region-conditional scoring are a v0.2 workstream.

---

## Why this dimension exists

Even a strong company can have an un-fundable round. Excessive valuations, unclear use of funds, weak cap table structure, or mismatched runway can all block an otherwise solid raise. This dimension assesses the structural fundability of the current round and the coherence of the plan to get to the next one.

---

## What this dimension assesses

1. **Round instrument** — SAFE, convertible note, bridge note, or priced equity; determines which subsequent questions appear
2. **Round size** — whether the raise is large enough to reach the milestones that justify a follow-on
3. **Pre-money valuation** — calibrated against UK stage norms; both under- and over-valuation score below the peak range
4. **Runway** — months of operational capacity funded by the raise
5. **Capital deployment plan** — the prose anchor; assesses whether the deployment plan connects to specific, named milestones and a clear bridge to the next raise
6. **Funding commitment** — percentage of the round already committed or soft-circled
7. **Cap table health** — structural clarity for the close process
8. **Next round path** — specificity of the milestone trigger for the following raise
9. **Prior funding history** — informational context for valuation and cap table structure
10. **Convertible terms** — cap, discount, MFN, and dilution arithmetic (shown only when q8.1 is SAFE/convertible/bridge)
11. **Cap table / term sheet upload** — optional; supports independent verification
12. **Valuation comparables** — optional; named comparable transactions to support the valuation
13. **Investor targeting** — optional; specificity of fit hypothesis for the investor list

---

## Question structure

### Required tier (5 questions)

| ID    | Type            | Weight | Signal |
|-------|-----------------|--------|--------|
| q8.1  | single-select   | 0.02   | Instrument type (informational; gates q8.10) |
| q8.2  | number (£k)     | 0.18   | Round size vs stage benchmarks |
| q8.3  | number (£m)     | 0.15   | Pre-money valuation vs stage benchmarks (non-monotonic) |
| q8.4  | number (months) | 0.13   | Runway months |
| q8.5  | long-text       | 0.22   | Capital deployment plan quality (prose anchor) |

### Recommended tier (5 questions)

| ID     | Type          | Weight | Signal |
|--------|---------------|--------|--------|
| q8.6   | number (%)    | 0.10   | Funding commitment percentage |
| q8.7   | single-select | 0.07   | Cap table structure category |
| q8.8   | long-text     | 0.09   | Next round milestone trigger and round sizing logic |
| q8.9   | single-select | 0.02   | Prior funding history (informational) |
| q8.10  | long-text     | 0.08   | Convertible terms and dilution arithmetic (showIf: q8.1) |

### Optional deep-dive (3 questions)

| ID     | Type        | Weight | Signal |
|--------|-------------|--------|--------|
| q8.11  | file-upload | 0.00   | Cap table / term sheet upload (informational) |
| q8.12  | long-text   | 0.04   | Valuation comparables |
| q8.13  | long-text   | 0.03   | Investor targeting specificity |

**Total scored weight: 1.13**

---

## Scoring notes

### Pre-money valuation: non-monotonic curve

The q8.3 scoring curve does not increase monotonically. Both very-low and excessive valuations score below the peak range:

| Pre-seed band (£m) | Score | Reason |
|--------------------|-------|--------|
| ≤ 1.49             | 40    | Over-dilution risk at close |
| 1.5 – 3.4          | 65    | Below-optimal but achievable |
| 3.5 – 7.0          | 82    | Peak range for UK institutional pre-seed |
| 7.01 – 10.0        | 70    | Boundary high — requires justification |
| 10.01 – 15.0       | 55    | High — creates milestone gap to next raise |
| > 15.0             | 30    | Excessive — materially above stage norms |

Entering 0 (uncapped SAFE) maps to the ≤ 1.49 band.

### Capital deployment plan: highest-weight question

q8.5 carries 0.22 weight — the largest single weight in the dimension. The AI rubric evaluates three criteria:
- **Milestone specificity** (40%) — are investment areas tied to named, evaluable milestones?
- **Bridge to next raise** (35%) — does the plan describe the state the business will be in at runway end in terms that justify the next round?
- **Capital efficiency logic** (25%) — is the spend plan proportional to the milestones it is supposed to fund?

### showIf gate on q8.10

q8.10 (convertible terms) is only shown when q8.1 is answered as `safe`, `convertible-note`, or `bridge-note`. When hidden, the scoring engine applies a penalty for the unanswered recommended question (P7 showIf-penalty bug — known, not resolved in this release).

---

## Benchmark coverage

| Region | Currency | Status |
|--------|----------|--------|
| UK     | GBP      | ✅ Live — `benchmarks/uk.yaml` |
| US     | USD      | 🔲 v0.2 workstream |
| EU     | EUR      | 🔲 v0.2 workstream |

UK benchmarks are calibrated against NIRE's review of UK pre-seed/seed deal data (2023–2025). Source citations will be added in v0.2 once third-party data licences are confirmed.

---

## COMING_SOON gate

D8 is behind `COMING_SOON_DIMENSION_IDS` in `src/lib/constants.ts`. It is filtered from the assessment form and listed in the "Available in v0.2" section of the report until the P1 verbose report cap ships. To release D8:

1. Remove `"round-capital"` from `COMING_SOON_DIMENSION_IDS` in `src/lib/constants.ts`
2. Remove `"Round & Capital Strategy"` from `COMING_SOON_DIMENSION_LABELS` in the same file

Both constants are in the same file — one removal step releases D8 from the form; the other removes it from the report's coming-soon chips.
