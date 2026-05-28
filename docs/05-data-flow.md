# 05. Data flow

This document describes how data flows from the founder questionnaire to the VC-side dashboard, including security, privacy, and access control.

---

## High-level flow

```
[Founder fills questionnaire]
       │
       ▼
[Answers stored, encrypted at rest]
       │
       ▼
[Scoring engine processes answers]
       │
       ▼
[Recommendation engine generates founder-facing report]
       │
       ▼
[Free tier: partial report shown in-app]
       │
       ▼
[Founder pays for full report → unlocks paid features]
       │
       ▼
[With consent: founder profile becomes discoverable to VCs]
       │
       ▼
[VC-side dashboard: tiered access based on VC plan]
```

---

## Founder consent model

A founder fills the questionnaire and receives their report. **Nothing is shared with VCs unless the founder explicitly consents.**

Consent is granular:

- **Anonymous aggregate**: founder data contributes to NIRE benchmarks (anonymised). Default opt-in.
- **Anonymous profile visibility**: VCs see a profile with no identifying info (no company name, no founder names, no URLs). Default opt-out.
- **Full profile visibility**: VCs see the founder's full profile and can initiate contact. Default opt-out.
- **Selective disclosure**: founder can choose specific VCs (or VC archetypes) to be visible to.

Consent is logged with timestamps and can be revoked at any time. Revocation removes future visibility but does not affect data that was viewed before revocation (which we cannot retract).

---

## Data tiering on the VC side

VCs see different levels of detail based on their plan:

### Free / explorer tier

- Anonymised aggregate insights ("there are 47 UK seed SaaS founders with strong scores currently active")
- No individual profiles
- No contact information

### Standard tier

- Anonymised individual profiles (NIRE score, archetype fit, key strengths/weaknesses, region, sector, stage)
- Filtering and search
- "Express interest" function (founder is notified anonymously and can choose to reveal themselves)

### Premium tier

- Full profiles (with founder consent)
- Direct contact information (with founder consent)
- Saved searches, alerts, portfolio comparison
- API access for CRM integration

### Enterprise tier

- All Premium features
- Custom archetype profiles calibrated to the fund's thesis
- Dedicated support for adding the fund's specific scoring preferences
- White-label or co-branded options

---

## Data model overview

The detailed data model lives in the Portfolio Tracker codebase (Supabase). At a high level:

### Founder side

- `assessments` (one per founder per major version): metadata, completion status, scores
- `answers` (one per question per assessment): the raw answer, scoring output, timestamps
- `documents` (uploaded supporting materials, encrypted): pitch decks, financials, screenshots
- `consent_grants`: time-stamped consent records linking founders to VCs or VC categories
- `recommendation_logs`: which recommendations were shown, when, and whether the founder marked them complete

### VC side

- `vc_organisations`: fund-level metadata
- `vc_users`: individual users at each fund, with role permissions
- `archetype_assignments`: which archetype(s) each VC user is mapped to
- `viewed_profiles`: audit log of every profile view (for transparency and consent enforcement)
- `expressions_of_interest`: recorded interest from VCs in specific founders

### Shared

- `audit_log`: append-only log of every access event
- `benchmarks`: regional benchmark data
- `framework_version`: which version of the assessment framework was used for each assessment

---

## Security principles

### Encryption

- **At rest**: All sensitive data (founder financial details, uploaded documents, personal information) encrypted using application-level encryption with keys managed in a secure key management system.
- **In transit**: TLS 1.3 minimum for all client-server and service-to-service communication.
- **Document storage**: Uploaded files stored in object storage with server-side encryption and signed-URL access only.

### Access control

- **Founder-side**: A founder can only access their own assessment.
- **VC-side**: Row-level security policies enforce that VCs only see data their plan tier and consent permissions allow.
- **Internal/admin**: Operations staff have role-based access; all access to founder data is logged and auditable.

### Auditability

Every access to a founder profile by a VC is logged with:

- Timestamp
- VC user ID
- Data accessed
- Reason category (e.g. "search result view", "saved search alert", "shared link")

Founders can request a complete log of who has viewed their profile.

### Data minimisation

We collect only what's needed for the assessment. We don't ask for personal identifiers we don't need. Uploaded financial documents are processed for the assessment and the founder can choose to delete them after.

### Right to erasure

Founders can request full deletion of their data at any time. Anonymised aggregate contributions (which cannot be linked back to them) may be retained for benchmark integrity.

---

## Framework versioning and historic assessments

Assessments are stamped with the framework version they were taken under. This matters because:

- A founder's score in v1.2 of the framework is not directly comparable to a score in v2.0
- VCs filtering on score need to know which framework version produced it
- When a founder retakes the assessment, we can show genuine improvement (not improvement caused by the framework changing)

Major framework versions trigger a "we recommend retaking" prompt to founders. Their old assessment is preserved for history; the new one becomes the current view.

---

## Compliance posture

NIRE handles personal data of EU residents and is therefore subject to UK GDPR and EU GDPR. Key commitments:

- Lawful basis for processing: consent (for profile sharing) and legitimate interest (for assessment processing)
- Data Protection Officer responsibilities are assigned within NIRE HQ LIMITED
- DPA in place with all sub-processors (Supabase, Vercel, payment processors, AI providers)
- Data Processing Agreements available to VC customers
- Founder-facing privacy policy is plain-English and version-controlled

Specific certifications (SOC 2, ISO 27001) are part of the post-traction roadmap.

---

## What lives where

To be unambiguous about the boundary:

- **This repository (`nire-assessment-framework`)** contains: the questions, scoring logic, archetypes, regional adaptation, recommendation templates. It does NOT contain founder data.
- **The application repository (Portfolio Tracker codebase)** contains: the runtime, the Supabase schema, the API, the UI. It consumes from this repository.
- **The production Supabase instance** contains: founder data, VC data, consent records, audit logs.

The framework is publishable IP. The data is not.
