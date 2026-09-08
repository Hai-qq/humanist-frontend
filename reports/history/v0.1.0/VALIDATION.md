# 验证记录

日期：2026-09-08。以下是本交付包在当前环境中实际执行的检查，不代表下游应用或 Agent 已通过验证。

| 检查 | 结果 | 范围 |
|---|---|---|
| token JSON 与生成 CSS 一致 | passed | scripts/build_tokens.py --check |
| 主规范与五份权威章节一致 | passed | 单元测试比较生成文本 |
| 必要文件、本地 Markdown 链接、来源 ID 和记录 | passed | 包内文件与元信息，不是外部 URL 全部可访问 |
| Python 单元测试 | 24 passed | 颜色计算、错误输入、生成物同步、命令退出码、安全复制安装等 |
| 明暗主题指定色对 | 88/88 passed | 2 个方向 × 2 种模式 × 22 组不透明 sRGB 色对 |
| SKILL.md YAML 解析 | passed | 在编写环境使用 PyYAML 实际解析；未使用它验证宿主全部行为 |
| 安装到临时项目 | passed | 三种目录复制、附属文件完整、已存在文件拒绝覆盖；不是宿主实机加载 |
| 浏览器视觉与交互 | not-run | 当前 Playwright 指向的 Chromium 可执行文件缺失；未下载浏览器 |
| 读屏软件、真实系统输入法 | not-run | 没有目标交互环境 |
| Claude Code / Codex / Kimi 实机执行 | not-run | 未在这些宿主里运行本 Skill |
| 第三方仓库构建/安全审计 | not-run | 本次是设计相关资料阅读，不是安装审计 |
| 12 个 Agent 场景与跨模型对照 | not-run | 已提供评估设计，未调用模型 API |

对比度反例：白字在 #D97757 上 3.1218887813:1，在 #007CFF 上 3.9421364544:1。它们没有被批准为本包普通白字按钮；本包另外定义更深的操作色。反例计算不等于对 Anthropic 或 Kimi 真实页面的合规判定。

没有执行浏览器或模型测试，就不能声称“视觉已验证”“完整 WCAG 合规”“与所有 Agent 完全兼容”或“优于某个基线”。

实际命令输出见 [check-1.log](check-1.log)、[check-2.log](check-2.log)、[check-3.log](check-3.log)、[check-4.log](check-4.log)。机器可读记录见 [validation.json](validation.json)。
