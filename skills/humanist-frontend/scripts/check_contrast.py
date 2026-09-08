"""Check the explicitly declared opaque sRGB token pairs; no network or DOM access."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
HEX = re.compile(r"^#[0-9a-fA-F]{6}$")

def luminance(color: str) -> float:
    if not isinstance(color, str) or not HEX.fullmatch(color):
        raise ValueError(f"Expected opaque #RRGGBB, got {color!r}")
    rgb = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

def contrast(a: str, b: str) -> float:
    lo, hi = sorted((luminance(a), luminance(b)))
    return (hi + 0.05) / (lo + 0.05)

def evaluate(data: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(data, dict):
        raise ValueError("Token root must be a JSON object")
    if data.get("format") != "humanist-frontend-tokens" or data.get("format_version") != 1:
        raise ValueError("Unsupported token format")
    profiles = data.get("profiles")
    pairs = data.get("contrast_pairs")
    if not isinstance(profiles, dict) or not profiles or not isinstance(pairs, list) or not pairs:
        raise ValueError("Nonempty profiles and contrast_pairs are required")
    rows = []
    for profile, modes in profiles.items():
        if not isinstance(modes, dict) or set(modes) != {"light", "dark"}:
            raise ValueError(f"{profile}: light and dark modes required")
        for mode, colors in modes.items():
            if not isinstance(colors, dict) or not colors:
                raise ValueError(f"{profile}/{mode}: nonempty color object required")
            for value in colors.values():
                luminance(value)
            for pair in pairs:
                fg, bg = pair["foreground"], pair["background"]
                threshold = pair["minimum"]
                if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not 1 <= threshold <= 21:
                    raise ValueError("Contrast threshold must be between 1 and 21")
                ratio = contrast(colors[fg], colors[bg])
                rows.append({"profile": profile, "mode": mode, "foreground": fg,
                             "background": bg, "minimum": threshold, "ratio": ratio,
                             "passed": ratio >= threshold})  # Never round before comparison.
    return rows

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tokens", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "assets/tokens.json")
    parser.add_argument("--json", action="store_true", help="Print machine-readable results")
    args = parser.parse_args()
    try:
        rows = evaluate(json.loads(args.tokens.read_text(encoding="utf-8")))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Invalid input: {exc}", file=sys.stderr)
        return 2
    failed = [r for r in rows if not r["passed"]]
    if args.json:
        print(json.dumps({"scope": "declared-opaque-token-pairs-only", "total": len(rows),
                          "failed": len(failed), "results": rows}, ensure_ascii=False, indent=2))
    else:
        print(f"{len(rows) - len(failed)}/{len(rows)} declared opaque token pairs passed.")
        for r in failed:
            print(f"FAIL {r['profile']}/{r['mode']} {r['foreground']} on {r['background']}: "
                  f"{r['ratio']:.4f} < {r['minimum']}")
        print("This is not a full-page accessibility or WCAG conformance test.")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
