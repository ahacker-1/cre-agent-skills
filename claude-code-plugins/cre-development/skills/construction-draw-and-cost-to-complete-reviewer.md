---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Construction Draw and Cost-to-Complete Reviewer

Review a monthly construction draw package end to end: schedule of values and pay application, percent complete against the independent inspector, retainage, stored materials, lien waivers, title date-down, change orders and contingency, budget reallocations, cost to complete, the in-balance test, and interest reserve burn, then recommend fund, partial-fund, or hold with conditions.

---

## When to Use This Skill

Use this skill on any periodic advance under a construction loan or an owner-funded construction budget: the developer assembling the requisition, the owner representative or construction consultant certifying it, the construction lender's loan administrator funding it, or the equity partner reading the monthly report and asking whether the project is still inside its money. Use it also on a first draw, where the schedule of values is being accepted for the life of the job, and on the final advance, where the holdback is released. For value-add renovation spend on a stabilized asset, the budget-versus-actual and rent-premium view belongs to [CapEx & Value-Add Execution Tracker](skills/asset-management/capex-value-add-execution-tracker.md); this skill reviews a lender-monitored or owner-funded construction advance. This is educational decision support, not legal, tax, investment, accounting, or financing advice. Lien law, retainage caps, waiver forms, and prompt-payment deadlines are state-specific and change; the executed loan agreement, the executed construction contract, and the governing state statute control, and counsel should review any waiver, lien, or notice question.

---

## What You'll Need to Provide

- The draw package: pay application and certificate (AIA G702 or the lender's form), continuation sheet (G703) or equivalent schedule of values detail, and the cover request, plus every prior funded application
- The approved development budget and each approved revision, and the current line-item budget the lender funds against
- Third-party inspector or construction consultant report for this period, with photos and an independent percent complete
- Change order log: executed and pending change orders and open construction change directives, with owner and contractor contingency usage shown separately
- Lien waivers for this period and for the prior funded period, the title date-down endorsement for this advance and the date of the last one, and certificates of insurance and bond information
- Loan documents: disbursement conditions, retainage and stored-materials provisions, in-balance covenant, interest reserve balance and draw history, remaining commitment
- Construction contract type and key terms: stipulated sum, GMP, or cost plus, with the retainage schedule and any reduction milestones
- Project state, program (conventional, FHA-insured, agency, SBA, public work), and the current schedule with the contract completion date
- The business question: fund as requested, fund a reduced amount, hold pending conditions, or escalate

---

## Mission

Establish what was actually built and paid for this period, confirm the money requested matches it, confirm the lien and title position is intact through this advance, and prove that what remains to be funded is still enough to finish the job and carry it to stabilization. Produce a fund / partial-fund / hold recommendation with a dollar figure and a numbered condition list.

---

## Strategy

### Step 1: Test the Schedule of Values Before You Test the Draw

The schedule of values is the ruler every later application is measured with. Test it on the first draw and again whenever it is revised. Confirm the SOV total ties to the executed contract sum and the sum ties to the budget line the lender funds; that the SOV is broken out by trade or CSI division rather than a few undifferentiated blocks, with general conditions, contractor fee, insurance, bonds, and contractor contingency each on their own line; that contractor contingency is visible rather than embedded across trades, so a contingency draw stays distinguishable from a change order; and that any SOV revision this period was approved and did not quietly move money out of unbought scope into completed lines.

Look hardest for front loading. The OCC Comptroller's Handbook defines it as a builder deliberately overstating the cost of early-stage work, and warns that if it is not detected early there will almost certainly be insufficient loan funds to complete construction on a default. Test general conditions and mobilization against the schedule duration, and early trades against a normal cost curve for the delivery type. If the SOV cannot be tied to the contract and the budget, stop; everything downstream inherits the error.

### Step 2: Reconcile the Pay Application to the Inspector

Run the arithmetic first, then the judgment.

| Check | What to confirm |
|---|---|
| Contract sum to date | Original contract sum plus net executed change orders equals the figure on the application |
| Completed and stored to date | Equals prior periods plus this period, line by line, with no line exceeding its scheduled value |
| Percent complete | Line-level percent equals completed and stored divided by scheduled value |
| Retainage | Computed at the contract rate on the correct base, and consistent with prior applications |
| Less previous certificates | Equals the sum actually funded, not the sum requested, on prior draws |
| Current payment due | Recomputes cleanly from the lines above |
| Balance to finish | Scheduled value less completed and stored, and it reconciles to Step 5 |

Then compare every line to the inspector. Both HUD and bank supervisory practice run the same rule: HUD requires that the amount advanced for construction items be consistent with construction progress as approved by the HUD inspector, and the OCC describes inspection reports as supporting disbursements based on percentage complete, with construction credit administration independent of the origination function where possible.

Decision rule: where the application's percent complete on a line exceeds the inspector's observed percent, fund the inspector's figure and list the line; where the inspector observed more than the application requests, fund the request. Report the aggregate dollar variance both ways, and do not apply a blanket tolerance band, because no source supports one. If there is no independent inspection this period, the review cannot certify percent complete; say so rather than funding on the contractor's assertion.

### Step 3: Retainage, Stored Materials, and Soft Costs

**Retainage.** Identify the controlling authority before judging the percentage. The regimes genuinely differ:

| Regime | Rule | Source basis |
|---|---|---|
| Common U.S. commercial bank practice | Bank normally retains 10% to 20% of each payment under a progress payment plan | OCC Comptroller's Handbook |
| California private work, contracts entered on or after 2026-01-01 | Retention capped at 5% of the payment and 5% of the contract price, flows down to every tier, non-waivable, mandatory attorney fee award, narrow exceptions | Civil Code section 8811 |
| Texas | Owner must reserve 10% of the contract price or 10% of the value of work during the work and for 30 days after completion | Property Code section 53.101 |
| FHA-insured multifamily | 10% until 50% completion, then 5% until 75%, then 2.5% to Final Endorsement, only where contractor identity of interest is not above 5%, with prior written surety consent and clean performance | HUD MAP Guide (4430.G), Chapter 12 |
| Federal construction contracts | Discretionary, for unsatisfactory progress only, capped at 10% | FAR 32.103 and FAR 52.232-5 |

Confirm the rate charged, the base it is charged on, whether any reduction milestone was hit, and whether a reduction on bonded work carries written surety consent. A reduction taken without consent can impair the bond.

**Stored materials.** Fund only what the contract and loan agreement allow. On site, confirm the material is there and insured. Off site, the strictest documented U.S. standard is HUD's: only manufactured or pre-assembled building components impractical to store on site qualify (precast panels, assembled bath or kitchen core units, fabricated structural steel), while appliances, carpeting, and wood roof trusses do not; payment is limited to invoice value; a bill of sale evidencing owner title and an itemized invoice accompany each request; the storage location is lender-approved; a first-lien UCC-1 is filed; and the contract carries the offsite rider and a 100% performance and payment bond. Private lenders vary, but an offsite request supported by an invoice alone should not be funded.

**Soft costs and fees.** Require bills or receipts above the lender's backup threshold. Confirm the developer fee draw is consistent with the disbursement basis in the loan agreement; the OCC notes a developer fee, distinct from developer profit, typically does not exceed 4% of project cost and is often deferred or disbursed on percentage of completion. Reject costs the loan agreement does not stipulate: the OCC names rebuilding to undisclosed specification changes, starting a new project, paying subcontractors for work performed elsewhere, and developer general corporate overhead.

### Step 4: Lien Waivers, Title, Insurance, and Bonds

Sequencing is the whole point. California's statutory forms are the clearest model: a conditional waiver on progress payment is effective only on the claimant's receipt of payment (Civil Code 8132), while an unconditional waiver carries the statutory notice that it is enforceable against the signer even if the signer has not been paid (Civil Code 8134).

Conditional waivers for this period accompany this request; unconditional waivers for the prior period arrive as proof the prior advance funded. Both should cover the general contractor and every subcontractor and supplier above the threshold, with amounts and through-dates that tie to the prior funded application. In a state that prescribes a form, the waiver must substantially follow it; advance waivers signed before the work, and waiver language embedded in a subcontract, are counsel questions. Unconditional waivers in the package for work not yet paid are a control failure: do not fund, correct the package.

Confirm the title date-down endorsement for this advance was issued and the endorsement sequence has no gap. The OCC states the lender's title policy should be updated with each draw and notes mechanics liens can take priority over the bank lien in some jurisdictions; ALTA's construction loan endorsements (32, 32.1, 32.2) and the disbursement endorsement (33) are the instruments to look for. Confirm builder's risk, general liability, and workers compensation are in force through the period with limits adequate against the revised contract sum, and on bonded work that the penal sum still covers it and the lender is named or holds a dual-obligee rider.

### Step 5: Change Orders, Contingency, and Budget Reallocations

Reconcile the change order log to the pay application: net executed change orders on the application must equal the log. Price the open construction change directives, since AIA directs that a CCD be priced as if it were a proposed change order and recorded in the log, and an unpriced directive open for multiple cycles makes the contract sum, the cost to complete, and the schedule all stale at once. Separate contingency draws from change orders: a contingency draw spends a reserve already inside the number, a change order increases it, and if contingency is drawn through change orders that also raise the GMP the cap is no longer a cap.

Test remaining contingency against remaining scope, not elapsed time. AIA cites 5% to 10% as common for construction contingency and 5% to 10% of construction cost for design contingency, and states remaining construction contingency is the owner's; those ranges are directional starting points, not requirements, and the executed contract controls where savings and unused contingency go. Diagnose the cause of each overrun, because the OCC frames contingency as covering reasonable but unexpected increases (material prices, overtime from shipping delays, weather) and says overruns from poor projections or management would ordinarily be borrower-funded. Review every budget reallocation: which line was reduced, whether that scope is bought and complete, and whether the reduction is real savings or a deferral. The OCC expects change orders to be reviewed by competent staff or a construction consultant, approved and documented by the bank and any take-out lender, and treats a rising change order count as a signal of planning, design, or construction problems.

### Step 6: Cost to Complete, In-Balance Test, and Interest Reserve Burn

Cost to complete, by line:

> Revised budget, less cost incurred to date (completed plus stored), plus the priced value of pending change orders and open construction change directives, plus remaining interest and carry.

Show pending changes at both the contractor's requested value and the owner representative's independent estimate rather than choosing one.

In-balance test, run every draw:

> Remaining loan commitment + unfunded borrower equity + remaining contingency >= cost to complete + remaining interest and carry

If it fails, the loan is out of balance and the borrower funds the gap before further advances. State the gap in dollars and name the source of the cure.

For the interest reserve, compute burn per month against the balance and the months remaining to completion and stabilization on the current schedule, not the original one. During lease-up, project cash flow is applied to interest before the reserve is drawn, and once cash flow covers interest the reserve draws should stop. Treat the balance as a diagnostic, not comfort: the OCC states plainly that the presence of an interest reserve may not accurately reflect a borrower's ability to pay, and that a decision to revise the budget and repack a depleted reserve with new loan proceeds is a red flag indicating possible credit deterioration, properly supported only by a new appraisal or evaluation and a fresh feasibility review. Deliver the monthly package the OCC expects: work completed, costs to date, cost to complete, deadlines, and loan funds remaining.

### Step 7: Reach a Verdict and Write the Conditions

- **FUND** when the arithmetic ties, the inspector supports percent complete, waivers and title are in sequence, the log reconciles, and the loan is in balance
- **PARTIAL FUND** when specific lines are unsupported. Fund the supported amount, name each held line and dollar figure, and state what releases it
- **HOLD** when percent complete cannot be verified, waiver or title sequence is broken, or the loan is out of balance. Pair a hold with a written statement of what is disputed and why: federal construction contracts carry a 14-day progress payment deadline, retainage release 30 days after approval, and a 7-day flow-down to subcontractors under FAR 52.232-27, and most states have private prompt-payment statutes with their own deadlines and penalties

On the final advance the release gate is fixed, per the OCC: all lien waivers or releases obtained, a final inspection confirming the project is complete and meets building specifications, and a certificate of occupancy. Insured and bonded deals add contractor cost certification and consent of surety. The approved budget and contingency it measures against come from [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md), and the commitment, retainage schedule, interest reserve, and in-balance covenant it enforces come from [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md). Send any change order or directive whose authorization, pricing, or entitlement to time is in question to [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md), and take the current completion date that drives interest reserve coverage from [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md). Permit conditions and conditions of approval that can gate a draw trace back to [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md). Hand the confirmed delivery date and final cost basis to [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md), and the cost-to-complete, in-balance, and reserve-coverage results to [Development IC Memo Writer](skills/development/development-ic-memo-writer.md).

---

## Output Format

```markdown
# Construction Draw Review
## Project / Draw No. / Period:
## Amount Requested / Amount Recommended:
## Recommendation: FUND | PARTIAL FUND | HOLD

### Application Reconciliation
| Line | Amount | Ties To | Result |
|---|---|---|---|
| Contract sum to date | | Contract + executed COs | |
| Completed and stored to date | | Prior + this period | |
| Retainage | | Contract rate / state rule | |
| Less previous certificates | | Prior funded | |
| Current payment due | | Recomputation | |
| Balance to finish | | SOV less completed | |

### Percent Complete vs Inspector
| SOV Line | App % | Inspector % | Variance $ | Funded % |
|---|---|---|---|---|

### Draw Controls
| Control | Status | Finding |
|---|---|---|
| Schedule of values / front loading | | |
| Retainage (state / program rule) | | |
| Stored materials (on site / off site) | | |
| Lien waivers (conditional current / unconditional prior) | | |
| Title date-down (ALTA 33 or equivalent) | | |
| Insurance and bonds in force, surety consent | | |
| Soft cost and fee backup | | |

### Changes and Contingency
| Item | Executed | Pending | Open CCD | Budget Impact |
|---|---|---|---|---|

- Contingency remaining vs remaining scope; reallocations this period and approval status:

### Cost to Complete and In-Balance
| Component | Amount |
|---|---|
| Revised budget less cost incurred to date | |
| Pending changes and open CCDs | |
| Remaining interest and carry | |
| Cost to complete | |
| Remaining commitment + unfunded equity + contingency | |
| Surplus / (Deficit) | |

- Interest reserve balance, burn per month, months of coverage vs months to stabilization:

### Discrepancies
| Issue | Severity | Dollar Impact | Condition to Clear |
|---|---|---|---|

### Conditions to Funding (numbered, each tied to a discrepancy above)

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every arithmetic line on the application recomputes, and previous certificates tie to amounts actually funded rather than amounts requested
- Percent complete is reconciled line by line to an independent inspection dated in this period, with variance shown in dollars, and no line was funded above the inspector's observation
- Retainage is tested against the controlling state statute or program rule, not against habit, and any milestone reduction shows surety consent where the work is bonded
- Conditional waivers cover this period and unconditional waivers cover the prior funded period, with amounts and through-dates that tie, and stored materials are supported to the standard the loan agreement sets
- The title date-down sequence has no gap and no advance was disbursed out of sequence
- The change order log reconciles to the application, open construction change directives are priced and carried in cost to complete, contingency draws are distinguishable from change orders, and remaining contingency is tested against remaining scope
- Cost to complete and the in-balance test are recomputed this period rather than carried forward, and interest reserve coverage is measured against the current schedule

---

## Red Flags & Dealbreakers

- Application percent complete exceeds the inspector's observation and nobody has reconciled it, or there is no independent inspection this period at all
- Schedule of values is front-loaded, or general conditions, fee, and contingency are buried in undifferentiated blocks
- Unconditional lien waivers are in the package for work that has not been paid, or a waiver in a form state does not substantially follow the statutory form
- Title date-down is missing for this advance, or advances were disbursed out of sequence with the endorsements, in a jurisdiction where mechanics liens can prime the mortgage
- Retainage is held above the governing state cap, or reduced at a milestone on bonded work without prior written surety consent
- Construction change directives have been open and unpriced across multiple draw cycles while the work proceeds
- Contingency is drawn through change orders that also increase the GMP, contingency is largely consumed while the schedule has slipped, or budget reallocations move money out of unbought scope into completed lines
- Off-site stored materials funded with no bill of sale, no lender-approved storage location, no UCC filing, and no insurance
- The in-balance test fails and the draw is funded anyway, the interest reserve is repacked with new loan proceeds instead of borrower or guarantor cash, or reserve draws continue after project cash flow is sufficient to cover interest
- Contractor has an identity of interest with ownership above a nominal level and retainage release, buyout, or pricing has not been tested at arm's length
- Final payment processed before final lien releases, final inspection confirming completion to specification, certificate of occupancy, and, on insured or bonded work, cost certification and consent of surety

---

## When Data is Missing

- No independent inspector report: do not certify percent complete. Fund only lines that are objectively verifiable (soft costs with receipts, invoiced stored materials with title evidence) and hold the balance
- No prior funded application: reconstruct previously completed from the lender's funding history before accepting the application's prior-period column. Change order log missing or stale: treat pending changes as unquantified, carry the contractor's requested value in cost to complete with a flag, and do not net unapproved changes into the contract sum
- Loan agreement not provided: state that retainage, stored materials, backup thresholds, and the in-balance covenant are being evaluated against general practice rather than the governing document, and mark confidence LOW
- State not identified: do not apply any retainage cap or waiver form rule; name the question and route it to counsel. Interest reserve history missing: compute months of coverage from the balance and the last known monthly interest, and label it an estimate
- Do not infer a percent complete, a waiver, or a title endorsement that is not in the package. Missing documents are findings, not assumptions

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Complete package with pay application, continuation sheet, prior funded applications, dated third-party inspection with photos, waivers in correct sequence, title date-down, current change order log, loan agreement, and a recomputed cost to complete and in-balance test |
| MEDIUM | Application and inspection available and reconcilable, but one control is incomplete: a waiver set, a title date-down, an unpriced directive, or an interest reserve history that has to be estimated |
| LOW | No independent inspection this period, no loan agreement, missing prior-period support, or an unreconciled change order log; percent complete and cost to complete cannot be certified |

---

## Related Knowledge Bases

- [Construction Contracts and Draw Controls](knowledge/construction-contracts-and-draw-controls.md)
- [Construction Lending Criteria](knowledge/construction-lending-criteria.md)

## Research Basis

- [Construction Draw and Cost-to-Complete Reviewer Research](research/development/construction-draw-and-cost-to-complete-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
