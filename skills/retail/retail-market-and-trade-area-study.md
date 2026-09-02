---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Market and Trade Area Study

Define and test the trade area behind a U.S. retail asset - demand, void and leakage, competitive supply, anchor draw, access, and category resilience - and render a verdict on trade-area durability.

---

## When to Use This Skill

Use this skill when you need to know whether a U.S. retail asset is supported by the people, spending, traffic, and competitive position around it. It fits acquisition screening, refinancing, appraisal review, and asset-plan resets for grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use, pad, and single-tenant net lease (STNL) retail. For a multifamily submarket, use [Market Study](skills/due-diligence/market-study.md); for office regime and sublease dynamics, use [Office Market and Flight-to-Quality Study](skills/office/office-market-and-flight-to-quality-study.md). This skill is the retail trade-area version neither of those covers. It is educational decision support, not legal, tax, investment, accounting, or financing advice.

---

## What You'll Need to Provide

- Property name, full address, and cross streets
- Format if known: grocery-anchored, community, power, strip / unanchored, lifestyle, mall, mixed-use, pad, or STNL
- Site plan and GLA, with anchor and shop square footage separated
- Rent roll or tenant list, and reported tenant sales if any exist
- Any demographic, traffic, or trade-area reports already in the file, with their vintage, plus the hold thesis and the question the study has to answer

---

## Mission

Build a defensible trade area for the subject, measure the demand inside it, test whether that demand is already served, count what competes for it now and what is being built, and state whether the trade area will still support this asset through the hold.

---

## Strategy

### Step 1: Classify the Asset and Set the Trade-Area Frame

- Verify format from the site plan and rent roll, not from the offering memorandum label. Check GLA, anchor count, and anchor share of GLA against [Retail Benchmarks](knowledge/retail-benchmarks.md).
- Set the starting primary ring from the ICSC trade-area size for that format: strip / convenience under 1 mile; neighborhood center 3 miles; community center 3 to 6 miles; power center 5 to 10 miles; regional mall 5 to 15 miles; super-regional mall 5 to 25 miles; lifestyle 8 to 12 miles; factory outlet 25 to 75 miles. Treat that ring as a starting point, not an answer - ICSC states the criteria are typical general features rather than a rule for all situations.
- For pad and STNL assets, note up front that the trade area drives residual and re-tenanting value while lease term, credit, and rent-to-market drive current value.

### Step 2: Define Primary, Secondary, and Competition-Adjusted Trade Areas

- Build three geographies and state each one explicitly: the ring, the drive time, and the competition-adjusted boundary.
- Drive time: state the bands used (for example 5 / 10 / 15 minutes) and the reason. There is no published universal standard, so justify the bands by road network, barriers, and shopping behavior.
- Competition adjustment: cut the boundary where a competing center of equal or better format and anchoring sits between the subject and the population, and name the competing trade centers you cut against. Test barriers - limited-access highways, rivers, rail, grade separations, one-way pairs, school district and municipal lines, toll crossings.
- If customer-origin or visit data exists, let it override the ring. Draw varies by tenant inside one center, so a destination anchor and a convenience shop do not share a trade area.
- Dense urban or transit-oriented retail: rings and drive time both fail. Use daytime population, block-level density, and pedestrian counts, and say so in the output.

### Step 3: Profile Demand - Demographics, Daytime Population, and Growth

Pull for each geography, with source and vintage on every figure:

- population, households, household size, and five-year growth
- median and per capita household income, and per capita income relative to the state or MSA
- age distribution, education, owner / renter split, and vehicle availability
- daytime population and jobs by work location from Census LEHD OnTheMap, plus home-to-work flows
- housing permits, major employer announcements, and any single-employer concentration

Decision rules:

- Weight demand by income, not by population alone. Potential sales scale with the ratio of local per capita income to the benchmark geography's per capita income.
- Aggregate OnTheMap block-level data to the whole trade area before drawing conclusions (LODES is partially synthetic and noisy at block level), and flag any trade area where one employer, campus, or base carries the daytime population.

### Step 4: Run the Void, Leakage, and Surplus Analysis

Compute by NAICS sector for the primary trade area:

| Measure | Formula | Reading |
|---|---|---|
| Potential sales | Population x benchmark per capita sales for the sector x (local per capita income / benchmark per capita income) | Spending the trade area should generate |
| Trade Area Capture | Actual sales / (benchmark per capita sales x income ratio) | Number of customers purchased for; aspatial, not a boundary |
| Pull Factor | Trade Area Capture / trade-area population | Drawing power |
| Surplus or leakage | Actual sales - potential sales | Dollar size of the gap |

- Read the Pull Factor in bands: under 0.9 underperforming, 0.9 to 1.1 performing as expected, over 1.1 overperforming. Treat 0.9 to 1.1 as no signal.
- If you are handed a purchased Leakage / Surplus Factor, a positive value is leakage out of the trade area and a negative value is a surplus drawing customers in. Report the factor and the dollar gap together; a factor alone is not actionable.
- Validate before you act. Modeled sales estimates are built on other estimates, and published critiques document 20% to 40% error factors in business directory listings plus systematic NAICS misclassification. Confirm any leakage that drives a conclusion against at least one harder input: state or local sales tax data by NAICS, actual reported tenant sales, a signed LOI, or a broker-confirmed comp.
- Suppression check: sector data is withheld where fewer than ten establishments exist and those sales fall into an unclassified bucket, so never recommend a category on leakage drawn from a suppressed sector. Tourism, seasonal, and recreational-home markets inflate Pull Factors; flag and caveat rather than reporting the number bare.
- Grocery void screen: USDA ERS measures supermarket access at 1 mile in urban areas and 10 miles in rural areas, counting only supermarkets, supercenters, and large grocery stores. Warehouse clubs, drug stores, dollar stores, and convenience stores do not count as grocery supply.

### Step 5: Inventory Competitive Supply and New Deliveries

- Build the competing set by format, anchor lineup, and trade-area overlap, not by proximity alone.
- For each competitor record: name, format, GLA, anchors, occupancy, asking shop rent, year built, last renovation, and distance and drive time from the subject.
- Add anticipated supply. Entitled and permitted projects belong in the analysis even when not under construction; the Interagency Appraisal and Evaluation Guidelines direct that a reader be able to understand the anticipated supply of competing properties. State entitlement status, expected delivery, and which of the subject's tenants or categories each project targets.
- Check the local pipeline against population. National construction is thin but extremely uneven: JLL reported a Q2 2026 national average of 16.4 SF under construction per 100 residents against 95.9 in Dallas-Fort Worth, 69.0 in Tampa / St. Petersburg, 68.7 in Las Vegas, and 0.0 in New York City (directional, Q2 2026).
- Identify dark boxes, shadow space, and any anchor that has gone dark or is rumored to close in the competing set. Hand those to [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md).

### Step 6: Test Anchor Draw, Cross-Shopping, Access, and Corridor Co-Tenancy

- Rank tenants by share of center visits where visit data exists, not by GLA. Visit-based research has found small-format tenants out-drawing department stores in the same mall, so the biggest box is not automatically the anchor.
- Test cross-shopping: which tenants share customers, whether a co-located competitor lifts or cannibalizes, and whether the mix gives a shopper a second reason to stop. A tenant opening another store of the same banner nearby cuts subject sales without changing the trade area, so check the tenant's own fleet before blaming the market.
- Traffic counts: require AADT, not ADT. FHWA defines AADT as the mean volume across all days of a year, while ADT is a short-duration average, often seven days or less. Record the state DOT station identifier, count year, and direction. Treat an undated or unsourced count in marketing material as unverified.
- Access and visibility checklist: signalized access, median cuts and left-turn permission, number and quality of curb cuts, cross-access easements to adjacent parcels, parking field depth and ratio, sight lines from the primary road, pylon and monument signage rights, and drive-thru feasibility on pads.
- Corridor co-tenancy: catalog what sits within the same retail node, including the shadow-anchor draw the subject does not own. A center that borrows traffic from an unowned supercenter has a durability risk the rent roll does not show.

### Step 7: Test Category Resilience, Submarket Metrics, and Render the Verdict

- Score the tenant mix for e-commerce exposure. Census reported e-commerce at 17.1% of total U.S. retail sales in Q2 2026, growing 12.2% year over year against 6.7% for total retail sales, so share is rising because the non-store channel grows faster, not because stores shrink. JLL's Q2 2026 Census-sourced category read (all directional): sporting goods, hobby and books +13.7%, non-store retail +12.6%, electronics +8.0%, clothing +5.6%, food and beverage places +3.8%, general merchandisers +3.6%, grocery +1.6%, furniture and home furnishings -1.1%.
- Pull submarket vacancy and asking rent by format from the local report. Never blend national series: for Q2 2026 CBRE published 4.9% availability at $24.79 PSF, JLL 4.4% total vacancy at $26.02 PSF, and Cushman & Wakefield 6.0% shopping-center vacancy at $25.65 PSF. They measure different universes. Rent growth is local too - JLL put national rent growth at 1.7% year over year in Q2 2026, ranging from Charlotte at +6.0% down to negative in some coastal gateway markets.
- Build shop-space lease-up from local comps and signed LOIs. National absorption is carried by freestanding and general retail: JLL reported 10.2 million SF of Q2 2026 absorption with nearly 7 million SF in general retail, while Cushman & Wakefield reported only 708,000 SF for shopping centers and -2.7 million SF year to date.
- Render the verdict on trade-area durability, hand the rent-roll implications to [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md), the growth and downtime assumptions to [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md), the market narrative and risks to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md), and any lender-facing market concern to [Retail Financing Fit](skills/retail/retail-financing-fit.md).

---

## Output Format

```markdown
# Retail Market and Trade Area Study: {Property Name}
## Date: {YYYY-MM-DD}
## Format: {grocery-anchored | community | power | strip | lifestyle | mall | mixed-use | pad | STNL}
## Trade-Area Verdict: DURABLE | STABLE | ERODING | WEAK

### Trade Area Definition
| Geography | Basis | Boundary | Population | Households | Notes |
|---|---|---|---|---|---|
| Primary | | | | | |
| Secondary | | | | | |
| Competition-adjusted | | | | | |

### Demand Profile
| Metric | Primary | Secondary | Benchmark (MSA / state) | Source / Vintage |
|---|---|---|---|---|
| Population / 5-yr growth | | | | |
| Households | | | | |
| Per capita income | | | | |
| Median HH income | | | | |
| Daytime population / jobs | | | | |

### Void, Leakage, and Surplus
| NAICS sector | Potential sales | Actual sales | Surplus / (leakage) | Pull Factor | Validated against |
|---|---|---|---|---|---|

### Competitive Supply and Anticipated Supply
| Competitor / Project | Format | GLA | Anchors | Status (existing / entitled / permitted / under construction) | Occupancy or delivery | Asking shop rent | Distance / drive time |
|---|---|---|---|---|---|---|---|

### Anchor Draw, Access, and Corridor
- Traffic anchor by draw:
- Cross-shopping read:
- AADT (station / year / source):
- Access and visibility:
- Corridor and shadow-anchor co-tenancy:

### Category Resilience and Submarket Position
| Category | Share of GLA | E-commerce exposure | Submarket read |
|---|---|---|---|

### Key Risks to Underwriting
| Risk | Evidence | Underwriting impact |
|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Format is verified from GLA, anchor count, and anchor GLA share, not from the marketing label
- Ring, drive time, and competition-adjusted boundaries are reported separately, and the drive-time bands are justified
- Every demographic and market figure carries a source and a vintage
- Every leakage figure that supports a conclusion is validated against sales tax data, reported tenant sales, an LOI, or a broker-confirmed comp, and the Pull Factor is reported in bands with 0.9 to 1.1 treated as no signal
- Traffic counts are AADT with station, year, and direction stated
- Anticipated supply includes entitled and permitted projects with status and expected delivery
- National vacancy figures name the publisher and the metric, and are never blended or averaged
- The verdict states what would change it

---

## Red Flags & Dealbreakers

- Trade area drawn as a single ring in a market cut by a highway, river, rail line, or toll crossing
- Leakage conclusion resting only on a purchased modeled estimate with no local validation, or drawn from a sector with fewer than ten establishments where the data is suppressed
- Pull Factor above 1.1 in a tourism or recreational-home market presented without the seasonal caveat
- Traffic count quoted with no year, station, or agency, or a short-duration ADT presented as AADT
- Population growth cited from a projection whose base year predates the last decennial census
- Grocery "void" that disappears once warehouse clubs, dollar stores, and convenience stores are excluded under the USDA definition, or one that persists only because a supercenter just outside the ring was ignored
- Competitive set built by distance rather than by format and trade-area overlap, or an entitled competing project omitted because it is not yet under construction
- Center dependent on a shadow anchor the ownership does not control
- Shop lease-up underwritten off national absorption headlines rather than local comps
- Single-employer or single-campus daytime population with no diversification
- Category concentration in the categories where growth is running in the non-store channel

---

## When Data is Missing

- If customer-origin or visit data is unavailable, use the ICSC ring plus drive time, label the trade area as unverified, and lower confidence
- If sub-state per capita sales benchmarks are unavailable, use state-level Census retail sales by subsector, state that the benchmark geography is the state, and note the loss of precision
- If tenant sales are not reported, do not infer them from leakage; state the gap and route the question to [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md) to confirm whether a sales reporting covenant exists
- If AADT is unavailable, request the state DOT count station rather than using a marketing figure; if the competitive pipeline is unclear, check municipal planning and permitting records and report what is entitled versus permitted versus under construction
- If recovery structure or expense load questions surface during the study, hand them to [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md)

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Trade area validated with customer-origin or visit data, current local market report, verified AADT, confirmed competitive set and pipeline, and at least one leakage figure validated against sales tax data or reported tenant sales |
| MEDIUM | ICSC ring plus drive time with a credible competition adjustment, current local market data, and a competitive set built from listings and site visits, but no customer-origin data and no independent sales validation |
| LOW | National or metro data used as a submarket proxy, unverified traffic counts, modeled leakage with no validation, or an incomplete competitive set and pipeline |

---

## Related Knowledge Bases

- [Retail Benchmarks](knowledge/retail-benchmarks.md)

## Research Basis

- [Retail Market and Trade Area Study Research](research/retail/retail-market-and-trade-area-study-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
