"""Build the readable spec from canonical Skill references; no network access."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "skills/humanist-frontend/references"
SOURCE_ID = r"[A-Z]\d+(?:-[A-Z]\d+)?"


def render() -> str:
    sections = []
    citations = {}
    for file in sorted(REFS.glob("0[1-5]-*.md")):
        text = file.read_text(encoding="utf-8")
        for line in text.splitlines():
            match = re.match(rf"^\[({SOURCE_ID})\]: (.+)$", line)
            if match:
                key, value = match.groups()
                if key in citations and citations[key] != value:
                    raise ValueError(f"Conflicting source definitions: {key}")
                citations[key] = value
        sections.append(re.sub(rf"^\[{SOURCE_ID}\]: .+$", "", text, flags=re.M).strip())
    release = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
    intro = f"""# Humanist Frontend · Agent 前端设计规范

版本 {release['version']} · 来源快照 {release['source_snapshot_date']}

面向 Agent 的原创实施规范，受 Anthropic/Claude/Kimi 公开资料启发，非官方品牌手册。
包含五部分：目标与证据、视觉系统、组件与交互、工程流程、可访问性与验收。

本版已合并原仓库与后续补读，含自动命名、输入建议、长任务快速路径、交易文案以及短片方法启发。
采用和拒绝的理由见 [证据与决策](research/EVIDENCE_AND_DECISIONS.md)；来源范围见 [来源审计](research/SOURCE_AUDIT.md)。两期完整访谈仍未取得，不能将本版描述成全部视频/图片/仓库文件均已读完。
Agent 日常使用 [SKILL.md](skills/humanist-frontend/SKILL.md) 按需加载，不必每次读这份完整汇编。

维护入口为 Skill 的 references/01–05；本文件由 scripts/build_spec.py 生成。"""
    return intro + "\n\n---\n\n" + "\n\n---\n\n".join(sections) + "\n\n## 引用索引\n\n" + "\n".join(f"[{k}]: {v}" for k, v in citations.items()) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    out = ROOT / "DESIGN_SPEC.md"
    if args.check:
        if not out.exists() or out.read_text(encoding="utf-8") != expected:
            print("DESIGN_SPEC.md is stale; run python scripts/build_spec.py")
            return 1
        print("DESIGN_SPEC.md matches canonical references.")
    else:
        out.write_text(expected, encoding="utf-8")
        print("Generated DESIGN_SPEC.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
