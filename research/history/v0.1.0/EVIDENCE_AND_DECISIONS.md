# 证据如何转成规则

本表记录主动保留与拒绝的部分，避免把文章收集误当成规则验证。规则标识可在 DESIGN_SPEC.md 和 Skill references 中检索。

| 问题 | 已读依据 | 本项目决定 | 规则 |
|---|---|---|---|
| 人文气质是否等于米白和衬线 | 原团队解释的是品牌整体表达，而非单个色值 [A1] [A2] | 用内容、字阶与交互清晰度落实气质，不输出心理效果承诺 | CTX-03 / CTX-05 |
| Anthropic 到底使用哪套字体 | 原案例与产物 Skill 字体不同 [A1] [S1] | 区分产品/年代/用途；新项目字体是自己的选择 | TYP-01 |
| 是否一律禁止 Inter、系统字 | Kimi 明确采用 Inter，历史提示示例存在相反偏好 [K1] [T1] [T2] | 不继承普遍禁令，以职责和项目要求判断 | CTX-02 |
| 是否一律要 Claude 色调 | 当前官方通用 Skill 强调服从具体 brief [S2] | 预设可选，已有系统优先 | VIS-01 |
| 社区规范是否等于生产实测 | Claude DESIGN.md 自标 alpha，范围是营销站，且存在“不要记录 hover”等绝对指令 [S3] | 使用结构化组织思路，不继承未验证事实与不合理禁令 | CTX-03 / CMP-01 |
| Kimi 是否所有界面都品牌蓝 | 品牌手册与 CLI CSS 是不同层次/产品 [K1] [S5] | 产品类型与品牌表达分开；不推定全站统一色板 | VIS-01 |
| 主题预设能否直接成为整个产品 | tweakcn 提供变量，Dembrandt 输出观察值并列出限制 [S4] [S9] | 仍须定义信息架构、交互与状态 | VIS-02 / RUN-03 |
| 漂亮的研究页面是否允许改结论 | Researcher 作者讨论信息保真与表现的取舍 [K3] | 信息不得为版式失真，图表/来源必须可理解 | DAT-01 |
| Good Friction 是否越多越好 | A3 只有可读节选，不能扩张为完整实验结论 | 自行按风险放置确认，不强制每次询问 | AGT-03 |
| 品牌色是否一定适合白字按钮 | 品牌值 + WCAG 对比度公式 [S1] [K1] [N2] | 原创深色操作色与品牌色分离，提供可复算结果 | VIS-03 |
| 44px 是否 AA 统一门槛 | AA 2.5.8 的数值是 24px，并有例外 [N4] | 分清标准底线与本包触屏推荐 | A11Y-01 |
| Agent 是否每次读取所有资料 | Agent Skills 采用元数据与按需正文/附属内容 [N1] | 短入口 + 任务路由；来源核验时才加载 ledger | SKILL.md |
| 工程是否只要生成一张好截图 | 官方改版案例有共享实现、影响范围与实际检查 [K4] | 交付代码和真实测试证据，区分没运行和通过 | RUN-04 / QA-04 |

## 未采纳为证据的内容

A7 与 K5–K11 未取得完整正文/转录；A3 只有公开节选。它们留在来源记录中，但不承担硬规则的证明。K5 是合集入口，不是已经阅读所有子帖的证据。未读取的图片没有被用于推算字号、边距或动画时间。

## 规范不是结果证明

本包尚未做跨模型随机化对照或真实用户研究。不得把参考项目的宣传语、模型生成例子或本包验收通过，转写成“必然提升审美/转化率/生产可靠性”。后续可使用 evals 的场景与盲评流程测试。

[A1]: https://geist.co/work/anthropic "Geist — Anthropic"
[A2]: https://www.thesubtext.online/all/anthropic-interview "The Subtext — Anthropic Brand Team Interview"
[S1]: https://github.com/anthropics/skills/tree/main/skills/brand-guidelines "anthropics/skills — brand-guidelines"
[K1]: https://www.kimi.ai/zh-hans/resources/kimi-brand "Kimi 品牌手册"
[T1]: https://claude.com/blog/improving-frontend-design-through-skills "Improving frontend design through Skills"
[T2]: https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics "Prompting for frontend aesthetics"
[S2]: https://github.com/anthropics/skills/tree/main/skills/frontend-design "anthropics/skills — frontend-design"
[S3]: https://github.com/voltagent/awesome-design-md/blob/main/design-md/claude/DESIGN.md "VoltAgent/awesome-design-md — Claude DESIGN.md"
[S5]: https://github.com/MoonshotAI/kimi-cli/tree/main/web "MoonshotAI/kimi-cli — web/"
[S4]: https://github.com/jnsahaj/tweakcn "tweakcn — Claude 主题"
[S9]: https://github.com/dembrandt/dembrandt "dembrandt/dembrandt"
[K3]: https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c "The Bitter Lessons Behind Kimi Researcher’s taste"
[N2]: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html "WCAG 2.2 — Contrast Minimum"
[N4]: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html "WCAG 2.2 — Target Size Minimum"
[N1]: https://agentskills.io/specification "Agent Skills specification"
[K4]: https://www.kimi.ai/zh-hans/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli "用 Kimi Code CLI 交付 Moonshot AI 的一次重构"
