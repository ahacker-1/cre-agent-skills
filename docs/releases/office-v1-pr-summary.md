# PR Summary: Office v1 and Repo Validation

## What Changed

- Added an Office v1 sector pack with 8 new U.S.-focused office skills
- Added 4 office knowledge bases and 12 office research notes
- Added the `/cre-office` Claude Code plugin
- Added strict repo validation with a PowerShell script and GitHub Actions workflow
- Updated README, usage docs, skill index, roadmap, changelog, release notes, and GitHub templates for `v1.4.0`

## Why It Matters

- Expands the repo into a major CRE property type with office-specific lease, rollover, TI/LC, tenant credit, and financing logic
- Gives users a complete office path from market/stacking-plan review through IC memo
- Makes future pack expansion safer by validating skill headings, plugin mirrors, research indexes, and public README counts
- Preserves existing multifamily, industrial, brokerage, and asset-management paths without moving or renaming them

## Review Focus

- Confirm office skill content stays office-specific and does not import multifamily or industrial assumptions
- Confirm TI/LC, downtime, rollover, tenant-credit, and lender-fit guidance is framed as decision support rather than investment advice
- Confirm plugin mirrors match root office skills and knowledge bases
- Confirm `.\scripts\validate-repo.ps1 -Strict` passes locally and in CI
