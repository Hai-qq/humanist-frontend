"""Generate current source audits from the ledger; performs no network access."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ("research/SOURCE_AUDIT.md", "skills/humanist-frontend/references/sources.md")


def coverage(data: dict) -> dict:
    sources = data["sources"]
    original = [s for s in sources if s["origin"] == "original-directory"]
    return {
        "total_records": len(sources),
        "original_directory": len(original),
        "original_status_counts": dict(sorted(Counter(s["status"] for s in original).items())),
        "technical_supplements": sum(s["origin"] == "supplement" for s in sources),
        "recovered_supplements": sum(s["origin"] == "recovered-supplement" for s in sources),
        "full_interview_transcripts_obtained": sum(s.get("full_transcript_obtained") is True for s in original if s["id"] in {"A3", "A7"}),
        "full_interviews_targeted": 2,
        "clip_transcripts_read": sum(s["status"] == "clip-transcript-read" for s in sources),
        "remaining_original_article_bodies": [s["id"] for s in original if s["status"] == "unavailable"],
    }


def render(data: dict) -> str:
    c = coverage(data)
    lines = ["# 来源阅读记录 · 当前合并状态", "",
        f"版本 {data['version']}；来源快照 {data['checked_at']}；合并日期 {data['assembled_at']}。", "",
        data["integration_note"], "",
        f"共 **{c['total_records']} 条来源记录**：原目录 {c['original_directory']} 条、技术补充 {c['technical_supplements']} 条、新补读材料 {c['recovered_supplements']} 条。镜像、同场短片与同案例汇编保留共同来源关系，数量不代表独立证据数量。", "",
        "## 原目录覆盖", "", "| 状态 | 数量 | 含义 |", "|---|---:|---|"]
    for status, count in c["original_status_counts"].items():
        lines.append(f"| `{status}` | {count} | {data['status_definitions'][status]} |")
    lines += ["", f"完整访谈转录：**{c['full_interview_transcripts_obtained']} / {c['full_interviews_targeted']}**。已读同场短片转录：**{c['clip_transcripts_read']} 段**。尚缺原帖正文：{', '.join(c['remaining_original_article_bodies'])}。", "",
        "文字、图片/动效、运行实现的核验是不同维度；原目录的 read 不等于全部图片、整个仓库或所有链接都读完。",
        "`used_as_normative_evidence` 仅是规则追踪标记，不是效果证明或官方背书。新补读的案例与短片作为设计启发，扩展的异常处理/竞态要求属于本项目原创。",
        "文件 Blob SHA 不是提交 SHA；未固定的页面/分支可能变化。本合并版没有重新执行下载或转录。", "",
        "完整仓库的 `research/history/` 保留旧快照与补读附件；`research/inputs.json` 记录归档字节校验。历史文件内的旧统计不应替代本表。", "",
        "## 全部条目", ""]
    for s in data["sources"]:
        lines += [f"### {s['id']} · {s['title']}", "", f"- 来源：{s['url']}",
            f"- 状态：`{s['status']}`；性质：`{s['kind']}`；来源组：`{s['evidence_family']}`。",
            f"- 实际读取范围：{s['read_scope']}",
            f"- 核验日期：{s['checked_at']}；记录依据：{', '.join(s['record_basis'])}。"]
        for field, label in [("published_at", "发布"), ("updated_at", "原页更新"), ("event_period", "叙述事件时期")]:
            if field in s:
                lines.append(f"- {label}：{s[field]}。")
        if s.get("previous_status") and s["previous_status"] != s["status"]:
            lines.append(f"- 本版状态迁移：`{s['previous_status']}` → `{s['status']}`。")
        if s.get("parent_id"):
            lines.append(f"- 对应原条目：{s['parent_id']}；不独立计为原访谈/原案例的完整阅读。")
        if s.get("related_sources"):
            lines.append(f"- 关联补读：{', '.join(s['related_sources'])}。")
        if s.get("git_blob_sha"):
            lines.append(f"- 已记录文件 Blob SHA：`{s['git_blob_sha']}`。")
        if "insight" in s:
            lines += ["", "提炼：" + s["insight"]]
        lines += ["", "边界：" + s["boundary"]]
        if s.get("rule_links"):
            lines += ["", "本项目规则关联：" + " / ".join(s["rule_links"]) + "。对应扩展为原创迁移，不是原作者的完整实现。"]
        if s.get("transcript_scope"):
            lines += ["", "仅短片可见转录；没有整场时间戳、音轨校对或画面核验。"]
        if s.get("alternative_access"):
            lines += ["", "同一期节目的其他入口（入口定位不等于下载成功）：", ""]
            for a in s["alternative_access"]:
                lines.append(f"- [{a['title']}]({a['url']}) — `{a['status']}`。")
        lines += [""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / "research/sources.json").read_text(encoding="utf-8"))
    expected = render(data)
    outputs = {p: expected for p in OUTPUTS}
    outputs["research/coverage.json"] = json.dumps(coverage(data), ensure_ascii=False, indent=2) + "\n"
    stale = []
    for rel, text in outputs.items():
        path = ROOT / rel
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                stale.append(rel)
        else:
            path.write_text(text, encoding="utf-8")
    if stale:
        print("Stale source outputs: " + ", ".join(stale))
        return 1
    print("Source audits and coverage match the ledger." if args.check else "Generated source audits and coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
