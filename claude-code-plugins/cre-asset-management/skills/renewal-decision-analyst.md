---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Renewal Decision Analyst

Run the per-lease retain-vs-replace economic comparison on every expiring multifamily lease and produce defensible, unit-level renewal recommendations.

---

## When to Use This Skill

Use this skill when a property has a rolling pipeline of expiring leases and the asset manager, revenue manager, or on-site leader must decide — resident by resident — what renewal rent to offer, how aggressive to price the bump, and when to accept the turn instead. The skill is the right entry point for:

- Monthly / quarterly renewal-batch reviews (the expiring-lease pipeline for the next 60–90 days)
- Overriding or stress-testing output from an algorithmic pricing engine (RealPage AIRM / LRO, Yardi RevenueIQ) before offers go out
- Softening-market environments where new-lease trade-out has gone negative and retention economics dominate
- Mid-hold asset reviews where loss-to-lease gap is widening and the operator is debating a stepped rent-correction plan
- Tenant-tier triage where some residents carry delinquency, lease-violation, or short-tenure flags and cannot be processed through a pure-financial renewal model

It is **not** the right skill for property-level absorption / lease-up underwriting (separate scope) or for value-add renovation capex decisions that are treated as a standalone program.

---

## What You'll Need to Provide

- **Rent roll with lease expirations** — per-unit, with current in-place rent, concessions remaining, lease-start date, and expiration date (at minimum for the 60–90 day forward window)
- **Market rent comps** — current achievable market rent per unit type at the subject property (comp-set averaged; as-of today, not as-of lease-signing) and most recent new-lease trade-out (achieved new-lease rent vs. prior in-place rent for the same or comparable unit)
- **Current concession policy** — standard renewal concession structure (if any), new-lease concession structure, and any loss-leader / retention-bonus programs currently in force
- **Unit-turn capex estimate** — operator's actual cost-per-turn benchmark for the property (or property class + submarket if not available; pack defaults will apply — see Section 2 of `knowledge/renewal-economics.md`)
- **Property class and submarket** — Class A / B / C, urban / suburban / tertiary, gateway-metro flag, vintage (pre-1990 flag), Tier 1 cost-of-living flag — to calibrate turn-capex, days-vacant, and leasing-cost defaults
- **Tenant-tier inputs (optional but strongly preferred)** — pay history, delinquency flags (per taxonomy seed §5 A/R aging), tenure, maintenance-ticket volume, lease-violation events

If any of the above is unavailable, the skill should apply pack defaults and explicitly flag the assumption — never silently fill from priors.

---

## Mission

Produce an auditable, unit-level renewal recommendation for every expiring lease in the forward pipeline by running the canonical Retain-vs-Replace cost comparison, applying rent-bump elasticity constraints, respecting tenant-tier treatment rules, and aggregating into a property-level renewal strategy that closes loss-to-lease without cratering retention.

---

## Strategy

### Step 1: Build the Expiring-Lease Pipeline

For each lease expiring in the forward window:

- Pull unit number, unit type, current in-place rent, concession remaining, lease-start and lease-end dates
- Compute current effective rent per the taxonomy seed rent-definition table (face rent minus amortized concession)
- Attach current market rent for the comparable unit type
- Compute loss-to-lease per unit: `LTL % = (Market Rent − In-Place Rent) / Market Rent × 100`
- Attach tenant-tier classification (A / B / C / D per renewal-economics.md §4) using pay history, tenure, delinquency, and violation flags

### Step 2: Classify Each Expiring Lease by Tenant Tier

Apply tier rules before running the financial model. Do not run the pure-financial model on Tier D residents (forward-default probability distorts the expected-value math). Flag Tier C residents for **contingent renewal** (balance cure required). Flag short-tenure renewals (resident on month <12 of first lease) for operator review regardless of tier.

### Step 3: Compute Retention Cost (per unit, per decision cycle)

```
Retention Cost = Renewal Concession $ (if any)
              + (Market Rent − Renewal Rent) × 12
              + ~$25 administrative cost
```

The `(Market Rent − Renewal Rent) × 12` term is the opportunity cost of renewing below market. If the renewal rent equals or exceeds market rent, this term is zero or negative (a retention *benefit*). [R4]

### Step 4: Compute Turnover Cost (per unit, per turn event)

```
Turn Cost = Unit-Turn CapEx
         + Downtime Rent Loss (Days Vacant × Monthly Rent / 30)
         + Leasing Cost Per New Lease
         + New-Lease Concession (annualized)
         − (New-Lease Rent − Current In-Place Rent) × 12    [replacement-lease rent pickup]
```

The final subtraction is the replacement-lease rent pickup — in tight markets this can be positive and materially offsets turn cost; in softening markets (Sun Belt 2024–2025) it is typically zero or negative, which amplifies the case for renewal. [R4]

### Step 5: Apply Pack Default Benchmarks When Operator Data Is Missing

| Class | Unit-Turn CapEx | Days Vacant | Leasing Cost |
|---|---|---|---|
| Class A urban/primary | $3,000 | 15 | $1,000 |
| Class B suburban/primary | $2,200 | 25 | $700 |
| Class C / tertiary | $1,500 | 35 | $500 |

Apply the Tier 1 cost-of-living multiplier (1.30x–1.70x for NYC, SF, Boston, DC, LA) to unit-turn capex and the pre-1990 vintage multiplier (1.10x–1.25x) where applicable. Add 5–15 days to the Days Vacant estimate for winter turns (Dec–Feb). [R4]

### Step 6: Recommend a Renewal Rent Level Within the Elasticity Band

Set the recommended renewal rent so that:

1. `Retention Cost < Turn Cost` (the unit-level renewal-favored rule), AND
2. The rent-bump percentage stays within an acceptable elasticity band — specifically: the **+5 to +7% band is the inflection point** where shopping behavior activates (renewal rate falls roughly 2–3 percentage points per additional 1% of rent bump), and **+10%+ craters retention** (renewal rate drops into the 15–25% range). [R4]
3. The recommended bump does **not** exceed the achievable new-lease trade-out on a comparable unit (floor rule — offering more than the replacement lease can achieve invites the resident to shop and confirm they can do better elsewhere).
4. The loss-to-lease gap supports the proposed bump (a resident at 12% below market tolerates a larger increase than one at 2% below market, because their outside option is worse).

Apply seasonal modifier: reduce recommended bump by 100–150 bps for Nov–Feb expirations; add 100 bps for May–Aug expirations where LTL gap supports.

### Step 7: Compute Expected-Value Retain vs. Turn

For each candidate renewal rent, weight the Retention Cost by expected renewal probability (from the elasticity table) and compare to Turn Cost × (1 − renewal probability) + Retention Cost × renewal probability. The recommended offer is the one minimizing expected total cost.

### Step 8: Aggregate to Property-Level Renewal Strategy

Roll up per-unit recommendations to:

- Total expected retention count (and rate)
- Total projected retention cost
- Total projected turn cost (on declined / non-offered leases)
- Forward LTL-gap closure estimate (renewals close ~50–60% of the gap; new leases on turned units close the full gap)
- Aggregate rent-roll impact on a 12-month forward basis

### Step 9: Flag Edge Cases for Operator Review

- Long-tenure resident (4+ years) at large LTL gap (15%+): anchored-renewal problem — flag stepped 2-cycle correction option vs. one-time upgrade-concession vs. accept-the-turn
- Unit scheduled for value-add renovation at next move-out: Turn Cost is only *incremental* make-ready over renovation cost — branch to separate treatment
- Winter expiration with non-negotiable timing (relocation): retention lever collapses to zero; recommend minimizing turn cost, not pushing rent
- Voucher / Section 8 resident: exclude from pure-financial framework (PHA-set payment standard, not negotiated)
- Resident with unresolved delinquency: contingent renewal only, not unconditional
- Compressed-spread peak market (new-lease > renewal growth): rare — operator may rationally push renewals; requires confirming new-lease trade-out data

---

## Output Format

```markdown
# Renewal Decision Analysis
## Property:
## Analysis Date:
## Forward Window:
## Status: COMPLETE | PARTIAL | FAILED

### Expiring-Lease Pipeline
- Total Expiring Leases:
- Class / Submarket:
- Current Average In-Place Rent:
- Current Average Market Rent:
- Property LTL Gap:
- Tenant-Tier Distribution (A / B / C / D):

### Per-Tenant Renewal Recommendation Table

| Unit | Tier | In-Place Rent | Market Rent | LTL % | Recommended Renewal Rent | Bump % | Expected Renewal Prob. | Retention Cost | Turn Cost | Delta (Turn − Retain) | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 101 | A | ... | ... | ... | ... | +X% | ~Y% | $ | $ | $ | RENEW / TURN / CONTINGENT |

### Aggregate Renewal Strategy
- Recommended Renewal Offers: X of Y expiring leases
- Expected Retention Rate: ~Z%
- Expected Turnover Count: N units
- Aggregate Projected Retention Cost:
- Aggregate Projected Turn Cost (on declined/non-offered):
- Forward 12-Month LTL-Gap Closure Estimate:
- Blended Rent-Roll Change (%):

### Retention-Cost vs Turnover-Cost Summary
- Average Retention Cost per Retained Unit:
- Average Turn Cost per Turned Unit:
- Portfolio-Weighted Retain-vs-Turn Delta:
- Highest-Value Retentions (top 5 units by delta):
- Accept-the-Turn Decisions (units where Turn Cost < Retention Cost or tenant tier triggers decline):

### Seasonal / Elasticity Considerations
- Peak-Season Expirations (May–Aug):
- Off-Season Expirations (Nov–Feb):
- Units in +5–7% Elasticity Band (inflection zone):
- Units in +10%+ Zone (retention-crater risk):

### Edge Cases Flagged
- Long-tenure + large LTL:
- Scheduled value-add renovation:
- Voucher / Section 8:
- Short-tenure first-lease:
- Delinquent / contingent:
- Winter-locked timing:

### Key Risks
- ...

### Verdict
PUSH RENEWALS | BALANCED | ACCEPT TURNS

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Worked Example (Class B Suburban, Softening Market)

Illustrative single-unit calculation, numbers cited to R4 benchmarks.

**Inputs:**
- Unit 204, 1BR, Class B suburban Sun Belt, built 2006 (no vintage penalty)
- In-place rent: $1,800/mo
- Current market rent: $1,850/mo (LTL gap = 2.7%)
- Achievable new-lease rent on comparable unit: $1,800/mo (new-lease trade-out of -3% vs. prior lease, consistent with FY 2024 MAA/CPT Sun Belt disclosures) [R4]
- Unit-turn capex: $2,200 (Class B pack default) [R4]
- Days vacant: 28 (slightly above Class B pack default of 25, reflecting Sun Belt competitive pressure) [R4]
- Leasing cost: $700 (Class B Sun Belt pack default) [R4]
- No renewal concession, no new-lease concession
- Tenant Tier B (on-time pay, 18 months in place, low maintenance volume)

**Retention Cost at proposed renewal rent $1,854 (+3%):**

```
Retention Cost = $0 (no concession)
              + ($1,850 − $1,854) × 12
              + $25
            = $0 + (−$48) + $25
            = −$23 (effectively zero — renewal rent is at/slightly above market)
```

**Turn Cost:**

```
Downtime rent loss = 28 × ($1,800 / 30) = $1,680

Turn Cost = $2,200 (unit-turn capex)
         + $1,680 (downtime)
         + $700 (leasing cost)
         + $0 (no new-lease concession assumed)
         − ($1,800 − $1,800) × 12  [replacement-lease rent pickup is zero in this softening scenario]
         = $4,580
```

**Delta = Turn Cost − Retention Cost = $4,580 − (−$23) = $4,603 in favor of renewal.**

Even at a +3% renewal bump, renewal dominates turn by ~$4,600. [R4]

**Stress test — what if operator pushes renewal to +8% ($1,944)?**

- Per the elasticity curve, renewal rate drops from ~55% baseline (at +3%) to ~35% (at +8%) — a 20 pp reduction. [R4]
- Incremental rent captured if resident renews: (8% − 3%) × $1,800 × 12 × 55% retained probability = **$594 in higher rent retained**
- Forgone value from 20 pp higher turn probability: 20% × $4,580 avoided turn cost = **$916 in expected turn cost incurred**
- **Net: pushing to +8% destroys ~$322 of expected value vs. the +3% offer.**

The +3% renewal is the right recommendation on this unit. The skill would offer renewal at $1,854 (+3%), flag this as a Tier B priority-retain decision, and document that pushing above +3% tips into the elasticity band where expected-value math inverts. This is the canonical shape of most Sun-Belt Class B renewal decisions in a softening 2024–2026 environment.

---

## Quality Checks

- **Retention Cost < Turnover Cost → recommend renew.** The core decision rule. Any recommended decline where Retention Cost < Turn Cost must be justified by tenant tier (Tier C/D) or edge-case flag, not by generic pricing preference.
- **Recommended renewal bump ≤ achievable new-lease trade-out on comparable unit.** Floor rule. Violation invites the resident to shop and confirm a better outside option.
- **Recommended bump stays out of the +10%+ retention-crater zone unless LTL gap is very large AND confirmed by market comps.** Above +10%, expected renewal rate drops to 15–25% — math only works for residents with a 12%+ LTL gap.
- **Seasonal modifier applied.** Nov–Feb expirations reduce recommended bump by 100–150 bps; May–Aug expirations add 100 bps where LTL supports. Absent this adjustment, winter turns materially under-price retention.
- **Tenant tier applied before financial model.** Tier D residents never enter the pure-financial model. Tier C residents receive contingent renewal. Short-tenure residents flagged regardless of tier.
- **Replacement-lease rent pickup modeled explicitly.** The `− (New-Lease Rent − Current Rent) × 12` term must appear in every Turn Cost computation — omitting it understates the case for turning in tight markets and is a common modeling error.
- **Pack defaults flagged when used.** Any field defaulted from the pack benchmark table (turn capex, days vacant, leasing cost) must be explicitly tagged in the per-unit output, not silently applied.

---

## Red Flags & Dealbreakers

- **Property-wide renewal rate projected below 45%** under the recommended strategy: either pricing is too aggressive, offer timing is late, or the resident satisfaction base is weak. Do not release the recommendation set without operator review.
- **Recommended renewal bump exceeds confirmed new-lease trade-out by more than 200 bps on any unit**: floor-rule violation. The resident is being offered a rent they could demonstrably beat elsewhere. Bump must be reduced or the unit reclassified as accept-the-turn.
- **Aggregate turn cost exceeds the property's quarterly operating budget for turnover**: the recommended set cannot be physically executed (make-ready capacity, leasing-agent bandwidth). Force a staggered / batched recommendation.
- **Any Tier D resident routed through the pure-financial model**: forward-default probability invalidates the expected-value calculation. Reject and re-route through the decline / conditional-renewal branch.
- **Loss-to-lease gap at property > 12% with recommendations that leave the gap unchanged after the cycle**: the renewal program is anchoring LTL, not closing it. Institutional best practice is to set renewal rent at the midpoint between in-place and market — not at in-place.

---

## When Data is Missing

- **Market rent comps unavailable or stale** (>90 days): apply submarket ask-rent average from the most recent Yardi Matrix / ALN / Costar pull; flag confidence as LOW on every unit and recommend a pre-release comp-set refresh before offers go out.
- **Operator unit-turn capex benchmark not provided**: fall back to pack defaults by class ($3,000 / $2,200 / $1,500 midpoint), apply Tier 1 multiplier if applicable, flag the assumption in the per-unit output. Confidence MEDIUM at best on those units.
- **Tenant-tier data (pay history, delinquency) incomplete**: classify as Tier B by default (standard renew) and flag for operator verification; do not escalate to Tier A treatment without confirmed on-time pay and tenure data.
- **New-lease trade-out data not available**: default to the REIT-peer-group indicative ranges by submarket (Sun Belt −3 to −5%, coastal +1 to +3%) per R4, flag the assumption, and recommend that the operator provide actual property-level trade-out before the final offer set is released.
- **Concession policy undefined**: assume zero concession on both renewal and new lease; flag. If actual concession activity is material at the property, the math is materially understated on the Turn Cost side.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Rent roll complete with tenant-tier data, current market comps (<30 days), operator-provided turn capex, recent new-lease trade-out data for the property, concession policy documented |
| MEDIUM | Rent roll complete, market comps 30–90 days old OR operator turn capex missing (pack defaults applied), tenant tier partially populated |
| LOW | Rent roll incomplete or stale, market comps >90 days, no new-lease trade-out data, no tenant tier flags, pack defaults applied across multiple inputs |

---

## Related Knowledge Bases

- [Renewal Economics](../knowledge/renewal-economics.md) — primary framework source; Retain-vs-Replace formula, rent-bump elasticity curve, tenant tier definitions, turnover cost components, seasonality modifiers
- [Asset Management Benchmarks](../knowledge/asset-management-benchmarks.md) — cross-reference for property-level retention/renewal-rate targets and turnover benchmarks
- [Multifamily Benchmarks](../knowledge/multifamily-benchmarks.md) — cost-of-living / vintage / catastrophe multipliers applied to turn capex; class-based turnover benchmarks
- [Underwriting Calculations](../knowledge/underwriting-calc.md) — canonical Loss-to-Lease, Effective Rent, and Concession formulas (cross-reference only; not redefined here)

---

## Structured Output

```json
{
  "skill": "renewal-decision-analyst",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "expiring_leases_count": 0,
    "per_tenant_recommendations": [],
    "retention_cost_total": 0,
    "turnover_cost_total": 0,
    "portfolio_retention_strategy": ""
  },
  "uncertainty_flags": [],
  "red_flags": []
}
```

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
