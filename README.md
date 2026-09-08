# Humanist Frontend

面向 Agent 的前端设计规范与 Skill。参考 Anthropic / Claude / Kimi 的公开设计资料，形成适合阅读、研究、创作与软件工作台的原创实施规则。

本项目是独立规范，与参考品牌无官方隶属关系。默认尊重已有设计系统；新项目可选择温暖阅读型 `editorial-warm` 或清晰轻盈型 `precise-light`。强调信息层级、组件状态、真实反馈、中文排版与可验证实现。

版本：**0.2.0**。资料快照与整合日期：2026-09-08。

## 使用入口

| 需要 | 入口 |
|---|---|
| 让 Agent 执行 | [Skill](skills/humanist-frontend/SKILL.md) |
| 阅读或修改规范 | [完整规范](DESIGN_SPEC.md) |
| 安装与升级 | [安装说明](docs/INSTALL.md) |
| 核对设计依据 | [证据与决策](research/EVIDENCE_AND_DECISIONS.md) / [来源记录](research/SOURCE_AUDIT.md) |
| 检查本包质量 | [本地复验与内容审查](reports/OPEN_SOURCE_REVIEW.md) / [评估场景](evals/README.md) |

## 安装到项目

复制整个 `skills/humanist-frontend/`，不要只复制 SKILL.md，否则会丢失按需读取的规范与资产。静态指导无需 API Key、网络服务或新前端框架。

先获取仓库：

```bash
git clone https://github.com/Hai-qq/humanist-frontend.git
cd humanist-frontend
```

在本仓库运行，目标必须是已经存在的项目目录：

```bash
# 任选目标工具；安装器只复制本地文件，不运行网络命令、不覆盖已有目录。
python scripts/install_skill.py --host codex --project /path/to/project
python scripts/install_skill.py --host claude --project /path/to/project
python scripts/install_skill.py --host kimi --project /path/to/project
```

分别复制到项目的 `.agents/skills/`、`.claude/skills/`、`.kimi/skills/`。目录依据相关官方文档；这是静态文件安装支持，不是本包已经在每个宿主完成了实机认证。加载后检查工具自己的 Skill 列表；企业策略、工作区信任和宿主版本可能影响启用。

官方目录说明：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[Kimi CLI](https://moonshotai.github.io/kimi-cli/en/customization/skills.html)。

其他 Agent 可直接读取 `SKILL.md` 并跟随相对路径；不保证它们都自动识别相同目录或命令。未授权时，Agent 不应自行修改用户全局配置或发布仓库。

## 调用示例

```text
使用 humanist-frontend，为当前项目实现中文研究笔记工作台。
先读取现有项目规则与组件；已有主题优先。
只修改笔记列表、编辑器和保存反馈，不修改权限或后端接口。
完成实际代码与可运行的检查，明确哪些视觉或交互未能验证。
```

```text
使用 humanist-frontend 审查当前设置页，不修改代码。
重点看中英文长文本、键盘焦点、错误后恢复和视觉层级。
给出可复现的问题，不把个人风格偏好当成缺陷。
```

自然语言也可以触发；具体选择和命令由宿主决定。本 Skill 不要求绑定某个模型版本。

## 使用原创 token

只在新建或已授权改版时导入；已有系统建议做语义映射而非覆盖。

```html
<html lang="zh-CN" data-hf-profile="editorial-warm" data-theme="light">
  <!-- 引入项目实际位置下的 tokens.css -->
</html>
```

```css
.workspace {
  background: var(--hf-canvas);
  color: var(--hf-text);
  font-family: var(--hf-font-ui);
}
.primary-action {
  background: var(--hf-action);
  color: var(--hf-on-action);
}
```

品牌色与操作色分开；`border-subtle` 只用于非必要分隔，输入轮廓使用 `border-control`。默认 2 种方向 × 明暗 2 种模式；没有要求暗色的项目不必额外增加维护范围。这些是原创实现起点，不是官方精确抽取值，也不宣称完整 DTCG 兼容。

## 本地验证

Python 3.10+；脚本只使用标准库。以下操作只检查本包，不运行第三方安装器：

```bash
python scripts/build_sources.py --check
python scripts/build_spec.py --check
python scripts/build_tokens.py --check
python scripts/validate_package.py
python -m unittest discover -s tests -v
python skills/humanist-frontend/scripts/check_contrast.py
```

修改 JSON 后先执行 `python scripts/build_tokens.py` 更新 CSS。对比度脚本只检查列明的不透明 sRGB 色对，不能证明整页 WCAG 合规。

## 来源与验证范围

来源台账保留 50 条资料记录，并区分正文、节选、未取得材料与共同来源；详见 [覆盖统计](research/coverage.json) 和 [来源记录](research/SOURCE_AUDIT.md)。这些是随包研究记录，本次发布仅抽查部分公开页面，未重新核验全部资料。规范中的主题数值属于原创默认，不代表官方 token。

本地检查覆盖结构、生成物一致性、安装、打包及列明的 88 个纯色色对。18 个 Agent 评估场景尚未执行，也未完成宿主实机加载、下游页面视觉、真实输入法或读屏测试。不能据此宣称视觉质量提升或整页 WCAG 合规。

版本变化见 [CHANGELOG](CHANGELOG.md)，补读整合过程见 [合并说明](docs/MERGE_NOTES.md)，历史材料保留在 [研究归档](research/history/README.md)。

## 本地重新打包

完成上面的检查后，运行：

```bash
python scripts/build_release.py --output ../releases
```

输出完整仓库 ZIP、独立 Skill ZIP 与外部 SHA-256 校验文件。两个 ZIP 各带逐文件 `SHA256SUMS`。默认拒绝覆盖；只有确实需要覆盖同名产物时才加 `--overwrite`。输出目录必须在源码目录之外。

同一源码快照、Python/zlib 环境下打包使用固定文件顺序与时间字段；日志变动会正常改变校验值。打包脚本本身不替代测试、浏览器验收或宿主加载。

## 维护

修改规范的权威入口为 `skills/humanist-frontend/references/01-05`；`DESIGN_SPEC.md` 是便于通读的汇编。更新后运行 `python scripts/build_spec.py`。来源以 `research/sources.json` 为入口，运行 `python scripts/build_sources.py` 同步当前审计、覆盖统计和独立 Skill 的来源文件。不要形成内容矛盾的两份规范。

来源更新可能改变建议；新增规则需交代适用范围、证据或原创假设和验收方法。新增字体/图标/截图/第三方代码须核对许可，不能直接复制品牌资产。

原创部分使用 [MIT](LICENSE)，第三方名称与素材的边界见 [声明](THIRD_PARTY_NOTICES.md)。
