#!/usr/bin/env python3
"""Lightweight structural lint for Mermaid text. No external dependencies."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

STARTERS = (
    "flowchart", "graph", "sequenceDiagram", "classDiagram", "stateDiagram",
    "erDiagram", "gantt", "gitGraph", "mindmap", "timeline", "journey",
    "requirementDiagram", "pie", "quadrantChart", "sankey-beta", "xychart-beta",
    "block-beta", "packet-beta", "architecture-beta", "kanban", "radar-beta",
    "treemap-beta"
)

def lint(text: str) -> dict:
    lines = [ln.rstrip() for ln in text.splitlines()]
    content = [ln.strip() for ln in lines if ln.strip() and not ln.lstrip().startswith("%%")]
    issues = []
    if not content:
        issues.append({"severity": "error", "message": "Diagram is empty."})
        return {"ok": False, "issues": issues}
    first = content[0]
    if not any(first.startswith(s) for s in STARTERS):
        issues.append({"severity": "warning", "message": f"Unrecognized Mermaid diagram declaration: {first!r}. It may be valid in a newer Mermaid version."})
    pairs = [("[", "]"), ("(", ")"), ("{", "}")]
    for op, cl in pairs:
        if text.count(op) != text.count(cl):
            issues.append({"severity": "warning", "message": f"Unbalanced {op}{cl}: {text.count(op)} opening vs {text.count(cl)} closing."})
    ids = re.findall(r"(?m)^\s*([A-Za-z_][\w-]*)\s*(?:\[|\(|\{|$)", text)
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    if duplicates:
        issues.append({"severity": "info", "message": "Repeated node declarations detected: " + ", ".join(duplicates[:20])})
    if len(lines) > 180:
        issues.append({"severity": "info", "message": "Large diagram source (>180 lines); consider splitting into focused views."})
    return {"ok": not any(i["severity"] == "error" for i in issues), "issues": issues, "line_count": len(lines)}

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("file", type=Path)
    args = p.parse_args()
    result = lint(args.file.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["ok"] else 1)

if __name__ == "__main__":
    main()
