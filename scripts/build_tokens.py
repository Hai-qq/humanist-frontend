"""Generate scoped CSS from the original tokens. No external dependencies."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills/humanist-frontend/assets"

def render(data: dict) -> str:
    lines = ["/* Generated from tokens.json. Original defaults, not an official brand system. */",
             "/* Opt in with data-hf-profile AND data-theme. This is not a global CSS reset. */",
             "[data-hf-profile] {"]
    for key, value in data["common"].items():
        lines.append(f"  --hf-{key}: {value};")
    lines.append("}")
    for profile, modes in data["profiles"].items():
        for mode, colors in modes.items():
            lines.append(f'\n[data-hf-profile="{profile}"][data-theme="{mode}"] {{')
            lines.append(f"  color-scheme: {mode};")
            for key, value in colors.items():
                lines.append(f"  --hf-{key}: {value};")
            lines.append("}")
    lines.extend(["", "@media (prefers-reduced-motion: reduce) {", "  [data-hf-profile] {",
                  "    --hf-motion-fast: 0ms;", "    --hf-motion-base: 0ms;", "    --hf-motion-panel: 0ms;",
                  "  }", "}", ""])
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if checked-in CSS differs")
    args = parser.parse_args()
    expected = render(json.loads((ASSETS / "tokens.json").read_text(encoding="utf-8")))
    out = ASSETS / "tokens.css"
    if args.check:
        if not out.exists() or out.read_text(encoding="utf-8") != expected:
            print("tokens.css is stale; run python scripts/build_tokens.py")
            return 1
        print("tokens.css matches tokens.json")
    else:
        out.write_text(expected, encoding="utf-8")
        print(out.relative_to(ROOT))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
