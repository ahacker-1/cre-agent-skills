# CRE Lender/Credit Claude Code Plugin

Install this folder into your Claude Code skills directory to use `/cre-lender-credit`.

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-lender-credit "$HOME\.claude\skills\"
```

The plugin includes:

- 8 lender/credit skills
- 4 lender/credit knowledge bases
- 2 shared CRE references: `underwriting-calc.md` and `risk-scoring.md`

Use it for U.S. CRE loan screening and sizing, sponsor and guarantor analysis, appraisal review, credit memo writing, annual risk rating, covenant and watchlist monitoring, problem loan workouts, and portfolio concentration and stress testing.
