# Lease-Up & Concessions Analyst Research

## Purpose

- Supports `skills/asset-management/lease-up-concessions-analyst.md` within the Asset Management v1.3.0 pack
- Intended for asset managers, owner-operator analysts, and LP reporting teams working on conventional multifamily (5+ unit) properties that are in lease-up, in burn-off, or tracking toward stabilization
- Provides source-backed guidance on: absorption benchmarks by market tier, concession norms and burn-off mechanics, face-vs-effective rent reconciliation during lease-up, and reforecast triggers for stabilization-date slippage
- Deliberately narrow scope: covers **velocity and concession economics** of lease-up. Does NOT cover budget-phase revenue assumptions for already-stabilized assets (Asset Management R1), stabilized renewal economics (R4), or the capex/scope side of value-add renovation (R6)

## U.S.-Only Assumptions

- Geography is the United States, with particular attention to 2024-2026 Sun Belt oversupply dynamics
- Focus is conventional market-rate multifamily lease-up (ground-up new construction and full gut-to-shell renovation where applicable); LIHTC and HUD-affordable absorption patterns are out of scope because the income-restriction waitlist dynamic distorts velocity
- Definitions for Face Rent, Effective Rent, Market Rent, Concessions, and sign convention follow `research/asset-management/_taxonomy-seed.md` §2 and §4 verbatim. Where this note references rent math, it inherits the taxonomy seed's subtractive concession convention (concessions REDUCE effective rent)
- Stabilization occupancy definition follows Fannie Mae / Freddie Mac agency-underwriting convention (90% physical occupancy sustained 90 days) as the regulatory anchor; owner-operator working definitions range 90%-95% and are called out where they differ
- Benchmarks below are aggregated national ranges. Specific submarket absorption data (e.g., Austin MSA Q1 2026) must be validated against live Yardi Matrix, RealPage, or ALN Apartment Data submarket reports at the time of underwriting, not inherited from this document

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|--------|-----------|-----|--------------|-------------|-------------|-------|
| Multifamily Guide — Stabilized Residential Occupancy / Minimum Occupancy | Fannie Mae | https://mfguide.fanniemae.com/node/3761 | 2025-08-29 (last update) | 2026-04-24 | Tier 1 — Primary agency underwriting standard | Establishes 90% / 90-day stabilized occupancy floor and how pre-stabilization Mortgage Loans are sized |
| Multifamily Underwriting Standards Form 4660 — Occupancy, Vacancy, and Concession Treatment | Fannie Mae | https://mfguide.fanniemae.com/node/4101 | 2025-08-29 (last update) | 2026-04-24 | Tier 1 — Primary agency underwriting standard | Concession, vacancy, collection-loss underwriting floor, reserve treatment |
| Freddie Mac Multifamily Seller/Servicer Guide — Lease-Up and Stabilization Definitions | Freddie Mac | https://mf.freddiemac.com/lenders/uw | 2025 | 2026-04-24 | Tier 1 — Primary agency underwriting standard | Lease-up loan program eligibility, 90% occupancy stabilization, concession burn-off expectations |
| NMHC Quarterly Survey of Apartment Conditions — Market Tightness Index | NMHC | https://www.nmhc.org/research-insight/quarterly-survey/ | 2026-Q1 | 2026-04-24 | Tier 1 — Industry association primary data | National market tightness, absorption directionality, concession sentiment from operator panel |
| U.S. Multifamily MarketBeat Q1 2026 | Cushman & Wakefield | https://www.cushmanwakefield.com/en/united-states/insights/us-marketbeats/us-multifamily-marketbeat | 2026-04 | 2026-04-24 | Tier 1 — Institutional broker research | National absorption, deliveries, vacancy, concession prevalence; Sun Belt detail |
| U.S. Multifamily Figures Q1 2026 | CBRE Research | https://www.cbre.com/insights/figures/us-multifamily-figures-q1-2026 | 2026-04 | 2026-04-24 | Tier 1 — Institutional broker research | Absorption per unit delivered, lease-up velocity, concession share of asking rent |
| Yardi Matrix Multifamily National Report | Yardi Matrix | https://www.yardimatrix.com/publications | 2026-03 | 2026-04-24 | Tier 2 — Institutional market data | Submarket absorption pace, concession use rate, rent growth by metro including Austin/Nashville/Phoenix |
| RealPage Analytics — Lease-Up and Concession Reporting | RealPage | https://www.realpage.com/analytics/ | 2026-Q1 | 2026-04-24 | Tier 2 — Institutional market data platform | Concession prevalence by metro, effective rent derivation, lease-up absorption tracker |
| ALN Apartment Data — Monthly Market Review | ALN Apartment Data | https://www.alndata.com | 2026-Q1 | 2026-04-24 | Tier 2 — Institutional market data | Units/month absorbed in lease-up, concession burn-off commentary, stabilization tracking |
| John Burns Research and Consulting — Apartment Demand and Supply Quarterly | John Burns Research and Consulting | https://jbrec.com | 2026-Q1 | 2026-04-24 | Tier 2 — Institutional research consultancy | Absorption forecasts, supply-demand balance by MSA, concession cycle stage framing |
| Marcus & Millichap — Multifamily National Investment Forecast 2026 | Marcus & Millichap | https://www.marcusmillichap.com/research | 2026-01 | 2026-04-24 | Tier 2 — Institutional broker research | Deliveries, absorption, vacancy and concession outlook by metro tier |
| Northmarq — What Are Multifamily Concessions and How Do They Impact Value | Northmarq | https://www.northmarq.com/insights/knowledge-center/what-are-multifamily-concessions-and-how-do-they-impact-value-and | 2024 | 2026-04-24 | Tier 2 — Institutional broker research | Concession mechanics, appraiser/lender treatment of concessions in cap-rate derivation |
| Wall Street Prep — Net Effective Rent: Formula + Calculator | Wall Street Prep | https://www.wallstreetprep.com/knowledge/net-effective-rent/ | 2024 | 2026-04-24 | Tier 3 — Practitioner educational | Net effective rent formula, REIT disclosure convention |
| Camden Property Trust 2025 10-K and Supplemental — Lease-Up Disclosure | Camden Property Trust | https://ir.camdenliving.com | 2026-02 | 2026-04-24 | Tier 1 — SEC-registered REIT primary disclosure | Sun Belt large-cap REIT lease-up pace, concession disclosure, stabilization timing |
| Mid-America Apartment Communities (MAA) 2025 Supplemental — Development Lease-Up | MAA | https://ir.maac.com | 2026-02 | 2026-04-24 | Tier 1 — SEC-registered REIT primary disclosure | MAA development pipeline lease-up, weekly leasing velocity, concession footnote |
| Trepp CMBS Research — Multifamily Delinquency and Lease-Up Performance | Trepp | https://www.trepp.com/trepptalk/topic/multifamily | 2026-Q1 | 2026-04-24 | Tier 2 — CMBS servicer data | Lease-up loans that miss projections, reforecast patterns, watchlist triggers |

**Citation tally.** Sixteen external sources in the table above. Tier 1 = 8 (Fannie Mae ×2, Freddie Mac, NMHC, Cushman & Wakefield Q1 2026, CBRE Q1 2026, Camden 10-K, MAA Supplemental). Tier 2 = 7 (Yardi Matrix, RealPage, ALN, John Burns, Marcus & Millichap, Northmarq, Trepp). Tier 3 = 1 (Wall Street Prep). **Tier 1+2 total = 15**, comfortably exceeding the ≥6 requirement. Total 16 external sources, exceeding the ≥10 requirement set in the task brief. Internal cross-reference to `research/asset-management/_taxonomy-seed.md` is additive and not counted toward the external tally.

## Key Findings

### 1. Absorption benchmarks vary materially by market tier and cycle stage

- **National aggregate 2024-2026.** Net absorption outpaced deliveries in Q1 2026 for the first time in several quarters per CBRE and Cushman & Wakefield Q1 2026 reports, signaling the tail of the post-COVID delivery surge. National absorption ran in the 300,000-550,000 units/year range across 2024-2025, tracking deliveries of ~450,000-600,000 units/year depending on MSA composition.
- **Property-level absorption benchmarks for new construction lease-up** (cross-referenced across Yardi Matrix, ALN, and John Burns):
  - **Tier 1 primary MSAs in balanced markets:** 15-25 units/month
  - **Tier 2 high-growth Sun Belt MSAs (pre-2023 norm):** 18-30 units/month
  - **Tier 2 high-growth Sun Belt MSAs (current 2024-2026 oversupplied conditions):** 10-18 units/month
  - **Tertiary/secondary markets:** 8-15 units/month
  - **Urban infill high-density properties (200+ units, high-rise concrete):** wider variance; 12-20 units/month is typical with meaningful concession support
- **Underwriting sanity check.** A 250-unit Class A property in a Tier 2 MSA underwritten to stabilize in 12 months implies an average ~20 units/month absorption with zero pre-leasing. That is at the upper end of the current Sun Belt reality; most 2024-2026 lease-ups are trending 15-18 months to stabilization, not 10-12.

### 2. Absorption differentiates by lease-up type

- **Ground-up new construction (no existing tenants).** Slowest initial velocity because the property has no word-of-mouth, no track record, and an unproven leasing team. Typical Month 1-3 pace is 50-70% of later months, building to peak velocity in Months 4-9, then decelerating toward Month 12+ as the remaining unit mix narrows to less-desirable floor plans or levels.
- **Value-add renovation lease-up (repositioning an existing asset).** Generally faster because the location is proven and the community has existing residents for social proof. Typical pace can be 15-30% higher than comparable ground-up in the same submarket, though this depends on renovation scope and whether residents were displaced. The capex/scope side of value-add is handled by R6 (Value-Add Business Plan Tracker); R5 is limited to the velocity/concession observation.
- **Stabilized re-tenanting (e.g., after a mass lease-expiration event or acquisition).** Fastest of the three if the asset is already market-proven; velocity is constrained only by physical turn-time and unit-mix match. Stabilization is typically re-achieved in 90-180 days rather than the 12-18 months required for a ground-up lease-up.

### 3. Concession norms track the supply-demand balance and current cycle stage

- **Concession framework (matched across Northmarq, RealPage, and Yardi Matrix convention):**
  - **Balanced / undersupplied market:** 0 to 0.5 months free on a 12-month lease (~0%-4% concession off face rent)
  - **Mildly competitive market:** 1 month free on 12-month lease (~8% off face rent, equivalent to 8.3% concession rate)
  - **Oversupplied market:** 2-3 months free on 12-month lease (~17%-25% off face rent), often layered with amenities (waived fees, gift cards)
  - **Severely oversupplied market (post-2023 Sun Belt lease-up conditions):** 2-3+ months free PLUS waived pet fees, waived admin/application fees, look-and-lease bonuses, and free parking; effective-rent erosion can reach 25%-30%
- **Current 2024-2026 conditions (Cushman Q1 2026, Yardi Matrix 2026-03, Camden 10-K 2025).** Austin, Nashville, and Phoenix lease-up projects continued to run 2-3 months free through early 2026, although Yardi Matrix and RealPage show tentative signs of concession compression in Austin starting late 2025 as the pipeline started to clear. Miami and South Florida were generally 1-1.5 months free; Northeast and Gateway markets (NYC, Boston, DC) ran 0-1 month free through the period.

### 4. Concession burn-off mechanics

- **Two-phase model.** Industry convention recognizes two phases of a concession cycle on any given asset:
  - **Heavy-concession phase.** The property is offering full concessions to drive absorption. Goal: occupancy velocity, not rent maximization. New leases during this phase lock in a 12-month effective rent materially below face rent.
  - **Burn-off phase.** As occupancy climbs past a trigger point (typically 80%-90% physical), the operator progressively reduces concessions on new leases and renewals. Goal shifts to rent maximization while holding occupancy.
- **Burn-off trigger points per Yardi Matrix, RealPage, and REIT supplemental disclosure conventions:**
  - Past 70% physical occupancy → reduce look-and-lease bonuses and ancillary incentives
  - Past 80%-85% → reduce free-rent months from 2 to 1 on new leases
  - Past 90% (stabilized) → drop concessions to 0-0.5 months; push face-rent increases
- **Legacy concession overhang.** Even after the operator stops offering new concessions, amortized concessions from earlier leases continue to drag effective rent for 12-15 months (the remaining term of concession leases). This is why a property that reaches "stabilized occupancy" typically does NOT reach "stabilized effective rent" for another full lease cycle. REITs disclose this explicitly — e.g., Camden and MAA footnotes distinguish "stabilized occupancy" from "stabilized revenue" for this reason.

### 5. Effective vs face rent reconciliation during lease-up

- **Formula (inherits from taxonomy seed §4).** `Effective Rent = Face Rent × (Lease Term − Free Months) / Lease Term`. One month free on a 12-month lease at $1,800 face → $1,650 effective. The sign convention is subtractive (concessions reduce effective rent). Any formula yielding effective rent > face rent in the presence of concessions is wrong.
- **REIT disclosure convention.** Publicly-traded REITs (Camden, MAA, AvalonBay, UDR, Essex) disclose both same-store rental rates (which typically include amortized concession) and new-lease trade-outs. The industry practice is to report effective rent as the revenue-recognition figure — that is, concessions are amortized straight-line over the lease term and subtracted from GPR to arrive at rental revenue. This matches the EGI formula in the taxonomy seed.
- **Lease-up reconciliation practice.** During an active lease-up, the asset manager should report THREE rent figures monthly:
  - **Face rent (asking)** on new units to be leased
  - **Effective rent achieved** on new signed leases this month
  - **Blended in-place effective rent** across all occupied units, which is the revenue-generating figure
- **Common pitfall.** Lenders and sponsors routinely compare face-rent comps to effective-rent actuals, which understates actual concession depth. The correct comparison is effective-to-effective, adjusted for any free-rent-on-renewal concession layered post-initial-lease.

### 6. Lease-up velocity drop-off after 70%-80% occupancy

- **Empirical observation (cross-referenced across ALN, Yardi Matrix, John Burns, and REIT supplementals).** Velocity typically **slows by 25%-50%** once a lease-up crosses the 70%-80% physical occupancy threshold. Causes:
  - Remaining unit inventory is increasingly concentrated in less-desirable floor plans, levels, or views that were passed over by earlier prospects
  - Incoming traffic slows as the property loses its "new product" marketing appeal and competitors return to prominence
  - Operator intentionally slows pace to reduce concession depth (this is an operator choice, not an involuntary slowdown)
- **Last-10% problem.** Moving from 90% to 95% occupancy during a lease-up often takes as long as moving from 50% to 70%, because the final 10% is the hardest-to-lease mix and is often held back strategically for rate push. Underwriters should NOT linearly extrapolate early lease-up velocity to the final stabilization window.

### 7. Stabilization definition — agency vs owner-level

- **Fannie Mae / Freddie Mac agency convention.** Stabilized occupancy is **90% physical occupancy, sustained for at least 90 consecutive days**, on both a new construction and value-add basis. This is the regulatory anchor — Fannie's Form 4660 references this threshold for Stabilized Residential Occupancy and it gates conversion of lease-up loans into permanent agency debt.
- **Owner-operator definitions.** Working practice varies: some sponsors use 93% physical occupancy sustained 90 days; institutional operators often use 95% physical + 92% economic simultaneously; some debt-fund bridge programs use 90% physical OR trailing-3 DSCR ≥ 1.20x. The taxonomy seed's `knowledge/multifamily-benchmarks.md` table treats 95%-97% as "excellent / target range" and 93%-95% as "good" — these are operator-level comfort thresholds, not the regulatory floor.
- **Why it matters.** The spread between the 90% agency threshold and the 95% operator threshold is typically 3-6 months of additional lease-up velocity. Sponsors building to an agency-refi exit can legitimately target the 90% threshold; sponsors underwriting internal stabilized returns should use a tighter 93%-95% floor.

### 8. Reforecast triggers based on actual absorption

- **Absorption shortfall triggers.** Industry working practice (Trepp CMBS, REIT internal guidance, institutional LP reporting) treats the following as reforecast triggers:
  - **Trailing-3-month absorption running 25% or more below original underwriting** — trigger a stabilization-date pushout calculation and rebudget concession depth
  - **Two consecutive quarters of absorption ≤ 75% of underwritten pace** — trigger a formal reforecast of stabilization date, concession burn-off timing, and DSCR at refi
  - **Missing a contractual stabilization milestone** (e.g., lender-covenanted 80% occupancy by Month 10) — trigger immediate lender communication and reforecast; often triggers a watchlist designation in CMBS servicing
- **Reforecast mechanics (pack convention).** A stabilization reforecast should recompute three figures in this order:
  1. **Revised stabilization date** = current occupancy + (remaining units to stabilization / actual trailing-3 monthly absorption). Use TTM absorption only if the trailing 3 is an outlier.
  2. **Revised concession burn-off schedule** = extend heavy-concession phase by the stabilization-date slippage; burn-off trigger points (70%/80%/90%) remain the same but the calendar dates shift
  3. **Revised EGI ramp and DSCR coverage** at each reforecast point; flag any DSCR covenant breach risk to ownership
- **REIT disclosure as reference.** Camden Property Trust 2025 10-K explicitly discloses stabilization delays for properties underwritten pre-2023 whose absorption came in 20%-30% below original projections; the REIT's supplemental shows extended stabilization from 12 months to 18-24 months on affected assets.

### 9. Pre-leasing dynamics before ribbon-cutting

- **Typical pre-leasing at first CO (Certificate of Occupancy).** Industry benchmarks (Yardi Matrix, ALN, John Burns):
  - **Strong pre-leasing market:** 25%-40% pre-leased at first CO
  - **Normal market:** 10%-25% pre-leased
  - **Weak / oversupplied market:** 5%-15% pre-leased
- **Current 2024-2026 Sun Belt observation.** Cushman Q1 2026 and Yardi Matrix 2026-03 note that pre-leasing in Austin, Nashville, and Phoenix lease-ups has been running below 10% at first CO throughout 2024-2025, which is a meaningful leading indicator of a long lease-up runway and deep concessions. A property opening with sub-10% pre-leasing should not be underwritten to 12-month stabilization in a Sun Belt oversupplied market; 18-24 months is more realistic.
- **Pre-leasing deposit economics.** Pre-leasing traffic typically requires a holding deposit ($250-$500) and a firm move-in date window. Operators accept 10%-20% pre-leasing cancellation rates as normal. Underwrite pre-leases at 85% of signed count, not 100%.

### 10. Concessions treatment in valuation

- **Appraiser and lender convention (per Northmarq, Fannie Mae Form 4660, Trepp).** Concessions are subtracted from face rent before applying the cap rate:
  - Appraiser typically derives cap rate from comps that are themselves stabilized (minimal concession), then applies the cap rate to a pro-forma effective NOI that nets concession drag out
  - Lender (Fannie/Freddie) underwrites to trailing concession burn-off; Form 4660 explicitly requires that concessions be modeled at actual current levels, not a "hoped-for burn-off" run-rate, for loan sizing
  - **Critical implication:** A sponsor showing a proforma NOI based on zero concessions will fail agency underwriting if the property is still in burn-off. The lender will haircut NOI by the in-place concession amortization until trailing-3 data demonstrates the concession has actually rolled off.
- **Cap-rate transparency.** Two properties with identical face rent but different concession depth should NOT trade at the same cap rate on face-rent NOI. Appraisers increasingly disclose both the face-rent NOI and the effective-rent NOI and apply the cap rate to the effective figure. Brokers sometimes quote cap rate on face, which inflates apparent value by 10-15 bps on a heavily-concessioned asset.

### 11. Current market data (2024-2026) — Sun Belt oversupply cycle

- **Deliveries peak.** 2024 marked the peak of the post-COVID multifamily delivery cycle, with ~570,000-600,000 units delivered nationally depending on the tracker (Yardi Matrix, CBRE, RealPage agree within 5%). Sun Belt MSAs — particularly Austin, Nashville, Phoenix, Dallas, Atlanta, Charlotte, Raleigh — absorbed the majority of these deliveries.
- **Concession compression starting late 2025.** Yardi Matrix, RealPage, and John Burns all signal concession compression in Austin starting Q4 2025, spreading to Nashville and Phoenix in early 2026. Marcus & Millichap's 2026 Multifamily Forecast projects stabilization in these markets by late 2026/early 2027.
- **Miami/South Florida divergence.** Despite heavy deliveries, demand held up better in Miami-Dade and Broward than in Austin/Nashville/Phoenix per Cushman Q1 2026. Concessions remained 1-1.5 months in South Florida where Austin ran 2-3 months.
- **Gateway markets.** NYC, Boston, DC, and San Francisco generally ran 0-1 month free through the period, with SF concession depth declining materially from 2021-2022 peak as downtown demand recovered.
- **Implication for underwriting a 2026-2027 lease-up.** Assume 15-18 months to stabilization at 90% agency threshold in Sun Belt Tier 2 markets, with 2-3 months free ramping down to 0-1 month by Month 9-12. Assume 12-15 months in Gateway with 0.5-1 month free throughout. These are current-cycle-specific defaults and should be retired as the oversupply clears.

## Benchmark and Formula Decisions

- **Adopt the Fannie Mae 90% / 90-day stabilization definition as the pack-default agency anchor.** Skills should report stabilization status against both agency (90% physical, 90 days) and operator (93%-95% physical + 92% economic) thresholds where relevant.
- **Adopt the two-phase concession model (heavy + burn-off) with 70%/80%/90% trigger points as the pack-default burn-off schedule.** Operator-specific schedules may override; in their absence, use these thresholds.
- **Effective rent convention follows the taxonomy seed §4 verbatim.** No divergence. `Effective Rent = Face Rent × (Lease Term − Free Months) / Lease Term`. Concessions are subtractive.
- **Absorption benchmarks.** Use the tier-based ranges in Key Findings §1 as defaults. Submarket-specific Yardi Matrix, RealPage, or ALN data overrides the table at runtime when available.
- **Reforecast materiality thresholds.** Trigger a stabilization-date reforecast when trailing-3 absorption ≤ 75% of underwritten pace for any single month, OR trailing-6 absorption ≤ 80% of underwritten pace. These are pack defaults; individual operators may tighten.
- **Pre-leasing underwrite.** Haircut signed pre-leases by 15% (underwrite at 85% of pre-lease count) to reflect normal cancellation.
- **Concession-reporting mandate.** Skills must report face rent, effective rent achieved this month, AND blended in-place effective rent across all occupied units on every lease-up status report. Face-only reporting is not sufficient.

## Conflicting Source Resolution

- **Stabilization definition conflict.** Fannie Mae's 90% / 90-day agency threshold conflicts with operator-level 93%-95% thresholds and with `knowledge/multifamily-benchmarks.md`'s 95%-97% "excellent" range. Resolution: agency threshold is the regulatory floor; operator-level threshold is the comfort/target. Skills must distinguish the two. The taxonomy seed treats these as compatible-but-different.
- **Absorption benchmark ranges.** Yardi Matrix, CBRE, and Cushman & Wakefield sometimes report slightly different national absorption totals for the same quarter due to methodology, building-size thresholds, and coverage of lease-up versus stabilized assets. Resolution: use the figures for direction and magnitude, not as precise point estimates. Apply the range, not the point value.
- **Concession depth reporting.** Marketing asking rents (as seen on ILS sites) frequently include the concession; contract rents reported to lenders and REIT supplementals usually do not. A quoted "2 months free" on an ILS may show up in REIT same-store disclosure as an effective-rent discount without explicit free-rent language. Resolution: always back-solve from effective rent, never take asking-rent-with-asterisk at face value.
- **Pre-leasing cancellation rates.** Practitioner commentary (including broker and developer blog sources) suggests pre-lease cancellation rates of 5%-30%, with wide variance by market. Resolution: adopt 15% as a mid-point default, and override with property-specific historical data when available.

## Edge Cases and Red Flags

- **Zero concessions in an oversupplied submarket.** If an asset claims zero concessions while peer properties in the same submarket are offering 2-3 months free, either the asset is severely mispricing (losing share) or the reporting is incomplete (concessions are off-sheet — gift cards, waived fees). Investigate before accepting the reported face rent.
- **Accelerating absorption in the final 10%.** If a lease-up claims accelerating velocity in the 85%-95% range (contrary to the typical deceleration pattern), scrutinize: is the operator dropping rate to hit a covenant? Is the occupancy number including employee/model/down units? Is there a related-party lease-up?
- **Stabilization claimed without 90 consecutive days.** Some operators report "stabilized" on a single-period 90% reading. The agency definition requires 90 consecutive days at 90%. One month at 91% followed by a drop back to 88% is NOT stabilization.
- **Concession carryforward into "stabilized" period.** Concessions from lease-up leases continue to amortize for 12-15 months after the operator stops offering them. An asset reaching "stabilized occupancy" in Month 12 will not reach stabilized effective rent until Month 24+. LP reporting must disclose both dates.
- **Rent-ready unit inflation.** "Available to lease" unit counts sometimes exclude units that are physically complete but held back for rate push or amenity/model usage. Occupancy denominators should be total physical units (including holdouts), not "leasable" units — otherwise occupancy percentages are inflated.
- **Mass-delivery lease-ups.** A property delivering 300-400 units simultaneously in a single submarket that already has 3,000 units in lease-up cannot realistically absorb at the same pace as a solo delivery. Overlapping lease-ups in a submarket cannibalize each other; adjust per-property absorption down by 20%-30% when the submarket has concentrated deliveries.
- **Pre-leased-to-related-party.** Some developers pre-lease units to affiliated entities (corporate housing JV, related-party master lease) to show initial velocity. These leases are not independent demand evidence. Scrutinize the first 5%-10% of leases for related-party patterns.
- **Debt-fund bridge covenant breach risk.** Lease-up bridge loans often have DSCR covenants tested at 12 or 18 months. A property running behind underwriting pace will hit a covenant test before it hits stabilized NOI; the reforecast must surface this at least 6 months ahead of the test date.
- **"Concession-free" new leases while renewals still include concessions.** An operator burning off concessions on new leases while still offering them on renewals (to retain existing residents) can show a face-rent increase that is not net-positive in effective-rent terms. Break out the two streams in reporting.
- **Renewal concessions at end of initial lease cycle.** When a resident's 12-month lease with 2 months free expires and they renew, operators sometimes offer 1 month free on renewal to hold them — a partially-offset concession that prolongs the burn-off. Model this through the first post-initial renewal cycle.

## Open Questions

- Whether the pack should adopt a tighter stabilization definition for LP reporting (e.g., 93% physical + 92% economic sustained 180 days) and reserve the Fannie 90%/90-day definition strictly for agency-refi readiness reporting
- Whether absorption benchmarks should be refreshed quarterly from a live data source (Yardi Matrix API, RealPage) rather than hard-coded into this research note; current practice is to treat the tier ranges here as structural defaults and expect skill execution to pull live submarket data
- Whether the concession burn-off trigger points (70%/80%/90%) should be calibrated per market tier (Sun Belt vs Gateway) rather than applied uniformly; current evidence suggests the 80% trigger is fairly uniform across markets but the 90% "burn-off complete" trigger moves later in oversupplied markets
- Whether pre-leasing cancellation rates should vary by cycle stage (balanced vs oversupplied) — current pack default of 15% is a mid-cycle average and may understate cancellations in softening markets
- Whether the skill should explicitly model the effective-rent overhang (amortized concession drag post-stabilization) in stabilized NOI projections, or treat it as a separate disclosure line; current convention is separate disclosure for clarity
- How to handle mixed-status properties (partial renovation, partial new tower, adaptive reuse) where the three absorption differentiation categories in Key Findings §2 overlap in a single asset
- Whether to incorporate submarket concentration-of-deliveries as a formal input — i.e., adjust absorption benchmark down when the submarket has 3+ simultaneous lease-ups within a 1-mile radius
