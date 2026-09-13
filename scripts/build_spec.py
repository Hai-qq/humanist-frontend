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
    intro = f"""# Humanist · 界面设计规范

版本 {release['version']} · 来源快照 {release['source_snapshot_date']}

从 Anthropic 与 Kimi 的公开设计指南、产品案例、团队访谈及实现资料中提炼的前端设计方法。面向希望理解设计理由的开发者与设计者，也为 Agent 提供按需参考。

## 如何使用

先阅读第一章的研究方法，再按任务进入视觉、交互、工程或验收章节。各章先说明材料线索、作者的综合判断、应用方式与检验方法，再展开可执行规则。数值预设是原创实施默认，可按实际项目调整。

- 研究依据与采用理由：[证据与决策](research/EVIDENCE_AND_DECISIONS.md)。
- 材料性质及取得范围：[来源导读](research/READING_GUIDE.md) / [来源台账](research/SOURCE_AUDIT.md)。
- Agent 的规则选择与执行入口：[SKILL.md](skills/humanist-frontend/SKILL.md)。

本规范不代表两家公司的官方统一系统；当前两段完整访谈仍未取得完整转录，节选仅支持其范围。研究记录与本次文档修订分开，不因新版发布提升来源完成状态。

维护入口为 Skill 的 references/01–05；本文件由 scripts/build_spec.py 生成，避免另存一份独立规则。"""
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
