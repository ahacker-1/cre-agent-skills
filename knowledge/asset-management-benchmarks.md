# Asset Management Benchmarks (Operational / Post-Acquisition)

> **What this is:** A shared-reference knowledge base of operational and asset-management-specific benchmarks used in post-acquisition multifamily asset management — variance materiality thresholds, A/R aging reserves, stabilization definitions, turnover-cost decomposition, unit-turn capex scopes, concession-depth norms, bad-debt ranges, absorption pace, ancillary-income lever lifts, and rent-premium realization ranges.
> **How to use it:** Load alongside `knowledge/multifamily-benchmarks.md` (underwriting-era benchmarks) and `knowledge/underwriting-calc.md` (canonical formulas). This KB extends those references with AM-specific cuts; it does not redefine formulas or duplicate benchmark ranges already codified in `multifamily-benchmarks.md`.

**This KB extends `knowledge/multifamily-benchmarks.md` with operational / AM-specific benchmarks. Consumed by skills:**
1. Annual Operating Budget Builder
2. Monthly Variance Analyst
3. Rent Collection & Delinquency Manager
4. Lease-Up & Concessions Analyst
5. CapEx / Value-Add Execution Tracker
6. NOI Improvement Analyst

**Authority and cross-reference rules:**
- **Formulas:** cross-reference `knowledge/underwriting-calc.md` and `research/asset-management/_taxonomy-seed.md` §2. Never redefine here.
- **OpEx per-unit ranges, regional/class/vintage/catastrophe multipliers:** defer to `multifamily-benchmarks.md`. Ranges in this KB are AM-specific additions (e.g., bad-debt sub-bands, turnover decomposition) not a replacement.
- **Vocabulary, KPI definitions, aging bands, variance buckets:** inherit verbatim from `_taxonomy-seed.md`.
- **Every benchmark cell cites a research note** in `research/asset-management/{file}-research.md`.

---

## 1. Variance Materiality Thresholds

The institutional dual-threshold convention: investigate and classify any variance that exceeds **EITHER** a percentage floor **OR** an absolute-dollar floor. The lower of the two triggers is the governing materiality test for that line item. Applies to monthly and YTD budget-vs-actual variance analysis.

**Formula cross-reference:** Timing / Permanent / One-Time classification rules are defined in `_taxonomy-seed.md` §3 and are NOT redefined here. This section provides the numeric thresholds that gate classification.

### Pack-Default Dual Threshold (Single-Asset, Stabilized)

| Threshold Component | Default | Conservative Floor | Source |
|---|---|---|---|
| Percentage of budgeted line | 10% | 5% (large lines: property taxes, payroll, insurance) | per research/asset-management/monthly-variance-analyst-research.md |
| Absolute dollar floor | $25,000 | $5,000 (50-unit / lean chart-of-accounts) | per research/asset-management/monthly-variance-analyst-research.md |
| Enterprise/large-portfolio uplift | $50,000 | Applies to portfolios >1,000 units or >$25M OpEx | per research/asset-management/monthly-variance-analyst-research.md |

### Thresholds by Property Size

| Property Size | % Floor | $ Floor | Notes |
|---|---|---|---|
| 25 – 75 units | 10% | $5,000 | Smaller denominator, tighter floor prevents noise-suppression of real issues. per research/asset-management/monthly-variance-analyst-research.md |
| 75 – 200 units | 10% | $10,000 – $15,000 | Transitional band; use $15K on stabilized assets with $2M+ OpEx. per research/asset-management/monthly-variance-analyst-research.md |
| 200 – 500 units | 10% | $25,000 (pack default) | Institutional stabilized band. per research/asset-management/monthly-variance-analyst-research.md |
| 500+ units or multi-property | 10% | $50,000 | Portfolio-level materiality; property-level threshold still applies per asset. per research/asset-management/monthly-variance-analyst-research.md |

### Line-Item Specific Considerations

| Line Item | Recommended Floor Adjustment | Reason |
|---|---|---|
| Property Taxes | 5% OR $25K | Large dollar line; 10% on a $600K line = $60K, which is large enough to matter but 5% = $30K captures earlier signal. per research/asset-management/monthly-variance-analyst-research.md |
| Insurance | 5% OR $25K | Same rationale — renewal step-changes hit hard. per research/asset-management/monthly-variance-analyst-research.md |
| Payroll | 5% OR $15K | Wage grids and staffing changes create structural shifts. per research/asset-management/monthly-variance-analyst-research.md |
| Marketing | 10% OR $5K | Often budgeted low; $25K floor would suppress real issues. per research/asset-management/monthly-variance-analyst-research.md |
| Professional Fees / Communications | 10% OR $5K | Small denominators; keep floor proportional. per research/asset-management/monthly-variance-analyst-research.md |
| R&M / Turnover | 10% OR $15K | Mid-range line; dual-threshold default works. per research/asset-management/monthly-variance-analyst-research.md |

### Reforecast Trigger Table

| Variance Bucket | Triggers Reforecast? | Cadence |
|---|---|---|
| Timing | No | Quarterly refresh; Timing converges by year-end |
| Permanent (above materiality) | Yes | Ad-hoc reforecast within 30 days of identification |
| One-Time | Generally no | But flag knock-on Permanent effects (e.g., post-storm premium step-up at next renewal) |
| Mixed Timing + Permanent | Yes, for Permanent component only | Split and report; reforecast the Permanent residual |

per research/asset-management/monthly-variance-analyst-research.md

**Sign convention.** Favorable variance = higher revenue or lower expense than budget (positive NOI impact). `Variance $ = Actual − Budget` is the institutional default; state convention explicitly at the top of every variance package.

---

## 2. A/R Aging Reserve Percentages by Band

The canonical 5-band aging schema used across Yardi, RealPage/OneSite, AppFolio, and Entrata, with reserve percentages aligned to Commercial Collection Agency Association (CCAA) collection-probability data.

**Cross-reference:** Aging band definitions, decision actions, split-aging rule, and bad-debt classification point are defined in `_taxonomy-seed.md` §5 and are NOT redefined here. This section provides the reserve % pack defaults and class-adjusted sub-bands.

### Pack-Default Reserve % by Aging Band

| Band | Days Past Due | Reserve % of Balance (Default) | Reserve % (Conservative) | Collection Probability |
|---|---|---|---|---|
| Current | 0 | 1% | 1% | ~99% |
| 1 – 30 | 1 – 30 | 5 – 10% | 10% | ~90% |
| 31 – 60 | 31 – 60 | 10 – 15% | 15% | ~85% |
| 61 – 90 | 61 – 90 | 15 – 20% | 20% | ~73% (CCAA) |
| 90+ | > 90 | 40 – 50% | 50% | < 50% (CCAA, drops below 50% after 6 months) |

per research/asset-management/rent-collection-delinquency-manager-research.md

### Reserve % Adjustments by Class

AM-specific overlay on the pack defaults. Apply on top of the band % for class-calibrated reserving.

| Property Class | Adjustment to Band Reserve % | Rationale |
|---|---|---|
| Class A (institutional coastal) | -25% relative (e.g., 61-90 band → 11 – 15%) | Lower skip rates (0.5 – 1.0% of move-outs), stronger tenant screening. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Class B | Pack default (no adjustment) | Baseline. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Class C | +25% relative (e.g., 61-90 band → 19 – 25%) | Higher skip rates (3 – 6%), income-volatility of resident base. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Affordable / Workforce (unsubsidized) | +50% relative (e.g., 61-90 band → 23 – 30%) | Income-volatility; 2.0 – 3.5% bad-debt ratio range. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Deep-Value-Add / Distressed repositioning | +100% relative (aggressive) | Skip rates 5 – 10%+; use conservative ceiling. per research/asset-management/rent-collection-delinquency-manager-research.md |

### 4-Band Operator Variance Rule

Some institutional operators (certain REITs) collapse 61-90 and 90+ into a single "60+" bucket in portfolio reporting. **Mechanical rule:** when source data provides only a combined 60+ band, apply the **90+ reserve rate (40 – 50%)** to the entire 60+ balance for conservatism.

per research/asset-management/rent-collection-delinquency-manager-research.md

### Warning Threshold

If **> 20 – 25% of total receivables are past due** (any bucket beyond Current), flag as a collections problem to ownership.

per research/asset-management/rent-collection-delinquency-manager-research.md

---

## 3. Stabilization Targets — Economic and Physical Occupancy

Stabilization is **not** a single number — it is a tiered definition depending on audience (agency lender vs LP vs internal ownership). This table resolves the conflict by publishing each tier explicitly so downstream skills can report against the correct one.

**Cross-reference:** Economic Occupancy formula is `Actual Collected Revenue / Gross Potential Revenue × 100` per `multifamily-benchmarks.md` §Economic Occupancy vs Physical Occupancy. NOT redefined here.

### Stabilization Definitions by Audience

| Audience | Physical Occupancy | Sustained Duration | Economic Occupancy | Notes |
|---|---|---|---|---|
| **Agency (Fannie Mae / Freddie Mac) — minimum floor** | 90% | 90 consecutive days | Not required (physical-only) | Regulatory anchor; gates conversion of lease-up loans to permanent agency debt. per research/asset-management/lease-up-concessions-analyst-research.md |
| **Owner-operator (working stabilization)** | 93 – 95% | 90 consecutive days | 91 – 93% | Internal stabilized-return threshold. per research/asset-management/lease-up-concessions-analyst-research.md |
| **Institutional LP-reporting (conservative)** | 95% | 180 consecutive days | 92%+ simultaneous | LP-grade; eliminates amortized-concession overhang noise. per research/asset-management/lease-up-concessions-analyst-research.md |
| **Debt-fund bridge (alternative covenant)** | 90% OR trailing-3 DSCR ≥ 1.20x | 90 days | Not required | Some bridge programs use DSCR as stabilization proxy. per research/asset-management/lease-up-concessions-analyst-research.md |

### Physical-vs-Economic Gap Guidance (AM-Specific)

Extends the `multifamily-benchmarks.md` §Economic Occupancy vs Physical Occupancy table with AM-specific diagnostic cuts for **post-stabilization** monitoring.

| Gap (Physical − Economic) | Interpretation | AM Action |
|---|---|---|
| 0 – 2 percentage points | Normal; modest concession + bad debt drag | No action. per research/asset-management/lease-up-concessions-analyst-research.md |
| 2 – 4 pp | Moderate drag; worth investigating | Audit concession schedule and 31-60 aging. per research/asset-management/rent-collection-delinquency-manager-research.md |
| 4 – 6 pp | Elevated; concession burn-off incomplete OR collections softening | Split diagnosis: concession amortization vs bad debt. per research/asset-management/rent-collection-delinquency-manager-research.md |
| 6+ pp | Red flag; investigate immediately | Collections problem or heavy concessions masking weakness. per research/asset-management/rent-collection-delinquency-manager-research.md |

### Concession-Overhang Rule (Post-Stabilization)

Even after reaching "stabilized occupancy," amortized concessions from lease-up leases continue to drag effective rent for **12 – 15 additional months**. Properties typically reach "stabilized effective rent" ~12 months after reaching "stabilized occupancy." REIT disclosure convention (Camden, MAA) discloses both dates separately; LP reporting should do the same.

per research/asset-management/lease-up-concessions-analyst-research.md

---

## 4. Turnover Cost Benchmarks (AM Decomposition)

Extends the `multifamily-benchmarks.md` turnover-cost row ($1,500 – $3,000/turn direct) with the AM wide-definition that includes all economic costs per move-out (not just make-ready). Required for accurate operating-budget construction.

### Direct vs Wide-Definition Turnover Cost

| Definition | Cost per Turn | Components | Use Case |
|---|---|---|---|
| **Direct (make-ready only)** | $1,500 – $3,000 | Paint, cleaning, carpet/flooring repair, appliance proration, minor repairs | Already in `multifamily-benchmarks.md`. Use for make-ready budget line only. per research/asset-management/annual-operating-budget-builder-research.md |
| **Wide (AM economic cost)** | $2,500 – $5,000 (2024 Zego avg: $3,872) | All direct costs + vacancy rent loss + marketing + leasing commission + concessions | Use for full-economic turnover impact in budget construction. per research/asset-management/annual-operating-budget-builder-research.md |

### Turnover Cost by Class (Wide Definition)

| Class | Blended Cost/Turn (2024-2026) | Notes |
|---|---|---|
| Class A | $4,000 – $5,500 | Higher finish replacement cost + higher rent = larger vacancy drag. per research/asset-management/annual-operating-budget-builder-research.md |
| Class B | $3,000 – $4,500 | Baseline. Zego 2024 national average $3,872 sits in this band. per research/asset-management/annual-operating-budget-builder-research.md |
| Class C | $2,200 – $3,500 | Simpler finish packages; lower rent drag but higher turnover frequency. per research/asset-management/annual-operating-budget-builder-research.md |

### Turnover Rate Benchmarks (2024 National)

| Tier | Annual Turnover Rate | Portfolio Economic Impact on 200-unit |
|---|---|---|
| Best-in-class | < 40% | ~80 turns × $3,872 = ~$310K/yr |
| National average | 45 – 55% (2024 avg: ~47.5%) | ~95 turns × $3,872 = ~$368K/yr |
| Weak | > 55% | ~120 turns × $3,872 = ~$465K/yr |

per research/asset-management/annual-operating-budget-builder-research.md

### Budget Allocation Rule (AM)

Per-turn cost spills across multiple GL lines. For budget construction, allocate the wide-definition cost as follows:

| Component | % of Wide Cost | GL Line |
|---|---|---|
| Paint, cleaning, flooring (make-ready) | ~40 – 50% | R&M or Turnover (per IREM chart) |
| Vacancy rent loss | ~25 – 30% | Contra-revenue (reduces EGI, not an OpEx line) |
| Marketing + leasing commission | ~15 – 20% | Marketing / Leasing Expenses |
| Concessions on new lease | ~5 – 10% | Contra-revenue |

per research/asset-management/annual-operating-budget-builder-research.md

---

## 5. Unit-Turn CapEx Ranges by Scope (Light / Medium / Heavy)

Three-tier interior renovation taxonomy converged across public REIT disclosures (MAA, Camden, UDR, AvalonBay), John Burns renter WTP research, and RSMeans/Gordian unit pricing. Costs in **2024-2026 dollars**, hard+soft including CM fee, excluding GC markup to sponsor G&A.

### Scope Tier Definitions

| Tier | Cost/Unit | Scope Description | Target Class | Typical Rent Premium Ceiling |
|---|---|---|---|---|
| **Light ("lipstick")** | $3,000 – $6,000 | Paint, accent wall, light fixtures, cabinet paint/resurface, hardware, faucets, mini-blinds, appliance color swap, flooring patch. | Class B- / C+ in Tier 3-4 markets | $50 – $100/mo |
| **Medium ("classic")** | $6,000 – $12,000 | Everything Light + full cabinet replacement or refacing, quartz/HG laminate counters, LVP flooring throughout, stainless appliance package, new lighting, bathroom vanity, tub reglaze. | Class B / B+ garden in Tier 2-3 markets | $75 – $175/mo |
| **Heavy ("full interior")** | $12,000 – $25,000 | Everything Medium + kitchen reconfiguration, new cabinet boxes, mitered quartz, shower conversion, tile bath, pull-down fixtures, smart-home package, W/D installation, new interior doors/trim. | Class C to B- repositioning; Class A re-amenitization | $150 – $350+/mo |

per research/asset-management/capex-value-add-execution-tracker-research.md

### Cost Split by Unit Type (Medium Scope Base Case)

| Unit Type | Cost Range (Medium) | Primary Cost Drivers |
|---|---|---|
| Studio / Efficiency | $5,500 – $8,000 | Smaller kitchen, single bath, limited flooring |
| 1BR / 1BA | $6,500 – $10,500 | Base case; drives per-unit benchmark |
| 2BR / 1BA | $7,500 – $11,500 | More flooring, same kitchen footprint |
| 2BR / 2BA | $8,500 – $13,000 | Second bath adds $1,000 – $2,500 |
| 3BR / 2BA | $9,500 – $14,500 | More flooring + sometimes larger kitchen |

per research/asset-management/capex-value-add-execution-tracker-research.md

### Cost Multipliers by COL Tier

Apply on top of the scope-tier base ranges. Cross-references `multifamily-benchmarks.md` §Cost of Living Multipliers (Labor/Payroll and Maintenance rows proxy most value-add cost-of-labor sensitivity).

| COL Tier | Multiplier | Example (Medium Scope $9K base) |
|---|---|---|
| Tier 1 (NYC, SF, LA, Boston, DC, Seattle) | 1.35x – 1.60x | $12,150 – $14,400 |
| Tier 2 (Portland, Denver, Austin, Nashville, Miami, Raleigh) | 1.10x – 1.25x | $9,900 – $11,250 |
| Tier 3 (Atlanta, Dallas, Phoenix, Charlotte, Tampa) | 0.95x – 1.05x | $8,550 – $9,450 (baseline) |
| Tier 4 (Memphis, OKC, Toledo, Indianapolis, Birmingham) | 0.80x – 0.95x | $7,200 – $8,550 |

per research/asset-management/capex-value-add-execution-tracker-research.md (cross-refs `multifamily-benchmarks.md` §Cost of Living Multipliers)

### Yield on Cost Benchmarks (Stabilized)

`Yield on Cost = (Monthly Rent Premium × 12) / Renovation Cost per Unit`

| Yield on Cost | Rating | Action |
|---|---|---|
| 18 – 22% | Institutional-grade execution | Scale program; defend pricing |
| 12 – 15% | Minimum acceptable | Review scope fit; audit premium capture |
| < 10% | Failing | Halt program; re-underwrite scope or exit |

per research/asset-management/capex-value-add-execution-tracker-research.md

### Cost Overrun Benchmarks by Era

| Era | Typical Overrun vs Original Budget | Context |
|---|---|---|
| Pre-2021 (stable materials) | 5 – 10% | Disciplined GP baseline |
| 2021 – 2023 (inflation surge) | 15 – 30% | BLS PPI materials +35% peak-to-trough |
| 2024 – 2026 (plateau) | 7 – 15% | Labor availability + discovered conditions dominate |

per research/asset-management/capex-value-add-execution-tracker-research.md

---

## 6. Concession Norms by Market Condition

Pack-default concession depth by supply-demand balance. Reported as **months free on a 12-month lease** and the equivalent **% face-rent discount**.

### Concession Depth by Market Condition

| Market Condition | Months Free (12mo Lease) | % Face-Rent Discount | Additional Incentives Layered |
|---|---|---|---|
| Balanced / undersupplied | 0 – 0.5 | 0 – 4% | None typical | per research/asset-management/lease-up-concessions-analyst-research.md |
| Mildly competitive | 1 | ~8% (8.3% concession rate) | Minor (look-and-lease bonus) | per research/asset-management/lease-up-concessions-analyst-research.md |
| Oversupplied | 2 – 3 | 17 – 25% | Waived fees, gift cards common | per research/asset-management/lease-up-concessions-analyst-research.md |
| Severely oversupplied (2023-2026 Sun Belt) | 2 – 3+ | 25 – 30% | Waived pet + admin + app fees, free parking, look-and-lease bonuses | per research/asset-management/lease-up-concessions-analyst-research.md |

### Current-Cycle Market Classification (2024-2026)

| Market | Concession Depth (Lease-Up) | Condition |
|---|---|---|
| Austin, Nashville, Phoenix | 2 – 3 months free | Severely oversupplied (concession compression in Austin starting Q4 2025) | per research/asset-management/lease-up-concessions-analyst-research.md |
| Dallas, Atlanta, Charlotte, Raleigh, Salt Lake City | 1.5 – 2.5 months free | Oversupplied | per research/asset-management/lease-up-concessions-analyst-research.md |
| Miami, South Florida | 1 – 1.5 months free | Mildly competitive | per research/asset-management/lease-up-concessions-analyst-research.md |
| NYC, Boston, DC, Gateway | 0 – 1 month free | Balanced | per research/asset-management/lease-up-concessions-analyst-research.md |
| San Francisco | 0.5 – 1 month free | Balanced (recovered from 2021-2022 peak) | per research/asset-management/lease-up-concessions-analyst-research.md |

### Burn-Off Trigger Points (Two-Phase Model)

| Occupancy Threshold | Burn-Off Action |
|---|---|
| Past 70% physical | Reduce look-and-lease bonuses and ancillary incentives | per research/asset-management/lease-up-concessions-analyst-research.md |
| Past 80 – 85% physical | Reduce free-rent months from 2 to 1 on new leases | per research/asset-management/lease-up-concessions-analyst-research.md |
| Past 90% (stabilized) | Drop concessions to 0 – 0.5 months; push face-rent increases | per research/asset-management/lease-up-concessions-analyst-research.md |

---

## 7. Bad Debt % Benchmarks by Class

Extends the `multifamily-benchmarks.md` KPI table (Bad Debt Ratio: <1% strong / 1-3% average / >3% weak) with class-specific sub-bands and regional overlays.

**Formula cross-reference:** `Bad Debt = GPI × Bad Debt Rate`; `Bad Debt Ratio = Uncollected Rent / Gross Potential Rent` per `_taxonomy-seed.md` §2 and `underwriting-calc.md`. NOT redefined here.

### Bad-Debt Ratio by Class (Post-Moratorium, 2023+ Baseline)

| Class | Strong | Typical Range | Watch | Source |
|---|---|---|---|---|
| Class A (institutional coastal) | < 0.5% | 0.5 – 1.0% | > 1.0% | per research/asset-management/rent-collection-delinquency-manager-research.md (EQR, AVB 10-K 2023) |
| Class A (Sun Belt REIT-grade) | < 0.75% | 0.5 – 1.2% | > 1.2% | per research/asset-management/rent-collection-delinquency-manager-research.md (MAA, CPT 10-K 2023) |
| Class B | < 1.0% | 1.0 – 1.5% | > 1.5% | per research/asset-management/rent-collection-delinquency-manager-research.md (NAA 2024 I/E) |
| Class C | < 1.5% | 1.5 – 2.5% | > 2.5% | per research/asset-management/rent-collection-delinquency-manager-research.md (NAA 2024 I/E) |
| Affordable / Workforce (unsubsidized) | < 2.0% | 2.0 – 3.0% | > 3.0% (approaching 3.5%) | per research/asset-management/rent-collection-delinquency-manager-research.md |

### Regional Overlay (AM-Specific)

Apply as a spread on top of the class baseline above.

| Region | Spread | Rationale |
|---|---|---|
| Sun Belt moderate-income markets | +0.25 – +0.75% | Higher income-volatility cohort. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Coastal gateway (NYC, SF, LA, DC, Boston) | -0.25% | Higher-income resident base, stronger screening. per research/asset-management/rent-collection-delinquency-manager-research.md |
| Midwest stable metros | 0% (baseline) | per research/asset-management/rent-collection-delinquency-manager-research.md |

### Moratorium-Era Caveat

**Do NOT use 2021-2022 bad-debt ratios as steady-state benchmarks.** Residual CDC moratorium receivables were written off in 2021-2022 at abnormally high rates (2-4%+ in some coastal portfolios). Use **2023+ T-12** for cleanest apples-to-apples comparison. ERAP residuals in NY, NJ, DC, IL continued to distort bad-debt metrics into 2024 — confirm no pending ERAP application before writing off 90+ balances.

per research/asset-management/rent-collection-delinquency-manager-research.md

### Surety-Product Adjustment

Properties using deposit-alternative surety products (LeaseLock, Rhino, Jetty) at 15 – 40%+ adoption will read **lower** bad-debt ratios than otherwise-comparable properties because the surety absorbs a slice of bad debt within coverage limits (typically 1-2x monthly rent). When benchmarking across operator portfolios, disclose surety-product usage.

per research/asset-management/rent-collection-delinquency-manager-research.md

---

## 8. Absorption Benchmarks (Units/Month) by Market Tier

Property-level absorption benchmarks for new-construction lease-up, cross-referenced across Yardi Matrix, ALN Apartment Data, John Burns, and REIT supplementals.

### Absorption Pace by Market Tier and Cycle Stage

| Market Tier | Pre-2023 Norm | Current (2024-2026 Oversupply) | Notes |
|---|---|---|---|
| Tier 1 Primary MSAs (balanced) | 15 – 25 units/mo | 15 – 25 units/mo | Gateway markets largely unaffected by Sun Belt oversupply cycle. per research/asset-management/lease-up-concessions-analyst-research.md |
| Tier 2 High-Growth Sun Belt | 18 – 30 units/mo | **10 – 18 units/mo** | Austin, Nashville, Phoenix, Raleigh all in this band. per research/asset-management/lease-up-concessions-analyst-research.md |
| Tier 3 Secondary | 12 – 20 units/mo | 8 – 15 units/mo | per research/asset-management/lease-up-concessions-analyst-research.md |
| Tier 4 Tertiary | 8 – 15 units/mo | 8 – 15 units/mo | Less exposed to delivery cycle. per research/asset-management/lease-up-concessions-analyst-research.md |
| Urban infill high-density (200+ units, high-rise) | 12 – 20 units/mo | 12 – 20 units/mo (with concession support) | Wider variance; meaningful concession support typical. per research/asset-management/lease-up-concessions-analyst-research.md |

### Absorption by Lease-Up Type

| Lease-Up Type | Absorption vs Ground-Up Baseline | Typical Stabilization Window |
|---|---|---|
| Ground-up new construction | Baseline | 12 – 18 months (Tier 1-2); 15 – 24 months (oversupplied Sun Belt) | per research/asset-management/lease-up-concessions-analyst-research.md |
| Value-add renovation re-lease-up | 15 – 30% faster than ground-up | 6 – 12 months | per research/asset-management/lease-up-concessions-analyst-research.md |
| Stabilized re-tenanting (post-acquisition mass-expiration) | Fastest | 90 – 180 days | per research/asset-management/lease-up-concessions-analyst-research.md |

### Velocity Deceleration Rule (Last-10% Problem)

Velocity typically **slows by 25 – 50%** once lease-up crosses the 70 – 80% physical occupancy threshold. Drivers: (a) remaining inventory is less-desirable floor plans/levels, (b) "new product" marketing appeal declines, (c) operator intentional slowdown to reduce concession depth. **Rule:** do NOT linearly extrapolate early lease-up velocity to the 80 – 95% stabilization window.

per research/asset-management/lease-up-concessions-analyst-research.md

### Reforecast Trigger (Absorption Shortfall)

| Trigger | Action |
|---|---|
| Trailing-3 absorption ≤ 75% of underwriting for one month | Flag; recalculate stabilization date | per research/asset-management/lease-up-concessions-analyst-research.md |
| Trailing-6 absorption ≤ 80% of underwriting | Formal reforecast (stabilization date, concession burn-off, DSCR) | per research/asset-management/lease-up-concessions-analyst-research.md |
| Missed contractual milestone (e.g., 80% by Month 10 covenant) | Immediate lender communication; CMBS watchlist risk | per research/asset-management/lease-up-concessions-analyst-research.md |

### Pre-Leasing at First CO

| Market Condition | Pre-Leased at First CO |
|---|---|
| Strong | 25 – 40% | per research/asset-management/lease-up-concessions-analyst-research.md |
| Normal | 10 – 25% | per research/asset-management/lease-up-concessions-analyst-research.md |
| Weak / oversupplied | 5 – 15% | per research/asset-management/lease-up-concessions-analyst-research.md |
| Sun Belt oversupplied (2024-2026) | < 10% | per research/asset-management/lease-up-concessions-analyst-research.md |

**Underwriting haircut:** Count pre-leases at 85% of signed count to reflect normal 10 – 20% cancellation rate.

per research/asset-management/lease-up-concessions-analyst-research.md

---

## 9. Ancillary Income Lever — Typical NOI Lifts

Extends the `multifamily-benchmarks.md` Ancillary Income Benchmarks table with AM-specific Year-1 lift estimates, time-to-realize, and difficulty ratings for each lever. Dollar ranges are **$/unit/year portfolio average** (accounting for typical penetration rates), **not** per-utilizing-unit.

**Cross-reference:** Per-tenant / per-utilizing-unit rates (e.g., pet rent $25 – $75/pet/mo) are in `multifamily-benchmarks.md` §Ancillary Income Benchmarks. This section calculates penetration-adjusted portfolio lifts.

### Ancillary Lever Library (Portfolio $/unit/yr)

| Lever | Year-1 Portfolio Lift ($/unit/yr) | Difficulty (1 easy – 5 hard) | Time-to-Realize |
|---|---|---|---|
| Pet Rent Program (50% penetration @ $40/mo) | $180 – $300 | 2 | 6 – 18 months | per research/asset-management/noi-improvement-analyst-research.md |
| Parking Unbundle (variable penetration) | $150 – $500 | 2 | 12 – 24 months | per research/asset-management/noi-improvement-analyst-research.md |
| Storage Units (20 – 40% penetration) | $120 – $360 | 3 | 3 – 12 months | per research/asset-management/noi-improvement-analyst-research.md |
| Valet Trash (net of vendor cost) | $120 – $360 | 2 | 6 – 12 months | per research/asset-management/noi-improvement-analyst-research.md |
| Package Locker / Delivery Subscription | $60 – $180 | 3 | 3 – 9 months | per research/asset-management/noi-improvement-analyst-research.md |
| Tech Package / Smart-Home Fee | $150 – $300 | 3 | 18 – 36 months | per research/asset-management/noi-improvement-analyst-research.md |
| RUBS Admin Fee (on top of pass-through) | $36 – $96 | 2 | 0 – 3 months | per research/asset-management/noi-improvement-analyst-research.md |
| Application / Admin / Late Fees (amortized) | $180 – $480 | 1 | Immediate | per research/asset-management/noi-improvement-analyst-research.md |
| Short-Term / M-to-M Premium (cohort-specific) | $50 – $200 (on cohort only) | 2 | 6 – 12 months | per research/asset-management/noi-improvement-analyst-research.md |

### Utility Recovery Levers

| Lever | Year-1 Portfolio Lift ($/unit/yr) | Difficulty | Time-to-Realize |
|---|---|---|---|
| RUBS (water only, no hardware) | $360 – $960 ($30 – $80/unit/mo net) | 3 – 4 (5 in rent-control CA) | 3 – 6 months | per research/asset-management/noi-improvement-analyst-research.md |
| Full Submetering (water/sewer/gas/electric retrofit) | $500 – $1,500 | 4 | 12 – 24 months (requires capex $300 – $800/unit) | per research/asset-management/noi-improvement-analyst-research.md |

### OpEx Reduction Levers

| Lever | Year-1 Portfolio Lift ($/unit/yr) | Difficulty | Time-to-Realize |
|---|---|---|---|
| Property Tax Appeal (successful 10% AV reduction @ 2% tax rate on $200K/unit) | ~$200/unit/yr (= $40K on 200-unit at 5.5% cap = ~$730K value lift) | 3 | 6 – 18 months | per research/asset-management/noi-improvement-analyst-research.md |
| Insurance RFP Shopping (5 – 15% of premium in soft market) | $40 – $180 | 1 – 2 | 3 – 6 months | per research/asset-management/noi-improvement-analyst-research.md |
| Centralized Procurement (5 – 10% on controllable) | $175 – $245 | 3 | 12 – 24 months | per research/asset-management/noi-improvement-analyst-research.md |
| Regional Maintenance Pod (~10-mile radius) | $150 – $400 | 4 | 12 – 24 months | per research/asset-management/noi-improvement-analyst-research.md |
| Third-Party Contract Renegotiation (5 – 15% on contract services) | $15 – $90 | 1 | 6 – 18 months | per research/asset-management/noi-improvement-analyst-research.md |
| LED Common-Area Retrofit | $75 – $200 | 2 | 6 – 18 months | per research/asset-management/noi-improvement-analyst-research.md |
| Smart Thermostat Rollout (ENERGY STAR default) | $40 – $60 | 2 | 6 – 12 months | per research/asset-management/noi-improvement-analyst-research.md |
| Smart Controls / BMS (10 – 20% utility save) | $150 – $300 | 3 | 12 – 24 months | per research/asset-management/noi-improvement-analyst-research.md |

### Property-Tax Appeal Success Rates

| Metric | Rate | Source |
|---|---|---|
| National appeal success (any reduction) | 40 – 60% | per research/asset-management/noi-improvement-analyst-research.md (IAAO / Lincoln aggregated) |
| With professional evidence & representation | 65 – 85% | per research/asset-management/noi-improvement-analyst-research.md |
| US properties over-assessed (% of base) | 30 – 60% | per research/asset-management/noi-improvement-analyst-research.md |
| Hays County TX (high-bound example) | 98.68% | per research/asset-management/noi-improvement-analyst-research.md |
| Cook County IL (low-bound example) | 62% | per research/asset-management/noi-improvement-analyst-research.md |

### Aggregate Ancillary Cap Rule

Per NAA/IREM/BOMA I/E IQ 2024: Other income = **$1,482/unit/yr (+5.4% YoY)**. Per NARPM / Multifamily Executive: typical ancillary = **7 – 9% of EGI** for stabilized portfolios; best-operated = **10%+**.

**Aggregate sanity cap (stacking constraint):**
- Class B: flag if aggregated lever recommendation > 15% of EGI or > $3,000/unit/yr
- Class A: flag if aggregated lever recommendation > 20% of EGI

per research/asset-management/noi-improvement-analyst-research.md

---

## 10. Rent-Premium Realization Ranges (% of Underwritten)

The single most-important value-add execution KPI: `Premium Realization % = (Actual Premium Achieved / Underwritten Premium) × 100`. Benchmarks segmented by source quality and market condition.

### Premium Realization by Sponsor Tier

| Sponsor Cohort | Premium Realization % | Notes |
|---|---|---|
| Public REITs (MAA, Camden, UDR) — Medium scope | **85 – 100%** of disclosed target | Audited 10-K disclosures; most reliable benchmark. Yields 17 – 20% on cost. per research/asset-management/capex-value-add-execution-tracker-research.md |
| AvalonBay re-development (Heavy scope) | 85 – 100% | Yields 7 – 10% on cost (heavier scope, higher base rents). per research/asset-management/capex-value-add-execution-tracker-research.md |
| Private top-quartile sponsors | 85 – 100% | Strong market selection + scope discipline. per research/asset-management/capex-value-add-execution-tracker-research.md |
| Private median sponsors (2019 – 2021 vintage) | 75 – 90% | Pre-supply-cycle baseline. per research/asset-management/capex-value-add-execution-tracker-research.md |
| Private median sponsors (2022 – 2024 vintage) | **60 – 80%** | Sun Belt oversupply compression + concession re-emergence. per research/asset-management/capex-value-add-execution-tracker-research.md |
| Private bottom-quartile sponsors | 40 – 60% | Usually poor market selection or scope mis-fit. per research/asset-management/capex-value-add-execution-tracker-research.md |

### Premium Realization by Market Condition (2024-2026)

| Market Condition | Realization % | Example Markets |
|---|---|---|
| Balanced / undersupplied | 80 – 95% | Gateway (NYC, Boston, DC), stable Midwest | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Moderately supplied | 65 – 85% | Atlanta, Dallas, Charlotte (some submarkets) | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Oversupplied Sun Belt | **40 – 65%** | Austin, Phoenix, Nashville, Raleigh, Salt Lake City (2024 delivery) | per research/asset-management/capex-value-add-execution-tracker-research.md |

### Realization Grading Scale (Execution Tracking)

| Realization % | Rating | Action |
|---|---|---|
| 85%+ | Strong | Defend pricing; scale program | per research/asset-management/capex-value-add-execution-tracker-research.md |
| 70 – 85% | Acceptable | Monitor; refine scope fit | per research/asset-management/capex-value-add-execution-tracker-research.md |
| 50 – 70% | Underperforming | Pause scale; diagnose (market, scope, pricing) | per research/asset-management/capex-value-add-execution-tracker-research.md |
| < 50% | Failing | Halt program; re-underwrite or exit | per research/asset-management/capex-value-add-execution-tracker-research.md |

### Steady-State vs First-Cohort Rule

The first 20 – 30 renovated units often capture **higher** premium than steady-state due to "novelty effect" in the submarket. Project steady-state premium from **Months 4 – 8** of leasing, not Months 1 – 2.

per research/asset-management/capex-value-add-execution-tracker-research.md

### Red Flags on Premium Realization

| Flag | Signal |
|---|---|
| Renovated-unit vacancy > 14 days between completion and lease | Mispricing; premium likely overshooting market | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Renovated-unit concessions of 1+ month free | Effective premium below underwritten; report effective, not face | per research/asset-management/capex-value-add-execution-tracker-research.md |
| High variance in cost/unit across first 20 units | GC scope not tight; re-bid before scaling | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Contingency burn > program-complete % at 40%+ complete | Overrun risk 15 – 25%+; re-baseline | per research/asset-management/capex-value-add-execution-tracker-research.md |

---

## Quick Reference — AM-Specific Red Flags

Extends `multifamily-benchmarks.md` §Quick Reference: Red Flags with AM-specific operational flags.

| Red Flag | Indicates | Source |
|---|---|---|
| Line-item variance > 10% AND > $25K for 2+ consecutive months same direction | Permanent variance; reforecast required | per research/asset-management/monthly-variance-analyst-research.md |
| > 25% of receivables past due | Collections problem; escalate to ownership | per research/asset-management/rent-collection-delinquency-manager-research.md |
| Economic occupancy 4+ pp below physical | Concession overhang or collections softening | per research/asset-management/lease-up-concessions-analyst-research.md |
| Trailing-3 absorption ≤ 75% of UW for one month | Stabilization date slippage; flag and recalculate | per research/asset-management/lease-up-concessions-analyst-research.md |
| Renovated-unit vacancy > 14 days | Premium mispriced | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Premium realization < 50% | Value-add program failing | per research/asset-management/capex-value-add-execution-tracker-research.md |
| Aggregate ancillary stack > 15% EGI (Class B) | Over-stacked; real-world penetration unlikely | per research/asset-management/noi-improvement-analyst-research.md |
| Bad-debt > 1.5% Class A / 2.5% Class B / 3% Class C | Watch; review screening, aging, eviction policy | per research/asset-management/rent-collection-delinquency-manager-research.md |
| Blanket CPI escalator applied to all budget lines | Structural budget error — line-items track different indices | per research/asset-management/annual-operating-budget-builder-research.md |
| Insurance increase > 15% YoY without cat event | Claims history, poor loss-control, or market hardening | per research/asset-management/annual-operating-budget-builder-research.md |
| Post-acquisition Year-1 tax line not stress-tested for reassessment | "Tax cliff" risk unmodeled | per research/asset-management/annual-operating-budget-builder-research.md |
| Partial payment accepted post-pay-or-quit without non-waiver addendum | Eviction voided; legal-risk event | per research/asset-management/rent-collection-delinquency-manager-research.md |
| Contingency burn > program-complete % at 40%+ CapEx complete | Cost overrun 15 – 25%+ likely | per research/asset-management/capex-value-add-execution-tracker-research.md |

---

## Cross-Reference Index

| Topic | Primary Source |
|---|---|
| KPI formulas (NOI, EGI, DSCR, LTL, economic occupancy, bad debt) | `knowledge/underwriting-calc.md` and `_taxonomy-seed.md` §2 |
| Line-item OpEx per-unit ranges (Class A/B/C) | `knowledge/multifamily-benchmarks.md` §Operating Expense Benchmarks |
| Regional, vintage, catastrophe, COL multipliers | `knowledge/multifamily-benchmarks.md` §Submarket Adjustment Protocol |
| Property tax effective rates by state/metro | `knowledge/multifamily-benchmarks.md` §Property Taxes by State / §Effective Tax Rates by Major Metro |
| Insurance catastrophe-zone adjustments (flood, hurricane, earthquake, wildfire, tornado) | `knowledge/multifamily-benchmarks.md` §Catastrophe Zone Adjustments |
| Rent-to-income ratios, loss-to-lease interpretation, rent growth by tier | `knowledge/multifamily-benchmarks.md` §Rent Benchmarks |
| Cap rate ranges and spread over treasuries | `knowledge/multifamily-benchmarks.md` §Cap Rate Ranges |
| Financing parameters (LTV, DSCR, debt yield, rate benchmarks) | `knowledge/multifamily-benchmarks.md` §Financing Standards |
| Variance Timing / Permanent / One-Time bucket decision rules | `_taxonomy-seed.md` §3 |
| A/R aging band definitions and split-aging rule | `_taxonomy-seed.md` §5 |
| Rent terminology (Face / Effective / Market / In-Place / Contract) | `_taxonomy-seed.md` §4 |
| Variance materiality thresholds (% + $ dual floor) | **This KB §1** |
| A/R reserve percentages by aging band | **This KB §2** |
| Stabilization definition matrix (agency / owner / LP / bridge) | **This KB §3** |
| Turnover cost — wide vs direct definition | **This KB §4** |
| Unit-turn capex Light / Medium / Heavy tiers | **This KB §5** |
| Concession depth by market condition | **This KB §6** |
| Bad-debt % by class with regional overlay | **This KB §7** |
| Absorption pace by market tier and cycle | **This KB §8** |
| Ancillary income levers — typical portfolio lifts | **This KB §9** |
| Rent-premium realization % by sponsor and market | **This KB §10** |

---

*Last updated: April 2026. Benchmarks are 2024-2026 calibrated and should be revalidated against current research notes and live market data (Yardi Matrix, RealPage, ALN, NAA/IREM/BOMA I/E IQ, REIT 10-Ks) for each specific asset. Knowledge base version v1.3.0 — companion to the Asset Management skill pack.*
