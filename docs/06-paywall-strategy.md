# 06. Paywall strategy

This document describes what's free, what's paid, and the conversion logic on both sides of the NIRE marketplace.

---

## Two-sided pricing

NIRE charges on both sides, but for different reasons:

- **Founder side**: pays for the **report**. One-time or subscription model. Value is the depth of feedback and discoverability.
- **VC side**: pays for the **dataset and tools**. Subscription model. Value is the standardised, comparable view of founder opportunities.

The two sides reinforce each other. More founders means more value to VCs. More VCs means more upside (visibility, intros, signal) to founders.

---

## Founder side: what's free

A founder who completes the questionnaire gets, for free:

- Their overall NIRE score (0-100) with confidence rating
- Their score breakdown across the 8 dimensions (numeric scores only)
- Their top 3 strengths (one-line summaries)
- Their top 3 gaps (one-line summaries, no detailed recommendations)
- A "preview" of one full recommendation, with the rest blurred/locked
- The ability to retake the assessment
- Anonymous benchmarking ("you score higher than X% of UK seed SaaS founders")

This is enough to be genuinely useful and to demonstrate the quality of the analysis. It is not enough to act on without paying.

---

## Founder side: what's paid

The full report unlocks:

- **All recommendations** with specific gap analysis and fix-it guidance
- **Archetype breakdown**: how each VC type would view them, and which to target
- **Detailed dimension reports**: question-level scoring and rationale
- **Downloadable PDF report** (for sharing with advisors, co-founders, mentors)
- **Discoverability** on the VC side of the marketplace (with consent)
- **Tracked improvement**: re-take and compare to previous version
- **Action plan**: a prioritised checklist with target completion dates
- **Email digest**: periodic check-ins on progress

---

## Founder pricing model (under design)

Three options under consideration. To be decided based on early customer development.

### Option A: One-time report purchase

- £49 / €59 / $59 per full report
- Includes 6 months of discoverability
- Discount for re-takes ("compare your improvement")

Pros: low friction, simple, no churn management.
Cons: low LTV, no recurring revenue.

### Option B: Subscription

- £19/month or £149/year
- Unlimited re-takes
- Ongoing discoverability
- Action plan tracking
- Quarterly check-ins

Pros: recurring revenue, deeper engagement.
Cons: harder conversion, churn risk.

### Option C: Hybrid

- One-time report (£49) gets the full unlock and 3 months of discoverability
- Optional upgrade to subscription (£15/month) extends discoverability and adds tracking

Pros: best of both. Lower entry, optional commitment.
Cons: more complex pricing page.

**Working hypothesis: Option C.** To be tested with the first 100 founders.

---

## VC side: what's free (explorer tier)

A VC can sign up for free and see:

- Anonymised aggregate insights about the founder pool
- Sector and region breakdowns
- High-level benchmark data
- The ability to set up a profile (which improves matching when they upgrade)

This is the "see what's possible" tier. No individual profiles.

---

## VC side: paid tiers

### Standard (£X/month - TBC)

- Anonymised individual founder profiles
- Filtering by stage, sector, region, score range, archetype fit
- Saved searches
- Express interest in specific founders (anonymous to founder until they choose to reveal)
- Up to 3 user seats per fund

### Premium (£X/month - TBC)

- Full founder profiles (where consent granted)
- Direct contact details (where consent granted)
- Custom archetype calibration (their fund's specific thesis weighted in)
- Saved searches with email alerts
- Unlimited user seats
- API access for CRM integration

### Enterprise (custom pricing)

- All Premium features
- Dedicated success manager
- Onboarding for fund partners
- Custom data exports
- Service-level agreement
- White-label or co-branded options
- Integration with the VC's portfolio management tools (including NIRE's own Portfolio Tracker)

---

## Conversion logic

### On the founder side

**Trigger points where we present the upgrade:**

1. **End of questionnaire**: "Your free score is ready. Unlock your full report and recommendations for £49."
2. **Score reveal**: "You scored 73/100. To see exactly what's holding you back and how to fix it, unlock the full report."
3. **Recommendation preview**: One full recommendation is shown, the rest are blurred. CTA to unlock.
4. **Re-take attempt**: Free users can re-take but only see their updated free score; paid users see updated full report.

### On the VC side

**Trigger points:**

1. **Search returning results**: free tier sees anonymised count; CTA to upgrade to see profiles.
2. **Profile click on standard tier**: sees anonymised version; CTA to upgrade for contact info.
3. **Saved search alerts**: free tier has limited alerts per month; CTA to upgrade for unlimited.

---

## Payment infrastructure

- **Stripe** for card payments and subscriptions on both sides
- **Stripe Tax** for automated VAT/sales tax handling
- **Webhooks** drive entitlements: subscription status changes immediately update what users see
- **GoCardless** considered for VC enterprise tier (direct debit for larger payments)

---

## Refund and trial policy (working draft)

### Founder side

- 14-day money-back guarantee on the first report purchase
- No refund on subsequent purchases (clear messaging that re-takes are free with subscription)

### VC side

- 14-day free trial on Standard tier
- Quarterly billing option for Premium tier
- Annual contracts available with discount for Enterprise

---

## What's not for sale

To keep the trust intact on both sides:

- **Founder data is never sold to third parties.** VCs access via subscription, not bulk purchase.
- **Rankings are not sold.** Founders cannot pay to score higher.
- **Visibility is consent-driven**, not pay-driven. A paying founder is not automatically more visible than a free founder who has opted in to discoverability.
- **Archetype scoring is not for sale.** VCs can calibrate their own archetype but cannot influence other archetypes' scoring of founders.

These boundaries protect the integrity that makes the product trustworthy.
