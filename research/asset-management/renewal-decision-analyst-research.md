# Renewal Decision Analyst Research

## Purpose

- Supports `skills/asset-management/renewal-decision-analyst.md` (Asset Management pack v1.3.0)
- Intended for multifamily asset managers, revenue managers, and on-site leadership weighing the economics of a renewal offer against the likely cost of letting a unit turn
- Produces the framework, benchmarks, and decision math for:
  - Setting renewal rent-bump targets by market, class, season, and loss-to-lease gap
  - Comparing the all-in cost of a retained resident (concession at renewal, below-market rent) to the all-in cost of a turn (downtime, unit-turn capex, leasing cost, new-lease concession)
  - Calibrating the rent-bump elasticity curve — the point at which renewal offers start pushing renewal rate below break-even vs. turning the unit

## U.S.-Only Assumptions

- Conventional stabilized multifamily (5+ unit), market-rate (non-LIHTC, non-HUD)
- U.S. market, post-2023 supply-normalization environment — Sun Belt softness through 2025, coastal/Midwest resilience, renewals running materially above new-lease growth at most public REITs
- Renewal decisions made at the **unit-resident level**, not at the property-lease-up level (lease-up absorption benchmarks are scope for R5 and are intentionally excluded here)
- Excludes ancillary-income / OpEx-reduction levers (R7 scope) and value-add renovation capex treated as a separate renovation program (R6 scope) — only the **make-ready unit-turn capex** required to put a vacated unit back on the market is in scope
- Revenue-management context: most institutional operators use algorithmic pricing (RealPage AIRM / LRO, Yardi RevenueIQ) for both new-lease and renewal pricing; this research assumes the analyst may override or stress-test those outputs

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|--------|-----------|-----|--------------|-------------|-------------|-------|
| AvalonBay Communities Form 10-K (FY 2024) | AvalonBay Communities / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000915912&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Like-term effective rent change on renewal vs new-move-in; turnover rate; Same-Store operating metrics |
| Essex Property Trust Form 10-K (FY 2024) and Q4 2024 Supplemental | Essex Property Trust / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000920522&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Financial occupancy, turnover, renewal vs new-lease rent change (West Coast portfolio) |
| Camden Property Trust Q4 2024 Supplemental Financial Information | Camden Property Trust / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000906345&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Turnover rate (Sun Belt), renewal rate, renewal vs new-lease effective rent growth |
| Equity Residential 2024 Annual Report / 10-K | Equity Residential / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000906107&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Coastal/urban renewal dynamics; turnover; resident retention data |
| Mid-America Apartment Communities (MAA) 2024 Annual Report | MAA / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000912595&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Sun Belt new-lease pricing under elevated supply; renewal vs new-lease spread; resident retention |
| UDR, Inc. 2024 Annual Report and Q4 Supplemental | UDR / SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000074260&type=10-K | 2025-02 | 2026-04-24 | Primary public filing (Tier 1) | Effective blended rent change, new-lease vs renewal, annualized turnover |
| National Multifamily Housing Council (NMHC) Quarterly Apartment Markets | NMHC | https://www.nmhc.org/research-insight/quarterly-survey/ | 2026-Q1 | 2026-04-24 | Industry trade association (Tier 1) | Trends in renewal rates, turnover, leasing conditions |
| National Apartment Association — "From Momentum to Management" 2024 Survey | NAA | https://naahq.org/news/momentum-management-navigating-elevated-costs-constrained-operating-environment | 2025 | 2026-04-24 | Industry trade association (Tier 1) | Make-ready cost, turnover cost, per-unit operating benchmarks |
| Institute of Real Estate Management — Income/Expense IQ | IREM | https://www.irem.org/file%20library/globalnavigation/learning/tools/irem-income-expense-iq-national-summary-23-final.pdf | 2024 | 2026-04-24 | Industry trade association (Tier 1) | Leasing expense line items (turnover, make-ready, advertising, commissions) |
| RealPage — "Multifamily Renewal Rent Growth" analytics | RealPage | https://www.realpage.com/analytics/ | 2025-2026 | 2026-04-24 | Revenue-management vendor research (Tier 2) | Renewal rent change vs new-lease rent change spread; retention elasticity |
| Yardi Matrix — Multifamily National Reports | Yardi Matrix | https://www.yardimatrix.com/Publications | 2025-2026 | 2026-04-24 | Data vendor research (Tier 2) | National asking rent, renewal vs new-lease trade-out, market-level retention |
| ALN Apartment Data — National Occupancy and Leasing | ALN Apartment Data | https://www.alndata.com/ | 2025-2026 | 2026-04-24 | Data vendor research (Tier 2) | Retention rate, days vacant, market-level leasing metrics |
| J Turner Research — Multifamily Renewal & Retention Studies | J Turner Research | https://www.jturnerresearch.com/ | 2024-2025 | 2026-04-24 | Industry survey firm (Tier 2) | Reasons-for-move-out, renewal-offer timing, resident-satisfaction driver analysis |
| RentCafe / Yardi — Renter Intent & Retention Survey | RentCafe (Yardi) | https://www.rentcafe.com/blog/rental-market/ | 2024-2025 | 2026-04-24 | Industry research (Tier 2) | Resident reasons-to-stay and reasons-to-leave |
| ResMan / Zego — Make-Ready Benchmark Blog Series | ResMan | https://myresman.com/resources/ | 2024-2025 | 2026-04-24 | Property-management platform (Tier 3) | Make-ready cycle time; $/turn by class |
| Multifamily Executive — "The True Cost of Resident Turnover" | Multifamily Executive magazine | https://www.multifamilyexecutive.com/ | 2024 | 2026-04-24 | Industry trade publication (Tier 3) | All-in turnover cost framework ($3,500-$5,000 aggregate) |
| Repo KB — `knowledge/multifamily-benchmarks.md` | This repo | — | 2026-01 | 2026-04-24 | Internal authoritative | Turnover cost, renewal metrics, days-vacant, cost-of-living and vintage multipliers |
| Repo KB — `knowledge/underwriting-calc.md` | This repo | — | 2026-01 | 2026-04-24 | Internal authoritative | Loss-to-lease, concession, effective rent formulas |
| Repo — `research/asset-management/_taxonomy-seed.md` | This repo (Phase 0a) | — | 2026-04 | 2026-04-24 | Internal authoritative | Canonical rent definitions, OpEx line items, KPIs |

**Tier tally: 9 Tier 1 (6 REIT 10-Ks + NMHC + NAA + IREM), 4 Tier 2 (RealPage, Yardi Matrix, ALN, J Turner), 2 Tier 3 (ResMan, MFE), 3 repo-internal = 18 total, 13 Tier 1/2 external.** Gate (≥10 total, ≥6 Tier 1/2) met.

## Key Findings

### 1. Turnover Rate Benchmarks — Class and Region

- Market-rate multifamily turnover has settled into a **roughly 45–55% annualized** range across the public-REIT peer group, materially below the **55–65%** pre-pandemic long-run norm NMHC historically reported. Two structural drivers: (a) weak for-sale housing affordability that keeps renters in place longer, and (b) revenue-management systems dampening aggressive renewal increases that historically drove voluntary move-outs.
- Public REIT disclosures show a coastal-to-Sun-Belt gradient: coastal REITs (AVB, ESS, EQR) report turnover in the **low-40s**, Sun Belt peers (MAA, CPT) report **mid-50s to low-60s** — consistent with higher housing mobility and more new-construction competition in Sun Belt submarkets [AVB, ESS, EQR, MAA, CPT 10-Ks].
- Repo benchmark (`multifamily-benchmarks.md`): best-practice turnover <40%, average 40–55%, above 55% flagged as weak. These REIT-derived ranges are consistent with that framework and are the appropriate benchmark for institutional-quality property analysis.
- **Class gradient** (repo benchmark, cross-checked against REIT disclosures and NAA survey):
  - Class A urban/coastal: 35–45% (skews young professional, employment-driven, price-sensitive to coastal rent levels)
  - Class A/B suburban: 45–55% (the institutional norm)
  - Class C / workforce: 55–70% (higher financial stress, job volatility, family-life-cycle events)
  - Student / short-hold product: 90%+ (non-comparable — 12-month lease cycle ~= turnover cycle)
- **Retention rate** (complement of turnover): target ≥55% (strong), 45–55% (average), <45% (weak). Retention ≠ renewal rate. Renewal rate denominator is only residents offered renewal; retention denominator is all residents in place. The gap is typically 10–15 percentage points (non-renewed residents who moved out vs. offered-but-declined residents).

### 2. Downtime / Days-Vacant Per Turn

- **Institutional benchmark: 10–30 days between move-out and new-lease move-in** for stabilized market-rate properties. Breakdown:
  - Make-ready cycle time: 5–10 days (paint, flooring, cleaning, punch)
  - Marketing/leasing cycle time: 5–20 days (application, approval, lease signing, move-in scheduling)
- Repo benchmark: strong 15–25 days, average 25–40 days, weak 40+ days. REIT disclosures (AVB, ESS) routinely cite 20–30 day averages in supplementals.
- **Class and market gradient**:
  - Class A urban/primary market: 10–20 days (deeper demand pool, faster application flow)
  - Class B suburban/primary: 20–35 days
  - Class C / tertiary market: 25–45 days
  - Winter turns (Dec–Feb) add roughly **5–15 days** vs. peak season (Apr–Sep) — seasonal leasing friction
- **Downtime rent loss formula**: Days Vacant × (Monthly Rent / 30). On a $1,800/mo unit at 25 days vacancy = $1,500 in lost rent; at 40 days = $2,400. This frequently exceeds the unit-turn capex itself.

### 3. Unit-Turn Capex — Make-Ready Scope and Cost

- **Scope (pack definition, mapped to IREM I/E IQ "Leasing Expenses — Make-Ready" sub-category)**:
  - Paint (full or touch-up based on wear): 40–60% of typical turn cost
  - Flooring — carpet clean, carpet replacement (3–7 year replacement cycle), or LVP patch/replace: 15–30%
  - Appliance prorate (replace-as-needed amortized over turns): 5–10%
  - Make-ready cleaning (deep clean, carpet extract): 10–15%
  - Minor repairs (fixtures, hardware, punch-list): 5–10%
  - Does NOT include value-add renovation capex (classic-to-premium upgrade) — that sits in the value-add program (R6 scope)
- **Cost per turn by class** (consistent with repo `multifamily-benchmarks.md` Operating Expense Benchmarks and triangulated against NAA 2024 survey data and REIT supplementals):
  - Class A (higher finish — quartz, LVP, stainless appliances): **$2,500 – $3,500 per turn**, exceptional cases to $4,500 for heavy wear or luxury finish replacement
  - Class B (mid-finish — laminate counters or mid-grade quartz, LVP or carpet-heavy, mid-grade appliances): **$1,800 – $2,700 per turn**
  - Class C (builder-grade — laminate, vinyl, older appliances): **$1,200 – $2,000 per turn**
- **Cost-of-living adjustment**: Apply the `multifamily-benchmarks.md` Tier 1 turnover multiplier of **1.30x–1.70x** for gateway metros (NYC, SF, Boston, DC, LA). A Class B Sun Belt turn at $2,200 translates to $2,860–$3,740 in coastal Tier 1.
- **Vintage adjustment**: Older product (pre-1990) frequently requires higher-frequency flooring replacement and more punch-list work; pack default multiplier **1.10x–1.25x** on turn cost for pre-1990 vintage.

### 4. Leasing Cost Per New Lease

The incremental cost to acquire a new resident that would NOT be incurred if the unit were retained through renewal. Distinct from make-ready capex.

- **Components**:
  - Internet Listing Service (ILS) allocation: $100–$250 per new lease on a per-lease-acquired basis (properties pay a monthly ILS retainer to Apartments.com, Zillow, Zumper, RentCafe; divide by new leases signed to get per-lease cost)
  - Paid digital marketing (Google Ads, Facebook, Meta): $100–$300 per lease
  - Leasing commission / leasing-agent incentive: $100–$400 per new lease (typical: half-month to full-month in incentive pools, amortized across leases signed per agent)
  - Screening / application processing net of fees collected: $25–$75 per approved applicant
  - Signage, print, community events (allocated): $50–$150 per new lease
- **All-in typical range**: **$500–$1,500 per new lease** for stabilized market-rate properties. Class A urban gateway properties frequently run $1,000–$1,500; Class B Sun Belt runs $500–$900; Class C tertiary $400–$700.
- **Zero-cost-at-renewal comparison**: The renewal decision should treat leasing-cost-per-new-lease as a direct saving on renewal — the resident stays without ILS spend, without commission, without application processing.

### 5. Rent-Bump Elasticity — Renewal vs New Lease

Public REIT 10-K and supplemental disclosures are the most reliable source for renewal-vs-new-lease trade-out, because they report both in comparable units.

**Recent peer-group disclosures (FY 2024 10-Ks and Q4 supplementals)**:

| REIT | Portfolio | FY 2024 New-Lease Change | FY 2024 Renewal Change | Blended |
|---|---|---|---|---|
| AvalonBay (AVB) | Coastal + expansion markets | +1–2% | +4–5% | +2.5–3.5% |
| Essex (ESS) | West Coast | +1–3% | +4–5% | +2.5–4.0% |
| Equity Residential (EQR) | Coastal urban/gateway | +1–3% | +4–5% | +2.5–3.5% |
| Mid-America (MAA) | Sun Belt | -3 to -5% | +4–5% | 0 to +1% |
| Camden (CPT) | Sun Belt | -3 to -5% | +4–5% | -0.5 to +1% |
| UDR | Coastal + diversified | +0–2% | +4–5% | +2–3% |

*Figures are rounded indicative ranges from each REIT's FY 2024 Operating and Financial Review section; downstream skill should re-pull the exact current-quarter figure from each REIT's most recent supplemental at run-time rather than rely on a stale benchmark.*

**Key pattern — the renewal/new-lease spread**:
- In **softening markets** (Sun Belt 2024–2025), renewal growth held at +4–5% while new-lease growth went **negative** (-3 to -5%). Operators protected renewals aggressively because replacement-lease economics were poor — a weak new lease forgoes the full renewal bump AND imposes turn cost AND imposes downtime AND imposes leasing cost. Rational response: push renewals, accept soft new leases, minimize turns.
- In **tight markets** (coastal 2024–2025), renewal growth ran +4–5% and new-lease growth +1–3%. Spread narrower because replacement-lease economics are decent.
- In **peak-cycle pricing** (2021–2022), new-lease growth exceeded renewal growth at most operators (new-lease +10–20%, renewal +5–10%) — the "gain-to-sell" dynamic where a voluntary move-out is economically attractive to the owner. Rare and cyclical.
- **Rule-of-thumb spread**: Expect renewal growth **100–300 bps above new-lease growth** in softening or stable markets; the spread can invert by 200–500 bps in tight or peak markets.

### 6. Retention-Cost vs Turnover-Cost Calculation

The core decision framework for the Renewal Decision Analyst skill.

**Cost of Retaining (Renewal)** — per unit, current decision cycle:
```
Retention Cost = Renewal Concession $ (if any)
              + (Market Rent − Renewal Rent) × 12   [opportunity cost of renewing below market]
              + de minimis administrative cost (~$25/renewal)
```

**Cost of Turning** — per unit:
```
Turn Cost = Unit-Turn CapEx ($1,200–$3,500 by class)
         + Downtime Rent Loss (Days Vacant × Monthly Rent / 30)
         + Leasing Cost Per New Lease ($500–$1,500)
         + New-Lease Concession (annualized $ value)
         − (New-Lease Rent − Old In-Place Rent) × 12   [replacement-lease rent pickup, if positive]
```

**Decision rule**: Offer renewal at a rent level where **Retention Cost < Turn Cost**, subject to an upper bound where the renewal rate itself falls below a threshold that makes the expected-value calculation unfavorable (see elasticity curve in Finding 7).

**Illustrative example — Class B suburban, softening market**:
- In-place rent $1,800/mo. Market rent $1,850/mo. Unit-turn capex $2,200. Downtime 28 days → $1,680 rent loss. Leasing cost $700. Renewal offer at $1,854 (+3%). New-lease rent achievable at $1,800 (-3% trade-out). No concessions either way.
  - **Retention Cost** = 0 + ($1,850 − $1,854) × 12 + $25 ≈ −$23 (effectively zero, renewal at or slightly above market)
  - **Turn Cost** = $2,200 + $1,680 + $700 + 0 − ($1,800 − $1,800) × 12 = **$4,580**
  - **Favors renewal by ~$4,600**, even at a +3% renewal bump.
- If renewal is pushed to +8% ($1,944), and data suggests renewal rate drops from 55% to 35% at that level (elasticity in Finding 7), expected value must weight the renewal-rate delta. At 20 pp lower renewal probability × $4,580 avoided turn cost ≈ $916 in forgone value vs. only (8% − 3%) × $1,800 × 12 × 55% = $594 in higher rent retained. **Pushing to +8% is value-destroying** in this scenario.

### 7. Renewal Rent-Bump Elasticity Curve

At what level of renewal increase does renewal rate collapse? Published empirical data is limited (operators treat this as proprietary), but RealPage, Yardi, and J Turner research converge on the following directional pattern [RealPage analytics; J Turner resident surveys]:

| Renewal Offer | Typical Renewal Rate Response (from ~55% baseline) | Commentary |
|---|---|---|
| 0% (flat) | 65–70% | Retention maximized; operators use only in genuinely soft markets or loss-leader scenarios |
| +1 to +3% | 60–65% | Historical norm; minimal elasticity |
| +3 to +5% | 50–60% | Modest elasticity; the institutional "sweet spot" in stable-to-tight markets |
| +5 to +7% | 40–50% | Noticeable elasticity — each additional 1 point of rent costs ~2–3 pp of retention |
| +7 to +10% | 25–40% | Sharp elasticity; residents begin actively shopping |
| +10%+ | 15–25% | Retention crater; most residents shop and many leave. Only viable where loss-to-lease gap is very large AND market rents are confirmed. |

**Key decision heuristics from survey and analytics research**:
- **Renewal-rate sensitivity is non-linear**. The +5–7% band is often the inflection point where resident shopping behavior activates — aligned with the "noticeable rent increase" threshold J Turner Research identifies in resident-survey work.
- **Loss-to-lease gap caps the renewal bump**. A resident whose in-place rent is 12% below market will tolerate a larger renewal increase (because leaving and re-leasing elsewhere still costs more than staying) than a resident whose rent is 2% below market.
- **Renewal bump ≤ available new-lease trade-out for comparable unit** is the floor rule. If a new lease on the same unit would only achieve +2%, offering the renewing resident +6% invites the resident to shop and confirm they can do better elsewhere — accelerating departure.

### 8. Loss-to-Lease Convergence at Renewal

- Loss-to-lease (market minus in-place, % of market — per taxonomy seed) closes most aggressively at **renewal events**, not at organic market movement. A 10% LTL gap at a property cannot close without lease events; renewals close roughly 50–60% of the gap, new leases close the full gap on the turned units.
- Convergence speed: On a property with 50% annual turnover and 60% renewal rate, roughly **85–90% of leases re-price within 12 months**. A 10% LTL gap typically compresses by **6–8 percentage points in year 1**, subject to renewal and new-lease trade-out levels.
- Renewals that substantially lag market rent **anchor the property's LTL gap**. Institutional best practice is to set renewal rent at the midpoint between in-place and market, not at in-place, to prevent LTL accumulation.

### 9. Seasonality of Renewal Offers

- **Peak leasing season** (April–September) is the highest-demand window for re-leasing. Residents who move during peak season take the smallest penalty (they can find a comparable unit easily); operators also can re-lease quickly (low downtime, high new-lease pricing power). Renewal offers during peak season can lean **more aggressive** — the operator is relatively willing to lose the resident.
- **Off-season** (October–March, especially December–February) is the opposite. Winter turns carry:
  - Higher downtime (+5–15 days above summer baseline)
  - Weaker new-lease rent (peak-to-trough new-lease rent swing of 2–5% in many markets)
  - Higher concession requirements to fill winter vacancies
  - Operators should lean **less aggressive on renewals** during winter months — a retained resident is worth more when the replacement lease is worth less.
- **Lease-stagger best practice**: Repo `multifamily-benchmarks.md` already notes the principle — offer 14-month or 16-month lease terms to shift winter expirations into favorable months. This converts the seasonal asymmetry into an upfront structural improvement.

### 10. Retention-Incentive Programs

- **Concession-at-renewal** structures (e.g., $500 renewal bonus, one-month free, amenity upgrades) are less value-destructive than rent reductions because:
  - They are one-time, not perpetuating into the rent base
  - They preserve market-rent comparability for the property
  - They avoid anchoring the resident's expectation of a below-market rate going forward
- **Rent-reduction renewals** (offering a renewal below in-place rent) are generally only rational in steeply softening markets where new-lease economics are worse than the renewal rent even post-reduction. Treat as last-resort.
- **Non-monetary retention levers** (J Turner, RentCafe surveys): appliance upgrades, interior refresh at renewal, assigned parking, storage allocation, carpet cleaning, minor finish upgrades. These often deliver the same retention lift as $300–$600 in cash concession at lower out-of-pocket cost because some of the capex doubles as unit-level value preservation.

## Benchmark and Formula Decisions

- **Use a unit-level decision model**, not a property-level assumption. Each renewal decision has its own economics (current rent, market rent, unit class, finish condition, likely downtime).
- **Canonical retention-vs-turn cost formula** (for skill output):
  ```
  Retain-vs-Turn Delta = Turn Cost − Retention Cost
  Turn Cost = Unit Turn CapEx + (Days Vacant × Monthly Rent / 30)
            + Leasing Cost Per New Lease + New-Lease Concession
            − (New-Lease Rent − Current Rent) × 12
  Retention Cost = Renewal Concession + (Market Rent − Renewal Rent) × 12 + $25
  If Delta > 0 → Renewal is preferred at proposed level.
  ```
- **Pack default benchmark ranges for skill**:
  - Turn capex: Class A $3,000, Class B $2,200, Class C $1,500 (midpoints)
  - Days vacant: Class A 15, Class B 25, Class C 35 (primary-market midpoints)
  - Leasing cost: Class A $1,000, Class B $700, Class C $500
  - Target renewal rate: 55% (floor), 60% (stable target), 65%+ (strong)
- **Decision-output structure** required of the skill:
  - Unit-level recommendation: offered renewal rent, expected renewal probability, expected retention cost, expected turn cost, recommended action
  - Aggregate property-level renewal-cycle summary: total expected retention, total expected turn cost, loss-to-lease closure projection
- **Seasonal modifier**: reduce recommended renewal bump by 100–150 bps for off-season (Nov–Feb) expirations; increase by 100 bps for peak-season (May–Aug) expirations where loss-to-lease gap supports it.

## Conflicting Source Resolution

- **REIT vs. broad-market turnover figures**: Public REIT portfolios (40–55% turnover) are skewed toward institutional-quality, well-located, well-managed product. Smaller operators and Class C product can run 60–75%. Skill should accept operator-specific turnover inputs and not default to REIT-range figures for sub-institutional product. Use repo benchmark ranges when operator data unavailable.
- **Renewal-rent-change methodology differences across REITs**: AVB reports "like-term effective rent change," MAA reports "effective blended rent growth," others use variants. The numerical figures are directionally comparable but not literally apples-to-apples. Use ranges, not point estimates, and cite the specific REIT methodology when quoted.
- **RealPage/Yardi elasticity research vs. academic literature**: Vendor research is more timely and more property-level specific; academic literature (where it exists) is more methodologically rigorous but dated. Prefer vendor data for operating decisions, supplemented by academic findings for structural pattern validation. Neither source is definitive on the elasticity curve — the curve in Finding 7 is directional, not a regression.
- **Turnover cost aggregate figures**: Multifamily Executive and some industry writeups cite $3,500–$5,000 "true cost of turnover" including downtime and leasing cost (i.e., the all-in Turn Cost per Finding 6). Repo `multifamily-benchmarks.md` cites $1,500–$3,000 turnover cost — which is the narrower **unit-turn capex only** (IREM chart-of-accounts-aligned). No conflict; the two figures describe different scopes. Skill output should report both: (a) IREM-aligned unit-turn capex and (b) all-in turn cost including downtime and leasing.

## Edge Cases and Red Flags

- **Short-tenure renewal** (resident on month 10 of first lease): Often declined by operator — high churn risk resident type, minimal data to forecast renewal probability. Treat conservatively.
- **Long-tenure resident at significant loss-to-lease** (resident in place 4+ years, 15%+ LTL gap): Classic "anchored renewal" problem. Options: stepped correction over 2 renewal cycles, one-time upgrade concession to justify larger bump, or deliberate accept-the-turn decision. Skill should flag both options and let operator choose.
- **Section 8 / housing-voucher residents**: Renewal math differs materially. Voucher payment standard is market-set by PHA, not negotiated with resident; resident portion is income-based. Exclude from standard pack framework unless skill has dedicated voucher logic.
- **Resident with unresolved delinquency**: If resident has 31–60 day balance per taxonomy A/R aging, renewal should be **contingent on balance cure**, not offered unconditionally. Don't force voucher-cure residents through pure-financial renewal model.
- **Property in active value-add renovation**: When the unit is scheduled for classic-to-premium renovation at resident move-out, the "Turn Cost" calculation must capture only the make-ready-incremental-to-renovation-capex — the operator is going to do the renovation anyway on some turn, so the renewal-vs-turn decision is effectively renewal-vs-accelerated-renovation. Skill should treat this as a separate branch.
- **Compressed-spread market** (new-lease growth > renewal growth in peak cycles): Rare, but when it occurs, the operator may rationally push renewal offers aggressively because the replacement lease is more valuable than retention. Requires recent new-lease trade-out data to trigger.
- **Winter lease expirations with non-negotiable timing**: If the resident must move in winter regardless (job relocation, life event), the retention-side of the calculation collapses to zero and the operator's only lever is to minimize turn cost — not to push renewal rent.

## Open Questions

- Whether future pack versions should integrate directly with RealPage AIRM or Yardi RevenueIQ APIs to pull property-specific elasticity curves rather than relying on pack-default ranges
- Whether a separate "renewal-campaign planning" skill is needed for batch-renewal scenarios (e.g., 40 units expiring in the same month) where the aggregation of decisions changes the single-unit economics (simultaneous turns overwhelm make-ready capacity, compound downtime)
- Whether the pack should include a dedicated voucher / affordable-housing renewal framework, given that a non-trivial share of Class C and workforce multifamily involves voucher residents
- Whether renewal-offer timing (45-day vs 60-day vs 90-day notice) should be a skill parameter, as survey research suggests earlier offers increase renewal rate by 3–5 pp but reduce operator optionality
- Whether the skill should integrate with the R2 (budget-actual-variance) output — e.g., if turnover costs are running materially above budget, the renewal-cost frontier shifts and the skill should adjust recommendations accordingly
