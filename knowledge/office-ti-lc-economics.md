# Office TI / LC Economics

Last updated: 2026-06-16

Scope: U.S. office tenant improvements, leasing commissions, free rent, downtime, and net effective rent analysis for acquisitions, lease-up, and refinancing. Costs are time-sensitive and market-specific. Validate with local brokers, contractors, and current proposals.

---

## Core Concepts

Office NOI is not enough. Cash flow after leasing costs is often the real investment constraint.

Key terms:

- TI: Tenant improvement allowance or landlord-funded build-out.
- LC: Leasing commission paid to brokers, usually capitalized below NOI.
- Free rent: Abated rent granted as a concession.
- Downtime: Months between vacancy and rent commencement.
- Net effective rent: Economic rent after TI, LC, and free rent.
- Transaction cost: TI + LC + free rent + landlord work + legal/marketing, as applicable.

---

## Fit-Out Cost Guardrails

Current source-backed guideposts:

- JLL 2026 U.S. and Canada guide: medium-quality corporate office fit-out regional average around $295/RSF, typical range $230-$375/RSF.
- Cushman & Wakefield 2026 Americas guide: U.S. average office fit-out cost around $149/RSF, up about 5% from the prior report, with high-cost West Coast markets above $220/RSF.

These guides use different methodologies and specifications. Do not average them blindly. Use them to test whether the underwriting assumption is in the right order of magnitude for the project quality.

---

## TI Allowance Underwriting

Model each lease or rollover with:

| Input | Required Treatment |
|---|---|
| Tenant size | Use rentable square feet unless lease is explicit otherwise |
| Fit-out scope | Second-generation refresh, heavy build-out, spec suite, shell condition, lab/medical, or law/finance high-finish |
| Landlord allowance | Dollars per RSF and total dollars |
| Tenant contribution | Above-allowance amount, timing, and credit risk |
| Payment mechanics | Reimbursement, direct pay, percentage of completion, lien waiver requirement |
| Rent start | Commencement, substantial completion, tenant delay, free-rent period |
| Ownership | Landlord-owned vs tenant-owned improvements |

Formula:

```text
Total TI Cost = Tenant RSF x TI Allowance PSF
Landlord Net TI Exposure = Total TI Cost - Tenant Contribution - Any Reimbursed Amount
```

---

## Leasing Commission Underwriting

Model LC as a below-NOI capital cost.

Common approaches:

- Percentage of total lease consideration.
- Dollars per RSF.
- Dollars per RSF per year of term.
- Split between listing broker and tenant broker.

Formula examples:

```text
Gross Lease Value = Annual Base Rent x Lease Term Years
LC Dollars = Gross Lease Value x Commission Rate
LC PSF = LC Dollars / RSF
LC PSF Per Year = LC Dollars / RSF / Lease Term Years
```

Red flags:

- Renewal commissions omitted.
- Co-broker commission omitted for tenant-rep heavy markets.
- LC included in NOI instead of below-the-line cash flow.
- Leasing costs assumed only on vacancy, not on rolling occupied tenants.

---

## Net Effective Rent

Use net effective rent to compare lease proposals.

```text
Gross Rent Value = Contract Rent PSF x Term Years
Concession Value = Free Rent PSF + TI PSF + LC PSF + Other Concessions PSF
Net Effective Rent PSF = (Gross Rent Value - Concession Value) / Term Years
```

For investor underwriting, also show cash timing:

- TI usually hits early.
- LC often hits on execution or commencement.
- Free rent suppresses early cash flow.
- Rent steps may improve GAAP rent but not near-term debt service coverage.

---

## Red Flags

- TI/LC exceeds one year of starting rent without strong lease term and credit support.
- Free rent plus downtime pushes cash payback beyond the hold period.
- Landlord funds shell-to-office conversion without separately budgeting base building upgrades.
- Tenant has termination rights before the landlord recovers leasing costs.
- Underwriting assumes renewals at market rent but omits renewal TI and LC.
- Spec suites are treated as generic capital even though they are tenant-specific.
- Construction cost inflation is ignored on rollovers more than 12 months away.

---

## Related Research

- [Office TI / LC Economics Research](research/office/office-ti-lc-economics-research.md)
- [Office TI / LC Underwriting Model Builder Research](research/office/office-ti-lc-underwriting-model-builder-research.md)
