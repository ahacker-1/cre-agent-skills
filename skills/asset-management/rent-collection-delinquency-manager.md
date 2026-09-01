---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Rent Collection & Delinquency Manager

Analyze A/R aging on a stabilized conventional multifamily property, classify each delinquent tenant, calculate a defensible bad-debt reserve, and prescribe collection actions calibrated to state eviction law.

---

## When to Use This Skill

Use this skill when you have an as-of-date rent roll with A/R aging columns, a delinquency list, the state in which the property sits, and (where applicable) any payment plans currently in force, and you need:

- a defensible A/R aging analysis with portfolio-health flags,
- a tenant-by-tenant collection-action list that correctly applies the oldest-band rule,
- a bad-debt reserve that ties to aging-band reserve percentages and class overlays, and
- a prioritized list of red flags and escalations for the asset manager and ownership.

This is the right skill at month-end close, on acquisition-diligence T-3 rent-roll review, and whenever portfolio receivables exceed the warning threshold defined below.

This skill does NOT cover: LIHTC / Section 8 / HUD-administrative collections, lease-up-era collections, lease-renewal retention decisions for non-delinquent tenants, or disposition-level write-off treatment — those live in their sister skills.

---

## What You'll Need to Provide

- Rent roll with A/R aging columns (Current / 1–30 / 31–60 / 61–90 / 90+, or the 4-band REIT collapse)
- Delinquency list: tenant name, unit, total balance, balance per aging band, notice status (pay-or-quit served? date?), last-payment date, lease end date
- State of property (drives eviction timeline, notice period, partial-payment waiver rules)
- Payment plans currently in force (signed written plan vs verbal; installment schedule; start date)
- Property class (A coastal / A Sun Belt / B / C / Affordable-unsubsidized / deep-value-add) — drives bad-debt benchmarks and reserve overlay
- Deposit-alternative surety product in use, if any (LeaseLock / Rhino / Jetty) — affects bad-debt-ratio comparability
- Prior-period uncollected lease revenue and GPR — to compute the bad-debt ratio benchmark
- Any pending ERAP applications or residual moratorium-era balances (flag jurisdictions: NY, NJ, DC, IL)

---

## Mission

Produce a state-law-calibrated, institutionally defensible A/R aging analysis that separates billed-but-collectable from bad-debt-likely, classifies each delinquent tenant as short-term / chronic / write-off, prescribes the correct collection action per the taxonomy-seed §5 split-aging rule, computes a bad-debt reserve using the aging × reserve-% × class-overlay methodology, and flags red flags (portfolio-health, legal-risk, compliance) that ownership must act on.

---

## Strategy

### Step 1: Normalize the Aging Schema

Apply taxonomy-seed §5 bands verbatim: **Current / 1–30 / 31–60 / 61–90 / 90+**. If the source data provides only a 4-band schema (Current / 1–30 / 31–60 / 60+), treat the entire 60+ balance at the 90+ reserve rate (40–50%) for conservatism, per the taxonomy-seed operator-variance rule.

Verify total balance per tenant reconciles to rent-roll balance column; flag any reconciling-item >$100.

### Step 2: Compute Portfolio-Level A/R Summary

Report:

- Total A/R balance
- A/R by band (Current / 1–30 / 31–60 / 61–90 / 90+), $ and % of total
- Past-due % of receivables = (Total A/R − Current) / Total A/R
- Bad-debt ratio (trailing) = Uncollected Rent / GPR (per `underwriting-calc.md` and `_taxonomy-seed.md` §2 — DO NOT redefine)
- Class-adjusted benchmark for the ratio using KB1 §7 (A coastal <1.0%, A Sun Belt <1.2%, B <1.5%, C <2.5%, Affordable <3.0%)

### Step 3: Apply the Split-Aging Rule (Mandatory, Per Taxonomy-Seed §5)

For EACH delinquent tenant with balances across multiple bands:

1. Find the **oldest band in which the tenant has a balance of at least $100** (de minimis floor).
2. Apply the decision action for that band to the tenant.
3. Report each band's balance separately in the tenant-level output (never collapse bands into a single column).
4. Continue normal billing on the current-band portion.

Worked example: Tenant with $800 in 31–60 + $500 Current → apply the 31–60 action (manual collections call, notice-to-pay prep) to the tenant; bill the $500 Current normally.

### Step 4: Classify Each Delinquent Tenant (Short-Term / Chronic / Write-Off)

Apply the R3 operational classification rules:

| Classification | Trigger (any one sufficient for Chronic; Write-Off requires at least one) |
|---|---|
| **Short-term** | Single late payment in trailing 12 months, no NSF events, no 60+ aging, and a clear precipitating event (single paycheck gap, one-time medical, etc.). Retain; apply band-level action only. |
| **Chronic delinquent** | (a) 3+ late payments in trailing 12 months, OR (b) 2+ NSF events in trailing 12 months, OR (c) any aging >60 days in trailing 12 months. Do not offer lease renewal at current market rent; non-renew or renew only at market + late-fee escalator + M-to-M premium. Monitor aging weekly. |
| **Write-off recommended** | (a) Eviction completed and unit vacated, OR (b) 90+ past due with no payment plan and no pending ERAP, OR (c) tenant skip / abandonment confirmed per state statutory presumption (e.g., TX, AZ have statutory abandonment triggers — do NOT assume abandonment without the statutory trigger). |

### Step 5: Prescribe Collection Action Per Band

Apply taxonomy-seed §5 decision actions:

| Band | Decision Action |
|---|---|
| Current | Normal billing cycle; no collection action. |
| 1–30 | Automated late notice; late fee per lease. |
| 31–60 | Manual collections call; prepare formal notice-to-pay-or-quit; begin eviction docket in single-action states. Offer signed written payment plan IF no pay-or-quit served yet. |
| 61–90 | AR manager escalation; file eviction; legal notice; cease lease-renewal offers. |
| 90+ | Executive review; write off to bad debt upon completion of eviction / judgment; refer to collections agency (if vacated, balance ≥$500, 30+ days post-move-out, no payment plan). |

### Step 6: Overlay State Eviction Timeline (R3 §Benchmark and Formula Decisions)

Apply the state of the property to the eviction-timeline reference table below to estimate days-from-notice-to-writ, and adjust urgency accordingly. State-level differences are material — not generic:

| State | Notice Period (nonpayment) | Filing → Judgment (uncontested) | Judgment → Writ / Lockout | Total (typical) |
|---|---|---|---|---|
| Georgia | Immediate demand on default (no statutory wait) | 7–14 days | 7 days | **2–4 weeks** (fastest major market) |
| Texas | 3 days (Tex. Prop. Code §24.005) | 10–14 days (JP court, Rule 510) | 5 days | 3–5 weeks |
| Arizona | 5 days (ARS §33-1368) | 3–6 days (special detainer) | 5 days | 2–4 weeks |
| Florida | 3 days excluding weekends/holidays (Fla. Stat. §83.56) | 2–3 weeks | 24 hours – 1 week | 4–6 weeks |
| North Carolina | 10-day demand (Ch. 42 Art. 3) | 2–3 weeks | 10 days | 4–7 weeks |
| Nevada | 7-day pay-or-quit summary (NRS §40.253) | Tenant-response driven (5 days to answer) | 24 hours – 1 week | 3–5 weeks |
| California (post AB 2347) | 3-day pay-or-quit | 30–60 days (10 business-day answer, trial set) | 5–15 days sheriff lockout | **45–90+ days** |
| New York (post-HSTPA) | 14-day demand (RPAPL Art. 7) | 60–120+ days | 14 days + marshal queue | **90–180+ days** |

Three concrete state-level differences with material asset-management implications (R3 §Key Findings):

1. **Georgia vs New York** — a 90+ balance in Georgia can be writ-served and unit re-leased inside 4 weeks; the same balance in New York routinely sits in A/R for 6+ months post-HSTPA even on an uncontested filing. This drives bad-debt reserve at the property level and must be modeled.
2. **California AB 2347 (effective 1/1/2025)** — extended tenant response window to 10 business days from 5 calendar days, adding ~2 weeks to every CA nonpayment case. Nolo state summaries may lag statutory amendments by 6–12 months; where Nolo and statute conflict, **statute wins**.
3. **Partial-payment waiver rules vary by state** — under common-law contract doctrine and many state statutes, accepting a partial payment after serving a pay-or-quit can **waive the eviction and restart the clock**. Texas and Florida are strict; some states tolerate partial payment with documented non-waiver addendum. In ALL states, require a signed non-waiver addendum OR convert to a formal written payment plan before accepting partial payment post-pay-or-quit.

### Step 7: Compute the Bad-Debt Reserve

Reserve = Σ (Band Balance × Band Reserve % × Class Overlay Multiplier)

Pack-default reserve % by band (`_taxonomy-seed.md` §5 + KB1 §2):

| Band | Reserve % (Default) | Reserve % (Conservative) |
|---|---|---|
| Current | 1% | 1% |
| 1–30 | 5–10% | 10% |
| 31–60 | 10–15% | 15% |
| 61–90 | 15–20% | 20% |
| 90+ | 40–50% | 50% |

Class overlay (KB1 §2 multiplier on top of band %):

| Property Class | Overlay | Example (61–90 band at 15–20% default) |
|---|---|---|
| Class A institutional coastal | −25% relative | 11–15% |
| Class B | Pack default | 15–20% |
| Class C | +25% relative | 19–25% |
| Affordable / Workforce | +50% relative | 23–30% |
| Deep-value-add / distressed | +100% relative | Use conservative ceiling (30–40% on 61–90; 80%+ on 90+) |

Apply state eviction-speed adjustment: in slow-track states (CA, NY), increase 61–90 and 90+ band reserves by 5–10 percentage points above the class overlay because the receivable sits longer before writ-eligible write-off, giving collection probability more time to erode.

**Do not additionally reserve on the full GPR** — the aging reserve REPLACES, not supplements, a gross bad-debt accrual. For CECL-reporting entities (ASC 326), flag that pack defaults are a reasonable starting point but the operator must support with its own historical loss experience and forward-looking adjustments; report a placeholder for "CECL overlay" in the output.

### Step 8: Enumerate Red Flags and Recommended Escalations

Scan the analysis for the triggers in the Red Flags section below and surface each as a prioritized action.

---

## Output Format

```markdown
# Rent Collection & Delinquency Report
## Property:
## As-of Date:
## Status: CLEAN | WATCH | PROBLEM
## Confidence: HIGH | MEDIUM | LOW

### A/R Summary
- Total A/R Balance:
- Past-Due % of Receivables:
- Bad-Debt Ratio (Trailing):
- Class Benchmark:
- Surety-Product Adjustment (if any):

### Aging Analysis
| Band | Balance ($) | % of Total A/R | Tenant Count |
|---|---|---|---|
| Current | | | |
| 1–30 | | | |
| 31–60 | | | |
| 61–90 | | | |
| 90+ | | | |

### Tenant-Level Action List
| Unit | Tenant | Classification | Balance by Band | Oldest Band ≥ $100 | Prescribed Action | Notice Status | State Eviction ETA |
|---|---|---|---|---|---|---|---|
| | | Short-Term / Chronic / Write-Off | | | | Pay-or-quit served Y/N, date | |

### Bad Debt Reserve Calculation
| Band | Balance | Reserve % (class-adjusted) | Reserve $ |
|---|---|---|---|
| Current | | | |
| 1–30 | | | |
| 31–60 | | | |
| 61–90 | | | |
| 90+ | | | |
| **Total Reserve** | | | |
| CECL Overlay (placeholder) | | | |

### Chronic Delinquents — Non-Renewal Watchlist
| Unit | Tenant | Lease End | Trailing 12mo Late Count | NSF Count | Recommended Lease-End Action |
|---|---|---|---|---|---|

### Write-Offs Recommended
| Unit | Tenant | 90+ Balance | Status (Vacated / Eviction Complete / Skip) | Collection-Agency Referral (Y/N, reason) |
|---|---|---|---|---|

### Red Flags & Recommended Escalations
- ...

### Verdict
CLEAN (past-due <15% of receivables, bad-debt ratio within class benchmark, no legal-risk flags)
WATCH (past-due 15–25% of receivables OR bad-debt ratio slightly above class benchmark)
PROBLEM (past-due >25% of receivables OR bad-debt ratio >class watch threshold OR any HIGH-severity red flag)
```

---

## Quality Checks

- Every delinquent tenant appears on the Tenant-Level Action List with a classification, prescribed action, and state eviction ETA (no tenant is omitted).
- Split-aging rule was applied: every tenant with multi-band balances has their "Oldest Band ≥ $100" column populated and the action matches the oldest band (not an average or a blended band).
- Bad-debt reserve $ total reconciles band-by-band to `Σ (Band Balance × Reserve % × Class Overlay)` within $1 of rounding; no band is skipped.
- Bad-debt ratio denominator is GPR per `underwriting-calc.md` / `_taxonomy-seed.md` §2 (never face rent × occupancy × 12 — that is a wrong denominator).
- 4-band-to-5-band collapse rule was applied correctly: if source data is only 60+ (not 61–90 + 90+), the 60+ balance carries the 90+ reserve rate (40–50%), not the 61–90 rate.
- Partial-payment exposure was checked: for every tenant with a pay-or-quit served, the report flags whether a partial payment was accepted and whether a non-waiver addendum is on file.
- ERAP residual check: for properties in NY / NJ / DC / IL, 90+ balances are cross-checked against pending ERAP applications BEFORE write-off recommendation.
- State eviction-timeline ETA is based on the property's actual state statute (from the table above), not a generic "4–8 weeks."

---

## Red Flags & Dealbreakers

| Severity | Flag | Threshold / Trigger | Recommended Action |
|---|---|---|---|
| HIGH | Past-due % of receivables exceeds **25%** | Taxonomy-seed §5 portfolio-health threshold (KB1 §2 Warning). | Escalate to ownership; freeze lease renewals for chronic-delinquent cohort; commission root-cause review (screening, market stress, policy gap). |
| HIGH | Bad-debt ratio above class watch threshold | Class A coastal >1.0% / A Sun Belt >1.2% / B >1.5% / C >2.5% / Affordable >3.0% per KB1 §7. | Review screening criteria, site-team discretion logs, and hardship-policy adherence; compare against surety-product-adjusted peer set. |
| HIGH | Partial payment accepted after pay-or-quit served without signed non-waiver addendum | Any occurrence. This is the single most common legal failure in multifamily collections (R3 §Edge Cases). | Counsel review immediately; likely eviction void and clock restart. Institute written site-team protocol prohibiting partial-payment acceptance post-pay-or-quit without counsel-approved addendum. |
| HIGH | 90+ balances in NY / NJ / DC / IL marked for write-off without ERAP clearance | Any 90+ balance in those jurisdictions where a pending ERAP application has not been confirmed absent. | Halt write-off; confirm no in-process ERAP; state-agency verification required. |
| MEDIUM | Chronic-delinquent cohort exceeds **15%** of resident base | R3 §Key Findings: REIT-disclosed chronic rates typically 5–15%. | Build non-renewal pipeline for leases ending in next 90 days; this cohort is often the largest NOI lever in stabilized AM. |
| MEDIUM | Bad-debt ratio is inconsistent with surety-product usage | Property uses 15–40%+ surety adoption but reported bad-debt ratio is at/above non-surety peer benchmark. | Audit surety-claim recovery; the surety is absorbing risk and should be depressing the ratio; non-performance suggests administration gap. |
| MEDIUM | In rent-control / just-cause jurisdictions (CA AB 1482, NJ, OR, NY HSTPA, Portland/Seattle/etc.), non-renewal is proposed without payment-history documentation | Any proposed non-renewal in those jurisdictions. | Preserve payment-history documentation BEFORE decision; chronic nonpayment is valid just cause but must be evidenced. |
| MEDIUM | Site-team hardship discretion is ad-hoc and undocumented | "Gave Mrs. Smith 2 weeks because she's nice" with no written policy. | Disparate-impact liability under Fair Housing Act; require documented hardship-approval criteria and decision log. |
| LOW | Verbal payment plan in force (not signed, not written) | Any tenant with "payment plan" marked but no signed document. | Convert to written plan within 7 days or escalate to band-level collection action; verbal plan does not toll eviction in most states. |
| LOW | Collection-agency referral to non-Regulation-F-compliant agency | Any referral where agency FDCPA/Reg F compliance not confirmed. | Re-vet agency; operator retains vicarious-compliance risk under CFPB Reg F (eff. 11/30/2021). |

---

## When Data is Missing

- **Missing aging-band detail (total A/R only, no buckets).** Apply the whole-A/R balance at the **most conservative (90+) reserve rate** until aging detail is provided. Flag confidence LOW. Request Yardi/RealPage/AppFolio/Entrata Resident Aging Report (all four default to the 5-band schema).
- **Missing state of property.** Do not assume a default state; request. The eviction-timeline overlay is material enough that applying the wrong state can over- or under-state days-to-writ by 90+ days. If truly unobtainable, report "state-agnostic" and apply a midpoint (~45-day) timeline with a HIGH-severity uncertainty flag.
- **Missing property class.** Apply Class B (pack default) overlay for reserve calculation and flag the class-overlay assumption explicitly in the uncertainty_flags. Report both a Class A and a Class C sensitivity on the Total Reserve line.
- **Missing trailing 12-month payment history for chronic-delinquency classification.** Use the current-snapshot-only triggers (any aging >60 days OR any 90+ balance) as a conservative proxy; do not use the 3-late / 2-NSF triggers. Flag confidence LOW on the chronic classification column.
- **Missing pay-or-quit service dates.** Assume NO pay-or-quit served unless documented; this prevents the partial-payment-waiver trap from being under-flagged. Explicitly request notice-service log from site team.
- **Missing ERAP status (jurisdictions NY/NJ/DC/IL).** Do NOT recommend write-off on any 90+ balance in those jurisdictions until ERAP status confirmed absent. Hold the balance at the 90+ reserve % (no write-off) pending confirmation.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full 5-band aging, trailing 12-month payment history, state of property, notice-service dates, payment-plan documentation, property class, and (if applicable) surety product usage all provided. No jurisdiction-specific data gaps (ERAP in NY/NJ/DC/IL; just-cause docs in CA/NY/OR). |
| MEDIUM | Core aging + state + class provided, but one or more of: trailing payment history, notice-service dates, or surety/ERAP status is missing. Reserve calculation defensible but chronic-delinquency classifications use conservative proxy. |
| LOW | Aging bands partial or absent (only total A/R); OR state of property unknown; OR property class unknown; OR material data gap (no payment-plan docs for tenants appearing to be on plans). Bad-debt reserve reported as a range, not a point; tenant-level action list carries explicit flagged assumptions. |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) — A/R aging reserve %s (§2), bad-debt % by class (§7)
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — bad-debt ratio KPI benchmark, class/regional overlays
- [Underwriting Calc](knowledge/underwriting-calc.md) — Bad Debt formula (`Bad Debt = GPI × Bad Debt Rate`), Bad Debt Ratio (cross-referenced, not redefined here)

## Research Basis

- [Rent Collection & Delinquency Manager Research](research/asset-management/rent-collection-delinquency-manager-research.md)

---

## Structured Output

```json
{
  "skill": "rent-collection-delinquency-manager",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "total_ar_balance": 0,
    "ar_by_band": { "current": 0, "1_30": 0, "31_60": 0, "61_90": 0, "90_plus": 0 },
    "past_due_pct_of_receivables": 0,
    "bad_debt_reserve": 0,
    "tenant_action_list": [],
    "chronic_delinquents": [],
    "writeoffs_recommended": []
  },
  "uncertainty_flags": [ { "field_name": "", "reason": "", "impact": "" } ],
  "red_flags": [ { "severity": "HIGH | MEDIUM | LOW", "description": "", "recommended_action": "" } ]
}
```

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
