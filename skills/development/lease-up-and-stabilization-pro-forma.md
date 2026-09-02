---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Lease-Up and Stabilization Pro Forma

Model the interval between first delivery and stabilization: absorption pace, pre-leasing, concessions and their burn-off, operating shortfall and interest carry, breakeven and stabilization dates, stabilized NOI, and whether the takeout repays the construction loan.

This is educational decision support, not legal, tax, investment, accounting, or financing advice. Every absorption, rent, concession, and cap rate figure referenced here is directional as of its stated date and must be re-validated against current submarket evidence and live lender feedback.

---

## When to Use This Skill

Use this skill once a project has a credible delivery date and needs the period after it modeled: at investment committee, at construction loan submission, when a takeout lender or buyer asks for the stabilization case, when leasing is running behind the underwriting and the interest reserve is draining, or when a construction loan maturity is approaching and the exit has to be tested. It covers ground-up and heavy redevelopment across multifamily, industrial, retail, office, and mixed-use. Post-stabilization operations belong to the sector packs and to the asset-management skills, notably [Lease-Up & Concessions Analyst](skills/asset-management/lease-up-concessions-analyst.md) for ongoing concession management, [Annual Operating Budget Builder](skills/asset-management/annual-operating-budget-builder.md) for the first stabilized budget, and [Hold/Sell/Refi Analyst](skills/asset-management/hold-sell-refi-analyst.md) for the post-stabilization exit decision. This skill hands off at stabilization; it does not restate stabilized operating practice.

---

## What You'll Need to Provide

- Delivery schedule: first certificate of occupancy or first unit or bay delivery, phased delivery by building or floor, and construction completion date
- Unit mix or space plan: units by type, bays and clear height, suites and floor plates, gross and net rentable area
- Pre-leasing evidence: signed leases, LOIs, build-to-suit or pre-sold commitments, with commencement dates and rent
- Market rent evidence: dated submarket comps at the subject's quality and vintage, with face rent and net effective rent shown separately
- Concession evidence: what competing projects in initial occupancy are offering, in months free or dollars, and whether abated or paid up front
- Absorption evidence: leasing velocity at comparable new deliveries in the same submarket, plus the delivery pipeline competing for the same demand
- Operating expense build for the lease-up period, including marketing, leasing staff, commissions, and pre-opening costs
- Construction loan terms: balance and remaining commitment, rate and index, maturity, extension options and their tests, interest reserve balance, carry reserve or carry guaranty
- Takeout assumptions: permanent lender or buyer, sizing tests, rate, term, amortization, and any occupancy, DSCR, or debt yield condition; or the sale case with an exit cap rate and closing costs
- Equity structure: remaining unfunded equity, preferred return accrual, distribution waterfall, and the business question (IC approval, lender submission, extension request, refinance versus sale, or a rebudget after a leasing miss)

---

## Mission

Produce a month-by-month path from first delivery to stabilization that a construction lender, a takeout lender, and an equity partner can all underwrite: how fast space leases, what it costs to get there, when the project covers its own debt service, what NOI it stabilizes at after concessions burn off, and whether the exit clears the loan.

---

## Strategy

### Step 1: Fix the Definitions and the Timeline Before Any Curve

Nothing downstream is comparable until these are written down.

- **Name the stabilization test.** The three public conventions are not interchangeable: AvalonBay uses "the earlier of (i) attainment of 90% or greater physical occupancy or (ii) the one-year anniversary of completion of development"; Camden "generally consider[s] a property stabilized once it reaches 90% occupancy" with no time backstop; Prologis reports properties as "pre-stabilized" and computes stabilized yield as estimated NOI assuming stabilized occupancy divided by total expected investment (FY2025 Forms 10-K). A one-year backstop caps the measured interval whether or not leasing cooperates. State which test you are using and never compare a date or a yield across sponsors without reconciling it.
- **Report the cash-flow milestone separately.** HUD defines sustaining occupancy as the occupancy at which monthly rents cover all operating expenses plus monthly debt service, which the MAP Guide states "is equivalent to a debt service coverage ratio (DSCR) of 1.0, a ratio also referred to as 'breakeven'" (HUD MAP Guide, revision March 19, 2021). The debt cares about that date, not about a percent-leased milestone.
- **Set the clock at first delivery, not at completion.** HUD measures the absorption period "from delivery of the first units." Across AvalonBay's 24 communities under construction at December 31, 2025, initial occupancy preceded estimated completion by a median of 3 quarters (range 0 to 8). A model that starts leasing at completion understates both the revenue ramp and the shortfall period.
- **Use the appraisal basis the lender will use.** Per the OCC, an as-complete value fits a preleased or owner-occupied building; an as-stabilized value is appropriate for "a property to be constructed that is not preleased to stabilized levels," and stabilized occupancy is "the occupancy level that a property is expected to achieve after the property is exposed to the market for lease-up over a reasonable period of time and at comparable terms and conditions to other similar properties" (OCC, *Comptroller's Handbook: Commercial Real Estate Lending*, Version 2.0).
- **Lay out the calendar in months**: first delivery, each phase delivery, construction completion, certificate of occupancy by building, breakeven month, stabilization month, construction loan maturity and each extension outside date, and the takeout funding date. Pull the delivery dates from [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md) rather than assuming them.

### Step 2: Build the Absorption Curve From Evidence, Not From a Straight Line

- **Define the pace metric.** HUD: "The Absorption Rate is the average number of units rented each month during the absorption period." For non-residential, use square feet or suites leased per month, and track signed versus commenced separately.
- **Start with pre-leasing.** Signed leases with commencement dates come out of the absorption curve entirely and go into the revenue schedule at their own dates. Pre-leasing also changes the valuation basis and the takeout condition, not just the ramp. Industrial reference point, dated: Prologis reported its consolidated development portfolio 53.5% leased at December 31, 2025 across 77 properties with $5.1 billion of total expected investment, with build-to-suit at 60.9% of 2025 development starts by TEI, up from 28.6% in 2024 (FY2025 Form 10-K).
- **Shape the curve.** Use a slow first two to three months while the leasing office ramps, a steeper middle, and a long tail through the last 10 percentage points of occupancy, which is where most pro formas are wrong. Do not model a constant units-per-month line to 95%.
- **Sanity-check the duration against dated evidence.** Institutional multifamily reference points: Camden's three FY2025 actual stabilizations ran 3 to 4 quarters from construction completion under a pure 90% test, while its current pipeline forecasts run 4 to 7 quarters, and Camden Village District (369 homes, Raleigh, NC) completed in 3Q25 was 60% leased at January 31, 2026 with stabilization estimated for 1Q27. Across AvalonBay's pipeline the interval from initial occupancy to stabilized operations ran a median of 6 quarters (range 3 to 10) under a definition that truncates the tail. A curve faster than the same sponsor's own recent forecasts needs an argument.
- **Apply the program ceiling as a screen.** HUD requires that the absorption period used to estimate market demand "should not exceed 18 months from delivery of the first units," a limit reduced from 24 months, with exceptions for large high-rise buildings requiring a larger initial operating deposit. That is FHA program policy, not a universal market rule, but a conventional deal underwritten past 18 months should carry a bigger reserve for the same reason.
- **Check the competitive set, not the national number.** National aggregates say which way supply leans, nothing more. Directional and dated: CBRE reported Q2 2026 multifamily net absorption of 167,000 units against completions of 77,700 units with 4.3% vacancy, and Q2 2026 industrial net absorption of 85.1 million sq ft against completions of 47.9 million sq ft with 6.5% vacancy and 252.2 million sq ft under construction (both published July 29, 2026). JLL reported over 30 million sq ft of trailing-twelve-month office occupancy gains with vacancy down 60 bps quarter over quarter (July 27, 2026). Cushman & Wakefield reported Q2 2026 shopping center absorption of 708,000 sq ft, 6.0% vacancy, and 2.3 million sq ft delivered (July 14, 2026). Replace all of these with submarket delivery counts inside the subject's own trade area before underwriting.

### Step 3: Price the Rent Twice, Face and Net Effective

- **Build both rent lines.** Face rent drives the rent roll and most lender rent comparisons; net effective rent drives value. Show them side by side by unit type or space type, with the concession assumption stated in months and in dollars.
- **Model concession burn-off on the accounting basis, not the cash basis.** AvalonBay states the mechanic: "We amortize concessions on a straight-line basis over the life of the respective leases (generally one year), reducing the income recognized over the lease term," and disclosed same-store concessions granted rising $6,976,000 to $24,198,000 in 2025 with an unamortized balance of $13,025,000 at year end (FY2025 Form 10-K). A concession granted in lease-up month 4 keeps suppressing recognized revenue into the following year, so physical and economic stabilization are different months whenever concessions are running. Carry the unamortized balance explicitly, show the month it reaches zero, and report both dates.
- **Interrogate comp rents for hidden concessions.** HUD's market study standard requires the analyst to report "the extent of rent concessions or similar incentives, particularly in projects in initial occupancy," and to address "whether the quoted rents are overstated due to concessions or other factors." The OCC's collateral-assessment list names "effective rental rates or sale prices, considering sales and financing concessions." There is no defensible national concession benchmark; use dated submarket evidence and say where it came from.
- **Commercial space carries its own drag.** First-generation tenant improvements, leasing commissions, and free rent belong in the capital and shortfall schedules, not netted into rent.

### Step 4: Size the Operating Shortfall and the Interest Carry

Build the shortfall month by month. HUD's three-interval structure is the cleanest available model because it separates what is already inside the construction loan from what is not (MAP Guide, revision March 19, 2021):

| Interval | Span | What gets charged |
|---|---|---|
| 1 (optional) | Certificate of occupancy to end of the construction period and cost certification (construction time plus two months) | Operating and leasing expenses only. No debt service, because construction-period interest already sits in the loan. No replacement reserves or ground rent |
| 2 (optional) | End of the construction period to the start of principal amortization, no more than two months | Operating expenses plus interest (and MIP on an FHA deal), no amortization. Ground rent if leasehold. No replacement reserves |
| 3 | From the start of amortization | Operating expenses plus fully amortizing debt service, plus ground rent and replacement reserves |

Rules that travel with it:

- **Do not double-count interest.** Construction-period interest funded through the loan is already in total development cost from [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md). What belongs here is the interest accruing after the construction interest line ends and before the takeout funds, including any gap between construction completion and the start of amortization. HUD requires amortization to begin no later than four months after construction completion for insurance of advances, and expressly directs that the unaccounted interest in that gap be added to the Initial Operating Deficit.
- **Size the reserve to lease-up, not to completion.** The OCC states that an appropriate interest reserve "provides sufficient funds to pay interest through the project's anticipated completion and lease-up, sale, or occupancy," judged against "the reasonableness of the development assumptions, including potential changes in interest rates, the timing of expected disbursements and pay downs, and the time required for the completion and sale or lease-up of the project." It is a budget line, not coverage: the OCC is explicit that "the presence of an interest reserve may not accurately reflect a borrower's ability to pay." Compute the shortfall independently, then compare it to what is funded.
- **Apply cash flow first.** Per the OCC, "during the lease-up period, any cash flow from the project is ordinarily applied to pay interest before interest reserves are applied. Once the cash flow is sufficient to cover the interest, no further draws on the reserve should be permitted."
- **Separate operating carry from interest carry.** A carry reserve or carry guaranty covering operating expenses, taxes, insurance, and utilities is a different instrument from the interest reserve. Confirm which the loan documents actually provide, using [Construction Lending Criteria](knowledge/construction-lending-criteria.md).
- **Output the peak cumulative shortfall and the month it occurs.** That number, not the total, is the equity call the sponsor has to be able to fund. Reconcile remaining loan availability against cost to complete with [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md), and check whether unresolved change orders from [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md) will consume the same dollars.

### Step 5: Compute the Milestones and the Stabilized NOI

Use the formula conventions in [Underwriting Calculations](knowledge/underwriting-calc.md) for GPI, EGI, NOI, DSCR, debt yield, and cap-rate valuation, plus these lease-up-specific tests:

| Milestone | Definition | Decision rule |
|---|---|---|
| Breakeven / sustaining occupancy | Occupancy at which collections cover operating expenses plus full monthly debt service; DSCR = 1.0 (HUD) | Compute as (operating expenses + debt service) / (achievable gross potential rent net of concessions, plus other income). Report the occupancy percentage and the calendar month |
| Sustained breakeven | Breakeven held for consecutive months | HUD's standard for new construction and substantial rehabilitation is 6 consecutive months. Use it as the test for guaranty burn-off and extension conditions unless the loan says otherwise |
| Physical stabilization | The named occupancy test, typically 90% or 95% | State the test and the month |
| Economic stabilization | The first month with a full stabilized rent roll, no unamortized concession drag, and normalized operating expenses | Usually later than physical stabilization. This is the NOI that belongs in the exit value |
| Stabilized NOI | Trailing-3 or trailing-12 annualized NOI at economic stabilization | Say which convention, and whether a takeout lender will accept an annualized trailing-3 |
| Stabilized yield on cost | Stabilized NOI / total development cost | Prologis convention: estimated NOI assuming stabilized occupancy divided by total expected investment. Reconcile the denominator to the budget skill so the two do not diverge |

Reference point, directional and dated: Prologis reported a 6.7% weighted average stabilized yield and a 25.4% estimated weighted average margin on its 40 buildings stabilized in 2025 (11 million sq ft, $2,271 million TEI), against 6.2% and 19.2% in 2024 (FY2025 Form 10-K). Lease-up assets contribute almost nothing until they get there: Camden's development and lease-up communities, 1,531 homes, contributed $2.2 million of property revenue and $0.7 million of NOI in FY2025 against $1.01 billion of total portfolio NOI, while its stabilized properties ran roughly 95% weighted average occupancy (FY2025 Form 10-K). Those homes were delivering during the year, so that is not a full-year run rate; it is a reminder of the size of the hole.

### Step 6: Test the Takeout Against the Construction Loan Payoff

- **Size the takeout with all the tests and take the lowest.** LTV on as-stabilized value, LTC, DSCR at stabilized NOI, and debt yield at stabilized NOI, per [Construction Lending Criteria](knowledge/construction-lending-criteria.md). Sizing mechanics belong to [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md); what this skill adds is the date and the NOI those tests are run on. Where an FHA execution is contemplated, HUD Mortgagee Letter 2025-03 (January 8, 2025) sets the loan as the lesser of the requested amount, statutory limits, the DSCR-supportable amount, and the ratio-supportable amount, at 87% LTV/LTC and 1.15x DSCR with a 7% vacancy factor for market rate, 90% and 1.11x with 5% for LIHTC with a rent advantage, and 90% and 1.11x with 3% for properties with 90% or greater rental assistance.
- **Compute the payoff gap.** Construction loan balance at the takeout date, plus accrued interest, exit and prepayment fees, unreleased retainage, and any out-of-balance funding, less takeout proceeds. If the gap is positive, name who funds it and from where.
- **Do not assume the takeout funds.** The OCC: take-out commitments are "usually conditioned on ... lease-up to break even or better with leases at minimum rental rates," a forward commitment obligates the permanent lender only "upon future completion and, almost always, lease-up," and "underwriting would ordinarily include analysis of the risk should the take-out commitment not be funded." Distinguish a forward commitment from a standby, and check whether the loan is limited to the floor of a commitment predicated on achieving stated rents or occupancy. The FDIC's validity tests are mechanical: counsel review of the agreement, review of the permanent lender's financial statements to assess capacity, a tri-party buy and sell agreement completed before the construction loan closes, and an automatic completion-date extension clause for delays beyond the builder's control.
- **Check tenor and extensions against the curve.** The OCC: the appropriate tenor is based on "the time needed for construction and stabilization or sale," a construction facility may convert "to bridge financing for the expected stabilization period," bridge loans run "up to three years," and extension option length "should be consistent with the expected construction time plus the projected absorption period." Flag any extension test the modeled curve fails, and give the month it fails.
- **Model the sale exit in parallel.** Value at economic stabilization using a submarket, quality-matched, dated exit cap rate, net of closing costs and taxes, and never at a cap tighter than the current going-in cap without a written argument.
- **Note the debt environment, dated.** The Federal Reserve's July 2026 Senior Loan Officer Opinion Survey reported Q2 2026 construction and land development standards "remained basically unchanged on net" with a moderate net share of banks reporting weaker CLD demand, and modest to moderate net shares easing standards for multifamily and nonfarm nonresidential. Fannie Mae's Multifamily Guide carries a "Near Stabilized Property Submissions" update (Guide Update 26-18, dated July 20, 2026), so an agency path short of full stabilization exists; its terms are quote-driven and must be confirmed with the lender.

### Step 7: Stress the Curve and Time the Equity

Run each case independently, then the downside combination, and recompute rather than interpolating:

- **Slower absorption**: lease-up extended 3, 6, and 12 months. Report the incremental shortfall, the new breakeven and stabilization months, whether the interest reserve survives, and whether the construction loan matures first.
- **Deeper concessions**: one and two additional months free, held for the full lease-up. Report the effect on net effective rent, on economic stabilization, and on takeout proceeds through DSCR and debt yield.
- **Lower achieved rent**: face rent 5% and 10% below underwriting, expenses held flat.
- **Higher rate and wider cap at exit**: +100 and +200 bps on the permanent rate, which cuts proceeds through DSCR before it touches LTV; and the current going-in cap, +50 bps, and +100 bps for both the refinance LTV test and the sale case.
- **Compute the break-even leasing pace**: the units or square feet per month below which the interest reserve depletes before the takeout can fund, and the month that happens.
- **Time the equity.** Show the remaining unfunded equity, the peak shortfall draw, the preferred return accruing through lease-up, the first month of distributable cash flow, and the return of capital at refinance or sale. A delay in stabilization moves every one of those dates, and the preferred return compounds through the whole delay.

Then write one verdict, the two or three findings that drive it, the dollar amounts of any gap, and the conditions that would change the answer. Feed the result into [Development IC Memo Writer](skills/development/development-ic-memo-writer.md), and reconcile the total development cost denominator back to [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md). Where site or entitlement conditions constrain phasing or occupancy, check them against [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md).

---

## Output Format

```markdown
# Lease-Up and Stabilization Pro Forma
## Project / Product Type / Units or NRSF:
## First Delivery / Completion / Loan Maturity:
## Stabilization Definition Used:
## Verdict: STABILIZES AND CLEARS TAKEOUT | STABILIZES WITH FUNDING GAP | LEASE-UP NOT SUPPORTED BY EVIDENCE | MATURITY RISK

### Absorption Assumptions
| Input | Value | Evidence / Source and Date |
|---|---|---|
| Pre-leased at delivery (units or SF, %) | | |
| Absorption rate (units or SF per month) and period from first delivery (months) | | |
| Face rent at stabilization / concession (months free or $) / net effective rent | | |
| Stabilized occupancy assumption | | |

### Lease-Up Schedule
| Month | Units/SF Delivered | Cumulative Leased | % Occupied | Face Revenue | Concession Amortization | Recognized Revenue | OpEx | NOI | Debt Service | Cash Shortfall | Cumulative Shortfall |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Milestones
| Milestone | Month | Occupancy | Note |
|---|---|---|---|
| First delivery | | | |
| Construction completion | | | |
| Breakeven (DSCR 1.0) | | | |
| Breakeven sustained 6 months | | | |
| Physical stabilization | | | |
| Economic stabilization (concessions burned off) | | | |
| Construction loan maturity (incl. extensions) | | | |

### Shortfall and Carry
| Item | Amount | Funded By | Sufficient? |
|---|---|---|---|
| Post-completion interest carry | | Interest reserve / equity / guaranty | |
| Operating deficit | | Carry reserve / equity | |
| First-generation TI and LC | | | |
| Peak cumulative shortfall (month: ___) | | | |
| Remaining unfunded equity | | | |

### Stabilized Result and Takeout
| Metric | Value | Basis |
|---|---|---|
| Stabilized NOI (economic) | | Trailing-3 annualized / trailing-12 |
| Stabilized yield on cost | | TDC denominator: |
| As-stabilized value | | Exit cap and comp source/date: |
| Takeout sized by LTV | | |
| Takeout sized by LTC | | |
| Takeout sized by DSCR | | Rate / amortization / DSCR test: |
| Takeout sized by debt yield | | |
| **Controlling takeout proceeds** | | Binding test: |
| Construction loan payoff (balance + interest + fees + retainage) | | |
| **Gap or surplus** | | Funded by: |
| Takeout type | Forward / standby / assumed / none | Conditions: |

### Sensitivity
| Case | Stabilization Month | Peak Shortfall | Stabilized NOI | Takeout Proceeds | Gap |
|---|---|---|---|---|---|
| Base | | | | | |
| Lease-up +3 / +6 / +12 months | | | | | |
| Concessions +1 / +2 months | | | | | |
| Rent -5% / -10% | | | | | |
| Takeout rate +100 bps | | | | | |
| Exit cap +50 / +100 bps | | | | | |
| Downside combination | | | | | |

Break-even leasing pace (reserve depletes before takeout): ___ per month, failing in month ___

### Equity Timing
- Last equity contribution (month, amount):
- Preferred return accrued through stabilization:
- First distributable cash flow (month):
- Return of capital at refinance or sale (month, amount):

### Issues and Next Steps
| Issue | Severity | Why It Matters | Next Step |
|---|---|---|---|

### Assumptions Requiring Validation
- Absorption, concession, rent, and exit cap comps: source and date for each
- Takeout terms: indicative / committed / assumed

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The stabilization test is named before any date, occupancy, or yield is reported
- The absorption clock starts at first delivery, not at construction completion, and phased deliveries are modeled separately
- Signed pre-leases are removed from the absorption curve and entered at their own commencement dates
- Face rent and net effective rent are both shown, with the concession assumption stated in months and dollars, and the unamortized concession balance carried to its burn-off month
- Breakeven (DSCR 1.0), physical stabilization, and economic stabilization are three separately reported months
- Construction-period interest already inside the loan is not double-counted in the shortfall
- The shortfall is computed independently of the funded reserve balance, then compared to it, and project cash flow is applied to interest before any reserve draw
- Peak cumulative shortfall and its month are stated, not just the total
- Takeout proceeds are the minimum of the LTV, LTC, DSCR, and debt yield results, with the binding test named, and the payoff includes accrued interest, exit and prepayment fees, and unreleased retainage
- A takeout-does-not-fund case is modeled
- The construction loan maturity, including extension outside dates, is plotted against the modeled stabilization month
- The exit cap rate is submarket-specific, quality-matched, dated, and not tighter than the current going-in cap without a written argument
- Every sensitivity case is recomputed, not interpolated

---

## Red Flags & Dealbreakers

- Absorption modeled as a straight line, or faster than the sponsor's own recent comparable projects, or faster than demonstrated submarket velocity at the subject's rent level
- Absorption underwritten from national aggregates instead of submarket delivery concentration in the subject's competitive set
- Rents underwritten at face value while competing projects in initial occupancy are offering concessions
- Stabilized NOI declared on the physical-occupancy date with an unamortized concession balance still running
- Interest reserve sized to construction completion rather than through lease-up, sale, or occupancy, or draws continuing after project cash flow covers interest
- A depleted reserve replenished with new loan proceeds rather than borrower or guarantor cash, which the OCC calls a red flag indicating possible credit deterioration
- No separate carry reserve or carry guaranty for operating expenses, taxes, and insurance during lease-up
- Construction loan maturity, or the last extension outside date, falling before the modeled stabilization month, or an extension test that depends on a leasing pace the market is not delivering with no fallback capital
- A takeout treated as certain when it is a standby, is conditioned on rents or occupancy the project has not reached, or has no tri-party buy and sell agreement
- Takeout proceeds sized on trended or stabilized rents while the in-place rent roll fails the DSCR or debt yield test at funding
- Exit cap rate tighter than the current going-in cap, or a refinance case requiring both rate compression and cap compression
- First-generation TI, leasing commissions, and free rent on commercial space netted into rent instead of funded as capital
- Preferred return accruing through an extended lease-up with no updated equity waterfall
- A single blended absorption curve across phases that hides a first phase which never reaches breakeven

---

## When Data is Missing

- If no submarket absorption comps exist, do not invent a pace. Run the model at three explicit paces, label them fast, base, and slow, and present the slow case as the working answer
- If concession evidence is missing, model one month free and two months free as bracketing cases rather than assuming zero; a lease-up with no concessions is an assertion that needs evidence
- If pre-leasing is unsigned, treat LOIs as unleased and show separately what signing them would do to the curve and the takeout
- If takeout terms are indicative rather than committed, size proceeds across a rate and DSCR band and report the range, not a point estimate
- If no exit cap comparable exists, present value across a plausible cap band and state that the takeout LTV test is unresolved
- If the operating expense build for lease-up is missing, do not scale a stabilized expense ratio down; lease-up carries marketing, leasing staff, and commissions that stabilized operations do not
- If the interest reserve balance is unknown, compute the required carry anyway and state the shortfall as an unfunded requirement
- If the construction loan documents are unavailable, do not assume extension options exist; model the stated maturity as hard
- Never fill a missing input with a rule of thumb; show the line as unresolved and quantify what value would break the deal

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Dated submarket absorption and concession comps at the subject's quality, meaningful signed pre-leasing, a firm delivery schedule, a committed takeout with written conditions, and a construction loan document set confirming reserve balances and extension tests |
| MEDIUM | Credible but partly unsupported absorption and rent assumptions, LOIs rather than signed leases, a planned delivery schedule, indicative takeout terms, and known reserve balances |
| LOW | Sponsor-supplied lease-up curve with no comp support, no concession evidence, an unfixed delivery date, or an assumed takeout; treat every date, NOI, and proceeds figure as directional only |

---

## Related Knowledge Bases

- [Development Benchmarks](knowledge/development-benchmarks.md)
- [Construction Lending Criteria](knowledge/construction-lending-criteria.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Lease-Up and Stabilization Pro Forma Research](research/development/lease-up-and-stabilization-pro-forma-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
