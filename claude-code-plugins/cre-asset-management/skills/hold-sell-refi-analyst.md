# Hold/Sell/Refi Analyst

Compare four mid-hold outcomes — continued Hold, Refinance-and-Hold, Sell-at-Current, and Sell-at-Stabilization — on a side-by-side IRR / Equity-Multiple / cash-to-LP basis, using a Since-Inception XIRR framework that correctly handles partial holding periods, quarterly interim distributions, and refinance cash-out as a distribution event.

---

## When to Use This Skill

Use this skill when:

- A stabilized (or near-stabilized) U.S. multifamily asset has been held ≥ 12 months and the sponsor, LP, or asset manager is evaluating a mid-hold decision (continued hold vs. refinance vs. sell).
- The owner has at least a preliminary current-market valuation (broker BOV, recent comparable sale, or updated cap-rate applied to T-12 NOI) and either (i) an existing loan that is inside its call window or (ii) a live or contemplated refi quote.
- An IRR-to-date and forward-looking scenario set are required as the quantitative backbone of the hold/sell/refi decision — not a qualitative narrative alone.
- An LP quarterly report, investment committee memo, or internal asset-plan review is triggering the re-underwrite.
- The output will feed either an internal IC recommendation OR a brokerage disposition workstream (the `disposition_handoff` block is designed for direct pass-through to the brokerage Broker-Opinion-of-Value / Listing-Proposal-Builder skills).

Do NOT use this skill for:
- Pre-acquisition underwriting (use `skills/underwriting/financial-model-builder.md` or the industrial equivalent).
- Distressed workout / loan-modification workflows (out of scope; requires specialized special-servicer framework).
- NOI-improvement playbooks (see Value-Add / Operating Levers skill).
- REIT portfolio-level roll-up decisions (single-asset only).

---

## What You'll Need to Provide

**Required:**
- Original underwriting model or key assumptions: initial equity contribution(s) with dates, original projected hold period, original exit cap, original base-case IRR and Equity Multiple.
- Actual cash flows to date: each LP distribution with date and amount; each capital call or follow-on equity contribution with date and amount.
- Current market value: either a signed BOV, a recent comparable trade, or T-12 NOI × current-market cap rate (submarket-calibrated per `multifamily-benchmarks.md`).
- Current debt stack: loan balance, coupon, amortization, maturity, IO period remaining, prepayment structure (yield maintenance, defeasance, step-down), any rate cap and strike/expiry on floating-rate paper.
- Trailing 12-month (T-12) NOI and T-3 annualized NOI (for Timing-vs-Permanent gate on the peak-NOI heuristic).

**Strongly preferred:**
- Refi quote if shopped: proposed new loan amount, coupon, amortization/IO, LTV, DSCR, closing costs, recourse posture.
- Forward NOI projection through the balance of the original business plan.
- Waterfall tiers: preferred return rate/structure (cumulative/compounding?), promote-tier IRR hurdles, catch-up, GP carry splits at each tier.
- Tax posture: depreciation taken to date (§1250 unrecaptured gain base), any cost-segregation study and §1245 bucket value, prior §1031 chain history, LP tax status (taxable / tax-exempt / pension).

**Nice to have:**
- LP alternative-yield benchmark (fund target IRR or realistic replacement-asset IRR).
- Portfolio-level NAV share of this asset (for concentration overlay).
- Sponsor fund-life remaining (for forced-sale overlay).

**If missing:** see `## When Data is Missing` — the skill degrades gracefully but confidence drops.

---

## Mission

Produce a rigorous four-scenario hold/sell/refi comparison that (i) correctly measures IRR-to-date using Since-Inception XIRR with marked-to-market NAV, (ii) projects forward IRR and Equity Multiple through a common terminal date for each of Hold, Refi+Hold, Sell-at-Current, and Sell-at-Stabilization, (iii) stress-tests each scenario on exit cap and rate sensitivity, (iv) identifies LP-vs-GP misalignment risk where IRR and Equity Multiple rank scenarios differently, and (v) outputs a recommendation with rationale and a structured `disposition_handoff` block ready to feed the brokerage BOV workflow.

---

## Strategy

### Step 1 — Reconstruct Equity Cash-Flow Ledger (Inception to Today)

Build an explicit dated cash-flow series at the **LP equity** level:

- Each equity contribution as a negative cash flow on its actual date (initial close, subsequent calls).
- Each LP distribution (operating cash flow + refi proceeds if any prior refi occurred) as a positive cash flow on its actual date.
- Measurement date "today" as the cut-off.

This is the raw input for IRR-to-date. Do NOT roll cash flows to year-end — it materially distorts IRR (published 280 bps spread between IRR and XIRR on identical series per Adventures in CRE).

### Step 2 — Compute IRR-to-Date Using SI-IRR with Mark-to-Market NAV

Apply the ILPA-recommended Since-Inception IRR convention:

- Equity contributions = negative cash flows on actual dates.
- Distributions received = positive cash flows on actual dates.
- **Add a simulated terminal proceed at today's date** equal to current NAV = (current market value) − (current debt payoff including any prepayment penalty if relevant) − (estimated sale friction, brokerage + closing, ~2-4%).
- Solve XIRR on the full series. This is IRR-to-date.

Compute Equity Multiple to date = (sum of distributions received + simulated NAV) / (sum of equity contributed).

Also compute realized-only IRR (excluding NAV) as a secondary liquidity metric; expect near-zero or negative on mid-hold.

Cross-reference `knowledge/underwriting-calc.md` Worked Example 5 (IRR) and Worked Example 6 (Equity Multiple) for the formulas — do NOT redefine them here.

### Step 3 — Gate the Peak-NOI Signal (Timing vs. Permanent)

Before treating current NOI as a projection base, classify recent NOI variance using `research/asset-management/_taxonomy-seed.md` §3 buckets:

- Is T-3 annualized NOI converging with T-12? If T-3 materially exceeds T-12 driven by a One-Time event (lump settlement, tax refund, concession burn-off not expected to persist), **do not** treat the implied stabilized NOI as the projection base.
- If the variance is Permanent (structural rent growth or sustained expense control), use the updated run-rate.
- If Timing (seasonal or invoice cadence), use a blended T-12 adjusted toward converged annual run-rate.

Document the classification — the projection base depends on it.

### Step 4 — Project Remaining Cash Flows at Three Exit Timings

Build three forward cash-flow projections from today:

1. **To original-plan exit** (Hold base case): use updated forward NOI from Step 3, remaining contractual rent growth, budgeted CapEx, existing debt service through maturity. Revise exit cap using `multifamily-benchmarks.md` submarket-calibrated ranges + the +25-75 bps expansion rule of thumb over entry cap.
2. **To near-term disposition** (~90-120 days from today): Sell-at-Current scenario. Use current market value net of broker commission (1.0-1.5% institutional / 2.0-3.0% middle-market), closing costs, loan prepayment penalty (yield maintenance or defeasance — 5-15% of outstanding balance on fixed-rate agency is common).
3. **To stabilized sale** (12-24 months forward, only relevant if value-add work remains): complete remaining lease-up / renovation, dispose at projected stabilized-basis pricing. Apply execution risk haircut.

### Step 5 — Evaluate Refinance Cash-Out (Refi+Hold Scenario)

If a refi quote is available OR if market terms can be estimated from the 2024-2026 snapshot in `renewal-economics.md` §9:

- Compute new loan amount at constrained-minimum of: (i) maximum allowed by LTV gate (≤65% for refi-test exemption, ≤75% at stretch), (ii) maximum allowed by DSCR gate (≥1.25x agency floor; ≥1.40x for refi-test exemption; ≥1.55x at ≤55% LTV per Freddie Mac), (iii) debt-yield floor if the lender uses one.
- Compute **DSCR_post-refi = T-12 NOI / New Annual Debt Service.** If result < 1.25x, auto-flag non-financeable at agency (forces life-co/bank alternative with different covenants).
- Compute cash-out proceeds = new loan − old loan payoff (including prepay penalty) − refi closing costs (2-4% of new loan) − any escrow adjustments.
- Treat the net cash-out as a **distribution event on the refi close date** in the forward cash-flow series.
- Project post-refi cash flows at the new (higher, typically) debt service through an extended exit (typically +3-5 years past original plan).
- Compute post-refi IRR and Equity Multiple.

Cross-reference `knowledge/underwriting-calc.md` for DSCR and debt-service formulas; `renewal-economics.md` §7 for refi application rules.

### Step 6 — Build the Four-Scenario Matrix

For each of Hold, Refi+Hold, Sell-at-Current, Sell-at-Stabilization:

- Assemble the full inception-to-terminal XIRR series (actual historical cash flows + projected forward cash flows + terminal proceed).
- Solve XIRR = projected IRR (inception to terminal).
- Compute projected Equity Multiple = total dollars distributed to LP / total equity contributed.
- Compute projected nominal cash return to LP = total distributions (pre-tax, pre-waterfall).
- Compute DSCR_post-refi for Refi+Hold.
- Compute net proceeds at disposition for sell scenarios (gross price − commission − closing − prepay − estimated taxes if not 1031'd).

### Step 7 — Sensitivity Analysis

Mandatory per `renewal-economics.md` §6: no single-point exit cap permitted.

- Exit cap ±50 bps and ±100 bps on every scenario (base, up, up-far, down, down-far).
- Rent-growth ±100 bps on Hold and Refi+Hold.
- Rate ±50 bps on Refi+Hold.
- Lease-up execution haircut (rent premium capture) ±25% on Sell-at-Stabilization if value-add remains.

Report the IRR-swing magnitude — a 100 bps exit-cap swing typically moves IRR ~540 bps on a leveraged 5-year multifamily hold.

### Step 8 — LP vs. GP Alignment Check

- Rank the four scenarios by LP IRR. Rank the four scenarios by LP Equity Multiple. If rankings disagree, flag it explicitly — the disagreement is a direct measure of GP-favorable-but-LP-suboptimal timing.
- Check: is IRR-sell-today within 50-100 bps of a promote-tier hurdle? Test whether small exit-cap or timing changes push across the hurdle. If yes, disclose the structural incentive.
- Compute Equity Multiple spread between top-IRR and top-EM scenarios. Spread > 0.15x is a material misalignment signal.

### Step 9 — Recommendation and Rationale

Apply the decision rule:

- If IRR-sell-today materially exceeds the marginal IRR-of-continuing-to-hold (forward-only IRR on today's net sale proceeds as initial negative + remaining forward CFs + original-plan terminal) by more than ~200 bps AND Equity Multiple ranking agrees → **sell now**.
- If marginal-IRR exceeds LP alternative-yield benchmark AND Refi+Hold produces accretive cash-out at acceptable DSCR AND tax shield of refi > after-tax sale value → **refi and hold**.
- If Sell-at-Stabilization IRR exceeds Sell-at-Current AND execution risk is manageable AND remaining hold ≤ 24 months → **sell at stabilization**.
- Otherwise → **hold** (including when the inversion point favors longer holds — typically 6-8 years for levered value-add).

Document the rationale referencing the specific IRR / EM numbers and the gating heuristics applied.

### Step 10 — Populate Disposition Handoff Block

Whether or not a sale is recommended, populate the `disposition_handoff` block so the downstream brokerage BOV skill has the inputs it needs. This enables one-click pass-through to `skills/brokerage/broker-opinion-of-value-builder.md` when the recommendation is sell.

---

## Worked Example (Partial Holding Period + Quarterly Distributions + Refi Cash-Out)

**Asset:** 180-unit Class B garden, Sun Belt primary market. Acquired 2023-03-15. Today's measurement date: 2026-04-01. Holding period to date: 3.05 years (partial).

**Original underwriting:** 5-year hold (exit 2028-03), $15.0M LP equity at close, projected LP IRR 15.5%, projected EM 1.85x, original exit cap 5.75%.

**Equity cash-flow ledger to date:**

| Date | Event | Amount ($) | Sign |
|---|---|---|---|
| 2023-03-15 | Initial close LP equity | -15,000,000 | Negative |
| 2023-09-30 | Q3-23 distribution | +180,000 | Positive |
| 2023-12-31 | Q4-23 distribution | +225,000 | Positive |
| 2024-03-31 | Q1-24 distribution | +250,000 | Positive |
| 2024-06-30 | Q2-24 distribution | +275,000 | Positive |
| 2024-09-30 | Q3-24 distribution | +300,000 | Positive |
| 2024-12-31 | Q4-24 distribution | +320,000 | Positive |
| 2025-03-31 | Q1-25 distribution | +335,000 | Positive |
| 2025-06-30 | Q2-25 distribution | +350,000 | Positive |
| 2025-09-30 | Q3-25 distribution | +360,000 | Positive |
| 2025-12-31 | Q4-25 distribution | +365,000 | Positive |
| 2026-03-31 | Q1-26 distribution | +370,000 | Positive |
| 2026-04-01 | **Simulated NAV (today)** | +18,500,000 | Positive (terminal proceed) |

Simulated NAV computation: current market value $38.0M (T-12 NOI $2.09M / 5.50% current cap) − loan payoff $19.2M − prepay penalty $0.3M (step-down still in effect at year 3) = $18.5M net LP proceeds if sold today.

**IRR-to-date (XIRR on full series):** 14.8%. Realized-only IRR (ex-NAV): negative — only $3.33M distributed vs. $15M contributed. Equity Multiple to date = (3.33 + 18.5) / 15.0 = **1.45x** (including NAV).

**Key observation — partial holding period handling:** IRR-to-date of 14.8% is below the original 15.5% underwrite but above the mid-hold marginal benchmark (typically 12-13% for Class B Sun Belt stabilized). The fact that realized-only IRR is negative is mechanical (mid-hold) and is not a decision signal — only the SI-IRR with NAV is decision-relevant.

**Refi cash-out as distribution event — modeling the Refi+Hold scenario:**

Assume refi on 2026-07-01 at new loan $24.5M (65% LTV on $37.7M conservative refi value), 10-yr fixed at 5.85%, 30-yr amortization, 2 years IO. Old loan payoff $19.0M + $0.2M prepay + closing costs $0.6M (2.4% of new loan) = $19.8M uses. Net cash-out = $24.5M − $19.8M = $4.7M distribution to LP on 2026-07-01.

Post-refi annual debt service ≈ $24.5M × 5.85% = $1.43M IO (then $1.74M P+I from year 3). T-12 NOI $2.09M → DSCR_post-refi = 2.09 / 1.43 = **1.46x** (clears the 1.40x refi-test bar; acceptable at agency).

The Refi+Hold scenario adds the $4.7M distribution at 2026-07-01, projects the post-refi levered CFs through an extended exit at 2030-03 (+2 years past original plan) at a revised 6.00% exit cap. Solving XIRR on the full inception-to-2030 series yields projected LP IRR 16.2% and EM 2.05x — a ~140 bps IRR lift and 0.20x EM lift over the Hold base case's 15.1% / 1.85x projection, driven primarily by (a) the earlier partial return of capital via cash-out and (b) the extra 2 years of compounding on trapped equity.

**Why this matters for the decision:** The Refi+Hold ranks #1 on both IRR and EM in this example — a rare no-misalignment case. If the Refi+Hold had ranked #1 on IRR but #2 on EM (or vice versa), the skill would flag an LP-vs-GP incentive spread.

### Second Case (Sell-at-Stabilization vs. Sell-at-Current with Partial-Period XIRR)

Same asset, same measurement date. The value-add plan originally called for interior renovations on 90 of 180 units at a $9,500/unit premium-finish package driving $175/unit/month rent premium. As of 2026-04-01, 62 of 90 are complete (69% through CapEx). Remaining 28 units are scheduled to be turned and renovated over the next 10 months at $1.05M of remaining CapEx (averaging $37.5k/unit fully-loaded).

**Sell-at-Current scenario:**

- Gross price: $38.0M (current market value per Step 1 input).
- Broker commission (middle-market): 2.25% = $855k.
- Closing costs: $150k (title, transfer, legal).
- Prepay penalty on existing loan: $300k (step-down tier 3).
- Estimated §1250 unrecaptured-gain tax (25% federal × ~$4.0M depreciation taken): $1.0M. (Pre-tax presentation also shown per `## When Data is Missing` item 5 if tax posture not confirmed.)
- Net LP proceeds at 2026-06-30 close: $38.0M − $0.855M − $0.150M − $0.300M − $19.2M loan − $1.0M tax = $16.495M.
- XIRR series: historical cash flows (Step 1 ledger) + terminal $16.495M at 2026-06-30. XIRR = **13.1%** after-tax (14.6% pre-tax). EM after-tax = (3.33 + 16.495) / 15.0 = **1.32x**.

**Sell-at-Stabilization scenario (exit 2027-02-01, ~10 months forward):**

- Complete remaining 28 unit renovations over months 1-10; lease-up absorbed over months 3-11 assuming +4 units/month absorption (consistent with comp-set). Incremental rent roll-in: 28 units × $175 × ~50% average lease-up weighting = ~$29k/month incremental rent by month 8+.
- Stabilized T-12 forward NOI at 2027-02: $2.28M (vs. current T-12 $2.09M — $190k of contractual roll-in, net of concession burn).
- Exit cap 5.65% (25 bps tighter than current 5.50% stressed case due to stabilized risk profile — but per the mandatory sensitivity, model also tests 5.50% and 5.85%).
- Gross stabilized price: $2.28M / 5.65% = $40.35M.
- Remaining CapEx spend (uses): $1.05M over months 1-10.
- Incremental CFADS during lease-up: roughly break-even (added NOI offset by concession burn and partial-occupancy drag).
- Net LP proceeds at 2027-02-01 close: $40.35M − $40.35M × 2.25% broker − $0.15M closing − $0.10M prepay (step-down tier 4) − $19.0M loan (slight amortization) − $1.05M remaining CapEx − $1.1M est. §1250 tax = $18.04M net to LP.
- XIRR series: historical ledger + three additional projected quarterly distributions at ~$0/quarter during lease-up + terminal $18.04M at 2027-02-01. XIRR = **14.2%** after-tax. EM after-tax = (3.33 + 18.04) / 15.0 = **1.42x**.

**Decision read:** Sell-at-Stabilization beats Sell-at-Current on both IRR (14.2% vs. 13.1%) and EM (1.42x vs. 1.32x). The marginal IRR on the ~$16.5M of trapped capital from today (2026-04) to the stabilized sale (2027-02) is roughly 18% — comfortably above a realistic LP alternative-yield benchmark. The **only** case for Sell-at-Current here is if execution risk on the remaining 28 renovations is elevated (e.g., GC availability, supply-chain issues). The sensitivity test applies a −25% rent-premium capture haircut to stress this: at 75% premium capture, Sell-at-Stabilization IRR falls to 13.6%, narrowing the spread but still above Sell-at-Current.

**What this case demonstrates:**
- **Partial holding period:** XIRR handles the 3.05-year historical + 0.83-year forward (3.88 years total to Sell-at-Stabilization) with zero discontinuity. Rolling to year-end would misrepresent the forward 0.83-year segment by ~200 bps.
- **Interim distributions at non-anniversary dates:** Each quarterly historical distribution (2023-09-30, 2023-12-31, 2024-03-31, …) sits on its own actual date. The XIRR function weights each appropriately. No distribution was forced to a year-end.
- **Refi cash-out as distribution event:** From the Refi+Hold walk in the first case, the $4.7M net refi proceeds on 2026-07-01 enters the forward XIRR series as a positive cash flow on that specific date — not rolled to year-end, not netted against anything. It is a true interim distribution event, and the XIRR mechanically compounds both the early partial return of capital AND the later terminal proceed.

---

## Output Format

```markdown
# Hold/Sell/Refi Analysis
## Property:
## Measurement Date:
## Status: RECOMMEND HOLD | RECOMMEND REFI+HOLD | RECOMMEND SELL NOW | RECOMMEND SELL AT STABILIZATION
## Confidence Level: HIGH | MEDIUM | LOW

---

### Position Snapshot
- Acquired:
- Hold Period to Date (years):
- Original Underwrite IRR / EM:
- Current Loan (balance, coupon, maturity, prepay structure):
- Current Market Value:
- Current NAV to LP (value − debt payoff − prepay − friction):

### Realized Performance (Inception to Measurement Date)
- SI-IRR (XIRR with MTM NAV): %
- Realized-Only IRR (ex-NAV): %
- Equity Multiple to Date (incl. NAV): x
- Total Distributions to LP to Date: $
- T-12 NOI: $
- T-3 Annualized NOI: $
- NOI Variance Classification (Timing / Permanent / One-Time):

### 4-Scenario Matrix

| Scenario | Projected IRR | Projected EM | Nominal Cash to LP | Terminal Date | Key Risk |
|---|---|---|---|---|---|
| Hold (base case) | % | x | $ | | Exit cap sensitivity |
| Refi + Hold | % | x | $ | | Rate + exit cap; DSCR_post-refi = x |
| Sell at Current | % | x | $ | | Prepay penalty; tax leakage |
| Sell at Stabilization | % | x | $ | | Execution risk on remaining value-add |

- Ranking by IRR:
- Ranking by Equity Multiple:
- **LP vs. GP Alignment Flag:** [AGREE / DISAGREE — if disagree, quantify the spread]

### Sensitivity Analysis

**Exit Cap Sensitivity (IRR)**

| Scenario | −100 bps | −50 bps | Base | +50 bps | +100 bps |
|---|---|---|---|---|---|
| Hold | | | | | |
| Refi + Hold | | | | | |
| Sell at Stabilization | | | | | |

**Rate Sensitivity (Refi + Hold only)**

| | −50 bps | Base | +50 bps |
|---|---|---|---|
| IRR | | | |
| DSCR_post-refi | | | |
| Cash-out proceeds | | | |

### Recommendation & Rationale

[Two to four paragraphs. Reference the specific IRR / EM numbers, the marginal-IRR-of-continuing-to-hold vs. alternative-yield benchmark, tax posture, LP liquidity posture, and any gating heuristic (peak-NOI classification, fund-life trigger, concentration overlay). If LP-vs-GP misalignment flag is triggered, disclose.]

### Red Flags Raised
- …

### Disposition Handoff (if sell recommended — feeds brokerage BOV skill)
- As-Is T-12 NOI:
- Stabilized NOI (if value-add remains):
- CapEx Completed to Date:
- Remaining CapEx to Stabilize:
- Suggested Pricing Range (Low / High):
- Deal Story (1-2 sentences for marketing narrative):
```

---

## Quality Checks

1. **XIRR dates used — not year-end rollups.** Every distribution carries its actual date. If dates were unavailable and end-of-quarter was used as a fallback, the assumption is explicitly disclosed. The published 280 bps IRR/XIRR spread on identical series makes date accuracy non-optional.
2. **Simulated NAV is net, not gross.** The terminal proceed in the SI-IRR series = current market value MINUS loan payoff MINUS prepay penalty MINUS sale friction. A gross-NAV error inflates IRR-to-date by 100-300 bps.
3. **Exit cap sensitivity is mandatory on every scenario.** Base case + ±50 bps + ±100 bps, not a single-point output. A 100 bps cap swing typically moves IRR ~540 bps.
4. **DSCR_post-refi clears agency floor (≥1.25x) OR the skill flags non-financeable.** Any DSCR result below 1.25x is auto-flagged as requiring life-co/bank alternative with different covenants — not silently presented as an agency-executable refi.
5. **IRR and Equity Multiple are both computed for every scenario.** Rankings are compared. Any disagreement is flagged — it is a direct measure of LP-vs-GP promote misalignment.
6. **Prepayment penalty is modeled explicitly on sell and refi scenarios.** Yield maintenance / defeasance on fixed-rate agency is typically 5-15% of outstanding balance. Silent omission is one of the most common modeling errors.
7. **Peak-NOI is gated by Timing-vs-Permanent classification.** Sell-at-Current and Sell-at-Stabilization projections that assume current NOI is the run-rate must pass the variance check in `_taxonomy-seed.md` §3.

---

## Red Flags & Dealbreakers

1. **Distressed refi signal.** Computed DSCR at 75% LTV prevailing-rate debt < 1.10x. This is not a refi opportunity — it is a distress signal. The skill must auto-flag and pivot to sell-or-modify analysis; the Refi+Hold scenario is mathematically dominated.
2. **Waterfall-hurdle-just-cleared with misaligned rankings.** IRR-sell-today within 50-100 bps of a promote-tier hurdle AND IRR-marginal-hold only 100-200 bps below IRR-sell-today AND Equity Multiple ranking favors hold over sell. Structural GP incentive to sell that does NOT align with LP dollar-return optimum. Disclose explicitly.
3. **Expiring rate cap on floating-rate debt within 12 months.** A meaningfully in-the-money cap with ≤12 months remaining can fundamentally reset debt service — 100-300 bps overnight spike post-expiration is common. Any analysis that ignores cap expiry and strike is incomplete; flag as dealbreaker if the skill cannot ingest that data.
4. **Prior §1031 chain within trailing 2 years + non-§1031 sale contemplated.** Deep §1031 chains create 60-70% effective tax rates on non-exchange sales because both current and previously-deferred gains recognize. After-tax IRR on Sell scenarios must reflect this; if it does not, after-tax rankings are wrong.
5. **Cost-segregation / §1245 recapture exposure not disclosed.** If the owner ran cost seg and is pursuing a non-§1245-matched 1031, ordinary-rate recapture up to 37% can trigger even on an otherwise perfect §1250 exchange. Skill must require disclosure in intake — silent non-disclosure is a dealbreaker for after-tax math.
6. **LP fund-life expiration within analysis horizon.** Fund mechanics may force sale regardless of IRR math (extension fees, LP consent friction). If the fund is within 18 months of stated termination, the decision is constrained — IRR-sell-today vs. IRR-marginal-hold is informational, not dispositive.

---

## When Data is Missing

1. **Missing distribution dates.** Fall back to end-of-quarter as a convention for each missing date. Flag the assumption and reduce confidence to MEDIUM. Note that the fallback can shift IRR by 30-150 bps vs. true-date XIRR; the result is directionally correct but precision is degraded.
2. **Missing current market value (no BOV, no comps).** Derive from T-12 NOI × submarket-calibrated cap rate per `multifamily-benchmarks.md`. Flag the assumption. Widen the exit-cap sensitivity range to ±100 bps and ±200 bps (vs. the default ±50/±100) to surface the uncertainty. Confidence drops to MEDIUM or LOW depending on market depth.
3. **Missing refi quote.** Estimate terms from `renewal-economics.md` §9 snapshot (agency low-to-mid 5% all-in, 5.7-6.8% on 10-year fixed depending on leverage/coverage). Flag the estimate. Hold the DSCR and LTV gates firm (do not loosen to make the refi pencil). If the estimated terms produce DSCR < 1.25x, auto-flag non-financeable. Confidence on the Refi+Hold scenario drops to MEDIUM.
4. **Missing waterfall structure.** Report LP-level IRR and EM without promote allocation. Flag that GP/LP split is not modeled and disclose that the LP-vs-GP alignment check (Step 8) cannot be run. Confidence on recommendation remains reliable for the LP-level numbers but the misalignment flag is unavailable.
5. **Missing tax posture (depreciation, prior §1031, cost seg).** Present pre-tax IRR only for sell scenarios. Require disclosure in the output that after-tax math is not computed and that qualified CPA / tax counsel engagement is required before execution. Do not guess tax figures — the range of plausible effective rates is too wide (25% flat §1250 baseline up to 60-70% on §1031-chain sales) to present a defensible number.
6. **Missing prepayment penalty structure.** Assume mid-point of yield-maintenance / defeasance range (10% of outstanding balance on fixed-rate agency) as placeholder. Flag the assumption. The prepay figure can materially shift Sell-at-Current net proceeds; confidence drops to MEDIUM on that scenario until the actual structure is confirmed from loan docs.
7. **Missing forward NOI projection.** Extrapolate from T-12 using submarket rent-growth and expense-growth defaults from `multifamily-benchmarks.md` calibrated to current market tone. Cap growth rate at 4% nominal unless a Permanent variance classification justifies higher. Flag the projection method and reduce Hold and Refi+Hold confidence to MEDIUM.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Actual distribution dates; signed BOV or recent comp-backed market value; live refi quote; full loan docs reviewed (prepay, cap details); forward NOI available; waterfall and tax posture documented. |
| MEDIUM | Some fallbacks applied (EOQ dates, NOI × cap valuation, estimated refi terms, mid-point prepay assumption) but no dealbreakers. Sensitivity ranges widened to surface the uncertainty. |
| LOW | Multiple fallbacks OR missing forward NOI OR undisclosed tax/§1031 chain history OR expiring rate cap with incomplete data. Recommendation is directional only; a follow-up with full data is required before execution. |

---

## Related Knowledge Bases

- [Renewal Economics & Hold/Sell/Refi Decision Frameworks](../knowledge/renewal-economics.md) — primary: Sections 6 (Hold Period Analytics), 7 (Refinance Economics), 8 (Disposition Timing), 9 (Capital Markets Snapshot)
- [Underwriting Calculations](../knowledge/underwriting-calc.md) — IRR (Worked Example 5), Equity Multiple (Worked Example 6), DSCR, debt-service, cap-rate formulas (cross-reference; do not redefine)
- [Multifamily Benchmarks](../knowledge/multifamily-benchmarks.md) — cap-rate ranges, submarket adjustments for exit-cap derivation, OpEx benchmarks for forward-NOI extrapolation

---

## Structured Output

```json
{
  "skill": "hold-sell-refi-analyst",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "hold_period_years_to_date": 0,
    "irr_to_date": 0,
    "equity_multiple_to_date": 0,
    "scenarios": {
      "hold": { "projected_irr": 0, "projected_em": 0, "nominal_cash_return": 0 },
      "refi_and_hold": { "projected_irr": 0, "projected_em": 0, "cash_out_proceeds": 0 },
      "sell_at_current": { "projected_irr": 0, "projected_em": 0, "net_proceeds": 0 },
      "sell_at_stabilization": { "projected_irr": 0, "projected_em": 0, "net_proceeds": 0 }
    },
    "recommendation": "hold | refi_and_hold | sell_now | sell_at_stabilization",
    "recommendation_rationale": ""
  },
  "uncertainty_flags": [],
  "red_flags": [],
  "disposition_handoff": {
    "as_is_noi_trailing": 0,
    "stabilized_noi": 0,
    "capex_completed": 0,
    "capex_remaining": 0,
    "suggested_pricing_range_low": 0,
    "suggested_pricing_range_high": 0,
    "deal_story": ""
  }
}
```
