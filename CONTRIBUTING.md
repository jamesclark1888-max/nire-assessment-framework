# Contributing to the NIRE Assessment Framework

Thank you for your interest in contributing. This document explains how to propose changes and the terms under which contributions are accepted.

---

## Important: IP assignment

**By submitting any contribution to this repository, you irrevocably assign to NIRE HQ LIMITED all right, title, and interest, including all intellectual property rights, in and to your contribution.**

This includes contributions made via:

- Pull requests
- Issue comments containing proposed text, questions, or scoring logic
- Suggestions made through any other channel and later incorporated

You confirm that:

1. Your contribution is your original work, or you have the right to assign it
2. Your contribution does not infringe any third-party rights
3. You are not contributing material under any conflicting licence or agreement

If you cannot agree to these terms, please do not contribute.

For substantial contributions, NIRE HQ LIMITED may require a separate written Contributor Licence Agreement (CLA).

---

## How to propose a change

### For question additions or modifications

1. Open an issue using the **Question Proposal** template
2. Include: the proposed question, why it matters from a VC perspective, where it belongs in the framework, and any supporting evidence
3. Wait for triage and discussion before opening a PR

### For scoring methodology changes

1. Open an issue using the **Scoring Issue** template
2. Include: the current behaviour, the proposed change, the expected impact on scores, and any data supporting the change
3. Scoring changes require documented rationale because they affect founder outcomes

### For regional additions

1. Open an issue describing the region and the regulatory/ecosystem context
2. Include source material for benchmarks and region-specific terminology
3. Regional changes need fluency with the local VC market; please indicate your relevant experience

### For documentation changes

Smaller documentation fixes (typos, clarifications) can go straight to PR.

---

## Pull request process

1. Branch from `main` using the naming convention `type/short-description` (e.g. `question/add-board-composition`, `fix/typo-in-philosophy`)
2. Make your changes
3. Run validation locally: `python tooling/validate.py`
4. Update [`CHANGELOG.md`](CHANGELOG.md) under the `[Unreleased]` section
5. Open a PR using the provided template
6. CI must pass (schema validation)
7. At least one approving review from a maintainer

---

## Style guide

### YAML files

- Two-space indentation
- Lowercase keys with hyphens (`founder-market-fit` not `founderMarketFit` or `founder_market_fit`)
- IDs follow the pattern `q{dimension}.{number}` (e.g. `q1.5`) for core questions and `q{dimension}.{region}{number}` for regional additions (e.g. `q1.uk1`)
- Always include a `why-it-matters` field explaining the VC perspective

### Markdown files

- UK English spelling and conventions
- Sentence-case headings (not Title Case)
- Avoid em dashes; use commas, colons, or parentheses

### Question writing principles

- Ask for evidence, not opinion
- One question per question (no compound questions)
- Provide helper text for ambiguous terms
- State clearly what the question is trying to surface

---

## Versioning

This framework uses Semantic Versioning (semver):

- **MAJOR** (e.g. 1.0.0 → 2.0.0): breaking changes to question structure, IDs, or scoring that would invalidate previous results
- **MINOR** (e.g. 1.0.0 → 1.1.0): new questions, new regions, new archetypes, additive changes
- **PATCH** (e.g. 1.0.0 → 1.0.1): typo fixes, clarifications, non-functional changes

See [`CHANGELOG.md`](CHANGELOG.md) for version history.

---

## Questions

For anything not covered here, open a Discussion on GitHub or contact the maintainer team.
