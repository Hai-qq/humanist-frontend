# 来源导读：设计材料如何进入规范

本项目围绕 Anthropic 与 Kimi 的公开设计实践整理材料。这里是阅读入口；每条来源的读取日期、证据类型和访问范围以 [sources.json](sources.json) 为准。以下概述沿用已有研究记录，2026-09-13 的文档重组没有增加新的全文阅读或访谈转录。

## 按问题选择材料

| 你关心的问题 | 材料及其性质 | 如何进入规范 |
|---|---|---|
| 人文表达如何进入技术品牌 | [Geist 的 Anthropic 项目](https://geist.co/work/anthropic)；[The Subtext 品牌团队访谈](https://www.thesubtext.online/all/anthropic-interview)：项目说明与团队观点 | 提炼字体职责、内容与表达的协调；不推导心理效果或当前产品唯一字体 |
| 品牌表达与功能布局怎样并存 | [Kimi 品牌手册](https://www.kimi.ai/zh-hans/resources/kimi-brand)：官方品牌资料 | 区分基础网格、表现力网格与操作区；不把整套品牌素材直接打包复刻 |
| 研究输出怎样保持信息可理解 | [Kimi Researcher 设计记录](https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c)：作者案例 | 关注信息保真、结构和渐进披露；不据文章宣称已测量阅读效率 |
| 设计怎样落入已有代码 | [Kimi 官网重构案例](https://www.kimi.ai/zh-hans/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli)：公开实施案例 | 采用既有规范、共享组件与检查方法；不绑定特定模型或框架 |
| 辅助操作怎样保留人的编辑权 | 自动标题、建议匹配、快速入口与付费文案案例，详见[证据与决策](EVIDENCE_AND_DECISIONS.md) | 从观察迁移到恢复、竞态和状态约束；新增工程约束属于作者推导 |
| 人如何主导设计过程 | FigBrew 同场短片的可见转录及其他访谈材料，见[来源台账](SOURCE_AUDIT.md) | 仅用已取得节选启发任务样例与取舍方法；不扩充为完整访谈结论 |

## 三种证据角色

**设计材料**说明特定团队在特定场景下的选择，包括品牌指南、团队访谈与产品案例。它们可以解释意图，但不自动证明普适效果。

**技术依据**包括 WCAG、ARIA、字体与浏览器行为文档，用于约束可读性、交互语义和实现。它们不代表两家公司的私有规范。

**作者综合**将材料中的可迁移方法转成自己的规则。例如案例中的自动标题启发辅助命名；“用户改名后旧请求不得覆盖”属于本项目的工程扩展。

## 保留的限制

50 条记录含共同来源与不同读取范围，不是 50 个独立验证。两段完整访谈的完整转录仍未取得；同场短片不等于读完整场。部分原帖未取得正文，文字阅读也不等于图片、动效或后端行为核验。

查当前状态看 [来源台账](SOURCE_AUDIT.md)，查迁移理由看 [证据与决策](EVIDENCE_AND_DECISIONS.md)，查执行条款看[完整规范](../DESIGN_SPEC.md)。历史记录保留在 history 中，不改写为当前完成状态。
