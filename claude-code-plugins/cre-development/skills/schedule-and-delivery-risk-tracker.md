---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Schedule and Delivery Risk Tracker

Track a development schedule from entitlement through certificate of occupancy, test the delivery date against the loan and the lease-up plan, price the delay, and produce a risk-rated milestone table with a recovery plan.

---

## When to Use This Skill

Use this skill during construction and lease-up when someone needs to know whether the project will deliver on time, what a slip costs per month, and whether the delivery date still clears the construction loan maturity, the extension tests, the interest reserve, and any pre-leasing delivery obligations. It is written for the owner, development manager, owner representative, construction lender, and equity partner view, not for the contractor's internal planning. For a renovation capital plan on an asset already owned and operating, use [CapEx & Value-Add Execution Tracker](skills/asset-management/capex-value-add-execution-tracker.md) instead; this skill covers the ground-up and heavy-redevelopment schedule from entitlement through certificate of occupancy.

This is educational decision support, not legal, tax, investment, accounting, or financing advice. Delay entitlement, concurrency, and damages are contract and counsel questions.

---

## What You'll Need to Provide

- Current CPM schedule and the accepted baseline, with the data date on each, plus the monthly narrative, update log, and any recovery or rebaseline history
- Entitlement approvals, permit status, and outstanding conditions of approval, from [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md) or the local record
- Procurement and submittal log: long-lead equipment ordered, confirmed delivery dates, substitutions
- Owner-contractor agreement schedule terms read through [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md): contract time, substantial completion definition, liquidated damages, float ownership, weather allowance, notice periods
- Change order and construction change directive log with time impact requested and granted, and measured percent complete from [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md)
- Construction loan terms from [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md): maturity, extension options and their tests, completion outside date, interest reserve balance and burn, rate cap expiry
- Lease-up or sales plan, signed pre-leases with delivery and outside dates, and the stabilization definition in use
- Third-party inspector reports and the local inspection and certificate-of-occupancy sequence
- Business question: monthly owner reporting, lender monitoring, equity partner update, recovery decision, or extension request

---

## Mission

Convert the current schedule into a defensible delivery forecast, identify which milestones actually control that forecast, test the forecast against every date the money depends on, quantify the monthly cost of slipping, and state what recovery would take.

---

## Strategy

### Step 1: Build the Milestone Spine and Test Whether the Schedule Is Usable

Lay out the controlling milestones in order and record baseline date, current forecast date, and variance in weeks for each: entitlement approval, permit issuance, notice to proceed, foundation complete, structure topped out or dry-in, MEP rough-in complete, life-safety and elevator acceptance, temporary certificate of occupancy, certificate of occupancy, first unit or suite delivery, substantial completion, final completion, stabilization.

Before using the schedule, test it against the four characteristics in the GAO Schedule Assessment Guide (GAO-16-89G, December 2015): comprehensive, well-constructed, credible, controlled. Reject the schedule as a control document and say so if any of these are true:

- No accepted baseline exists, or the baseline has been silently replaced rather than formally rebaselined
- Activities have open-ended logic beyond the first and last, or the schedule was never statused with actual start and finish dates against the current data date
- No schedule risk analysis has been run and the reported finish is a single deterministic date

State the schedule variance against the accepted baseline. GSA's P-120 policy (PBS 1000.6B, November 7, 2022) requires a written explanation for variance over 15 percent; adopt that as the reporting trigger.

### Step 2: Test the Critical Path and the Float

The critical path is the longest path through the network. Confirm it is a plausible physical sequence, not an artifact of constraints.

- List the current critical path activities and the total float on each controlling milestone as of the data date
- Set and state a near-critical float band for this project. GAO rejects a universal target such as a fixed number of days or a percentage of duration, and illustrates 5 days on a short schedule versus 2 to 3 months on a multiyear program. Pick one, say why, and track everything inside it
- Question every activity showing negative float, which almost always means a constraint, missing logic, or an unrealistic sequence. If it cannot be mitigated, move the forecast milestone to eliminate it rather than reporting a constrained date. Question unreasonably high total float too; it usually indicates invalid logic rather than real flexibility
- Confirm who owns float under the executed contract. The reference position in federal specifications and in the AIA A201 text reviewed is that float belongs to the project and no party may claim loss of it; negotiated agreements often differ, and the answer decides who pays for a delay
- Report a deterministic finish and a risk-adjusted finish. Where a schedule risk analysis exists, state the percentile; prefer the 80th percentile as the committed date, since GAO notes the 55th and 65th are less certain against a right-skewed distribution. Schedule contingency is the gap between the deterministic finish and the committed date

### Step 3: Test Procurement, Weather, Labor, and Inspection Dependencies

- Procurement: for each long-lead item, record order date, confirmed ship date, need date from the schedule, and float. Do not use published or remembered lead times; use the purchase order, the vendor confirmation, and the submittal log. A substitution or a value-engineering decision resets the clock. Turner's Q2 2026 index commentary emphasizes early procurement precisely because this is where schedules break
- Weather: confirm the schedule already carries a weather calendar or an equivalent allowance for anticipated adverse weather. Under the A201 text reviewed, contract time is presumed to account for average local weather, and a weather claim requires data showing conditions were abnormal for the period, could not reasonably have been anticipated, and actually affected scheduled work. Federal practice treats only unusually severe weather as excusable
- Labor: identify the trades that control the current critical path and whether they are staffed. Skilled mechanical and electrical labor availability was named the industry's biggest challenge in Turner's Q2 2026 commentary, and Cumming Group reported construction labor costs up 3.7 percent year over year as of June 2025 with shortages expected to lengthen timelines. Both are directional and dated
- Inspections and occupancy: map the local inspection sequence and the certificate-of-occupancy path. Occupancy is prohibited until the building official issues the certificate; a temporary certificate can cover portions that can be occupied safely, and a certificate can be suspended or revoked if issued in error or on incorrect information. Treat a temporary certificate as a conditional date, never as delivery

### Step 4: Test the Delivery Date Against Every Date the Money Depends On

Compare the risk-adjusted delivery and stabilization dates to:

- Construction loan maturity, each extension option, and the specific test that unlocks each extension, such as completion by an outside date, a minimum debt service coverage or debt yield, minimum leasing, or an extension fee
- The completion date set in the building and loan agreement, which FDIC examination procedures expect to exist
- Interest reserve runway in months, calculated as remaining funded reserve divided by projected monthly interest at the current rate and projected balance. The OCC handbook requires the reserve to cover interest through anticipated completion and lease-up, sale, or occupancy, applies project cash flow to interest before reserve draws during lease-up, and treats repacking a depleted reserve with new loan proceeds as a red flag of credit deterioration
- Rate cap or hedge expiry and replacement cost at current pricing, and pre-lease delivery obligations: tenant delivery dates, abatement triggers, and outside dates carrying termination rights, which often bind earlier than the loan does
- The lease-up plan from [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md): first units or suites available, absorption pace assumed, and the stabilization definition. State whether stabilization means 90 percent occupancy, a one-year backstop after completion, or both, since AvalonBay defines it as the earlier of the two and comparisons break without it
- Market timing: a slip delivers into a different market. CBRE reported Q2 2026 multifamily completions of 77,700 units, down 14 percent year over year, against 167,000 units of net absorption, with vacancy at 4.3 percent and rent growth of 0.5 percent year over year. Directional as of that date only

### Step 5: Price the Delay

Compute a monthly delay cost and multiply by the risk-adjusted slip. Monthly delay cost = interest carry on projected average outstanding balance + real estate taxes and insurance + site general conditions and owner staffing + contractor extended general conditions if owed + escalation on unbought scope + foregone net operating income from delayed rent commencement + extension fee and rate cap replacement amortized over the delay - liquidated damages actually collectible. Pull the carry, escalation, and contingency lines from [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md).

Two rules on the last term. Do not assume delay damages are recoverable from the contractor: the A201 text reviewed carries a mutual waiver of consequential damages under which the owner waives rental expense, loss of use, income, profit, and financing, which is why liquidated damages are usually the only monetary schedule remedy. Count liquidated damages only where the clause applies to this milestone, the delay is not owner-caused, and no apportionment or concurrency issue is open.

Then state the funding answer plainly: which line pays for the delay, whether contingency and reserves cover it, and what the equity or guarantor call is if they do not.

### Step 6: Rate Each Milestone and Build the Recovery Plan

Rate every controlling milestone ON TRACK, WATCH, AT RISK, or CRITICAL using total float against the near-critical band, forecast variance versus baseline, and whether the constraint is inside the team's control. Then build recovery:

- A recovery plan must name the resource, sequence, or scope change that produces the recovery: added crews, added shifts or workdays, resequencing, early release of a work package, or descoping
- Reject any recovery that comes from revising logic, adding constraints, shortening durations, or changing calendars. Federal specification language prohibits artificially improving progress, and it is the most common way a slip is hidden
- Price the recovery against the monthly delay cost. Acceleration that costs more than the delay it avoids is not recovery, it is a transfer
- Identify which delays, if any, support a time extension request. The federal test is that the delay must consume all available project float and push the finish milestone past the contract completion date; use the contract's own notice period and prepare a fragnet-based prospective time impact analysis
- Where owner-caused and contractor-caused delay overlap, flag concurrency and stop. Do not allocate fault

Hand the verdict, milestone table, and recovery plan to [Development IC Memo Writer](skills/development/development-ic-memo-writer.md) for partner or committee reporting.

---

## Output Format

```markdown
# Schedule and Delivery Risk Report
## Project:
## Data Date / Baseline Date:
## Verdict: ON SCHEDULE | AT RISK | DELAYED - RECOVERABLE | DELAYED - MATERIAL

### Delivery Forecast
| Item | Baseline | Current Forecast | Risk-Adjusted | Variance (weeks) |
|---|---|---|---|---|
| Certificate of occupancy | | | | |
| Substantial completion | | | | |
| First delivery | | | | |
| Stabilization | | | | |

Risk-adjusted basis: schedule risk analysis at __ percentile, or judgment overlay (state which). Near-critical float band used: __ working days (state why).

### Milestone Risk Table
| Milestone | Forecast | Total Float | On Critical Path? | Rating | Driver |
|---|---|---|---|---|---|

### Dependency Exposure
| Dependency | Status | Need Date | Confirmed Date | Float | Note |
|---|---|---|---|---|---|
| Long-lead equipment | | | | | |
| Permits and conditions | | | | | |
| Inspections / TCO / CO | | | | | |
| Critical trade staffing | | | | | |

### Money Tests
| Test | Date or Threshold | Forecast | Pass / Fail | Cushion |
|---|---|---|---|---|
| Loan maturity | | | | |
| Extension test | | | | |
| Interest reserve runway | | | | |
| Rate cap expiry and pre-lease delivery dates | | | | |
| Stabilization assumption | | | | |

### Delay Cost
| Component | $ per Month | Basis |
|---|---|---|
| Interest carry | | |
| Taxes and insurance | | |
| Site general conditions, owner staffing, extended GC conditions | | |
| Escalation on unbought scope | | |
| Foregone NOI | | |
| Extension fee and rate cap replacement, less collectible LDs | | |
| **Net monthly delay cost** | | |

Exposure at risk-adjusted slip of __ months: $__

### Recovery Plan
| Action | Milestone Recovered | Weeks Recovered | Cost | Owner | By When |
|---|---|---|---|---|---|

### Open Items and Notice Deadlines
| Item | Contract Basis | Notice Deadline | Status |
|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Baseline and current schedule are compared at stated data dates, not against a memory of the plan
- The critical path is the longest path and is physically plausible, not constraint-driven
- Total float is reported per controlling milestone, the near-critical band is stated rather than assumed, and negative float is explained or resolved by moving the forecast date
- The risk-adjusted date states its basis and percentile, or admits there is none
- Long-lead items are supported by purchase orders and vendor confirmations, not generic lead times
- Certificate-of-occupancy path and any temporary certificate conditions are separated from construction completion
- Every money test is run against the risk-adjusted date, not the contractor's date
- Delay cost is built line by line, does not assume recovery from the contractor, and every recovery action is physical, priced, owned, and dated

---

## Red Flags & Dealbreakers

- Finish date unchanged for multiple updates while activities slip, which means float is being consumed silently
- Recovery achieved by changing logic, durations, constraints, or calendars rather than by adding resources or resequencing, or a schedule rebaselined without documented approval
- Negative float carried on the certificate-of-occupancy or substantial completion milestone while the project is reported on track
- Long-lead equipment shown as ordered with no confirmed ship date, or a substitution made after order without a schedule impact analysis
- Construction change directives open and unpriced across draw cycles, leaving both the cost to complete and the time impact stale
- Interest reserve runway shorter than remaining construction plus lease-up, or a reserve refunded or repacked with loan proceeds
- Loan maturity or the last extension option falling before the risk-adjusted stabilization date, or an extension test the project cannot meet treated in the model as automatic
- A tenant delivery outside date inside the risk-adjusted delivery window, with a termination or abatement right attached
- Weather claim asserted with no weather calendar in the baseline and no abnormality data
- Concurrent owner-caused and contractor-caused delay being netted to zero by either side without analysis
- Temporary certificate of occupancy treated as delivery when it carries open conditions or an expiration

---

## When Data is Missing

- If there is no accepted baseline, say the project has no schedule control document and report variance only against the earliest defensible schedule, labeled as such
- If the schedule has not been statused, do not compute float; report the gap and request an updated schedule with actual dates
- If no schedule risk analysis exists, present the deterministic date plus an explicit judgment overlay and label the delivery date unvalidated
- If procurement confirmations are missing, treat the affected items as unconfirmed with unknown float rather than assuming the schedule date holds
- If loan documents are unavailable, list maturity, extension tests, and completion covenants as unknown and do not assume an extension is available
- If contract schedule terms are unavailable, state that float ownership, notice periods, and liquidated damages are unknown and price delay with no damages offset
- If the local inspection and occupancy sequence is unknown, flag it as an open dependency; it is the last thing standing between construction and revenue

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Accepted baseline plus a statused current schedule, a schedule risk analysis, confirmed procurement dates, loan documents, and signed leases are all available and reconciled |
| MEDIUM | Statused schedule and loan terms are available, but the risk-adjusted date rests on judgment or one major dependency is unconfirmed |
| LOW | No accepted baseline, an unstatused or narrative-only schedule, or missing loan and contract terms |

---

## Related Knowledge Bases

- [Development Benchmarks](knowledge/development-benchmarks.md)
- [Construction Contracts and Draw Controls](knowledge/construction-contracts-and-draw-controls.md)

## Research Basis

- [Schedule and Delivery Risk Tracker Research](research/development/schedule-and-delivery-risk-tracker-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
