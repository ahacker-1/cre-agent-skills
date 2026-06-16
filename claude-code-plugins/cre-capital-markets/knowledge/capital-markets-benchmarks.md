# Capital Markets Benchmarks

Reference guide for sizing CRE debt, diagnosing refinance gaps, and comparing lender or capital-stack alternatives.

---

## Core Debt Metrics

| Metric | Formula | Use |
|---|---|---|
| Loan-to-Value (LTV) | Loan Amount / As-Is Value | Caps leverage against value |
| Loan-to-Cost (LTC) | Loan Amount / Total Project Cost | Caps leverage for acquisitions, development, or major capex |
| Debt Service Coverage Ratio (DSCR) | NOI / Annual Debt Service | Tests cash-flow coverage |
| Debt Yield | NOI / Loan Amount | Tests lender basis independent of interest rate and cap rate |
| Debt Constant | Annual Debt Service / Loan Amount | Converts loan amount into annual debt service burden |
| Refinance Proceeds Gap | Existing Payoff - Supportable New Loan Proceeds | Quantifies paydown or rescue-capital need |
| Interest-Only Coverage | NOI / Annual Interest Expense | Tests early-period cash flow before amortization |
| Break-Even Occupancy | (Operating Expenses + Debt Service) / Gross Potential Income | Shows occupancy needed to cover debt |

Use in-place NOI, trailing NOI, and stabilized NOI separately. Never size a refinance only on stabilized NOI unless the lender structure explicitly supports a future-funding or earnout path.

---

## Sizing Hierarchy

For any refinance, recap, acquisition debt, or rescue-capital analysis, calculate supportable proceeds under each test and use the lowest credible result as the controlling proceeds estimate.

1. DSCR proceeds
2. Debt-yield proceeds
3. LTV proceeds
4. LTC proceeds, if acquisition, capex, or redevelopment
5. Loan-per-unit, loan-per-key, or loan-per-square-foot sanity check
6. Sponsor liquidity and reserve requirement
7. Lender appetite and property-type overlay

The controlling test should be named explicitly. If multiple tests bind, show all.

---

## Benchmark Ranges

These are directional screening ranges, not quotes.

| Situation | DSCR Guide | Debt Yield Guide | LTV Guide | Notes |
|---|---:|---:|---:|---|
| Stabilized multifamily | 1.20x-1.35x | 7.0%-9.0% | 55%-70% | Agency execution may use different constraints |
| Stabilized industrial | 1.20x-1.35x | 8.0%-10.0% | 55%-65% | Tenant quality and WALT matter |
| Stabilized retail | 1.25x-1.45x | 9.0%-11.0% | 50%-65% | Grocery and necessity retail may price better |
| Stabilized office | 1.30x-1.60x | 10.0%-13.0% | 45%-60% | Quality, rollover, and tenant credit dominate |
| Transitional / bridge | 1.00x-1.25x in-place plus takeout proof | 9.0%-13.0% | 45%-65% | Structure and reserves matter more than headline leverage |
| Distressed / rescue | Case-specific | 12.0%+ often screened | 30%-55% | Fresh-money basis, control rights, and exit path dominate |

If a live quote conflicts with these ranges, the quote controls. Document the live quote source and date.

---

## Refinance Gap Waterfall

Calculate the gap in this order:

1. Existing payoff, including accrued interest, default interest, exit fees, yield maintenance, prepayment premium, legal fees, and reserves to be replenished
2. Supportable new senior loan by the sizing hierarchy
3. Required paydown = payoff - new senior loan
4. Required reserves for taxes, insurance, capex, TI/LC, debt service, operating deficits, or carry
5. Transaction costs and lender deposits
6. Total gap = paydown + reserves + costs
7. Funding sources = sponsor equity + new JV equity + preferred equity + mezzanine + note purchase discount + asset sale proceeds
8. Residual gap after all sources

Do not present a refinance as solved if the paydown is covered but the reserve and carry need is not.

---

## Capital Stack Alternatives

| Alternative | Best Fit | Key Constraint |
|---|---|---|
| Senior refinance | Stabilized or near-stabilized asset | DSCR, debt yield, LTV, rollover |
| Senior extension | Sound asset with near-term timing issue | Lender consent, paydown, fees, maturity tests |
| Bridge debt | Transitional asset with credible takeout | Interest reserve, capex/leasing budget, exit |
| Mezzanine debt | Strong senior lender consent path and equity value | Intercreditor agreement, remedies, current-pay burden |
| Preferred equity | Need capital behind senior debt with flexible economics | Governance rights, dilution, redemption, recognition agreement |
| Common JV equity | Large gap or reset basis | Sponsor dilution and control |
| Note sale / discounted payoff | Lender wants exit and borrower has capital | Price discovery, release terms, tax effects |
| Asset sale | Refinance not viable or ownership cannot fund gap | Timing, value, broker process, lender cooperation |

---

## Required Inputs Checklist

- Existing loan payoff letter or loan statement
- Maturity date and extension options
- Interest rate, amortization, IO period, reserves, covenants, fees
- Current NOI, T-12, budget, and rent roll
- In-place and stabilized pro forma
- Current valuation support or broker opinion
- Leasing, capex, and carry budget
- Sponsor liquidity and willingness to contribute
- Lender type and servicing path
- Property type, market, tenancy, and risk narrative

---

## Red Flags

- Maturity is inside 180 days and no lender package is ready
- Existing payoff exceeds supportable proceeds and sponsor cannot fund paydown
- Refinance depends only on lower rates without NOI or value improvement
- DSCR, debt yield, and LTV all fail
- Major rollover occurs before or soon after proposed new maturity
- Existing lender requires paydown, reserves, or recourse the borrower has not modeled
- Rescue capital solves maturity but leaves no credible exit
- Proposed capital source requires consent that has not been confirmed

---

## Use With Skills

- Debt Maturity Diagnostic
- Refinance Proceeds Gap Analyzer
- Capital Stack Term Sheet Comparator
- Rescue Capital Comparator
- Recap IC Memo Writer
