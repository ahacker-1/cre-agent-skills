# NOI Improvement Analyst

Identify and prioritize NOI improvement levers at a stabilized conventional multifamily property, producing a scored, sequenced action list that separates quick wins from strategic initiatives.

---

## When to Use This Skill

Use this skill when you have a stabilized (non-value-add, non-refi, non-renovation-driven) multifamily property and need to identify where incremental NOI can be unlocked through operating-level initiatives. It is the right starting point for annual business plans, mid-hold asset reviews, and LP update cycles where the question is "what do we do this year and next to push NOI?" — not "what physical renovation do we underwrite?" (→ value-add CapEx skill) or "should we refinance / sell?" (→ hold-sell-refi skill) or "how do we improve retention?" (→ renewal skill). It is especially useful on assets where rent growth has flattened and the remaining upside sits in ancillary income, expense discipline, and recovery programs.

---

## What You'll Need to Provide

- Current T-12 operating statement (income and expense detail by line item)
- Current rent roll (unit-level contract rent, market rent estimate, lease end dates)
- Property class (A / B / C) and vintage
- Market and state (for RUBS legality, tax-appeal jurisdiction, insurance market posture)
- Current ancillary income mix (what's already charged: pet, parking, RUBS, valet trash, etc.) with $/unit/yr
- Recent insurance premium and deductible structure (last renewal date, carrier, CAT exposures)
- Recent property-tax history (assessed value trajectory; any prior appeals in last 24 months)
- Unit count, occupancy (physical and economic), current concession schedule
- Operator-specific constraints (rent-control exposure, corporate ESG mandates, fee-transparency policy)

---

## Mission

Produce a prioritized, scored list of NOI-improvement initiatives for a stabilized multifamily property, with each lever quantified in $/unit/yr, sanity-checked against institutional benchmarks, scored on two axes (Impact × Difficulty) with a time-to-realize dimension, and separated into a 6-month Quick-Win list and an 18-month Strategic Roadmap. Flag regulatory and retention-interaction risks explicitly.

---

## Strategy

### Step 1: Baseline NOI and Ancillary Share

Compute and record:

- T-12 EGI, Total OpEx, NOI (per `_taxonomy-seed.md` and `knowledge/underwriting-calc.md`)
- NOI per unit per year
- Current Other Income as % of EGI (institutional benchmark: 7–9% typical; 10%+ best-operated; per `knowledge/asset-management-benchmarks.md`)
- Total owner-paid utility spend (the recovery pool for RUBS/submetering)
- Insurance premium as $/unit/yr
- Property taxes as $/unit/yr (flag vs state benchmark in `knowledge/multifamily-benchmarks.md`)
- Current concession load ($/unit/yr and % of GPR)
- Loss-to-Lease % (Market Rent vs In-Place, per taxonomy §4)

The baseline establishes what is **already captured** and prevents double-counting.

### Step 2: Walk the Lever Library (from R7)

For each lever family, determine (a) whether it is already implemented, (b) partially implemented, or (c) not implemented. Only estimate lift against the un-captured portion.

**2A. Ancillary Income Levers**

- **Pet Rent Program.** $25–$75/pet/mo (Class-dependent); at 50% penetration + $40/mo avg → ~$240/unit/yr. FHA assistance-animal exclusion required.
- **Parking (covered / garage / reserved / EV).** $50–$200/unit/mo where scarcity exists. EV premium $25–$50/mo on assigned spots (capex routes to value-add skill if material).
- **Storage Units.** $25–$150/unit/mo per rented unit at 20–40% penetration → ~$120–$360/unit/yr portfolio-wide. Fire/egress review required.
- **Short-Term / Month-to-Month Premium.** $50–$200/unit/mo on the short-term cohort only.
- **Tech Package (smart lock / thermostat / wifi).** $25–$50/unit/mo; capex $300–$1,200/unit. If the economic case is base-rent premium, route to value-add skill.
- **Valet Trash.** $25–$50/unit/mo gross; net $10–$30/unit/mo after vendor → $120–$360/unit/yr. Fee-transparency disclosure mandatory.
- **Package Locker / Delivery Subscription.** $5–$15/unit/mo; Luxer-as-a-Service avoids $20–60K capex.
- **RUBS Admin Fee.** $3–$8/unit/mo = $36–$96/unit/yr (on top of pass-through). Scrutinized in CA rent-control.
- **Application / Admin / Late Fees.** Combined $15–$40/unit/mo = $180–$480/unit/yr. State caps apply (CA application-fee cap ~$59.67 as of 2025).

**2B. RUBS / Utility Recovery (with state-legality flag)**

- Water-only RUBS: $30–$80/unit/mo net recovery; near-zero capex; 3–6 months to realize.
- Full submetering: 85–95% cost recovery; $300–$800/unit capex; 12–24 months.
- **State-legality flag (MANDATORY per R7).** Run the CA / TX / IL / FL check:
  - **CA:** No statewide ban, but rent-stabilized jurisdictions (Mountain View CSFRA, SF RSO, LA RSO, Oakland, Berkeley, Santa Monica, San Diego with AB 1482 overlay) may treat RUBS fees as rent subject to annual cap. Require jurisdiction-specific legal opinion before recommending.
  - **TX:** Permitted; Texas Water Code §13.503 / PUC rules govern disclosure and registration for allocation billing.
  - **IL:** Permitted statewide; Chicago adds disclosure requirements.
  - **FL:** Permitted statewide under PSC rules; standard lease disclosure.
  - **Other high-regulation states (NY, MA, NJ, MD):** Require legal review before rollout.
- **Universal rules:** No markup-for-profit; allocation formula disclosed at signing; mid-lease formula change requires consent.

**2C. Property-Tax Appeal**

- Typical AV reduction on successful appeal: 5–20%; at 2% effective rate and 10% AV cut on a $20M property → ~$40,000/yr OpEx relief (~$200/unit/yr on 200-unit).
- **National success rates (per R7):** 40–60% baseline; **65–85% with professional representation and evidence**.
- **Jurisdiction variance:** Hays County TX 98.68% vs Cook County IL 62%. Texas counties generally >75% for protested commercial. CA Prop-13 limits useful appeals outside transfer years.
- Cost: $2,500–$10,000 flat OR 25–40% contingency of savings.
- Time-to-realize 6–18 months to decision; multi-year lookback often available.
- Route to professional contingency firm (no-downside) vs pro-se on commercial/MF.

**2D. Insurance Shopping & Structures**

- Annual RFP (institutional norm >$50M insured value): typical 5–15% savings in soft/normal market; 0–5% in hard market (post-Ian 2022–2024 coastal habitational).
- Captive (single-parent economical >$1M–$3M annual premium): $100K–$500K setup; 18–36 months to realize; underwriting-profit retention plus investment income.
- Parametric CAT (hurricane/EQ/wildfire): complement, not replacement. Basis-risk disclosure mandatory (Hurricane Beryl cat-bond non-payment precedent). 60–120 days to execute.

**2E. OpEx Reduction**

- **Centralized procurement (MRO + capital).** 5–10% savings on controllable spend → on a Class B ~$2,500–$3,500/unit controllable base, 7% → $175–$245/unit/yr. 12–24 months to realize.
- **Regional maintenance pods (10-mile radius model).** 10–25% payroll efficiency gain → $150–$400/unit/yr at Class B/C. Requires geographic density.
- **Third-party contract renegotiation.** 5–15% on contract services → $15–$90/unit/yr at Class B.
- **Energy efficiency.** LED common-area: 50–66% lighting reduction → $75–$200/unit/yr; smart thermostats: ~8% HVAC savings, ~$50/unit/yr (ENERGY STAR conservative); BMS broadly: 10–20% building-level → up to $225/unit/yr on $1,500/unit utility base. Do not embed rebate revenue in steady-state.

**2F. Technology-Enabled Revenue**

- **AI leasing / AI-guided tours.** 44.8% higher lead-to-lease, 30% higher lead-to-tour (vendor-reported, treat as upper bound). Implied $100–$300/unit/yr NOI on assets with prior response-lag problems; ~$0 where leasing was already strong.
- **Concession policy optimization.** Upfront-month-free > spread-discount for Year-2 NOI (clean renewal anchor per R7).
- **Loss-to-Lease recapture at renewal.** Cap at 3–5% per renewal cycle; anything >5% routes to retention skill for validation.

### Step 3: Score Each Lever (2-Axis: Impact × Difficulty)

**Impact score (1–5):** based on estimated $/unit/yr lift after applying class/regional multipliers from `knowledge/multifamily-benchmarks.md`.

| Impact Score | $/unit/yr Estimated Lift |
|---|---|
| 1 | < $50 |
| 2 | $50–$150 |
| 3 | $150–$300 |
| 4 | $300–$500 |
| 5 | > $500 |

**Difficulty score (1–5, where 1 = easy, 5 = hard):**

| Difficulty Score | Criteria |
|---|---|
| 1 | Zero capex, no lease change, no regulatory exposure. (Insurance RFP in soft market; contract renegotiation at renewal.) |
| 2 | Lease-template change only; no hardware or staff restructuring. (Pet rent, parking unbundle.) |
| 3 | Hardware/tech install; modest capex; measurable resident experience change. (Smart thermostats, package lockers.) |
| 4 | Staff restructuring OR regulatory exposure. (Maintenance pods, RUBS in CA rent-control overlay.) |
| 5 | Captive setup, parametric structure, or fundamental billing-model change in high-regulation jurisdiction. |

**Time-to-realize (months):** Fast 0–6, Medium 6–18, Slow 18–36+.

**Priority Score formula:**

```
Priority Score = (Impact $/unit/yr ÷ Difficulty Score) × (12 ÷ Time-to-Realize in months)
```

### Step 4: Apply Sanity-Check Constraints

1. No lever with >$500/unit/yr impact is ranked #1 unless you have validated current state does not already capture it.
2. No lever with Difficulty ≥ 4 is ranked top 3 unless operator explicitly requests.
3. Legal/regulatory-risk levers (RUBS in CA rent-control, captive setup, mandatory-fee rollout) carry a mandatory disclosure footnote.
4. Total ancillary cap: Class B ≤ 15% EGI; Class A ≤ 20% EGI. Over-stacking beyond this is flagged as implausible.
5. LTL recapture > 5% in single renewal cycle routes to retention skill for validation before recommending.

### Step 5: Produce Quick-Win and Strategic Splits

- **Quick Wins (6-month):** Fast time-to-realize levers (insurance RFP, admin-fee changes, RUBS admin fee, contract renegotiation, LTL bump next renewal, pet rent rollout on new leases).
- **Strategic (18-month roadmap):** Medium and slow levers sequenced by dependency (e.g., centralized procurement precedes contract renegotiation; submetering retrofit precedes higher recovery; tax appeal timing aligned to jurisdiction filing window).

### Step 6: Cross-Check Against Benchmarks

- Aggregated projected other-income ≤ 15% EGI Class B / 20% EGI Class A — otherwise flag over-stacking.
- Projected OpEx ratio post-initiatives not more aggressive than `knowledge/multifamily-benchmarks.md` best-in-class for the property's class and region.
- Total projected NOI lift stated both in $ and as % of baseline NOI (typical stabilized-asset realistic range: 3–8% NOI lift over 18 months; >12% flag as likely overstated).

---

## Output Format

```markdown
# NOI Improvement Analysis
## Property: {name}
## Class: {A | B | C}   Market: {metro, state}   Unit Count: {n}
## Analysis Date: {YYYY-MM-DD}
## Confidence Level: HIGH | MEDIUM | LOW

### NOI Baseline
- T-12 EGI: $
- T-12 Total OpEx: $
- T-12 NOI: $
- NOI per unit/yr: $
- Current Other Income: $  ({%} of EGI)
- Current Insurance: $/unit/yr
- Current Property Taxes: $/unit/yr
- Current Loss-to-Lease: %

### Lever-by-Lever Analysis Table

| # | Lever | Category | Current State | Est. Lift $/unit/yr | Annualized Lift $ | Impact (1-5) | Difficulty (1-5) | Time-to-Realize (mo) | Priority Score | Regulatory Flag | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ... | Ancillary / RUBS / Tax / Insurance / OpEx / Tech |  |  |  |  |  |  |  |  |  |

### Prioritized Action List (Top 10, descending Priority Score)

1. {Lever} — est. $X/yr lift; Impact {n}, Difficulty {n}, {n} months. Next step: {...}
2. ...

### Quick-Win Summary (6-Month Horizon)

- {Lever}: $X/yr; owner of action: {...}; expected impact by month {n}.
- {Lever}: ...

Projected 6-month NOI lift (annualized): $

### 18-Month Strategic Roadmap

- Months 0–6: {sequence of Quick Wins}
- Months 6–12: {medium-cycle initiatives — e.g., procurement platform launch, tax-appeal filing, submetering scoping}
- Months 12–18: {longer-cycle — e.g., maintenance-pod rollout, captive feasibility, full LTL recapture}

Projected 18-month total NOI lift: $  (% of baseline NOI: {%})

### Regulatory & Retention Risk Flags

- RUBS state-legality: {state-specific note}
- Rent-control overlay: {yes/no, jurisdiction}
- Fee-transparency exposure: {state junk-fee laws triggered: CA/CO/MN/...}
- LTL recapture exceeds 5%/cycle: {yes/no → route to retention skill if yes}
- AI-leasing disclosure: {Colorado AI Act / CA AB 2013 compliance noted}

### Confidence Level
HIGH | MEDIUM | LOW

### Key Assumptions
- ...
```

---

## Quality Checks

- Baseline NOI is computed per taxonomy seed conventions (NOI excludes Replacement Reserves; NCF = NOI − Replacement Reserves for agency/LP reporting bridge).
- Every lever's estimated lift is bounded against `knowledge/multifamily-benchmarks.md` class/regional ranges — no lever estimate exceeds its benchmark range without documented justification.
- Current-state column is populated for every lever (already-implemented / partial / not-implemented) to prevent double-counting.
- Scoring is genuinely 2-axis: Impact AND Difficulty both populated; Priority Score uses `(Impact $/Difficulty) × (12/Time-to-Realize)`, not impact alone.
- Total ancillary projection after stacking ≤ 15% EGI (Class B) or 20% EGI (Class A).
- RUBS recommendations carry the CA / TX / IL / FL state-legality flag (or equivalent state-specific note) and require operator legal opinion before implementation.
- Property-tax-appeal lever notes the 40–60% national success rate and the 65–85% with professional representation; jurisdiction-specific variance cited when state is known.
- Loss-to-Lease recapture > 5% per cycle flagged and routed to retention skill for validation.
- Quick-Win list (≤6 month) is genuinely separable from Strategic (>12 month) — no lever appearing in both unless phased.
- Confidence is rated using the rubric below; missing-data items are enumerated.

---

## Red Flags & Dealbreakers

- **Over-stacking ancillary fees.** Stacked ancillary projection > 15% EGI for Class B or > 20% EGI for Class A — real-world portfolios do not stack all levers cleanly and the market will not bear it. Cap the aggregate recommendation or refuse the over-stacked case; do not publish a headline NOI number built on stacked fees above these thresholds (per R7 prioritization framework).
- **RUBS rollout in rent-stabilized jurisdiction without legal opinion.** Mountain View CSFRA ruling treats RUBS fees as rent subject to annual rent-control cap; similar logic applies across SF RSO, LA RSO, Oakland, Berkeley, Santa Monica, San Diego (AB 1482 overlay), NYC, and other controlled markets. Never recommend RUBS implementation in a rent-stabilized jurisdiction without operator-attached jurisdiction-specific legal opinion.
- **Aggressive LTL recapture that erases itself through churn.** Loss-to-Lease recapture > 5% in a single renewal cycle drives move-outs; turnover cost + vacancy drag frequently erases the renewal-bump NOI gain. Must route to retention skill for retention-model validation before implementation.
- **Mandatory fee rollout without fee-transparency compliance.** Post-2024 junk-fee laws in CA, CO, MN, and others, plus NMHC RETTC / MITS 5.0 guidance and the Greystar class-action precedent (Colorado, Jan 2024), mean mandatory fees (valet trash, tech package, admin fee) must appear in advertised rent figures per state rules. Never recommend a mandatory-fee structure without a compliance review.
- **Parametric CAT insurance as primary coverage.** Parametric is a complement layered over (not replacing) traditional indemnity. Hurricane Beryl $150M cat-bond non-payment is the cautionary precedent. Any recommendation that positions parametric as primary CAT coverage is wrong.
- **Insurance RFP savings projection in a hard market.** In a hard CAT-exposed market (post-Ian 2022–2024 coastal habitational is the current reference point), 5–15% savings is not achievable. Assume 0–5% and flag upside separately — do not bake 10% insurance savings into the NOI lift projection.
- **Tax-appeal in Prop-13 California outside transfer year.** Structurally appeal-rare; skip the lever for long-held CA assets unless specific triggering facts (economic-obsolescence claim, base-year error) exist.

---

## When Data is Missing

- **If T-12 OpEx line-item detail is missing** (only summary totals provided), OpEx-reduction lever estimates collapse to Class-benchmark-range central values from `knowledge/multifamily-benchmarks.md`; confidence drops to MEDIUM or LOW. Flag Centralized Procurement and Contract Renegotiation as "range-only; requires line-item detail to refine."
- **If current ancillary-income mix is unspecified**, assume a Class-typical baseline (Class A ~10% of EGI; Class B ~8%; Class C ~6%) and flag every ancillary lever as "validation-required — confirm not already captured." Do not publish ancillary lift estimates without this flag.
- **If state is unknown**, suppress all state-legality-dependent recommendations (RUBS specifics, application-fee increases, AI-leasing disclosure requirements). Output generic lever identification with an "awaiting jurisdiction" annotation.
- **If property-tax appeal history is missing**, annotate the lever with "Appeal history unknown — check if assessment has been challenged in last 24 months before recommending; many jurisdictions impose cooldown periods."
- **If loss-to-lease cannot be computed** (no market-rent estimate supplied), route to the renewal / market-rent analysis step before scoring LTL recapture. Do not score a lever you cannot estimate.
- **If insurance renewal date is unknown**, annotate Insurance RFP with "timing-dependent; RFP only useful in 60–120 day window before renewal" and suppress from Quick-Win list if renewal just occurred.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | T-12 with full line-item detail, current ancillary mix documented, state known, property-tax history available, recent insurance renewal terms provided. Every scored lever has a current-state flag. |
| MEDIUM | T-12 at summary level OR one of (ancillary mix / state / tax history / insurance terms) missing. Scored levers require documented assumptions; range-only estimates for affected categories. |
| LOW | T-12 summary only AND multiple missing inputs (state unknown OR ancillary baseline unclear OR no tax-appeal history OR no insurance data). Output is directional — identify lever categories but suppress specific dollar projections outside benchmark ranges. |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) — ancillary lift benchmarks, Class-specific ranges
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — per-unit OpEx ranges, property-tax by state, insurance deep dive, class/regional multipliers
- [Underwriting Calc](knowledge/underwriting-calc.md) — NOI, EGI, LTL, bad debt, concession formulas

---

## Structured Output

```json
{
  "skill": "noi-improvement-analyst",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "baseline_noi": 0,
    "total_estimated_lift": 0,
    "lift_as_pct_of_noi": 0,
    "prioritized_levers": [
      {
        "lever": "",
        "category": "",
        "estimated_lift_annual": 0,
        "impact_score": 0,
        "difficulty_score": 0,
        "time_to_realize_months": 0,
        "priority_score": 0
      }
    ],
    "quick_wins": [],
    "regulatory_risk_levers": []
  },
  "uncertainty_flags": [],
  "red_flags": []
}
```
