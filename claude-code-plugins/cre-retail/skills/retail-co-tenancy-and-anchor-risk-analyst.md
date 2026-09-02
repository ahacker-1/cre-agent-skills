---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Co-Tenancy and Anchor Risk Analyst

Map every anchor and every co-tenancy clause at a U.S. retail center, model the dark-anchor cascade, test the REA for re-tenanting restrictions, and produce an anchor risk rating with a mitigation plan.

---

## When to Use This Skill

Use this skill during acquisition diligence, refinancing, asset management, or a watch-list review of a multi-tenant U.S. retail asset when an anchor is dark, expiring, in bankruptcy, rumored to close, or simply large enough that its departure would reprice the center. Use it any time the rent roll shows co-tenancy language and the model does not. Standalone tenant credit work for non-retail space belongs to [Office Tenant Credit and Exposure Analyst](skills/office/office-tenant-credit-and-exposure-analyst.md) or [Industrial Tenant Credit Analyst](skills/industrial/industrial-tenant-credit-analyst.md); here credit is read only as one input to anchor durability and the co-tenancy chain. This is educational decision support, not legal, tax, investment, accounting, or financing advice. Co-tenancy, continuous-operation, and liquidated-damages enforceability is state-law specific, and recorded REA / OEA interpretation is document and title specific. Have counsel review the operative documents.

---

## What You'll Need to Provide

- Rent roll with suite, SF, tenant, term, expirations, options, and current rent actually being billed
- Full lease stack for anchors, junior anchors, and any tenant with co-tenancy rights, including amendments, side letters, and estoppels
- Recorded REA / OEA / ECR / COREA, plus any operating covenants, supplemental agreements, and the title report
- Site plan with parcel and ownership boundaries showing which boxes the landlord owns, ground-leases, or does not own at all
- Tenant sales reports where reported, and any anchor closure notices, going-dark notices, or bankruptcy filings
- Trade area and competitive supply context, and the local broker's view of replacement demand for the box
- Business question: acquisition underwriting, lender sizing, hold-or-sell, or live anchor closure response

---

## Mission

Identify every anchor and the ownership form that controls it, connect each co-tenancy clause to the exact trigger that fires it and the remedy that follows, quantify the cascade in dollars and months, test whether the assumed backfill is legally possible under the REA, and deliver an anchor risk rating with a mitigation plan a decision maker can act on.

---

## Strategy

### Step 1: Build the Anchor Inventory and Ownership Map

For every box that functions as an anchor, junior anchor, or mini-major, record ownership form, because ownership decides what control exists:

- Landlord-owned and leased to the anchor - a lease to abstract and remedies to enforce
- Ground-leased to the anchor - land rent only, no recovery participation, reversion and financeability to check
- Owned in fee by the anchor and bound only by a recorded REA - no lease, no term, no landlord remedy; or shadow / non-owned, where the anchor sits outside or adjacent to the property and the landlord holds nothing at all

Anchor GLA is frequently not the landlord's to control. Macerich's FY2025 Form 10-K reports total anchor GLA of 18,211,000 SF, of which 8,594,000 SF is owned by the anchor and 9,617,000 SF is leased, with 19 vacant anchors totaling 2,343,000 SF. Regency Centers' FY2025 Form 10-K defines "shadow anchors" as retailers owning space just outside or adjacent to a center whose vacancy would still reduce center traffic.

Then record, for each anchor: SF, base rent PSF, share of total rent, lease or REA expiration, remaining options, operating covenant and its expiry, go-dark right, recapture right, and whether the anchor pays CAM, a fixed contribution, or self-maintains its tract. Pull clause detail from [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md) where an abstract already exists.

### Step 2: Score Anchor Health

Gather what exists and mark what does not: trailing-twelve-month reported sales and sales PSF for stores open a full year; occupancy cost ratio using the category frames and fleet-comparison method in [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md); this store's rank inside that tenant's own fleet, which predicts renewal better than the ratio level; credit of the entity actually on the lease and any guarantor, not the brand; corporate signals such as closure programs, going-concern language, banner conversions, and restructurings; and whether in-place rent sits above or below what a replacement would pay.

Anchors carry small rent and large risk. Macerich reports that anchors accounted for approximately 6.9% of total rents for FY2025. Underwrite the traffic and the co-tenancy exposure, not the rent line.

### Step 3: Map Every Co-Tenancy Clause to Its Trigger and Remedy

Read every lease, not just the anchors'. For each co-tenancy provision, extract into one table:

- Type: opening co-tenancy (before the tenant must open or pay full rent) or ongoing / operating co-tenancy
- Trigger: named anchors, a count of anchors or mini-majors, an occupancy threshold, or a combination. Cox, Castle & Nicholson describes mini-majors at roughly 15,000 to 30,000 SF and combined tests such as one of two anchors plus four of seven mini-majors plus 75% of shop space. The lease in JJD-HOV Elk Grove, LLC v. Jo-Ann Stores, LLC required three anchors or comparable substitutes, or 60% of gross leasable area occupied excluding the tenant's own space.
- Measurement base: which GLA counts, whether the tenant's own space is excluded, and whether leased or open-and-operating is the test
- Conditions on the tenant: no default, itself operating, personal to the original signatory, required proof of a sales decline; and the landlord cure period and replacement-tenant standard, including who may propose the replacement
- Remedy: abatement percentage, substitute rent formula, right to close, delayed opening, or termination
- Timing: when relief starts, when termination becomes available, sunset, snap-back, landlord recapture, and whether relief is already running today

Conventions to test against, never to assume: Cox Castle describes abatement often at 50% of fixed rent, termination typically requiring six months and often a year of continued violation, and a return to full rent or landlord recapture after about one year. The 2025 ICSC operating covenants materials list the landlord-side limitations that decide cost: a cure period, a forced election between termination and rent reduction, remedies limited to fixed rent rather than percentage rent, carve-outs for casualty, remodeling, and force majeure, landlord-proposed replacements, and a requirement that the tenant prove measurable damage.

### Step 4: Model the Dark-Anchor Cascade

Run at least one scenario per at-risk anchor, and never model an anchor closure as a single vacancy line. Stage the loss:

```text
Cascade NOI Loss = lost anchor rent + lost anchor recoveries + triggered rent relief + rent lost to triggered terminations
Triggered Rent Relief = sum over affected leases of (in-place annual rent - substitute or abated rent) x months in effect / 12
Backfill Capital = allowance PSF x SF + leasing commissions + landlord work + carry during downtime
Recovery Leakage = the anchor share of the CAM / tax / insurance denominator the remaining pool must absorb
```

Rules that make the scenario honest:

- A dark-but-paying anchor still fires co-tenancy. Regency's 10-K states some anchors have the right to vacate and may prevent re-tenanting "by continuing to comply and pay rent." Rent roll occupancy will show nothing.
- Sequence the clauses. Abatement usually precedes the termination window; count abatement months separately from terminations, and apply the sunset or snap-back where one exists.
- Run second-order triggers. A shop closure caused by the first cascade can drop occupancy below a second threshold. Brixmor's 10-K states an anchor's failure to occupy "could potentially trigger lease termination rights or reductions in rent due from certain other tenants," and CBL's 10-K adds that a tenant bankruptcy resulting in lease rejection can itself trigger co-tenancy clauses in other leases.
- Build downtime from local comps, broker LOIs, and a named list of tenants in the market for that box size. There is no defensible national average; do not import one.
- Sanity-check backfill economics against institutional disclosure rather than defaulting to it. Regency's FY2025 new anchor-space leases averaged $17.46 PSF base rent against $28.67 PSF of tenant allowance and landlord work plus $4.65 PSF of commissions. Brixmor reports anchor expirations through 2028 at a weighted average $11.37 PSF expiring ABR against $17.84 PSF on new anchor leases signed in 2025.
- Route the recovery-pool effect through [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md), and hand the case where the box does not re-lease inside the loan term to [Retail Financing Fit](skills/retail/retail-financing-fit.md).

### Step 5: Test the REA / OEA Against the Backfill Plan

Before any replacement tenant enters the model, confirm the recorded documents permit it:

- Approving parties and consent rights. The ICSC REA materials state approval rights under a center-wide REA are often limited to the master developer and the top few anchor retailers who own their own parcels.
- Prohibited uses. Older REAs routinely bar the categories that now backfill dark boxes - fitness, entertainment, bars, office, hotel, residential - and the ICSC materials note antiquated prohibited-use lists are accelerating decline, especially at enclosed malls.
- Exclusives, and whether a "use it or lose it" clause extinguishes an exclusive when the benefited retailer closes or changes use. Without one, a dead retailer's exclusive still clouds title and blocks the obvious replacement.
- Site plan controls: permissible building areas, height limits, de-malling restrictions, roadway, drive, curb-cut, parking-configuration, and access-point restrictions. The ICSC materials call site plan controls the biggest contractual impediment to needed redevelopment, and note retailers often require significant economic concessions to consent.
- Parking ratios by use and whether each tract must self-park; REA term and expiration; whether any anchor operating covenant has already lapsed; and whether the vacated parcel participates in CAM at all

### Step 6: Assess Replacement-Anchor Probability

Build a named-candidate list, not an adjective. For the specific box - SF, depth, frontage, loading, clear height, parking field, drive-through or liquor potential, divisibility - identify actual expanding operators and what each would pay and require, using the demand and competitive-supply read from [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md).

Demand is real and category-specific. Sprouts Farmers Market opened 37, 33, and 30 stores in fiscal 2025, 2024, and 2023 and plans more than 40 in fiscal 2026. Burlington Stores ended its fiscal year at 1,212 stores, plans approximately 110 net new stores in the year ending January 30, 2027, and discloses acquiring leases through bankruptcy proceedings that generated $35.5 million and $15.7 million of pre-opening costs in its two most recent fiscal years. The other tail is equally documented: CBL's 10-K reports department store market share declining and traffic-driving ability substantially decreased, non-department-store replacement anchors demanding higher allowances or less favorable terms, delay leasing space adjacent to a vacant anchor, and replacement difficulty exacerbated when the anchor space is owned by a third party the landlord cannot buy out. If the anchor is in bankruptcy, run the shopping-center levers under 11 U.S.C. 365 rather than assuming a free assignment: 365(d)(4) requires assumption or rejection by the earlier of 120 days after the order for relief or plan confirmation; 365(f)(1) overrides anti-assignment clauses; and 365(b)(3) requires adequate assurance of the rent source and of an assignee with financial condition and operating performance similar to the debtor's at lease inception, that percentage rent will not decline substantially, that the assignment breaches no radius, location, use, or exclusivity provision in any other lease, financing agreement, or master agreement at the center, and that tenant mix and balance are not disrupted.

### Step 7: Rate the Risk and Write the Mitigation Plan

Rate LOW / MODERATE / ELEVATED / SEVERE on the combination of exposure, control, and replaceability - never on any single factor. This rating covers anchor and co-tenancy exposure only; when the finding has to be weighted into an asset-level score, carry it into the Market and Tenant Concentration categories of [Risk Scoring](knowledge/risk-scoring.md) rather than restating a second scale, and size the dollar consequences with [Underwriting Calculations](knowledge/underwriting-calc.md).

| Factor | What raises the rating |
|---|---|
| Exposure and proximity | Share of center rent and GLA subject to relief or termination, and how close the center sits to a named-anchor or occupancy threshold today |
| Control | Landlord-leased anchor (most control) to fee-owned or shadow anchor (none) |
| Remedy severity | Termination rights, no cure period, no sunset, no snap-back, no forced election |
| Replaceability | Named candidates and their terms, versus a box with no identified user |
| Document friction | REA consent rights, prohibited uses, exclusives, site plan controls |
| Timing | Whether the cascade lands inside the loan term or hold period |

Each mitigation item names the action, the owner, the document that must change, the cost, and the deadline. Typical items: buy out or lease-back the dark box, buy the non-owned anchor parcel, negotiate a co-tenancy waiver or amendment for a fee, pre-negotiate an REA consent or a use-it-or-lose-it amendment, secure a replacement LOI before closing, escrow a leasing reserve, or reprice.

---

## Output Format

```markdown
# Retail Co-Tenancy and Anchor Risk Analysis
## Property:
## Format / GLA:
## Documents Reviewed:
## Anchor Risk Rating: LOW | MODERATE | ELEVATED | SEVERE

### Anchor Inventory
| Anchor | SF | Ownership Form | Rent PSF | % of Total Rent | Expiration / Options | Operating Covenant | Health Signal |
|---|---|---|---|---|---|---|---|

### Co-Tenancy Clause Map
| Tenant | Suite / SF | Type | Trigger | Measurement Base | Cure | Remedy | Termination Window | Sunset / Snap-Back | Live Today? |
|---|---|---|---|---|---|---|---|---|---|

### Dark-Anchor Cascade Scenario
| Stage | Trigger | Rent / NOI Impact | Timing (months) | Source Provision |
|---|---|---|---|---|
| Anchor rent and recoveries lost | | | | |
| Triggered abatement / substitute rent | | | | |
| Triggered terminations | | | | |
| Recovery pool leakage | | | | |
| Backfill downtime and capital | | | | |
| **Total NOI at risk** | | | | |

### REA / OEA Re-Tenanting Test
| Restriction | Provision | Blocks Which Backfill | Consent Needed From | Workaround / Cost |
|---|---|---|---|---|

### Replacement-Anchor Assessment
| Candidate | Fit to Box | Likely Rent PSF | Likely Allowance | Blocking Issue |
|---|---|---|---|---|

### Mitigation Plan
| Action | Owner | Document to Change | Cost | Deadline |
|---|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every anchor is classified by ownership form, including shadow and fee-owned boxes with no lease
- Every lease in the rent roll was read for co-tenancy language, not only the leases someone flagged
- Each co-tenancy clause names its trigger anchor(s) or threshold, its measurement base, and its remedy
- Any relief already in effect is identified and the rent roll is restated to show unimpaired contract rent
- The cascade is staged and sequenced, with abatement and termination counted separately, and downtime and re-tenanting cost come from local comps and named candidates rather than a national average
- The backfill plan was tested against the recorded REA, exclusives, and site plan controls before it was priced
- Bankruptcy scenarios run the 365(b)(3) shopping-center items and calendar the 365(d)(4) deadline
- Findings reconcile to [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md) and feed [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md) and [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md)

---

## Red Flags & Dealbreakers

- Anchor is dark but paying, so it shows as occupied everywhere while co-tenancy rights are live at the shop level
- Substitute or reduced rent is already running and is presented in the rent roll as in-place rent
- A co-tenancy remedy has no landlord cure period, no forced election, no sunset, and no snap-back
- A material share of shop rent can terminate on a single named anchor's closure
- The trigger anchor is owned in fee by the retailer or sits off-site as a shadow anchor, so the landlord has no remedy
- A named-anchor trigger references an entity or banner that no longer exists after a merger or conversion
- REA prohibited uses or a surviving exclusive with no use-it-or-lose-it clause bars the assumed backfill, or the redevelopment or pad plan needs approving-party consent nobody has requested
- The REA is approaching expiration, an anchor operating covenant has already lapsed, or backfill is underwritten at anchor rent with shop-level downtime and no allowance
- A 365 assignment is assumed without testing use, exclusivity, radius, and tenant mix across every other lease
- Kick-out rights driven by tenant sales land in the same window as the cascade and were modeled separately

---

## When Data is Missing

- If the recorded REA is not in the data room, treat the backfill plan as unverified and do not credit re-tenanting value
- If anchor leases are missing, do not assume there is no operating covenant, go-dark right, or recapture right
- If co-tenancy clauses cannot be read for every lease, state the percentage of rent reviewed and rate confidence LOW
- If anchor sales are not reported, say so rather than estimating a ratio; screen on credit, fleet position, and rent-to-market instead
- If box ownership cannot be established, pull the title report and site plan before rating
- If no named replacement candidate exists, model the downside case and price the box as a redevelopment basis; if estoppels are missing or stale, assume they may surface co-tenancy claims the abstract does not show

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | All leases with co-tenancy rights read in full, recorded REA and title reviewed, anchor ownership confirmed on the site plan, anchor sales or credit available, and named replacement candidates with market terms |
| MEDIUM | Anchor and major-tenant leases read, REA reviewed, but some shop leases abstracted only, or replacement demand supported by broker view rather than LOIs |
| LOW | Rent roll and abstracts only, REA not reviewed, anchor ownership unconfirmed, or relief already running with no supporting documents |

---

## Related Knowledge Bases

- [Retail Lease Structures](knowledge/retail-lease-structures.md)
- [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md)
- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md) and [Risk Scoring](knowledge/risk-scoring.md)

## Research Basis

- [Retail Co-Tenancy and Anchor Risk Analyst Research](research/retail/retail-co-tenancy-and-anchor-risk-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
