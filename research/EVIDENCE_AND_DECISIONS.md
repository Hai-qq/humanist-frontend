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

## v0.2.0 已合入的补读规则

以下为对既有补读材料的整合，没有新增外部阅读。案例观察和本项目扩展分开记录；来源部分可读，并不意味着其所有状态已验证。

| 实际取得材料 | 本项目原创迁移 | 规则与待执行场景 |
|---|---|---|
| K8：原站索引返回的短正文，提及跳过思考 [K8] | 区分快速结果、停止显示与取消执行；检查能力与切换失败 | AGT-04；E15 |
| K9：原帖自动标题描述 [K9] | 手动命名优先；内容与标题分别失败；迟到响应校验对象和版本 | CMP-04；E13 |
| K10-R1：同作者汇编中的关键词匹配章节 [K10-R1] | 建议填入与立即执行分开；不覆盖草稿；遵循适用的组合框键盘模型 | CMP-05；E14 |
| K11：历史付费表达正文 [K11] | 保留品牌语气，同时清楚表达金额、权益、周期和续费；不把动画当付款成功 | COPY-01；E16 |
| A7-C1/C2：主持人发布的同场短片可见转录 [A7-C1] [A7-C2] | 用任务样例验证设计取舍，关注人的操作权；不强制固定迭代轮次 | CTX-06；E18 |
| 两轮补读中有节目说明、短片与下载入口，但没有完整音轨 | 分别记录文字/画面/行为核验；不把发现地址等同于已下载或已读完 | SRC-01；E17 |

映射的机器可读版本在 [rule_traceability.json](rule_traceability.json)。这些场景是评估设计，不是已经跑过的模型或前端测试。

## 仍未用作完整证据的内容

A3 仍只有节目说明/公开节选和音频入口；A7 原访谈仍为 partial，两个短片只能支持各自可见文字。
K6、K7、K10 原帖正文仍未取得；K10-R1 不替代原帖的全文状态。K5 仅有目录列表。
K8 的正文取得路径为原站索引，而非原页直读。各案例图片/动效没有因文字补齐而自动通过视觉核验。

不能用短片补出字体、色号或动效时长；本版不据此改动原主题数值。访问失败不是来源不存在，多个转载入口也不是多个独立实验。

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

[K8]: https://www.uisdc.com/hunter/0221502862.html "Kimi 深度思考跳过入口（原站索引正文）"
[K9]: https://www.uisdc.com/hunter/0221575035.html "Kimi 自动标题案例"
[K10-R1]: https://www.uisdc.com/ai-prompt-design "同作者汇编：关键词匹配章节"
[K11]: https://www.uisdc.com/hunter/0221567725.html "Kimi 历史付费表达案例"
[A7-C1]: https://www.linkedin.com/posts/ahhogan_what-does-it-take-to-shape-an-ai-brand-activity-7341874716992749570-9zGJ "FigBrew 同场短片：创作实践"
[A7-C2]: https://www.linkedin.com/posts/ahhogan_ai-design-activity-7343386927309471744--vXU "FigBrew 同场短片：具体需求与人的主导权"
