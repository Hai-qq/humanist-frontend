<h1 align="center">Humanist</h1>

<p align="center"><a href="README.md">简体中文</a> · <b>English</b></p>

<p align="center">A frontend design spec and Agent Skill for Chinese-language interfaces, distilled from Anthropic's and Kimi's public design material, covering details that often go wrong: Chinese typography, save-and-recover flows, and long-running task states.</p>

<p align="center"><img src="docs/assets/themes.svg" width="820" alt="Light and dark previews of the two optional palettes, editorial-warm and precise-light, on the same research-notes screen with saved and save-failed states"></p>

```bash
npx skills add Hai-qq/humanist-frontend
```

> The spec, the Skill and the preview images are written in Chinese. Rule IDs below link to the Chinese spec.

## What it guards against

Five common failures in Chinese interfaces, each covered by a rule:

| Failure | What the spec requires | Rules |
|---|---|---|
| Pressing Enter to pick a candidate in a Chinese input method sends the message | While composition is active, Enter must not submit; handle compositionstart / compositionend and mind framework synthetic events versus `nativeEvent` | [CMP-02](DESIGN_SPEC.md#cmp-02--输入保存与反馈) · [CMP-05](DESIGN_SPEC.md#cmp-05--输入建议与执行动作分开) |
| A save fails but the UI says "Saved", and the draft is gone after a refresh | Distinguish unsaved, saving, saved and failed; never show "Saved" after an unconditional `setTimeout`; on failure, say whether input was kept and whether retry is possible | [CMP-02](DESIGN_SPEC.md#cmp-02--输入保存与反馈) |
| After clicking "Stop", the UI says stopped while the backend task keeps running | Keep "stop showing output" separate from "cancel execution"; a cancel request enters `cancelling` and shows `cancelled` only after the executor confirms | [AGT-04](DESIGN_SPEC.md#agt-04--快速结果不是取消任务的别名) · [AGT-01](DESIGN_SPEC.md#agt-01--长任务有可理解的状态模型) |
| Chinese body text inherits Latin line height, letter spacing and all-caps labels | No added letter spacing or ALL CAPS for Chinese body text; reading line height starts at 1.7 and the reading column at 32–42em, then check with real content | [TYP-02](DESIGN_SPEC.md#typ-02--中文不能套用英文字体微调) · [TYP-01](DESIGN_SPEC.md#typ-01--字体按职责选择) |
| An auto-generated title overwrites the name the user just typed | Saving content and generating a title may fail independently; a late title must not overwrite a manual rename, and results for a switched or deleted object are discarded | [CMP-04](DESIGN_SPEC.md#cmp-04--自动命名是可编辑的辅助元数据) |

The spec has 42 rules grouped by goals and evidence (CTX), visuals and typography (VIS, TYP, LAY), components and long tasks (CMP, AGT), implementation workflow (RUN), and accessibility and review (A11Y, QA). Each rule states its basis, when it applies and how to check it. Full text: [DESIGN_SPEC.md](DESIGN_SPEC.md).

![Three facets of one research task: reading hierarchy, workspace organization, and save failure with recovery.](docs/assets/principles.svg)

The image applies these rules to one "organize a research note" screen: reading hierarchy, workspace layout, and recovery after a failed save. [About the example](docs/EXAMPLES.md)

## Install

The Skill is a whole directory (a `SKILL.md` entry plus references, assets, templates and scripts). Pick one method.

**skills CLI** (Claude Code, Codex, Cursor and others; needs Node.js)

```bash
npx skills add Hai-qq/humanist-frontend
```

Installs into the current project by default and asks which agents to target; use `-a claude-code` to pick one and `-g` for your user directory. The CLI is maintained by [vercel-labs/skills](https://github.com/vercel-labs/skills).

**Claude Code plugin**

```text
/plugin marketplace add Hai-qq/humanist-frontend
/plugin install humanist-frontend@humanist-frontend
```

**Python installer** (no Node.js; supports Codex, Claude Code and Kimi)

```bash
git clone https://github.com/Hai-qq/humanist-frontend.git
python3 humanist-frontend/scripts/install_skill.py --host claude --project /path/to/project
```

`--host` accepts `codex`, `claude` or `kimi`. The installer only copies files and never overwrites an existing Skill. Upgrades, manual copies and host directories: [docs/INSTALL.md](docs/INSTALL.md) (Chinese).

## Usage

Name the Skill in a task, for example:

```text
Use humanist-frontend to improve reading and saving in this research-notes project.
Keep the existing theme. Settle the content hierarchy and state handling first, then implement.
Check long Chinese text, save failure and recovery, and say which behaviors were not verified.
```

You can also skip the install: read the [spec](DESIGN_SPEC.md), or copy the relevant rules into your project's own design notes using the [template](skills/humanist-frontend/templates/DESIGN.template.md). An existing design system takes precedence.

## Documents

| Topic | Where (Chinese) |
|---|---|
| Every rule with rationale, scope and checks | [Design spec](DESIGN_SPEC.md) |
| Which sources were read, and how far | [Reading guide](research/READING_GUIDE.md) · [Source ledger](research/SOURCE_AUDIT.md) |
| Why a practice was adopted, adapted or dropped | [Evidence and decisions](research/EVIDENCE_AND_DECISIONS.md) |
| How an agent picks rules for a task | [Skill entry](skills/humanist-frontend/SKILL.md) |
| Palette variables | [Tokens](docs/TOKENS.md) |
| Development, checks and evaluation | [Development](docs/DEVELOPMENT.md) · [Validation record](reports/VALIDATION.md) · [Evaluation protocol](evals/README.md) |

## Evidence boundaries

- This is a personal research synthesis. It is not an official Anthropic or Kimi specification, not a joint system from the two companies, and not affiliated with either.
- The spec labels three kinds of content separately: what sources say, the author's synthesis, and original implementation defaults.
- The source ledger has 50 records, including technical references, excerpts and shared sources; it does not mean 50 independent works were read in full. Two full interviews still lack complete transcripts. The source snapshot is dated 2026-09-08, and external sources have not been fully re-checked since.
- Both palettes and the example images are original examples, not official themes, product screenshots, or test results from a shipped application.
- The bundled checks cover generated-file sync, local links, source and rule traceability, install copying, archive manifests and 92 declared solid-color contrast pairs, in 47 unit tests. See the [validation record](reports/VALIDATION.md).
- Not yet run: the 18 Agent evaluation scenarios, loading inside real agent hosts, visual and interaction checks on downstream pages, real OS input methods, screen readers and full-page WCAG review. The project therefore makes no claim that using it improves interfaces.

If a rule fails or misleads in a real project, please [open an issue](https://github.com/Hai-qq/humanist-frontend/issues/new). See [CONTRIBUTING](CONTRIBUTING.md) for adding evidence or rules.

---

<p align="center"><img src="docs/assets/brand/mark.svg" width="144" height="144" alt="Humanist mark: offset frame with a terracotta square"></p>

<p align="center">
  <a href="https://github.com/Hai-qq/humanist-frontend/actions/workflows/validate.yml"><img src="https://github.com/Hai-qq/humanist-frontend/actions/workflows/validate.yml/badge.svg" alt="Package checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-625E56" alt="MIT License"></a>
  <a href="https://github.com/Hai-qq/humanist-frontend/releases"><img src="https://img.shields.io/github/v/release/Hai-qq/humanist-frontend?color=A64B32&amp;label=release" alt="Latest release"></a>
</p>

Display name: **Humanist · 界面设计札记**. The repository, install directory and invocation name stay `humanist-frontend`. [Changelog](CHANGELOG.md) · [Brand](docs/BRAND.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md)

Original work is licensed under the [MIT License](LICENSE). Third-party names, materials and asset boundaries: [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).
