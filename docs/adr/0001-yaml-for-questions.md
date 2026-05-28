# ADR 0001: YAML for structured framework data

**Status:** Accepted
**Date:** 2026-05-28
**Decision-maker:** NIRE HQ LIMITED

---

## Context

The NIRE Assessment Framework needs a structured data format for its question bank, scoring rules, benchmarks, archetypes, and recommendation templates. The format must be:

1. **Human-readable**: editable by the maintainer team without specialist tooling
2. **Machine-readable**: consumable by the founder-side and VC-side applications
3. **Validatable**: enforceable schemas so malformed data cannot enter the repository
4. **Diff-friendly**: changes must be reviewable in pull requests
5. **Mature and ubiquitous**: supported by every language and tool the team uses

We considered three primary options: JSON, YAML, and TOML.

---

## Decision

We use **YAML** as the structured data format for all framework files, validated against **JSON Schema** definitions.

---

## Options considered

### Option 1: JSON

**Pros:**
- Native to JavaScript / TypeScript (the application stack)
- Universally supported
- No ambiguity in spec

**Cons:**
- No comments support (significant downside for question files where the "why" matters)
- Verbose with quotes everywhere
- Less readable for nested data with long strings
- Harder for non-technical contributors to edit

### Option 2: YAML

**Pros:**
- Supports comments (critical for documenting why a question exists)
- Cleaner syntax for nested data and multi-line strings
- More natural for human writers and reviewers
- Well supported in all languages
- JSON Schema can validate YAML

**Cons:**
- Whitespace-sensitive (occasional gotchas)
- More implementation variability than JSON
- Requires care with special characters

### Option 3: TOML

**Pros:**
- Clearer than YAML for flat configuration
- Less whitespace ambiguity than YAML

**Cons:**
- Less elegant for deeply nested data (which we have)
- Smaller ecosystem
- Less natural for the question-and-options structure

---

## Why YAML

The defining factor is **the importance of comments and readability for question files**. Questions evolve based on VC feedback. The rationale for why a question exists, why it's worded a certain way, and why it scores how it does is critical context that must live alongside the question itself.

JSON's lack of comments forces this context into separate documentation, which inevitably drifts. YAML keeps the rationale inline.

For the validation layer, JSON Schema is mature, well-tooled, and works against YAML via parsing. This gives us schema enforcement (the JSON ecosystem) with human-readable files (YAML).

---

## Consequences

### Positive

- Maintainers can leave comments explaining decisions
- Pull request diffs are easier to review
- Non-engineers (advisors, future product hires) can edit with minimal training
- The structure is enforceable via CI

### Negative

- We must enforce a consistent style (two-space indentation, lowercase-hyphen keys) to prevent the variability YAML allows
- Whitespace errors will occasionally bite us in PRs
- Special characters (colons, quotes inside strings) require care

### Mitigations

- A linter is included in `tooling/validate.py` that runs in CI on every PR
- A style guide is documented in `CONTRIBUTING.md`
- PR template requires confirmation that local validation passed

---

## Revisit

This decision should be revisited if:

- The application team experiences significant runtime issues with YAML parsing
- We find ourselves needing structural features YAML doesn't support cleanly
- An emerging format (e.g. KDL) offers materially better trade-offs

For now, YAML + JSON Schema is the right balance.
