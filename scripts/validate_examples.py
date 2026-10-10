#!/usr/bin/env python3
"""Validate repository conventions and run per-example non-destructive checks.

An example is a direct child directory inside a category. Empty categories use
.gitkeep files, so the initial repository runs without any example projects.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = (
    "kubernetes",
    "infrastructure",
    "observability",
    "api-engineering",
    "ai-agents",
    "mcp",
    "documentation",
)
REQUIRED_ROOT_FILES = ("README.md", "CONTRIBUTING.md", "LICENSE", ".gitignore")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    failures: list[str] = []
    checked = 0

    # Only inspect tracked files to avoid false alarms from local virtualenvs.
    tracked = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=False
    )
    if tracked.returncode == 0:
        for raw_path in tracked.stdout.decode("utf-8").split("\0"):
            if not raw_path:
                continue
            name = Path(raw_path).name
            if ((name == ".env" or name.startswith(".env.")) and not name.endswith(".example")) or name.endswith((".pem", ".key", ".p12", ".pfx")):
                failures.append(f"Possible secret-bearing file committed: {raw_path}")

    for filename in REQUIRED_ROOT_FILES:
        if not (ROOT / filename).is_file():
            failures.append(f"Missing required root file: {filename}")

    for name in CATEGORIES:
        category = ROOT / name
        if not category.is_dir():
            failures.append(f"Missing category: {name}/")
            continue

        for entry in sorted(category.iterdir()):
            if entry.is_file() and entry.name == ".gitkeep":
                continue
            if not entry.is_dir():
                failures.append(f"Unexpected file at category root: {entry.relative_to(ROOT)}")
                continue
            if not SLUG.fullmatch(entry.name):
                failures.append(f"Example folder must use kebab-case: {entry.relative_to(ROOT)}")
                continue
            readme = entry / "README.md"
            makefile = entry / "Makefile"
            if not readme.is_file():
                failures.append(f"Missing example README: {readme.relative_to(ROOT)}")
            if not makefile.is_file():
                failures.append(f"Missing validation Makefile: {makefile.relative_to(ROOT)}")
                continue
            if not re.search(r"(?m)^validate\s*:", makefile.read_text(encoding="utf-8")):
                failures.append(f"Missing 'validate' target: {makefile.relative_to(ROOT)}")
                continue
            checked += 1
            print(f"Validating {entry.relative_to(ROOT)}/", flush=True)
            try:
                subprocess.run(["make", "validate"], cwd=entry, check=True)
            except (subprocess.CalledProcessError, OSError) as exc:
                failures.append(f"Validation failed for {entry.relative_to(ROOT)}: {exc}")

    if failures:
        print("\nRepository checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Repository checks passed. Validated {checked} example(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
