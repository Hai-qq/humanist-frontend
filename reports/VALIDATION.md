# 验证记录

仓库里只保留这一份验证摘要。每次运行的原始输出不提交，发布时作为 Release 附件；v0.3.0 及以前的原始日志见下文“已发布版本”。各版本的记录只说明当时实际跑过什么，不能作为其他版本的通过依据。

## v0.3.0 之后的未发布改动

2026-10-16，macOS（Darwin 25.6.0），Python 3.13.5。GitHub Actions 另在 Python 3.10 与 3.13 上运行这七项。

| 检查 | 命令 | 结果 |
|---|---|---|
| 来源生成物同步 | `python scripts/build_sources.py --check` | passed |
| 规范汇编同步 | `python scripts/build_spec.py --check` | passed |
| token 同步 | `python scripts/build_tokens.py --check` | passed |
| 文件、本地链接、版本、来源与规则追踪、历史哈希、插件市场路径 | `python scripts/validate_package.py` | passed |
| 单元测试 | `python -m unittest discover -s tests -v` | 47 passed |
| 声明的不透明 sRGB 色对 | `python skills/humanist-frontend/scripts/check_contrast.py` | 92/92 passed |
| 双 ZIP 打包 | `python scripts/build_release.py --output <仓库外目录>` | passed |

### 安装方式（手动实测，CI 不运行）

| 方式 | 做法 | 结果 |
|---|---|---|
| skills CLI 1.7.2 | 在临时空项目运行 `npx skills add Hai-qq/humanist-frontend -a claude-code -a codex -y`，来源为当时的 GitHub main | 识别到 1 个 Skill；完整目录装到 `.agents/skills/humanist-frontend/`，与仓库 `skills/humanist-frontend/` 逐文件一致；`.claude/skills/humanist-frontend` 是指向它的软链接；装好的对比度脚本可运行；用户目录 `~/.agents` 未改动 |
| skills CLI 1.7.2 | 加入 `.claude-plugin/marketplace.json` 后，对本地仓库运行 `npx skills add <仓库路径> --list` | 仍只识别 1 个 Skill，没有重复 |
| Claude Code 2.1.289 插件 | 设置 `CLAUDE_CONFIG_DIR=<临时目录>` 隔离个人配置，运行 `claude plugin validate .`（含 `--strict`）、`claude plugin marketplace add <仓库路径>`、`claude plugin install humanist-frontend@humanist-frontend` | 校验通过，安装成功；`claude plugin details` 列出 `Skills (1) humanist-frontend` |
| skills CLI 1.7.2 | 推送本 PR 分支后，在另一个空项目运行 `npx skills add https://github.com/Hai-qq/humanist-frontend/tree/<分支> -a claude-code -y` | 识别到 1 个 Skill；只选 Claude Code 时直接复制到 `.claude/skills/humanist-frontend/`，与仓库逐文件一致 |
| Claude Code 2.1.289 插件 | 同样隔离配置，从 GitHub 运行 `claude plugin marketplace add Hai-qq/humanist-frontend@<分支>` 与 `claude plugin install humanist-frontend@humanist-frontend` | 安装成功；版本号取自提交 SHA；缓存中是整个仓库（约 1.7 MB），`claude plugin details` 列出 `Skills (1) humanist-frontend` |
| README 规则链接 | 用 GitHub 的 HTML 渲染接口取得分支上的 DESIGN_SPEC.md，对照两份 README 里的 7 个规则锚点 | 全部存在 |

这些只说明文件被正确复制、插件被正确登记，没有启动 Agent 会话确认模型会调用这个 Skill。安装测试都在临时目录与隔离配置中进行，结束后不保留。

### 未执行

- 18 个 Agent 评估场景：只有场景定义与评估协议。
- 在 Codex、Claude Code、Kimi 中实际调用 Skill 完成设计任务。
- 下游页面的浏览器视觉与交互、真实系统输入法、读屏、整页 WCAG 验收。
- 跨模型对照或用户研究；没有“质量提升”“优于基线”的实验证据。
- 重新核验全部外部来源、新的音视频转录与画面核验。

对比度检查只覆盖列明的不透明色对，不覆盖透明层、渐变、图片背景或所有控件状态。

## 已发布版本

| 版本 | 日期 | 当时的结果 | 原始输出 |
|---|---|---|---|
| v0.3.0 | 2026-09-13 | Python 3.12.14；来源、规范、token 同步与包检查通过；47 项测试通过；88/88 声明色对通过（重新设计配色之前） | [v0.3.0 标签下的 reports/](https://github.com/Hai-qq/humanist-frontend/tree/v0.3.0/reports) 中的 `v0.3.0-check-*.log`、`validation.json`；同样包含在 [Release](https://github.com/Hai-qq/humanist-frontend/releases/tag/v0.3.0) 的完整仓库 ZIP 中 |
| v0.2.0 | 2026-09-08 | Python 3.13.5；同上各项通过，47 项测试，88/88 色对；SKILL.md 用 PyYAML 解析通过；主题数值与 v0.1.0 一致。首次开源整理时另用 Python 3.9.6 复跑通过 | 同一位置的 `VALIDATION-v0.2.0.md`、`*-sync.log`、`unit-tests.log`、`local-*.log`、`OPEN_SOURCE_REVIEW.md` |
| v0.1.0 | 2026-09-08 | 24 项测试、88/88 色对 | 同一位置的 `history/v0.1.0/` |
