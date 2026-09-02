# Retail Rent Roll and Tenant Mix Analyst Research

## Purpose

- Supports `skills/retail/retail-rent-roll-and-tenant-mix-analyst.md`
- Establishes the space-classification, reconciliation, rollover, concentration, credit-mix, and mark-to-market tests the skill applies to a U.S. retail rent roll
- Pairs with `knowledge/retail-benchmarks.md` and `knowledge/retail-tenant-sales-and-occupancy-cost.md`; formulas stay in `knowledge/underwriting-calc.md` and scoring in `knowledge/risk-scoring.md`
- Intended users: acquisition, asset management, and credit teams reviewing rent rolls for grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use, pad, and single-tenant net lease (STNL) retail

## U.S.-Only Assumptions

- Geography: United States. Foreign square footage and rent disclosed by the same issuers (Realty Income U.K. and Europe) is excluded from every figure cited below.
- Deal type: acquisition, refinancing, and asset review of income-producing U.S. retail. Ground-up development lease-up is out of scope.
- Measurement: U.S. retail is leased on Gross Leasable Area (GLA), not on a grossed-up rentable area with a load factor. The ANSI/BOMA Z65.5-2020 Retail Standard is the U.S. reference where a measurement standard is named in the lease.
- Legal: percentage rent, exclusive, co-tenancy, radius, and go-dark language is read by counsel. This research supports economic issue spotting only, not legal interpretation.
- Reporting: REIT portfolio statistics are non-GAAP operating statistics disclosed under issuer-specific definitions. They are reference points for a diversified national portfolio, not targets for a single asset.

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| U.S. Shopping-Center Classification and Characteristics | ICSC (with CoStar Realty Information) | https://www.icsc.com/uploads/research/general/US_CENTER_CLASSIFICATION.pdf | 2017-01 | 2026-09-01 | Industry association standard (quasi-primary) | Typical GLA range, number of anchors, percent anchor GLA, tenant count, and trade area by center type |
| CREFC Investor Reporting Package, Version 8.4 | CRE Finance Council | https://www.crefc.org/common/Uploaded%20files/CREFC%20IRP%20v8.4_Final.pdf | n.d. (v8.4) | 2026-09-01 | Industry standards body (quasi-primary) | Property File tenant fields, "Dark" and "Sub-leased/name" annotations, servicer watchlist rollover and occupancy triggers |
| Brixmor Property Group FY2025 Form 10-K | SEC / Brixmor | https://www.sec.gov/Archives/edgar/data/1581068/000158106826000007/brx-20251231.htm | 2026-02 | 2026-09-01 | Primary company filing | Anchor vs shop split at 10,000 SF, leased vs billed occupancy, signed-but-not-commenced schedule, 10-year rollover ladder, top 20 tenants, expiring vs new anchor ABR PSF |
| Kimco Realty FY2025 Form 10-K | SEC / Kimco | https://www.sec.gov/Archives/edgar/data/879101/000119312526060760/kim-20251231.htm | 2026-02 | 2026-09-01 | Primary company filing | Largest-tenant and top-five ABR concentration, ten-year expiration schedule by ABR, new vs renewal rent and leasing cost PSF |
| Federal Realty Investment Trust FY2025 Form 10-K | SEC / Federal Realty | https://www.sec.gov/Archives/edgar/data/34903/000003490326000017/frt-20251231.htm | 2026-02 | 2026-09-01 | Primary company filing | Leased vs occupied gap, national / regional / local mix language, single-tenant ABR cap, new vs renewal tenant improvement PSF, typical lease terms |
| Realty Income FY2025 Form 10-K | SEC / Realty Income | https://www.sec.gov/Archives/edgar/data/726728/000072672826000011/o-20251231.htm | 2026-02 | 2026-09-01 | Primary company filing | STNL client and industry concentration, investment-grade ABR share, store-level profitability as an underwriting input |
| The 2020 BOMA Retail Standard | Turner Drake & Partners | https://www.turnerdrake.com/wp-content/uploads/2024/05/The-2020-BOMA-Retail-Standard-1.pdf | 2024-05 (hosted) | 2026-09-01 | Practitioner commentary on a standards body document | ANSI/BOMA Z65.5-2020 approved 2021-02-11; out-to-out GLA convention, exterior dining areas, inter-building allocation, 2% measurement tolerance |
| A Primer on Percentage Rent | Holland & Knight | https://www.hklaw.com/en/insights/publications/2001/03/a-primer-on-percentage-rent | 2001-03-26 | 2026-09-01 | Practitioner legal commentary | Natural vs artificial breakpoint mechanics, gross sales inclusions and exclusions, reporting and audit rights |
| Q2 2026 U.S. Retail Figures | CBRE | https://www.cbre.com/insights/figures/q2-2026-us-retail-figures | 2026-07-29 | 2026-09-01 | Institutional market research | National availability 4.9%, average asking rent $24.79 PSF up 2.4% year over year, historically low completions |
| U.S. Retail Market Dynamics, Q2 2026 | JLL | https://www.jll.com/content/dam/jllcom/en/us/documents/reports/research-reports/26-insights-us-retail-q2-2026.pdf | 2026 Q2 | 2026-09-01 | Institutional market research | 11.8 billion SF inventory, 4.4% total vacancy, $26.02 market rent PSF, 10.2 million SF Q2 absorption, absorption by center type |
| Tips for Analyzing Grocery-Anchored Retail Properties | Bullpen (Tyler Kastelberg) | https://bullpenre.com/insights/tips-for-analyzing-grocery-anchored-retail-properties | 2022-03 | 2026-09-01 | Practitioner commentary | Grocer occupancy cost frame, grocer share of GLA, rent roll collection-history diligence |
| Tenant Sales and Occupancy Cost in Retail Underwriting | Adventures in CRE (Spencer Burton) | https://www.adventuresincre.com/tenant-sales-occupancy-cost-analysis/ | 2022-06-02 | 2026-09-01 | Practitioner technical commentary | Sales PSF and occupancy cost construction, benchmark sourcing, link from ratio to renewal probability |
| CMBS: North American CMBS Property Evaluation Methodology | KBRA | https://www.kbra.com/publications/hrxjTYTm | 2026-01-09 | 2026-09-01 | Rating agency methodology (quasi-primary) | Only the title, date, table of contents, and introduction were publicly accessible; confirms a combined retail / office / industrial net cash flow section exists but supports no threshold in this note |

## Key Findings

### Measurement and reconciliation

- U.S. retail leases on GLA. Under ANSI/BOMA Z65.5-2020, approved by ANSI on February 11, 2021, GLA is measured to the outside face of walls bordering the retail unit and to the centerline of walls shared with adjoining units, and the standard deliberately avoids grossing up GLA with a load factor for base rent. Exterior space for a single tenant's exclusive use that is part of the retail experience, such as a dining patio, must be shown separately but is still included in GLA.
- The same standard accepts a 2% variance between measurements taken by different parties, so a small rent roll versus site plan difference is a measurement issue, not automatically an error.
- The CREFC Investor Reporting Package defines Current Net Rentable Square Feet as the property's net rentable area as of the determination date and expects it to be populated for retail. Its Property File carries the five largest tenants by square feet, their square footage, and their lease expiration dates, each drawn from the most recent annual lease rollover review.

### Anchor, shop, pad, and outparcel splits

- The 10,000 SF line is the operative anchor / shop cut in open-air disclosure. Brixmor's FY2025 10-K reports the portfolio at 8,552 leases across 62,684,741 SF, split into 1,473 leases and 42,226,295 SF at 10,000 SF or larger (67.4% of GLA, 48.6% of ABR, $13.49 ABR PSF) and 7,079 leases across 20,458,446 SF under 10,000 SF (32.6% of GLA, 51.4% of ABR, $29.79 ABR PSF).
- That inversion is the central structural fact of an open-air rent roll: roughly two-thirds of the GLA produces slightly less than half the rent, and roughly one-third of the GLA produces slightly more than half. A rent roll summarized only in square feet will misstate where the income actually sits.
- ICSC's classification standard sets the expected anchor share of GLA by format: neighborhood center 30%-50% with 1+ anchor and 5-20 stores, community center 40%-60% with 2+ anchors and 15-40 stores, power center 70%-90% with 3+ anchors, regional and super-regional mall 50%-70%, lifestyle 0%-50% with 0-2 anchors, and strip / convenience under 30,000 SF with no anchor or a small convenience anchor.
- Pads and outparcels are a lease-structure and ownership description, not a center format. They must be separated on the rent roll because their rent, term, credit, and residual value behave like STNL rather than like inline shop space. Brixmor treats outparcel development as a distinct reinvestment category alongside anchor space repositioning.

### Occupancy: leased, billed, and occupied are three different numbers

- Brixmor reported total leased occupancy of 95.1% at December 31, 2025 against 91.6% billed, a 350 basis point spread, with a signed-but-not-yet-commenced population of 2.7 million SF and $62.3 million of ABR. That SNO figure included 90 basis points of GLA tied to space that existing tenants will vacate in the near term.
- Federal Realty reported 96.1% leased against 94.1% occupied across 28.8 million commercial SF, a 200 basis point gap.
- Brixmor's shop-space leased occupancy was 92.2% against 95.1% total, a roughly 290 basis point anchor-to-shop spread inside a single large open-air portfolio.
- Practical consequence: three occupancy percentages can all be true for the same asset on the same day. A rent roll analysis that does not state which one it is using is not usable.

### Dark-but-paying and sub-leased space

- The CREFC IRP instructs the servicer, at the property level, that if a tenant is not occupying the space but is still paying rent the servicer may print "Dark" after the tenant name, and if the tenant has sub-leased the space may print "Sub-leased/name" after the tenant name. This applies to the largest through fifth-largest tenant fields for retail among other property types.
- This is the only reviewed source that gives a standardized reporting convention for dark space. It confirms that dark-but-paying is an expected, reportable condition rather than an edge case, and that a rent roll showing full occupancy can coexist with a dark box.

### Rollover, WALT, and lease-term expectations

- Brixmor states that anchor leases generally have original terms of 10 to 20 years and smaller tenants generally 5 to 10 years, with renewal options that may or may not exist. Federal Realty states that commercial leases generally range from three to ten years, with certain anchor leases longer.
- Brixmor's FY2025 rollover ladder, assuming no exercise of renewal options: month-to-month 176 leases / 1.1% of leased GLA / 1.0% of in-place ABR at $15.28 PSF; 2026 851 leases / 8.1% / 6.9% at $14.97; 2027 1,098 / 13.4% / 12.5% at $16.36; 2028 1,096 / 11.6% / 12.0% at $18.21; 2029 970 / 13.4% / 12.6% at $16.62; 2030 934 / 13.0% / 12.4% at $16.75; then declining through 2035, with 2036 and later at 8.9% of GLA and 10.5% of ABR.
- Kimco's FY2025 schedule, stated in percent of gross annual rent: 0.9% month-to-month or in renewal, 7.6% in 2026, 12.5% in 2027, 14.8% in 2028, 12.9% in 2029, 12.3% in 2030, then declining to roughly 5% per year through 2035, across 9,444 leases in the consolidated operating portfolio.
- Both ladders cluster 12% to 15% of rent in each of the third through fifth forward years. A single-asset ladder that concentrates two or three times that share in one year is a structural exposure, not a national norm.
- The CREFC IRP servicer watchlist gives three usable rollover and occupancy triggers, expressed as credit items. Occupancy Decrease: added when occupancy drops more than 20% from underwriting on fixed-rate loans, or 10% of in-place tenants as of underwriting on floating-rate loans, sourced from the borrower rent roll or operating statements rather than from an inspection. Major Tenant Expiring: added when a single tenant occupying greater than 30% has a lease expiring within the next 12 months for loans of $30 million or more, or within 6 months for loans under $30 million. Top 3 Tenants Expiring: added when the top three tenants with expirations inside the next 6 months individually occupy at least 5% of net rentable area and cumulatively more than 30%.

### Concentration and credit mix

- Portfolio-level concentration in diversified national retail is low by construction. Kimco reported its single largest tenant at 3.8% and its five largest at 10.9% of annualized base rental revenue, with no single center above 1.2% of ABR. Federal Realty reported no one tenant or corporate group above 2.4% of ABR across roughly 3,700 commercial leases. Brixmor's top 20 retailers were 30.7% of GLA and 24.0% of ABR at $13.14 PSF, with the largest, TJX, at 4.1% of GLA and 3.2% of ABR.
- A single center inverts this. A neighborhood center with a grocer at 30%-50% of GLA per the ICSC standard has, by definition, a top-tenant concentration an order of magnitude above the portfolio figures above. Portfolio disclosure is therefore useful as a definition of the metric and as evidence of how the market thinks about it, and is not a threshold for a single asset.
- Federal Realty describes its objective as maintaining "a mix of strong national, regional, and local retailers," which is the clearest issuer statement of the national / regional / local framing. Neither that filing nor any other reviewed source publishes a target percentage for the mix.
- Realty Income's disclosure shows the STNL variant of the same problem measured differently: 32.2% of total portfolio ABR from investment-grade clients, subsidiaries or affiliates, and top 20 clients at 35.8% of ABR with 11 of the 20 investment grade. Its underwriting criteria explicitly include store-level profitability for retail locations when available, or the importance of the real estate location to the client's business when sales are not reported.

### In-place versus market rent

- Brixmor's FY2025 disclosure is the cleanest published anchor mark-to-market: the weighted average expiring ABR PSF of anchor lease expirations through 2028, assuming no remaining renewal options are exercised, is $11.37 against $17.84 weighted average ABR PSF for new anchor leases signed during 2025. That is a roughly 57% gap on anchor space alone.
- Brixmor achieved rent spreads of 38.7% on new leases and blended spreads on new and renewal leases of 21.7% excluding options or 16.4% including options in 2025. The gap between the two blended figures is the cost of below-market renewal options, quantified.
- Kimco reported average rent of $22.61 PSF on new leases against $21.50 PSF on renewals and options in 2025, and leasing costs on 2025 activity of $149.2 million on approximately 10.8 million SF, or $41.65 PSF, comprising $115.6 million of tenant improvements and $33.6 million of external leasing commissions.
- Federal Realty reported tenant improvements and incentives on comparable spaces of $58.91 PSF for new leases against $3.25 PSF for renewals in 2024. Any mark-to-market conclusion drawn from a rent roll must be net of that spread, or it overstates value.

### Sales, occupancy cost, and percentage rent on the rent roll

- Sales PSF is trailing 12-month gross sales at the location divided by that location's leased SF; occupancy cost is base rent plus percentage rent plus CAM, real estate tax, and other reimbursables at that location, divided by the same period's gross sales. Whether a resulting ratio is healthy depends on the retail type, the tenant, and the tenant's importance to the center, and benchmark data is materially less available than rent comparables.
- Percentage rent is owed on sales above a breakpoint. A natural breakpoint is base rent divided by the percentage rate; an artificial breakpoint decouples the two so minimum rent and the percentage can be negotiated independently. Gross sales definitions commonly exclude customer refunds, employee discounts, credit card commissions, inter-store transfers, returns to manufacturers, and sales tax. Leases typically require records, periodic reports, and landlord audit rights.
- A practitioner frame for grocery anchors puts a healthy store around 2%-4% occupancy cost, below roughly 1% as evidence of room to raise rent, and above roughly 5% as closure risk, alongside a preference for at least ten years remaining on the grocer lease. `knowledge/retail-tenant-sales-and-occupancy-cost.md` carries a wider rating-agency grocery frame of roughly 2%-7%; see conflict resolution below.

### Market context, dated

- CBRE reported national retail availability unchanged at 4.9% in Q2 2026 with average asking rent of $24.79 PSF, up 2.4% year over year, and historically low completions (published July 29, 2026).
- JLL reported 11.8 billion SF of inventory, 4.4% total vacancy, $26.02 PSF market rent, 56.1 million SF under construction, and Q2 2026 net absorption of 10.2 million SF after a negative first quarter of -4.5 million SF, with general retail at nearly 7 million SF of that absorption and malls and neighborhood centers turning positive.
- These are national figures cited for direction only. Neither supports a market rent conclusion for a specific space; that comes from signed comparable leases in the trade area.

## Benchmark and Formula Decisions

Suitable as repo defaults, with the sourcing stated in the skill:

- Classify space at the 10,000 SF line into anchor / junior anchor and inline shop, and carry pad and outparcel as separate rows. Sourced to Brixmor's FY2025 disclosure convention.
- Require three occupancy figures, not one: leased, billed or occupied, and economic (paying) occupancy, plus the SNO population in SF and dollars. Sourced to Brixmor and Federal Realty.
- Require the anchor-versus-shop split of both GLA and ABR before accepting any blended occupancy or ABR PSF. Sourced to Brixmor.
- Compare anchor GLA share to the ICSC band for the asserted format; a material deviation means the format label on the offering memorandum is wrong or the center has an unleased or shadow anchor.
- Rollover screens carried into the skill as flags rather than as pass or fail: any single tenant above 30% of GLA expiring inside 12 months; top three tenants each at or above 5% of GLA and cumulatively above 30% expiring inside 6 months; occupancy more than 20 percentage points below the underwritten or historical level. Sourced to the CREFC IRP servicer watchlist.
- Flag any lease year carrying more than roughly twice the 12%-15% per-year rent expiration share seen in the Brixmor and Kimco ladders as a rollover spike requiring a reserve or a lender conversation.
- Mark-to-market must be reported net of the new-versus-renewal capital spread, using the property's own deal history where available and the Kimco $41.65 PSF blended and Federal Realty $58.91 new versus $3.25 renewal figures only as directional context.
- Dark-but-paying and sub-leased space is annotated on every rent roll row, following the CREFC "Dark" and "Sub-leased/name" convention, and excluded from any traffic, sales, or co-tenancy count even while its rent is collected.

Case-by-case only, not defaults:

- Occupancy cost thresholds by category beyond the grocery and power-center frames already carried in `knowledge/retail-tenant-sales-and-occupancy-cost.md`. No reviewed source publishes them.
- Sales PSF benchmarks for grocery, power-center, pad, or STNL tenants. Not publicly benchmarked; they must come from sales reports, estoppels, or lease reporting covenants.
- Target national / regional / local tenant mix percentages. No reviewed source publishes one.
- Any single-asset top-tenant concentration limit. Portfolio figures do not transfer; the limit is set by the lender and by the backfill cost of that specific box.
- Market rent for any specific space. Comes from signed trade-area comparables, not from a national asking-rent figure.

## Conflicting Source Resolution

- Grocery occupancy cost. The practitioner frame reviewed here calls 2%-4% healthy and above roughly 5% a closure signal; the rating-agency frame already carried in the pack knowledge base is roughly 2%-7% depending on volume. Resolution: the wider rating-agency band controls as the published range, and the tighter practitioner band is used as the point at which to open a file on the store rather than as a verdict. Both are read against the store's sales PSF and its rank inside that grocer's own fleet, which neither source replaces.
- National market rent. CBRE reported $24.79 PSF average asking rent for Q2 2026 and JLL reported $26.02 PSF market rent for the same quarter, on different inventories and different definitions of rent. Resolution: neither is used as a mark-to-market input. Both are cited only as dated national direction, and the skill requires trade-area comparables for any rent conclusion.
- Occupancy definitions. Brixmor reports leased versus billed, Federal Realty reports leased versus occupied, and the CREFC IRP reports a physical occupancy field. Resolution: the skill does not adopt one issuer's vocabulary; it requires the analysis to state which definition each number uses and to show the SNO bridge between them.
- Anchor / shop cut. The 10,000 SF line is an open-air disclosure convention, not a standard. Malls report in-line under 10,000 SF, power centers routinely have junior anchors between 10,000 and 40,000 SF, and ICSC classifies by anchor share of GLA rather than by unit size. Resolution: use 10,000 SF as the default cut, and require the analysis to add a junior anchor band whenever the center is a power, community, or lifestyle format.

## Edge Cases and Red Flags

- The rent roll does not reconcile to the site plan or to the survey. Under ANSI/BOMA Z65.5-2020 a 2% variance between measurements by different parties is acceptable; a larger gap needs a source document, not a plug row.
- Non-GLA revenue rows carried inside the GLA total. Storage, kiosk, cart, cell tower, billboard, parking, ATM, and license agreements produce rent without occupying leasable area and will inflate occupancy and deflate ABR PSF if they are not pulled out.
- Ground-leased pads. The tenant owns the building, the rent roll square footage may be land area or building area or blank, and the residual is land. These must never be blended into shop ABR PSF.
- Shadow anchors. A traffic-driving box on an adjacent parcel that is not on the rent roll and not controlled by the owner supports the trade area but cannot be underwritten as controlled tenancy. Confirm ownership and any REA/OEA obligations rather than reading the site plan.
- Anchors that are not collateral. In some structures the anchor owns its parcel or is excluded from the loan collateral. Anchor GLA share, occupancy, and ABR PSF all change depending on whether that GLA is in the denominator.
- Signed-not-open leases counted as income. Brixmor's own SNO disclosure includes GLA tied to space existing tenants will vacate, so an SNO number is not automatically incremental rent.
- Dark-but-paying tenants shown as occupied. The rent is real, the traffic is not, and neighbors may hold co-tenancy remedies. Route to the co-tenancy and anchor risk analysis rather than resolving it on the rent roll.
- Percentage rent underwritten off a partial year, a store open under 12 months, or an unaudited sales report, or a breakpoint that is artificial rather than natural without the lease being read.
- Renewal options priced below market. Brixmor's 2025 blended rent spread fell from 21.7% excluding options to 16.4% including options; a rent roll that ignores option rent overstates the mark-to-market.
- Franchisee-operated units credited to the franchisor. The credit is the franchisee's absent a parent guaranty on the actual lease.
- Collection quality invisible on a static rent roll. Late payment history, landlord-funded rent, and deferral or repayment agreements only show up in the general ledger and the aged receivables report.
- Any conclusion about co-tenancy triggers, exclusives, go-dark rights, kick-out clauses, or CAM caps drawn from the rent roll alone. Those live in the leases and in the REA/OEA.

## Open Questions

- A published U.S. standard for classifying pad, outparcel, junior anchor, and non-GLA revenue rows on a retail rent roll. None was located; the skill's classification scheme is assembled from issuer disclosure conventions and the ICSC format standard.
- Category-level sales PSF and occupancy cost benchmark tables. Would require a subscription tenant-sales database; deliberately deferred rather than estimated.
- Rating agency retail net cash flow criteria in full. The KBRA property evaluation methodology's retail section and the Morningstar DBRS property analysis criteria PDF were both behind access walls this session, so no threshold in this note rests on them.
- Empirical renewal probability by occupancy cost decile. No public dataset was located; the skill treats renewal probability as a judgment informed by the ratio, the sales trend, the option rent, and the backfill cost rather than as a modeled number.
- Whether the 10,000 SF anchor cut holds in lifestyle and mixed-use formats, where large-format specialty and food and beverage tenants blur the line. Left to the analyst with a required junior anchor band.
