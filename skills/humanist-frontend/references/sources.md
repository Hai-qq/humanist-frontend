# 来源阅读记录 · 当前合并状态

版本 0.3.0；来源快照 2026-09-08；合并日期 2026-09-08。

整合已有来源记录与两轮补读笔记；本轮未新增外部阅读、转录或视觉核验。

共 **50 条来源记录**：原目录 32 条、技术补充 15 条、新补读材料 3 条。镜像、同场短片与同案例汇编保留共同来源关系，数量不代表独立证据数量。

## 原目录覆盖

| 状态 | 数量 | 含义 |
|---|---:|---|
| `index-read` | 1 | 只读目录列表，不递归代表子页。 |
| `partial` | 2 | 整体未读完，仅节选、节目说明或关联短片可读。 |
| `read` | 25 | 已读到正文或条目列明的技术文件；不代表整仓库/全站/全部图片。 |
| `read-via-index` | 1 | 搜索工具返回的原站短正文已读；原页直读未成功。 |
| `unavailable` | 3 | 目标正文未取得；片段/替代入口在 read_scope 中说明。 |

完整访谈转录：**0 / 2**。已读同场短片转录：**2 段**。尚缺原帖正文：K6, K7, K10。

文字、图片/动效、运行实现的核验是不同维度；原目录的 read 不等于全部图片、整个仓库或所有链接都读完。
`used_as_normative_evidence` 仅是规则追踪标记，不是效果证明或官方背书。新补读的案例与短片作为设计启发，扩展的异常处理/竞态要求属于本项目原创。
文件 Blob SHA 不是提交 SHA；未固定的页面/分支可能变化。本合并版没有重新执行下载或转录。

完整仓库的 `research/history/` 保留旧快照与补读附件；`research/inputs.json` 记录归档字节校验。历史文件内的旧统计不应替代本表。

## 全部条目

### A1 · Geist — Anthropic

- 来源：https://geist.co/work/anthropic
- 状态：`read`；性质：`primary-case`；来源组：`A1`。
- 实际读取范围：案例正文；图片资源访问失败，未做逐图尺寸测量
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：原团队解释字体配对、温暖色调、手工视觉与功能化组件的关系。

边界：借鉴内容与品牌表达的协调；不宣称重建当前 Claude 的 CSS。

### A2 · The Subtext — Anthropic Brand Team Interview

- 来源：https://www.thesubtext.online/all/anthropic-interview
- 状态：`read`；性质：`primary-interview`；来源组：`A2`。
- 实际读取范围：品牌团队访谈正文（页面重复段落去重）
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2025-06-30。

提炼：公司品牌与 Claude 产品表达服务不同对象；强调克制而有人的表达。

边界：把品牌目标写进 brief；不把受访者的体验判断当成因果实验。

### A3 · How Anthropic Is Redesigning Human–AI Interaction

- 来源：https://promptedwithcam.substack.com/p/how-anthropic-is-redesigning-humanai
- 状态：`partial`；性质：`primary-excerpt`；来源组：`A3`。
- 实际读取范围：原文章公开节选；官方节目说明和章节目录；同一期 Podbay 播放器与下载入口。未取得完整字幕或音轨。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum, alternative-media-recovery。
- 发布：2025-12-02。

提炼：公开介绍讨论协作及适当的操作阻力。

边界：这些入口对应同一期节目，不是多份独立证据。章节起点不是逐字稿时间戳；未下载不等于音源不存在。只作背景线索。

同一期节目的其他入口（入口定位不等于下载成功）：

- [完整视频入口](https://www.youtube.com/watch?v=GBxs67h4_lo) — `metadata-only`。
- [官方 Simplecast 节目页](https://prompted-ai-people-and-the-creative-spark.simplecast.com/episodes/the-hidden-design-choices-behind-claude-with-joel-lewenstein-head-of-product-design-at-anthropic-8EexA0Ti) — `description-and-chapters-read`。
- [Podbay 同期播放器](https://podbay.fm/p/prompted-ai-people-and-the-creative-spark/e/1764673200) — `description-and-download-link-read`。
- [Podscan 同期页面](https://podscan.fm/podcasts/prompted-ai-people-and-the-creative-spark/episodes/the-hidden-design-choices-behind-claude-with-joel-lewenstein-head-of-product-design-at-anthropic) — `metadata-only; full transcript not available in prior read`。
- [公开 RSS](https://feeds.simplecast.com/MWJ0vTGb) — `route-found; body-not-read`。
- [播放器提供的 MP3 路由](https://evrstrck.com/functions/v1/prefix-track/ddc3a8c4d3b5ee74/afp-922686-injected.calisto.simplecastaudio.com/9536941d-4b0f-427b-8265-df8b40f11ec9/episodes/3bf7c731-ab01-41d1-af0e-083d370e44fd/audio/128/default.mp3?aid=rss_feed&awCollectionId=9536941d-4b0f-427b-8265-df8b40f11ec9&awEpisodeId=3bf7c731-ab01-41d1-af0e-083d370e44fd&feed=MWJ0vTGb) — `route-found; download-failed`。

### A4 · Claude 介面設計解析：Anthropic 如何用色彩、字體和摩擦力打造品牌定位

- 来源：https://rar.design/posts/claude-interface-design-philosophy
- 状态：`read`；性质：`secondary-analysis`；来源组：`A4`。
- 实际读取范围：文章正文、比较表与延伸资源说明
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2026-04-01。

提炼：把色彩、字形与协作模式串联起来，但对心理效果和竞品的归纳较强。

边界：仅作解释性参考；不采纳未经实验验证的用户心理结论。

### A5 · Seamlessly Crafting AI Branding and Visual Identity for Anthropic

- 来源：https://abduzeedo.com/seamlessly-crafting-ai-branding-and-visual-identity-anthropic
- 状态：`read`；性质：`secondary-case`；来源组：`A1`。
- 实际读取范围：案例正文
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2024-11-21。

提炼：主要整理 Geist 的同一项目。

边界：与 A1 属同一证据链，不计作独立交叉验证。

### A6 · Anthropic — Ideas on Design

- 来源：https://www.ideasondesign.com/p/anthropic
- 状态：`read`；性质：`secondary-note`；来源组：`A6`。
- 实际读取范围：品牌笔记正文
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：以早期品牌价值解释视觉取舍。

边界：历史背景，不用于确认现版产品细节。

### A7 · FigBrew: Branding AI with Everett Katigbak (Anthropic) | Figma

- 来源：https://www.youtube.com/watch?v=BeP5mqFn2z8
- 状态：`partial`；性质：`video`；来源组：`A7`。
- 实际读取范围：原视频元信息；已读主持人发布的两段同场短片页面可见转录，分别记录为 A7-C1、A7-C2；未读完整访谈。
- 核验日期：2026-09-08；记录依据：v0.1.0, alternative-media-recovery。
- 本版状态迁移：`unavailable` → `partial`。
- 关联补读：A7-C1, A7-C2。

提炼：短片涉及创作实践、具体需求与人的主导权；没有提供可核验的组件数值。

边界：整体仍是 partial；引用短片时使用各自编号，不把两段短片算成完整访谈。

### A8 · Redesigning Claude Code on desktop for parallel agents

- 来源：https://claude.com/blog/claude-code-desktop-redesign
- 状态：`read`；性质：`official-product`；来源组：`A8`。
- 实际读取范围：桌面改版文章正文
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2026-04-14。

提炼：展示多会话与多面板组织，以及可调整的信息披露深度。

边界：借鉴工作台结构；不复制具体产品全部行为。

### K1 · Kimi 品牌手册

- 来源：https://www.kimi.ai/zh-hans/resources/kimi-brand
- 状态：`read`；性质：`official-brand`；来源组：`K1`。
- 实际读取范围：品牌手册公开正文、颜色/字体/网格/界面说明；未完成所有图片的视觉核验
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：Inter、Geist Mono、Sentient 分工明确；品牌展示与暖白产品工作区并存。

边界：视觉方向依据；本包的尺寸、暗色与组件状态是原创设计决策。

### K2 · MoonshotAI Branding Guide

- 来源：https://moonshotai.github.io/Branding-Guide/
- 状态：`read`；性质：`official-assets`；来源组：`K2`。
- 实际读取范围：公开 Logo 素材页与说明
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：主要是标志形态和背景适用例。

边界：不等于组件系统；未分发任何标志或字体。

### K3 · The Bitter Lessons Behind Kimi Researcher’s taste

- 来源：https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c
- 状态：`read`；性质：`primary-maker-story`；来源组：`K3`。
- 实际读取范围：作者复盘正文；不声称运行其内部评价方案
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2025-07-15。

提炼：讨论报告呈现中的导航、布局、审美与信息保真权衡。

边界：报告视图参考；不当作 Kimi App 外壳规范或普遍性能结论。

### K4 · 用 Kimi Code CLI 交付 Moonshot AI 的一次重构

- 来源：https://www.kimi.ai/zh-hans/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli
- 状态：`read`；性质：`official-engineering`；来源组：`K4`。
- 实际读取范围：官网重构文章正文
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2026-09-01。
- 叙述事件时期：2026-03。

提炼：从已存在的 Figma、共享变量和真实代码出发，处理影响范围并验证结果。

边界：采用有证据的设计到代码流程；未取得文中内部 Skill 源码。

### K5 · 优设「细节猎人」Kimi 产品合集

- 来源：https://www.uisdc.com/hunter_product/kimi
- 状态：`index-read`；性质：`secondary-index`；来源组：`K5`。
- 实际读取范围：搜索返回的原站目录列表文本；当时快照 10 项。原页与图片未完成核验，也没有递归读完全部子帖。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum。
- 本版状态迁移：`unavailable` → `index-read`。

提炼：目录用于定位案例，不作为全部子帖已读的证明。

边界：目录快照不是当前完整性或实时数量保证；不据列表摘要制定硬规则。

### K6 · 在 Kimi App 里摇晃手机，解锁与 IP 形象的新互动方式！

- 来源：https://www.uisdc.com/hunter/0221610701.html
- 状态：`unavailable`；性质：`secondary-case`；来源组：`K6`。
- 实际读取范围：原页失败；仅可见索引片段
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：索引描述移动端摇动与品牌形象反馈。

边界：没有据摘要增加摇动或吉祥物的硬性要求。

### K7 · 4个插画、1个Logo：Kimi如何用设计给高考带来意想不到的惊喜？

- 来源：https://www.uisdc.com/hunter/0221627391.html
- 状态：`unavailable`；性质：`secondary-case`；来源组：`K7`。
- 实际读取范围：原页失败；既有目录与索引信息
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：记录节日插画案例入口。

边界：正文待补读；不得声称分析过全部图片。

### K8 · AI 深度思考功能，为什么需要一个「逃生出口」？

- 来源：https://www.uisdc.com/hunter/0221502862.html
- 状态：`read-via-index`；性质：`secondary-case`；来源组：`K8`。
- 实际读取范围：搜索返回的原站完整“细节描述”短正文；不是原页直接读取。图片和动作前后状态未核验。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum。
- 发布：2025-05-27。
- 本版状态迁移：`unavailable` → `read-via-index`。

提炼：历史案例描述思考过程中的跳过入口；没有验证后端取消/切换实现。

边界：提供长任务快速路径的设计启发。接口能力、异常处理和状态约束为本项目原创要求，不声称来自案例验证。

本项目规则关联：AGT-04。对应扩展为原创迁移，不是原作者的完整实现。

### K9 · Kimi 的 AI 标题魔法，你体验了吗？

- 来源：https://www.uisdc.com/hunter/0221575035.html
- 状态：`read`；性质：`secondary-case`；来源组：`K9`。
- 实际读取范围：原页标题、日期与“细节描述”正文；未完成配图视觉核验。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum。
- 发布：2024-07-19。
- 本版状态迁移：`unavailable` → `read`。

提炼：保存常用语时依据内容生成标题，减少单独命名。

边界：自动标题可编辑、用户命名优先、异步竞态和失败恢复是本项目扩展，不是作者给出的完整实现。

本项目规则关联：CMP-04。对应扩展为原创迁移，不是原作者的完整实现。

### K10 · Kimi 引入搜索匹配，能让 AI 取代传统搜索引擎？

- 来源：https://www.uisdc.com/hunter/0221606311.html
- 状态：`unavailable`；性质：`secondary-case`；来源组：`K10`。
- 实际读取范围：原帖正文仍未取得；另读到同作者汇编中的关键词匹配章节，见 K10-R1。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum。
- 关联补读：K10-R1。

提炼：记录输入建议案例入口。

边界：汇编不冒充原帖全文；原帖仍列为 unavailable。

### K11 · Kimi 如何打破传统会员费模式的冰冷感，让付费体验更加生动？

- 来源：https://www.uisdc.com/hunter/0221567725.html
- 状态：`read`；性质：`secondary-case`；来源组：`K11`。
- 实际读取范围：原页标题、日期与“细节描述”正文；GIF 获取失败，没有观察动效。
- 核验日期：2026-09-08；记录依据：v0.1.0, recovery-addendum。
- 发布：2024-05-29。
- 本版状态迁移：`unavailable` → `read`。

提炼：历史案例用生活化措辞表达支持性付费。

边界：只研究表达方式，不描述现行价格或会员规则。交易事实清晰的规则为原创产品约束，不是法律结论。

本项目规则关联：COPY-01。对应扩展为原创迁移，不是原作者的完整实现。

### S1 · anthropics/skills — brand-guidelines

- 来源：https://github.com/anthropics/skills/tree/main/skills/brand-guidelines
- 状态：`read`；性质：`official-skill`；来源组：`S1`。
- 实际读取范围：完整 SKILL.md
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`47c72c607bdb5dd81bdea5de2b5e4f3992a5fd59`。

提炼：给出品牌色及偏文档产物的字体指导。

边界：不能直接当作网页组件规范；品牌色不自动满足文字对比度。

### S2 · anthropics/skills — frontend-design

- 来源：https://github.com/anthropics/skills/tree/main/skills/frontend-design
- 状态：`read`；性质：`official-skill`；来源组：`S2`。
- 实际读取范围：完整 SKILL.md
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`a5333457c414d20d625f307df945842c0952ecc3`。

提炼：当前版本强调根据具体任务设计，并明确已指定的视觉方向优先。

边界：借鉴按 brief 设计与评审的方法，不照抄提示文本。

### S3 · VoltAgent/awesome-design-md — Claude DESIGN.md

- 来源：https://github.com/voltagent/awesome-design-md/blob/main/design-md/claude/DESIGN.md
- 状态：`read`；性质：`community-design`；来源组：`S3`。
- 实际读取范围：DESIGN.md 的结构化变量、正文、响应式与 Known Gaps；部分长响应分段读取
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`f92dc464d9bfdb6c6306f45a9ce406c6fca17432`。

提炼：是 alpha 状态的 Claude.com 展示网站分析。

边界：不采纳“永不记录 hover”等绝对规则；不用其估算值冒充官方。

### S4 · tweakcn — Claude 主题

- 来源：https://github.com/jnsahaj/tweakcn
- 状态：`read`；性质：`community-tool`；来源组：`S4`。
- 实际读取范围：README 与 utils/theme-presets.ts 的 Claude 段落（限定主题相关范围）
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`f5112cf34322c21976ff6ddf3597fa01dbd0395b`。

提炼：主题提供颜色与字体变量，不提供完整产品的信息架构。

边界：可借鉴变量组织；未安装编辑器，未验证全部预设。

### S5 · MoonshotAI/kimi-cli — web/

- 来源：https://github.com/MoonshotAI/kimi-cli/tree/main/web
- 状态：`read`；性质：`official-code`；来源组：`S5`。
- 实际读取范围：web/ 与 web/src/ 目录、完整 web/src/index.css；其他业务组件未作全量阅读
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`06601e57e87e7d6866993d55ea0b07029212ea95`。

提炼：实际 CSS 具有语义变量、暗色映射、代码区和触屏控件处理。

边界：这是 Kimi CLI Web 而非 kimi.com；没有构建、运行或代码安全审计。

### S6 · 12 UI/UX Design Skills to Build Modern Interfaces

- 来源：https://www.kimi.ai/resources/ui-ux-design-skills-for-agents
- 状态：`read`；性质：`official-resource-guide`；来源组：`S6`。
- 实际读取范围：12 Skills 资源文章正文
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2026-08-25。

提炼：介绍通用设计能力与其他项目入口。

边界：不是 Kimi 品牌专属 Skill；未递归读完文内所有第三方仓库。

### S7 · Kimi Code CLI — Agent Skills

- 来源：https://moonshotai.github.io/kimi-cli/en/customization/skills.html
- 状态：`read`；性质：`official-doc`；来源组：`S7`。
- 实际读取范围：Skill 目录、加载、frontmatter、组织建议和调用章节
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：支持目录化 SKILL.md 与按需加载附属内容。

边界：本包使用标准格式；安装路径及加载效果仍需在目标工具确认。

### S8 · pbakaus/impeccable

- 来源：https://github.com/pbakaus/impeccable
- 状态：`read`；性质：`community-tool`；来源组：`S8`。
- 实际读取范围：README 的目的、命令、安装与限制说明；未审计全部 detector/engine 源码
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`c4b9831a5cd45fdd02a0215f376bbb9f6e6217ff`。

提炼：将设计评审与技术检查区分，提供进一步精修命令。

边界：采用检查维度，不继承禁止系统字体等教条；未运行其工具或 hook。

### S9 · dembrandt/dembrandt

- 来源：https://github.com/dembrandt/dembrandt
- 状态：`read`；性质：`community-tool`；来源组：`S9`。
- 实际读取范围：完整 README
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`d3d9c90c722689febabb5d3ff1442dd062ce1dc0`。

提炼：提取渲染后的样式观察值，并说明动态内容和交互状态限制。

边界：观察值不等于品牌意图；不默认开启抓取或外部上传。

### S10 · Leonxlnx/kimi-code-desktop — DESIGN.md

- 来源：https://github.com/Leonxlnx/kimi-code-desktop/blob/main/docs/DESIGN.md
- 状态：`read`；性质：`community-design`；来源组：`S10`。
- 实际读取范围：完整 docs/DESIGN.md
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 已记录文件 Blob SHA：`f4397c7507c0e67232538e4d7b8393e61c1be65e`。

提炼：以连续工作区、有限强调、可恢复交互组织桌面工具。

边界：社区自有设计，不称为 Moonshot 官方规范。

### T1 · Improving frontend design through Skills

- 来源：https://claude.com/blog/improving-frontend-design-through-skills
- 状态：`read`；性质：`official-article`；来源组：`T1`。
- 实际读取范围：前端 Skill 方法文章正文与提示示例
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 发布：2025-11-12。

提炼：展示将设计维度转成可复用上下文的方式。

边界：历史提示实验，不采纳其中对字体的绝对禁令。

### T2 · Prompting for frontend aesthetics

- 来源：https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics
- 状态：`read`；性质：`official-cookbook`；来源组：`T2`。
- 实际读取范围：Cookbook 说明、生成代码与隔离提示示例
- 核验日期：2026-09-08；记录依据：v0.1.0。

提炼：展示按字体、主题等维度控制生成的实验结构。

边界：未调用收费 API；不把示例截图当成普遍效果证明。

### T3 · Set up your design system in Claude Design

- 来源：https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- 状态：`read`；性质：`official-doc`；来源组：`T3`。
- 实际读取范围：设计系统设置说明正文
- 核验日期：2026-09-08；记录依据：v0.1.0。
- 原页更新：2026-08-06。

提炼：用项目代码、截图和已有规范建立自己的设计系统。

边界：不是 Claude 品牌手册；未操作账号或配置产品。

### N1 · Agent Skills specification

- 来源：https://agentskills.io/specification
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N1`。
- 实际读取范围：name、description、目录、渐进加载及相关格式约束
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N2 · WCAG 2.2 — Contrast Minimum

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N2`。
- 实际读取范围：SC 1.4.3、适用例外与 sRGB 对比度公式
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N3 · WCAG 2.2 — Non-text Contrast

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N3`。
- 实际读取范围：SC 1.4.11 与控件识别、图形、焦点示例
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N4 · WCAG 2.2 — Target Size Minimum

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N4`。
- 实际读取范围：SC 2.5.8 的 24 CSS px 要求与例外
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N5 · WCAG 2.2 — Reflow

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N5`。
- 实际读取范围：SC 1.4.10 的重排、窄视口与二维内容例外
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N6 · WCAG 2.2 — Status Messages

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N6`。
- 实际读取范围：SC 4.1.3：无需获得焦点也能被辅助技术感知的状态
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N7 · WCAG 2.2 — Focus Not Obscured Minimum

- 来源：https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N7`。
- 实际读取范围：SC 2.4.11：获得键盘焦点的组件不被作者内容完全遮挡
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N8 · WAI-ARIA APG — Modal Dialog

- 来源：https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N8`。
- 实际读取范围：对话框模式与键盘焦点规则
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N9 · WAI-ARIA APG — Combobox

- 来源：https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N9`。
- 实际读取范围：组合框模式、键盘和弹出层关联规则
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N10 · WAI-ARIA APG — Tabs

- 来源：https://www.w3.org/WAI/ARIA/apg/patterns/tabs/
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N10`。
- 实际读取范围：标签页与面板关联、激活模式和键盘规则
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N11 · MDN — prefers-reduced-motion

- 来源：https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N11`。
- 实际读取范围：reduce/no-preference 的含义及媒体查询机制
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N12 · Google web.dev — Web Vitals

- 来源：https://web.dev/articles/vitals
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N12`。
- 实际读取范围：LCP、INP、CLS 的良好阈值与现场数据口径
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N13 · DTCG Format Module 2025.10

- 来源：https://www.designtokens.org/tr/2025.10/format/
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N13`。
- 实际读取范围：类型、值、引用和序列化相关章节；不是全文通读
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N14 · OpenAI — Build skills

- 来源：https://learn.chatgpt.com/docs/build-skills
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N14`。
- 实际读取范围：本地 Skill 的格式与 Codex 项目目录位置
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### N15 · Claude Code — Extend Claude with skills

- 来源：https://code.claude.com/docs/en/skills
- 状态：`scoped-read`；性质：`primary-technical`；来源组：`N15`。
- 实际读取范围：SKILL.md 格式与项目级目录位置
- 核验日期：2026-09-08；记录依据：v0.1.0。

边界：仅引用列明章节；不声称通读整个站点或标准全文。

### A7-C1 · FigBrew 同场短片：创作实践（Andrew Hogan 发布）

- 来源：https://www.linkedin.com/posts/ahhogan_what-does-it-take-to-shape-an-ai-brand-activity-7341874716992749570-9zGJ
- 状态：`clip-transcript-read`；性质：`primary-clip-transcript`；来源组：`A7`。
- 实际读取范围：原帖说明及 Transcript 栏完整可见文字；字幕生成方式未确认，没有音轨复核或画面检查。
- 核验日期：2026-09-08；记录依据：alternative-media-recovery。
- 对应原条目：A7；不独立计为原访谈/原案例的完整阅读。

提炼：创作依赖实践，也包含休息与工作内容转换；不支持强制持续加班。

边界：用于 CTX-06 的方法启发；不构成固定迭代轮数或具体视觉参数依据。

本项目规则关联：CTX-06。对应扩展为原创迁移，不是原作者的完整实现。

仅短片可见转录；没有整场时间戳、音轨校对或画面核验。

### A7-C2 · FigBrew 同场短片：具体需求与人的主导权（Andrew Hogan 发布）

- 来源：https://www.linkedin.com/posts/ahhogan_ai-design-activity-7343386927309471744--vXU
- 状态：`clip-transcript-read`；性质：`primary-clip-transcript`；来源组：`A7`。
- 实际读取范围：原帖说明及 Transcript 栏完整可见文字；未取得可靠整场时间戳，未播放或下载视频。
- 核验日期：2026-09-08；记录依据：alternative-media-recovery。
- 对应原条目：A7；不独立计为原访谈/原案例的完整阅读。

提炼：面向小群体的具体需求，关注人的主导权；生成更多应用不等于更多有用作品。

边界：是受访者的判断，不是数量预测或实验证据；迁移为任务成效优先的设计判断。

本项目规则关联：CTX-06 / AGT-03。对应扩展为原创迁移，不是原作者的完整实现。

仅短片可见转录；没有整场时间戳、音轨校对或画面核验。

### K10-R1 · 优设同作者汇编：关键词匹配章节

- 来源：https://www.uisdc.com/ai-prompt-design
- 状态：`scoped-read`；性质：`same-author-compilation`；来源组：`K10`。
- 实际读取范围：仅关键词匹配说明及指向 K10 原帖的链接；不声称读完汇编全部章节。
- 核验日期：2026-09-08；记录依据：recovery-addendum。
- 对应原条目：K10；不独立计为原访谈/原案例的完整阅读。

提炼：输入框提供匹配提示词，帮助构造请求。

边界：同一案例的替代文字入口，不是独立验证；键盘行为仍参照 APG，编辑/执行和异步竞态规则由本项目制定。

本项目规则关联：CMP-05。对应扩展为原创迁移，不是原作者的完整实现。
