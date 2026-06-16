# CRE Office Claude Code Plugin

Install this folder into your Claude Code skills directory to use `/cre-office`.

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-office "$HOME\.claude\skills\"
```

The plugin includes:

- 8 office skills
- 4 office knowledge bases
- 2 shared CRE references: `underwriting-calc.md` and `risk-scoring.md`

Use it for U.S. office acquisitions, refinancings, lease-up, tenant credit, TI/LC underwriting, lender-fit analysis, and office IC memo writing.
