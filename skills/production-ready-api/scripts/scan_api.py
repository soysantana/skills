#!/usr/bin/env python3
"""Lightweight API repository signal scanner. Standard library only."""

from pathlib import Path
import argparse, json

SKIP = {".git", "node_modules", ".next", "dist", "build", "target", ".venv",
        "venv", "__pycache__", ".idea", ".vscode", "coverage"}

SIGNALS = {
    "nestjs": ["@nestjs/core"],
    "express": ["express"],
    "fastify": ["fastify"],
    "fastapi": ["fastapi"],
    "spring_boot": ["org.springframework.boot", "spring-boot"],
    "aspnet_core": ["Microsoft.AspNetCore"],
    "axum": ["axum"],
    "prisma": ["@prisma/client", "prisma"],
    "sqlalchemy": ["sqlalchemy"],
    "ef_core": ["Microsoft.EntityFrameworkCore"],
}

HIGH_SIGNAL_NAMES = {
    "package.json", "pyproject.toml", "requirements.txt", "Cargo.toml",
    "pom.xml", "build.gradle", "build.gradle.kts", "Program.cs",
    "Dockerfile", "docker-compose.yml", "compose.yml", ".dockerignore",
    ".env.example", "schema.prisma"
}

def files(root):
    for p in root.rglob("*"):
        if any(part in SKIP for part in p.parts):
            continue
        if p.is_file():
            yield p

def read_small(path, limit=1_000_000):
    try:
        if path.stat().st_size > limit:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = Path(args.path).resolve()
    all_files = list(files(root))
    manifests = [p for p in all_files if p.name in HIGH_SIGNAL_NAMES]
    corpus = "\n".join(read_small(p) for p in manifests)
    detected = [name for name, needles in SIGNALS.items()
                if any(n.lower() in corpus.lower() for n in needles)]

    env_tracked = [str(p.relative_to(root)) for p in all_files
                   if p.name == ".env"]
    tests = [p for p in all_files if
             "test" in p.name.lower() or "spec" in p.name.lower()]
    ci = [p for p in all_files if ".github" in p.parts and "workflows" in p.parts]
    migrations = [p for p in all_files if "migration" in str(p).lower()]
    docker = [p for p in all_files if
              p.name == "Dockerfile" or p.name.startswith("docker-compose") or p.name == "compose.yml"]

    report = {
        "root": str(root),
        "detected_technologies": detected,
        "high_signal_files": [str(p.relative_to(root)) for p in manifests],
        "signals": {
            "env_files_named_dot_env": env_tracked,
            "test_file_count": len(tests),
            "ci_workflow_file_count": len(ci),
            "migration_file_count": len(migrations),
            "docker_file_count": len(docker),
        },
        "note": "Signals are not findings. Verify each item against repository context."
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("Production API repository signals")
        print("=" * 33)
        print("Detected:", ", ".join(detected) or "unknown")
        for p in report["high_signal_files"]:
            print(" -", p)
        print("\nCounts:", json.dumps(report["signals"], indent=2))

if __name__ == "__main__":
    main()
