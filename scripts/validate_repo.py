#!/usr/bin/env python3
"""Cross-platform port of scripts/validate-repo.ps1.

Checks the same invariants as the PowerShell validator so contributors on
macOS / Linux can run the strict gate locally:

- every root skill has the 9 required "## " headings
- every root skill has a Claude Code plugin mirror with the same filename and identical content
- every plugin has SKILL.md, and its skills/ and knowledge/ copies map to root files
- every research area has INDEX.md and one <skill>-research.md per root skill
- README badges match actual counts
- every skill file (root, plugin mirror, plugin SKILL.md) carries the attribution
  frontmatter and footer stamped by scripts/add_attribution.py

Usage: python3 scripts/validate_repo.py [--strict]
Exit code 1 on any error.
"""
import argparse
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

REQUIRED_SKILL_HEADINGS = [
    "When to Use This Skill",
    "What You'll Need to Provide",
    "Mission",
    "Strategy",
    "Output Format",
    "Quality Checks",
    "When Data is Missing",
    "Confidence Scoring",
    "Related Knowledge Bases",
]


def rel(path):
    return os.path.relpath(path, REPO_ROOT)


def md_files(directory, recursive=True):
    out = []
    if not os.path.isdir(directory):
        return out
    if recursive:
        for base, _dirs, files in os.walk(directory):
            for f in files:
                if f.endswith(".md"):
                    out.append(os.path.join(base, f))
    else:
        for f in os.listdir(directory):
            p = os.path.join(directory, f)
            if os.path.isfile(p) and f.endswith(".md"):
                out.append(p)
    return sorted(out)


def has_heading(text, heading):
    pattern = r"(?m)^##\s+" + re.escape(heading) + r"\s*$"
    return re.search(pattern, text) is not None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    errors = []
    warnings = []

    skills_dir = os.path.join(REPO_ROOT, "skills")
    plugins_dir = os.path.join(REPO_ROOT, "claude-code-plugins")
    knowledge_dir = os.path.join(REPO_ROOT, "knowledge")
    research_dir = os.path.join(REPO_ROOT, "research")

    root_skills = md_files(skills_dir)
    root_by_name = {}
    for s in root_skills:
        name = os.path.basename(s)
        if name in root_by_name:
            errors.append(
                f"Duplicate root skill filename '{name}' at {rel(s)} and {rel(root_by_name[name])}."
            )
        else:
            root_by_name[name] = s

    plugin_skill_files = [
        p for p in md_files(plugins_dir) if "/skills/" in p.replace(os.sep, "/")
    ]
    plugin_knowledge_files = [
        p for p in md_files(plugins_dir) if "/knowledge/" in p.replace(os.sep, "/")
    ]
    plugin_skill_names = {os.path.basename(p) for p in plugin_skill_files}

    for s in root_skills:
        with open(s, encoding="utf-8") as fh:
            text = fh.read()
        for h in REQUIRED_SKILL_HEADINGS:
            if not has_heading(text, h):
                errors.append(f"{rel(s)} is missing required heading '## {h}'.")
        if os.path.basename(s) not in plugin_skill_names:
            errors.append(f"{rel(s)} has no Claude Code plugin mirror.")

    plugins = sorted(
        d for d in (os.path.join(plugins_dir, x) for x in os.listdir(plugins_dir))
        if os.path.isdir(d)
    ) if os.path.isdir(plugins_dir) else []

    for plugin in plugins:
        if not os.path.isfile(os.path.join(plugin, "SKILL.md")):
            errors.append(f"{rel(plugin)} is missing SKILL.md.")
    for p in plugin_skill_files:
        root = root_by_name.get(os.path.basename(p))
        if root is None:
            errors.append(f"{rel(p)} has no root skill with matching filename.")
            continue
        with open(p, "rb") as fh_mirror, open(root, "rb") as fh_root:
            if fh_mirror.read() != fh_root.read():
                errors.append(
                    f"{rel(p)} differs from {rel(root)}; root is the source of truth, copy it over the mirror."
                )
    for k in plugin_knowledge_files:
        if not os.path.isfile(os.path.join(knowledge_dir, os.path.basename(k))):
            errors.append(f"{rel(k)} has no root knowledge file with matching filename.")

    if os.path.isdir(research_dir):
        for area_name in sorted(os.listdir(research_dir)):
            area = os.path.join(research_dir, area_name)
            if not os.path.isdir(area):
                continue
            if not os.path.isfile(os.path.join(area, "INDEX.md")):
                errors.append(f"{rel(area)} is missing INDEX.md.")
            skill_area = os.path.join(skills_dir, area_name)
            if os.path.isdir(skill_area):
                for s in md_files(skill_area, recursive=False):
                    stem = os.path.splitext(os.path.basename(s))[0]
                    expected = os.path.join(area, f"{stem}-research.md")
                    if not os.path.isfile(expected):
                        errors.append(
                            f"{rel(s)} is in a research-backed area but lacks {rel(expected)}."
                        )

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import add_attribution  # noqa: E402

    for path in add_attribution.target_files():
        with open(path, encoding="utf-8") as fh:
            gaps = add_attribution.missing(fh.read())
        if gaps:
            errors.append(
                f"{rel(path)} lacks attribution {' and '.join(gaps)}; run scripts/add_attribution.py."
            )

    readme = os.path.join(REPO_ROOT, "README.md")
    knowledge_count = len(md_files(knowledge_dir, recursive=False))
    research_note_count = len(
        [p for p in md_files(research_dir) if os.path.basename(p) != "INDEX.md"]
    )
    if os.path.isfile(readme):
        with open(readme, encoding="utf-8") as fh:
            readme_text = fh.read()
        expectations = [
            ("Skills", r"Skills-(\d+)", len(root_skills)),
            ("Knowledge_Bases", r"Knowledge_Bases-(\d+)", knowledge_count),
            ("Research_Notes", r"Research_Notes-(\d+)", research_note_count),
            ("Claude_Code_Plugins", r"Claude_Code_Plugins-(\d+)", len(plugins)),
        ]
        for label, pattern, actual in expectations:
            m = re.search(pattern, readme_text)
            if not m:
                warnings.append(f"README badge for {label} was not found.")
                continue
            declared = int(m.group(1))
            if declared != actual:
                errors.append(
                    f"README badge {label} declares {declared} but repo has {actual}."
                )

    if warnings:
        print("Validation warnings:")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("Validation errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(
        f"Validation passed: {len(root_skills)} skills, {knowledge_count} knowledge bases, "
        f"{len(plugins)} plugins, {research_note_count} research notes."
    )
    if args.strict:
        print("Strict mode enabled.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
