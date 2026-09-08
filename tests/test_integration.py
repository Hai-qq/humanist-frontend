"""Structural regression tests for the merged release, not Agent/UI behavior tests."""
from __future__ import annotations
from contextlib import contextmanager
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile
ROOT = Path(__file__).resolve().parents[1]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sources = load("hf_source_builder", "scripts/build_sources.py")
spec_builder = load("hf_spec_builder_integration", "scripts/build_spec.py")
validator = load("hf_validator_integration", "scripts/validate_package.py")
releaser = load("hf_releaser", "scripts/build_release.py")
LEDGER = json.loads((ROOT / "research/sources.json").read_text(encoding="utf-8"))
BY_ID = {s["id"]: s for s in LEDGER["sources"]}


@contextmanager
def clone():
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "repo"
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        yield dest


class SourceIntegrationTests(unittest.TestCase):
    def test_generated_source_audit_matches(self):
        for rel in sources.OUTPUTS:
            self.assertEqual((ROOT / rel).read_text(encoding="utf-8"), sources.render(LEDGER))

    def test_generated_coverage_matches(self):
        self.assertEqual(json.loads((ROOT / "research/coverage.json").read_text()), sources.coverage(LEDGER))

    def test_original_32_entries_retained_with_scoped_statuses(self):
        c = sources.coverage(LEDGER)
        self.assertEqual(c["original_directory"], 32)
        self.assertEqual(c["total_records"], 50)
        self.assertEqual(c["original_status_counts"], {"read":25,"read-via-index":1,"index-read":1,"partial":2,"unavailable":3})

    def test_full_interviews_still_partial(self):
        for sid in ("A3", "A7"):
            with self.subTest(sid=sid):
                self.assertEqual(BY_ID[sid]["status"], "partial")
                self.assertFalse(BY_ID[sid]["full_transcript_obtained"])
                self.assertFalse(BY_ID[sid]["audio_download_succeeded"])
        self.assertEqual(sources.coverage(LEDGER)["full_interview_transcripts_obtained"], 0)

    def test_clips_keep_same_parent_and_no_invented_timestamps(self):
        for sid in ("A7-C1", "A7-C2"):
            s = BY_ID[sid]
            self.assertEqual(s["parent_id"], "A7")
            self.assertEqual(s["evidence_family"], "A7")
            self.assertEqual(s["transcript_scope"], "clip-only")
            self.assertIsNone(s["timestamp_in_full_video"])
            self.assertFalse(s["audio_verified"])

    def test_compilation_does_not_upgrade_original_article(self):
        self.assertEqual(BY_ID["K10"]["status"], "unavailable")
        self.assertEqual(BY_ID["K10-R1"]["status"], "scoped-read")
        self.assertEqual(BY_ID["K10-R1"]["evidence_family"], "K10")

    def test_extended_source_ids_resolve_in_spec(self):
        spec = spec_builder.render()
        for sid in ("A7-C1", "A7-C2", "K10-R1"):
            self.assertIn(f"[{sid}]", spec)
            self.assertRegex(spec, rf"(?m)^\[{re.escape(sid)}\]: https://")

    def test_new_rules_and_case_links_exist(self):
        trace = json.loads((ROOT / "research/rule_traceability.json").read_text())
        self.assertEqual({r["rule_id"] for r in trace["rules"]}, {"CTX-06","SRC-01","CMP-04","CMP-05","AGT-04","COPY-01"})
        case_ids = {c for r in trace["rules"] for c in r["eval_ids"]}
        self.assertEqual(case_ids, {"E13","E14","E15","E16","E17","E18"})
        self.assertEqual(validator.validate(), [])

    def test_evaluations_remain_unexecuted(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())
        self.assertEqual(cases["execution_status"], "not-run")
        self.assertEqual(len(cases["cases"]), 18)

    def test_historical_hash_change_is_detected(self):
        with clone() as r:
            p = r / "research/history/ALTERNATIVE_MEDIA_RECOVERY_2026-09-08.md"
            p.write_text(p.read_text() + "\nchanged\n", encoding="utf-8")
            self.assertTrue(any("Historical input changed" in x for x in validator.validate(r)))

    def test_partial_source_cannot_be_promoted_to_normative(self):
        with clone() as r:
            p = r / "research/sources.json"
            d = json.loads(p.read_text());next(s for s in d["sources"] if s["id"] == "A7")["used_as_normative_evidence"] = True
            p.write_text(json.dumps(d), encoding="utf-8")
            self.assertTrue(any("Incomplete source marked normative: A7" in x for x in validator.validate(r)))

    def test_unknown_trace_source_is_detected(self):
        with clone() as r:
            p = r / "research/rule_traceability.json"
            d = json.loads(p.read_text()); d["rules"][0]["source_ids"].append("A999")
            p.write_text(json.dumps(d), encoding="utf-8")
            self.assertTrue(any("Unknown traceability source" in x for x in validator.validate(r)))

    def test_unresolved_extended_citation_is_detected(self):
        with clone() as r:
            p = r / "skills/humanist-frontend/references/01-foundations.md"
            p.write_text(p.read_text()+"\nUnknown reference [A7-C99].\n", encoding="utf-8")
            self.assertTrue(any("Unresolved source IDs" in x and "A7-C99" in x for x in validator.validate(r)))

    def test_conflicting_reference_definitions_fail_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            refs = Path(tmp) / "refs"; shutil.copytree(spec_builder.REFS, refs)
            p = refs / "02-visual-system.md"
            p.write_text(p.read_text().replace("https://geist.co/work/anthropic", "https://invalid.example/"), encoding="utf-8")
            with patch.object(spec_builder, "REFS", refs), self.assertRaises(ValueError):
                spec_builder.render()

    def test_version_drift_is_detected(self):
        with clone() as r:
            p = r / "skills/humanist-frontend/SKILL.md"
            p.write_text(p.read_text().replace('version: "0.2.0"', 'version: "9.9.9"'), encoding="utf-8")
            self.assertTrue(any("Skill version differs" in x for x in validator.validate(r)))


class ArchiveTests(unittest.TestCase):
    def test_archives_are_deterministic_for_same_tree(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            first, second = releaser.build(ROOT, Path(a)), releaser.build(ROOT, Path(b))
            self.assertEqual([p.read_bytes() for p in first], [p.read_bytes() for p in second])

    def test_both_zip_manifests_match_every_payload_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = releaser.build(ROOT, Path(tmp))
            for output in outputs[:2]:
                with ZipFile(output) as z:
                    lines = z.read("humanist-frontend/SHA256SUMS").decode().splitlines()
                    self.assertEqual(len(lines), len(z.namelist())-1)
                    for line in lines:
                        digest, rel = line.split("  ", 1)
                        self.assertNotIn("..", Path(rel).parts)
                        self.assertEqual(hashlib.sha256(z.read("humanist-frontend/"+rel)).hexdigest(), digest)
            for line in outputs[2].read_text().splitlines():
                digest, name = line.split("  ", 1)
                self.assertEqual(hashlib.sha256((Path(tmp)/name).read_bytes()).hexdigest(), digest)

    def test_standalone_skill_matches_nested_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            full, skill, _ = releaser.build(ROOT, Path(tmp))
            with ZipFile(full) as a, ZipFile(skill) as b:
                for name in b.namelist():
                    if name.endswith("/SHA256SUMS"):
                        continue
                    nested = "humanist-frontend/skills/" + name
                    self.assertEqual(a.read(nested), b.read(name))

    def test_release_never_silently_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            releaser.build(ROOT, Path(tmp))
            with self.assertRaises(FileExistsError):
                releaser.build(ROOT, Path(tmp))

    def test_release_output_cannot_be_inside_source(self):
        with self.assertRaises(ValueError):
            releaser.build(ROOT, ROOT / "output")

    def test_local_caches_and_environment_files_are_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = Path(tmp);(r/"scripts/__pycache__").mkdir(parents=True);(r/"research").mkdir()
            (r/"scripts/__pycache__/private.pyc").write_bytes(b"cache")
            (r/"research/.env.local").write_text("secret")
            (r/"README.md").write_text("public")
            self.assertEqual(releaser.collect(r), {"README.md":b"public"})

    def test_release_rejects_font_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = Path(tmp);(r/"skills").mkdir();(r/"skills/example.woff2").write_bytes(b"not-a-font")
            with self.assertRaises(ValueError):
                releaser.collect(r)

    def test_release_rejects_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            r = Path(tmp);(r/"skills").mkdir();p=Path(outside)/"source.md";p.write_text("outside")
            (r/"skills/ref.md").symlink_to(p)
            with self.assertRaises(ValueError):
                releaser.collect(r)


if __name__ == "__main__":
    unittest.main()
