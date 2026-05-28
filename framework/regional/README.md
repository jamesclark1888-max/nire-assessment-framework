# Regional adaptation files

This directory contains region-specific configuration that overlays the universal framework.

Each regional file describes ecosystem context, programmes, accelerators, and country-specific notes that inform recommendations. Regional regulatory questions live with their dimensions (e.g. q1.uk1) rather than here.

---

## Files

| File | Region | Tier | Status |
|------|--------|------|--------|
| `uk.yaml` | United Kingdom | 1 | 🟡 Skeleton |
| `france.yaml` | France | 2 | 🟡 Skeleton |
| `germany.yaml` | Germany | 2 | 🟡 Skeleton |
| `netherlands.yaml` | Netherlands | 2 | 🟡 Skeleton |
| `nordics.yaml` | Nordics (SE/NO/FI/DK) | 2 | 🟡 Skeleton |
| `_generic-eu.yaml` | EU fallback | 3 | 🟡 Skeleton |

Ireland (`ie.yaml`) to be added; falls back to UK benchmarks for now.

---

## What each file contains

- Ecosystem context (notable accelerators, government programmes, tax schemes)
- Reference points used in recommendations
- Region-specific guidance templates
- Sources for benchmarks

The regulatory question definitions (e.g. EMI for UK, BSPCE for France) live in the dimension files alongside their universal counterparts. This separation keeps the structured data co-located by topic.
