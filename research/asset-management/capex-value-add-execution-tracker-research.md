# CapEx / Value-Add Execution Tracker Research

## Purpose

- Supports the Asset Management pack v1.3.0 skill `skills/asset-management/capex-value-add-execution-tracker.md` and the shared KB extensions that will document value-add execution benchmarks.
- Intended for asset managers, owner-operator GPs, LP reporting teams, and construction managers responsible for tracking multifamily value-add capital plans **after** acquisition close.
- Focused on **execution tracking vs underwriting assumptions** — unit-turn scope and cost, rent-premium realization, common-area and major-systems capex, schedule adherence, cost-overrun diagnostics, and the KPIs used in monthly/quarterly asset-management reporting.
- Explicitly out of scope: (a) pre-acquisition capex underwriting — covered by the existing Due Diligence pack's capex and physical inspection skills; (b) ongoing maintenance capex baselines and replacement reserve accruals — covered by R1 (replacement reserves research); (c) routine turnover economics on non-renovated units — covered by R4 (turnover economics research). Handoff points to those adjacent research notes are identified in §7.

## U.S.-Only Assumptions

- Geography is the United States — definitions align with Fannie Mae / Freddie Mac agency supplemental reporting conventions, NCREIF property-level reporting, and REIT supplemental disclosures (MAA, Camden, UDR, Essex, AvalonBay, Equity Residential).
- Product type is conventional stabilized multifamily (5+ units, garden / mid-rise / high-rise), Class B and Class C being the dominant value-add target classes. Class A "re-amenitization" value-add is treated as a narrower sub-scenario.
- Capital program context is **in-place stabilized asset with interior/common-area renovation**, not ground-up development and not gut rehab / adaptive reuse (those fall into Opportunistic underwriting, which is a different track).
- Cost ranges are stated in 2024–2026 dollars. Ranges reflect the post-2022 construction-cost plateau following the 2021–2023 inflation surge.
- Rent-premium realization evidence is drawn from public REIT supplementals, agency lender data, broker research, and sponsor limited-partnership reports where disclosed; private-deal performance is more variable and this note flags that dispersion explicitly.

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|--------|-----------|-----|--------------|-------------|-------------|-------|
| Walker & Dunlop — Multifamily Outlook 2025 (Value-Add in a Higher-Rate World) | Walker & Dunlop Research | https://www.walkerdunlop.com/insights/2024/multifamily-outlook-2025/ | 2024-12 | 2026-04-24 | Institutional lender research | Rent-premium realization commentary, bridge-to-perm value-add financing context |
| John Burns Research & Consulting — Apartment Renovations: What Renters Will Pay For | John Burns Research & Consulting | https://jbrec.com/insights/apartment-renovations-what-renters-will-pay-for/ | 2023-09 | 2026-04-24 | Institutional consumer research | Renter willingness-to-pay by scope element; tier saturation signals |
| Marcus & Millichap — Multifamily National Investment Forecast 2025 | Marcus & Millichap Research Services | https://www.marcusmillichap.com/research/research-reports/national-reports | 2025-01 | 2026-04-24 | Institutional brokerage research | Value-add deal flow, premium compression in oversupplied Sun Belt submarkets |
| CBRE — U.S. Multifamily Figures Q4 2024 / Multifamily Outlook 2025 | CBRE Research | https://www.cbre.com/insights/reports/us-multifamily-figures-q4-2024 | 2025-02 | 2026-04-24 | Institutional research | Rent growth by vintage, class-B rent performance vs class-A |
| RealPage Analytics — Renovation Rent Premiums and Lease Trade-Out | RealPage Market Analytics | https://www.realpage.com/analytics/ | 2024 | 2026-04-24 | Market data / platform research | Premium realization by submarket, demand-supply absorption of renovated units |
| Fannie Mae Multifamily — Green Rewards & Supplemental Renovation Financing | Fannie Mae | https://multifamily.fanniemae.com/financing-options/specialty-financing/green-financing | Updated 2025 | 2026-04-24 | Primary GSE / agency source | Underwriting conventions for supplemental value-add loans; renovation reserve treatment |
| MAA (Mid-America Apartment Communities) — 2024 Annual Report / 10-K (Interior Redevelopment Program) | MAA / SEC EDGAR | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000912595&type=10-K | 2025-02 | 2026-04-24 | Primary public filing | Interior redev unit counts, cost/unit disclosed, achieved rent premium, ROI disclosed |
| Camden Property Trust — 2024 Annual Report / 10-K (Value-Add Program) | Camden / SEC EDGAR | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000906345&type=10-K | 2025-02 | 2026-04-24 | Primary public filing | Disclosed renovation cost/unit and realized rent premium |
| UDR, Inc. — 2024 Annual Report / 10-K (Value-Add / Kitchen & Bath program) | UDR / SEC EDGAR | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000074260&type=10-K | 2025-02 | 2026-04-24 | Primary public filing | Disclosed kitchen-and-bath program cost and premium, unit count by tier |
| AvalonBay Communities — 2024 Annual Report / 10-K (Re-development Program) | AvalonBay / SEC EDGAR | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000915912&type=10-K | 2025-02 | 2026-04-24 | Primary public filing | Re-development budget, timeline, achieved yield-on-cost |
| NAA / NMHC — 2024 Survey of Operating Income and Expenses | NAA / NMHC | https://naahq.org/ | 2024 | 2026-04-24 | Institutional research | CapEx reserve benchmarking; renovation vs replacement distinction |
| RSMeans / Gordian Construction Cost Data (Residential Remodeling) | RSMeans / Gordian | https://www.rsmeans.com/ | 2024 | 2026-04-24 | Institutional construction-cost data | Unit pricing for cabinets, flooring, fixtures, appliances used in sponsor budgeting |
| Bureau of Labor Statistics — PPI, Building Materials & Construction Inputs | U.S. BLS | https://www.bls.gov/ppi/ | 2024–2025 | 2026-04-24 | Primary government source | Material-cost inflation index 2021–2023, plateau 2024–2025 |
| Associated Builders & Contractors — Construction Input Price Index | ABC | https://www.abc.org/News-Media/News-Releases | 2024–2025 | 2026-04-24 | Trade-association index | Cost-overrun benchmarking |
| Multi-Housing News / Multifamily Dive — Value-Add Execution Coverage | Multi-Housing News / Multifamily Dive | https://www.multihousingnews.com/ ; https://www.multifamilydive.com/ | 2024–2025 | 2026-04-24 | Trade press | Sponsor case studies, typical scope ranges, schedule norms |
| Freddie Mac Multifamily — Renovation / Moderate Rehab Supplemental | Freddie Mac | https://mf.freddiemac.com/ | Updated 2024 | 2026-04-24 | Primary GSE / agency source | Supplemental loan sizing against projected post-renovation NOI |

## Key Findings

### Unit-turn scope tiers and cost benchmarks

The industry converges on a three-tier scope taxonomy for interior value-add renovations. The tiers below are synthesized from John Burns renter willingness-to-pay research, sponsor limited-partnership disclosures, and agency (Fannie/Freddie) supplemental loan sizing conventions. Costs are 2024–2026 dollars, hard-and-soft costs including construction management fee but excluding GC markup to sponsor G&A.

- **Light / "lipstick" scope — $3,000–$6,000/unit.** Paint, two-tone accent wall, updated light fixtures, cabinet paint or resurface, new hardware (pulls/knobs), faucet replacements, mini-blinds, appliance black-out-package swap (if appliances functional), patch-and-clean flooring. Targets Class B- to C+ assets in Tier 3–4 markets where premium ceiling is $50–$100/mo. Payback typically 24–36 months.
- **Medium / "classic" scope — $6,000–$12,000/unit.** Everything in Light, plus: full cabinet replacement or refacing with new doors, quartz or high-grade laminate counters, LVP / plank flooring throughout living and wet areas, stainless appliance package (range, refrigerator, dishwasher, microhood), new lighting package, bathroom vanity replacement, tub surround refresh / reglaze, USB-integrated outlets. Targets Class B to B+ garden properties in Tier 2–3 markets. Premium ceiling $75–$175/mo; payback 18–30 months.
- **Heavy / "full interior" scope — $12,000–$25,000/unit.** Everything in Medium, plus: full kitchen reconfiguration, new cabinet boxes not just doors, waterfall or mitered-edge quartz, new tub/shower surround or shower conversion, tile flooring in baths, upgraded plumbing fixtures (pull-down kitchen, rain shower heads), smart-home package (thermostat, locks, leak detectors), in-unit W/D hookup or stacker installation, lighting throughout, new interior doors and trim, upgraded HVAC registers/returns. Targets Class C to B- assets being repositioned up a half-class, or legacy Class A re-amenitization. Premium ceiling $150–$350+/mo; payback 30–48 months with higher variance.

John Burns' renter-WTP research is foundational here: renters **pay meaningfully** for (in descending order) in-unit washer/dryer, stainless appliances, quartz counters, and LVP flooring; they pay **less** for cabinet-door-only refacing, mini-blinds, and backsplash tile when the rest of the kitchen is dated. Sponsors systematically overestimate the premium impact of "lipstick" scopes applied without a full kitchen refresh.

Cost dispersion around these ranges is large. RSMeans / Gordian unit pricing combined with ABC labor indices suggest a 1.3x–1.6x spread between low-cost (Texas, Georgia, Alabama, Ohio, Indiana) and high-cost (California, New York, Massachusetts, Washington state) markets for the same scope. A Medium scope priced at $9,000/unit in Dallas is plausibly $12,500–$14,500/unit in Los Angeles for the identical finish package.

### Interior-scope cost split by unit type

Per-unit totals vary by bedroom count, driven mostly by cabinet linear footage, flooring area, and paint-and-drywall labor, not by fixture count. Indicative splits at the Medium tier:

| Unit Type | Typical Cost (Medium Scope) | Primary Cost Drivers |
|---|---|---|
| Studio / Efficiency | $5,500 – $8,000 | Smaller kitchen, single bath, limited flooring area |
| 1BR / 1BA | $6,500 – $10,500 | Base-case; drives per-unit benchmark |
| 2BR / 1BA | $7,500 – $11,500 | More flooring, same kitchen |
| 2BR / 2BA | $8,500 – $13,000 | Second bath adds $1,000–$2,500 |
| 3BR / 2BA | $9,500 – $14,500 | More flooring + sometimes larger kitchen |

Sponsors frequently underwrite a single blended unit cost across the property. Asset-management tracking should decompose actual costs to unit type because the premium captured per scope dollar differs by bedroom count — 2BR renovations typically realize 80–100% of budgeted premium while 3BR/townhome renovations often realize only 60–80% (large-unit renters are more price-sensitive in suburban Tier 3 markets per CBRE and Marcus & Millichap data).

### Rent-premium realization vs underwriting

This is the single most-important tracking metric. Aggregate evidence:

- **Public REIT disclosure (MAA, Camden, UDR):** Disclosed interior-redevelopment programs in 2022–2024 10-K filings consistently show realized rent premiums in the **$125–$200/mo** range on Medium-tier scopes of $7,500–$12,000/unit, producing stated yield-on-cost (annualized rent premium ÷ renovation cost) of 18–24%. These are the most reliable benchmarks because they are audited disclosures.
- **John Burns / RealPage sponsor surveys:** Private-deal value-add sponsors report **75–90% of underwritten premium realized** as a baseline in 2019–2021 vintage business plans. The 2022–2024 cohort has trended lower — closer to **60–80% of underwritten premium** — driven by (a) oversupply in Sun Belt submarkets compressing organic rent growth, (b) concession re-emergence, and (c) amenity-tier saturation where the renovated unit no longer stands out from new supply.
- **Walker & Dunlop (2024–2025 commentary):** Identifies a specific "2021–2022 vintage underwriting miss" — business plans written at peak rent growth underwrote 4–6% base rent growth plus full premium capture; actual 2023–2024 delivery saw 0–2% base growth plus partial (50–70%) premium capture. The financing structure (bridge loans maturing into higher-rate perm markets) then converted the execution miss into a capital-stack problem.
- **Marcus & Millichap (2025 National Forecast):** Flags specific oversupplied metros (Austin, Phoenix, Nashville, Raleigh, Charlotte, Salt Lake City) where realized premiums on 2023-delivered renovations are running materially below pro-forma. In those markets, 40–65% of underwritten premium was achievable in 2024.

The tracking implication is that **a single "realized premium %" KPI is the single most operationally-consequential value-add metric** — more important than any cost metric, because premium drives both NOI and the exit cap rate's implied valuation lift.

### Common-area and amenity capex benchmarks

Common-area capex is typically sized as a distinct budget from interior renovations and tracked by project rather than by unit. Indicative ranges for a 200-unit garden / mid-rise property:

- **Amenity deck / package:** $500k–$2.0M depending on scope. A light refresh of clubhouse paint, furniture, and flooring runs $200k–$500k. A full amenity repositioning (new fitness center equipment, clubhouse reconfiguration, business center, coworking nook, package room/lockers) runs $1.0M–$2.0M.
- **Exterior envelope / curb appeal:** $200k–$500k. Paint, signage, monument/entry feature, mailbox cluster, lighting package, building-number refresh, porte-cochère. Critical for leasing velocity — listing photos drive tour conversion.
- **Landscaping:** $100k–$300k. Tree work, new beds, irrigation repair, sod, pet-relief stations, decorative fencing.
- **Pool area:** $150k–$400k. Pool resurface ($40k–$80k), deck resurface or replace, new furniture, shade structures, pool-bath refresh, gate/fence upgrade.
- **Fitness center:** $100k–$250k. New equipment package, flooring, mirrors, audio, climate.
- **Technology / smart-home rollout:** $500–$1,000/unit. Smart locks, thermostats, leak detection, community Wi-Fi backbone. Implementation risk is significant — retrofit networking in older buildings has a >20% variance rate against budget.
- **Dog park / pet amenities:** $25k–$75k. Among the highest-ROI small-dollar items per John Burns renter research in pet-heavy Tier 2–3 markets.

### Major-systems capex benchmarks

These are tracked separately from value-add capex because they preserve the asset rather than generate premium. Sponsors typically fund from capital reserves or separate loan proceeds, not the interior renovation budget. Benchmarks:

- **Roof replacement:** $8–$15/sqft of roof area. A 200-unit garden property with ~200,000 SF of flat TPO / modified-bitumen roof runs $1.6M–$3.0M. Pitched shingle on a walk-up property runs $6–$10/sqft.
- **HVAC replacement (individual PTAC / split units):** $6,000–$12,000/unit total cost, including condenser, air handler, thermostat, registers, and labor. Replacement program typically phased over 3–5 years at 20–30 units/year.
- **Central boiler / chiller replacement:** $50k–$200k per system depending on capacity. Mid-rise / high-rise properties with 1960s–1980s central systems frequently require this.
- **Plumbing risers / supply-line replacement:** $5,000–$10,000/unit for full repipe. Polybutylene (1978–1995 vintage) and galvanized (pre-1970) properties are the dominant candidates. Scheduling is disruptive — typically phased by riser stack and coordinated with unit turns.
- **Electrical panel upgrade:** $1,500–$3,500/unit for panel replacement; add $1,500–$2,500/unit if service upgrade from the utility is also required (e.g., FPE / Zinsco panel replacement).
- **Elevator modernization:** $150k–$300k per car for a full modernization; $40k–$80k for a partial (controller + fixtures) upgrade.
- **Parking lot resurface / seal & stripe:** Seal and stripe $0.25–$0.50/SF; mill and overlay $3–$5/SF; full replacement $5–$8/SF.

These systems capex items interact with value-add execution in two ways: (a) they can consume renovation-budget contingency when discovered during unit turns (hidden galvanized plumbing, failed HVAC, concealed roof leaks), and (b) they create downtime that delays unit delivery into the renovated lease-up pipeline. Asset managers should track both in the same monthly dashboard even though they have different budget lines.

### Schedule norms

- **Unit-turn renovation cadence:** Stabilized asset with natural turnover drives a **10–20 units/month** renovation pace on a 200–300 unit property. This is governed by natural lease-expiration velocity, not construction capacity. Pushing beyond the natural turn rate requires vacate-and-renovate (offering early-termination incentives) or in-place renovations (disruptive, limited scope).
- **Total program duration:** For a stabilized asset, interior value-add is typically **phased over 2–3 years** (24–36 months) from kickoff to full program completion. Pushing to a 12–18 month timeline requires aggressive vacate strategies and typically signals a repositioning / re-tenanting play rather than a pure value-add.
- **Common-area timeline:** Amenity and exterior work is typically **front-loaded** in months 1–9 because the leasing narrative ("new clubhouse, new pool, updated grounds") needs to support renovated-unit asking rents. Sponsors who back-load common-area work often see the interior premium capture underperform by 10–20% in the first 12 months.
- **Lease-up of renovated units:** Target absorption of **3–5 renovated units/month of new leases** at the premium rent. If renovated units sit more than 30 days vacant, the premium is likely mispriced relative to comps.
- **Typical project milestones a tracker should monitor:** kickoff, GC / vendor selection, scope locked, first unit complete, 10% complete, 25% complete, 50% complete, 75% complete, program complete, stabilized post-renovation occupancy, refinance or supplemental loan draw.

### Cost overrun rates

- **Historical baseline (pre-2021):** Sponsor LP reports and agency data suggest a typical cost overrun of **5–10% vs budget** for disciplined GPs on interior renovations.
- **2021–2023 inflation surge:** BLS PPI for building materials rose ~35% peak-to-trough; ABC construction input indices showed lumber, electrical, and HVAC material up 40–60% at peaks. Sponsor LP reports from this cohort disclose cost overruns of **15–30% vs original underwriting** on programs that were not re-priced mid-stream.
- **2024–2025 plateau:** BLS PPI has stabilized. Cost overruns for 2024-executed programs have returned to a **7–15% range**, with the residual overrun driven by labor availability (especially HVAC and electrical trades) and scope creep during in-unit construction (discovered subfloor, drywall, plumbing issues).
- **Key drivers of overruns beyond materials:**
  1. Discovered conditions at unit turn (hidden damage behind cabinets, subfloor rot, failed plumbing) — budget 5–10% contingency line explicitly
  2. Scope creep when amenities are value-engineered up during execution
  3. Change orders driven by finish-package substitutions (appliance availability, cabinet-supplier lead times)
  4. Schedule slippage causing carrying-cost overruns (interest on renovation loan, taxes on vacant units)

### Sponsor-reported realized vs projected premium (public disclosures)

The clearest independent benchmarks come from REIT 10-K disclosures (pages referencing "value-add," "interior redevelopment," or "same-store capital improvement" programs):

- **MAA (Mid-America Apartment Communities):** Discloses the interior-redevelopment program cost per unit and the achieved rent premium. 2023–2024 disclosures show ~$7,000–$8,500/unit cost with ~$110–$135/mo rent premium, yielding ~17–20% yield-on-cost. The program has been steadily de-risked since 2018 and the achieved premiums are among the most consistent in the REIT universe.
- **Camden Property Trust:** Discloses value-add / interior-renovation unit counts and spending. Historical premiums disclosed in $100–$150/mo range at $7,500–$10,000/unit cost.
- **UDR:** Discloses kitchen-and-bath programs as a separate capital category. Disclosed premium/cost ratios in the 15–20% yield-on-cost range have been consistent across multiple years of supplementals.
- **AvalonBay:** Re-development program (a heavier scope than the other three) discloses multi-year budgets and realized rents upon re-delivery. Yields disclosed typically in the 7–10% yield-on-cost range — lower because the scope is heavier (closer to gut rehab) and the base Class A rents are already high.

Private sponsor disclosures via LP quarterly reports show a **wider distribution** — top-quartile sponsors hit 85–100% of underwritten premium; bottom-quartile sponsors hit 40–60%. The spread is almost entirely a function of (a) market selection (avoiding oversupply), (b) scope fit to the submarket, and (c) execution discipline on schedule.

### KPIs that asset-management dashboards should track

The monthly / quarterly value-add execution dashboard converges on a small set of metrics:

- **Units renovated this month / cumulative units renovated vs plan.** Numerator, denominator, and % complete. Shows schedule adherence.
- **$ spent this month / cumulative $ spent vs budget.** Total and per-unit. Shows cost adherence.
- **Cost per renovated unit (actual) vs budget per unit.** Rolls up to overall program variance.
- **Renovated-unit achieved rent vs underwritten market rent at renovation.** This is the premium-capture %. Report in $/mo and % of UW target.
- **Premium realization % = (actual premium / underwritten premium) × 100.** The single-most-important lagging indicator.
- **Trade-out on renovated units = (new lease rent − prior lease rent) / prior lease rent.** The operator-internal measure of premium realization; compare new-to-new trade-outs (vacant unit leased to new tenant) vs renewals (existing tenant accepts renovated status on renewal at a premium rent).
- **Renovation-lease-up vacancy days.** Days between renovation-complete and new-lease-commencement. If >30 days, premium is likely mispriced.
- **Yield on cost (stabilized).** Annualized rent premium ÷ renovation cost per unit. Benchmark 15–25% for Medium scopes; below 12% is typically a sign of either overspending or underpricing.
- **Common-area capex actual vs budget by project.** By project, not by unit, because amenity spend is lumpy.
- **Contingency burn rate.** Of the contingency line, what % has been committed at what % of program complete? A 75% contingency burn at 50% program complete is an early-warning signal.
- **Forward pipeline / scheduled vs. actual turn-to-renovation flow.** Units vacating, units scoped, units under construction, units delivered, units leased.

## Benchmark and Formula Decisions

- Adopt the **three-tier interior scope taxonomy** (Light $3–6k / Medium $6–12k / Heavy $12–25k) as the canonical scope vocabulary. Do not invent additional tiers; do not publish single-point cost estimates outside these ranges.
- State ranges in **2024–2026 dollars** and include a note that material-cost indexing should be refreshed annually against BLS PPI for building materials.
- Use **yield on cost (annualized rent premium ÷ renovation cost per unit)** as the canonical ROI metric for value-add unit renovations. Target benchmarks: 18–22% institutional, 12–15% minimum acceptable, <10% failing.
- Use **premium realization % (actual premium / underwritten premium)** as the canonical execution-tracking metric. Target benchmarks: 85%+ strong, 70–85% acceptable, 50–70% underperforming, <50% failing.
- Apply cost dispersion by **COL tier** using the multipliers already defined in `knowledge/multifamily-benchmarks.md` §Cost of Living Multipliers (specifically the Labor / Payroll and Maintenance & Repairs rows, which proxy most of the value-add cost-of-labor sensitivity).
- Treat **common-area capex as separate from unit interior capex** in all dashboards and LP reports. Combining them hides the distinct execution risks of each.
- Treat **major-systems capex as separate from value-add capex** in all dashboards — major-systems preserves NOI, value-add generates NOI. Reporting them together creates false ROI signals.
- Use **REIT 10-K disclosures (MAA, Camden, UDR, AvalonBay) as the Tier-1 benchmark for premium realization** rather than sponsor pitch decks. REIT disclosures are audited; pitch decks are selection-biased toward winning deals.

## Conflicting Source Resolution

- **Sponsor pitch-deck premium claims vs public REIT disclosures.** Pitch-deck underwritten premiums often cluster at $175–$250/mo for Medium scopes; REIT realized premiums cluster at $110–$150/mo for similar scopes in similar markets. The skill should anchor on REIT realized data for benchmarking and treat sponsor pitch-deck underwritten premiums as aspirational. Do not re-adjudicate this as a "both sources valid" — the realized data is the evidence, the pitch deck is the hypothesis.
- **John Burns WTP surveys vs RealPage revealed-preference data.** Burns' survey data captures renter stated preferences; RealPage captures actual lease trade-out differentials across renovated vs un-renovated units in the same property. Where they disagree, **RealPage revealed-preference wins for premium estimation**; Burns is more useful for scope prioritization (which items to include).
- **Walker & Dunlop vs Marcus & Millichap on 2024 premium compression.** Both identify the 2023–2024 premium compression; they disagree modestly on magnitude (W&D says ~20% below UW on aggregate; M&M says 35–60% below UW in specific oversupplied metros). Resolve by **segmenting by metro oversupply level** — M&M is right in oversupplied Sun Belt submarkets, W&D's lower compression estimate applies to balanced / undersupplied markets.
- **Cost ranges from RSMeans vs sponsor actuals.** RSMeans represents median commercial construction unit pricing; sponsor actuals include GC markup, construction management fee, permit fees, and contingency. Use RSMeans as a lower bound and apply a 1.15x–1.30x all-in multiplier to reach sponsor-reported all-in cost.
- **Cost-overrun framing.** Some sources report overruns as % of original budget; others report as % of final actual cost. The skill should standardize to **% of original budget** ((actual − original budget) / original budget) for consistency across sponsor LP reports.

## Edge Cases and Red Flags

- **Rent-control / stabilization jurisdictions.** In rent-stabilized markets (NYC, some CA cities, Portland, St. Paul), the rent-premium capture rule changes fundamentally — premiums are limited to individual apartment improvement (IAI) allowances or similar regulatory caps. Value-add underwriting that projects market-rate premium capture in a rent-controlled unit is a fundamental error. The skill must flag this and redirect to a regulatory-cap calculation.
- **LIHTC / affordable housing overlay.** Properties with LIHTC, Section 8, or tax-credit restrictions cap rent growth to AMI-indexed schedules regardless of renovation scope. Value-add of an LIHTC property is a compliance-first exercise, not a premium-capture exercise.
- **Luxury / Class A re-amenitization.** A "value-add" program on a 10-year-old Class A property is a re-amenitization play, not a classic value-add. Premium ceilings are lower (renters are already paying near-market) and the primary ROI driver is competitive defense (retaining renters from new supply) rather than rent lift. Use AvalonBay's re-development yield benchmarks (7–10%) rather than MAA/Camden's interior-redev benchmarks (17–20%).
- **Tax reassessment interaction.** In reassessment-on-transfer states (most states), a large value-add spend combined with a recent acquisition can trigger a reassessment that adds $300–$800/unit/yr in property taxes, partially offsetting premium capture. The Hold/Sell/Refi analyst skill and this execution tracker must handshake on whether the post-renovation NOI in the dashboard is net or gross of the reassessment impact.
- **Insurance premium impact of upgraded finishes.** Post-renovation replacement cost rises, which lifts property-insurance premiums by 10–25% depending on scope. Often overlooked in premium-capture net-NOI calculations.
- **Red flag: premium realized on first cohort ≠ durable premium.** The first 20–30 units renovated often capture higher premium than the steady state because the property has a novelty effect in the submarket. Project the steady-state premium from the 4th–8th month of leasing, not the first two months.
- **Red flag: high variance in actual cost per unit across the first 20 units.** Indicates the GC scope-of-work was not tight or the construction manager did not unitize pricing. Operators should re-bid before scaling.
- **Red flag: contingency burn > program-complete %.** If 60% of contingency is committed at 40% of program complete, overall overrun at completion is likely 15–25%+. Re-baseline budget immediately rather than absorbing through remaining contingency.
- **Red flag: renovated-unit concessions.** If the property is offering 1+ month free on renovated units, the premium is not real — the effective rent is below the underwritten rent premium. Report effective premium, not face premium.
- **Red flag: renovated-unit downtime > 14 days between completion and lease commencement.** Signal of mispricing or absorption weakness.
- **Red flag: schedule to complete slipping by >20% without contingency reserve reallocation.** Indicates both a schedule miss and a budget miss that has not been formally recognized in LP reporting.
- **Red flag: demographic shift away from the renovation tier.** A Class B property renovating up toward Class A finishes in a submarket where the Class A renter demographic is leaving (e.g., return-to-office coastal markets in 2020–2022) will fail premium capture even if scope is executed well. Cross-check with market study and demographic trend data before scaling the program.

## Open Questions

- Whether future versions should include a dedicated **rent-control jurisdiction overlay** (NYC, CA, Portland, St. Paul) that translates IAI / MCI / regulatory-cap mechanics into the premium-tracking framework.
- Whether the skill should include **specific metro-level premium realization benchmarks** (Austin, Phoenix, Dallas, Atlanta, Charlotte, Nashville, etc.) sourced from RealPage submarket data — valuable but data-currency-sensitive.
- Whether a companion **value-add financing tracker** (bridge-to-perm conversion, supplemental draw sizing, DSCR maintenance during construction) should be split out into its own skill — current scope includes construction execution but handshakes only lightly with the financing side.
- Whether the **steady-state premium vs first-cohort premium** distinction should be codified as a required reporting field (two separate numbers, or one steady-state field with a reporting floor of the 4th–8th unit window).
- Whether the skill should attempt to model the **reassessment / insurance / utility-cost drag** against gross premium capture as a structured calculation, or leave those as narrative flags.
- Whether to publish a **reference sponsor-LP-report variance template** (realized vs underwritten premium, realized vs underwritten cost, realized vs underwritten schedule) that LP reporting teams could adopt as a common format, or whether format proliferation in LP reporting means such a template would not be adopted.
