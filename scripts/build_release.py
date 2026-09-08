"""Build local repository and standalone Skill ZIPs, each with a content manifest."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules", "dist"}
ROOT_FILES = {".gitignore", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md", "CHANGELOG.md", "DESIGN_SPEC.md", "release.json"}
ROOT_DIRS = {".github", "skills", "research", "reports", "scripts", "tests", "evals", "docs"}
FONT_EXTENSIONS = {".ttf", ".otf", ".woff", ".woff2"}


def collect(root: Path) -> dict[str, bytes]:
    """Use an allowlisted repository layout; reject symlinks, skip local caches."""
    entries: dict[str, bytes] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if any(part.startswith(".env") for part in rel.parts) or path.name == ".DS_Store" or path.suffix in {".pyc", ".pyo"}:
            continue
        if rel.parts[0] not in ROOT_FILES | ROOT_DIRS:
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing symlink in release inputs: {rel}")
        if path.is_file():
            if path.suffix.lower() in FONT_EXTENSIONS:
                raise ValueError(f"Refusing bundled font: {rel}")
            if path.suffix.lower() in {".mp3", ".mp4", ".wav", ".webm", ".srt", ".vtt"}:
                raise ValueError(f"Raw third-party media/transcript not expected in this release: {rel}")
            entries[rel.as_posix()] = path.read_bytes()
    return entries


def zip_bytes(path: Path, entries: dict[str, bytes], date: str) -> None:
    year, month, day = map(int, date.split("-"))
    if not 1980 <= year <= 2107:
        raise ValueError("Release date outside ZIP timestamp range")
    manifest = "".join(f"{hashlib.sha256(value).hexdigest()}  {name}\n" for name, value in sorted(entries.items()))
    files = dict(entries)
    files["SHA256SUMS"] = manifest.encode("utf-8")
    with ZipFile(path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, value in sorted(files.items()):
            info = ZipInfo("humanist-frontend/" + name, (year, month, day, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, value, compresslevel=9)


def build(root: Path, output: Path, overwrite: bool = False) -> list[Path]:
    root, output = root.resolve(), output.expanduser().resolve()
    if output.is_relative_to(root):
        raise ValueError("Output directory must be outside the source repository")
    release = json.loads((root / "release.json").read_text(encoding="utf-8"))
    version = release["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid release version")
    output.mkdir(parents=True, exist_ok=True)
    paths = [output / f"humanist-frontend-v{version}.zip", output / f"humanist-frontend-skill-v{version}.zip",
             output / f"humanist-frontend-v{version}-SHA256SUMS.txt"]
    if not overwrite and any(p.exists() or p.is_symlink() for p in paths):
        raise FileExistsError("Release output exists; use a new directory or explicit --overwrite")
    if any(p.is_symlink() for p in paths):
        raise ValueError("Refusing symlink output")
    entries = collect(root)
    skill_prefix = "skills/humanist-frontend/"
    skill = {name[len(skill_prefix):]: value for name, value in entries.items() if name.startswith(skill_prefix)}
    for required in ("SKILL.md", "LICENSE", "references/sources.md", "assets/tokens.json", "scripts/check_contrast.py"):
        if required not in skill:
            raise ValueError(f"Missing standalone Skill input: {required}")
    zip_bytes(paths[0], entries, release["release_date"])
    zip_bytes(paths[1], skill, release["release_date"])
    paths[2].write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in paths[:2]), encoding="utf-8")
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT.parent)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        paths = build(ROOT, args.output, args.overwrite)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Release build failed: {exc}", file=sys.stderr)
        return 1
    for path in paths:
        print(f"{path.name}: {path.stat().st_size} bytes")
    print("Packaging does not run application, browser or Agent evaluations. Run the documented checks first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
