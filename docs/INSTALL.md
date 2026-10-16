# 使用、安装与升级

Humanist · 界面设计札记有三种使用方式。展示名称更新后，仓库与 Skill 标识仍为 `humanist-frontend`。

| 目的 | 使用方式 | 是否安装 |
|---|---|---|
| 理解设计方法 | 阅读[完整规范](../DESIGN_SPEC.md)与[来源导读](../research/READING_GUIDE.md) | 无需安装 |
| 形成项目约定 | 从规范选取相关规则，按需填写[设计模板](../skills/humanist-frontend/templates/DESIGN.template.md)，记录调整理由 | 无需安装 |
| 让 Agent 在任务中应用 | 安装下面的完整 Skill 目录，再检查宿主加载 | 需要文件复制 |


## 安装对象

这是目录式设计 Skill 和参考规范，不是前端框架、自动设计服务或 UI 组件库。
所有静态文件可离线读取；可选脚本使用 Python 3.10+ 标准库。Skill 本身没有 API Key、遥测、hook、自动下载或账号操作。

不要只复制 SKILL.md：它会引用相邻的 references、assets、templates 和 scripts。下面三种方式都会安装完整目录，任选其一。

### skills CLI

适用于 Claude Code、Codex、Cursor 等支持 Agent Skills 的工具，需要 Node.js。在项目根目录运行：

```bash
npx skills add Hai-qq/humanist-frontend
```

CLI 会克隆本仓库、识别 `skills/humanist-frontend/`，再询问要装给哪些 Agent。常用参数：`-a claude-code`、`-a codex` 指定 Agent，`-g` 装到用户目录，`-y` 跳过确认，`--copy` 复制而不是建软链接。

项目级安装会在项目根目录写入 `skills-lock.json`。只选 Claude Code 时，完整目录直接复制到 `.claude/skills/humanist-frontend/`；同时选了 Codex 等共用 `.agents/skills/` 的 Agent 时，完整目录放在 `.agents/skills/humanist-frontend/`，Claude Code 那份是指向它的软链接（加 `--copy` 改为各自复制）。这个 CLI 由 [vercel-labs/skills](https://github.com/vercel-labs/skills) 维护，参数、目录以及它自己的网络访问与统计行为以它的文档为准。

### Claude Code 插件

仓库根目录的 `.claude-plugin/marketplace.json` 把本仓库声明为插件市场，其中只有 `humanist-frontend` 一个插件。在 Claude Code 会话里运行：

```text
/plugin marketplace add Hai-qq/humanist-frontend
/plugin install humanist-frontend@humanist-frontend
```

也可以在终端运行 `claude plugin marketplace add Hai-qq/humanist-frontend` 和 `claude plugin install humanist-frontend@humanist-frontend`。插件默认装到用户范围，Skill 以 `humanist-frontend:humanist-frontend` 的名字出现。插件来源是仓库根目录，Claude Code 会把整个仓库（约 1.7 MB）复制到插件缓存，但只加载其中的 Skill。插件不设固定版本号，Claude Code 按提交记录判断更新；第三方市场默认不自动更新，可运行 `/plugin marketplace update humanist-frontend` 手动拉取。

### Python 安装器

不需要 Node.js，支持 Codex、Claude Code 与 Kimi。从仓库根目录运行，选择实际宿主即可：

```bash
python scripts/install_skill.py --host codex --project /path/to/project
python scripts/install_skill.py --host claude --project /path/to/project
python scripts/install_skill.py --host kimi --project /path/to/project
```

路径中的项目必须已经存在。安装器分别复制完整 Skill 到 `.agents/skills/humanist-frontend/`、`.claude/skills/humanist-frontend/`、`.kimi/skills/humanist-frontend/`。
这些映射沿用 2026-09-08 已读取文档；目录复制已测不等于宿主实机加载已测。安装后检查宿主自己的 Skill 列表和工作区信任设置；本包不替用户批准权限。

### 手工复制

也可以手工复制整个 `skills/humanist-frontend/`，或解压 [Release](https://github.com/Hai-qq/humanist-frontend/releases/latest) 里的独立 Skill 包后复制其 `humanist-frontend/`。
独立包的 SHA256SUMS 放在包根目录，用于校验，不是自动执行脚本。

## 从旧版升级

用 skills CLI 安装的，运行 `npx skills update humanist-frontend`；用插件安装的，见上文的 `/plugin marketplace update`。下面针对 Python 安装器和手工复制。

安装器拒绝覆盖，避免丢失你修改过的规则。先比较新版与已安装目录，保留自己明确需要的定制；备份放在宿主自动发现的 skills 目录之外，避免同时加载两份同名规则。确认后用新版完整目录替换旧目录。

不要覆盖项目自己的 DESIGN.md、业务代码或全局配置。v0.3.0 重组了设计解释与执行入口，没有改变主题变量数值、CSS 前缀或主题选择方式，不需要因此迁移应用样式。以完整目录替换，避免新版入口引用旧版附属文件。

v0.3.0 之后的版本重新设计了两套主题的色值（见 [更新记录](../CHANGELOG.md)），并新增 `surface-inverse`、`on-inverse`。项目里已经复制了 `tokens.css` 的，升级前先比较差异：editorial-warm 的主要按钮从陶土色改为墨色，`on-action` 随之变化。

## 调用与范围

可以在正常任务中指定“使用 humanist-frontend”。新建页面按任务选择风格；已有系统默认继承，局部修复不扩成整体改版，只审查就不改源码。

源材料仅在核对出处时按需读，不要求每次任务加载 50 条来源记录。完整使用路径见 [README](../README.md)；规则汇编见 [DESIGN_SPEC](../DESIGN_SPEC.md)。

## 验证边界

本仓库脚本检查文件、元数据、色对与打包完整性，以及 `marketplace.json` 指向的 Skill 目录是否存在；不会替你测试应用路由、视觉效果、真实输入法、读屏或模型遵从。skills CLI 与插件两种安装方式是手动实测的，CI 不运行它们。
具体发布时实际跑过什么，以 [验证记录](../reports/VALIDATION.md) 为准。
