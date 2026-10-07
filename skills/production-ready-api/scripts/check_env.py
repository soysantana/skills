#!/usr/bin/env python3
"""Check env/config files for risky patterns without printing secret values."""

from pathlib import Path
import argparse, re

SKIP = {".git", "node_modules", "dist", "build", "target", ".venv", "venv"}
SENSITIVE = re.compile(r"(SECRET|PASSWORD|PASSWD|TOKEN|API_KEY|PRIVATE_KEY|DATABASE_URL)", re.I)
PLACEHOLDER = re.compile(r"^(|change.?me|example|placeholder|your[_-].+|xxx+|<.+>)$", re.I)

def iter_files(root):
    names = {".env", ".env.local", ".env.production", ".env.prod",
             ".env.example", ".env.sample"}
    for p in root.rglob("*"):
        if any(part in SKIP for part in p.parts):
            continue
        if p.is_file() and (p.name in names or p.name.startswith(".env.")):
            yield p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.path).resolve()
    found = False

    for path in iter_files(root):
        rel = path.relative_to(root)
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key, value = key.strip(), value.strip().strip("'\"")
            if SENSITIVE.search(key) and value and not PLACEHOLDER.match(value):
                found = True
                print(f"{rel}:{i}: sensitive-looking variable {key} has a non-placeholder value")

    if not found:
        print("No obvious non-placeholder sensitive values detected in scanned env files.")
    print("Note: this is heuristic only; values are intentionally never printed.")

if __name__ == "__main__":
    main()
