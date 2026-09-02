# Contributing to CRE Agent Skills

Thank you for your interest in improving these skills. Contributions are welcome.

## How to Contribute

### Improving Existing Skills

If you find a formula that's wrong, a threshold that's outdated, or a step that could be clearer:

1. Fork this repo
2. Make your changes to the root file in `skills/` or `knowledge/`
3. If the same file exists in `claude-code-plugins/`, update the mirrored copy there in the same change
4. Submit a pull request with a clear description of what changed and why

### Adding New Skills

If you want to add a new CRE analysis skill:

1. Follow the template structure used by existing skills (see any file in `skills/` for the pattern)
2. Include all required sections: When to Use, What You'll Need, Mission, Strategy, Output Format, Quality Checks, When Data is Missing, Confidence Scoring, Related Knowledge Bases
3. Place it in the appropriate department directory under `skills/`
4. Create a companion research note under `research/` that documents sources, assumptions, benchmark rationale, conflicting-source resolution, and edge cases
5. Add it to the relevant Claude Code plugin in `claude-code-plugins/`
6. Run `python3 scripts/add_attribution.py` so the new file carries the attribution frontmatter and footer (the validator fails without it)
7. Update README.md and docs/SKILL-INDEX.md
8. Run the strict validator before opening the PR. On Windows use `.\scripts\validate-repo.ps1 -Strict`; on macOS / Linux use `python3 scripts/validate_repo.py --strict`. The Python script is a port of the PowerShell one and checks the same invariants, and CI runs both.

### Research-Backed Authoring Standard

New sector skills and knowledge bases must follow the standards in [docs/RESEARCH-STANDARDS.md](docs/RESEARCH-STANDARDS.md).

This applies to both:

- property-type packs, such as industrial
- role-based packs, such as brokerage

Minimum requirements for new sector content:

- One companion research note per new skill or knowledge base
- At least 10 cited sources
- At least 3 primary or quasi-primary sources where available
- Publish dates and access dates for time-sensitive market or lending sources
- Explicit geography and scope assumptions

Use the root files under `skills/` and `knowledge/` as the authored source of truth. The plugin copies are distribution mirrors for Claude Code.

### Updating Knowledge Bases

Knowledge base files contain formulas, benchmarks, and criteria. If you have updated industry data:

1. Cite your source for any benchmark or threshold changes
2. Preserve all existing formulas unless correcting an error
3. Update both the `knowledge/` file and any copies in `claude-code-plugins/`

## Code of Conduct

Be professional. These skills are used for real financial analysis. Accuracy matters.

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
