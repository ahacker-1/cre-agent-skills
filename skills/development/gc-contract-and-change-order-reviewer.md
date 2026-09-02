---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# GC Contract and Change Order Reviewer

Review a general contractor or construction manager agreement and its exhibits for price, time, payment, and risk transfer, review individual change orders for entitlement, pricing, and schedule impact, and produce an issues list with negotiation positions.

---

## When to Use This Skill

Use this skill when a GC or CM agreement arrives for signature, when a GMP amendment is delivered at the end of preconstruction, when a construction lender or equity partner conditions closing on contract review, when a change order or construction change directive needs a disposition, or when a project is already in trouble and someone needs to know what the contract actually says. This is educational decision support, not legal, insurance, tax, accounting, or financing advice. Contract interpretation, lien and waiver sufficiency, enforceability of liquidated damages and indemnity, and insurance adequacy require counsel and a licensed broker in the project state.

The scope here is the construction contract and its exhibits only. Adjacent documents belong to other packs: [Loan Document Reviewer](skills/legal/loan-doc-reviewer.md) reads the loan agreement and its covenants, and [Insurance Coordinator](skills/legal/insurance-coordinator.md) places and verifies coverage against a lender's requirements. Reconcile against those rather than duplicating them.

---

## What You'll Need to Provide

- The agreement itself and its form family: AIA A101 (stipulated sum), A102 (cost plus fee with a GMP), A133 (construction manager as constructor with a GMP), A134 (no GMP), or a ConsensusDocs, EJCDC, DBIA, or owner-drafted equivalent
- Every exhibit and attachment: the GMP amendment and its assumptions and clarifications, the schedule of values, unit price schedule, alternates, allowance schedule, the insurance and bonds exhibit, supplementary and special conditions, and the list of drawings and specifications the price is based on
- The general conditions actually adopted (A201-2017 or equivalent) **in its modified form**, not a clean copy of the standard document, plus the baseline schedule, the substantial completion date, and any liquidated damages or early completion incentive provision
- For change order review: the change order or directive, the pricing backup, the RFI, ASI, bulletin, or field condition that generated it, the notice correspondence, and a schedule analysis if time is claimed
- Deal context: the construction loan term sheet or loan agreement, the development budget and contingency balances, bond or letter of credit requirements, and whether the contractor has any identity of interest with ownership
- The business question: negotiate, sign, price a change, defend a delay claim, or brief a lender or equity partner

---

## Mission

Determine what price the owner actually has, what is excluded from it, who bears each category of overrun, what the delay remedy is worth, when money leaves the owner's control and when it comes back, and whether the risk transfer and lender provisions survive as drafted. On a change order, determine whether the contractor is entitled to anything at all before arguing about the number.

---

## Strategy

### Step 1: Identify the Form, the Delivery Method, and Everything That Modifies It

Delivery method (who builds, when they join) and contracting format (how they are paid) are separate choices; do not conflate them.

- Name the agreement, the general conditions adopted, the owner-architect agreement, and every exhibit, and state which documents are missing
- Read the supplementary and special conditions **before** the general conditions and build a modification map: which sections were deleted, replaced, or rewritten. AIA numbering survives modification; the text does not. A finding that cites a section number without quoting the executed language is not a finding
- Classify who bears overrun: stipulated sum (contractor bears overrun, keeps savings), GMP (contractor bears cost above the GMP absent an approved adjustment, owner keeps the benefit below it per the savings provision), cost plus with no GMP (owner bears it)
- On an A133 or A102, go straight to the GMP amendment. Per AIA's A133-2019 instructions it must state the GMP amount, an itemized breakdown, the assumptions and clarifications the price rests on, a schedule of values with unit prices and the quantity limitations they assume, the alternates included and the conditions for accepting alternates later, and the substantial completion date
- State design completeness at GMP as a percentage and name the drawing set and date. A GMP on a 60% set is a budget with a signature on it

### Step 2: Test the Price and What Is Excluded From It

The assumptions and clarifications page is the highest-yield page in the document. Scope that looks priced is excluded there.

| Item | What to confirm | Owner position |
|---|---|---|
| Assumptions and clarifications | Every qualification, exclusion, allowance-by-another-name, and "by others" item, reconciled line by line to the drawing list | Convert each one into a priced line, a stated owner risk, or a deleted qualification |
| Allowances | What each covers. Under A201 3.8 the allowance covers materials and equipment delivered plus required taxes less trade discounts; unloading, handling, labor, installation, overhead and profit sit in the contract sum, not the allowance | Define scope per allowance, set a selection deadline (3.8.3 requires owner selection with reasonable promptness), and state who bears overage |
| Contractor's contingency | Location (inside the GMP), what draws are permitted, and whether a draw is reported separately from a change order | Written draw approval; unused contingency reverts to the owner; contingency never funds scope growth or an incomplete budget |
| Unit prices and alternates | The rate **and** the quantity band it assumes; which alternates are in, and the deadline and condition for accepting one later | A rate with no quantity limit is not a control; alternates carry a price and an expiration |
| Cost of the work, fee, and savings | Definition of reimbursable cost, general conditions detail, self-perform work, audit rights, and where buyout and GMP savings go | Line-item general conditions, open books, audit right surviving final payment; AIA's GMP guidance treats the savings split as a drafting choice, not a default |

Directional benchmark, sourced: AIA cites 5%-10% as a common construction contingency and 5%-10% of construction cost as a common design contingency, and states that unused contractor contingency belongs to the owner in CM/GC delivery. Treat these as starting points, not requirements. Contractor fee, general conditions percentage, and savings splits are negotiated and market-specific; this library publishes no default for any of them.

### Step 3: Test Time, Completion, and Delay Damages

- Confirm the commencement date, contract time, milestone and substantial completion dates, whether time is of the essence, what Substantial Completion means in this document, who certifies it, what the certificate allocates (security, maintenance, utilities, insurance, punch duration), and what Final Completion additionally requires
- Test liquidated damages on the two-prong standard practitioners apply: damages were difficult to ascertain when the contract was signed, and the amount is a reasonable estimate of probable damages or reasonably proportionate to actual damages. A rate a challenger can show is shockingly disproportionate risks being struck as a penalty
- Then find the apportionment clause. Under the non-apportionment rule described in the commentary reviewed, liquidated damages can be unenforceable where the party benefiting from them caused part of the delay, unless the contract provides for apportionment. On a project with any owner-caused delay, a liquidated damages clause without apportionment language is a remedy that may not exist
- Read the mutual waiver of consequential damages (A201 15.1.7) against the liquidated damages rate. The waiver typically gives up the owner's lost rent, loss of use, income, profit, and financing damages while expressly preserving liquidated damages, so the rate is not a cap on the delay remedy, it is usually the whole remedy. Size it against carry, rate-lock, and lease-commencement exposure from [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md)
- Confirm force majeure, weather, and excusable-versus-compensable delay definitions, and whether an early completion bonus exists and what triggers it

### Step 4: Test Payment, Retainage, and Closeout

- Application timing, required backup, the certification chain, and who may withhold. A201 9.5.1 supplies the checklist of grounds: defective work not remedied; third-party claims filed or reasonable evidence of probable filing without acceptable security; failure to pay subcontractors or suppliers; reasonable evidence the work cannot be completed for the unpaid balance; damage to the owner or a separate contractor; reasonable evidence the work will not finish within the contract time and the unpaid balance would not cover actual or liquidated damages; and failure to carry out the work per the contract documents
- Test the retainage percentage against **state law first, contract habit second**. Directional and dated, confirm current law: California Civil Code 8811, for private-work contracts entered into on or after 2026-01-01, caps retention at 5% of the payment and 5% of the contract price, with bond-failure and small-residential exceptions and mandatory attorney fees to the prevailing party. Texas Property Code 53.101 requires the owner to reserve 10% of the contract price or of the value of work done during the work and for 30 days after completion. HUD's MAP Guide requires 10% until 50% completion, then permits 5% to 75% and 2.5% to Final Endorsement, conditioned on no identity of interest above a 5% equity interest, prior written surety consent, and no open performance questions
- Confirm the stored materials provision, off-site storage conditions, lien waiver forms and sequencing (California prescribes four statutory forms under Civil Code 8132, 8134, 8136, and 8138, where conditional waivers bind only on actual payment and unconditional waivers bind on signature), and the final payment conditions
- Build the closeout holdback from HUD's model: 150% of the cost estimate for items of delayed completion, any owed or contested lien amounts, the lesser of liquidated or actual damages, and the net of change orders where that net is negative. Hand the schedule of values, retainage schedule, and stored materials terms to [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md)

### Step 5: Test Risk Transfer and Lender-Required Provisions

- **Bonds.** Confirm whether the owner has a performance and payment bond, a letter of credit, cash, a subcontractor default program, or a parent guaranty, and confirm the penal sum, the obligee, and whether the lender is named or has a dual-obligee rider. Federal thresholds do not transfer to private work: FAR 28.102-1 requires bonds above $150,000 on federal construction contracts and alternative payment protections above $35,000 up to $150,000, furnished before notice to proceed. On private work bonding is a negotiated credit decision
- **Insurance.** In the A201-2017 family the detailed insurance requirements sit in an exhibit to the owner-contractor agreement, not in Article 11, so read both. Confirm builder's risk in at least the initial contract sum, who buys it, deductible allocation, off-site and transit coverage, waiver of subrogation, and whether the lender is loss payee. If a wrap-up is used, confirm sponsorship (OCIP by the owner, CCIP by the contractor), what is enrolled, and that contractors still carry off-site work, excluded operations, and deductibles or retentions, which is where enrollment disputes start
- **Warranty, correction, and disputes.** Separate the one-year correction period (A201 12.2.2.1, running from Substantial Completion, extended for work first performed later, not extended by corrective work) from product warranties assigned at Substantial Completion and from the statute of limitations, and confirm the notice obligation, since failure to give prompt notice can waive the right to require correction. Then confirm owner termination for cause and for convenience and what each pays, suspension rights and the resulting sum and time adjustment, the claims notice period (commonly 21 days from the event or from recognition of the condition), the initial decision maker and their impartiality, and the mediation and binding dispute resolution path and venue
- **Lender provisions.** Standard A201-2017 section 13.2.2 lets the owner assign the contract to a construction lender without the contractor's consent if the lender assumes the owner's rights and obligations, and obliges the contractor to execute the consents reasonably required. Section 5.4 gives the owner a contingent assignment of subcontracts effective only on termination for cause, for subcontracts the owner accepts, subject to the surety's prior rights. Both are frequently deleted by modification. Confirm they survive, and reconcile them to the loan documents with [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md)

### Step 6: Review the Individual Change Order in Three Separate Passes

Never argue price before settling entitlement.

**Pass 1 - Entitlement.** Classify the cause, then confirm the contractor did what the contract required.

| Classification | Cause | Who pays |
|---|---|---|
| Necessary | Latent condition differing from the documents, code change after execution, design error or omission, damage to completed work | Owner, from contingency or from the design team |
| Betterment | Increases net income, reduces long-term operating or maintenance cost, or otherwise enhances value | Owner, if the return justifies it |
| Equivalent | Substitution at equal or better utility, or a price reduction at equal or better utility | Neutral or credit to owner |
| Contractor risk | Scope already in the documents, coordination or means-and-methods failure, unauthorized work, or a change performed without the required notice | Contractor |

Notice is the gate. Confirm written notice within the contract period, that notice preceded performance where the contract requires it, and that no work proceeded on a verbal direction. Under A201 7.1.4 changes made without prior authorization outside an emergency are at contractor risk, and under 7.4 a contractor who performs a minor change without first noticing its cost or time effect waives the adjustment.

**Pass 2 - Pricing.** Price it by the contract's own rules, not by the proposal's format. Test labor hours against the composite rates the contract pre-approves; test material cost against substantiated vendor invoices or quotes; test equipment rental against the contract's threshold and rate schedule; confirm markup against the contract's stated ceilings and that the contractor's markup on subcontracted work is separately capped; confirm deletions are credited at actual net cost and that on a change with both adds and deducts, overhead and profit is computed on the net increase, not the gross add. Confirm the change is not already covered by an allowance, a unit price, or contingency, and confirm whether it draws contingency (which should not raise the GMP) or increases the contract sum (which does).

**Pass 3 - Time.** A time request needs a schedule analysis against the current accepted schedule showing critical path impact, not a stated day count. Determine whether the delay is excusable-only or excusable and compensable, whether it is concurrent with a contractor-caused delay, and whether granting it moves the liquidated damages start date. On bonded work, confirm surety consent before granting a time extension; HUD requires written surety approval for any time-extension change order unless completion assurance is cash or a letter of credit. Track directives separately from change orders: a directive is signed by owner and architect only, the contractor must proceed, price is determined later with interim payment certified in the architect's judgment, and a directive open across multiple draw cycles means the contract sum, the cost to complete, and the schedule are all stale.

### Step 7: Issue the Issues List and Negotiation Positions

Rank every issue by dollar or schedule exposure, not by contract order. For each, state the executed language, the exposure, the requested revision, and the fallback. Separate items that are counsel referrals (indemnity, no-damages-for-delay, lien waiver form sufficiency, enforceability of liquidated damages, insurance adequacy) from items that are commercial negotiation. Then close with a signing recommendation and route the outputs: cost and contingency conclusions to [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md), site condition and permit-driven change causes back to [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md), delivery date and liquidated damages to [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md), and the contract summary, open items, and residual risk to [Development IC Memo Writer](skills/development/development-ic-memo-writer.md).

---

## Output Format

```markdown
# GC Contract and Change Order Review
## Project / Contractor / Form and Delivery Method:
## Contract Sum or GMP / Date:
## Documents Reviewed (and Missing):
## Contract Rating: ACCEPTABLE | ACCEPTABLE WITH REVISIONS | MATERIALLY DEFICIENT | DO NOT SIGN
## Recommendation: SIGN | SIGN AFTER LISTED REVISIONS | RENEGOTIATE | ESCALATE TO COUNSEL

### Price and Exclusions
| Item | Executed Language / Section | Exposure to Owner | Position |
|---|---|---|---|
| GMP assumptions, clarifications, and design completeness at GMP | | | |
| Allowances (scope, selection deadline, overage) and contingency (location, draw approval, reversion) | | | |
| Unit prices with quantity bands, and alternates | | | |
| Cost of the work, fee, general conditions, savings and buyout | | | |

### Time and Delay Damages
| Item | Executed Language / Section | Exposure | Position |
|---|---|---|---|
| Substantial / Final Completion definitions and certification | | | |
| Liquidated damages rate, cap, and apportionment clause | | | |
| Consequential damages waiver vs actual delay exposure; excusable vs compensable delay | | | |

### Payment, Retainage, and Closeout
| Item | Contract | Governing State Law / Lender Rule | Gap |
|---|---|---|---|
| Retainage percentage and step-down | | | |
| Withholding grounds, stored materials, and lien waiver forms | | | |
| Final payment conditions and holdbacks | | | |

### Risk Transfer and Lender Provisions
| Item | Status | Issue | Position |
|---|---|---|---|
| Bonds / LC / cash assurance, penal sum, obligee | | | |
| Builder's risk and liability, including any OCIP / CCIP | | | |
| Warranty, correction period, termination, and dispute resolution | | | |
| Assignment to lender and contingent assignment of subcontracts | | | |

### Change Order Review
| CO / CCD | Description | Entitlement Class | Notice OK? | Requested $ | Supported $ | Funding Source | Days Requested | Days Supported | Disposition |
|---|---|---|---|---|---|---|---|---|---|

- Open unpriced directives, cumulative change orders as a percentage of the original contract sum, and contingency drawn to date vs remaining scope:

### Issues List and Negotiation Positions
| # | Issue | Section | Exposure ($ / days) | Requested Revision | Fallback | Counsel Referral? |
|---|---|---|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every finding quotes the executed language and its section number, and no finding rests on the standard form's text where the document has been modified
- The exhibit stack is complete and reconciled: assumptions and clarifications, schedule of values, unit prices, allowances, alternates, and the insurance and bonds exhibit are all present, and the drawing and specification list the price is based on is identified by set and date
- Allowance, contingency, unit price, and alternate amounts are reconciled to the development budget so nothing is counted twice or missed, and retainage, lien waiver forms, and payment timing are tested against the governing state's law and the lender's requirements, not against habit
- Each change order carries a separate entitlement conclusion, pricing conclusion, and time conclusion, the funding source is identified as contingency, owner change, allowance, or contractor risk, and cumulative changes and open directives are stated as a percentage of the original contract sum
- Counsel and broker referrals are labeled as referrals rather than answered

---

## Red Flags & Dealbreakers

- A GMP set on a materially incomplete design, or an assumptions and clarifications page that excludes scope the owner believes is priced
- Contingency drawn through change orders that also increase the GMP, so the cap is no longer a cap, or contingency with no written draw approval and no reversion to the owner
- Allowances with no defined scope, selection deadline, or statement of who bears overage, or unit prices with no quantity band
- Liquidated damages with no apportionment clause on a project where owner-caused delay is already documented, or a consequential damages waiver paired with a liquidated damages rate far below actual carry and lease-commencement exposure
- Retainage above the governing state's cap, a step-down on bonded work without prior written surety consent, or retainage released before final lien releases and consent of surety
- Notice, claim, and change provisions rewritten to remove the owner's ability to reject a late claim, a course of dealing in which work proceeds on verbal direction and is papered afterward, or construction change directives left unpriced across multiple draw cycles
- Assignment of the contract to the construction lender deleted, contractor consent withheld, or the contingent assignment of subcontracts struck, leaving the lender no path to complete after a default
- Insurance requirements referenced but the exhibit missing, builder's risk below the contract sum, or wrap-up enrollment silent on off-site work, excluded operations, and deductibles
- The contractor has an identity of interest with the ownership entity and pricing, buyout, contingency draws, and retainage release have not been tested at arm's length or disclosed to the lender and equity partner

---

## When Data is Missing

- If the supplementary conditions are missing, do not review the general conditions at all; state that the review cannot proceed and say why. If the GMP amendment's assumptions and clarifications page is missing, treat the GMP as an estimate, not a cap
- If the insurance and bonds exhibit is missing, do not infer coverage from Article 11 alone; show the line as unconfirmed
- If pricing backup for a change order is missing, do not negotiate the number; return it as unsupported and state what backup the contract requires. If a time extension is requested without a schedule analysis, treat the day count as unsupported rather than splitting the difference
- If the governing state's retainage, waiver, or prompt-payment rules are unknown, show the contract term and flag the confirmation as a counsel item rather than assuming a national norm

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Executed agreement, adopted general conditions with all supplementary and special conditions, every exhibit including the GMP amendment and the insurance and bonds exhibit, the baseline schedule, and the loan documents are all in hand, and the governing state's retainage and waiver rules are confirmed |
| MEDIUM | Core agreement and general conditions available, but one exhibit, the schedule, or the loan document reconciliation is missing, or state-law confirmation is pending |
| LOW | Unmodified standard form reviewed, exhibits or supplementary conditions absent, change orders reviewed without backup or schedule analysis, or the form family cannot be identified |

---

## Related Knowledge Bases

- [Construction Contracts and Draw Controls](knowledge/construction-contracts-and-draw-controls.md)
- [Construction Lending Criteria](knowledge/construction-lending-criteria.md)
- [Development Benchmarks](knowledge/development-benchmarks.md)

## Research Basis

- [GC Contract and Change Order Reviewer Research](research/development/gc-contract-and-change-order-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
