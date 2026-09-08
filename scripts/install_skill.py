"""Copy the complete local Skill to an existing project; never overwrite or fetch."""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path
SOURCE = Path(__file__).resolve().parents[1] / "skills/humanist-frontend"
HOST_DIRS = {"codex": ".agents", "claude": ".claude", "kimi": ".kimi"}

def install(project: Path, host: str) -> Path:
    if host not in HOST_DIRS:
        raise ValueError(f"Unknown host: {host}")
    project = project.expanduser().resolve(strict=True)
    if not project.is_dir():
        raise ValueError("Project must be an existing directory")
    target = project / HOST_DIRS[host] / "skills" / SOURCE.name
    # Reject parents that would silently redirect writes outside this project.
    if not target.resolve().is_relative_to(project):
        raise ValueError("Target resolves outside the selected project")
    if target.exists() or target.is_symlink():
        raise FileExistsError(f"Refusing to overwrite: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
    return target

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--host", required=True, choices=HOST_DIRS)
    args = parser.parse_args()
    try:
        target = install(args.project, args.host)
    except (OSError, ValueError) as exc:
        print(f"Installation not completed: {exc}", file=sys.stderr)
        return 1
    print(f"Copied static Skill files to {target}")
    print("Check discovery in your agent. No host settings, hooks or accounts were configured.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
