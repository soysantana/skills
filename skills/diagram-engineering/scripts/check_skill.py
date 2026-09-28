#!/usr/bin/env python3
"""Validate the portable essentials of this Agent Skill."""
from __future__ import annotations
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
issues = []
if not skill.exists():
    issues.append("Missing SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        issues.append("Missing or malformed YAML frontmatter delimiters")
    else:
        fm = m.group(1)
        nm = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)", fm)
        dm = re.search(r"(?m)^description:\s*(.+)$", fm)
        if not nm: issues.append("Missing name")
        else:
            name = nm.group(1).strip()
            if name != root.name: issues.append(f"name {name!r} does not match folder {root.name!r}")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name): issues.append("name is not valid kebab-case")
            if len(name) > 64: issues.append("name exceeds 64 characters")
        if not dm: issues.append("Missing description")
    if len(text.splitlines()) > 500: issues.append("SKILL.md exceeds 500 lines")
for rel in re.findall(r"\]\((references/[^)]+|scripts/[^)]+|assets/[^)]+)\)", skill.read_text(encoding="utf-8") if skill.exists() else ""):
    if not (root / rel).exists(): issues.append(f"Broken resource link: {rel}")
print(json.dumps({"ok": not issues, "issues": issues}, indent=2))
raise SystemExit(0 if not issues else 1)
