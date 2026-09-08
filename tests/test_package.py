from __future__ import annotations
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

color = load("hf_contrast", ROOT / "skills/humanist-frontend/scripts/check_contrast.py")
builder = load("hf_tokens", ROOT / "scripts/build_tokens.py")
spec_builder = load("hf_spec", ROOT / "scripts/build_spec.py")
installer = load("hf_install", ROOT / "scripts/install_skill.py")
validator = load("hf_validate", ROOT / "scripts/validate_package.py")
TOKENS = json.loads((ROOT / "skills/humanist-frontend/assets/tokens.json").read_text(encoding="utf-8"))

class ContrastTests(unittest.TestCase):
    def test_black_white(self):
        self.assertAlmostEqual(color.contrast("#000000", "#FFFFFF"), 21)
    def test_same_color(self):
        self.assertEqual(color.contrast("#a64b32", "#a64b32"), 1)
    def test_symmetry(self):
        self.assertEqual(color.contrast("#A64B32", "#FAF9F5"), color.contrast("#FAF9F5", "#A64B32"))
    def test_known_reference(self):
        self.assertAlmostEqual(color.contrast("#d97757", "#ffffff"), 3.121888781312851)
    def test_brand_blue_not_normal_white_text(self):
        self.assertLess(color.contrast("#007cff", "#ffffff"), 4.5)
    def test_invalid_colors(self):
        for bad in ["#fff", "#12345678", "red", "#zz0000", "ffffff", None]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                color.luminance(bad)
    def test_all_declared_pairs(self):
        rows = color.evaluate(TOKENS)
        self.assertEqual(len(rows), 88)
        self.assertTrue(all(r["passed"] for r in rows))
    def test_comparison_not_rounded(self):
        data = copy.deepcopy(TOKENS)
        data["contrast_pairs"] = [{"foreground":"brand-accent","background":"surface","minimum":3.12189}]
        result = color.evaluate(data)[0]
        self.assertFalse(result["passed"])
    def test_non_object_root_rejected(self):
        with self.assertRaises(ValueError): color.evaluate([])
    def test_non_object_mode_rejected(self):
        data = copy.deepcopy(TOKENS); data["profiles"]["editorial-warm"]["light"] = []
        with self.assertRaises(ValueError): color.evaluate(data)
    def test_empty_pairs_rejected(self):
        data = copy.deepcopy(TOKENS); data["contrast_pairs"] = []
        with self.assertRaises(ValueError): color.evaluate(data)
    def test_wrong_schema_rejected(self):
        data = copy.deepcopy(TOKENS); data["format_version"] = 999
        with self.assertRaises(ValueError): color.evaluate(data)
    def test_invalid_threshold_rejected(self):
        data = copy.deepcopy(TOKENS); data["contrast_pairs"][0]["minimum"] = float("nan")
        with self.assertRaises(ValueError): color.evaluate(data)
    def test_unknown_token_rejected(self):
        data = copy.deepcopy(TOKENS); data["contrast_pairs"][0]["foreground"] = "not-present"
        with self.assertRaises(KeyError): color.evaluate(data)

class PackageTests(unittest.TestCase):
    def test_generated_css_is_current(self):
        actual = (ROOT / "skills/humanist-frontend/assets/tokens.css").read_text(encoding="utf-8")
        self.assertEqual(builder.render(TOKENS), actual)
    def test_generated_spec_is_current(self):
        self.assertEqual(spec_builder.render(), (ROOT / "DESIGN_SPEC.md").read_text(encoding="utf-8"))
    def test_theme_key_parity(self):
        groups = [set(colors) for modes in TOKENS["profiles"].values() for colors in modes.values()]
        self.assertTrue(all(g == groups[0] for g in groups))
    def test_package_links_and_metadata(self):
        self.assertEqual(validator.validate(), [])
    def test_cli_json_output(self):
        proc = subprocess.run([sys.executable, str(ROOT / "skills/humanist-frontend/scripts/check_contrast.py"), "--json"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)["total"], 88)
    def test_cli_invalid_input_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(ROOT / "skills/humanist-frontend/scripts/check_contrast.py"), str(Path(tmp) / "absent.json")], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
    def test_installer_copies_self_contained_skill(self):
        for host, folder in installer.HOST_DIRS.items():
            with self.subTest(host=host), tempfile.TemporaryDirectory() as tmp:
                target = installer.install(Path(tmp), host)
                self.assertEqual(target.parent.parent.name, folder)
                self.assertTrue((target / "references/02-visual-system.md").is_file())
                self.assertTrue((target / "LICENSE").is_file())
                proc = subprocess.run([sys.executable, str(target / "scripts/check_contrast.py")], capture_output=True, text=True)
                self.assertEqual(proc.returncode, 0, proc.stderr)
    def test_installer_never_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = installer.install(Path(tmp), "codex")
            sentinel = target / "SKILL.md"; sentinel.write_text("user-edited", encoding="utf-8")
            with self.assertRaises(FileExistsError): installer.install(Path(tmp), "codex")
            self.assertEqual(sentinel.read_text(), "user-edited")
    def test_missing_project_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError): installer.install(Path(tmp) / "absent", "claude")
    def test_external_symlink_parent_rejected(self):
        with tempfile.TemporaryDirectory() as project, tempfile.TemporaryDirectory() as outside:
            (Path(project) / ".agents").symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError): installer.install(Path(project), "codex")

if __name__ == "__main__":
    unittest.main()
