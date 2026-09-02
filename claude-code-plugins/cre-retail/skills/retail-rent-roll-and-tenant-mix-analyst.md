---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Rent Roll and Tenant Mix Analyst

Turn a U.S. retail rent roll into a reconciled, decision-ready read on space mix, tenant productivity, rollover, concentration, credit, and mark-to-market. This is educational decision support, not legal, tax, investment, accounting, or financing advice. Lease rights are read by counsel; market rent comes from signed trade-area comparables.

---

## When to Use This Skill

Use this skill when a retail rent roll needs to be reconciled and interpreted before anything is underwritten, sized, or offered: acquisition diligence, refinancing, annual asset review, a lender's rent roll request, or a broker's offering memorandum you do not yet trust. It covers grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use, pad, and single-tenant net lease (STNL) retail. Do not use it to interpret co-tenancy, exclusive, radius, go-dark, kick-out, or CAM language; those handoffs are named in Step 7. Turning a rent roll file into structured data is [Rent Roll Parser](skills/document-ingestion/rent-roll-parser.md), and the unit-level multifamily version of this analysis is [Rent Roll Analyst](skills/due-diligence/rent-roll-analyst.md); this skill is the GLA-based retail read those do not produce.

---

## What You'll Need to Provide

- Current rent roll with tenant name, suite, GLA, lease start and expiration, base rent, escalations, option terms, and recovery type
- Site plan or survey with a stated GLA, and the measurement standard if one is named in the leases
- Trailing 12-month tenant sales reports where reporting is required, plus CAM, tax, and insurance billing detail
- Aged receivables and collection history, any deferral agreements, and the signed but not commenced (SNO) schedule
- Ownership and collateral map: which parcels, anchors, and pads are owned, ground leased, excluded, or shadow
- Center format as marketed (neighborhood, community, power, lifestyle, mall, strip, mixed-use, pad, STNL) and the business question being asked

---

## Mission

Produce a rent roll that reconciles to GLA, states which occupancy definition every number uses, separates anchor from inline from pad from non-GLA revenue, ranks tenants by productivity and durability rather than by size, and ends in a tenant mix verdict with a named watch list.

---

## Strategy

### Step 1: Reconcile the Rent Roll to GLA

- Sum leased plus vacant GLA and tie to the site plan or survey total. Under ANSI/BOMA Z65.5-2020 (ANSI-approved February 11, 2021), GLA is measured to the outside face of walls bordering the unit and to the centerline of shared walls, and the standard accepts a 2% variance between measurements taken by different parties. Treat a gap inside 2% as measurement noise; anything larger needs a source document, not a plug row.
- Pull non-GLA revenue rows into a separate schedule: storage, kiosk, cart, cell tower, billboard, ATM, parking, and license or specialty leasing agreements. They produce rent without occupying leasable area and will inflate occupancy and deflate ABR PSF if left in.
- Flag ground-leased pads separately: the tenant owns the building, the square footage field may be land or building or blank, the residual is land, and these must never be blended into shop ABR PSF. State the collateral boundary at the same time - which anchors, pads, and parcels are owned, ground leased, excluded from the loan, or shadow (a traffic-driving box on an adjacent parcel that is not on the rent roll and not controlled).
- Reconcile rent roll base rent to the trailing 12-month operating statement and to the aged receivables report; a static rent roll cannot show late payment history, landlord-funded rent, or deferral agreements.

### Step 2: Classify Space and Test the Format Label

Split GLA and annualized base rent (ABR) into anchor, junior anchor, inline shop, pad / outparcel, and non-GLA. Use 10,000 SF as the default anchor / shop cut, and add a junior anchor band (roughly 10,000 to 40,000 SF) for any power, community, or lifestyle center. Report both GLA share and ABR share for each band; the inversion is the point. Brixmor's FY2025 Form 10-K reports space at or above 10,000 SF as 67.4% of GLA but 48.6% of ABR at $13.49 ABR PSF, while space under 10,000 SF is 32.6% of GLA but 51.4% of ABR at $29.79 PSF. Then test the marketed format against the ICSC U.S. shopping-center classification (January 2017), which sets expected anchor share of GLA:

| Format | Anchors | Anchor GLA share | Typical tenants |
|---|---|---|---|
| Neighborhood center | 1+ | 30%-50% | 5-20 stores |
| Community center | 2+ | 40%-60% | 15-40 stores |
| Power center | 3+ | 70%-90% | few small tenants |
| Regional / super-regional mall | 2+ / 3+ | 50%-70% | 40-80+ stores |
| Lifestyle | 0-2 | 0%-50% | large-format specialty |
| Strip / convenience (under 30,000 SF) | none or convenience | n/a | narrow service mix |

A material deviation means the format label is wrong, an anchor is dark or vacant, or the anchor is shadow and not on your rent roll. Say which.

### Step 3: State Three Occupancy Numbers, Not One

Three figures can all be true on the same day, so report all three plus the bridge: leased (space under signed lease, including SNO), billed or occupied (actually billed or physically occupied), and economic (rent collected against gross potential rent, from the receivables report). The bridge is the signed-but-not-commenced schedule in SF, annual rent, and commencement dates.

Directional portfolio reference points. Brixmor reported 95.1% leased against 91.6% billed at December 31, 2025, a 350 basis point spread, with 2.7 million SF and $62.3 million of ABR signed but not yet commenced; Federal Realty reported 96.1% leased against 94.1% occupied. Brixmor's SNO population explicitly included 90 basis points of GLA tied to space existing tenants will vacate, so SNO is not automatically incremental rent. Always show the anchor-versus-shop occupancy split as well; Brixmor's shop-space leased occupancy was 92.2% against 95.1% total, and a strong blended number can hide shop weakness.

Annotate dark-but-paying and sub-leased space on every affected row. The CREFC Investor Reporting Package (v8.4) instructs servicers that where a tenant is not occupying the space but is still paying rent the servicer may print "Dark" after the tenant name, and "Sub-leased/name" where the space is sublet. Rent from a dark box counts in cash flow and counts for nothing in traffic, sales, or co-tenancy.

### Step 4: Rank Tenants by Productivity, Not by Size

For every tenant with a sales reporting obligation, compute trailing 12-month sales PSF and the occupancy cost ratio on the same period, using the definitions in [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md). Checklist per tenant: is reporting contractually required and how often (if not, mark the ratio "not available" rather than estimating it); is the store open a full 12 months and was it closed or remodeled during the period (exclude ramp-up and partial-year stores); what does the lease define as gross sales, and does the report include e-commerce fulfilled from or returned to this store; is the ratio rising or falling year over year, since a rising ratio with flat rent means falling sales and is the earliest quiet warning.

Read every ratio next to the sales PSF that produced it and against that tenant's own other stores. Grocery anchors sit in a roughly 2%-7% band per the rating-agency frame carried in the knowledge base; a practitioner frame treats 2%-4% as healthy and above roughly 5% as a reason to open a file on the store. Power-center and category-killer anchors run near 10%, with above 10% triggering a viability review. Beyond those two anchor categories no reviewed source supports a category default, so benchmark each tenant against its own fleet and against signed comparable leases. Percentage rent: schedule in place against potential. Compute the natural breakpoint as base rent divided by the percentage rate, note where the lease uses an artificial breakpoint instead, and confirm the gross sales definition, which commonly excludes refunds, employee discounts, credit card commissions, inter-store transfers, returns to manufacturers, and sales tax. Do not underwrite percentage rent growth in strip, unanchored, or STNL models.

### Step 5: Build the Rollover Ladder and WALT

Build the ladder assuming no renewal options are exercised, then again assuming all below-market options are exercised; the spread between the two is a real number, not a footnote. For each lease year report number of leases, expiring GLA, percent of leased GLA, percent of in-place ABR, in-place ABR PSF, and ABR PSF at expiration, with anchor separated from shop. Report WALT weighted by ABR and by GLA and state which is which. Flag any of these:

| Test | Flag when | Source of the test |
|---|---|---|
| Single-tenant expiry | One tenant above 30% of GLA expires within 12 months for loans of $30 million or more, within 6 months for loans under $30 million, or is on notice of non-renewal | CREFC IRP servicer watchlist, Major Tenant Expiring |
| Clustered expiry | Top three tenants each at or above 5% of GLA and cumulatively above 30% expire within 6 months | CREFC IRP servicer watchlist, Top 3 Tenants Expiring |
| Occupancy slide | Occupancy below 80% of underwritten occupancy on a fixed-rate loan, or below 90% of in-place tenants as of underwriting on a floating-rate loan | CREFC IRP servicer watchlist, Occupancy Decrease |
| Rollover spike | Any single year carries roughly twice the 12%-15% of rent seen per year in large open-air ladders | Brixmor and Kimco FY2025 expiration schedules |
| Term mismatch | Anchor term under the 10-20 year original norm, or shop term under the 5-10 year norm, without a business reason | Brixmor FY2025 10-K lease description |

Also flag month-to-month and holdover tenants, expired leases still in place, and any expiration landing after loan maturity or the intended hold.

### Step 6: Test Concentration, Credit Mix, and Mark-to-Market

Concentration. Report the top five and top ten tenants by ABR and by GLA, plus category concentration (grocery, off-price, fitness, restaurant, medical, service, entertainment, soft goods). Portfolio benchmarks do not transfer to a single asset and must be labeled as such: Kimco reported its largest tenant at 3.8% and top five at 10.9% of ABR, Federal Realty reported no tenant above 2.4%, and Brixmor's top 20 were 30.7% of GLA and 24.0% of ABR. A single neighborhood center whose grocer holds 30%-50% of GLA is by construction far more concentrated than any of those; the real limit is the backfill cost and downtime for that specific box plus what the lender will accept.

Credit mix. Bucket every tenant as investment grade, large national unrated, national franchisor-branded but franchisee-operated, regional chain, or local independent, and report the ABR share of each. Verify the rating or financials attach to the entity actually on the lease and any guarantor; franchisee-operated units carry the franchisee's credit absent a parent guaranty. No reviewed source publishes a target national / regional / local mix - Federal Realty states only that it seeks a mix of strong national, regional, and local retailers.

Mark-to-market. Compare in-place rent to signed trade-area comparables, by band, never to a national asking rent. Report the gap in dollars PSF and percent for anchor, junior anchor, shop, and pad, net of the capital required to capture it. Directional context: Brixmor's weighted average expiring anchor ABR PSF through 2028 was $11.37 against $17.84 on new anchor leases signed in 2025, with 2025 spreads of 38.7% on new leases and blended spreads of 21.7% excluding options against 16.4% including them - a 530 basis point drop that is the measured cost of below-market options. On the capital side, Kimco's 2025 leasing cost ran $41.65 PSF blended, and Federal Realty reported $58.91 PSF of tenant improvements on new comparable leases against $3.25 PSF on renewals.

### Step 7: Reach a Verdict, Name the Watch List, and Hand Off

Rate tenant mix health HEALTHY, STABLE WITH WATCH ITEMS, WEAK, or IMPAIRED against five tests: reconciliation integrity, anchor durability, shop depth and productivity, rollover shape, and mark-to-market net of capital. Put a tenant on the watch list when any of these is true: occupancy cost ratio rising two consecutive reporting periods; store in the bottom quartile of that tenant's own fleet; dark but paying; sub-leased; month-to-month or holdover; expiring inside 24 months with a below-market option; chronic late payment or an active deferral; announced closure program or going-concern qualification at the parent.

Hand off rather than resolving here. Trade area, competitive supply, and shadow anchor context go to [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md). Options, exclusives, radius, kick-out, and go-dark language behind any flagged row go to [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md). Co-tenancy triggers, anchor replacement, and dark-box remedies go to [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md). Recovery structure, CAM caps, exclusions, and fixed-CAM anchor deals go to [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md). Cash flow, downtime, retention, leasing capital, and valuation go to [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md); rollover, concentration, and reserve consequences for debt sizing to [Retail Financing Fit](skills/retail/retail-financing-fit.md); and the committee narrative and tenant exhibit to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md).

---

## Output Format

```markdown
# Retail Rent Roll and Tenant Mix Analysis
## Property / Format / Date of Rent Roll:
## Tenant Mix Verdict: HEALTHY | STABLE WITH WATCH ITEMS | WEAK | IMPAIRED

### GLA Reconciliation
Rent roll GLA ____ | Site plan / survey GLA ____ | Variance ____ SF / ____% (2% tolerance per ANSI/BOMA Z65.5-2020) | Non-GLA rows excluded ____

### Space Mix
| Band | Leases | GLA | % GLA | ABR | % ABR | ABR PSF |
|---|---|---|---|---|---|---|
| Anchor (10,000 SF+) | | | | | | |
| Junior anchor | | | | | | |
| Inline shop (under 10,000 SF) | | | | | | |
| Pad / outparcel (note ground leases) | | | | | | |
| Vacant | | | | | | |
Format asserted ____ | ICSC anchor GLA band ____ | Actual ____ | Consistent? Y/N

### Occupancy
Leased ____% (incl. SNO) | Billed / occupied ____% | Economic (collected) ____% | Anchor leased ____% | Shop leased ____%
SNO ____ SF / $____ / commencing ____ | Dark but paying ____ SF / $____ | Sub-leased ____ SF / $____

### Tenant Productivity and Percentage Rent
| Tenant | Band | GLA | ABR PSF | TTM Sales PSF | Occ. Cost % | Trend | % Rent In Place / Potential |
|---|---|---|---|---|---|---|---|

### Rollover Ladder (no options exercised)
| Year | Leases | Expiring GLA | % Leased GLA | % In-Place ABR | In-Place ABR PSF | ABR PSF at Expiry |
|---|---|---|---|---|---|---|
WALT ABR-weighted ____ yrs | GLA-weighted ____ yrs | With below-market options exercised ____ yrs | Flags triggered ____

### Concentration and Credit Mix
| Measure | % ABR | % GLA | Comment |
|---|---|---|---|
| Top tenant | | | |
| Top 5 | | | |
| Largest category | | | |
| Investment grade / national unrated | | | |
| Franchisee-operated / regional / local | | | |

### In-Place vs Market Rent
| Band | In-Place ABR PSF | Market PSF (comp source) | Gap $ | Gap % | Capital to Capture |
|---|---|---|---|---|---|

### Watch List
| Tenant | Trigger | Severity | Next Step | Hand Off To |
|---|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Rent roll GLA ties to the site plan or survey within 2%, or the variance is explained by a source document
- Non-GLA revenue rows, ground-leased pads, and excluded or shadow parcels are pulled out and labeled
- Every occupancy percentage names its definition, and the SNO bridge between leased and billed is shown
- Anchor, junior anchor, shop, and pad bands each report both GLA share and ABR share, and the asserted format is tested against the ICSC anchor GLA band
- Rent roll base rent ties to the trailing 12-month operating statement, and collections are checked against aged receivables
- Sales PSF and occupancy cost use the same trailing period and exclude stores open under 12 months; the rollover ladder is built both with and without option exercise, WALT states its weighting, and mark-to-market is net of the new-versus-renewal capital spread
- Dark, sub-leased, holdover, and month-to-month rows are annotated, not silently counted as occupied

---

## Red Flags & Dealbreakers

- Rent roll GLA and site plan GLA differ by more than 2% with no measurement or amendment support
- A blended occupancy or ABR PSF presented without the anchor-versus-shop split
- SNO rent counted as incremental when part of it backfills space existing tenants are vacating
- A dark-but-paying anchor shown as occupied while neighboring leases carry co-tenancy remedies
- Anchor GLA share far outside the ICSC band for the marketed format, indicating a mislabeled center or a shadow anchor doing the work
- One tenant above 30% of GLA expiring inside 12 months, top three above 30% cumulatively inside 6 months, or any year carrying two or more times the 12%-15% of rent typical in large open-air ladders with no reserve
- Below-market renewal options ignored in the mark-to-market; the option-inclusive spread is the honest one
- Percentage rent underwritten off an artificial breakpoint, an unaudited report, or a store open under 12 months, or franchisee-operated units credited at the franchisor's rating with no parent guaranty on the lease
- In-place-to-market gap presented gross of the tenant improvement and commission cost, or ground-leased pad square footage blended into shop ABR PSF
- Chronic late payments, landlord-funded rent, or repayment agreements absent from the rent roll narrative

---

## When Data is Missing

- No site plan or survey: report GLA as unreconciled, use the rent roll total, and cap the analysis at MEDIUM
- No tenant sales: mark occupancy cost "not available" rather than estimating it, and shift weight to lease term, credit, rent-to-market, and backfill cost - the standard STNL and pad posture
- No SNO schedule: treat leased occupancy as unverified and use billed occupancy for cash flow. No receivables: state that economic occupancy could not be tested and treat rent roll rent as gross potential, not collected
- No option schedule: build the ladder without options, state that WALT may be understated, and flag it as a diligence item
- No comparable leases: do not mark to market; state the gap as undetermined and request signed comps
- Conflicting GLA across the rent roll, leases, and site plan: show each figure with its source and request the lease measurement exhibit or amendment
- Ownership and collateral map unclear: analyze the owned parcels only and state which anchors or pads were treated as shadow

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Rent roll ties to site plan within 2% and to the trailing 12-month operating statement; anchor, shop, and pad bands separated; sales reported for anchors and the material shop tenants; option and SNO schedules available; signed trade-area comps in hand |
| MEDIUM | Rent roll reconciles but one input is missing or stale: sales for some tenants, the option schedule, the SNO detail, or receivables; comps are asking rather than signed |
| LOW | Rent roll only, or GLA does not reconcile, or no sales reporting and no comparable leases, or the collateral and ownership boundary is unresolved |

---

## Related Knowledge Bases

- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md)

## Research Basis

- [Retail Rent Roll and Tenant Mix Analyst Research](research/retail/retail-rent-roll-and-tenant-mix-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
