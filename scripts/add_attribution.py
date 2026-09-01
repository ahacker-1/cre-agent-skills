#!/usr/bin/env python3
"""Stamp every skill file with attribution: YAML frontmatter + an Attribution footer.

Applies to:
- root skills under skills/**/*.md
- plugin mirrors under claude-code-plugins/*/skills/*.md
- plugin entry points claude-code-plugins/*/SKILL.md

Idempotent: files that already carry the notice are left untouched.
Run after adding a new skill or pack:

    python3 scripts/add_attribution.py            # apply
    python3 scripts/add_attribution.py --check    # report only, exit 1 if any file is missing it
"""
import argparse
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

AUTHOR = "Avi Hacker, J.D."
ORG = "The AI Consulting Network"
COPYRIGHT = f"Copyright 2026 {AUTHOR} / {ORG}"
HOMEPAGE = "https://www.theaiconsultingnetwork.com"
SOURCE = "https://github.com/ahacker-1/cre-agent-skills"
UTM = "utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills"

FRONTMATTER_FIELDS = f"""license: Apache-2.0
metadata:
  author: "{AUTHOR}"
  organization: "{ORG}"
  homepage: {HOMEPAGE}
  source: {SOURCE}
  copyright: "{COPYRIGHT}"
"""

FOOTER_HEADING = "## Attribution"

FOOTER = f"""
---

{FOOTER_HEADING}

Built and maintained by [{ORG}]({HOMEPAGE}/?{UTM}), the commercial real estate AI consulting practice of {AUTHOR}, and part of [CRE Agent Skills]({SOURCE}), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out]({HOMEPAGE}/contact?{UTM}). We would love to work with you.

{COPYRIGHT}. Licensed under the [Apache License 2.0]({SOURCE}/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
"""

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def rel(path):
    return os.path.relpath(path, REPO_ROOT)


def target_files():
    out = []
    skills_dir = os.path.join(REPO_ROOT, "skills")
    plugins_dir = os.path.join(REPO_ROOT, "claude-code-plugins")
    for base, _dirs, files in os.walk(skills_dir):
        out.extend(os.path.join(base, f) for f in files if f.endswith(".md"))
    if os.path.isdir(plugins_dir):
        for plugin in sorted(os.listdir(plugins_dir)):
            pdir = os.path.join(plugins_dir, plugin)
            if not os.path.isdir(pdir):
                continue
            skill_md = os.path.join(pdir, "SKILL.md")
            if os.path.isfile(skill_md):
                out.append(skill_md)
            sdir = os.path.join(pdir, "skills")
            if os.path.isdir(sdir):
                out.extend(
                    os.path.join(sdir, f) for f in sorted(os.listdir(sdir)) if f.endswith(".md")
                )
    return sorted(out)


def has_frontmatter_attribution(text):
    m = FRONTMATTER_RE.match(text)
    return bool(m) and "license: Apache-2.0" in m.group(1) and COPYRIGHT in m.group(1)


def has_footer(text):
    return FOOTER_HEADING in text and COPYRIGHT in text.split(FOOTER_HEADING, 1)[-1]


def missing(text):
    """Return list of what the file lacks: 'frontmatter', 'footer'."""
    out = []
    if not has_frontmatter_attribution(text):
        out.append("frontmatter")
    if not has_footer(text):
        out.append("footer")
    return out


def apply(text):
    m = FRONTMATTER_RE.match(text)
    if not has_frontmatter_attribution(text):
        if m:
            existing = m.group(1).rstrip("\r\n")
            body = text[m.end():]
            text = f"---\n{existing}\n{FRONTMATTER_FIELDS}---\n{body}"
        else:
            text = f"---\n{FRONTMATTER_FIELDS}---\n\n{text.lstrip()}"
    if not has_footer(text):
        text = text.rstrip("\r\n") + "\n" + FOOTER
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report only; exit 1 if any file lacks attribution")
    args = parser.parse_args()

    changed, lacking = [], []
    for path in target_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        gaps = missing(text)
        if not gaps:
            continue
        lacking.append((path, gaps))
        if not args.check:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(apply(text))
            changed.append(path)

    if args.check:
        if lacking:
            print("Files missing attribution:")
            for path, gaps in lacking:
                print(f"  - {rel(path)}: {', '.join(gaps)}")
            return 1
        print(f"All {len(target_files())} skill files carry attribution.")
        return 0

    print(f"Stamped {len(changed)} of {len(target_files())} skill files.")
    for path in changed:
        print(f"  + {rel(path)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
