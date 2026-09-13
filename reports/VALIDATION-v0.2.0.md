# v0.2.0 验证记录

执行日期：2026-09-08；Python 3.13.5。以下为本版实际运行结果，旧版本日志不作为本版通过依据。

| 检查 | 实际结果 | 范围与证据 |
|---|---|---|
| 当前来源审计、覆盖统计与 Skill 来源副本 | passed | [source-sync.log](source-sync.log)，生成物逐字比较 |
| 主规范与五份权威章节 | passed | [spec-sync.log](spec-sync.log) |
| token JSON 与 CSS | passed | [token-sync.log](token-sync.log) |
| 文件、链接、版本、来源与规则追踪 | passed | [package.log](package.log)，不测试外部 URL 的可达性 |
| 单元测试 | **47 passed** | [unit-tests.log](unit-tests.log)；颜色、结构、来源边界、安装与归档行为 |
| 明暗主题指定色对 | **88/88 passed** | [contrast.log](contrast.log)；仅列明的不透明 sRGB 配对 |
| Skill YAML 实际解析 | passed | [yaml-parse.log](yaml-parse.log)；编写环境的可选 PyYAML，不是运行依赖 |
| 与 v0.1.0 主题兼容 | passed | [theme-compatibility.log](theme-compatibility.log)；除 design_version 外 JSON 内容不变 |
| 临时目录安装 | passed | 单元测试内覆盖三种宿主目录、完整附属文件与拒绝覆盖；不等于宿主实机加载 |
| 双 ZIP 清单、文件对应与确定性 | passed | 单元测试内对临时产物验证逐文件哈希、独立 Skill 对应内容、同环境同输入确定性 |
| 下游浏览器视觉/交互 | not-run | 本仓库是规范与 Skill，没有随包实现待验收的应用 fixture |
| 读屏/真实系统输入法 | not-run | 未使用目标交互环境 |
| Agent 宿主实机运行 | not-run | 未启动 Codex / Claude Code / Kimi 执行设计任务 |
| 18 个 Agent 场景 | not-run | 仅有场景定义与评估协议，不是已经通过的 E2E 测试 |
| 跨模型/用户研究 | not-run | 没有质量提升或优于基线的实验证据 |
| 新音视频转录与画面核验 | not-run | 本轮只合并已有记录；完整访谈转录仍为 0/2 |

没有浏览器或模型测试，不能把这些检查描述为“视觉效果已验证”“完整 WCAG 合规”“兼容所有 Agent”或“审美必然提升”。

自动命名、输入建议等新增规则的单元测试仅检查文档存在、引用和场景关联，并未运行实现这些交互的真实前端。对比度测试不覆盖 DOM 透明层、渐变、图片背景或所有控件状态。

机器可读结果见 [validation.json](validation.json)。历史日志位于 [history](history/README.md)。
