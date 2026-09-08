"""Check repository structure, traceability and metadata; not UI or host certification."""
from __future__ import annotations
from collections import Counter
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID = r"[A-Z]\d+(?:-[A-Z]\d+)?"
RULE_ID = r"[A-Z][A-Z0-9]*-\d{2}"
FONT_EXTENSIONS = {".ttf", ".otf", ".woff", ".woff2"}


def validate(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    required = ["README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "DESIGN_SPEC.md", "release.json", "CHANGELOG.md",
                "research/SOURCE_AUDIT.md", "research/sources.json", "research/coverage.json",
                "research/rule_traceability.json", "research/inputs.json", "evals/cases.json",
                "skills/humanist-frontend/SKILL.md", "skills/humanist-frontend/LICENSE",
                "skills/humanist-frontend/references/sources.md",
                "skills/humanist-frontend/assets/tokens.css", "skills/humanist-frontend/assets/tokens.json"]
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"Missing file: {rel}")
    if errors:
        return errors
    skill = (root / "skills/humanist-frontend/SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not match:
        errors.append("SKILL.md must begin with closed YAML frontmatter")
    else:
        front = match.group(1)
        for key, limit in [("name", 64), ("description", 1024)]:
            found = re.search(rf"^{key}:\s*(.+)$", front, re.M)
            value = found.group(1).strip().strip('\"\'') if found else ""
            if not value or len(value) > limit:
                errors.append(f"Invalid {key} length")
            if key == "name" and value != "humanist-frontend":
                errors.append("Invalid skill name")
    if len(skill.splitlines()) >= 500:
        errors.append("SKILL.md exceeds the project's compact-entry limit")
    # Historical snapshots are checked for internal links but not upgraded to the latest ledger.
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            dest = (md.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root):
                errors.append(f"Local link escapes package in {md.relative_to(root)}: {target}")
            elif not dest.exists():
                errors.append(f"Broken local link in {md.relative_to(root)}: {target}")
        used = set(re.findall(rf"\[({SOURCE_ID})\](?![:(])", text))
        defined = set(re.findall(rf"^\[({SOURCE_ID})\]:", text, re.M))
        if used - defined:
            errors.append(f"Unresolved source IDs in {md.relative_to(root)}: {sorted(used-defined)}")
    try:
        release = json.loads((root / "release.json").read_text(encoding="utf-8"))
        version = release["version"]
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append("Invalid release version")
        if not re.search(rf'^  version:\s*"{re.escape(version)}"\s*$', skill, re.M):
            errors.append("Skill version differs from release.json")
        data = json.loads((root / "research/sources.json").read_text(encoding="utf-8"))
        ledger = data["sources"]
        ids = [s["id"] for s in ledger]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate source IDs")
        if any(not re.fullmatch(SOURCE_ID, sid) for sid in ids):
            errors.append("Invalid source ID format")
        original = [s for s in ledger if s["origin"] == "original-directory"]
        if len(original) != 32:
            errors.append("Original source coverage must retain 32 entries")
        known = set(ids)
        incomplete = {"unavailable", "partial", "index-read"}
        for s in ledger:
            if s["status"] not in data["status_definitions"]:
                errors.append(f"Unknown source status: {s['id']}")
            if s["status"] in incomplete and s["used_as_normative_evidence"]:
                errors.append(f"Incomplete source marked normative: {s['id']}")
            for field in ("parent_id", "evidence_family"):
                if field in s and s[field] not in known:
                    errors.append(f"Unknown {field}: {s['id']}")
            for related in s.get("related_sources", []):
                if related not in known:
                    errors.append(f"Unknown related source: {related}")
            if not s["read_scope"] or not s["boundary"] or not s["record_basis"]:
                errors.append(f"Source scope/boundary missing: {s['id']}")
        cov = json.loads((root / "research/coverage.json").read_text(encoding="utf-8"))
        expected_counts = dict(sorted(Counter(s["status"] for s in original).items()))
        if cov["original_status_counts"] != expected_counts or cov["total_records"] != len(ledger):
            errors.append("Source coverage summary differs from ledger")
        if cov["clip_transcripts_read"] != sum(s["status"] == "clip-transcript-read" for s in ledger):
            errors.append("Clip transcript count differs from ledger")
        if cov["remaining_original_article_bodies"] != [s["id"] for s in original if s["status"] == "unavailable"]:
            errors.append("Outstanding article list differs from ledger")
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        if cases["execution_status"] != "not-run":
            errors.append("Update evaluation evidence before claiming execution")
        case_ids = [c["id"] for c in cases["cases"]]
        if len(case_ids) != len(set(case_ids)):
            errors.append("Duplicate evaluation case IDs")
        for c in cases["cases"]:
            if not c["fixture_requirements"] or not c["expected_actions"] or not c["critical_failures"]:
                errors.append(f"Incomplete evaluation case: {c['id']}")
        canonical = "\n".join(p.read_text(encoding="utf-8") for p in sorted((root / "skills/humanist-frontend/references").glob("0[1-5]-*.md")))
        rule_ids = re.findall(rf"^## ({RULE_ID})\s", canonical, re.M)
        if len(rule_ids) != len(set(rule_ids)):
            errors.append("Duplicate canonical rule IDs")
        defined_sources = set(re.findall(rf"^\[({SOURCE_ID})\]:", canonical, re.M))
        if defined_sources - known:
            errors.append("Canonical reference missing from source ledger")
        trace = json.loads((root / "research/rule_traceability.json").read_text(encoding="utf-8"))
        seen_trace = set()
        for rule in trace["rules"]:
            if rule["rule_id"] in seen_trace:
                errors.append("Duplicate traceability rule")
            seen_trace.add(rule["rule_id"])
            if rule["rule_id"] not in rule_ids:
                errors.append(f"Unknown canonical rule: {rule['rule_id']}")
            if not set(rule["source_ids"]) <= known:
                errors.append(f"Unknown traceability source: {rule['rule_id']}")
            if not set(rule["eval_ids"]) <= set(case_ids):
                errors.append(f"Unknown traceability evaluation: {rule['rule_id']}")
            if not rule["scope"] or not rule["not_claimed"]:
                errors.append(f"Missing traceability boundary: {rule['rule_id']}")
        for s in ledger:
            if not set(s.get("rule_links", [])) <= set(rule_ids):
                errors.append(f"Unknown source rule link: {s['id']}")
        tokens = json.loads((root / "skills/humanist-frontend/assets/tokens.json").read_text(encoding="utf-8"))
        if any(d["version"] != version for d in (data, cases, trace)) or tokens["design_version"] != version:
            errors.append("Versioned metadata is inconsistent")
        for rel in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
            if (root / rel).read_bytes() != (root / "skills/humanist-frontend" / rel).read_bytes():
                errors.append(f"Standalone Skill copy differs: {rel}")
        if (root / "research/SOURCE_AUDIT.md").read_bytes() != (root / "skills/humanist-frontend/references/sources.md").read_bytes():
            errors.append("Standalone source audit differs")
        inputs = json.loads((root / "research/inputs.json").read_text(encoding="utf-8"))
        for entry in inputs["inputs"]:
            p = (root / entry["archived_path"]).resolve()
            if not p.is_relative_to(root) or not p.is_file():
                errors.append(f"Missing/unsafe historical input: {entry['archived_path']}")
            elif hashlib.sha256(p.read_bytes()).hexdigest() != entry["sha256"]:
                errors.append(f"Historical input changed: {entry['archived_path']}")
    except (OSError, KeyError, ValueError, TypeError) as exc:
        errors.append(f"Invalid metadata: {exc}")
    for f in root.rglob("*"):
        if f.is_file() and f.suffix.lower() in FONT_EXTENSIONS:
            errors.append(f"Unexpected bundled font: {f.relative_to(root)}")
    return errors


if __name__ == "__main__":
    errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Local package checks: {'FAILED' if errors else 'PASSED'}")
    print("Scope: files, local links, versions, source/evaluation traceability, historical hashes, standalone parity and font exclusion.")
    raise SystemExit(bool(errors))
