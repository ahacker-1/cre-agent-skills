# NOI Improvement Analyst — Phase 0b Research (R7)

> **Purpose.** Catalog of NOI-improvement levers an institutional multifamily asset manager can deploy at a stabilized, non-value-add, non-refi, non-retention-driven property. This research backs a downstream `noi-improvement-analyst` skill that will prioritize levers by impact × difficulty × time-to-realize.
>
> **Scope boundaries (inherited from pack plan).**
> - IN: Ancillary income programs, OpEx reduction, property-tax appeals, utility recovery (RUBS / submetering), insurance shopping and structures, technology-enabled revenue, concession-policy and loss-to-lease recapture at the operating level.
> - OUT: Value-add renovation capex (handled by R6); refinance-driven cash-flow improvement (R8); retention-driven revenue improvement (R4). Any lever whose primary mechanism is a rent premium from renovation, a coupon reduction from refi, or a turnover-cost reduction from retention is explicitly deferred to the owning research agent.
>
> **Alignment.** Vocabulary, formulas, and classification rules inherit from `_taxonomy-seed.md` (Phase 0a). Per-unit ranges and class/regional multipliers defer to `knowledge/multifamily-benchmarks.md`. This file contains *lever-library* content, not definitions — definitions route to the taxonomy.

---

## 1. Purpose and Scope Statement

The `noi-improvement-analyst` skill consumes a stabilized property's T-12, rent roll, ancillary income schedule, and OpEx detail, and produces a prioritized action list of NOI-improvement initiatives with: (a) estimated $/unit/year impact with a confidence range, (b) capital requirement (one-time + ongoing), (c) time-to-realize (months to steady-state), (d) difficulty (operational friction, tenant backlash, legal risk), and (e) sequencing dependencies. The skill does NOT propose physical renovation (→ R6), does NOT re-lever the capital stack (→ R8), and does NOT model retention impacts per se (→ R4) — though it must flag retention-adjacent downside on any lever that could materially affect resident churn (e.g., aggressive RUBS rollout in a soft-market submarket).

**In scope — lever families covered in this document:**
1. Ancillary income lever library (§3).
2. Utility recovery (RUBS / submetering) with state-legality overlay (§3, §4).
3. Property-tax appeal (success rates, jurisdiction variance) (§3, §4).
4. Insurance shopping, captive, and parametric structures (§3).
5. OpEx-reduction precedents: centralized procurement, regional maintenance pods, energy-efficiency retrofits (§3).
6. Technology-enabled revenue (AI leasing, self-guided/AI-guided tours) and concession-policy optimization at the operating level (§3).
7. Prioritization framework: impact × difficulty × time-to-realize (§4).

**Out of scope:** Unit-interior renovation ROI, in-unit smart-home deployments whose primary sell is rent premium (which routes to R6), refinance / recap economics, and retention-program design. Where a lever listed below overlaps with those adjacent packs, a routing note directs the downstream skill to the correct research file.

---

## 2. US-Only Assumptions

- Conventional, stabilized multifamily, 5+ unit, institutional quality. Affordable/LIHTC and student housing are excluded from default ranges; the skill should flag and require operator-specific overrides if applied to those subtypes.
- RUBS-legality notes are state-level US only; landlord–tenant utility-billing law outside the US is not covered.
- Property-tax appeal mechanics vary by state and county. The success-rate ranges in §3 are US national averages cited from IAAO / Lincoln Institute / National Taxpayers Union Foundation data and are NOT underwriting-grade for any specific jurisdiction.
- Insurance market commentary reflects the post-2022–2024 US hurricane cycle (Ian 2022, Helene/Milton 2024) and 2025 marketplace conditions per WTW, Aon, and captive-industry sources.
- Benchmarks for per-unit ancillary revenue defer to `knowledge/multifamily-benchmarks.md` (Ancillary Income Benchmarks table). Ranges in this research file are **corroboration** against external institutional sources, not replacements.

---

## 3. Source Tiers and Lever Library

### Source Table

| # | Source | Tier | URL | Date | Notes |
|---|---|---|---|---|---|
| 1 | NAA / IREM / BOMA — Income/Expense IQ 2024 (2024 operating data) | 1 | https://naahq.org/news/momentum-management-navigating-elevated-costs-constrained-operating-environment | 2025 | Other income $1,482/unit +5.4% YoY; concessions $82/unit +30.9% YoY; vacancy+rent loss $1,323/unit +2.6% YoY — 4,666 properties, ~1.09M units, 109 metros |
| 2 | NMHC — Industry Benchmarks Data / Research Reports | 1 | https://www.nmhc.org/research-insight/industry-benchmarks/about-the-industry-benchmarks-data/ | 2025 | NMHC ancillary-revenue and fee-transparency (RETTC / MITS 5.0) guidance for operators |
| 3 | John Burns Research & Consulting — "NMHC Apartment Strategies 2026 — Multifamily Consequences, Opportunities" | 1 | https://jbrec.com/insights/nmhc-apartment-strategies-2026-multifamily-btr-trends/ | 2026 | Explicit call-out that the value-add upside is now about NOI levers (RUBS, fee optimization, parking, pet fees, bulk internet), not big rent hikes |
| 4 | Fannie Mae Multifamily Guide — Catastrophic Risk Insurance | 1 | https://mfguide.fanniemae.com/node/4451 | 2025 | Agency convention for catastrophic/parametric overlays on agency-financed multifamily |
| 5 | Lincoln Institute of Land Policy — Assessment Regressivity research | 1 | https://www.lincolninst.edu/publications/articles/assessment-regressivity | 2024 | Foundational research underpinning the 40–60% appeal-success-rate national average; regressivity skews high-value assessments disproportionately |
| 6 | Multifamily Dive — "The pros, cons of centralized maintenance" (Buckingham case study) | 2 | https://www.multifamilydive.com/news/centralization-apartment-operations-maintenance-service-pods/724695/ | 2024 | 10-mile-radius maintenance pod model; tech-enabled routing; specialization by skill set (HVAC, plumbing) |
| 7 | RealPage Analytics — Loss-to-Lease and Renewal Rent Trends | 2 | https://www.realpage.com/analytics/here-are-4-implications-of-loss-to-lease-dropping-below-long-term-average/ | 2024 | LTL long-term average ~4.5%; renewal spread larger when LTL is larger; concession-burn dynamics into 2026 |
| 8 | WTW — Insurance Marketplace Realities 2025 (Middle Market) | 2 | https://www.wtwco.com/en-us/insights/2024/10/insurance-marketplace-realities-2025-middle-market | 2024 | Habitational / CAT-exposed accounts remain challenged; captives increasingly used for middle-market operators |
| 9 | Captives.Insure — March 2025 Captive Insights | 2 | https://captives.insure/insights/march-2025-captive-insights | 2025 | ~30% of newly formed captives in prior year include a parametric component; deductible buy-down via parametric is common structure |
| 10 | Triple-I — Parametric Insurance Gains Traction Across U.S. | 2 | https://insuranceindustryblog.iii.org/parametric-insurance-gains-traction-across-u-s/ | 2025 | Industry institute perspective on parametric as complement-not-replacement; basis-risk warning |
| 11 | NetsmartRE / RealPage press release — OpsTechnology acquisition | 2 | https://www.realpage.com/news/realpage-acquires-opstechnology/ | 2008 (platform now RealPage-owned) | Centralized MRO/capital procurement typically saves **5–10% of controllable MRO and capital spend** at adopting operators |
| 12 | EliseAI — Self-Guided Apartment Tours / AI-Guided Tours | 2 | https://eliseai.com/blog/self-guided-apartment-tours-reinvented-introducing-eliseais-ai-guided-tours | 2025 | 60% of prospects prefer weekend/after-hours tours; AI-guided tours as the productivity layer on top of SGT |
| 13 | NCLC Digital Library — An Introduction to Ratio Utility Billing Systems for Tenant Advocates | 2 | https://library.nclc.org/article/introduction-ratio-utility-billing-systems-tenant-advocates | 2024 | Tenant-advocacy perspective; documents variance in state legality and the markup/profit prohibition |
| 14 | O'Connor & Associates — Commercial Property Tax Protection Program | 3 | https://www.poconnor.com/commercial-property-tax-protection-program/ | 2025 | Industry practitioner — $213M in 2025 client savings claimed; 49-state commercial coverage incl. multifamily; 25–40% contingency fee |
| 15 | AppealDesk — Property Tax Appeal Success Rates by State (aggregates IAAO / Lincoln / NTUF data) | 3 | https://www.appealdesk.com/blog/property-tax-appeal-success-rates-by-state | 2026 | 40–60% national success rate; 65–85% with professional evidence; extreme jurisdiction variance (Hays County TX 98.68% vs Cook County IL 62%) |
| 16 | National Taxpayers Union Foundation — overassessment research (as quoted in AppealDesk and practitioner sources) | 2 | https://www.ntu.org/foundation | 2024 | 30–60% of US residential properties over-assessed; <5% of homeowners ever appeal |
| 17 | Multifamily Executive — "Ancillary Income Can Boost Bottom Line" | 3 | https://www.multifamilyexecutive.com/property-management/ancillary-income-can-boost-bottom-line_o | 2024 | ~65% of MF operators charge fees for extras; ancillary can be 10%+ of revenue at best-operated communities; 7–9% EGI share typical (NARPM benchmark) |
| 18 | ENERGY STAR — Smart Thermostats product criteria and savings | 1 | https://www.energystar.gov/products/smart_thermostats | 2025 | ~8% HVAC savings, ~$50/unit/yr average; demand-response compatibility required for certification |
| 19 | US Department of Energy — building-smart-controls savings | 1 | (DOE commentary aggregated via ENERGY STAR Playbook and CRE Insight Journal) https://creinsightjournal.com/the-energy-star-playbook-which-retrofits-move-your-score/ | 2024 | Smart controls / BMS deliver 10–20% energy reduction without mechanical-equipment replacement |
| 20 | Dune Labs / Synergy Utility Billing — RUBS State Laws overview | 3 | https://dunelabs.ai/2022/11/07/things-you-need-to-know-about-rubs-regulations-across-states/ | 2024 | State-by-state RUBS legality; "no state outright prohibits RUBS" but local rent-control cities can restrict |
| 21 | Bornstein Law — California Ratio Utility Billing Systems | 3 | https://bornstein.law/california-ratio-utility-billing-systems/ | 2024 | California municipal overlays; Mountain View CSFRA ruling that RUBS fees count as rent under local rent control; Santa Monica / San Diego litigation context |
| 22 | Luxer One — Turning Package Management into a New Revenue Stream | 3 | https://www.luxerone.com/new-revenue-stream-for-multifamily-communities/ | 2025 | Package locker SaaS/subscription revenue model; average MF community receives 250–400 packages/week (NMHC cited) |
| 23 | Multifamily Affordable Housing Business — "Owners Embrace Ancillary Income, Despite Risk" | 3 | https://multifamilyaffordablehousing.com/owners-embrace-ancillary-income-despite-risk/ | 2024 | Greystar junk-fee class action (Colorado, Jan 2024) as the primary fee-transparency/regulatory-risk warning |
| 24 | Fetch / Tour24 — self-guided & AI-assisted touring outcomes | 3 | https://www.tour24.io/article/how-ai-and-self-guided-tours-are-transforming-multifamily-leasing-strategies/ | 2025 | Industry practitioner stats: AI leasing produced 44.8% higher lead-to-lease conversion and 30% more lead-to-tour conversion at adopter communities |

**Citation gate.** 24 external sources, of which Tier 1 = 7 (¹ NAA/IREM/BOMA, ² NMHC, ³ JBREC, ⁴ Fannie, ⁵ Lincoln, ¹⁸ ENERGY STAR, ¹⁹ DOE via ENERGY STAR Playbook) and Tier 2 = 9 (⁶ MF Dive, ⁷ RealPage, ⁸ WTW, ⁹ Captives.Insure, ¹⁰ Triple-I, ¹¹ RealPage/OpsTechnology, ¹² EliseAI, ¹³ NCLC, ¹⁶ NTUF) = 16 Tier 1+2. Gate: ≥10 total (✓), ≥6 Tier 1/2 (✓). Met.

---

### Lever Library (the core of this research)

The lever library is organized by **category → lever → mechanism → typical impact → capital / difficulty / time-to-realize → risks**. This is the structural content the downstream skill consumes. Impact ranges reconcile to `knowledge/multifamily-benchmarks.md` Ancillary Income Benchmarks table where applicable; any divergence is flagged inline.

---

#### 3A. Ancillary Income Levers

**3A.1 Pet Rent Program**

- **Mechanism.** Monthly pet rent per pet charged on top of base rent, supported by pet deposit ($200–$500) and often non-refundable pet fee ($150–$400). Differentiated pricing by weight class is common.
- **Typical impact.** **$25–$75/pet/month** [Repo KB multifamily-benchmarks.md Ancillary row]; corroborated at **$25–$50/pet/month** by Multifamily Executive [¹⁷]. Penetration 40–60% of units typical [Repo KB]. At 50% penetration and $40/mo average: **~$240/unit/yr** incremental NOI.
- **Capital / difficulty / time-to-realize.** Near-zero capex; policy rollout + lease-addendum. **Time-to-realize: 6–18 months** (only captures on new leases and renewals).
- **Risks.** Fair-housing concern if policy effectively discriminates against assistance animals — assistance animals are NOT pets under FHA and cannot be charged pet rent. Greystar class-action [²³] is a cautionary note on disclosure practice.

**3A.2 Parking (covered, garage, reserved, EV)**

- **Mechanism.** Unbundle parking from base rent; tiered pricing (open > covered > reserved > garage > EV-charger spots). Most impactful in dense suburban and urban properties with scarcity.
- **Typical impact.** **$50–$200/unit/mo** [Repo KB]. EV-charger premium $25–$50/mo on top for assigned EV spots where installed.
- **Capital / difficulty / time-to-realize.** Negligible if already-built parking; EV-charger install is capex ($4,000–$8,000 per charger stall) but typically routes to capex planning, not operating NOI — flag to R6 if material. Time-to-realize 12–24 months (lease rollover).
- **Risks.** Softens on value in markets where street parking is free and abundant (tertiary, low-density suburban). Jurisdictions with parking-minimums reform may reduce marketability.

**3A.3 Storage Units**

- **Mechanism.** Convert attic, basement, garage corners, or outdoor yard into contracted storage. Often revenue-share with a third-party locker vendor or 100% captive operator revenue.
- **Typical impact.** Repo KB: **$50–$150/unit/mo** for a rented storage unit; at ~20–40% unit-penetration: **~$120–$360/unit/yr** portfolio average. External ranges (Multifamily Executive [¹⁷]) cite **$25–$75/mo**, which likely reflects lower-density / walk-up markets — pack range is $25–$150/mo, penetration-dependent.
- **Capital / difficulty / time-to-realize.** Minor build-out ($500–$2,000 per unit) if chain-link storage cages; heavier if finished. Time-to-realize 3–12 months.
- **Risks.** Fire-code and egress review required before rollout. HOA / condo conversions sometimes carry storage-assignment restrictions. Do not stack on top of amenity-parking spaces where parking scarcity already extracts that value.

**3A.4 Short-Term Rental / Month-to-Month Premium**

- **Mechanism.** Premium charged above base rent for leases shorter than 12 months (month-to-month, 3-month, 6-month). Protects the operator against turn-cost exposure on short tenants.
- **Typical impact.** **$50–$200/unit/mo** premium when applied (only on the short-term cohort, not portfolio-wide) — per pack guidance, realized NOI impact depends on short-term-lease mix.
- **Capital / difficulty / time-to-realize.** Zero capex, policy change. Time-to-realize 6–12 months.
- **Risks.** Local short-term-rental ordinances (Airbnb-style regulations) can constrain use even for direct-operator month-to-month. Some jurisdictions treat ≤30-day rentals as hotel occupancy for tax purposes.

**3A.5 Technology Package / Smart-Home**

- **Mechanism.** Bundled smart-lock, smart-thermostat, leak-detection, and building-wifi offering charged as a monthly tech fee.
- **Typical impact.** **$25–$50/unit/mo** per pack default.
- **Capital / difficulty / time-to-realize.** Capex $300–$1,200/unit for hardware; time-to-realize 18–36 months portfolio-wide. **Routing note:** If the primary economic justification is a rent premium on the base lease (and not a separate tech fee), this lever belongs to R6 (value-add renovation). Here it is scoped only as a **separate tech-fee** line, not a base-rent repositioning.
- **Risks.** Resident backlash when the fee is perceived as mandatory and bundled with services they don't value. Smart-lock systems have well-documented security concerns — operator must own the incident-response plan.

**3A.6 Valet Trash**

- **Mechanism.** Resident pays a fee; vendor picks up trash from door nightly.
- **Typical impact.** **$25–$50/unit/mo** gross (Repo KB aligns at $20–$40). Vendor cost typically $10–$20/unit/mo, so **net $10–$30/unit/mo** retained = **$120–$360/unit/yr** contribution. Lincoln Property Co. case cited in Multifamily Executive [¹⁷]: 300-unit community nets ~$20,500/yr, validating mid-range.
- **Capital / difficulty / time-to-realize.** Near-zero capex. Time-to-realize 6–12 months (contract + rollout).
- **Risks.** Must be disclosed as a mandatory fee per fee-transparency (NMHC RETTC / MITS 5.0) and post-2024 state junk-fee legislation (CA, CO, MN). Greystar class action [²³] specifically named valet trash as a misleading fee.

**3A.7 Package Locker / Delivery Subscription**

- **Mechanism.** Charge a monthly fee for 24/7 locker access or delivery-to-door service. Luxer "Luxer as a Service" subscription model converts capex to opex [²²]. Fetch delivers packages to doors on a per-resident fee model.
- **Typical impact.** Pack default **$5–$15/unit/mo**; locker hardware payback within ~12 months of rollout at subscription-fee communities [²²]. Critical mass is high: average MF community receives **250–400 packages/week** [²² citing NMHC].
- **Capital / difficulty / time-to-realize.** Capex $20,000–$60,000 per community for Luxer-style lockers, or $0 upfront on Luxer-as-a-Service. Time-to-realize 3–9 months.
- **Risks.** Amazon Hub restricts which carriers hit the locker (though marketing claims carrier-agnostic) — lockers that accept less than 100% of packages create staff workload spillover and resident complaints.

**3A.8 RUBS Administrative Fee**

- **Mechanism.** A flat per-unit admin fee layered on top of the RUBS utility pass-through, to compensate the operator for billing/collection overhead. Typically $3–$8/unit/mo.
- **Typical impact.** **$3–$8/unit/mo = $36–$96/unit/yr.**
- **Capital / difficulty / time-to-realize.** None incremental if RUBS is already running. Time-to-realize 0 (next billing cycle).
- **Risks.** In California per Bornstein Law [²¹], any RUBS-related fee may be scrutinized as part of rent under local rent-control ordinances (Mountain View CSFRA ruling). NCLC [¹³] position: any admin fee above actual billing cost is effectively a markup and prohibited.

**3A.9 Application Fees, Admin Fees, Late Fees**

- **Mechanism.** Screening application fee ($50–$100/application), admin / move-in fee ($200–$400 one-time), late fees (typically 5% of rent or $75 cap).
- **Typical impact.** Repo KB amortized estimates: application $5–$15/unit/mo, late fees $10–$25/unit/mo. Combined: **$15–$40/unit/mo = $180–$480/unit/yr.**
- **Capital / difficulty / time-to-realize.** Zero. Time-to-realize immediate.
- **Risks.** Application-fee caps exist in CA, WI, and other states (e.g., CA application fee capped at ~$59.67 as of 2025 CPI adjustment). Junk-fee laws in 2024–2025 increasingly restrict admin fees at move-in.

---

#### 3B. RUBS / Ratio Utility Billing System — Dedicated Treatment

**Mechanism.** RUBS allocates the property's total utility bill (water/sewer most common, trash second, sometimes gas/electric in master-metered buildings) across residents by an allocation formula (square footage, occupancy count, bedroom count, or hybrid) rather than actual consumption [¹³][²⁰]. RUBS is distinct from submetering, which measures actual per-unit consumption. Submetering generally produces higher recovery rates (85–95% of owner utility cost) but requires physical infrastructure; RUBS recovers 70–90% of costs depending on formula and vacancy vacancy adjustments, with no hardware spend.

**Typical impact.** **$30–$80/unit/mo on utilities recovered, net of vendor fee** — pack default range consistent with JBREC commentary [³] that explicitly names RUBS among primary NOI levers for 2026. Repo KB shows a wider range of $50–$150/unit/mo — the pack defaults to the narrower range here for conservatism on water-only recovery; hitting the top of the repo-KB range generally requires billing multiple utility streams (water + sewer + trash + gas) and is market-dependent.

**Capital / difficulty / time-to-realize.** Near-zero capex if water-only RUBS (no hardware). Submetering retrofit is $300–$800/unit capex. Time-to-realize 3–6 months for RUBS; 12–24 months for full submetering retrofit.

**State-level legality overlay (mandatory for downstream skill).** No US state currently imposes a blanket prohibition on RUBS for conventional multifamily [¹³][²⁰]. Material variance is at the **local / rent-control-ordinance** level:

| State | Status | Key Statute / Rule | Operator Action |
|---|---|---|---|
| **California** | Permitted statewide, no statewide ban. Local overlays critical. | Civil Code §1940.9 (submetering disclosure); Mountain View Community Stabilization and Fair Rent Act (CSFRA) — RUBS fees treated as part of rent under local rent control. Litigation in Santa Monica, San Diego [²¹]. | Before rollout: check local rent-control jurisdiction. In rent-stabilized markets (LA RSO, SF RSO, Oakland, Berkeley, Santa Monica, San Diego with AB 1482 overlay), assume RUBS is either restricted or treated as a rent increase subject to annual cap. |
| **Texas** | Permitted. Widely used in 100+ unit communities [²⁰]. | Texas Water Code §13.503 + Utilities Code governs allocation-based billing for water/sewer — provider registration and disclosure requirements, but RUBS is explicitly allowed. | Register with Texas PUC (now operates under the Texas PUC's water-utility-allocation rules) if required; comply with tenant-disclosure requirements. |
| **Illinois** | Permitted statewide; no ban [²⁰]. | Chicago ordinances impose additional disclosure on lease. Local compliance required. | Build local-ordinance check into lease template for Chicago assets; other Illinois jurisdictions generally permissive. |
| **Florida** | Permitted statewide; no ban [²⁰]. | PSC rules govern metered recovery; RUBS permitted for water/sewer with standard disclosure. | Standard disclosure language in lease; no material Florida-specific constraint. |
| **Other high-regulation states** | Various. | NY, MA, NJ, MD have varying restrictions; NY City's "Air Conditioning Surcharge" rules and master-meter pass-through restrictions apply under NYC HMC. | Require legal review before rolling out RUBS in any Northeast market. |

**Source caveat.** The state-by-state citations above aggregate Tier 2/3 practitioner sources [²⁰][²¹] plus NCLC [¹³]. Downstream skill must not treat these as legal advice. Pack convention: for any state-regulated rollout, require operator to attach a jurisdiction-specific legal opinion before the skill recommends implementation.

**Universal RUBS rules (from NCLC [¹³]):**
1. Markup-for-profit is **prohibited** in every US jurisdiction. Operator may pass through actual utility cost plus reasonable admin, not above.
2. Allocation formula must be disclosed to tenant at lease signing.
3. Changing the allocation formula mid-lease generally requires tenant consent or lease-renewal-cycle implementation.

---

#### 3C. Property-Tax Appeal

**Mechanism.** Challenge the assessed value of the property with the local assessing authority (informal hearing, appraisal review board, or tax court), typically via (a) sales-comp approach, (b) income-capitalization approach using actual T-12 NOI, and/or (c) cost approach. For multifamily, income approach is dominant.

**Typical impact.** A successful appeal reduces assessed value by **5–20%** typical, with **15%+ reductions** on over-assessed properties. At a 2% effective tax rate, a 10% AV reduction on a $20M property = $40,000/yr OpEx reduction = **~$200/unit/yr on a 200-unit deal**, which at a 5.5% cap rate is ~$730,000 of value. In Tennessee's 2025 reassessment [cited in Ryan commentary from search], successful appeals reduce taxes for the next four years, compounding value.

**Success rates — national benchmarks.**

| Metric | Value | Source |
|---|---|---|
| National appeal success rate (any reduction) | **40–60%** | IAAO and Lincoln Institute research [⁵], aggregated and cited in AppealDesk [¹⁵] |
| Success rate with professional evidence and representation | **65–85%** | AppealDesk [¹⁵] aggregating professional-firm outcome data |
| Share of US properties over-assessed | **30–60%** | National Taxpayers Union Foundation [¹⁶] |
| Share of owners who actually appeal | **<5%** (homeowner base); **higher for commercial/MF, but <30% in most jurisdictions** | NTUF [¹⁶]; O'Connor [¹⁴] commercial commentary |
| O'Connor 2025 client savings claim | **>$213M** across 49 states, commercial including multifamily | O'Connor [¹⁴] |

**Jurisdiction variance.** Extreme, and central to underwriting any appeal opportunity. **Hays County, TX: 98.68% success rate** (routine informal-settlement culture). **Cook County, IL: 62%** (adversarial review board). These two end-points from AppealDesk [¹⁵] bracket the realistic range. Additional pack-level guidance: Texas counties generally exceed 75% for protested commercial properties [NTUF/O'Connor]; Cook County IL, NJ, and NY (outside NYC) are middle-of-range; California (Prop 13 limits outside transfer years) is structurally appeal-rare.

**Capital / difficulty / time-to-realize.** Typically $2,500–$10,000 flat fee or 25–40% contingency of savings [O'Connor at 25–40%, ¹⁴]. Time-to-realize 6–18 months from filing to decision, then tax-bill impact next cycle. Many jurisdictions allow multi-year lookback on successful appeals.

**Risks.** Reassessment-up risk if property has been under-assessed (rare but possible in transfer-reassessment states like TX, FL, NC). Appeal firms on contingency have no downside for the owner; flat-fee firms carry execution risk.

**Repo-KB interaction.** Property-tax ranges are defined in `knowledge/multifamily-benchmarks.md` Property Taxes by State table. The appeal lever here is not a substitute for those benchmarks — it is an overlay to model post-appeal values when the initial assessment is plausibly high.

---

#### 3D. Insurance Shopping and Structures

**Mechanism.** Stabilized-property insurance programs include (1) standard property/liability RFP shopping, (2) captive insurance (single-parent or cell captive for large portfolios), and (3) parametric catastrophe layers for hurricane/earthquake/wildfire exposure.

**(1) Annual RFP shopping.** **Annual RFP is the institutional norm** for any portfolio above ~$50M insured value. WTW [⁸] notes "CAT-exposed / habitational" accounts face continued pressure to differentiate — meaning well-marketed, loss-controlled accounts can achieve materially better renewal terms than non-marketed accounts. Typical savings from a disciplined RFP (vs. broker-direct renewal): **5–15% of premium** in a normal market; negligible or negative in a very hard market.

**(2) Captive insurance.** A single-parent captive becomes economic above **~$1M–$3M in annual premium** for a portfolio. Captives can insure deductibles (deductible buy-down), high-layer property, and increasingly, parametric triggers. ~30% of newly formed captives in the prior year included a parametric component [⁹]. Captives carry setup and domicile costs (Vermont, Cayman, Bermuda most common) and require ongoing actuarial certification.

**(3) Parametric catastrophe.** Post-Hurricane Ian (2022) and Helene/Milton (2024), parametric hurricane coverage has become mainstream for Florida/Gulf habitational portfolios [⁴][⁹][¹⁰]. Payout triggers on an objectively measured parameter (central pressure, wind speed, storm surge depth) rather than indemnity. Payouts in **~14 days** (Automated Petroleum case after Ian / Nicole via Swiss Re STORM program [⁹]) vs. months for traditional indemnity. Fannie Mae Multifamily Guide [⁴] explicitly accommodates catastrophic-risk insurance structures on agency debt.

**Basis risk — mandatory disclosure in any recommendation.** Parametric payouts may not match actual losses. A $150M Hurricane Beryl parametric cat bond did not pay because air pressure narrowly missed the trigger [¹⁰]. Pack rule: **parametric is a complement, not a replacement** for traditional indemnity coverage, and operators should not buy parametric as primary CAT coverage.

**Typical NOI impact.** Insurance-RFP savings 5–15% of premium in a normal-to-soft year. For a $800/unit/yr insurance line item (Class B non-coastal, Repo KB range), a 10% save = **$80/unit/yr**. For a $1,200/unit/yr coastal FL/TX line item, a 10% save = **$120/unit/yr**. Captive and parametric structures typically are value-captured over a multi-year horizon rather than an immediate NOI lift; the lever on annual NOI is the captive's **underwriting-profit retention** plus investment income on captive reserves.

**Capital / difficulty / time-to-realize.** RFP: ~$5,000–$25,000 broker/consultant fee; time-to-realize 3–6 months (next renewal). Captive: $100K–$500K setup; ongoing $50K–$200K/yr; time-to-realize 18–36 months. Parametric: broker-structured, typical execution 60–120 days.

---

#### 3E. OpEx Reduction Precedents

**3E.1 Centralized Purchasing (MRO + Capital).**
- **Mechanism.** Portfolio-level contracted suppliers for maintenance, repair, operating supplies, and project-capital materials, typically routed through a purchasing platform (RealPage OpsBuyer/OpsMarket, FacilGo, Connexus).
- **Typical impact.** **5–10% savings on controllable MRO and capital spend** per OpsTechnology/RealPage self-reported adopter data [¹¹]. Applied to a Repo KB Class B OpEx stack of ~$7,500/unit/yr, excluding non-controllables (taxes, insurance, utilities, payroll, management), the controllable base is ~$2,500–$3,500/unit/yr (R&M + turnover + contract services + supplies + admin materials). 7% of that = **$175–$245/unit/yr** typical save, realized over 12–24 months after contract rollout.
- **Capital / difficulty / time-to-realize.** Platform licensing $10K–$50K/yr plus integration time. Time-to-realize 12–24 months for full adoption; 6 months for partial pilot.
- **Risks.** Centralization often conflicts with site-manager discretion; property-level pushback is the #1 cause of failed rollouts per Multifamily Dive [⁶] case studies.

**3E.2 Regional Labor Pooling / Maintenance Pods.**
- **Mechanism.** Instead of fully-staffing each property, operator creates a regional maintenance "pod" covering 4–5 properties within a **~10-mile radius** [⁶ Buckingham case study], with dispatch routed by skill set (HVAC, plumbing, electrical) via tech-enabled work-order system.
- **Typical impact.** Payroll-line savings of 10–25% via elimination of duplicated generalist positions, offset partially by higher wages for specialized technicians and pod-leader roles. Net typical save: **$150–$400/unit/yr** on payroll at Class B/C. Buckingham [⁶] explicitly states the intent was **efficiency over payroll reduction** — the save shows up partly as unfilled positions being absorbed by the pod.
- **Capital / difficulty / time-to-realize.** Tech investment $20K–$80K per region (dispatch + mobile). Time-to-realize 12–24 months; requires geographic density.
- **Risks.** Resident-satisfaction risk on response-time during transition; requires strong dispatch software and robust backup scheduling. Not applicable to geographically dispersed portfolios.

**3E.3 Third-Party Contract Renegotiation.**
- **Mechanism.** Systematic renegotiation at renewal of landscaping, pool maintenance, pest control, elevator, fire/life safety, and trash contracts, often bundled for scale discount.
- **Typical impact.** **5–15% savings on contract-services line** [pack default, consistent with [⁶][¹¹] procurement outcomes]. Repo KB contract services $250–$600/unit/yr Class B, so **$15–$90/unit/yr save**.
- **Capital / difficulty / time-to-realize.** Zero capex, staff time only. Time-to-realize 6–18 months (aligned with contract-renewal dates).
- **Risks.** Service-quality dip if lowest-bidder approach; pack convention: always require references and site visits before switching providers on essential-safety contracts (fire/life safety especially).

**3E.4 Energy-Efficiency Retrofits.**
- **Mechanism.** LED retrofit (common areas, corridors, stairwells, parking); smart thermostats in-unit and vacant-unit automation; low-flow fixtures; demand-response HVAC controls; solar for common-area load (where PPA-structured).
- **Typical impact.**
  - **LED common-area retrofit:** 50–66% lighting energy reduction; 2-year typical payback after rebates [DOE / ENERGY STAR commentary via ¹⁹, plus Marriott case cited]. At ~$150–$300/unit/yr of owner-paid common-area lighting cost, save **$75–$200/unit/yr**.
  - **Smart thermostats (ENERGY STAR-certified):** ~8% HVAC savings, ~**$50/unit/yr** on average [¹⁸]; multifamily-specific deployments with vacant-unit automation achieve materially more — one enterprise deployment cited ~$17K/yr/community vacant-unit savings plus 27% in-unit usage reduction, though this is an upper-bound case.
  - **Smart controls / BMS broadly:** DOE commentary (aggregated via ENERGY STAR Playbook [¹⁹]): **10–20% building-level energy reduction** without mechanical-equipment replacement. On a Class B $1,500/unit/yr utility line item, 15% save = **$225/unit/yr.**
- **Capital / difficulty / time-to-realize.** LED: $150–$400/unit (net of rebates); 18–36 month payback. Smart thermostats: $100–$250/unit installed, 1–3 year payback. Time-to-realize 6–18 months on rollout + measurement.
- **Repo-KB routing.** Larger in-unit retrofit programs (HVAC replacement, solar PV, full building envelope) whose primary justification is a rent premium or major capex underwrite route to R6 (value-add renovation). This section covers only energy retrofits justified purely by OpEx-reduction NOI math.
- **Risks.** Utility-rebate programs have budget caps and non-guaranteed renewals; do not embed rebate revenue in steady-state NOI. Smart thermostats face HVAC-equipment compatibility issues in ~10–15% of older stock.

---

#### 3F. Technology-Enabled Revenue

**3F.1 AI Leasing / AI-Guided Tours.**
- **Mechanism.** AI chat assistant handles first-touch responses 24/7, qualifies leads, books tours; self-guided tours with IoT unit-unlock; AI-guided tours where conversational AI accompanies the prospect via SMS/voice [¹²].
- **Typical impact.** Adopter-reported **44.8% higher lead-to-lease conversion** and **30% more lead-to-tour conversion** [²⁴]. On a lease-up or churning-property rent roll, this compresses days-vacant materially. The NOI impact routes through vacancy reduction, not fee income; pack default: **$100–$300/unit/yr** implied NOI lift on a stabilized property with prior response-lag problems, zero lift where leasing response was already strong. Also frees leasing headcount for higher-value tasks (lease-up push, renewal conversion).
- **Capital / difficulty / time-to-realize.** SaaS subscription $50–$200/unit/yr; IoT self-guided tour hardware ~$200–$500/unit one-time. Time-to-realize 3–9 months.
- **Risks.** Response-time claims are self-reported by vendors; independent validation is thin. Regulatory risk around AI-communication disclosure (Colorado AI Act, California AB 2013) is emerging.

**3F.2 Concession-Policy Optimization at the Operating Level.**
- **Mechanism.** At the operating level, concession-policy choice between (a) upfront free-month on a 12-month lease vs. (b) spread-discount (reduced monthly rent) vs. (c) concession at renewal (instead of new-lease). RealPage [⁷] explicitly documents that **upfront concessions create cleaner renewal-pricing** because the resident psychologically returns to the headline rent, whereas spread concessions anchor the tenant at the discounted effective rent.
- **Typical impact.** Hard to generalize without property-specific concession schedule. Pack default guidance:
  - Upfront-month-free > spread-discount for LTL recapture and NOI Year-2 per the RealPage analysis.
  - Concession-at-renewal is preferable to concession-on-new when market is soft for new-lease but retention is the primary economic driver — but that routes to R4 (retention-driven improvement) and is not a lever owned here.
- **Capital / difficulty / time-to-realize.** Zero capex. Time-to-realize 12 months (full cycle through renewals).
- **Risks.** In markets with broad concession-rich competing supply (RealPage 2026 outlook [⁷]), burning off concessions is not feasible even with the policy switch.

**3F.3 Loss-to-Lease Recapture at Renewal.**
- **Mechanism.** Push renewal rents toward market when in-place rents sit materially below market rate. Rule of thumb from RealPage [⁷]: **the larger the LTL, the larger the justifiable renewal bump**.
- **Typical impact.** If LTL is 10%, don't assume 100% recapture in Year 1 — cap at **3–5% annual** until LTL closes [RealPage + Tactica RES commentary]. On a $18,000/unit/yr GPR, 3% captured = **~$540/unit/yr** in Year 1; full 10% recapture over 3 years = cumulative **~$1,800/unit/yr** by stabilization.
- **Capital / difficulty / time-to-realize.** Zero capex. Time-to-realize 12–36 months for full recapture.
- **Risks.** Retention-driven move-out spike risk — this lever materially intersects with R4. Pack rule: any LTL-recapture push above **5% in a single renewal cycle** routes to R4 for retention-model validation before implementation.
- **Scope note.** This lever is included here because the **mechanism** is a pricing-policy change (operating-level revenue optimization), not a retention-program design. The retention-model validation (what renewal bump drives what churn rate) routes to R4.

---

## 4. Benchmark and Formula Decisions / Prioritization Framework

The downstream skill will produce a ranked lever list. Ranking uses **three dimensions**:

### 4.1 Impact (NOI lift per year, $/unit/yr)
Each lever in §3 carries a pack-default impact range. The skill will:
1. Apply the Repo KB's Class A/B/C and regional multipliers from `multifamily-benchmarks.md` to adjust ranges.
2. Require operator input on current state (e.g., is RUBS already running? has property tax been appealed in last 24 months?) to avoid double-counting.
3. Bound the Year-1 and Year-3 impact separately — most levers realize over 12–24 months, not immediately.

### 4.2 Difficulty (operational friction, legal/regulatory risk, tenant backlash)
**Scoring rubric (1 = easy, 5 = hard):**
- **1 (easy):** Zero capex, no lease-template change, no regulatory exposure. E.g., insurance RFP in soft market; contract renegotiation at renewal date.
- **2:** Lease-template change only; no hardware or staff restructuring. E.g., pet-rent rollout, parking unbundle.
- **3:** Hardware or tech install required; modest capex; measurable resident-experience change. E.g., smart thermostats, package lockers.
- **4:** Staff restructuring OR regulatory exposure. E.g., regional maintenance pods, RUBS in CA under rent-control overlay.
- **5:** Captive setup, parametric structure, or fundamental billing-model change in a high-regulation jurisdiction.

### 4.3 Time-to-Realize (months to steady-state NOI contribution)
- **Fast (0–6 months):** Insurance RFP, application-fee increase, admin-fee change, RUBS admin fee, contract renegotiation at next cycle, LTL bump at next renewal.
- **Medium (6–18 months):** Pet rent, parking unbundle, package lockers, storage buildout, valet trash, LED retrofit common area, smart thermostats, centralized procurement partial.
- **Slow (18–36+ months):** Property-tax appeal cycle (decision then tax-year flow-through), regional-maintenance-pod rollout, captive setup, full centralized procurement adoption, full LTL recapture.

### 4.4 Scoring Aggregation (pack default)
```
Priority Score = (Impact in $/unit/yr ÷ Difficulty Score) × (1 ÷ Time-to-Realize in years)
```
Rank levers descending. The skill should present the top 10 by score, with manual override allowed per operator-specific priorities.

**Sanity-check constraints (mandatory):**
1. No lever with estimated impact >$500/unit/yr is ranked #1 unless the skill has validated that the current-state of the property does not already capture it.
2. No lever with Difficulty ≥4 is ranked in the top 3 unless explicitly requested by the operator.
3. Legal/regulatory-risk levers (RUBS in CA rent-control, captive setup) carry a MANDATORY disclosure footnote in the skill output.

### 4.5 Total Other-Income Benchmark (sanity check)
Per NAA/IREM/BOMA I/E IQ 2024 [¹]: **other income = $1,482/unit/yr, +5.4% YoY**. Per NARPM / Multifamily Executive [¹⁷]: typical ancillary = **7–9% of EGI** for stabilized portfolios; best-operated = **10%+**.
- On a Class B property with $20K/unit rent base, 7–9% of EGI = ~$1,400–$1,800/unit/yr, consistent with IREM benchmark.
- **Rule:** If the skill's aggregated lever-library recommendation would push estimated other income above $3,000/unit/yr (Class B), flag as over-stacked — real-world portfolios do not stack all levers cleanly.

---

## 5. Conflicting Source Resolution

**Pet-rent range divergence.** Repo KB gives $25–$75/pet/month. Multifamily Executive [¹⁷] gives $25–$50/pet/month. **Resolution:** Use Repo KB range; Multifamily Executive is a narrower market-average that likely excludes high-amenity Class A urban assets where $60–$75 is achievable. Flag as class-dependent.

**Storage-unit range divergence.** Repo KB gives $50–$150/unit/mo (per-storage-unit rented). Multifamily Executive [¹⁷] indicates $25–$75/unit/mo. **Resolution:** Use blended $25–$150/unit/mo range, dependent on storage-unit size and local self-storage market pricing. The skill should cross-reference local Extra Space / Public Storage rates as comparable.

**Ancillary-as-share-of-EGI divergence.** Multifamily Executive [¹⁷] cites "10%+ at best communities" and "7–9% typical" per NARPM. Repo KB aligns at 10–15% best, 5–10% average. **Resolution:** Use Repo KB range as primary; external sources corroborate.

**RUBS legality-by-state.** Tier-3 practitioner sources [²⁰][²¹] are not legal advice. NCLC [¹³] provides the strongest tenant-advocacy perspective; legality practitioner sources provide operator-side. **Resolution:** Pack requires jurisdiction-specific legal opinion before any recommendation to implement RUBS; the summary table in §3B is directional, not authoritative.

**Property-tax appeal success rate 40–60% vs higher in Texas.** AppealDesk [¹⁵] gives 40–60% national; individual jurisdiction outcomes range 62% (Cook IL) to 98.68% (Hays TX). **Resolution:** Use 40–60% as the US national baseline; skill must require jurisdiction-specific success-rate input for any specific appeal recommendation. Professional-representation uplift to 65–85% applies only when operator actually engages a tax-appeal firm.

**Energy-efficiency savings ranges.** ENERGY STAR [¹⁸] is conservative (8% HVAC, ~$50/unit/yr). DOE BMS commentary [¹⁹] at 10–20% building-level. Enterprise MF deployments claim $17K/community on vacant-unit automation. **Resolution:** Use ENERGY STAR as the central default (8% and $50/unit/yr per smart thermostat); treat the higher end as an upper-bound achievable only with strong vacant-unit-automation deployment. Pack rule: do not underwrite above 12% HVAC savings on a default deployment.

**Parametric as replacement vs complement.** Practitioner sources (Aon [via Captive International], Captives.Insure [⁹]) present parametric as transformative; Triple-I [¹⁰] and Hurricane Beryl cat-bond-failure example establish that parametric is a complement, not a replacement. **Resolution:** Pack rule — parametric always layered over (not under) traditional indemnity CAT coverage.

---

## 6. Edge Cases and Red Flags

**Fee-transparency / "junk fee" regulatory exposure.** Post-2024, CA, CO, MN, and several other states have enacted junk-fee / fee-transparency legislation. NMHC RETTC fee-transparency guidance [²] and MITS 5.0 standard represent the industry's response. The Greystar class-action [²³] (Colorado, Jan 2024) is the baseline cautionary precedent. **Pack rule:** Any ancillary lever that produces a "mandatory" fee (valet trash, tech package, admin fee) must be disclosed in the advertised rent figure per state advertising-rent rules. Do not recommend a mandatory-fee structure without a compliance review.

**RUBS in rent-controlled jurisdictions.** Mountain View CSFRA ruling [²¹] treats RUBS fees as rent — meaning a RUBS rollout in that jurisdiction is effectively a rent increase subject to annual rent-control cap. Similar logic will likely apply in SF RSO, Oakland, Berkeley, Santa Monica, LA RSO, and other California rent-stabilized markets. **Pack rule:** Do not recommend RUBS in a rent-stabilized jurisdiction without legal confirmation that the local ordinance permits utility-cost pass-through outside the rent cap.

**Tax-appeal downside: reassessment-up risk.** In most jurisdictions, the assessor cannot raise the assessed value during an appeal process above the proposed assessment. However, in Texas (per annual reassessment), a poorly supported appeal can result in the next year's notice coming in higher based on sales data the owner's appeal attached. **Pack rule:** Always use a professional tax-appeal firm on contingency (no-downside) rather than pro-se owner appeal on commercial / multifamily.

**Captive insurance domicile risk.** Vermont is the dominant US captive domicile, with pro-parametric regulatory stance (2022 law updated 2024 per [⁹] context). Offshore domiciles (Bermuda, Cayman) carry federal-tax complexity under IRS rules on controlled foreign corporations. **Pack rule:** Captives route to specialized insurance-and-tax counsel; the skill should only flag the opportunity, not prescribe the structure.

**Over-stacking ancillary fees.** At a Class B property, stacking pet rent + parking + storage + valet trash + tech package + RUBS + admin fee can exceed $4,000/unit/yr in ancillary — which exceeds realistic market penetration. **Pack rule:** Cap aggregate other-income recommendation at 15% of EGI for Class B and 20% for Class A; flag anything higher for manual review.

**Loss-to-lease / renewal-push retention interaction.** Aggressive LTL recapture drives move-outs, which route through turnover cost + vacancy drag, often erasing the renewal-bump NOI gain. **Pack rule:** LTL recapture >5% in a single renewal cycle requires R4 (retention-driven) validation before implementation.

**AI leasing disclosure risk.** Emerging state laws (Colorado AI Act, California AB 2013) require disclosure that a consumer is interacting with AI. Pack rule: AI-leasing rollouts must include compliant disclosure language at first-touch.

**Insurance hard-market timing.** A disciplined RFP in a hard market (as post-Ian 2022–2024 coastal habitational) may yield flat or worse terms. Pack rule: do not underwrite 5–15% insurance savings in a hard market; assume 0–5% and flag upside separately.

---

## 7. Open Questions

- **Should the skill include solar PV (rooftop or common-area) as a lever?** It routes partially to energy-efficiency OpEx reduction (covered here) and partially to value-add renovation capex (R6). Current pack decision: exclude PV unless PPA-structured with no capex.
- **Should bulk-internet / cable re-sell be its own lever or folded into tech-package fee?** Repo KB lists it separately at $10–$30/unit/mo. Pack current decision: fold into tech-package in the lever library for simplicity; flag as a parameter for operators whose bulk-internet economics meaningfully deviate.
- **Is RATIO billing a separate lever from RUBS?** Research question from task description. Functionally, "RATIO billing" is the broader label for ratio-allocation utility billing, of which RUBS is the standard implementation. No material downstream-skill distinction. Pack decision: treat as synonymous.
- **Should the skill produce a separate "Quick Wins" (<6 month) list vs a "Strategic" (>12 month) list?** Pack current decision: yes, and the §4.3 Time-to-Realize categorization supports this split automatically. Downstream skill spec should require this as two separate output sections.
- **How should the skill handle property-tax-appeal recommendations in Prop-13 California?** Under Prop 13, appeals are rarely fruitful outside the transfer year (reassessment year). Pack rule: skip the lever for long-held CA assets unless specific triggering facts exist (economic-obsolescence claim, base-year error).
- **Where does the line fall between an AI-leasing deployment that counts as "technology-enabled revenue" here vs. a full digital-leasing system that routes to R6 (value-add)?** Pack current decision: anything subscription-SaaS with <12-month payback belongs here; anything requiring hardware replacement (new smart-intercoms, building-wide automation) routes to R6.
- **Should the skill explicitly model concession-burn dynamics for 2026 renewals per RealPage [⁷]?** Pack current decision: yes, as a Year-1 risk factor; the skill should flag properties with concession-rich original leases coming up for renewal in the next 12 months as at-risk for move-out-driven vacancy even under a recapture push.

---

## 8. Research Quality Summary and Gaps

**Citation tally.** 24 external sources (gate: ≥10 ✓). Tier 1 = 7 (NAA/IREM/BOMA, NMHC, JBREC, Fannie Mae MF Guide, Lincoln Institute, ENERGY STAR, DOE via ENERGY STAR Playbook); Tier 2 = 9 (Multifamily Dive, RealPage Analytics, WTW, Captives.Insure, Triple-I, RealPage OpsTechnology, EliseAI, NCLC, NTUF). Tier 1+2 total = **16**, gate ≥6 ✓. Tier 3 = 8 (practitioner commentary and SaaS-vendor citations, all clearly labeled).

**Coverage — what is solid:**
- Ancillary income per-unit benchmarks (pet, parking, storage, valet, RUBS admin, application/admin/late fees).
- RUBS mechanics and directional state-legality overlay for CA / TX / IL / FL.
- Property-tax appeal national success rate (40–60% per IAAO/Lincoln) and jurisdiction variance range.
- Insurance-market structure (RFP norms, captive economics, parametric post-Ian context).
- OpEx-reduction precedents (centralized procurement 5–10% save, maintenance pod 10-mile radius, energy retrofit 8–20% range).
- Technology-enabled revenue (AI leasing conversion-lift evidence, self-guided tour adoption).
- Prioritization framework (impact ÷ difficulty × inverse-time).

**Gaps and caveats — explicit:**
- **Tier 1 John Burns ancillary-specific report** not located at a public URL. JBREC's ancillary-income research is proprietary; the skill cites the public JBREC "Apartment Strategies 2026" commentary [³] instead, which names the lever categories but not per-unit dollar figures. Tier 1 quantitative ancillary benchmarks therefore rest primarily on NAA/IREM/BOMA I/E IQ [¹] and NMHC data [²], which is adequate.
- **REIT supplemental "other income" line-item detail** was not successfully extracted at the per-REIT-disclosure granularity requested (AvalonBay, Camden, MAA). Publicly available supplemental disclosures aggregate other income at a portfolio level without the pet-vs-parking-vs-RUBS breakdown. Downstream skill should cite the IREM benchmark and note that REIT public filings do not provide the per-category breakdown.
- **State-level RUBS legality** is directional. The four-state summary covers the largest multifamily markets but is not a substitute for jurisdiction-specific legal opinion. Pack rule makes this explicit.
- **Property-tax appeal success rates by state/county** are cited at the national aggregate (40–60% per IAAO/Lincoln) and with two endpoint examples (Hays TX 98.68%, Cook IL 62%). A complete 50-state matrix is beyond this research scope and depends on annual-jurisdiction data from AppealDesk / O'Connor / practitioner firms. Downstream skill should integrate operator-supplied local-firm success-rate data for any specific recommendation.
- **Energy-efficiency ROI** varies dramatically by climate zone and building vintage; pack default ranges are conservative central estimates, not project-specific underwriting.
- **AI-leasing conversion-lift figures** ([²⁴] 44.8% lead-to-lease, 30% lead-to-tour) are vendor-reported and lack independent third-party validation. Downstream skill should treat as upper-bound and cite source-is-vendor.
- **Captive and parametric insurance** mechanics are covered at a strategic level; actuarial and tax-domicile detail routes to specialized counsel.

**Reconciliation with repo KBs.** This research is additive to `knowledge/multifamily-benchmarks.md` (Ancillary Income Benchmarks table, Insurance Deep Dive, Property Taxes by State). No conflicts with the repo KB have been identified; where ranges diverge (pet rent, storage, ancillary share of EGI), the repo KB range is primary and this research documents the external corroboration and any conservative-narrowing applied.

**Skill-design handoff notes.**
1. The skill should NOT compute NOI levers as a blind additive stack. It should require the operator to flag existing state for each lever (e.g., "RUBS already implemented Yes/No") to avoid double-counting.
2. The skill MUST include the §4.4 sanity-check constraints (no lever >$500 at top unless validated; Difficulty ≥4 excluded from top 3 without explicit operator request; regulatory-risk levers carry mandatory disclosure footnote).
3. The skill MUST route retention-sensitive levers (LTL recapture >5%, aggressive RUBS in soft-market submarket) to R4 for validation before recommending implementation.
4. The skill MUST output both a "Quick Wins" (<6 month to realize) list and a "Strategic" (>12 month to realize) list per §4.3.
5. The skill output MUST cite `_taxonomy-seed.md` for all KPI / definition references, `knowledge/multifamily-benchmarks.md` for all per-unit benchmarks, and this research file for lever-library content.

---

*Last updated: 2026-04-24. Research file for Phase 0b of cre-agent-skills Asset Management pack v1.3.0.*
