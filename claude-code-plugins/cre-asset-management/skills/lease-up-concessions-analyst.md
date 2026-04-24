# Lease-Up & Concessions Analyst

Track leasing velocity against the original plan, reconcile effective vs face rent under active concession programs, model concession burn-off, and reforecast the stabilization date when absorption diverges from underwriting.

---

## When to Use This Skill

Use this skill when a property is **actively leasing up**, **burning off concessions**, or **tracking toward stabilization**, and you need to assess whether the asset is on plan, behind plan, or at risk of covenant breach. The three lease-up types are distinguished because their velocity benchmarks and stabilization windows differ materially (per R5 §2):

- **New construction lease-up (ground-up).** No existing tenants, no word-of-mouth, no track record. Months 1–3 typically run 50–70% of peak velocity. Typical stabilization window: 12–18 months in Tier 1–2 balanced markets; 15–24 months in oversupplied Sun Belt.
- **Value-add renovation lease-up (repositioning).** Existing location with social proof. Typical velocity 15–30% faster than comparable ground-up in the same submarket. Typical stabilization window: 6–12 months. (Capex/scope side is owned by the Value-Add Execution Tracker — this skill covers only velocity and concession economics.)
- **Stabilized re-tenanting (post-acquisition mass expiration or re-letting event).** Fastest of the three — the asset is already market-proven and velocity is constrained only by physical turn time and unit-mix match. Typical re-stabilization: 90–180 days.

Do NOT use this skill for: budget-phase revenue assumptions on an already-stabilized asset (Annual Operating Budget Builder), stabilized renewal economics (NOI Improvement Analyst / renewal pricing), or LIHTC / HUD-affordable waitlist dynamics (out of scope — income-restriction distorts velocity).

---

## What You'll Need to Provide

- Property name, address, unit count, first-CO date (or re-start date for renovation / re-tenanting)
- Lease-up type: **NEW CONSTRUCTION**, **RENOVATION**, or **STABILIZED RE-TENANTING**
- Original underwritten leasing schedule: month-by-month target occupancy, target stabilization month, target stabilization occupancy threshold
- Trailing leasing data: at minimum trailing 3 months of new leases signed per month; ideally trailing 6 months
- Current occupancy: total physical units, occupied units, model/employee/down units (for denominator clarity)
- Pre-leasing data if pre-CO: signed pre-leases and deposit status
- Current concession program: months free offered on new leases, any layered incentives (waived pet / admin / app fees, look-and-lease bonuses, free parking, gift cards), lease term months
- Face (asking) rent schedule by floor plan
- Effective rent achieved on new leases signed this month and blended in-place effective rent across occupied units
- Submarket and market tier (Tier 1 Primary / Tier 2 Sun Belt / Tier 3 Secondary / Tier 4 Tertiary / Urban infill high-density)
- Lender type and any occupancy covenants (agency refi target, bridge DSCR covenant, lease-up bridge milestones)
- Operator stabilization definition if different from pack defaults (agency 90% / 90d, owner 93–95% / 90d, LP 95% / 180d + 92% economic)

---

## Mission

Report the property's leasing velocity vs the original plan, quantify the gap between face and effective rent under the current concession program, model the burn-off schedule, and — if trailing absorption is materially below plan — produce a reforecast stabilization date with revised concession burn-off and flag any covenant-breach risk.

---

## Strategy

### Step 1: Establish the Lease-Up Type and Benchmark Anchor

Declare the lease-up type up front because the benchmark sets differ (per R5 §2 and asset-management-benchmarks.md §8):

- **NEW CONSTRUCTION** → use Tier-based absorption ranges (Tier 1 balanced: 15–25 u/mo; Tier 2 Sun Belt 2024–2026 oversupplied: 10–18 u/mo; Tier 3: 8–15 u/mo; Urban infill high-density: 12–20 u/mo with concession support). Default stabilization window 12–18 months (Tier 1–2), 15–24 months (oversupplied Sun Belt).
- **RENOVATION** → scale ground-up pace by +15% to +30%. Default stabilization 6–12 months.
- **STABILIZED RE-TENANTING** → velocity limited by physical turn capacity and unit-mix match. Default re-stabilization 90–180 days.

State the submarket and whether it is currently balanced, oversupplied, or severely oversupplied (per asset-management-benchmarks.md §6 — Austin / Nashville / Phoenix severely oversupplied through early 2026; Dallas / Atlanta / Charlotte / Raleigh / Salt Lake City oversupplied; Miami / South Florida mildly competitive; Gateway balanced). Cite a live Yardi Matrix / RealPage / ALN submarket read when available rather than inheriting the table defaults.

### Step 2: Compute Absorption Status vs Plan

For the current reporting period (typically month-end):

- **Current occupancy %** = Occupied Units / Total Physical Units × 100. Use total physical units as denominator (including model / employee / down units, NOT just "leasable" units) per R5 §9 — this prevents inflated occupancy through rent-ready-exclusion games.
- **Trailing-3 absorption** = new leases signed over the last 3 months / 3 (units/month).
- **Trailing-6 absorption** = new leases signed over the last 6 months / 6 (units/month).
- **Velocity vs plan %** = Actual trailing-3 absorption / Original underwritten absorption for the same period × 100.
- **Units remaining to stabilization** = (Target stabilization occupancy × Total Units) − Occupied Units.
- **Months to stabilization at current pace** = Units remaining / Trailing-3 monthly absorption (fallback to Trailing-6 only if trailing-3 is an outlier per R5 §8).

Apply the **velocity deceleration rule** (R5 §6, KB §8): once the property passes 70–80% physical occupancy, do NOT linearly extrapolate early pace — velocity typically slows 25–50% in the final 10–20%. If the property is in the deceleration band, mark the extrapolation as an upper-bound estimate and apply a deceleration haircut (25% deceleration for 70–80% occupied, 50% for 80%+) before computing the reforecast date.

### Step 3: Reconcile Effective vs Face Rent — Subtractive Convention

Per `_taxonomy-seed.md` §4, Effective Rent is computed **subtractively** — concessions REDUCE effective rent. Any formula producing Effective Rent > Face Rent when concessions > 0 is wrong and must be flagged.

Canonical formula (inherits verbatim from taxonomy seed §4 and underwriting-calc.md):

```
Effective Rent = (Face Rent × Lease Months − Concession Value) / Lease Months
              = Face Rent × (Lease Term − Free Months) / Lease Term
```

Adversarial sanity check: on a 12-month lease at $1,800 face with 1 month free, Effective Rent must equal $1,650. Not $1,950. Not $1,800. If the reported effective rent is $1,800 or higher, the operator is either reporting face-rent mislabeled as effective OR omitting layered concessions (waived fees, gift cards) from the calculation. Flag and re-derive.

Report three rent figures every reporting period (R5 §5):

- **Face rent (asking)** on new units to be leased — by floor plan, averaged unit-weighted
- **Effective rent achieved** on new signed leases this month — actual concessions netted out
- **Blended in-place effective rent** across ALL occupied units — this is the revenue-recognition figure and the number that flows to EGI

When comparing to comps, enforce effective-to-effective comparison (R5 §5). Asking-rent comps from ILS sites routinely embed or obscure concessions; back-solve effective from the face-rent-plus-concession disclosure rather than accepting the posted asking rent.

### Step 4: Characterize the Concession Program and Burn-Off Phase

Classify the current program against the pack two-phase model (R5 §4, KB §6):

- **Heavy-concession phase.** Property is prioritizing velocity over rent maximization. Typical in oversupplied markets below 70% occupancy — 2–3+ months free + layered incentives (waived pet/admin/app, look-and-lease, free parking, gift cards).
- **Tapering phase.** Occupancy has crossed 70–85%; operator is progressively reducing concession depth. Typical: 1 month free on new leases; ancillary incentives curtailed.
- **Normal / burn-off-complete phase.** Occupancy has crossed 90% (stabilized); concessions are 0–0.5 months on new leases; face-rent increases are being pushed.

Pack-default burn-off trigger points (KB §6):

- Past 70% physical → reduce look-and-lease bonuses and ancillary incentives
- Past 80–85% physical → reduce free-rent months from 2 to 1 on new leases
- Past 90% (stabilized) → drop concessions to 0–0.5 months; push face rent

Compute the **concession dollar drag (monthly)**:

```
Monthly Concession Drag = (Face Rent Avg − Effective Rent Avg in-place) × Occupied Units
```

Also break out the concession drag by lease cohort (leases signed during heavy phase vs tapering phase vs normal phase) because even after the operator stops offering new concessions, amortized concessions from earlier leases continue to drag effective rent for **12–15 months** (R5 §4, KB §3 concession-overhang rule). This is why "stabilized occupancy" typically precedes "stabilized effective rent" by a full lease cycle.

### Step 5: Reforecast the Stabilization Date (if Triggered)

Apply the reforecast-trigger table (R5 §8, KB §8):

| Trigger | Action |
|---|---|
| Trailing-3 absorption ≤ 75% of UW for one month | Flag; recalculate stabilization date |
| Trailing-6 absorption ≤ 80% of UW | Formal reforecast (stabilization date, concession burn-off, DSCR at refi) |
| Missed contractual milestone (e.g., 80% by Month 10 lender covenant) | Immediate lender communication; CMBS watchlist risk |

When a reforecast is triggered, compute the three figures in this order (R5 §8 reforecast mechanics):

1. **Revised stabilization date** = Current occupancy + (Remaining units to stabilization / Actual trailing-3 monthly absorption). Use the deceleration haircut from Step 2 if crossing the 70–80% deceleration band.
2. **Revised concession burn-off schedule.** Extend the heavy-concession phase by the stabilization-date slippage; the 70%/80%/90% trigger points remain the same but the calendar dates shift. Project the month at which concessions drop to 1 month and to 0–0.5 months.
3. **Revised EGI ramp and DSCR coverage** at each reforecast point. If a lease-up bridge covenant DSCR test sits at a date before the revised stabilization date, flag the covenant-breach risk to ownership at least 6 months ahead of the test date (R5 §edge-case on debt-fund bridge covenant breach risk).

### Step 6: Declare the Stabilization Threshold Being Applied

The stabilization definition varies by audience (KB §3). Declare explicitly which threshold is being used and why:

- **Agency floor (Fannie Mae / Freddie Mac)** — 90% physical, sustained 90 consecutive days. Regulatory anchor for agency-refi readiness; gates conversion of lease-up loans into permanent agency debt.
- **Owner-operator working target** — 93–95% physical, 90 days sustained, with economic occupancy 91–93% simultaneously for the higher threshold.
- **Institutional LP-reporting (conservative)** — 95% physical + 92% economic simultaneous, sustained 180 days. Eliminates amortized-concession overhang noise.
- **Debt-fund bridge covenant alternative** — 90% physical OR trailing-3 DSCR ≥ 1.20x, 90 days.

The spread between the 90% agency floor and the 95% operator target is typically 3–6 months of additional lease-up velocity — always flag which threshold a reported "stabilized" status refers to. A sponsor building to an agency-refi exit can legitimately target 90%; a sponsor underwriting internal stabilized returns should use 93–95%.

### Step 7: Market Context and Forward View

Anchor the report with submarket context:

- Current concession depth vs submarket peer lease-ups
- Submarket delivery pipeline over next 12 months (overlapping lease-ups cannibalize demand; adjust per-property absorption down 20–30% when the submarket has concentrated deliveries per R5 edge cases)
- Pre-leasing rate at first CO (if new construction) vs market benchmark (Strong 25–40%, Normal 10–25%, Weak 5–15%, Sun Belt oversupplied <10% per R5 §9 and KB §8). Haircut signed pre-leases by 15% for cancellation per KB §8 underwriting haircut.
- Whether concession compression is showing in the submarket (Austin began compressing Q4 2025 per R5 §11)

---

## Output Format

```markdown
# Lease-Up & Concessions Analysis
## Property:
## Lease-Up Type: NEW CONSTRUCTION | RENOVATION | STABILIZED RE-TENANTING
## Submarket / Tier:
## Report Date:
## Status: ON PLAN | BEHIND PLAN | AT RISK | STABILIZED

---

### Absorption Status

- Total Physical Units:
- Occupied Units (incl. model/employee/down excluded from numerator):
- Current Physical Occupancy %:
- Trailing-3 Absorption (units/month):
- Trailing-6 Absorption (units/month):
- Original Underwritten Absorption (units/month, same period):
- Velocity vs Plan %:
- Units Remaining to Stabilization (at declared threshold):
- Months to Stabilization at Current Pace (with deceleration haircut if 70%+):

### Effective-vs-Face Rent Reconciliation

- Face Rent Avg (unit-weighted):
- Effective Rent Achieved — new leases signed this month:
- Blended In-Place Effective Rent — all occupied units:
- Concession Program: X months free on Y-month lease + layered incentives
- Monthly Concession Dollar Drag: $
- Sign Check: Effective < Face when concessions > 0 — PASS | FAIL

### Concession Program Status

- Current Burn-Off Phase: HEAVY | TAPERING | NORMAL
- Layered Incentives Active:
- Occupancy Trigger Points:
  - 70% (reduce ancillary): MET | NOT MET — current % is ___
  - 80–85% (reduce free months 2→1): MET | NOT MET
  - 90% (drop to 0–0.5): MET | NOT MET
- Concession Cohort Overhang: Leases signed in heavy phase amortize through Month ___; blended effective rent will not stabilize until ~12 months after occupancy stabilizes.

### Stabilization Reforecast

- Declared Stabilization Threshold: Agency 90%/90d | Owner 93–95%/90d | LP 95%/180d + 92% econ | Bridge 90% or DSCR ≥ 1.20x
- Rationale for Threshold:
- Original Stabilization Date:
- Reforecast Stabilization Date:
- Slippage (months):
- Reforecast Trigger Fired: NONE | Trailing-3 ≤ 75% | Trailing-6 ≤ 80% | Missed Covenant Milestone
- Revised Concession Burn-Off Schedule:
  - Heavy → Tapering (projected month):
  - Tapering → Normal (projected month):
  - Effective-Rent Stabilization (projected month, ~12mo after occ stabilization):
- Covenant-Breach Risk: Y/N — describe
- DSCR Impact at Refi Test Date:

### Market Context

- Submarket Condition: Balanced | Mildly Competitive | Oversupplied | Severely Oversupplied
- Submarket Concession Peer Depth:
- Overlapping Deliveries in Submarket (12mo pipeline):
- Pre-Leasing at First CO (if applicable): ___% vs market benchmark of ___%
- Concession Compression Signal: None | Early | Underway
- Comparable REIT Disclosure Reference (Camden / MAA / AvalonBay / UDR / Essex, if relevant):

### Key Risks

- ...

### Verdict

ON PLAN | BEHIND PLAN | AT RISK | STABILIZED (against declared threshold)

### Confidence Level

HIGH | MEDIUM | LOW
```

---

## Quality Checks

- **Effective rent < Face rent when concessions > 0 (sign check).** Apply the taxonomy-seed §4 subtractive convention. Any reported effective rent equal to or above face rent while concessions are in force is a sign error or an incomplete concession disclosure — re-derive from face + concession value before reporting.
- **Occupancy denominator is total physical units, not "leasable" units.** Rent-ready / held-back / model / down units stay in the denominator to prevent inflated occupancy percentages (R5 §edge-case on rent-ready unit inflation).
- **Lease-up type declared and matched to its benchmark set.** A ground-up new construction is not benchmarked against a stabilized re-tenanting; if the type is not declared, the velocity-vs-plan assessment is meaningless.
- **Stabilization threshold explicitly declared.** Agency 90%/90d vs owner 93–95% vs LP 95%/180d — the audience determines the threshold. Any "stabilized" claim without the threshold and the sustained-duration check is not a stabilization claim.
- **Pre-lease cancellation haircut applied (15% pack default).** Signed pre-leases are counted at 85% of the signed number, not 100%, because 10–20% cancellation is normal (R5 §9). Not applying the haircut overstates incoming velocity.
- **Velocity deceleration rule applied when occupancy ≥ 70%.** Do not linearly extrapolate early pace into the final 10–20% window — apply the 25–50% deceleration haircut per R5 §6.
- **Three rent figures reported.** Face (asking), effective on new signed leases this month, blended in-place effective across all occupied units. Face-only reporting is not sufficient.
- **Concession cohort overhang disclosed.** If the property is approaching or past stabilized occupancy, disclose that amortized concessions from lease-up leases continue to drag effective rent for 12–15 months after the operator stops offering new concessions (R5 §4, KB §3).

---

## Red Flags & Dealbreakers

- **Accelerating absorption in the final 10% (85%–95%).** Contrary to the typical deceleration pattern. Signals the operator may be dropping rate to hit a covenant, the occupancy number may include model/employee/down units in the numerator, or a related-party lease-up is masking real demand. Investigate before accepting reported velocity (R5 §edge-cases).
- **Zero concessions reported in an oversupplied submarket.** If peer properties in the same submarket are offering 2–3 months free and this property reports zero, either (a) the asset is severely mispricing and losing share, or (b) concessions are off-sheet (gift cards, waived fees, parking) and excluded from the effective-rent calculation. Re-derive effective rent from a full-program audit before accepting the reported face rent.
- **"Stabilized" claimed without 90 consecutive days at threshold.** A single-period 90% reading followed by a drop to 88% is NOT stabilization under the agency definition. A property claiming stabilized status without 90 consecutive days is premature and must be re-verified.
- **Missed lender occupancy covenant (e.g., 80% by Month 10).** Triggers immediate lender communication. CMBS watchlist designation risk (R5 §8, Trepp reference). Do not defer — a reforecast that surfaces this at least 6 months ahead of a bridge-loan DSCR covenant test is materially better than a surprise breach.
- **Pre-leases concentrated in related parties (corporate housing JV, affiliated master lease).** Not independent demand evidence. Scrutinize the first 5–10% of leases for related-party patterns (R5 §edge-cases on pre-leased-to-related-party).
- **Face-rent NOI used for cap-rate valuation on a heavily concessioned asset.** Per R5 §10, appraisers increasingly disclose both face-rent NOI and effective-rent NOI; brokers sometimes quote cap rate on face, inflating apparent value by 10–15 bps. If a valuation was struck on face-rent NOI during active concession burn-off, the lender (Fannie Form 4660) will haircut it back.

---

## When Data is Missing

- **If trailing-6 absorption data is unavailable**, use trailing-3 only, mark the reforecast as directional, and lower confidence. Pull back-month data from Yardi Matrix / RealPage / ALN if accessible.
- **If the operator will not disclose the full concession program (layered incentives)**, back-solve the likely effective rent from observed EGI or blended in-place rent divided by total occupied units — the residual vs face is the implied concession. Flag the derivation as inferred, not disclosed.
- **If the original underwritten stabilization schedule is not available**, substitute the pack default for the property's lease-up type and market tier (per KB §8 tier ranges), state the substitution explicitly, and lower confidence. A velocity-vs-plan ratio computed against a substituted plan is directional, not precise.
- **If submarket peer concession data is unavailable**, default to the pack market-condition classification (KB §6) for the submarket and note that concession-peer comparison is indicative, not live.
- **If pre-leasing history is unavailable on a pre-CO new construction**, underwrite to the weak / oversupplied default (5–15% pre-leased, or <10% for Sun Belt oversupplied per R5 §9) rather than to the strong / normal default. Conservative bias; adjust with operator-specific data when provided.
- **If model / employee / down unit counts are not disclosed**, treat the reported "occupied" figure as an upper bound; apply a 1–3% haircut to occupancy for reasonable back-of-envelope adjustment; mark confidence LOW on the occupancy figure.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Trailing-6 absorption available; original underwritten schedule intact; full concession program disclosed (including layered incentives); occupancy denominator clear (physical units including model/down); submarket peer data from Yardi Matrix / RealPage / ALN current within 60 days |
| MEDIUM | Trailing-3 available and directionally clean; concession program partially disclosed (face + months free only, layered incentives inferred); plan substitution is from pack defaults for tier / type; submarket peer data older than 60 days or second-hand |
| LOW | Only point-in-time occupancy available; concession program inferred from EGI residual; no original underwritten schedule; submarket condition classified from table defaults only; pre-lease / model-unit ambiguity in occupancy numerator |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](../knowledge/asset-management-benchmarks.md) — §3 stabilization definitions, §6 concession depth by market condition + burn-off triggers, §8 absorption by market tier + lease-up type + reforecast triggers
- [Multifamily Benchmarks](../knowledge/multifamily-benchmarks.md) — rent growth by tier, economic-vs-physical occupancy diagnostic, cap-rate ranges
- [Underwriting Calc](../knowledge/underwriting-calc.md) — Concessions and free-rent adjustment formula (verbatim), EGI derivation, DSCR

---

## Structured Output

```json
{
  "skill": "lease-up-concessions-analyst",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "current_occupancy_pct": 0,
    "absorption_velocity_units_per_month": 0,
    "velocity_vs_plan_pct": 0,
    "face_rent_avg": 0,
    "effective_rent_avg": 0,
    "concession_dollar_drag_monthly": 0,
    "stabilization_date_original": "",
    "stabilization_date_reforecast": "",
    "burn_off_phase": "heavy | tapering | normal"
  },
  "uncertainty_flags": [],
  "red_flags": []
}
```
