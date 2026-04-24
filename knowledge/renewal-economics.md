# Renewal Economics & Hold/Sell/Refi Decision Frameworks

> **What this is:** A shared-reference knowledge base capturing the decision economics for (a) keeping an existing resident on renewal vs. accepting a unit turn, and (b) holding, selling, or refinancing a stabilized multifamily asset mid-hold.
> **How to use it:** This KB captures renewal + hold/sell/refi decision frameworks. Consumed by: Renewal Decision Analyst, CapEx/Value-Add Tracker, Hold/Sell/Refi Analyst. Load alongside the consuming skill. All IRR, DSCR, cap rate, and equity multiple formulas are defined in `knowledge/underwriting-calc.md` — this KB adds the *application layer* on top of those formulas and should not redefine them.

This reference assumes conventional, stabilized, U.S. market-rate multifamily (5+ units), post-2023 supply-normalization environment. All ranges should be adjusted for local submarket, vintage, and catastrophe exposure using the Submarket Adjustment Protocol in `knowledge/multifamily-benchmarks.md`.

---

## Section 1 — Retain-vs-Replace Framework (Renewal Decision Core)

The fundamental renewal decision is a unit-level comparison: the all-in cost of keeping an existing resident through renewal vs. the all-in cost of accepting a turn and re-leasing.

### The Canonical Formulas

**Retention Cost** (per unit, per decision cycle):

```
Retention Cost = Renewal Concession $
              + (Market Rent − Renewal Rent) × 12
              + ~$25 administrative cost
```

The `(Market Rent − Renewal Rent) × 12` term is the opportunity cost of renewing a resident at below-market rent. If renewal rent equals or exceeds market, this term is zero or negative (a retention *benefit*).

**Turn Cost** (per unit, per turn event):

```
Turn Cost = Unit-Turn CapEx
         + Downtime Rent Loss (Days Vacant × Monthly Rent / 30)
         + Leasing Cost Per New Lease
         + New-Lease Concession (annualized)
         − (New-Lease Rent − Current In-Place Rent) × 12    [replacement-lease rent pickup]
```

The final term is **subtracted** because the turn may produce a new lease at a higher rent than the current resident pays — the replacement-lease rent pickup offsets the cost of turning.

**Decision rule:** Offer renewal at a rent level where `Retention Cost < Turn Cost`, subject to the rent-bump elasticity ceiling in Section 3 (above which the renewal rate itself falls so low that expected-value math inverts). [R4]

### Illustrative Worked Example (Class B, softening market)

- In-place rent $1,800/mo. Market rent $1,850/mo. Unit-turn capex $2,200. Downtime 28 days → $1,680 rent loss. Leasing cost $700. Renewal offer $1,854 (+3%). New-lease trade-out -3% ($1,800). No concessions either way.
- **Retention Cost** = $0 + ($1,850 − $1,854) × 12 + $25 ≈ −$23 (effectively zero; renewal at market)
- **Turn Cost** = $2,200 + $1,680 + $700 + $0 − ($1,800 − $1,800) × 12 = **$4,580**
- **Renewal dominates turn by ~$4,600**, even at +3% bump. [R4]

### Scope Boundary — What "Turn Cost" Includes

- **In scope:** make-ready capex (IREM "Leasing Expenses — Make-Ready"), downtime rent loss, leasing cost per new lease, new-lease concession
- **Out of scope:** value-add renovation capex (classic-to-premium upgrade — track in CapEx/Value-Add Tracker); if a unit is already scheduled for a value-add renovation at next move-out, only the *incremental* make-ready cost over and above the renovation cost enters the Turn Cost line. [R4]

---

## Section 2 — Turnover Cost Components

### Unit-Turn CapEx (Make-Ready Only)

Defined as the minimum capital required to put a vacated unit back on the market at existing finish level. Excludes value-add upgrades.

| Class | Finish Level | Unit-Turn CapEx | Pack Default (Midpoint) |
|---|---|---|---|
| Class A | Quartz, LVP, stainless | $2,500 – $3,500 (exceptional $4,500) | $3,000 [R4] |
| Class B | Mid-grade counters/flooring, mid-grade appliances | $1,800 – $2,700 | $2,200 [R4] |
| Class C | Builder-grade, laminate, older appliances | $1,200 – $2,000 | $1,500 [R4] |

**Scope composition (typical turn):**
- Paint (full or touch-up): 40–60% of cost
- Flooring (carpet clean/replace, LVP patch/replace — 3–7 year replacement cycle): 15–30%
- Appliance prorate (replace-as-needed, amortized): 5–10%
- Make-ready cleaning: 10–15%
- Minor repairs (fixtures, hardware, punch-list): 5–10% [R4]

**Cost-of-living adjustment:** Apply Tier 1 turnover multiplier **1.30x–1.70x** for gateway metros (NYC, SF, Boston, DC, LA) per `multifamily-benchmarks.md` Submarket Adjustment Protocol. Example: Class B Sun Belt turn at $2,200 → $2,860–$3,740 in coastal Tier 1. [R4 + cross-reference `multifamily-benchmarks.md`]

**Vintage adjustment:** Apply **1.10x–1.25x** for pre-1990 product (higher flooring replacement frequency, more punch-list work). [R4]

### Downtime (Days Vacant Per Turn)

Time from move-out to new-lease move-in. Institutional benchmark: **10–30 days** for stabilized market-rate properties. Breakdown:
- Make-ready cycle: 5–10 days
- Marketing/leasing cycle: 5–20 days [R4]

| Class/Market | Days Vacant | Pack Default |
|---|---|---|
| Class A urban/primary | 10–20 days | 15 [R4] |
| Class B suburban/primary | 20–35 days | 25 [R4] |
| Class C/tertiary | 25–45 days | 35 [R4] |
| Winter turns (Dec–Feb) | Add 5–15 days vs. peak-season | Seasonal leasing friction [R4] |

**Downtime rent loss formula:** `Days Vacant × (Monthly Rent / 30)`. On a $1,800/mo unit: 25 days = $1,500; 40 days = $2,400. Frequently exceeds unit-turn capex itself. [R4]

### Leasing Cost Per New Lease

Incremental cost to acquire a new resident that is *not* incurred at renewal. Distinct from make-ready capex.

**Components:**
- Internet Listing Services (Apartments.com, Zillow, Zumper, RentCafe — monthly retainer ÷ leases signed): $100–$250 per lease
- Paid digital marketing (Google Ads, Meta): $100–$300 per lease
- Leasing commission/agent incentive (typically half-month to full-month, amortized): $100–$400 per lease
- Screening/application processing, net of fees: $25–$75 per approved applicant
- Signage, print, community events (allocated): $50–$150 per lease [R4]

| Class/Market | Leasing Cost | Pack Default |
|---|---|---|
| Class A urban/gateway | $1,000 – $1,500 | $1,000 [R4] |
| Class B Sun Belt/primary | $500 – $900 | $700 [R4] |
| Class C tertiary | $400 – $700 | $500 [R4] |
| **All-in typical range** | **$500 – $1,500** | [R4] |

**Zero-at-renewal principle:** The entire leasing cost line item is saved when a resident renews — ILS spend, commission, and application processing do not recur.

---

## Section 3 — Rent-Bump Elasticity at Renewal

At what level of renewal increase does renewal rate collapse? Published empirical data is limited (operators treat this as proprietary), but REIT 10-K disclosures, RealPage analytics, Yardi, and J Turner Research converge on the following directional curve. [R4]

| Renewal Offer | Renewal Rate Response (from ~55% baseline) | Commentary |
|---|---|---|
| 0% (flat) | 65–70% | Retention maximized; loss-leader or genuinely soft market only [R4] |
| +1 to +3% | 60–65% | Historical norm; minimal elasticity [R4] |
| +3 to +5% | 50–60% | Modest elasticity; institutional "sweet spot" in stable/tight markets [R4] |
| +5 to +7% | 40–50% | Noticeable elasticity — each additional 1 point costs ~2–3 pp retention [R4] |
| +7 to +10% | 25–40% | Sharp elasticity; residents actively shopping [R4] |
| +10%+ | 15–25% | Retention crater; only viable with large confirmed loss-to-lease gap [R4] |

**Key heuristics:**
- **Elasticity is non-linear.** The +5–7% band is the typical inflection point where shopping behavior activates (J Turner resident-survey threshold).
- **Loss-to-lease gap caps the bump.** A resident with in-place rent 12% below market tolerates a larger increase than one 2% below market — their outside option is worse.
- **Floor rule: renewal bump ≤ available new-lease trade-out on comparable unit.** Offering renewal at +6% when new-lease trade-out is only +2% invites the resident to confirm they can do better elsewhere. [R4]

### Renewal vs. New-Lease Trade-Out Spread (REIT Disclosures, FY 2024)

Indicative ranges from FY 2024 10-Ks — downstream skills should re-pull current-quarter figures from each REIT's latest supplemental rather than rely on this snapshot.

| REIT | Portfolio | New-Lease Change | Renewal Change | Blended |
|---|---|---|---|---|
| AvalonBay (AVB) | Coastal + expansion | +1 to +2% | +4 to +5% | +2.5 to +3.5% [R4] |
| Essex (ESS) | West Coast | +1 to +3% | +4 to +5% | +2.5 to +4.0% [R4] |
| Equity Residential (EQR) | Coastal/gateway | +1 to +3% | +4 to +5% | +2.5 to +3.5% [R4] |
| Mid-America (MAA) | Sun Belt | -3 to -5% | +4 to +5% | 0 to +1% [R4] |
| Camden (CPT) | Sun Belt | -3 to -5% | +4 to +5% | -0.5 to +1% [R4] |
| UDR | Coastal + diversified | 0 to +2% | +4 to +5% | +2 to +3% [R4] |

**Rule-of-thumb spread:** Expect renewal growth **100–300 bps above new-lease growth** in softening/stable markets. Spread can invert by 200–500 bps in peak-cycle tight markets (2021–2022 pattern — rare and cyclical). [R4]

---

## Section 4 — Tenant Tier Definitions (Renewal Priority Framework)

A pack convention for classifying residents by renewal desirability. Synthesized from R4 retention research; used by the Renewal Decision Analyst skill to calibrate the aggressiveness of renewal offers and contingent-renewal logic.

| Tier | Profile | Treatment | Renewal Posture |
|---|---|---|---|
| **Tier A (Priority Retain)** | On-time pay history; tenure 24+ months; low maintenance-ticket volume; no delinquency in trailing 12 months | Offer renewal first, at the lower end of the rent-bump band; consider non-monetary retention levers (appliance upgrade, interior refresh) [R4] | Preserve — avoid turn |
| **Tier B (Standard Renew)** | On-time pay; tenure 12–24 months; typical maintenance volume; no current delinquency | Offer renewal at market rent-bump band; standard concession structure if any [R4] | Keep at market terms |
| **Tier C (Conditional Renew)** | Pay history mixed but current; any 31–60 day delinquency events in trailing 12 months; elevated maintenance flags | Offer renewal **contingent on balance cure** and pay-plan compliance; do not default to aggressive rent bumps [R4] | Retain only if cure |
| **Tier D (Non-Renew / Decline)** | Current delinquency >60 days, lease violations, chronic late pay, or property damage claims | Decline renewal or offer only as last resort with performance conditions [R4] | Actively turn |

**Application rules:**
- Never run the standard Retain-vs-Replace financial model on Tier D residents — the expected-value math is distorted by forward default probability.
- Tier C residents require the renewal to be structured as a **contingent offer** (cure balance by X date; month-to-month bridge otherwise). Don't force voucher-cure residents through the pure-financial renewal model. [R4]
- Short-tenure renewal (resident on month 10 of first lease) is typically declined by operators regardless of tier: high churn risk, minimal forecast data. [R4]

---

## Section 5 — Retention Rate & Renewal Rate Benchmarks

**Important distinction:**
- **Renewal rate** denominator = only residents offered renewal
- **Retention rate** denominator = all residents in place
- Typical gap = 10–15 percentage points (non-renewed move-outs vs. offered-but-declined). [R4]

### Turnover Rate by Class (Annualized)

| Class / Segment | Turnover Rate | Source/Notes |
|---|---|---|
| Class A urban/coastal | 35–45% | Young-professional, employment-driven, coastal-rent sensitive [R4, AVB/ESS/EQR 10-Ks] |
| Class A/B suburban | 45–55% | Institutional norm [R4] |
| Class B Sun Belt | 50–60% | Higher mobility, more new-construction competition [R4, MAA/CPT 10-Ks] |
| Class C / workforce | 55–70% | Financial stress, job volatility, life-cycle churn [R4] |
| Student / short-hold | 90%+ | 12-month lease = turnover cycle (non-comparable) [R4] |
| **REIT peer group aggregate** | **45–55%** | Below pre-pandemic 55–65% norm (housing affordability + revenue-mgmt moderation) [R4] |

### Renewal Rate Targets (Pack Defaults)

| Level | Rate | Interpretation |
|---|---|---|
| Strong | ≥65% | Top-quartile institutional execution [R4] |
| Stable target | 60% | Pack-default operating target [R4] |
| Floor | 55% | Below this, renewal program is underperforming [R4] |
| Weak | <55% | Investigate pricing, offer timing, condition, competitive set [R4, cross-reference `multifamily-benchmarks.md`] |

### Retention Rate (complement)

Target ≥55% strong, 45–55% average, <45% weak. [R4]

### Loss-to-Lease Convergence at Renewal

- Renewals close roughly 50–60% of the LTL gap; new leases close the full gap on turned units. [R4]
- On a property with 50% annual turnover and 60% renewal rate, ~85–90% of leases re-price within 12 months. A 10% LTL gap typically compresses by 6–8 pp in year 1. [R4]
- **Best practice:** set renewal rent at the midpoint between in-place and market (not at in-place) to prevent LTL accumulation. [R4]

### Seasonality

- **Peak season (Apr–Sep):** Smallest re-lease penalty; operators can lean more aggressive on renewals (replacement lease is strong). [R4]
- **Off-season (Oct–Mar, especially Dec–Feb):** Higher downtime (+5–15 days), weaker new-lease rent (2–5% peak-to-trough swing), higher concession requirements. **Lean less aggressive on renewals.** [R4]
- **Pack seasonal modifier:** reduce recommended renewal bump by 100–150 bps for Nov–Feb expirations; increase by 100 bps for May–Aug expirations where LTL gap supports it. [R4]

---

## Section 6 — Hold Period Analytics Framework

Forward-looking IRR projection is where the hold/sell/refi decision is actually made. The core formulas (IRR, Equity Multiple, DSCR) are defined in `knowledge/underwriting-calc.md` — *cross-reference, do not redefine*.

### Three IRR-to-Date Conventions — Use SI-IRR

| Convention | Definition | Use Case |
|---|---|---|
| **SI-IRR (Since-Inception IRR)** — pack default | Original equity contributions (neg), LP distributions received (pos), current NAV at measurement date as simulated terminal proceed (pos) | ILPA-recommended convention; the only number with a mechanical bridge to "what IRR do I lock if I sell today" [R8, ILPA Performance Template v2.0; NCREIF/PREA] |
| **Realized IRR** (distributions only) | Excludes simulated NAV | Liquidity/distribution-pacing analysis only. On mid-hold asset this is typically near zero or negative — NOT a hold/sell decision input [R8] |
| **TWR (Modified Dietz)** | Neutralizes timing/size of capital flows | Measures *manager skill*, not *LP outcome*. Use only on explicit request for manager-attribution analysis [R8, NCREIF Academy] |

### Interim Distribution Handling — Use XIRR

- Excel `=IRR()` assumes equal spacing and returns periodic rate.
- Excel `=XIRR()` takes explicit dates, returns effective annual rate using 365-day count and annual compounding.
- Multifamily LP distributions are typically quarterly — modeling them as year-end cash flows materially overstates IRR.
- **Published worked example:** same cash-flow series → IRR 13.45% vs. XIRR 16.25% (280 bps spread, timing-convention only). [R8, Adventures in CRE]
- **Pack convention: default to XIRR with actual distribution dates.** Fall back to end-of-quarter if dates missing; flag the assumption. [R8]
- Reinvestment-fallacy caveat: neither IRR nor XIRR mathematically assumes reinvestment at IRR. MIRR is the explicit-reinvestment-rate alternative if needed. [R8]

### Remaining / Marginal IRR — The Decision Lens

The hold/sell/refi comparison collapses to three forward IRRs from today through a common terminal date:

- **IRR-sell-today:** Inception through hypothetical ~90-day disposition close, net of broker commission (1.0–1.5% institutional / 2.0–3.0% middle-market), closing costs, loan prepayment penalty, and taxes (if not 1031'd). [R8]
- **IRR-hold-through-original-plan:** Inception through original underwritten exit, using updated remaining cash flows, forward NOI, and revised exit cap. [R8]
- **IRR-refi-and-hold:** Inception through extended exit, with cash-out refi proceeds as interim distribution, higher debt service, later exit. [R8]

**Core rule:** Sell if IRR-sell-today materially exceeds the *remaining marginal IRR* of continuing to hold. Marginal IRR = forward-only return on the capital left in the deal by not selling, computed from (today's net sale proceeds as initial negative) + (remaining forward cash flows) + (original-plan terminal exit). If marginal IRR < LP alternative-use yield, sell. [R8]

### Exit Cap Rate as Dominant Variable

- 100 bps swing in exit cap → ~540 bps IRR swing (disposition proceeds are 60–80% of total return on typical 5-year hold). [R8]
- Rule of thumb: **+25–75 bps expansion over entry cap**, or +5–10 bps per year of hold as a floor. [R8]
- **Pack convention: sensitivity mandatory.** Base case + ±50 bps + ±100 bps on every scenario. No single-point exit caps permitted in output. [R8]

### Hold-Period Inversion Point

There is an exit-cap level above which extending the hold period stops reducing IRR and starts increasing it (lower terminal discounted more; interim cash compounds in). For heavily levered value-add: typically 6–8 years. Unlevered core: 10+ years. Quantitative rebuttal to the "held five years — time to sell" heuristic. [R8]

---

## Section 7 — Refinance Economics Framework

**All IRR / DSCR / LTV formulas:** see `knowledge/underwriting-calc.md`. This section adds application rules only.

### When Cash-Out Refi Dominates Continued-Hold

A refi is economically preferred when **all three** of these converge:

1. **Rate/spread environment is friendly** — agency all-in rates ≤ existing loan coupon. In 2025–2026 this is rare for pre-2022 fixed-rate paper; more commonly, refi is *defensive* (extending a maturing loan to avoid distressed refi at the maturity wall). [R8, Northmarq; CREFC]
2. **Post-refi DSCR and LTV clear agency gates** (see below).
3. **LP needs liquidity AND tax shield of debt > sale is valuable** — refi proceeds are non-taxable (borrowing, not realization); defers capital gains and §1250 unrecapture. For high-basis-differential assets (long held, deep depreciation), refi preserves step-up-at-death optionality that a sale forecloses. [R8]

### Agency DSCR & LTV Gates (Post-Refi)

| Leverage Tier | DSCR Minimum | LTV Maximum | Notes |
|---|---|---|---|
| High leverage | ≥1.25x | >65% | Agency floor [R8, Freddie Mac Multifamily] |
| Refinance test exemption | ≥1.40x | ≤65% | Loan exempted from refinance test [R8, Freddie Mac] |
| Low leverage | ≥1.55x | ≤55% | Preferred tier [R8, Freddie Mac] |

**DSCR_post-refi** = `Trailing 12-month NOI / New Annual Debt Service`. Any result below 1.25x flagged non-financeable at agency → forces downsize or life-co/bank alternative with different covenants. [R8]

### Cash-Out NPV Test (Conceptual)

Refi cash-out NPV > Sale NPV when:

```
PV(refi proceeds) + PV(remaining levered CFADS at new debt service) + PV(deferred-exit sale proceeds)
    − PV(refi closing costs, 2–4% of new loan)
>
PV(net sale proceeds today, after tax, broker, closing, prepay penalty)
    + PV(reinvestment yield on those proceeds to same terminal date)
```
[R8, DS Property Experts]

### Refi Cost & Rate-Shock Benchmarks

- **Closing costs:** 2–4% of new loan amount. $2M loan = $40k–$80k. [R8]
- **Rate-shock example:** Refi 3.5% → 6.5% coupon on $2M adds ~$44k/yr of debt service. This drag must be offset by NOI growth for refi to be accretive vs. holding existing loan to maturity. [R8]
- **Yield maintenance / defeasance** on existing fixed-rate agency paper typically 5–15% of outstanding balance as a prepayment penalty — must be modeled explicitly; ignoring it is a common underwriting error. [R8]

---

## Section 8 — Disposition Timing Heuristics

Heuristics should be used as **screening filters** that trigger the four-scenario IRR comparison — not as standalone decision rules. Each heuristic has failure modes.

| Heuristic | Logic | Works When | Fails When |
|---|---|---|---|
| **Peak-NOI** | Sell when NOI stabilizes at business-plan target; further growth tapers to organic market rate [R8] | After value-add execution; T-3 and T-12 NOI converge on plan, not macro-driven | Peak is temporary (concession burn-off, one-time tax refund, anomalous expense control that reverts). Gate with Timing-vs-Permanent variance classification per `_taxonomy-seed.md` §3 [R8] |
| **Cycle-top** | Sell when cap compression outpaces NOI growth; price-per-unit near historical peak multiple [R8] | Owner has credible cycle view AND can hold cash / redeploy into another cycle's trough | Cycle-timing is notoriously hard. Pre-2022 sellers held into rate hikes and gave back gains; post-2023 sellers at the bottom missed the 2024–2025 spread recovery [R8] |
| **Value-add-complete** | Sell once renovation capex + lease-up done; rents marked-to-market; risk profile has changed [R8] | Cleanest analytically. Value-add sponsor's LP base may differ in risk tolerance from core buyer's LP base | Post-stabilization market cap is lower than expected (proceeds strong but redeployment into another value-add deal is costly — fewer opportunities, higher friction) [R8] |
| **Held-5-years** | Quasi-default driven by LP fund life and waterfall structures (NOT tax-driven — §1250 does not change past 1-year hold) [R8] | Aligns with promote tiers and LP liquidity expectations | Mechanical; ignores marginal-IRR analysis; inversion point shows longer holds frequently outperform on IRR [R8] |
| **REIT practice: strategic-fit + market-conditions** | AVB and ESS disclose NO fixed hold-period policy. Dispositions triggered by (i) asset no longer fits long-term strategy, OR (ii) pricing is favorable. Proceeds recycle into expansion-region development/acquisition [R8, AvalonBay 2024 10-K; Essex 2024 10-K] | REIT-scale portfolio with redeployment infrastructure | Small-sponsor single-asset LP deals lack REIT redeployment infrastructure; heuristic must be adapted [R8] |

### Four-Scenario Comparison Matrix (Pack Standard)

Every hold/sell/refi analysis must produce:

| Scenario | Definition | Key Metrics |
|---|---|---|
| **Hold (base case)** | Continue original plan through original exit; current debt unchanged | IRR-inception-to-projected-exit; Equity Multiple; remaining years; exit cap ±50/±100 bps sensitivity [R8] |
| **Refi + Hold** | Cash-out refi at market terms; distribute net proceeds; extended exit typically +3–5 yrs | IRR (with refi distribution as interim CF); Equity Multiple; DSCR_post-refi; marginal IRR on trapped equity; rate ±50 bps and exit cap ±50 bps sensitivity [R8] |
| **Sell at Current** | Disposition 60–120 days; assume taxable event | IRR-sell-today; after-tax IRR; after-tax Equity Multiple; net per LP; waterfall promote calc [R8] |
| **Sell at Stabilization** | Complete remaining value-add / lease-up; dispose at projected stabilized pricing 12–24 months forward | IRR-inception-to-stabilized-sale; marginal IRR from today to stabilized; lease-up execution risk and exit cap sensitivity [R8] |

**Ranking rule:** Rank by LP IRR AND LP Equity Multiple. If rankings disagree, flag — the spread is a direct measure of LP vs. GP misalignment driven by promote structure (see Edge Cases below). [R8]

### Transaction-Volume Seasonality (Process Timing)

- Q4 is the highest CRE transaction-volume quarter; December is the single biggest month. Q4 2024: $108.5B (+33.6% QoQ). Q4 2025: $179.9B (+20.7% QoQ). [R8, Altus Group]
- Q1 is the structural low (pipelines exhausted by year-end closings). [R8]
- **Process-timing implication:** launch marketed process late Q2 to close Q4 → aligns with peak buyer demand. Q3-launch / Q1-close is the worst combination. [R8, MIT SRE]
- **Use for process timing, not go/no-go.** Seasonal volume is a distribution property, not a forecast for an individual asset. [R8]

---

## Section 9 — Capital Markets Snapshot (2024–2026)

> **SNAPSHOT — NOT LIVE DATA.** These benchmarks reflect the 2024–2026 rate regime as of Q1 2026. Rates, spreads, and agency policy shift frequently; downstream skills must re-verify before relying on specific figures. Figures below are calibration reference only.

### Treasury & Agency (2024–2026 Regime)

| Metric | Snapshot Value / Range | Source |
|---|---|---|
| 10-Year Treasury | ~3.85%–4.5% range; MBA forecast ~4.2% 2026 average | [R8, MBA; Northmarq] |
| Agency multifamily all-in rates (prime, moderate leverage) | Low-to-mid 5% | [R8, Freddie Mac; Select Commercial] |
| Agency 10-year fixed range | 5.7%–6.8% depending on LTV / coverage | [R8, Northmarq] |
| Long-run Treasury average (1990–2025) | ~5.85% | Rate-regime context [R8, MBA] |
| Post-Fed-cut behavior | Last two cuts saw the 10Y *rise* immediately — refinance off long end, not Fed funds | [R8, Northmarq] |

### CMBS & Conduit Spreads

| Metric | Snapshot Value | Source |
|---|---|---|
| Conduit AAA spread | ~78 bps | [R8, CREFC] |
| Conduit AA spread | ~145 bps | [R8, CREFC] |
| Conduit BBB- spread | ~450 bps | [R8, CREFC] |
| Multifamily conduit spread over Treasury | ~152 bps (down from 166 bps mid-2025) | [R8, CREFC] |
| Multifamily as % of conduit collateral | ~24% | [R8, CREFC] |
| Agency CMBS YTD issuance (through Dec 2025) | $147.9B | [R8, CREFC] |

### Delinquency & Credit Stress

- CMBS total delinquency: **7.23% July 2025** (+10 bps MoM), multifamily drove +24 bps of the increase. 2023-vintage multifamily conduit loans disproportionately stressed. [R8, Trepp via CREFC]
- Distressed-hold sellers face sharpened refi-vs-sell pressure — less negotiating leverage. [R8]

### 2026 Maturity Wall

- **$875B** of commercial mortgages mature in 2026 (17% of ~$5T outstanding). [R8, MBA]
- Only **$39B (4%)** is agency multifamily — majority of the wall is bank (~$396B), CMBS/CLO (~$200B), life-co (~$76B). [R8, MBA]
- Owners holding bank or CMBS paper approaching maturity have sharper refi-vs-sell pressure than owners holding agency paper. [R8]

### FHFA 2026 Agency Loan Purchase Caps

- **$88B each** for Fannie and Freddie in 2026 (+20% vs. 2025).
- **50% mission-driven allocation.**
- **Workforce housing excluded from caps** → mission-driven assets have structurally larger allocation headroom and better refi optionality than market-rate product. [R8, FHFA]

### Cap-Rate-to-Treasury Spread (Macro Context)

- 1991–2025 long-run average: **314 bps.**
- Historical range: 58 bps (June 2007 froth) to 495 bps (December 2009 distress).
- Current multifamily cap spreads near the long-run average → neither froth nor distress at the macro level. [R8, Northmarq]

### Tax Framework (Citation Only — NOT Tax Advice)

Skills must reference but not opine on:
- **§1031 like-kind exchange:** Defers capital gains + §1250/§1245 recapture if: replacement property ≥ relinquished value, all net equity reinvested, debt replaced (or matched with cash). 45-day ID / 180-day close. QI required. [R8, Accruit]
- **§1250 unrecaptured gain:** Depreciation on §1250 real property recaptured at **flat 25% federal rate.** Not offset by prior capital losses the same way ordinary gains are. [R8]
- **§1245 bonus-depreciation recapture trap:** Cost-segregation-accelerated depreciation into §1245 personal-property buckets (appliances, carpet, parking-lot striping) recaptures at **ordinary-income rates up to 37%.** A 1031 that does not replace like-kind §1245 property still triggers recapture on those buckets. [R8, R.E. Cost Seg]
- **Step-up at death:** Holding until death eliminates deferred tax liability via basis step-up. Primary estate-planning argument for refi-over-sell on highly appreciated, depreciation-deep assets. [R8]
- **State taxes:** CA, NY, OR, and other high-tax states add 8–13% on federal capital-gains number. Materially affects sell-vs-hold math in those geographies. [R8]

**Rule:** cite the framework; require user/sponsor to engage qualified CPA/tax counsel for actual numbers. Do not produce a specific tax figure.

---

## Edge Cases & Red Flags (Consolidated)

### Renewal-Decision Edge Cases [R4]

- **Short-tenure renewal** (first-lease month 10): typically declined; treat conservatively, minimal forecast data.
- **Long-tenure + large LTL gap** (4+ years, 15%+ LTL): classic anchored-renewal problem. Options: stepped 2-cycle correction, upgrade-concession to justify larger bump, or accept-the-turn. Flag both for operator choice.
- **Section 8 / voucher residents:** payment standard is PHA-set, not negotiated; resident portion is income-based. Exclude from standard framework unless dedicated voucher logic exists.
- **Unresolved delinquency:** renewal must be **contingent on balance cure** (Tier C treatment).
- **Unit scheduled for value-add renovation at next move-out:** only the incremental make-ready-over-renovation capex enters Turn Cost. Skill should branch.
- **Compressed-spread peak markets** (new-lease > renewal growth): operator may rationally push renewals aggressively — replacement lease more valuable than retention. Requires current new-lease trade-out data.
- **Winter lease expiration, non-negotiable timing** (job relocation): retention side collapses to zero; only lever is minimizing turn cost, not pushing renewal rent.

### Hold/Sell/Refi Edge Cases [R8]

- **Distressed refi:** computed DSCR at 75% LTV prevailing-rate debt <1.10x is a distress signal, not a refi opportunity. Auto-flag.
- **Yield maintenance / defeasance:** 5–15% of outstanding balance as prepayment penalty on fixed-rate agency. Ignoring it is a common modeling error.
- **Assumable-debt value as disposition accelerant:** pre-2022 below-market assumable loans can add 100–300 bps to effective sale price by enabling buyer leverage. Adjust exit cap.
- **LP fund-life expiration:** mechanics may force sale regardless of IRR math — flag early.
- **Concentration-driven sale:** single asset >25% of LP portfolio NAV may trigger sale for diversification even when IRR favors hold.
- **Tax lock-up from recent §1031:** property acquired via §1031 within past 2 years carries forward original depreciation/basis. Non-§1031 sale triggers current + previously-deferred gain. Deep §1031 chains can create 60–70% effective tax rates.
- **Prior cost-seg / §1245 recapture risk:** must be disclosed in skill intake (ordinary-rate recapture up to 37%).
- **Waterfall-hurdle-just-cleared:** if IRR-sell-today is within 50–100 bps of a promote-tier breakpoint AND IRR-marginal-hold is only 100–200 bps below IRR-sell-today, GP has structural incentive to sell that LP reviewer should scrutinize. The standard multi-tier waterfall (e.g., 80/20 to 8%, 70/30 to 12%, 50/50 thereafter) front-loads GP economics via IRR. Flag and require Equity Multiple as co-primary ranking metric. [R8, Breneman Capital]
- **Floating-rate debt with expiring rate cap:** a meaningfully in-the-money cap expiring within 12 months is a hidden time-bomb — post-expiration debt service can spike 100–300 bps overnight. Skill must ingest rate-cap expiry + strike, not just current debt terms.

---

## Cross-Reference Map

| Concept | Defined In | Referenced Here For |
|---|---|---|
| IRR / XIRR mechanics | `knowledge/underwriting-calc.md` §Return Metrics | Hold/sell forward-IRR framework (Section 6) [R8] |
| Equity Multiple | `knowledge/underwriting-calc.md` §Return Metrics | Co-primary ranking metric alongside IRR (Section 8) [R8] |
| Cap Rate | `knowledge/underwriting-calc.md` §Valuation Metrics | Exit-cap sensitivity (Section 6) [R8] |
| DSCR / LTV / Debt Yield | `knowledge/underwriting-calc.md` §Debt Metrics | Refi gates (Section 7) [R8] |
| Loss-to-Lease | `knowledge/underwriting-calc.md` §Multifamily Income Analysis | Renewal LTL convergence (Section 5) [R4] |
| Cap rate ranges, OpEx benchmarks | `knowledge/multifamily-benchmarks.md` | Exit-cap derivation + turn-cost submarket adjustment [R4, R8] |
| Cost-of-living / catastrophe / vintage multipliers | `knowledge/multifamily-benchmarks.md` §Submarket Adjustment Protocol | Applied to unit-turn capex and leasing-cost ranges (Section 2) [R4] |
| Canonical rent definitions, OpEx line items, variance classification | `research/asset-management/_taxonomy-seed.md` | Timing-vs-Permanent gate on peak-NOI heuristic (Section 8) [R8] |

---

## Citation Key

- **[R4]** = `research/asset-management/renewal-decision-analyst-research.md` (Renewal Decision Analyst research, sourced from AVB/ESS/EQR/MAA/CPT/UDR FY 2024 10-Ks, NMHC, NAA, IREM, RealPage, Yardi Matrix, ALN, J Turner, RentCafe, ResMan, Multifamily Executive)
- **[R8]** = `research/asset-management/hold-sell-refi-analyst-research.md` (Hold/Sell/Refi Analyst research, sourced from ILPA, NCREIF/PREA, INREV, AvalonBay and Essex 2024 10-Ks, Freddie Mac Multifamily, FHFA, MBA, CREFC, Trepp, Northmarq, Altus Group, MIT SRE, Nareit, Adventures in CRE, Wall Street Prep, Accruit, R.E. Cost Seg, Corecast, Bonfire Capital, IPG, Breneman Capital, Trinity Real Estate, DS Property Experts)

---

*Last updated: January 2026. Capital-markets figures in Section 9 are a 2024–2026 snapshot and should be re-verified against current sources before use in live decisions. Benchmarks should be validated against current local market data and the most recent REIT supplementals for each specific property.*
