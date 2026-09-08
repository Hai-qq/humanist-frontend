<p align="center">
  <img src="docs/assets/logo.png" width="112" height="112" alt="Humanist Frontend：带陶土色折角的小写 h 标识">
</p>

<h1 align="center">Humanist Frontend</h1>

<p align="center"><strong>让 Agent 写出的界面，更适合人使用。</strong></p>
<p align="center">前端设计 Skill · 中文排版 · 真实交互 · 两套可选主题</p>

<p align="center">
  <a href="https://github.com/Hai-qq/humanist-frontend/actions/workflows/validate.yml"><img src="https://github.com/Hai-qq/humanist-frontend/actions/workflows/validate.yml/badge.svg" alt="包检查状态"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-625E56?style=flat" alt="MIT License"></a>
  <a href="https://github.com/Hai-qq/humanist-frontend/releases"><img src="https://img.shields.io/github/v/release/Hai-qq/humanist-frontend?color=A64B32&amp;label=release" alt="最新版本"></a>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="DESIGN_SPEC.md">设计规范</a> ·
  <a href="https://github.com/Hai-qq/humanist-frontend/releases/latest">下载 Skill</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

---

Humanist Frontend 是一套面向编码 Agent 的设计规范和可安装 Skill，适合阅读页、研究工具、创作界面与软件工作台。参考 Anthropic、Claude 和 Kimi 的公开设计资料，关注信息层级、中文排版与可恢复的交互。

**已有项目沿用原设计系统；新项目按需要选择主题。** 无需 API Key，也不要求换框架。

## 两种方向，同一套交互原则

![两套主题的静态示意：温暖阅读型与清晰轻盈型，使用仓库实际浅色色值。](docs/assets/themes.svg)

| 温暖阅读型 · `editorial-warm` | 清晰轻盈型 · `precise-light` |
|---|---|
| 纸色背景、温暖强调、舒展的阅读层次 | 轻盈中性色、蓝色操作、清晰的工作区 |
| 适合长文、笔记与研究阅读 | 适合编辑器、设置与任务工作台 |

预览为静态设计示意，不是已实现的应用。两套主题均附明暗色值；[查看 token 用法](docs/TOKENS.md)。

## 它会帮助 Agent 做什么

- **按内容设计**：区分阅读页、工作台和事务页，用真实长文本检验布局。
- **处理真实状态**：保存失败保留输入，旧请求不覆盖新对象，取消状态以实际结果为准。
- **照顾中文使用**：检查中英混排、长文件名、组合输入与键盘操作。
- **按需读取规范**：入口保持简短，字体、组件、工程和验收细则分别加载。

## 快速开始

需要 Python 3.10+。先下载源码：

```bash
git clone https://github.com/Hai-qq/humanist-frontend.git
cd humanist-frontend
```

选择你的工具，将 `/path/to/project` 换成已有项目目录：

```bash
# Codex
python3 scripts/install_skill.py --host codex --project /path/to/project

# Claude Code
python3 scripts/install_skill.py --host claude --project /path/to/project

# Kimi CLI
python3 scripts/install_skill.py --host kimi --project /path/to/project
```

安装器只复制本地文件，拒绝覆盖已有 Skill。安装后在宿主工具中检查是否加载。[手动安装与升级 →](docs/INSTALL.md)

然后在项目里告诉 Agent：

```text
使用 humanist-frontend，为当前项目实现中文研究笔记工作台。
沿用现有组件与主题，只修改笔记列表、编辑器和保存反馈。
完成实现并检查主要操作路径，说明未验证项。
```

只需审查时，可以说：`使用 humanist-frontend 审查当前设置页，不修改代码。`

## 文档导航

| 你想做什么 | 去哪里 |
|---|---|
| 直接使用 Skill | [Skill 入口](skills/humanist-frontend/SKILL.md) |
| 通读设计规则 | [完整设计规范](DESIGN_SPEC.md) |
| 接入颜色、字体和主题 | [Token 使用](docs/TOKENS.md) |
| 了解规则为什么这样定 | [证据与决策](research/EVIDENCE_AND_DECISIONS.md) |
| 核对来源和阅读范围 | [来源记录](research/SOURCE_AUDIT.md) |
| 修改、检查或打包 | [开发指南](docs/DEVELOPMENT.md) |
| 查看变化 | [更新记录](CHANGELOG.md) |

## 质量与边界

包检查覆盖生成物同步、文件与引用、安装和打包；当前包含 **47 项测试**与 **88 个不透明色对检查**。[复验报告](reports/OPEN_SOURCE_REVIEW.md)

18 个 Agent 评估场景尚未执行；包检查不代表宿主实机认证、页面视觉验收或整页 WCAG 合规。[评估协议](evals/README.md)

## 一起改进

欢迎提交真实项目中遇到的问题、可复现的交互缺陷和有依据的规则改进。

[报告问题](https://github.com/Hai-qq/humanist-frontend/issues/new) · [贡献约定](CONTRIBUTING.md) · [项目视觉标识](docs/BRAND.md)

---

原创部分采用 [MIT License](LICENSE)。本项目与 Anthropic、Claude、Kimi 无官方隶属关系；第三方品牌与素材说明见 [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md)。
