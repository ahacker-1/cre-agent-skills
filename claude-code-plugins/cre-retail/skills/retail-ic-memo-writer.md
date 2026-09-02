---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail IC Memo Writer

Synthesize completed retail trade-area, rent roll, lease, co-tenancy, recovery, underwriting, and financing work into one investment committee memo with a decision table, a risk score, and named conditions.

---

## When to Use This Skill

Use this skill when the retail diligence is far enough along to make a call and the committee needs one document instead of seven. It fits acquisitions, refinancings, recapitalizations, and hold / sell / refi reviews of grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use, pad, and single-tenant net lease (STNL) retail. It is a synthesis skill: it reconciles upstream outputs, exposes where they disagree, and forces a decision with conditions. It does not re-run the underlying analysis. Use the memo skill that matches the asset: [IC Memo Writer](skills/underwriting/ic-memo-writer.md) for multifamily, [Office IC Memo Writer](skills/office/office-ic-memo-writer.md) for office, [Industrial IC Memo Writer](skills/industrial/industrial-ic-memo-writer.md) for industrial. This is educational decision support, not legal, tax, investment, accounting, or financing advice.

---

## What You'll Need to Provide

- Proposed transaction: action, price or basis, GLA, capital stack, hold period, target return, and who is deciding what by when
- The upstream outputs that exist, each with its date and confidence level: [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md), [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md), [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md), [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md), [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md), [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md), and [Retail Financing Fit](skills/retail/retail-financing-fit.md)
- Site plan with anchor and shop GLA separated, current rent roll, trailing operating statements, and the most recent full-year CAM reconciliation
- Reported tenant sales and occupancy cost by tenant where sales reporting exists, plus the sponsor's own occupancy cost threshold if it has one
- Sponsor thesis, business plan, capital plan, return hurdles, exit assumption and its comp support, any term sheet, appraisal, PCA, or Phase I in hand, and the open diligence list with owners

---

## Mission

Convert the pack's seven workstreams into one committee-ready decision that separates durable in-place retail income from anchor-, co-tenancy-, and recovery-dependent income, prices the cash cost of holding the asset through its rollover, scores the risk on a common framework, and states go / conditional go / no-go with conditions a person can actually satisfy.

---

## Strategy

### Step 1: Frame the Decision and Inventory the Evidence

Open with the decision, not the property. State the action, basis, capital required, hold, target return, and the recommendation in the first six lines, then build the evidence inventory before anything else.

- Classify the format from the site plan and rent roll against [Retail Benchmarks](knowledge/retail-benchmarks.md), which carries the ICSC GLA, anchor-count, anchor-GLA-share, and trade-area bands; a memo that inherits the offering memorandum's label inherits its bias.
- List every upstream analysis with its date, confidence level, and one-line verdict, and flag vintage conflicts explicitly. Missing analyses become open items in Step 6, never assumptions, and a trade-area study that predates a competing center's opening, an anchor bankruptcy, or a co-tenancy notice is stale for this decision.
- For pad and STNL, say up front that the memo is a lease-and-credit decision: term, credit, rent-to-market, and residual use carry current value, and the trade area governs residual value. Do not force a center memo shape onto a single-tenant box.

### Step 2: Build the Durable-Income Bridge

Show three income figures, never one. Formulas come from [Underwriting Calculations](knowledge/underwriting-calc.md); do not restate them in the memo.

1. **Contractual in-place NOI** as the rent roll and trailing statements support it.
2. **Durable NOI**, after removing percentage rent, specialty and temporary income, signed-not-open rent, the billed-to-recoverable gap from the recovery analysis, rent already subject to co-tenancy relief or an alternative-rent election, and rent from tenants whose occupancy cost says the renewal is unlikely.
3. **Stabilized NOI net of the capital to get there**, with TI, landlord work, commissions, downtime, free rent, and any anchor demising or capital work shown below the NOI line, not netted into it.

- Percentage rent is a tenant-health signal and equity upside, not underwritable income. Macerich disclosed percentage rent at 0.6% of tenant sales in 2025 (FY2025 10-K, directional), and lenders generally give it no credit toward debt service per [Retail Lender Criteria](knowledge/retail-lender-criteria.md).
- Renewal capital and new-deal capital are different orders of magnitude in open-air retail, so the retention assumption moves capital-adjusted cash flow more than the rent assumption does. State it as an assumption and sensitize it. If durable NOI is materially below contractual NOI, that gap is the memo's real subject; lead with it.

### Step 3: Test the Anchor, Co-Tenancy, and Lease Spine

This is where retail memos fail. Pull from the co-tenancy and lease work and present a cascade, not a line item.

- Anchor identity, ownership (leased, owned pad, or ground-leased), expiration against both loan maturity and the hold exit, option rent versus market, and whether an REA or OEA the sponsor does not control governs the site plan, parking, or backfill.
- For each co-tenancy clause: whether it is an opening or an operating co-tenancy, the trigger (named key tenants, a count of mini-majors, an occupancy percentage, or a stack of all three), the cure period, the remedy (rent reduction, alternative rent, or termination), and whether the tenant's own conditions to invoke are satisfiable. A replacement-tenant provision that a comparable backfill would satisfy is a materially different risk than a named-tenant trigger with no replacement language.
- Go-dark rights, continuous operation covenants, kick-outs, radius restrictions, and the exclusives and prohibited uses that shrink the backfill pool for the anchor and each major box. Then model the cascade: anchor goes dark, which co-tenancy clocks start, which tenants can reduce or terminate, and what durable NOI becomes. Assume the trigger fires in the downside case unless the clause's own conditions make that implausible.
- Pre-screen the result against the lender's own deterioration view. The CREFC watchlist cluster summarized in [Retail Lender Criteria](knowledge/retail-lender-criteria.md) treats a major tenant above 30% of NRA that is expiring, dark, defaulted, or bankrupt as trouble. If a plausible anchor loss would trip several of those, say so in the memo rather than at the credit committee.

### Step 4: Position the Trade Area, Tenant Mix, and Recovery Quality

Compress the trade-area and rent roll work into what changes the decision, and keep every market figure dated and sourced.

- Trade area: which boundary was used and why, demand and daytime population, the void and leakage read, the competitive set and pipeline, access, and what would break it
- Tenant mix: anchor and shop occupancy shown separately, not blended; WALT; top-tenant and top-five concentration; category exposure split between necessity, service, and experiential tenants on one side and categories whose growth is running in the non-store channel on the other. Census put e-commerce at 17.1% of total retail sales in Q2 2026, growing 12.2% year over year against 6.7% for total retail (U.S. Census Bureau, released 2026-08-18, directional).
- Sales and occupancy cost: report the ratio per tenant with its components named (base rent, CAM and tax reimbursements, percentage rent) and the share of inline GLA above the sponsor's stated threshold. Do not assert a national healthy band; the ratio only means something against that tenant's own fleet
- Recovery quality: the structure (pro rata, caps, base year, gross-up, admin fee, capital recovery, anchor carve-outs), the billed-to-recoverable gap, and whether the gap is structural or a vacancy artifact. A stabilized center recovering materially less than its recoverable expense base needs a structural explanation, not a growth assumption.

### Step 5: Present Underwriting, Valuation, Financing, and Exit

- Show base, downside, and a co-tenancy-fires case side by side, each with its own NOI, DSCR low point, IRR, equity multiple, and peak equity; a downside case without an anchor event is not a retail downside case. Name the three assumptions that carry the return and sensitize each: renewal retention, market rent and concession posture, and exit cap.
- Present as-is value with the deductions and discounts a supervised appraisal would carry. The Interagency Appraisal and Evaluation Guidelines (2010-12-02) require that for proposed and partially leased rental developments the appraiser make deductions and discounts for leasing commissions, rent loss, tenant improvements, and entrepreneurial profit, with absorption of unleased space considered, and that non-market lease terms be disclosed with the interest appraised. The same guidelines require the appraisal function to be independent of loan production and the appraiser to hold no direct, indirect, or prospective interest in the property or transaction, so if the only value in the file was commissioned by the seller or the broker, say so.
- Borrow the disclosed institutional criteria as a completeness test: industry, tenant credit, and market conditions; expected returns under multiple scenarios including default; the value of the underlying real estate on replacement cost, market rent, and alternative use; and unit-level store profitability where available (Realty Income FY2025 Form 10-K). A memo missing one of those four is incomplete.
- State the lender lane, the sizing test that binds, and the reserve and cash-management structure, drawing on [Retail Lender Criteria](knowledge/retail-lender-criteria.md). Expect a haircut to broker or issuer NOI, and show what proceeds look like on durable NOI rather than stabilized NOI.
- Run the refinance test explicitly: at maturity, on durable NOI, at a stressed constant, does the loan clear? The OCC's Spring 2026 Semiannual Risk Perspective calls retail a bright spot with low vacancy and little space available in most markets while flagging that a substantial volume of CRE loans originated at lower rates must refinance at prevailing rates, and the Federal Reserve's July 2026 SLOOS found a moderate net share of banks easing standards on nonfarm nonresidential loans while its special questions found standards still at the tighter end of the range since 2005 for every category except C&I. Both are directional context with dates, not support for the math.
- Exit: name the buyer type and support the exit cap with a comp. For pad and STNL, The Boulder Group reported Q2 2026 STNL cap rates of 6.82% overall and 6.60% for retail, with overall STNL marketed supply up 12.5% to roughly 5,800 properties and investment grade product under 10% of retail supply (2026-07-07, directional). For centers, no published cap-rate matrix by format is available here; the exit cap needs a transaction comp or it is an assumption.

### Step 6: Score the Risk, Build the Decision Table, and Set Conditions

- Score with [Risk Scoring](knowledge/risk-scoring.md): the nine-category framework, the strategy weights for core, value-add, or opportunistic, the hard and soft dealbreaker checklist, and the recommendation values (PROCEED, PROCEED_WITH_MITIGATIONS, PROCEED_WITH_CAUTION, FURTHER_DILIGENCE, REJECT). Category 9 is multifamily-specific and is not scored here; retail escalations live inside Financial, Market, and Tenant Concentration, and escalate to at least HIGH within Tenant Concentration when an anchor above 30% of GLA expires inside the loan term or hold with no signed renewal and no reserve, when a co-tenancy trigger is already satisfied or would be by a single plausible event, or when top-tenant concentration and co-tenancy triggers sit in the same leases.
- Build the decision table: each driver gets a test, a finding, and a PASS / WATCH / FAIL verdict. The recommendation must be consistent with the table, and any FAIL that is not a dealbreaker must carry a condition.
- Write conditions precedent as testable statements with an owner and a date: estoppels from the anchor and each co-tenancy-holding tenant; the recorded REA / OEA and any amendments; the anchor's signed renewal or a sized reserve; three years of CAM reconciliations and the audit history; sales reports for the tenants carrying the occupancy cost conclusion; a lender term sheet on durable NOI; PCA, Phase I, and survey; and any price adjustment the findings support.
- A conditional approval that cannot name its conditions is a no-go; say that plainly rather than hedging the recommendation.

---

## Output Format

```markdown
# Retail Investment Committee Memo
## Property / Format / GLA (anchor vs shop):
## Transaction:
## Recommendation: GO | CONDITIONAL GO | NO-GO
## Risk Score: [0-100] | [LOW | MEDIUM | HIGH | CRITICAL] | Framework recommendation value:

### 1. Executive Decision
- Action, basis, price PSF, capital required, hold, target return:
- Main reason to proceed / main reason to pause:
- What has to be true for this to work:

### 2. Evidence Inventory
| Upstream Analysis | Date | Confidence | Verdict | Gap Carried Forward |
|---|---|---|---|---|

### 3. Investment Thesis, Trade Area, and Recovery Quality

### 4. Tenant Mix, Sales, and Occupancy Cost
| Tenant | Role | GLA | % ABR | Expiry | Sales PSF | Occupancy Cost % | Renewal Read |
|---|---|---:|---:|---|---:|---:|---|

### 5. Anchor, Co-Tenancy, and Lease Risk
| Clause / Right | Tenant | Trigger | Cure | Remedy | Rent at Risk | Fires in Downside? |
|---|---|---|---|---|---:|---|

### 6. Income Bridge
| Measure | Amount | PSF | Notes |
|---|---:|---:|---|
| Contractual in-place NOI | | | |
| Less percentage / specialty / signed-not-open | | | |
| Less recovery leakage | | | |
| Less at-risk rent (co-tenancy, occupancy cost) | | | |
| Durable NOI | | | |
| Stabilized NOI (net of capital to get there) | | | |

### 7. Returns, Financing Fit, Exit, and Refinance Test
| Case | NOI | DSCR Low Point | IRR | Equity Multiple | Key Assumption |
|---|---:|---:|---:|---:|---|
| Base | | | | | |
| Downside | | | | | |
| Co-tenancy fires | | | | | |
| Lender lane, binding test, reserves, exit comp | | | | | |

### 8. Decision Table
| Driver | Test | Finding | Verdict |
|---|---|---|---|
| Trade area durability | | | PASS / WATCH / FAIL |
| Anchor term and control | | | |
| Co-tenancy cascade | | | |
| Tenant mix, concentration, and occupancy cost headroom | | | |
| Recovery structure and durable NOI vs contractual NOI | | | |
| Capital plan funded | | | |
| Debt sizing, refinance test, exit comp support | | | |

### 9. Risks and Mitigants
| Risk | Risk-Scoring Category | Score | Impact | Mitigant / Condition |
|---|---|---:|---|---|

### 10. Conditions Precedent and Open Diligence Items
| Item | Condition Precedent or Open Item | Blocks Decision? | Owner | Due |
|---|---|---|---|---|

### 11. Final Recommendation

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every number traces to a named upstream analysis, a lease section, a filing, or an operating statement, no figure is created inside the memo, and anchor occupancy and shop occupancy are shown separately rather than blended into one leased rate
- Contractual, durable, and stabilized NOI all appear, and leasing and capital costs sit below the NOI line
- Occupancy cost ratios name their components and are compared to the tenant's own fleet, not to a national band
- Every co-tenancy clause has a trigger, a cure period, a remedy, and a stated view on whether it fires in the downside case, and the downside case includes an anchor event
- Exit cap is supported by a comp, and every market figure carries a date and a source and is labeled directional
- The risk score, the decision table, and the recommendation agree; every FAIL carries a condition or a dealbreaker call, and conditions precedent are testable with an owner and a date

---

## Red Flags & Dealbreakers

- GO recommended while an anchor above 30% of GLA expires inside the loan term or hold with no signed renewal, no reserve, and no backfill plan, or a co-tenancy trigger already satisfied (or satisfied by one plausible event) with the relief rent still shown as in-place income
- Anchor dark but paying, presented as stable rent, while traffic collapses, inline sales fall, and co-tenancy clocks may already be running
- Durable NOI materially below contractual NOI, with the memo underwriting the contractual figure
- Site plan, parking, pad splits, or backfill controlled by an REA or OEA the sponsor does not control, and treated as a formality
- A recovery structure with caps, base years, or anchor carve-outs that leaves a permanent billed-to-recoverable gap not reflected in underwritten NOI
- Return driven by cap-rate compression, rate cuts, or a refinance that has not been quoted, or a stabilized value used without the deductions and discounts for leasing commissions, rent loss, tenant improvements, and absorption
- Conditional approval with no named conditions, or conditions with no owner and no date
- Any hard dealbreaker on the [Risk Scoring](knowledge/risk-scoring.md) checklist, which overrides the score and the narrative

---

## When Data is Missing

- If an upstream analysis is missing, carry the topic as an open diligence item with the decision it blocks, and never substitute a national benchmark for the analysis
- If lease documents are incomplete, mark lease and co-tenancy confidence LOW and do not net any at-risk rent back into durable NOI
- If reported tenant sales do not exist, say the occupancy cost conclusion is unsupported and route the reporting-covenant question to [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md); if CAM reconciliations are missing, model recoveries at the billed-to-recoverable gap the trailing statements imply and flag the structure as unverified
- If financing terms are missing, present unlevered returns plus a debt-sizing sensitivity and do not recommend GO on a levered return; if the underwriting model is incomplete or a hard dealbreaker is unresolved, the recommendation is NO-GO or FURTHER_DILIGENCE, not a conditional GO

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | All seven upstream analyses complete and current, lease and REA / OEA documents reviewed, CAM reconciliations and tenant sales in hand, term sheet received, exit cap supported by a comp, and no material vintage conflicts |
| MEDIUM | Core underwriting, lease, and co-tenancy work complete but one or two workstreams open, or sales coverage partial, or financing indicative rather than quoted |
| LOW | Material lease, co-tenancy, recovery, sales, or financing data missing; upstream analyses of conflicting vintage; or national data used as a substitute for trade-area evidence |

---

## Related Knowledge Bases

- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Retail Lender Criteria](knowledge/retail-lender-criteria.md)
- [Risk Scoring](knowledge/risk-scoring.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Retail IC Memo Writer Research](research/retail/retail-ic-memo-writer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
