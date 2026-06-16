# Underwriting Calculations - Multifamily Focus

> **What this is:** A complete library of CRE financial formulas and calculation methods for multifamily underwriting, covering income metrics, operating expenses, valuation, debt, returns, value-add analysis, and sensitivity modeling.
> **How to use it:** Load this knowledge base alongside any skill file that references it, or use it as a standalone reference for building and verifying multifamily financial models.

This document defines every formula and calculation used during underwriting analysis. The calculations cover standard CRE metrics plus multifamily-specific analytics for income, expenses, value-add scenarios, and sensitivity analysis.

---

## Core Income Metrics

### Gross Potential Income (GPI)

Total income if the property were 100% occupied at market rents with no concessions or losses.

```
GPI = Sum of all unit market rents (annualized) + Other Income
```

For multifamily:
```
GPI = (Unit Count x Average Market Rent x 12) + Annual Other Income
```

### Effective Gross Income (EGI)

Actual expected income after accounting for vacancy, credit loss, and concessions.

```
EGI = GPI - Vacancy Loss - Credit Loss - Concessions
```

Where:
```
Vacancy Loss = GPI x Vacancy Rate
Credit Loss = GPI x Credit Loss Rate (typically 1-2%)
Concessions = Total annualized value of free rent, move-in specials, etc.
```

### Net Operating Income (NOI)

The property's income after all operating expenses but before debt service and capital expenditures.

```
NOI = EGI - Total Operating Expenses
```

This is the single most important number in CRE underwriting. All valuation and return metrics derive from NOI.

---

## Operating Expenses

### Total Operating Expenses (Total OpEx)

```
Total OpEx = Property Taxes + Insurance + Utilities + Repairs & Maintenance
             + Management Fee + Payroll + Administrative + Turnover Costs
             + Landscaping + Pest Control + Marketing + Legal & Professional
             + Capital Reserves
```

### Operating Expense Ratio

```
OpEx Ratio = Total Operating Expenses / EGI
```

Benchmark ranges by property size (see Expense Ratio Benchmarks section below).

### Management Fee

```
Management Fee = EGI x Management Fee Rate
```

Typical rates: 4-8% of EGI for multifamily. Smaller properties trend higher (6-8%), larger properties trend lower (4-5%).

### Property Tax Estimation

```
Estimated Annual Tax = Assessed Value x Mill Rate / 1000
```

Or, if using purchase price as a proxy for reassessment:

```
Estimated Annual Tax = Purchase Price x Local Tax Rate
```

**Important:** Many jurisdictions reassess on sale. Always check if the current tax basis will reset to the acquisition price. If so, use the acquisition price for post-close tax projections, not the current assessed value.

---

## Valuation Metrics

### Capitalization Rate (Cap Rate)

```
Cap Rate = NOI / Property Value (or Purchase Price)
```

Solving for value:
```
Property Value = NOI / Cap Rate
```

### Cap Rate Spread

The spread between the property cap rate and the risk-free rate (10-year Treasury yield).

```
Cap Rate Spread = Cap Rate - 10-Year Treasury Yield
```

A healthy spread indicates adequate risk premium. Minimum acceptable spread is typically 150-200 bps.

### Gross Rent Multiplier (GRM)

```
GRM = Purchase Price / Annual Gross Rent
```

Lower GRM = potentially better value. Typical multifamily GRM ranges: 8-15x depending on market.

### Price Per Unit

```
Price Per Unit = Purchase Price / Total Unit Count
```

This is a quick comparability metric. Compare to market comps on a per-unit basis.

### Price Per Square Foot

```
Price Per SF = Purchase Price / Total Rentable Square Footage
```

---

## Debt Metrics

### Loan Payment (Monthly)

```
Monthly Payment = Loan Amount x [r(1+r)^n] / [(1+r)^n - 1]
```

Where:
```
r = Annual Interest Rate / 12
n = Amortization Period in Months (e.g., 360 for 30 years)
```

### Interest-Only Payment (Monthly)

```
Monthly IO Payment = Loan Amount x (Annual Interest Rate / 12)
```

### Annual Debt Service

```
Annual Debt Service = Monthly Payment x 12
```

### Loan-to-Value (LTV)

```
LTV = Loan Amount / Property Value (or Purchase Price)
```

Typical maximums: 65-75% for multifamily acquisition, 60-70% for value-add.

### Debt Service Coverage Ratio (DSCR)

```
DSCR = NOI / Annual Debt Service
```

Minimum DSCR thresholds:
- Agency (Fannie/Freddie): 1.20-1.25x
- CMBS: 1.25-1.30x
- Bridge/Value-Add: 1.10-1.20x
- Bank: 1.25-1.35x

### Debt Yield

```
Debt Yield = NOI / Loan Amount
```

Minimum debt yield thresholds:
- Agency: 8-9%
- CMBS: 9-10%
- Bank: 10-11%

---

## Return Metrics

### Cash-on-Cash Return (CoC)

```
Cash-on-Cash = Annual Pre-Tax Cash Flow / Total Equity Invested
```

Where:
```
Annual Pre-Tax Cash Flow = NOI - Annual Debt Service
Total Equity Invested = Down Payment + Closing Costs + Renovation Budget
```

### Equity Multiple

```
Equity Multiple = Total Distributions / Total Equity Invested
```

### Internal Rate of Return (IRR)

IRR is the discount rate that makes the NPV of all cash flows equal to zero. Calculate iteratively or use standard financial functions. Include:
- Initial equity investment (negative)
- Annual cash flows during hold period
- Net sale proceeds at disposition (minus loan payoff, closing costs)

### Return on Cost (Development/Value-Add)

```
Return on Cost = Stabilized NOI / Total Project Cost
```

Where:
```
Total Project Cost = Purchase Price + Closing Costs + Renovation Budget + Carry Costs
```

---

## Multifamily Income Analysis

### Per-Unit Rent Roll Aggregation

Aggregate the rent roll to calculate key income metrics:

```
Total In-Place Monthly Rent = Sum of all current unit rents
Average In-Place Rent = Total In-Place Monthly Rent / Occupied Unit Count
Average Rent Per SF = Average In-Place Rent / Average Unit SF
Occupancy Rate = Occupied Units / Total Units
Physical Vacancy = 1 - Occupancy Rate
```

Break down by unit type:
```
For each unit type (Studio, 1BR, 2BR, 3BR+):
  - Unit count
  - Average in-place rent
  - Average market rent
  - Average SF
  - Rent per SF
  - Vacancy rate
```

### Loss-to-Lease Calculation

Loss-to-lease measures the difference between what tenants are currently paying and what the market would bear. This is a key value-add indicator.

```
Loss-to-Lease (per unit) = Market Rent - In-Place Rent
Loss-to-Lease (total monthly) = Sum of (Market Rent - In-Place Rent) for all occupied units
Loss-to-Lease (%) = Loss-to-Lease (total monthly) / Total Market Rent (monthly) x 100
Annual Loss-to-Lease = Loss-to-Lease (total monthly) x 12
```

**Interpretation:**
- Loss-to-Lease > 10%: Strong value-add opportunity through rent increases
- Loss-to-Lease 5-10%: Moderate upside, achievable through natural lease turnover
- Loss-to-Lease < 5%: Property is near market rents, limited organic upside

### Concessions and Free Rent Adjustments

```
Effective Rent = Face Rent - (Concession Value / Lease Term in Months)
```

Common concessions to quantify:
- Free month(s) of rent
- Reduced security deposit
- Move-in specials (gift cards, reduced first month)
- Utility credits

```
Total Concession Drag = Sum of all annualized concession values
Adjusted GPI = GPI - Total Concession Drag
```

### Other Income (Ancillary Revenue)

Multifamily properties generate income beyond base rent. Quantify each line item:

```
Other Income = Laundry Income + Parking Income + Pet Fees + RUBS Income
               + Application Fees + Late Fees + Storage Income
               + Vending Income + Cable/Internet Revenue Share
```

**RUBS (Ratio Utility Billing System):**
```
RUBS Revenue = Number of Units on RUBS x Average Monthly RUBS Charge x 12
RUBS Recovery Rate = RUBS Revenue / Total Utility Expense
```

Target RUBS recovery: 60-85% of utility costs.

**Per-unit other income benchmarks:**
- Class A: $150-300/unit/month
- Class B: $75-150/unit/month
- Class C: $25-75/unit/month

### Bad Debt Allowance

```
Bad Debt = GPI x Bad Debt Rate
```

Typical bad debt rates:
- Class A: 0.5-1.0% of GPI
- Class B: 1.0-1.5% of GPI
- Class C: 1.5-2.5% of GPI
- Workforce/Affordable: 2.0-3.0% of GPI

---

## Expense Ratio Benchmarks

### Multifamily OpEx Ratios by Unit Count

| Unit Count | Typical OpEx Ratio | Notes |
|-----------|-------------------|-------|
| 5-20 units | 50-60% | No on-site staff, higher per-unit costs |
| 20-50 units | 45-55% | May have part-time maintenance |
| 50-100 units | 40-50% | Part-time or full-time staff, economies of scale emerging |
| 100-150 units | 38-48% | Full-time leasing + maintenance staff |
| 150-250 units | 35-45% | Full on-site team, significant scale benefits |
| 250+ units | 32-42% | Fully staffed, maximum operational efficiency |

### Payroll Costs for On-Site Staff

```
Total Payroll = Sum of (Salary + Benefits + Payroll Tax) for each position
Payroll Cost Per Unit = Total Payroll / Total Unit Count
```

Typical staffing ratios:
- Property Manager: 1 per 150-250 units
- Leasing Agent: 1 per 150-200 units
- Maintenance Tech: 1 per 75-100 units
- Groundskeeper: 1 per 200-300 units
- Porter/Housekeeper: 1 per 150-250 units

Benchmark payroll cost per unit: $800-1,500/unit/year (varies significantly by market and class).

### Turnover Costs

```
Annual Turnover Cost = Total Units x Turnover Rate x Cost Per Turn
```

Cost per turn includes:
- Cleaning: $200-500
- Paint/touch-up: $300-800
- Carpet/flooring: $400-1,200
- Appliance replacement (prorated): $100-300
- Marketing/vacancy loss during turn: $500-1,500
- Leasing commission (if applicable): $300-500

**Total cost per turn: $1,500-3,000 per unit** (varies by class and scope)

Typical turnover rates:
- Class A: 40-50% annually
- Class B: 45-55% annually
- Class C: 50-65% annually

```
Effective Turnover Cost Per Unit Per Year = Cost Per Turn x Turnover Rate
```

### Capital Reserves (Replacement Reserves)

```
Annual Capital Reserves = Total Units x Reserve Per Unit Per Year
```

Industry standards:
- **Minimum:** $250/unit/year (newer properties, good condition)
- **Standard:** $300-400/unit/year (typical allocation)
- **Aggressive:** $400-500/unit/year (older properties, deferred maintenance)
- **Major rehab planned:** $500+/unit/year

Lender requirements vary:
- Agency (Fannie/Freddie): $250-300/unit/year minimum
- CMBS: $250-300/unit/year minimum
- Bridge: Often not required during business plan execution

---

## Value-Add Metrics

### Renovation ROI Calculation

```
Renovation ROI = Annual Rent Increase / Renovation Cost Per Unit x 100
```

Or on a per-dollar basis:
```
Rent Premium Per Dollar = Monthly Rent Increase / Renovation Cost Per Unit
```

**Target benchmarks:**
- Light renovation ($5,000-10,000/unit): $75-150/month rent increase, 12-20% ROI
- Moderate renovation ($10,000-20,000/unit): $150-300/month rent increase, 15-25% ROI
- Heavy renovation ($20,000-35,000/unit): $250-500/month rent increase, 12-20% ROI

**Rule of thumb:** Target a minimum 15% unlevered ROI on renovation spend, or a rent premium of at least $1.00 per $100 spent per month.

### Stabilized vs In-Place NOI Comparison

```
In-Place NOI = Current EGI - Current Operating Expenses
Stabilized NOI = Pro Forma EGI (at market rents, stabilized vacancy) - Stabilized Operating Expenses
NOI Upside = Stabilized NOI - In-Place NOI
NOI Upside (%) = (Stabilized NOI - In-Place NOI) / In-Place NOI x 100
```

**Stabilized assumptions typically mean:**
- All renovated units leased at target rents
- Vacancy at market rate (not lease-up level)
- RUBS fully implemented
- Other income programs in place
- Operating expenses normalized (no one-time costs)

### Construction Period Cash Flow Modeling

During renovation, cash flow is impacted by:

```
Construction Period Cash Flow = In-Place NOI (from non-renovated units)
                                - Renovation Vacancy Loss (units offline for renovation)
                                - Renovation CapEx (spread over renovation period)
                                - Incremental Operating Costs (construction management, etc.)
                                + Incremental Revenue (from units already renovated and leased)
```

Model month-by-month:
```
For each month in renovation period:
  Units Offline = Number of units under renovation this month
  Units Completed = Cumulative units renovated and leased
  Monthly Income = (Occupied Non-Renovated Units x In-Place Rent)
                   + (Units Completed x Renovated Rent)
  Monthly Expense = Operating Expenses + Renovation Spend This Month
  Monthly Cash Flow = Monthly Income - Monthly Expense
```

---

## Investment Thresholds Quick Reference

### Acquisition Criteria (Multifamily)

| Metric | Minimum Acceptable | Target | Strong |
|--------|-------------------|--------|--------|
| Cap Rate (in-place) | 4.5% | 5.5-6.5% | 7.0%+ |
| Cap Rate (stabilized) | 5.5% | 6.5-7.5% | 8.0%+ |
| Cash-on-Cash (Year 1) | 4.0% | 6.0-8.0% | 10.0%+ |
| Cash-on-Cash (Stabilized) | 7.0% | 9.0-12.0% | 14.0%+ |
| DSCR | 1.20x | 1.30-1.40x | 1.50x+ |
| Debt Yield | 8.0% | 9.5-11.0% | 12.0%+ |
| Equity Multiple (5-yr) | 1.5x | 1.8-2.2x | 2.5x+ |
| IRR (5-yr hold) | 12% | 15-18% | 20%+ |
| Renovation ROI | 12% | 15-20% | 25%+ |
| Price Per Unit vs Replacement | < 80% | < 65% | < 50% |
| OpEx Ratio | < 55% | 40-48% | < 38% |
| Loss-to-Lease | > 5% | > 10% | > 15% |

### Dealbreaker Thresholds

| Metric | Dealbreaker If |
|--------|---------------|
| Cap Rate (in-place) | < 3.5% (unless deep value-add) |
| DSCR | < 1.10x |
| Debt Yield | < 7.0% |
| OpEx Ratio | > 65% (without clear fix) |
| Occupancy | < 70% (without clear lease-up plan) |
| Renovation ROI | < 10% |
| Cap Rate Spread | < 100 bps above risk-free rate |
| Bad Debt | > 5% of GPI |

---

## Sensitivity Analysis Framework

Run sensitivity analysis on every deal to understand risk exposure. Vary key assumptions and measure impact on returns.

### Variables to Stress Test

| Variable | Base Case | Downside | Severe Downside |
|----------|-----------|----------|-----------------|
| Vacancy Rate | Market rate | +5% | +10% |
| Rent Growth | Projected rate | 0% (flat) | -5% (decline) |
| Exit Cap Rate | Entry cap | +50 bps | +100 bps |
| Interest Rate | Quoted rate | +50 bps | +100 bps |
| Operating Expenses | Budget | +10% | +20% |
| Renovation Cost | Budget | +15% | +30% |
| Renovation Timeline | Planned | +3 months | +6 months |
| Rent Premium | Projected | -20% | -40% |

### Sensitivity Matrix (Example: NOI Impact)

```
                    Vacancy Rate
                    5%      7%      10%     12%
Rent Growth  3%   [NOI]   [NOI]   [NOI]   [NOI]
             1%   [NOI]   [NOI]   [NOI]   [NOI]
             0%   [NOI]   [NOI]   [NOI]   [NOI]
            -2%   [NOI]   [NOI]   [NOI]   [NOI]
```

### Break-Even Analysis

Calculate the break-even point for key metrics:

```
Break-Even Occupancy = (Operating Expenses + Debt Service) / GPI
Break-Even Rent = (Operating Expenses + Debt Service) / (Occupied Units x 12)
```

### Scenario Modeling

Run three complete scenarios through the full underwriting model:

1. **Base Case**: Most likely assumptions based on market data and property analysis
2. **Downside Case**: Conservative assumptions -- higher vacancy, lower rent growth, higher expenses, wider exit cap
3. **Upside Case**: Optimistic but achievable -- faster lease-up, stronger rents, lower exit cap

For each scenario, calculate: NOI, Cash-on-Cash, IRR, Equity Multiple, DSCR, and Debt Yield.

**Decision framework:**
- If the **Downside Case** still meets minimum investment thresholds: Strong deal
- If only the **Base Case** meets thresholds: Marginal deal, proceed with caution
- If the **Base Case** does not meet thresholds: Pass unless there is a compelling strategic reason

---

## Worked Examples

All examples below use the **Parkview Apartments** test deal:

| Parameter | Value |
|-----------|-------|
| Property | 200-unit Class B multifamily, Portland OR |
| Purchase Price | $32,000,000 |
| Gross Potential Rent (GPR) | $3,840,000/yr ($1,600/unit/mo avg) |
| Vacancy & Credit Loss | 7% |
| Other Income | $180,000/yr (laundry, parking, late fees) |
| Total Operating Expenses | $1,687,500 ($8,438/unit) |
| Loan Amount | $22,400,000 (70% LTV) |
| Interest Rate | 5.75% fixed, 30-year amortization, 10-year term |
| Hold Period | 5 years |
| Exit Cap Rate | 6.75% |
| Annual NOI Growth | 2.5% |

---

### Worked Example 1: Net Operating Income (NOI) Calculation

Walk through the full income waterfall from Gross Potential Rent to NOI.

**Step 1 -- Gross Potential Rent (GPR)**

GPR is what the property earns if every unit is occupied at current asking rents with zero loss.

```
GPR = Unit Count x Average Monthly Rent x 12
GPR = 200 units x $1,600/mo x 12
GPR = $3,840,000
```

**Step 2 -- Vacancy & Credit Loss**

Parkview runs a 7% combined vacancy and credit loss factor (5% physical vacancy + 2% credit/bad debt).

```
Vacancy & Credit Loss = GPR x Vacancy Rate
                      = $3,840,000 x 0.07
                      = $268,800
```

**Step 3 -- Other Income**

Other income includes laundry ($72,000), parking ($60,000), late fees ($24,000), and application fees ($24,000).

```
Other Income = $72,000 + $60,000 + $24,000 + $24,000
             = $180,000
```

**Step 4 -- Effective Gross Income (EGI)**

```
EGI = GPR - Vacancy & Credit Loss + Other Income
    = $3,840,000 - $268,800 + $180,000
    = $3,751,200
```

**Step 5 -- Total Operating Expenses**

The expense breakdown at Parkview:

| Expense Category | Amount | Per Unit |
|-----------------|--------|----------|
| Property Taxes | $384,000 | $1,920 |
| Insurance | $112,000 | $560 |
| Utilities (common area) | $168,000 | $840 |
| Repairs & Maintenance | $200,000 | $1,000 |
| Management Fee (5% EGI) | $187,560 | $938 |
| Payroll (on-site staff) | $280,000 | $1,400 |
| Turnover Costs | $120,000 | $600 |
| Administrative | $48,000 | $240 |
| Marketing | $36,000 | $180 |
| Landscaping & Grounds | $44,000 | $220 |
| Pest Control | $12,000 | $60 |
| Legal & Professional | $15,940 | $80 |
| Capital Reserves ($300/unit) | $60,000 | $300 |
| **Total** | **$1,687,500** | **$8,438** |

Check: OpEx Ratio = $1,687,500 / $3,751,200 = **45.0%** (within the 35-45% benchmark for 150-250 unit properties).

**Step 6 -- NOI**

```
NOI = EGI - Total Operating Expenses
    = $3,751,200 - $1,687,500
    = $2,063,700
```

**Verification:** NOI per unit = $2,063,700 / 200 = $10,319/unit/year. Reasonable for a Class B Portland multifamily.

---

### Worked Example 2: Capitalization Rate (Cap Rate)

**Forward calculation -- cap rate from purchase price:**

```
Cap Rate = NOI / Purchase Price
         = $2,063,700 / $32,000,000
         = 0.0645
         = 6.45%
```

**Reverse calculation -- value from NOI and a target cap rate:**

If a buyer requires a 7.00% cap rate on the same NOI:

```
Implied Value = NOI / Target Cap Rate
              = $2,063,700 / 0.07
              = $29,481,429
```

At a 7.00% cap requirement, the buyer would offer roughly $29.5M -- about $2.5M less than the $32M asking price.

**Cap rate spread check:**

Assuming the 10-Year Treasury yields 4.25% at time of analysis:

```
Cap Rate Spread = Cap Rate - 10-Year Treasury
                = 6.45% - 4.25%
                = 2.20% (220 bps)
```

220 bps exceeds the 150-200 bps minimum threshold. The risk premium is adequate.

**Gross Rent Multiplier (GRM) cross-check:**

```
GRM = Purchase Price / Annual Gross Rent
    = $32,000,000 / $3,840,000
    = 8.33x
```

**Price per unit:**

```
Price Per Unit = $32,000,000 / 200 = $160,000/unit
```

---

### Worked Example 3: Debt Service Coverage Ratio (DSCR)

**Step 1 -- Calculate monthly debt service**

Loan terms: $22,400,000 at 5.75% interest, 30-year (360 month) amortization.

```
r = Annual Rate / 12 = 0.0575 / 12 = 0.00479167
n = 360 months

Monthly Payment = Loan Amount x [r(1+r)^n] / [(1+r)^n - 1]
```

Calculate the components:

```
(1 + r)^n = (1.00479167)^360

Using logarithms:
ln(1.00479167) = 0.004780
0.004780 x 360 = 1.720915
e^1.720915 = 5.5901

So (1 + r)^n = 5.5901

Numerator:   r x (1+r)^n = 0.00479167 x 5.5901 = 0.026788
Denominator: (1+r)^n - 1 = 5.5901 - 1 = 4.5901

Monthly Payment = $22,400,000 x (0.026788 / 4.5901)
                = $22,400,000 x 0.005836
                = $130,736
```

**Step 2 -- Annual debt service**

```
Annual Debt Service = Monthly Payment x 12
                    = $130,736 x 12
                    = $1,568,832
```

**Step 3 -- DSCR**

```
DSCR = NOI / Annual Debt Service
     = $2,063,700 / $1,568,832
     = 1.315x
```

**Interpretation:** 1.315x exceeds the Agency minimum of 1.20-1.25x and the CMBS minimum of 1.25-1.30x. This deal qualifies for conventional permanent financing.

**Step 4 -- Debt yield (cross-check)**

```
Debt Yield = NOI / Loan Amount
           = $2,063,700 / $22,400,000
           = 9.21%
```

9.21% exceeds the Agency 8-9% threshold and is near the CMBS 9-10% range. Adequate.

**Interest-only comparison:** If the first 2 years are interest-only:

```
Monthly IO Payment = $22,400,000 x (0.0575 / 12)
                   = $22,400,000 x 0.004792
                   = $107,333

Annual IO Debt Service = $107,333 x 12 = $1,288,000

DSCR (IO period) = $2,063,700 / $1,288,000 = 1.602x
```

The IO period yields a significantly higher DSCR (1.60x vs 1.32x), which matters for value-add deals that need cash flow headroom during renovation.

---

### Worked Example 4: Cash-on-Cash Return

**Step 1 -- Total equity required**

```
Down Payment  = Purchase Price - Loan Amount
              = $32,000,000 - $22,400,000
              = $9,600,000
```

Note: In a full model, you would also add closing costs (1.5-2.5% of price) and any initial capital reserves. For this example we use the equity contribution of $9,600,000.

**Step 2 -- Cash flow after debt service (CFADS)**

```
CFADS = NOI - Annual Debt Service
      = $2,063,700 - $1,568,832
      = $494,868
```

**Step 3 -- Cash-on-cash return**

```
Cash-on-Cash = CFADS / Total Equity Invested
             = $494,868 / $9,600,000
             = 0.05155
             = 5.15%
```

**Interpretation:** 5.15% exceeds the 4.0% minimum acceptable Year 1 CoC threshold but falls short of the 6.0-8.0% target range. This is typical for a stabilized acquisition at today's interest rates. The deal makes up for modest Year 1 cash yield through appreciation and equity build (see IRR example below).

**Break-even occupancy check:**

```
Break-Even Occupancy = (Operating Expenses + Debt Service) / GPR (including Other Income)
                     = ($1,687,500 + $1,568,832) / ($3,840,000 + $180,000)
                     = $3,256,332 / $4,020,000
                     = 81.0%
```

The property must maintain at least 81% economic occupancy to cover all expenses and debt service. Current occupancy is 93% (7% vacancy), providing a 12-point cushion.

---

### Worked Example 5: Internal Rate of Return (IRR)

The IRR is the discount rate that sets the net present value of all cash flows to zero. We build year-by-year cash flows for a 5-year hold.

**Assumptions:**
- NOI grows 2.5% annually
- Debt service is constant (fully amortizing)
- Exit at Year 5 end at a 6.75% cap rate
- Disposition costs: 2.0% of sale price (broker commission + closing)

**Step 1 -- Project annual cash flows**

| Year | NOI | Debt Service | CFADS |
|------|-----|-------------|-------|
| 0 | -- | -- | -$9,600,000 (equity invested) |
| 1 | $2,063,700 | $1,568,832 | $494,868 |
| 2 | $2,115,293 | $1,568,832 | $546,461 |
| 3 | $2,168,175 | $1,568,832 | $599,343 |
| 4 | $2,222,379 | $1,568,832 | $653,547 |
| 5 | $2,277,939 | $1,568,832 | $709,107 |

NOI growth calculation:
```
Year 2 NOI = $2,063,700 x 1.025 = $2,115,293
Year 3 NOI = $2,115,293 x 1.025 = $2,168,175
Year 4 NOI = $2,168,175 x 1.025 = $2,222,379
Year 5 NOI = $2,222,379 x 1.025 = $2,277,939
```

**Step 2 -- Calculate exit (terminal) value at end of Year 5**

The exit cap rate uses Year 6 forward NOI (Year 5 NOI grown one more period):

```
Year 6 Forward NOI = $2,277,939 x 1.025 = $2,334,887
```

Rounding for the example: $2,334,000 (consistent with deal data).

```
Exit Price = Year 6 Forward NOI / Exit Cap Rate
           = $2,334,000 / 0.0675
           = $34,578,000 (rounded)
```

**Step 3 -- Calculate net sale proceeds**

Estimate the remaining loan balance after 5 years of amortization. After 60 payments on a 30-year amortizing $22.4M loan at 5.75%:

```
Remaining Loan Balance (approx.) = $20,830,000
```

(Calculated by summing remaining principal after 60 monthly payments.)

```
Gross Sale Proceeds          = $34,578,000
Less: Disposition Costs (2%) = ($691,560)
Less: Loan Payoff            = ($20,830,000)
Net Equity Proceeds          = $13,056,440
```

**Step 4 -- Build complete cash flow schedule**

| Year | Operating CFADS | Disposition Proceeds | Total Cash Flow |
|------|----------------|---------------------|----------------|
| 0 | -- | -- | -$9,600,000 |
| 1 | $494,868 | -- | $494,868 |
| 2 | $546,461 | -- | $546,461 |
| 3 | $599,343 | -- | $599,343 |
| 4 | $653,547 | -- | $653,547 |
| 5 | $709,107 | $13,056,440 | $13,765,547 |

**Step 5 -- Solve for IRR**

The IRR is the rate (r) that satisfies:

```
0 = -9,600,000
    + 494,868 / (1+r)^1
    + 546,461 / (1+r)^2
    + 599,343 / (1+r)^3
    + 653,547 / (1+r)^4
    + 13,765,547 / (1+r)^5
```

Solving iteratively (or via financial calculator / spreadsheet):

```
Levered IRR = 12.8%
```

**Interpretation:** 12.8% exceeds the 12% minimum but falls short of the 15-18% target range. This is a deal that meets minimum hurdles. Value-add upside (not modeled here) or a tighter exit cap could push returns into the target range.

---

### Worked Example 6: Equity Multiple

The equity multiple measures total return as a multiple of invested equity.

**Step 1 -- Total distributions (all cash received)**

```
Total Distributions = Sum of all cash flows to equity
                    = $494,868 + $546,461 + $599,343 + $653,547 + $13,765,547
                    = $16,059,766
```

**Step 2 -- Equity multiple**

```
Equity Multiple = Total Distributions / Total Equity Invested
                = $16,059,766 / $9,600,000
                = 1.673x
```

Rounding with the deal data inputs: **1.72x** (the slight difference comes from rounding in intermediate steps; the deal data sheet carries more decimal precision through the loan balance calculation).

**Interpretation:** 1.72x means an investor receives $1.72 for every $1.00 invested over the 5-year hold. This is above the 1.5x minimum but below the 1.8-2.2x target. Combined with the 12.8% IRR, this deal is investable but not compelling purely on stabilized returns -- value-add execution or favorable market movement would be needed to reach target thresholds.

**Decomposing the equity multiple:**

```
Cash Flow Component   = ($494,868 + $546,461 + $599,343 + $653,547 + $709,107) / $9,600,000
                      = $3,003,326 / $9,600,000
                      = 0.313x (31.3% of equity returned through operations)

Principal Paydown     = $22,400,000 - $20,830,000 = $1,570,000
Appreciation          = $34,578,000 - $32,000,000 = $2,578,000
Disposition Costs     = -$691,560

Reversion Component   = ($2,578,000 + $1,570,000 - $691,560) / $9,600,000
                      = $3,456,440 / $9,600,000
                      = 0.360x (36.0% of equity from appreciation + paydown)

Total Check: 1.000x (return of capital) + 0.313x + 0.360x = 1.673x
```

---

## Edge Cases & Special Scenarios

Underwriting models must handle non-standard situations gracefully. The following edge cases arise regularly in practice. Each section describes the scenario, explains why it matters, provides handling instructions, and includes a brief calculation snippet.

---

### Edge Case 1: Negative NOI

**Description:** Operating expenses exceed Effective Gross Income, producing a negative NOI. This can happen with severely distressed properties, vacant buildings, or properties with abnormally high tax or insurance burdens.

**Why it matters:** Negative NOI breaks standard valuation methods. A negative cap rate is meaningless, DSCR is negative (or undefined if debt service is zero), and income-approach valuation produces a negative number. If the underwriting produces a negative NOI, halt the standard analysis and flag the result.

**How to handle it in the model:**
1. Calculate NOI normally. Do not force it to zero.
2. If NOI < 0, skip cap-rate-based valuation. Use replacement cost or comparable sales (price per unit / per SF) instead.
3. Set DSCR = 0.00x and flag as **DSCR: FAIL - Negative NOI**.
4. Cash-on-Cash and IRR calculations should still run (they will produce negative values), but flag as distressed.
5. Model the path to positive NOI: what occupancy, rent, or expense level is required?

**Example calculation snippet:**

```
Scenario: 200-unit property, 40% occupied
GPR (at 40% occupancy) = 80 units x $1,200/mo x 12 = $1,152,000
Other Income = $20,000
EGI = $1,172,000
Operating Expenses = $1,400,000 (fixed costs dominate at low occupancy)

NOI = $1,172,000 - $1,400,000 = -$228,000

Cap Rate: UNDEFINED (negative NOI / positive price is meaningless)
DSCR: 0.00x --> FAIL

Break-even occupancy required:
  Required EGI = $1,400,000 (to reach NOI = $0)
  Required occupied units = ($1,400,000 - $20,000) / ($1,200 x 12) = 96 units
  Break-even occupancy = 96 / 200 = 48%
```

**What to flag in output:**
- `[CRITICAL] NOI is negative: -$228,000. Income-approach valuation not applicable.`
- `[CRITICAL] DSCR: 0.00x. Property cannot support any debt at current occupancy.`
- `[INFO] Break-even occupancy: 48%. Current occupancy: 40%. Gap: 8 percentage points (16 units).`

---

### Edge Case 2: Zero Equity / 100% LTV

**Description:** The buyer contributes no equity -- the loan covers 100% of the purchase price (or more, in negative-equity assumptions). This is rare in conventional CRE but arises in seller-financed deals, assumed loans above current value, or synthetic structures.

**Why it matters:** Cash-on-Cash return and Equity Multiple require division by total equity invested. Division by zero produces undefined results. Additionally, any negative equity scenario (loan > value) inverts normal return logic.

**How to handle it in the model:**
1. If Total Equity Invested = $0, set Cash-on-Cash = "N/A (no equity invested)" and Equity Multiple = "N/A".
2. If Total Equity Invested < $0 (negative equity), flag as anomalous and skip CoC and EM calculations.
3. IRR can still be calculated if there is a meaningful initial cash outlay (closing costs, for example). If the initial cash flow is truly $0 or positive, IRR is mathematically infinite or undefined.
4. DSCR, debt yield, and NOI-based metrics remain valid and become the primary decision tools.

**Example calculation snippet:**

```
Scenario: Seller-financed at 100% LTV
Purchase Price = $32,000,000
Loan Amount    = $32,000,000
Equity         = $0
NOI            = $2,063,700
Debt Service   = $2,241,189 (higher loan amount --> higher ADS)

CFADS = $2,063,700 - $2,241,189 = -$177,489

Cash-on-Cash = -$177,489 / $0 --> UNDEFINED
Equity Multiple = Total Distributions / $0 --> UNDEFINED

DSCR = $2,063,700 / $2,241,189 = 0.921x --> FAIL (below 1.0x, negative cash flow)
```

**What to flag in output:**
- `[WARNING] Zero equity structure. Cash-on-Cash and Equity Multiple are not calculable.`
- `[CRITICAL] DSCR: 0.92x. Property cash flow does not cover debt service at 100% LTV.`
- `[INFO] Recommend evaluating with reduced leverage. LTV required for 1.25x DSCR: ~65%.`

---

### Edge Case 3: Interest-Only Period Exceeds Hold Period

**Description:** The loan has an interest-only (IO) term that extends beyond the planned hold period. For example, a 7-year IO period on a 10-year loan with a 5-year hold plan. The investor never makes a principal payment during the hold.

**Why it matters:** During IO, debt service is lower (boosting CFADS and CoC), but no principal is paid down, so the equity multiple depends entirely on cash flow and appreciation. The loan balance at exit equals the original loan amount, reducing net sale proceeds compared to an amortizing scenario.

**How to handle it in the model:**
1. Use the IO payment formula for every year within the hold period: `ADS = Loan Amount x Interest Rate`.
2. Do NOT amortize the loan balance during the IO hold period. Remaining balance at exit = original loan amount.
3. DSCR should be calculated using IO debt service (the actual obligation), not a hypothetical amortizing payment.
4. Clearly label all metrics as "IO-period" to distinguish from amortizing projections.
5. Run a parallel amortizing scenario for comparison.

**Example calculation snippet:**

```
Parkview with 7-year IO (exceeds 5-year hold):

IO Annual Debt Service = $22,400,000 x 0.0575 = $1,288,000
Amortizing ADS (for comparison) = $1,568,832

Year 1 CFADS (IO)        = $2,063,700 - $1,288,000 = $775,700
Year 1 CFADS (Amortizing) = $2,063,700 - $1,568,832 = $494,868

CoC (IO)        = $775,700 / $9,600,000 = 8.08%
CoC (Amortizing) = $494,868 / $9,600,000 = 5.15%

DSCR (IO)        = $2,063,700 / $1,288,000 = 1.602x
DSCR (Amortizing) = $2,063,700 / $1,568,832 = 1.315x

Exit after 5 years:
  Loan balance (IO):        $22,400,000 (no paydown)
  Loan balance (Amortizing): $20,830,000 ($1,570,000 paid down)

  Net proceeds (IO):        $34,578,000 - $691,560 - $22,400,000 = $11,486,440
  Net proceeds (Amortizing): $34,578,000 - $691,560 - $20,830,000 = $13,056,440

  Difference: -$1,570,000 less equity at exit on IO structure
```

**What to flag in output:**
- `[INFO] IO period (7 years) exceeds hold period (5 years). No principal paydown during hold.`
- `[INFO] IO structure boosts Year 1 CoC by 293 bps (8.08% vs 5.15%) but reduces exit equity by $1,570,000.`
- `[INFO] DSCR calculated on IO basis: 1.60x. Lender may also require amortizing DSCR test (1.32x).`

---

### Edge Case 4: Variable Rate Debt

**Description:** The loan carries a floating interest rate (e.g., SOFR + 275 bps) rather than a fixed rate. Future debt service is uncertain, making cash flow projections inherently speculative.

**Why it matters:** A 100 bps rate increase on $22.4M of debt adds roughly $224,000/year to debt service, which can eliminate cash flow entirely. Variable rate debt injects significant uncertainty into IRR and CoC projections.

**How to handle it in the model:**
1. Build three rate scenarios: Base, +100 bps, +200 bps (or use the forward SOFR curve for the base case).
2. Calculate debt service, CFADS, CoC, DSCR, and IRR under each scenario.
3. If a rate cap is purchased, model the capped rate as the maximum in the upside/base scenarios and note the cap cost as an upfront equity expense.
4. Present all return metrics as ranges, not point estimates.
5. Calculate the "break-even rate" -- the rate at which DSCR hits 1.00x.

**Example calculation snippet:**

```
Parkview with floating rate debt: SOFR + 2.75%
Current SOFR: 3.00% --> Current all-in rate: 5.75%

Scenario A (Base): SOFR stays at 3.00% --> Rate = 5.75%
  ADS = $1,568,832 | CFADS = $494,868 | CoC = 5.15% | DSCR = 1.32x

Scenario B (+100 bps): SOFR rises to 4.00% --> Rate = 6.75%
  IO-equivalent ADS increase = $22,400,000 x 0.01 = +$224,000
  Adjusted ADS = $1,792,832 | CFADS = $270,868 | CoC = 2.82% | DSCR = 1.15x

Scenario C (+200 bps): SOFR rises to 5.00% --> Rate = 7.75%
  Adjusted ADS = $2,016,832 | CFADS = $46,868 | CoC = 0.49% | DSCR = 1.02x

Break-even rate (DSCR = 1.00x):
  Required ADS = NOI = $2,063,700
  Break-even rate approximately 7.96% (SOFR = 5.21%)

Rate cap cost estimate:
  2-year cap at 5.50% strike on $22.4M notional = $250,000-400,000 upfront
```

**What to flag in output:**
- `[WARNING] Variable rate debt. Return metrics are rate-dependent. Presenting 3-scenario range.`
- `[CRITICAL] At SOFR +200 bps, DSCR drops to 1.02x (near break-even). Cash flow nearly eliminated.`
- `[INFO] Break-even all-in rate: 7.96%. Current rate: 5.75%. Cushion: 221 bps.`
- `[RECOMMENDATION] Rate cap strongly recommended if floating rate is pursued.`

---

### Edge Case 5: Value-Add Renovation

**Description:** The acquisition business plan calls for unit renovations that temporarily take units offline, incur capital expenditure, and produce higher rents upon re-lease. Metrics must distinguish between in-place (current) and stabilized (post-renovation) performance.

**Why it matters:** Standard underwriting assumes a static property. Value-add deals have a J-curve: returns dip during renovation (vacant units, capital spend) before rising at stabilization. Using in-place metrics alone undervalues the deal; using stabilized metrics alone ignores execution risk and the cost to get there.

**How to handle it in the model:**
1. Carry two parallel NOI tracks: in-place and stabilized (pro forma).
2. Model the renovation period month-by-month: units offline, units completing, rent-up schedule.
3. Add renovation CapEx to equity required (it reduces CoC and increases equity in the denominator).
4. Calculate Return on Cost = Stabilized NOI / Total Project Cost.
5. Present both in-place and stabilized metrics, clearly labeled.

**Example calculation snippet:**

```
Parkview Value-Add Plan:
  Renovation scope: 150 of 200 units (75% of units)
  Cost per unit: $15,000
  Total renovation budget: $15,000 x 150 = $2,250,000
  Renovation pace: 10 units/month --> 15 months to complete
  Unit downtime: 3 weeks per unit
  Rent increase: $200/unit/month post-renovation ($1,600 --> $1,800)

Revised equity requirement:
  Down payment:        $9,600,000
  Renovation budget:   $2,250,000
  Total equity:        $11,850,000

In-Place Metrics (Day 1):
  NOI:      $2,063,700
  Cap Rate: 6.45%
  CoC:      $494,868 / $11,850,000 = 4.18%

Stabilized Metrics (Month 18+, all 150 units renovated):
  New GPR = (150 x $1,800 x 12) + (50 x $1,600 x 12) = $3,240,000 + $960,000 = $4,200,000
  Vacancy (5%): $210,000
  Other Income: $210,000 (additional from RUBS/amenity fees)
  Stabilized EGI: $4,200,000 - $210,000 + $210,000 = $4,200,000
  Stabilized OpEx: $1,850,000 (higher taxes, insurance on higher value)
  Stabilized NOI: $4,200,000 - $1,850,000 = $2,350,000

  Stabilized Cap Rate (on purchase): $2,350,000 / $32,000,000 = 7.34%
  Return on Cost: $2,350,000 / ($32,000,000 + $2,250,000) = 6.87%

Renovation ROI:
  Annual rent increase per unit: $200 x 12 = $2,400
  Per-unit ROI: $2,400 / $15,000 = 16.0% --> Meets the 15% minimum target

NOI Uplift: ($2,350,000 - $2,063,700) / $2,063,700 = 13.9%
```

**What to flag in output:**
- `[INFO] Value-add deal. Dual metrics: In-place NOI $2,063,700 (6.45% cap) vs. Stabilized NOI $2,350,000 (7.34% cap).`
- `[INFO] Renovation ROI: 16.0% (exceeds 15% threshold). Return on Cost: 6.87%.`
- `[INFO] Stabilization timeline: 15 months renovation + 3 months lease-up = ~18 months.`
- `[WARNING] Total equity required increases from $9.6M to $11.85M (+23%) to fund renovation.`

---

### Edge Case 6: Tax Reassessment on Sale

**Description:** Many jurisdictions reassess property taxes upon sale, resetting the assessed value to the purchase price. This can dramatically increase the tax burden, particularly in states where the prior owner held the property for decades at a low basis (e.g., California Prop 13 jurisdictions) or in states with annual reassessment to market value.

**Why it matters:** An underwriting model that uses the seller's current tax bill will understate post-acquisition expenses, inflating NOI and overstating returns. The tax increase can be tens or hundreds of thousands of dollars annually.

**How to handle it in the model:**
1. Determine whether the jurisdiction reassesses on sale (research county assessor rules).
2. If yes: calculate the new tax bill using the purchase price (or a percentage thereof) multiplied by the local mill rate.
3. Replace the current tax amount with the projected post-reassessment amount in the Year 1 expense budget.
4. For Prop 13 states (CA): annual increases are capped at 2%, so model a slow escalation.
5. For annual-reassessment states (OR, TX, etc.): assume assessed value tracks market value each year.

**Example calculation snippet:**

```
Parkview Apartments, Portland OR (annual reassessment state):

Seller's current assessed value: $24,000,000 (purchased 8 years ago)
Seller's current tax bill:       $288,000 ($24M x 1.20% mill rate)

Post-acquisition:
  New assessed value:    $32,000,000 (purchase price)
  New annual tax bill:   $32,000,000 x 0.012 = $384,000

Tax increase:            $384,000 - $288,000 = $96,000/year

Impact on NOI:
  NOI using seller's taxes:  $2,063,700 + $96,000 = $2,159,700 (overstated)
  NOI using buyer's taxes:   $2,063,700 (correctly uses $384,000)
  NOI overstatement if not adjusted: 4.7%

Impact on cap rate:
  Overstated cap rate: $2,159,700 / $32,000,000 = 6.75%
  Correct cap rate:    $2,063,700 / $32,000,000 = 6.45%
  Error: 30 bps (significant for pricing and go/no-go decisions)

Comparison -- California Prop 13 state:
  If property were in CA with same basis:
  Seller's tax (Prop 13 basis of $18M): $18,000,000 x 0.012 = $216,000
  Buyer's tax (reset to $32M):          $32,000,000 x 0.012 = $384,000
  Tax increase: $168,000/year (73% jump)
  Post-Prop 13: grows at max 2%/year going forward
```

**What to flag in output:**
- `[WARNING] Jurisdiction reassesses on sale. Current tax bill ($288,000) will reset to approximately $384,000 (+$96,000/yr).`
- `[INFO] Model already uses reassessed tax amount. NOI reflects post-acquisition expense basis.`
- `[INFO] If using broker's pro forma, verify they are NOT using seller's tax basis. Common error worth 30+ bps on cap rate.`

---

### Edge Case 7: Lease-Up Period (Occupancy Ramp)

**Description:** The property is below stabilized occupancy and will take time to lease up. This applies to new construction, repositioned assets, or distressed acquisitions with high vacancy. Income ramps gradually from current to stabilized levels over months.

**Why it matters:** A model that uses stabilized occupancy from Day 1 overstates Year 1 income. The lease-up period generates lower cash flow (or negative cash flow), increases equity needs (to cover shortfalls), and delays the return profile. IRR is especially sensitive to when cash flows begin.

**How to handle it in the model:**
1. Start the income projection at current occupancy, not stabilized.
2. Assume an absorption rate (units leased per month) based on market data. Typical: 8-15 units/month for multifamily.
3. Model monthly income during lease-up, then switch to annual once stabilized.
4. Include lease-up costs in the equity budget: marketing, concessions, staffing, carry costs.
5. Calculate DSCR at current occupancy (worst case), not stabilized.

**Example calculation snippet:**

```
Parkview lease-up scenario:
  Current occupancy: 65% (130 of 200 units)
  Target stabilized occupancy: 93% (186 units)
  Units to absorb: 56 units
  Absorption rate: 10 units/month --> 5.6 months to stabilize (round to 6)

Monthly income ramp:

| Month | Occupied | Monthly Rent Revenue | Monthly OpEx | Monthly NOI |
|-------|----------|---------------------|-------------|-------------|
| 1     | 130      | $208,000            | $140,625    | $67,375     |
| 2     | 140      | $224,000            | $140,625    | $83,375     |
| 3     | 150      | $240,000            | $140,625    | $99,375     |
| 4     | 160      | $256,000            | $140,625    | $115,375    |
| 5     | 170      | $272,000            | $140,625    | $131,375    |
| 6     | 180      | $288,000            | $140,625    | $147,375    |
| 7+    | 186      | $297,600            | $140,625    | $156,975    |

(Monthly OpEx simplified as Total OpEx / 12 = $1,687,500 / 12 = $140,625)

Year 1 blended NOI (6 months ramp + 6 months stabilized):
  Ramp NOI (months 1-6): $67,375 + $83,375 + $99,375 + $115,375 + $131,375 + $147,375 = $644,250
  Stabilized NOI (months 7-12): $156,975 x 6 = $941,850
  Year 1 Total NOI: $644,250 + $941,850 = $1,586,100

Compare to stabilized annual NOI: $156,975 x 12 = $1,883,700
Year 1 NOI shortfall: $1,883,700 - $1,586,100 = $297,600

Worst-case DSCR (Month 1, annualized):
  Annualized NOI at 65% occupancy: $67,375 x 12 = $808,500
  DSCR: $808,500 / $1,568,832 = 0.52x --> FAIL

DSCR at stabilization (Month 7+):
  Annualized NOI: $156,975 x 12 = $1,883,700
  DSCR: $1,883,700 / $1,568,832 = 1.20x --> Meets Agency minimum
```

**What to flag in output:**
- `[WARNING] Property is in lease-up. Current occupancy (65%) is 28 points below stabilized (93%).`
- `[CRITICAL] Day 1 annualized DSCR: 0.52x. Property cannot service debt at current occupancy. Interest reserve or earnout structure required.`
- `[INFO] Estimated time to stabilization: 6 months at 10 units/month absorption.`
- `[INFO] Year 1 NOI shortfall vs. stabilized: $297,600. Budget this as carry cost in equity.`

---

### Edge Case 8: Below-Market Leases (Loss-to-Lease)

**Description:** Existing tenants are paying rents significantly below current market rates. This is the "loss-to-lease" -- the gap between what tenants pay and what the market would bear. Leases turn over at different times, so the income lift is gradual, not immediate.

**Why it matters:** Loss-to-lease represents embedded upside but it is not immediately accessible. Models must reflect the phased timing of rent increases as leases expire and renew. Overstating the speed of rent convergence inflates near-term returns; understating it misses real value.

**How to handle it in the model:**
1. Calculate total loss-to-lease as the difference between in-place rents and market rents, aggregated across all units.
2. Obtain the lease expiration schedule (or assume even distribution if unavailable).
3. Model rent increases at each lease expiration: new rent = market rent (or market minus a retention discount of 3-5%).
4. Apply a renewal rate assumption (typically 50-60% of tenants renew; non-renewals incur turnover cost + vacancy).
5. Build a month-by-month or quarter-by-quarter rent convergence schedule.

**Example calculation snippet:**

```
Parkview loss-to-lease analysis:

  200 units, average in-place rent: $1,600/month
  Market rent: $1,750/month
  Loss-to-lease per unit: $150/month
  Total monthly loss-to-lease: 200 x $150 = $30,000/month
  Annual loss-to-lease: $360,000
  Loss-to-lease as % of market rent: $150 / $1,750 = 8.6%

Interpretation: 8.6% falls in the 5-10% "moderate upside" range.

Lease expiration schedule (assumed even distribution):
  Leases expiring per quarter: 200 / 4 = 50 units/quarter
  (In practice, pull actual expiration dates from the rent roll.)

Rent convergence model:
  - Upon renewal/re-lease: rent moves to $1,750 (market)
  - Retention discount for renewals: 3% --> renewal rent = $1,698
  - Renewal rate: 55% renew, 45% turn over
  - Turnover cost: $2,000/unit; vacancy loss: 1 month

Quarter-by-quarter rent capture:

| Quarter | Units Expiring | Renewals (55%) | New Leases (45%) | Avg New Rent | Incremental Monthly Revenue |
|---------|---------------|----------------|-----------------|-------------|---------------------------|
| Q1      | 50            | 28 @ $1,698    | 22 @ $1,750     | $1,721      | 50 x ($1,721 - $1,600) = $6,050 |
| Q2      | 50            | 28 @ $1,698    | 22 @ $1,750     | $1,721      | $6,050                    |
| Q3      | 50            | 28 @ $1,698    | 22 @ $1,750     | $1,721      | $6,050                    |
| Q4      | 50            | 28 @ $1,698    | 22 @ $1,750     | $1,721      | $6,050                    |

Cumulative monthly revenue increase after full year: $24,200/month
Annualized revenue increase: $24,200 x 12 = $290,400
Capture rate: $290,400 / $360,000 = 80.7% of total loss-to-lease captured in Year 1

Remaining loss-to-lease after Year 1: $360,000 - $290,400 = $69,600
  (From renewals priced at $1,698 vs. $1,750 market)

NOI impact:
  Incremental revenue (Year 1): $290,400
  Less: turnover costs (90 units x $2,000): -$180,000
  Less: vacancy loss (90 units x 1 month x $1,750): -$157,500
  Net NOI impact (Year 1): -$47,100 (turnover drag exceeds partial-year rent gain)
  Net NOI impact (Year 2+, steady state): +$290,400 (no additional turnover drag)
```

**What to flag in output:**
- `[INFO] Loss-to-lease: 8.6% ($360,000/year). Moderate value-add opportunity through organic lease turnover.`
- `[INFO] Full rent convergence requires 12 months assuming even lease expirations.`
- `[WARNING] Year 1 net NOI impact is negative (-$47,100) due to turnover costs and vacancy during re-leasing. Upside is realized in Year 2+.`
- `[INFO] Renewal retention discount (3%) leaves $69,600 residual loss-to-lease after Year 1. Full market rents achieved only through tenant turnover.`