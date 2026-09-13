# 使用、安装与升级

Humanist · 界面设计札记有三种使用方式。展示名称更新后，仓库与 Skill 标识仍为 `humanist-frontend`。

| 目的 | 使用方式 | 是否安装 |
|---|---|---|
| 理解设计方法 | 阅读[完整规范](../DESIGN_SPEC.md)与[来源导读](../research/READING_GUIDE.md) | 无需安装 |
| 形成项目约定 | 从规范选取相关规则，按需填写[设计模板](../skills/humanist-frontend/templates/DESIGN.template.md)，记录调整理由 | 无需安装 |
| 让 Agent 在任务中应用 | 安装下面的完整 Skill 目录，再检查宿主加载 | 需要文件复制 |


## 安装对象

这是目录式设计 Skill 和参考规范，不是前端框架、自动设计服务或 UI 组件库。
所有静态文件可离线读取；可选脚本使用 Python 3.10+ 标准库。没有 API Key、遥测、hook、自动下载或账号操作。

从仓库根目录运行以下命令，选择实际宿主即可：

```bash
python scripts/install_skill.py --host codex --project /path/to/project
python scripts/install_skill.py --host claude --project /path/to/project
python scripts/install_skill.py --host kimi --project /path/to/project
```

路径中的项目必须已经存在。安装器分别复制完整 Skill 到 `.agents/skills/humanist-frontend/`、`.claude/skills/humanist-frontend/`、`.kimi/skills/humanist-frontend/`。
这些映射沿用 2026-09-08 已读取文档；目录复制已测不等于宿主实机加载已测。安装后检查宿主自己的 Skill 列表和工作区信任设置；本包不替用户批准权限。

也可以手工复制整个 `skills/humanist-frontend/`，或解压独立 Skill 包后复制其 `humanist-frontend/`。
不要只复制 SKILL.md：它会引用相邻的 references、assets、templates 和 scripts。
独立包的 SHA256SUMS 放在包根目录，用于校验，不是自动执行脚本。

## 从旧版升级

安装器拒绝覆盖，避免丢失你修改过的规则。先比较新版与已安装目录，保留自己明确需要的定制；备份放在宿主自动发现的 skills 目录之外，避免同时加载两份同名规则。确认后用新版完整目录替换旧目录。

不要覆盖项目自己的 DESIGN.md、业务代码或全局配置。v0.3.0 重组了设计解释与执行入口，没有改变主题变量数值、CSS 前缀或主题选择方式，不需要因此迁移应用样式。以完整目录替换，避免新版入口引用旧版附属文件。

## 调用与范围

可以在正常任务中指定“使用 humanist-frontend”。新建页面按任务选择风格；已有系统默认继承，局部修复不扩成整体改版，只审查就不改源码。

源材料仅在核对出处时按需读，不要求每次任务加载 50 条来源记录。完整使用路径见 [README](../README.md)；规则汇编见 [DESIGN_SPEC](../DESIGN_SPEC.md)。

## 验证边界

本仓库脚本检查文件、元数据、色对与打包完整性；不会替你测试应用路由、视觉效果、真实输入法、读屏或模型遵从。
具体发布时实际跑过什么，以 [验证记录](../reports/VALIDATION.md) 为准。
