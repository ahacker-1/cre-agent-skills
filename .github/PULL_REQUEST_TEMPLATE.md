## What does this PR do?

<!-- Describe your changes -->

## Which files are affected?

- [ ] Skill file(s) in `skills/`
- [ ] Knowledge base file(s) in `knowledge/`
- [ ] Claude Code plugin(s) in `claude-code-plugins/`
- [ ] README or documentation
- [ ] Templates

## Checklist

- [ ] Changes to `skills/` files are also reflected in the corresponding `claude-code-plugins/` copy
- [ ] Changes to `knowledge/` files are also reflected in any `claude-code-plugins/` copies
- [ ] No orchestration-specific language (checkpoints, pipelines, deal-id, etc.)
- [ ] All knowledge base references use `knowledge/` paths
- [ ] Formulas and thresholds are sourced from industry data (cite source if adding new ones)
- [ ] Ran `.\scripts\validate-repo.ps1 -Strict`
