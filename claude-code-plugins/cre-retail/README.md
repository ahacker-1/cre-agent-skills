# CRE Retail Claude Code Plugin

Install this folder into your Claude Code skills directory to use `/cre-retail`.

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-retail "$HOME\.claude\skills\"
```

The plugin includes:

- 8 retail skills
- 4 retail knowledge bases
- 2 shared CRE references: `underwriting-calc.md` and `risk-scoring.md`

Use it for U.S. retail trade-area studies, rent roll and tenant mix analysis, lease abstraction, co-tenancy and anchor risk review, CAM reconciliation, underwriting, lender-fit analysis, and retail IC memo writing.
