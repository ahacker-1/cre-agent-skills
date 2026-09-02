---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Financing Fit

Map a U.S. retail asset to the lender lanes that will actually quote it, find the test that controls proceeds, and specify the structure a lender will require before it closes.

---

## When to Use This Skill

Use this skill when sizing acquisition debt, testing a refinance, planning a bridge or anchor-backfill loan, or reviewing a loan maturity on a grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use retail, pad, or single-tenant net lease (STNL) asset. Use it before calling lenders, so the call starts with a lane and a structure rather than a request.

Retail proceeds are set by lease documents and tenant sales, not by leverage appetite. Anchor term, co-tenancy triggers, go-dark rights, exclusives, percentage rent, and CAM recovery leakage move the loan more than the LTV conversation does.

This skill stops at lane fit and required structure. Building the lender call list is [Lender Outreach](skills/financing/lender-outreach.md), comparing quotes once they arrive is [Quote Comparator](skills/financing/quote-comparator.md), and formalizing the selected quote is [Term Sheet Builder](skills/financing/term-sheet-builder.md).

This is educational decision support, not legal, tax, investment, accounting, or financing advice. Loan documents, carve-out guaranties, cash management agreements, and REA / co-tenancy interpretation are state-law and deal specific and require counsel and a real lender quote.

---

## What You'll Need to Provide

- Property profile: format, total GLA, year built and renovated, market and trade area, anchor identity, whether the anchor leases or owns its tract, and whether a recorded REA / OEA governs the site
- Rent roll with GLA, in-place rent, recovery method, expiration, options, and the anchor and top-five tenant share of GLA and of base rent
- T-12, current-year budget, and the stabilized pro forma, with recoveries, percentage rent, specialty income, and signed-not-open rent broken out separately
- CAM reconciliation history and the billed-to-recoverable gap, plus reported tenant sales and occupancy cost ratios where lease reporting covenants exist
- Co-tenancy, go-dark, exclusive, and kick-out provisions from the lease abstracts, with trigger thresholds, cure periods, and remedies
- Capital plan: TI, LC, anchor demising or box splits, roof, parking lot, and any deferred maintenance from the property condition report
- Existing debt terms if refinancing, the requested loan amount or payoff, purchase price or basis, and sponsor liquidity and CRE track record

---

## Mission

Determine which lender lanes are realistic for this asset, which single test controls proceeds, how much the anchor and co-tenancy exposure cuts the loan in a downside case, and what reserves, cash management, and recourse posture a lender will require. Produce a lane recommendation a sponsor can act on and a structure list a broker can take to market.

---

## Strategy

### Step 1: Classify the Asset's Financeability

Place the asset in one class before any math. The class, not the sponsor's target leverage, determines which lanes are open.

- CORE FINANCEABLE: stabilized, anchor term well beyond loan maturity, healthy shop occupancy, clean recoveries, no near-term co-tenancy trigger.
- SELECTIVE: sound asset with one real story - anchor rollover inside the loan term, a recovery gap, moderate shop vacancy, or a secondary trade area. Needs a relationship lender or structure.
- TRANSITIONAL: anchor backfill, box demising, lease-up, pad splits, redevelopment, or a discounted basis with a plan to execute.
- SPECIAL SITUATION: maturity default, dark anchor, impaired value, or a co-tenancy cascade already in motion.

Format matters to the class. Power centers concentrate release risk in a few boxes; strip and unanchored centers spread it across thin credit; malls and outlets carry percentage rent and occupancy cost exposure; STNL and pad are lease-credit objects, not center-metric objects. Format definitions and anchor GLA share are in [Retail Benchmarks](knowledge/retail-benchmarks.md).

Sector context is directional and dated. The OCC's Semiannual Risk Perspective, Spring 2026 (published 2026-05) states "Retail remains a bright spot. The vacancy rate in retail properties remains low, with little space available for lease in most markets," while warning that CRE refinance risk "merits continued attention." Trepp data reported 2026-08-11 put July 2026 retail CMBS delinquency at 6.96% against 1.13% for industrial, with non-performing balloons accounting for 66% of newly delinquent balances across all property types. Both are true: fundamentals are tight, and maturity is the dominant retail default mode. Neither sizes this loan.

### Step 2: Build the Sizing NOI Before Testing Anything

Every test downstream is only as good as the NOI. Build it from the rent roll and the leases, not from the offering memorandum.

Remove or haircut:

- Percentage rent. Lenders give it no credit toward debt service; the practitioner formulation is "You can spend the percentage rent we just won't let you borrow against it." Check the breakpoint math while you are there - natural breakpoint equals annual minimum rent divided by the percentage rate, and anything else is an artificial breakpoint that will not move with rent steps.
- Specialty, temporary, kiosk, and short-term income, plus signed-not-open rent unless the lease is executed, the space is delivered, and rent commencement falls inside the underwriting period.
- The billed-to-recoverable CAM gap. Caps, base years, admin fee limits, gross leases, and anchor fixed-CAM deals create permanent leakage. Feed the number from [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md).
- Above-market anchor rent where renewal or replacement would reset it down.

Then compute LTV, DSCR, debt yield, and loan constant using [Underwriting Calculations](knowledge/underwriting-calc.md). Run each test twice: on in-place NOI and on the stabilized case. Do not blend them.

### Step 3: Run the Anchor, Co-Tenancy, and Rollover Downside

This is where retail proceeds are actually decided. Do not stop at "the anchor is in place."

Build a downside case in this order:

1. Anchor leaves at expiration or goes dark. Remove anchor rent and its recovery contribution.
2. Every inline lease whose co-tenancy trigger is broken by that event moves to its alternative-rent remedy. Regency Centers' FY2025 Form 10-K describes the variants: a tenant may postpone opening, may close before lease expiration if another tenant closes, or "more commonly, they may allow a tenant to pay reduced levels of rent until a certain number of tenants open their stores."
3. Leases whose cure period lapses without cure exercise termination. Count that GLA as vacant.
4. Add the cost to fix it: anchor demising, TI, LC, and downtime. Regency's FY2025 pro-rata disclosure shows new anchor deals at $17.46 PSF base rent against $28.67 PSF allowance and landlord work plus $4.65 PSF commissions, and new shop deals at $43.16 PSF base rent against $51.12 PSF allowance plus $17.37 PSF commissions, while renewals ran under $1.50 PSF of allowance. Directional, FY2025, and the same table swung materially year over year - size from real deal terms, not from these figures.

Then screen the result against the CREFC Investor Reporting Package v8.4 Servicer Watchlist triggers. These are CMBS surveillance thresholds, not origination limits, but they are the clearest published statement of what institutional lenders treat as trouble, and an asset that would trip several of them on a plausible anchor loss is not a clean permanent-loan candidate.

| Trigger | Threshold | What it tests here |
|---|---|---|
| 1E fixed rate DSCR | NCF DSCR below 1.10x; excludes CTL, co-ops, ground leases, single tenant NNN | Downside coverage floor |
| 1F DSCR vs underwriting | NCF DSCR below 1.40x and below 75% of underwritten DSCR | Whether the stabilized case has room to be wrong |
| 1G floating rate DSCR | DSCR below 1.00x and below 90% of in-place NOI as of underwriting | Bridge sizing |
| 5A maturity | Balloon balance inside 90 days | Exit |
| 4A occupancy decrease | Below 80% of underwritten occupancy (fixed rate); below 90% of in-place tenants (floating) | Practical co-tenancy proxy |
| 4C major tenant rollover | Single tenant or any tenant above 30% of NRA expiring within 12 months for loans >= $30 million, within 6 months below that, or on non-renewal notice | Anchor term vs loan term |
| 4D top-three rollover | Top three tenants each at least 5% of NRA and cumulatively above 30% expiring within 6 months | Concentrated rollover |
| 4E tenant bankruptcy | Same 5% / 30% combination in bankruptcy | Credit event |
| 4F dark or defaulted major tenant | Major tenant above 30% of NRA in default, terminated, or dark | Dark-but-paying anchor |

Anchor and co-tenancy detail should come from [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md), lease terms from [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md), and rollover concentration from [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md).

### Step 4: Match Lender Lanes and Name the Controlling Test

Score each lane LIKELY, CONDITIONAL, or UNLIKELY with a one-line reason. Lane definitions and frictions are in [Retail Lender Criteria](knowledge/retail-lender-criteria.md).

- Relationship bank. Best for local or regional sponsors on necessity retail with deposits on the table. Constraint is often upstream of the asset: OCC Bulletin 2006-46 screens institutions where construction, land, and land development loans reach 100% or more of total risk-based capital, or total CRE reaches 300% or more of capital with 50%+ growth over 36 months. That triggers "further supervisory analysis," not a cap - but it is why a clean center gets declined by a bank that likes it.
- Life company. Best-in-class stabilized product, low leverage, long hold. Availability cannot be assumed: MBA reported (2026-08-06) that Q2 2026 life company originations fell 27% year over year while retail originations overall rose 61%, CMBS rose 68%, and depositories rose 61%.
- CMBS / conduit. Larger stabilized centers with durable in-place cash flow and a defensible anchor. Wrong lane for any plan that needs lender flexibility after close.
- Debt fund / bridge. Anchor backfill, demising, lease-up, pad splits, and discounted basis. Priced for it, with milestones, extension tests, and heavy reserves.
- Credit tenant lease for STNL. PGIM Private Capital's published program offers up to 100% LTV based on the present value of lease obligations, $25 million to $100+ million, and 20+ year maturities for investment grade corporate, not-for-profit, and government tenants, with below investment grade case by case. Both the credit and the lease must qualify. CREFC excludes CTL, ground leases, and single tenant NNN from its DSCR triggers, and excludes fully amortizing CTL loans from the major-tenant-rollover trigger where the lease is co-terminus with the loan - that is the mechanical reason CTL sizes off the lease rather than the property.
- SBA 504 owner-user. Only for an operating business buying its own storefront or pad. The SBA 504 program page sets a maximum of $5 million, or up to $5.5 million for certain projects, and lists among prohibited uses "Speculation or investment in rental real estate." Occupancy percentage thresholds are administered through SBA SOP and the certified development company - confirm with the CDC, do not assume.

Then state which single test controls proceeds. Practitioner-published bands, directional as of 2026-09-01: life company LTV roughly 60%-75%, DSCR roughly 1.25x-1.35x, debt yield roughly 8%-10%; general retail up to about 75% LTV, DSCR about 1.25x to 1.35x. The tightest test governs, and in retail it is frequently sustainable NOI rather than leverage. No published band exists for loan per square foot by retail format - judge it against as-is basis, replacement cost, and local comps, and say so.

### Step 5: Specify Structure, Reserves, and Cash Management

Name the mechanism and its trigger. Do not invent reserve dollar amounts - lenders size reserves to the actual rent roll, lease documents, and property condition report.

- Upfront reserves: TI/LC, replacement, immediate repairs from the PCR, unfunded landlord obligations, and outstanding free rent or gap rent.
- Springing anchor reserve: funds monthly on the earlier of a non-renewal notice, a go-dark event, or a fixed number of months before anchor expiration. This is the standard answer to a CREFC 4C or 4F profile.
- Co-tenancy cure reserve: sized to the alternative-rent exposure of triggered inline leases through the expected cure period.
- Holdbacks and earnouts: proceeds released on signed leases, rent commencement, occupancy, or debt-yield milestones rather than funded at close.
- Cash management: springing lockbox, excess-cash trap, or a letter of credit in lieu. CREFC v8.4 treats "Occurrence of Servicing Trigger Event in the Mortgage Loan Documents (for example: Springing Lockbox, Establishment of LOC, Trap Excess Cash)" as its own watchlist trigger, released on cure or on posting the LOC or lockbox - confirmation these are standard mechanics, not exotic asks. Tie the trigger to a DSCR or debt-yield floor, an anchor event, or both, and say which.
- Recourse posture: case-by-case. Published life company material shows non-recourse, limited recourse, and full recourse all in use, with springing recourse for loan fraud, transfer, or subordinate financing without consent. CMBS and CTL are typically non-recourse with a deal-specific carve-out schedule. State the posture you expect and flag the carve-outs for counsel, along with amortization versus interest-only, extension tests, tenant notice covenants, and anchor estoppel or SNDA delivery conditions.

### Step 6: Test the Exit Before Accepting the Entry

A retail loan that clears today and cannot be refinanced is a maturity default with a delay.

- Re-run DSCR and debt yield at maturity on the projected rent roll, with the anchor at renewal-option rent or at market, whichever is worse, and stress the exit cap above the entry cap against the balloon.
- Confirm the anchor's remaining term at maturity clears a takeout lender's own rollover screen. An anchor expiring within a year of the balloon date is a refinance problem before it is a leasing problem.
- Expect a credit committee to underwrite to a sustainable cash flow below broker NOI and to a value derived from that cash flow. KBRA's published methodology derives value by income capitalization, dividing sustainable net cash flow by a long-term asset-specific cap rate rather than accepting an appraisal.
- If maturity is already the problem, note that the interagency Policy Statement on Prudent CRE Loan Accommodations and Workouts (FIL-23-2023, issued 2023-06-29) tells examiners that modified loans to borrowers able to repay "will not be subject to adverse classification solely because the value of the underlying collateral has declined." That is room for a bank to extend. It is not evidence that the refinance math works, and it is not a substitute for counsel and servicer engagement.

### Step 7: State the Verdict and Hand Off

Give one verdict, the controlling test, the recommended lane, and the structure list. Feed the result to [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md) for the debt schedule and returns, and to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md) for the financing section. Pull trade-area evidence supporting the takeout from [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md).

---

## Output Format

```markdown
# Retail Financing Fit
## Property / Format / GLA:
## Requested Loan / Basis:
## Financeability Class: CORE FINANCEABLE | SELECTIVE | TRANSITIONAL | SPECIAL SITUATION
## Verdict: FINANCEABLE NOW | FINANCEABLE WITH STRUCTURE | BRIDGE / TRANSITIONAL ONLY | NOT FINANCEABLE AT REQUESTED PROCEEDS

### Sizing NOI Build
| Line | Amount | Treatment |
|---|---:|---|
| Broker / T-12 NOI | | |
| Less percentage rent | | No debt-service credit |
| Less specialty / temporary / signed-not-open | | |
| Less CAM recovery leakage | | Billed-to-recoverable gap |
| Sizing NOI | | |

### Sizing Tests
| Test | In-Place | Stabilized | Downside | Controls? |
|---|---:|---:|---:|---|
| LTV | | | | |
| DSCR | | | | |
| Debt yield | | | | |
| Loan PSF | | | | Comp-based, no published band |
| Supportable proceeds | | | | |

### Anchor, Co-Tenancy, and Rollover Exposure
| Item | Finding | Proceeds Impact |
|---|---|---|
| Anchor term vs loan maturity | | |
| Go-dark right | | |
| Co-tenancy triggers exposed | | |
| Top-three rollover inside term | | |
| CREFC triggers tripped in downside | | |
| Cost to cure / backfill | | |

### Lender Lane Fit
| Lane | Fit | Rationale |
|---|---|---|
| Relationship bank | LIKELY / CONDITIONAL / UNLIKELY | |
| Life company | | |
| CMBS / conduit | | |
| Debt fund / bridge | | |
| CTL (STNL only) | | |
| SBA 504 (owner-user only) | | |

**Recommended lane:** | **Controlling test:**

### Required Structure
| Mechanism | Trigger / Condition | Purpose |
|---|---|---|

Recourse posture expected, and carve-outs to review with counsel:

### Exit / Refinance Test
- Maturity DSCR and debt yield, anchor term remaining at maturity, exit cap stress vs balloon

### Key Financing Risks
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Sizing NOI is built explicitly, with percentage rent, specialty income, signed-not-open rent, and CAM leakage removed line by line rather than assumed away
- In-place, stabilized, and downside cases are run separately and never blended
- The downside case runs the full anchor-to-co-tenancy-to-termination chain, not just the anchor rent
- One controlling test is named, not a list of tests that all passed
- Every lane gets a verdict with a reason, including the lanes that are unavailable and why
- Structure is stated as mechanism plus trigger, with no invented reserve dollar amounts, and loan PSF is a comp comparison rather than a benchmark
- Time-sensitive market figures carry their date and source in the text
- Exit is tested at maturity with the anchor at renewal-option or market rent
- CTL is proposed only where both the tenant credit and the lease document qualify; SBA only for an owner-user

---

## Red Flags & Dealbreakers

- Anchor expires before loan maturity with no signed renewal, no reserve, and no backfill plan
- Anchor dark but paying: coverage looks fine, traffic is gone, and co-tenancy cure clocks may already be running
- Anchor rent well below market, so in-place NOI flatters the loan and the renewal or replacement case is punitive
- Co-tenancy triggers concentrated in the best-credit inline leases, so one event cascades through the strongest rent
- Proceeds sized on stabilized NOI while in-place NOI fails coverage, with no reserve or holdback bridging the gap
- Percentage rent, specialty income, or signed-not-open rent carrying the DSCR, or a permanent recovery gap from caps, base years, or anchor fixed-CAM deals left out of sizing NOI
- Site plan, parking, or redevelopment rights controlled by an REA or OEA the borrower does not control, with no lease remedy available
- Exclusives or use restrictions that shrink the realistic backfill pool for the anchor or a major box
- CMBS proposed for an asset whose business plan needs lender flexibility after close
- CTL proposed for a below-investment-grade tenant, a lease shorter than the loan, or a lease with surviving landlord obligations - that is a conventional retail loan wearing an STNL label
- SBA proposed for an investor-owned center: a structural disqualification, not a negotiation point
- Refinance plan that depends on cap-rate compression or lower rates with no backup, or a sponsor without liquidity to fund TI, LC, or anchor demising overruns

---

## When Data is Missing

- No lease abstracts: run the CREFC 4C through 4F screen on the rent roll alone, label proceeds preliminary, and state that co-tenancy exposure is unquantified rather than zero
- No CAM reconciliation: assume a recovery gap exists, model recoveries conservatively, and request three years of reconciliations before calling the deal financeable
- No tenant sales: say so. Occupancy cost headroom cannot be inferred from rent alone, and renewal risk stays unpriced
- No property condition report: reserves are unsized and any reserve figure quoted is a placeholder
- No sponsor liquidity or track record: lane fit for bank and debt fund execution is uncertain regardless of asset quality
- No existing debt terms on a refinance: show proceeds ranges under each lane rather than a single number that reads like a quote
- Never present a rate, spread, or reserve amount as a quote. This skill produces lane fit and structure requirements; only a lender produces terms

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Rent roll, lease abstracts with co-tenancy and anchor terms, T-12 and budget, CAM reconciliations, capital plan, property condition report, and sponsor context are all available and reconciled |
| MEDIUM | Rent roll and financials available, anchor terms known, but co-tenancy detail, CAM reconciliation, tenant sales, or sponsor liquidity is incomplete |
| LOW | Offering-memorandum-level data only, no lease documents, no recovery detail, or anchor and co-tenancy exposure unverified |

---

## Related Knowledge Bases

- [Retail Lender Criteria](knowledge/retail-lender-criteria.md)
- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)
- [Risk Scoring](knowledge/risk-scoring.md)

## Research Basis

- [Retail Financing Fit Research](research/retail/retail-financing-fit-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
