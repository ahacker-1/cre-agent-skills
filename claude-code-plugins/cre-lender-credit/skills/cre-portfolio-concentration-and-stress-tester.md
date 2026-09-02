---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# CRE Portfolio Concentration and Stress Tester

Segment a U.S. CRE loan book, measure it against the supervisory concentration criteria, stress it under sensitivity and scenario tests, estimate rating migration and reserve pressure, and produce a board or ALCO-ready report with limits and actions.

---

## When to Use This Skill

Use this skill when someone has to answer a portfolio question rather than a loan question: are we concentrated, in what, how much of the book breaks if rates or values move, what happens at the maturity wall, and what do we tell the board. It fits the quarterly concentration package, the annual stress test, a limit-setting or policy refresh, capital planning, examination preparation, and the moment a fast-growing segment starts drawing attention. It is written for CRE portfolio managers, credit officers, credit analysts, loan review, and risk staff at U.S. banks and credit unions. It is educational decision support, not legal, tax, investment, accounting, regulatory, or financing advice; ratio construction, call report classification, allowance conclusions, and capital planning belong to your institution, its board, and its primary federal regulator.

---

## What You'll Need to Provide

- Loan-level extract: borrower and sponsor, property type and subtype, MSA, current balance and unfunded commitment, purpose, rate type and index, current rate, next reprice date, interest-only flag and IO expiration, amortization term, maturity date, extension options, recourse, owner-occupied flag, HVCRE flag, risk rating, and most recent NOI, DSCR, LTV, appraised value with effective date, and occupancy
- Capital and allowance: tier 1 capital, the allowance for credit losses attributed to loans and leases, total risk-based capital, risk-weighted assets, and the board's post-stress capital floor
- History: the CRE balance 36 months prior, risk-rating migration by segment and vintage, and net charge-off history by segment
- Policy: board-approved concentration limits and sublimits, coverage and leverage floors, interest-only and exception policy, the LTV exception basket balances, and the CRE strategy and growth plan
- Scenario inputs: the rate, value, cap-rate, vacancy, and NOI paths the board approved, with the source and date of each
- If any of this is unavailable, say so in the output rather than substituting an estimate. A missing 36-month prior balance means the growth test cannot be run, not that it passes.

---

## Mission

Turn a loan tape into a defensible portfolio view: where the book is concentrated and against which threshold, which segment breaks first and at what shock level, how much of the maturity ladder fails a refinance test, what the stressed ratings and allowance look like, and which limits, underwriting rules, pricing, or capital actions the results require.

---

## Strategy

### Step 1: Build the Denominator and the Numerators Before Any Ratio

Get the arithmetic right first, because both halves are definitional, not collateral-code driven.

- **Denominator.** For supervisory concentration measurement the agencies use tier 1 capital plus the allowance attributed to loans and leases (ALLL for institutions that have not adopted ASC 326), effective March 31, 2020, per the joint statement in OCC Bulletin 2020-29. That replaced the total risk-based capital referenced in the 2006 guidance footnotes. Where the bank used a CECL capital transition rule, subtract from tier 1 the ACL amount already counted in tier 1 so it is not double counted. Name the denominator on the face of every ratio.
- **CRE numerator.** The 2006 interagency guidance defines CRE as land development, construction, and other land loans, plus multifamily and nonfarm nonresidential loans where 50% or more of repayment comes from third-party, nonaffiliated rental income or from sale, refinancing, or permanent financing proceeds. Loans to REITs and unsecured loans to developers count when performance is closely linked to CRE markets. Loans repaid from the operations of the owner-occupant or its affiliate are excluded from the ratio, though not from risk analysis.
- **Construction numerator.** Construction, land development, and other land loans, reported separately. Reconcile the tape to the call report: list what you added (participations purchased, unsecured developer lines, REIT exposure) and what you removed (owner-occupied), and state whether unfunded commitments are in or out under board policy.

### Step 2: Segment the Book the Way the Guidance Names

Cut every dimension the 2006 guidance names, then cross-tab. Detail and definitions live in [CRE Concentration and Stress Testing](knowledge/cre-concentration-and-stress-testing.md).

| Dimension | Cut | Why it earns a line in the report |
|---|---|---|
| Property type and subtype | Office, retail, industrial, multifamily, hospitality, self-storage, special purpose, land | Correlated demand shocks |
| Geography | MSA, county, and submarket where data allows | Single-employer and supply shocks |
| Tenant, tenant industry, sponsor, developer | Top 10 each, plus loans to tenants | Hidden correlation between borrower and rent roll |
| Loan type and purpose | Construction, land, bridge, permanent, and the HVCRE bucket separately | ADC carries the heaviest testing expectation |
| Rate structure | Fixed, floating by index, floating with an in-the-money cap, cap expiry date | Sizes the rate shock |
| Amortization | Amortizing, IO with expiration date, IO-to-amortizing conversion in the horizon | Payment shock timing |
| Maturity ladder | 0-12, 13-24, 25-36 months, with and without extension options exercised | The live exposure |
| Owner-occupied vs investor | Both, reported separately | One is in the ratio, one is not |
| Risk rating, LTV band, DSCR band, policy exceptions | Full distribution | Feeds migration and finds the thin tail |

Cross-tab maturity against risk rating and property type. A book that looks diversified by property type can still be concentrated in one quarter of maturities. Stratification must be reasonable and supportable, and the guidance is explicit that the portfolio should not be divided into segments simply to avoid the appearance of concentration.

### Step 3: Measure Against Every Threshold That Applies

Report all of these, each with its own denominator stated. None of them is a lending limit.

- **Construction criterion.** Construction, land development, and other land at 100% or more of capital. No growth condition attaches.
- **Total CRE criterion.** Total CRE at 300% or more of capital **and** 50% or more growth over the prior 36 months. Both halves must be true; report the ratio and the growth rate separately so a board can see which one moved.
- **General concentration trigger.** The Comptroller's Handbook on Concentrations of Credit defines a concentration as direct, indirect, or contingent obligations exceeding 25% of tier 1 plus ALLL or ACL. Apply it to every segment; a single property type or MSA can be a reportable concentration long before the CRE ratio moves.
- **LTV exception baskets.** Under the Interagency Guidelines for Real Estate Lending, loans exceeding the supervisory LTV limits at origination should not exceed 100% of total capital in aggregate, and the commercial, agricultural, multifamily, and other non-1-4 family portion should not exceed 30% of total capital. The entire outstanding balance counts, not just the excess, and loans that conformed at origination and later fell out because value declined are not exceptions.
- **HVCRE.** Report the 150% risk-weighted HVCRE bucket separately from construction and land development; they overlap but are not the same set. Confirm the 15% "as completed" contributed capital test and whether any exposure now qualifies for reclassification because construction is substantially complete and cash flow supports debt service under permanent-financing criteria.
- **Board limits and sublimits.** Where a broad pool limit exceeds 100% of capital, the handbook expects sublimits for material segments. Flag any pool with no sublimit.

Say plainly in the output that the 100% and 300% figures are screening indicators for further supervisory analysis, that they set no limit, and that being below them is not a safe harbor when other risk indicators are present.

### Step 4: Run Sensitivity First, Then Scenario

Sensitivity finds the breaking variable. Scenario sizes the capital impact. Both are expected; a sophisticated portfolio model is not. Use [Underwriting Calculations](knowledge/underwriting-calc.md) for DSCR, debt yield, LTV, and cap-rate math rather than restating it.

Move one variable at a time, across the shock variables named in the FDIC examination module, and report the level at which each segment breaks a policy floor:

| Sensitivity | How to run it | What it exposes |
|---|---|---|
| Rate shock | +100 / +200 / +300 bps applied at reprice date on floating balances, at maturity on fixed, honoring cap strikes and cap expiry | Coverage failure on floating and repricing loans |
| IO conversion | Recast every IO loan as-if amortizing on the bank's standard schedule, whether or not the IO period has ended | Payment shock the current DSCR hides |
| NOI decline | -5% / -10% / -20%, with and without expense relief | Coverage and debt yield compression |
| Vacancy and absorption | Occupancy decline by property type; slower lease-up on construction and transitional | NOI timing on ADC and lease-up |
| Value decline | Direct haircut to as-is value | LTV migration, guarantor reliance, loss given default |
| Cap-rate expansion | +50 / +100 / +150 bps applied to in-place NOI | Value loss independent of NOI, and the refinance gap |

Then build two or three coherent scenarios (base, adverse, severely adverse) that move rates, values, cap rates, vacancy, and NOI together with a stated narrative and horizon. Do both levels: transaction-level results rolled up bottom-up where loan-level data supports it, and a top-down stressed-loss-rate pass on thin-data segments, labeled as top-down. Focus the sample on vulnerable segments - low DSC, high LTV, single geography, property type, or industry - and confirm the sample reflects the pool.

Severity is a board decision. No regulator sets the shock size for an individual institution. Anchor it to the institution's own worst segment loss experience, current market data by MSA and property type, and the post-stress capital floor. The Federal Reserve's June 24, 2026 supervisory stress test used a 39% CRE price decline in its severely adverse scenario and projected roughly $75 billion of CRE losses across 32 large banks; that is a large-bank scenario and may be cited only as a labeled borrowed upper bound, not adopted. An undocumented shock size is itself a finding.

### Step 5: Run the Maturity Refinance Test

This is the test that separates a book that is current from a book that is safe. Borrowers who can make payments may still be unable to refinance a balloon when value has fallen.

For every loan maturing inside the horizon, including construction loans reaching completion and IO loans converting: project NOI at maturity under each scenario; re-size proceeds at a stressed constant and stressed exit cap rate as the lesser of stressed LTV, stressed DSCR tested as-if amortizing, and stressed debt yield; compute the gap to the projected balance after amortization; then bucket the ladder into refinances cleanly, refinances with a paydown of stated size, needs restructure, or no exit. Run the ladder both with and without extension options exercised, and separately without any sale or securitization assumption. Portfolio liquidity is a mitigant the 2006 guidance recognizes, but a plan that depends on selling into the same stress that closes those markets is not one.

Loans with no exit go to [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md). Loans with a paydown gap and a willing sponsor go to [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md) for tracking, and the sponsor's ability to fund the gap is sized in [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md).

### Step 6: Estimate Rating Migration and Reserve Pressure

Management reporting is expected to show changes in the portfolio's risk profile including risk-rating migrations. That is the bridge from a stress number to a classification and allowance conversation.

- Map each stressed loan against the interagency criteria in [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md): a well-defined weakness jeopardizing liquidation of the debt is the substandard threshold; potential weaknesses deserving close attention are special mention.
- Project criticized and classified balances by segment under each scenario using the institution's own historical migration by segment and vintage. No regulator publishes a stressed migration matrix, so that history is the only defensible input; say so if you had to substitute judgment.
- Translate migration into reserve pressure under ASC 326: which segments would change risk characteristics, which qualitative factors and reasonable-and-supportable forecasts the scenario implies, where a collateral-dependent measurement would take over, and the provision and earnings effect.
- Run the post-stress capital math (capital less stressed losses net of pre-provision earnings, over stressed risk-weighted assets) against the board floor, and flag any scenario that breaches it.
- Label all of this as planning output. A projected downgrade is not a rating action, and a performing loan is not adversely classified solely because collateral value fell below the balance. Actual downgrades run through [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md).

### Step 7: Convert Results Into Limits and Actions

Examiners ask whether the results were used. FDIC examination procedures list the destinations by name, and a report that ends at a number is an incomplete report.

For each failing segment, name the specific change: slow or redirect origination; tighten or add a board-approved sublimit; raise coverage, debt yield, or leverage floors; restrict interest-only; reprice; tighten exception tolerance; add capital or reduce the concentration; adjust ACL qualitative factors; or build workout, appraisal review, and special assets capacity ahead of the migration. FDIC's December 2023 advisory pairs strong capital and appropriate allowances with close portfolio management, updated borrower financial information, bolstered workout infrastructure, and adequate liquidity with diverse funding. Note when the methodology was last independently validated; the absence of a validation is a finding on its own. New originations in a constrained segment feed back to [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md), and the portfolio position becomes a stated section in [Credit Memo Writer](skills/lender-credit/credit-memo-writer.md).

---

## Output Format

```markdown
# CRE Portfolio Concentration and Stress Report
## As of: | Denominator: Tier 1 + ACL = $
## Verdict: WITHIN APPETITE | ELEVATED - MONITOR | ACTION REQUIRED | LIMIT BREACH

### Concentration Position
| Measure | Balance | Ratio | Threshold | Status |
|---|---|---|---|---|
| Construction, land development and other land | | | 100% screening criterion | |
| Total CRE (guidance definition) | | | 300% screening criterion | |
| 36-month CRE growth | | | 50% growth condition | |
| HVCRE (150% risk weight) | | | Board sublimit | |
| LTV exception basket - total / commercial | | | 100% / 30% of total capital | |
| Largest segment vs 25% of Tier 1 + ACL | | | 25% general trigger | |

Screening criteria are supervisory indicators, not limits, and not a safe harbor.

### Segment Exposure
| Segment | Balance | % of Capital | Board Limit | Criticized % | 12-Mo Growth | Flag |
|---|---|---|---|---|---|---|

### Maturity Ladder and Refinance Test
| Bucket | Balance | Wtd DSCR | Wtd LTV | Refinances Clean | Needs Paydown | No Exit |
|---|---|---|---|---|---|---|
| 0-12 months | | | | | | |
| 13-24 months | | | | | | |
| 25-36 months | | | | | | |

### Sensitivity Results (single variable, source and date of each assumption)
| Shock | Level | Segment That Breaks First | Balance Below Policy Floor |
|---|---|---|---|

### Scenario Results
| Scenario | Loss Estimate | Criticized | Classified | Provision | Post-Stress Capital | vs Board Floor |
|---|---|---|---|---|---|---|
| Base | | | | | | |
| Adverse | | | | | | |
| Severely adverse | | | | | | |

Severity source and rationale:
Method: bottom-up / top-down by segment:
Last independent validation of methodology:

### Actions and Limit Recommendations
| Finding | Segment | Recommended Action | Owner | Timing |
|---|---|---|---|---|

### Data Gaps
List each missing or unreliable field, the tests it blocked, the owner, and the remediation date.

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every ratio names its denominator and numerator definition, and the tape reconciles to the call report with additions and exclusions listed
- Owner-occupied loans are excluded from the ratio numerator and still shown in portfolio risk analysis; REIT loans, unsecured developer lines, participations purchased, and unfunded commitments are addressed explicitly, in or out, with the policy basis stated
- HVCRE and construction and land development are reported as separate buckets, and the 300% test reports the ratio and the 36-month growth rate separately
- Every shock level carries a source, a date, and a rationale; borrowed supervisory scenario values are labeled as borrowed
- Sensitivity and scenario results are distinguished, and bottom-up and top-down segments are labeled
- The refinance test is run without extension options and without any asset-sale or securitization assumption
- Migration and reserve estimates are labeled as planning output, not rating or accounting conclusions
- Every failing segment carries a named action, an owner, and a date

---

## Red Flags & Dealbreakers

- The concentration ratio is quoted with no denominator named, or on total risk-based capital rather than tier 1 plus ACL
- The 300% criterion is presented as a hard cap, or being below it is presented as clearance
- The book has been sliced into narrow segments so that no single one trips a limit, or a broad pool carries a limit above 100% of capital with no sublimits beneath it
- Loan-level NOI, DSC, LTV, maturity, and rate type are unreliable, so the test runs on aggregate balances while being presented as loan-level
- A maturity ladder is presented with no refinance test, in a market where non-performing matured balloon loans were 65% of newly delinquent CMBS balances in June 2026 (Trepp data reported July 27, 2026)
- Interest-only loans are counted at contractual coverage with no as-if-amortizing recast, or IO is being extended on renewal without strong LTV and as-if-amortizing coverage
- Scenario severity is copied from a public supervisory stress test with no institution-specific calibration and no statement that it was borrowed
- Results are presented to the board with no change to limits, underwriting, pricing, capital, or ACL, or the methodology has never been independently validated
- Growth in a segment is outrunning the institution's ability to underwrite, monitor, and work out loans in it
- Improving headline delinquency is used to override a failing refinance test. FDIC's Quarterly Banking Profile for Q2 2026 (released August 25, 2026) showed nonfarm nonresidential CRE past-due and nonaccrual falling 14 bps to 1.52%, against an industry rate of 1.44%; that is a lagging measure on a different population from CMBS data and is not a forward signal
- Bank classification and ratio vocabulary is applied to a debt fund, life company, CMBS, or NCUA-supervised credit union portfolio without saying the framework does not govern it

---

## When Data is Missing

- No 36-month prior CRE balance: report the 300% ratio alone and state the growth test is unrun. Do not infer it from period-end balances of a different vintage
- No loan-level NOI, DSC, or LTV: run a labeled top-down test applying stressed loss rates to pools with common risk characteristics, and report the data gap as a finding in its own right rather than a footnote
- Stale appraisals: do not compound a cap-rate shock onto a value whose assumptions no longer hold. Route the affected loans to [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md) and mark the stressed LTV as indicative
- No board-approved scenario or post-stress capital floor: run the sensitivity grid, report the breaking level for each variable and segment and the post-stress ratio against the regulatory minimum, and note that appetite is undefined rather than issuing a scenario verdict
- No institution-specific migration history: state that migration is judgment-based, show the assumption, and do not present a stressed classified balance as a projection
- Owner-occupied flag unreliable: report the ratio both with and without the ambiguous balances and flag the classification as unverified

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Loan-level tape with current NOI, DSC, LTV, maturity, rate type, IO and HVCRE flags reconciled to the call report; capital and allowance confirmed; 36-month history and segment migration history available; board scenarios and limits supplied; methodology independently validated |
| MEDIUM | Loan-level tape complete on balances and structure but with stale or partial NOI, DSC, or valuation data, or with board scenarios or limits missing; results reported as ratios and sensitivities with the gaps named |
| LOW | Aggregate balances only, unreliable owner-occupied or CRE classification, no 36-month history, or no loan-level maturity and rate data; output is a top-down indication and a data-remediation list, not a portfolio verdict |

---

## Related Knowledge Bases

- [CRE Concentration and Stress Testing](knowledge/cre-concentration-and-stress-testing.md)
- [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [CRE Portfolio Concentration and Stress Tester Research](research/lender-credit/cre-portfolio-concentration-and-stress-tester-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
