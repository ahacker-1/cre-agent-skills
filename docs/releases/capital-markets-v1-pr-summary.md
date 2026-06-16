# PR Summary: Capital Markets v1

## What Changed

- Added a Capital Markets / Debt Maturity & Recap v1 pack with 8 new cross-property CRE skills
- Added 4 capital markets knowledge bases and 12 capital markets research notes
- Added the `/cre-capital-markets` Claude Code plugin
- Updated README, usage docs, skill index, roadmap, changelog, release notes, and GitHub templates for `v1.5.0`

## Why It Matters

- Adds a property-type-agnostic toolkit for the refinance and maturity pressure now affecting CRE owners and lenders
- Extends the Office, Asset Management, Brokerage, Financing, and shared underwriting packs with debt maturity and recap workflows
- Gives users a complete path from maturity diagnostic through refinance gap, rescue capital, lender package, special servicing readiness, and IC memo
- Preserves all existing paths and plugin commands

## Review Focus

- Confirm the pack stays decision-support oriented and avoids legal, tax, investment, or financing advice
- Confirm refinance and recap skills separate payoff, reserves, supportable proceeds, sponsor liquidity, consent risk, and exit feasibility
- Confirm plugin mirrors match the root capital markets skills and knowledge bases
- Confirm `.\scripts\validate-repo.ps1 -Strict` passes locally and in CI
