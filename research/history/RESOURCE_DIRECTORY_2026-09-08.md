# Anthropic 与 Kimi：UI、审美、设计规范及前端资源目录
检索日期：2026-09-08。
本目录服务于借鉴两家公司的设计方法与视觉语言，区分官方规范、团队一手解释、第三方分析、风格实现和通用生成工具。它不是两家公司未公开设计系统的重建，也不宣称覆盖互联网所有资料。
## 阅读建议
先看 A1／A2 和 K1，理解品牌；开发桌面或工具型界面补充 A8／K4。落实到代码时，参考 S1、S2、S3、S4，或阅读 S5 的实际前端。品牌资料决定参考方向，通用 Skill 提供执行与检查方法。不要同时加载多套相互冲突的样式规则。
## 必须保留的区别
1. Anthropic 公司品牌、Claude 品牌网站、Claude 聊天界面、Claude Code 桌面应用不是同一个界面。Kimi 品牌传播、官网、聊天 App、Researcher 生成报告也不能混为一谈。
2. 官方发布的 frontend-design 是通用前端设计指导；brand-guidelines 才直接规定 Anthropic 品牌样式。所谓“Claude Design”项目名称也可能指设计工具，而不是 Claude 风格。
3. 本次找到了 Kimi 官方品牌手册与官方 Web 前端源码，但没有核验到一个覆盖 Kimi 全部产品样式、可直接套用的官方 React 组件库或品牌专属 SKILL.md。检索不到不能证明它们不存在。
4. 所有社区主题、DESIGN.md 和复刻项目均不能代替当前官方规范；选定目标产品、页面和版本后，应另外核对截图。
5. 品牌字体名称不等于可以无条件嵌入和再分发。中文界面需单独设计中文字体回退、字重与行高；本目录不附带任何字体文件。
## 资源索引
| 编号 | 资源 | 类型 | 优先级 |
|---|---|---|---|
| A1 | [Geist — Anthropic](https://geist.co/work/anthropic) | 原设计团队案例／英文 | 优先 |
| A2 | [The Subtext — Anthropic Brand Team Interview](https://www.thesubtext.online/all/anthropic-interview) | 品牌团队一手访谈／英文 | 优先 |
| A3 | [How Anthropic Is Redesigning Human–AI Interaction](https://promptedwithcam.substack.com/p/how-anthropic-is-redesigning-humanai) | 主持人发布的访谈页面／英文 | 优先 |
| A4 | [Claude 介面設計解析：Anthropic 如何用色彩、字體和摩擦力打造品牌定位](https://rar.design/posts/claude-interface-design-philosophy) | 第三方中文解读 | 优先 |
| A5 | [Seamlessly Crafting AI Branding and Visual Identity for Anthropic](https://abduzeedo.com/seamlessly-crafting-ai-branding-and-visual-identity-anthropic) | 第三方案例整理／英文 | 补充 |
| A6 | [Anthropic — Ideas on Design](https://www.ideasondesign.com/p/anthropic) | 第三方品牌笔记／英文 | 补充 |
| A7 | [FigBrew: Branding AI with Everett Katigbak (Anthropic) | Figma](https://www.youtube.com/watch?v=BeP5mqFn2z8) | Figma 视频访谈／英文 | 补充 |
| A8 | [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 官方产品改版说明／英文 | 优先 |
| K1 | [Kimi 品牌手册](https://www.kimi.ai/zh-hans/resources/kimi-brand) | 官方品牌手册／中文 | 优先 |
| K2 | [MoonshotAI Branding Guide](https://moonshotai.github.io/Branding-Guide/) | 官方品牌素材页与仓库 | 补充 |
| K3 | [The Bitter Lessons Behind Kimi Researcher’s taste](https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c) | 团队成员 Crystal J 一手复盘／英文 | 优先 |
| K4 | [用 Kimi Code CLI 交付 Moonshot AI 的一次重构](https://www.kimi.ai/zh-hans/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli) | 官方前端工程复盘／中文 | 优先 |
| K5 | [优设「细节猎人」Kimi 产品合集](https://www.uisdc.com/hunter_product/kimi) | 第三方中文案例合集 | 优先 |
| K6 | [在 Kimi App 里摇晃手机，解锁与 IP 形象的新互动方式！](https://www.uisdc.com/hunter/0221610701.html) | 第三方中文微交互案例 | 补充 |
| K7 | [4个插画、1个Logo：Kimi如何用设计给高考带来意想不到的惊喜？](https://www.uisdc.com/hunter/0221627391.html) | 第三方中文品牌交互案例 | 补充 |
| K8 | [AI 深度思考功能，为什么需要一个「逃生出口」？](https://www.uisdc.com/hunter/0221502862.html) | 第三方中文加载交互案例 | 补充 |
| K9 | [Kimi 的 AI 标题魔法，你体验了吗？](https://www.uisdc.com/hunter/0221575035.html) | 第三方中文组织交互案例 | 补充 |
| K10 | [Kimi 引入搜索匹配，能让 AI 取代传统搜索引擎？](https://www.uisdc.com/hunter/0221606311.html) | 第三方中文输入交互案例 | 补充 |
| K11 | [Kimi 如何打破传统会员费模式的冰冷感，让付费体验更加生动？](https://www.uisdc.com/hunter/0221567725.html) | 第三方中文文案／付费体验案例 | 补充 |
| S1 | [anthropics/skills — brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | 官方品牌样式 Skill | 优先 |
| S2 | [anthropics/skills — frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 官方通用前端设计 Skill | 优先 |
| S3 | [VoltAgent/awesome-design-md — Claude DESIGN.md](https://github.com/voltagent/awesome-design-md/blob/main/design-md/claude/DESIGN.md) | 社区风格分析／结构化设计文档 | 优先 |
| S4 | [tweakcn — Claude 主题](https://github.com/jnsahaj/tweakcn) | 社区可视化主题编辑器／开源项目 | 优先 |
| S5 | [MoonshotAI/kimi-cli — web/](https://github.com/MoonshotAI/kimi-cli/tree/main/web) | 官方开发工具的 Web 前端源代码 | 优先 |
| S6 | [12 UI/UX Design Skills to Build Modern Interfaces](https://www.kimi.ai/resources/ui-ux-design-skills-for-agents) | Kimi 官方资源文章／Skill 导航 | 补充 |
| S7 | [Kimi Code CLI — Agent Skills](https://moonshotai.github.io/kimi-cli/en/customization/skills.html) | 官方 Skill 接入文档 | 补充 |
| S8 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 源于 Anthropic frontend-design 的社区设计工具 | 补充 |
| S9 | [dembrandt/dembrandt](https://github.com/dembrandt/dembrandt) | 网站设计变量提取工具 | 补充 |
| S10 | [Leonxlnx/kimi-code-desktop — DESIGN.md](https://github.com/Leonxlnx/kimi-code-desktop/blob/main/docs/DESIGN.md) | 社区桌面应用设计说明 | 补充 |
| T1 | [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | Anthropic 官方技术文章 | 优先 |
| T2 | [Prompting for frontend aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics) | Anthropic 官方 Cookbook | 优先 |
| T3 | [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design) | Anthropic 官方产品文档 | 补充 |

## Anthropic：品牌与产品设计

### A1. Geist — Anthropic
来源：https://geist.co/work/anthropic

性质：原设计团队案例／英文。优先级：优先。

时间／版本：历史品牌基础，页面未明确标注发表日期。

值得看什么：品牌标识、Styrene 与 Tiempos 字体组合、温暖色彩、手绘插画、摄影，以及功能优先的网页和产品界面系统。适合先看图再理解体系。

适用边界：这是原设计项目案例，不是当前所有 Claude 产品界面的完整 CSS 规范。

核验情况：已读取正文。

### A2. The Subtext — Anthropic Brand Team Interview
来源：https://www.thesubtext.online/all/anthropic-interview

性质：品牌团队一手访谈／英文。优先级：优先。

时间／版本：2025-06-30。

值得看什么：讨论 Anthropic 与 Claude 的品牌分工，解释温暖、朴实、协作感以及克制表达。适合理解视觉与文案背后的判断。

适用边界：品牌团队访谈，不是组件库或像素级规范。

核验情况：已读取正文。

### A3. How Anthropic Is Redesigning Human–AI Interaction
来源：https://promptedwithcam.substack.com/p/how-anthropic-is-redesigning-humanai

性质：主持人发布的访谈页面／英文。优先级：优先。

时间／版本：2025-12-02。

值得看什么：Joel Lewenstein 谈 Claude 的协作式交互、适当的操作阻力，以及 Plan Mode 等设计选择。页面提供 Apple、Spotify、YouTube 入口。

适用边界：偏产品交互哲学；不能由此推出所有场景都应该增加点击或确认。

核验情况：已读取节目介绍及文字节选；未完整收听音频。

### A4. Claude 介面設計解析：Anthropic 如何用色彩、字體和摩擦力打造品牌定位
来源：https://rar.design/posts/claude-interface-design-philosophy

性质：第三方中文解读。优先级：优先。

时间／版本：页面显示 2026-04-01；搜索索引显示 2026-03-31，可能存在时区差异。

值得看什么：串联配色、字体、定位与 Good Friction，并给出原始访谈和设计案例入口。

适用边界：设计师解读，不是官方规范；文中的心理效果和竞品比较不应当成受控实验结论。

核验情况：已读取正文。

### A5. Seamlessly Crafting AI Branding and Visual Identity for Anthropic
来源：https://abduzeedo.com/seamlessly-crafting-ai-branding-and-visual-identity-anthropic

性质：第三方案例整理／英文。优先级：补充。

时间／版本：2024-11-21。

值得看什么：围绕 Geist 项目解释字体、色调、模块化布局与信任感，适合作为图文案例入口。

适用边界：主要复述同一历史设计案例，不是新的独立设计系统。

核验情况：已读取正文。

### A6. Anthropic — Ideas on Design
来源：https://www.ideasondesign.com/p/anthropic

性质：第三方品牌笔记／英文。优先级：补充。

时间／版本：2024 年文章，引用更早的品牌资料。

值得看什么：用品牌价值与个性梳理 Anthropic，适合看设计目标如何转译为视觉表达。

适用边界：较早资料，不能用于确认当前界面细节。

核验情况：已读取正文。

### A7. FigBrew: Branding AI with Everett Katigbak (Anthropic) | Figma
来源：https://www.youtube.com/watch?v=BeP5mqFn2z8

性质：Figma 视频访谈／英文。优先级：补充。

时间／版本：不据搜索摘要断言精确发布日期。

值得看什么：品牌从业者讨论 AI 品牌，可作为延伸观看材料。

适用边界：未据视频内容提炼具体结论。

核验情况：核对到视频标题与发布方；未取得完整文字稿或完整观看。

### A8. Redesigning Claude Code on desktop for parallel agents
来源：https://claude.com/blog/claude-code-desktop-redesign

性质：官方产品改版说明／英文。优先级：优先。

时间／版本：2026-04-14。

值得看什么：多会话侧边栏、可拖放面板、终端／编辑／差异查看／预览一体化，以及信息密度模式。适合开发桌面工具和 Agent 工作台。

适用边界：是这一版 Claude Code 桌面应用的案例，不是 Anthropic 通用品牌规范。

核验情况：已读取正文。

## Kimi：品牌、界面与设计复盘

### K1. Kimi 品牌手册
来源：https://www.kimi.ai/zh-hans/resources/kimi-brand

性质：官方品牌手册／中文。优先级：优先。

时间／版本：按 2026-09-08 可见页面；未确认手册的精确发布日期。

值得看什么：覆盖标志、蓝色为主的色彩系统、Inter／Geist Mono／Sentient、网格、视觉资产与界面升级；适合建立有官方依据的参考。

适用边界：品牌表现与产品工作区需要分开。手册说首页由灰蓝转为暖白，不能把“蓝色科技风”当成所有页面的规则。并非完整 React 组件库。

核验情况：已读取正文及公开配色／字体／界面升级说明。

### K2. MoonshotAI Branding Guide
来源：https://moonshotai.github.io/Branding-Guide/

性质：官方品牌素材页与仓库。优先级：补充。

时间／版本：较早的品牌资源入口。

值得看什么：主要提供不同背景与组合方式的 Logo 素材。仓库：https://github.com/MoonshotAI/Branding-Guide

适用边界：主要是标志资产，不等于包含按钮、间距、动效和交互状态的 UI 设计系统；使用资源前检查对应条款。

核验情况：已读取素材页与仓库。

### K3. The Bitter Lessons Behind Kimi Researcher’s taste
来源：https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c

性质：团队成员 Crystal J 一手复盘／英文。优先级：优先。

时间／版本：2025-07-15。

值得看什么：通过反例统一审美评价，讨论长篇研究结果的导航和布局，以及美观、交互、信息忠实性的取舍。

适用边界：重点是 Researcher 生成的研究报告／网页呈现，不等于整个 Kimi App 外壳的规范；没有公开可直接复现的完整评测数据或工程实现。

核验情况：已读取正文。

### K4. 用 Kimi Code CLI 交付 Moonshot AI 的一次重构
来源：https://www.kimi.ai/zh-hans/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli

性质：官方前端工程复盘／中文。优先级：优先。

时间／版本：发表于 2026-09-01，讲述 2026 年 3 月的改版。

值得看什么：Figma MCP、共享 token 与组件、依赖分析、动效行为、字体体积、diff 审查和浏览器核验。适合参考真实设计交付方法。

适用边界：官网设计大多已在 Figma 中完成，不是靠一句提示词从零自动设计。文中内部规则和审查 skill 不等于已公开下载。

核验情况：已读取正文。

## Kimi：中文交互细节案例

### K5. 优设「细节猎人」Kimi 产品合集
来源：https://www.uisdc.com/hunter_product/kimi

性质：第三方中文案例合集。优先级：优先。

时间／版本：跨版本案例合集。

值得看什么：按产品收集具体 UI/UX 细节；适合从案例找到动效、输入、反馈和情绪化设计灵感。

适用边界：部分细节是历史版本。此次未声称完整读完合集所有文章。

核验情况：搜索索引核对；合集原页抓取超时。

### K6. 在 Kimi App 里摇晃手机，解锁与 IP 形象的新互动方式！
来源：https://www.uisdc.com/hunter/0221610701.html

性质：第三方中文微交互案例。优先级：补充。

时间／版本：2025-02-18。

值得看什么：把品牌形象变成可回应用户动作的交互对象。

适用边界：历史移动端案例，不意味着桌面端应该照搬摇动操作。

核验情况：搜索索引核对。

### K7. 4个插画、1个Logo：Kimi如何用设计给高考带来意想不到的惊喜？
来源：https://www.uisdc.com/hunter/0221627391.html

性质：第三方中文品牌交互案例。优先级：补充。

时间／版本：2025-06-09。

值得看什么：节日／事件期间通过插画和标志变化传递关怀，不必重做整个页面。

适用边界：历史活动案例，不是常态首页规范。

核验情况：搜索索引核对；原页抓取超时。

### K8. AI 深度思考功能，为什么需要一个「逃生出口」？
来源：https://www.uisdc.com/hunter/0221502862.html

性质：第三方中文加载交互案例。优先级：补充。

时间／版本：历史产品案例；未核对精确发布日期。

值得看什么：长时任务的退出或切换入口，让用户不必一直被动等待。

适用边界：不把文章中对模型准确性的泛化描述当作实验证据。

核验情况：搜索索引核对。

### K9. Kimi 的 AI 标题魔法，你体验了吗？
来源：https://www.uisdc.com/hunter/0221575035.html

性质：第三方中文组织交互案例。优先级：补充。

时间／版本：历史产品案例；未核对精确发布日期。

值得看什么：自动生成标题，降低保存和管理常用提示内容的负担。

适用边界：针对该文章记录的功能，不保证当前入口与当时相同。

核验情况：搜索索引核对。

### K10. Kimi 引入搜索匹配，能让 AI 取代传统搜索引擎？
来源：https://www.uisdc.com/hunter/0221606311.html

性质：第三方中文输入交互案例。优先级：补充。

时间／版本：历史产品案例；未核对精确发布日期。

值得看什么：通过输入匹配／建议降低用户组织问题的负担。

适用边界：标题是讨论性提问，不是 AI 已取代搜索的事实。

核验情况：搜索索引核对。

### K11. Kimi 如何打破传统会员费模式的冰冷感，让付费体验更加生动？
来源：https://www.uisdc.com/hunter/0221567725.html

性质：第三方中文文案／付费体验案例。优先级：补充。

时间／版本：2024-05-29。

值得看什么：用“加油”及生活化意象替代冰冷的付费表达，适合观察语气如何参与产品设计。

适用边界：仅为历史设计案例，不代表当前收费方案、价格或会员状态。

核验情况：搜索索引核对。

## 可复用 Skill、设计文档与代码

### S1. anthropics/skills — brand-guidelines
来源：https://github.com/anthropics/skills/tree/main/skills/brand-guidelines

性质：官方品牌样式 Skill。优先级：优先。

时间／版本：读取 main 分支时的版本。

值得看什么：提供 Anthropic 的品牌配色与产物字体指导，是最直接相关的官方品牌 Skill。原始文件：https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md

适用边界：内容偏产物／文档样式，并非完整前端系统；Poppins／Lora 不等于 Geist 历史案例中的 Styrene／Tiempos，也不能据此断言当前 Claude 全站字体。

核验情况：已读取 SKILL.md；未安装或执行。

### S2. anthropics/skills — frontend-design
来源：https://github.com/anthropics/skills/tree/main/skills/frontend-design

性质：官方通用前端设计 Skill。优先级：优先。

时间／版本：读取 main 分支时的版本。

值得看什么：指导视觉方向、排版、层次、动效与设计评审。原始文件：https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md

适用边界：它教 Agent 为不同项目形成合适风格，不自动生成 Anthropic 风格。当前文本把奶油底＋衬线＋陶土橙也列为可能的模板化默认，但明确要求遵守用户指定方向。

核验情况：已读取 SKILL.md；未安装或执行。

### S3. VoltAgent/awesome-design-md — Claude DESIGN.md
来源：https://github.com/voltagent/awesome-design-md/blob/main/design-md/claude/DESIGN.md

性质：社区风格分析／结构化设计文档。优先级：优先。

时间／版本：文件自标 alpha；读取 main 分支时的版本。

值得看什么：整理颜色、字阶、间距、圆角、组件和状态，方便作为编码 Agent 的参考输入。原始文件：https://raw.githubusercontent.com/voltagent/awesome-design-md/main/design-md/claude/DESIGN.md

适用边界：非官方，侧重 Claude.com 品牌网站而非聊天应用。包含分析者设定或推断，不应把全部尺寸／字体／标志描述当成精确提取的生产规范。

核验情况：已读取完整文件结构与关键内容；未按其实现项目。

### S4. tweakcn — Claude 主题
来源：https://github.com/jnsahaj/tweakcn

性质：社区可视化主题编辑器／开源项目。优先级：优先。

时间／版本：读取时的公开版本。

值得看什么：为 shadcn/ui 与 Tailwind 调整主题，适合现有 React 工程先统一颜色和组件视觉。编辑器：https://tweakcn.com/

适用边界：Claude 是社区主题，不是官方组件库；主题不包含完整页面结构和交互。未验证某个主题 JSON 安装端点，因此不提供未经核对的一键安装链接。

核验情况：已读取仓库；网站索引确认 claude 预设；未运行。

### S5. MoonshotAI/kimi-cli — web/
来源：https://github.com/MoonshotAI/kimi-cli/tree/main/web

性质：官方开发工具的 Web 前端源代码。优先级：优先。

时间／版本：读取 main 分支时的版本。

值得看什么：可研究真实的 React／Vite／Tailwind／Radix 等前端组织方式。依赖清单：https://github.com/MoonshotAI/kimi-cli/blob/main/web/package.json

适用边界：这是 Kimi CLI 的 Web UI，不是 kimi.com 全站源码，也不是 Kimi 公开通用组件库。未对代码质量或安全性作审计。

核验情况：已核对目录和 package.json；未安装／构建／测试。

### S6. 12 UI/UX Design Skills to Build Modern Interfaces
来源：https://www.kimi.ai/resources/ui-ux-design-skills-for-agents

性质：Kimi 官方资源文章／Skill 导航。优先级：补充。

时间／版本：读取时的公开版本。

值得看什么：介绍 design-system-builder、landing-page-scaffold 和第三方 UI/UX Skills；适合找截图到设计系统等方法。

适用边界：这是“用 Kimi 做设计”的资源页，不是“Kimi 品牌风格 Skill”；内置功能介绍不等于已提供同名公开 SKILL.md。

核验情况：已读取正文；未验证各内置命令的实际账号可用性。

### S7. Kimi Code CLI — Agent Skills
来源：https://moonshotai.github.io/kimi-cli/en/customization/skills.html

性质：官方 Skill 接入文档。优先级：补充。

时间／版本：读取时的公开版本。

值得看什么：解释 SKILL.md 格式和发现／加载机制，供把项目设计规范接入 Kimi 编码工作流时参考。

适用边界：接入能力与输出审美是两件事；支持 Skill 不表示自带完整 Kimi 品牌样式。

核验情况：已读取公开文档。

### S8. pbakaus/impeccable
来源：https://github.com/pbakaus/impeccable

性质：源于 Anthropic frontend-design 的社区设计工具。优先级：补充。

时间／版本：读取时的公开版本。

值得看什么：提供 critique、audit、polish、harden 等设计审查和完善命令，适合检查一致性、可访问性及边界状态。

适用边界：不是 Anthropic 或 Kimi 专属皮肤，审美建议必须服从项目已有明确风格。

核验情况：已读取 README 与命令说明；未安装／运行。

### S9. dembrandt/dembrandt
来源：https://github.com/dembrandt/dembrandt

性质：网站设计变量提取工具。优先级：补充。

时间／版本：读取时的公开版本。

值得看什么：从渲染 DOM 的 computed styles 整理颜色、字体、间距等，可输出设计变量和 DESIGN.md。

适用边界：提取到的是观察结果，不是官方意图或完整交互系统；动态、Canvas、登录状态等可能缺失。应只对允许自动访问的页面或自有系统使用。

核验情况：已读取 README、输出和限制；未运行网站提取。

### S10. Leonxlnx/kimi-code-desktop — DESIGN.md
来源：https://github.com/Leonxlnx/kimi-code-desktop/blob/main/docs/DESIGN.md

性质：社区桌面应用设计说明。优先级：补充。

时间／版本：读取 main 分支时的版本。

值得看什么：以安静的 Windows 原生感、石墨色工作区和明确状态表达组织桌面工具，可作为应用界面层的参考。

适用边界：社区应用的自有设计，不是 Kimi 官方品牌系统，更不代表 Kimi 网页端。

核验情况：已读取设计文档；未构建应用。

## 官方前端技术资料

### T1. Improving frontend design through Skills
来源：https://claude.com/blog/improving-frontend-design-through-skills

性质：Anthropic 官方技术文章。优先级：优先。

时间／版本：2025-11-12。

值得看什么：解释如何把设计上下文封装成 Skill，引导字体、颜色、布局与动态表现，并展示不同指导方式的输出。

适用边界：方法文章，不是品牌配色规范；历史示例不能当作当前模型性能保证。

核验情况：已读取正文。

### T2. Prompting for frontend aesthetics
来源：https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics

性质：Anthropic 官方 Cookbook。优先级：优先。

时间／版本：2025 年示例。

值得看什么：可查看可操作的审美指导、提示变量以及前后对比，学习怎样把模糊偏好变成可执行输入。

适用边界：示例环境和模型有时间边界；不必原样继承与项目要求冲突的审美偏好。

核验情况：已读取示例和实验结构；未运行。

### T3. Set up your design system in Claude Design
来源：https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design

性质：Anthropic 官方产品文档。优先级：补充。

时间／版本：2026-08-06 更新。

值得看什么：用代码、原型截图、品牌资源和其他材料建立项目设计系统；适合已有设计参考的工作流。

适用边界：是 Claude Design 产品能力介绍，不是 Claude 自身的视觉规范；本次未配置用户账号或导入资产。

核验情况：官方搜索索引核对；中文官方页面亦可见。

## 转成自己项目的设计输入：建议，不是官方规范

为一个具体软件选定一个主参考，而不是抽象地要求“Anthropic 和 Kimi 混合风”。保存少量带日期的关键页面截图，并写清借鉴的是布局、阅读层次、状态反馈还是品牌表达。

项目级 DESIGN.md 应至少明确：页面背景与表面层次、文本角色、强调色与语义色、中文与英文字体、字阶与行长、间距与圆角、常用组件的状态、动效触发条件、键盘焦点和减弱动画要求。数值由项目自行确认，不冒称来自官方。

把已确认的规则交给一种主要前端设计 Skill 执行；最终在真实页面检查长文本、空状态、加载、失败、窄窗口、暗色模式和键盘操作。对工具型软件，优先借鉴工作区的阅读和交互秩序，而不是复制营销首页的大标题和大面积动效。

## 核验与使用说明

- 未安装或执行本目录中的任何第三方 Skill、CLI 或前端项目，未作性能／安全审计，也未验证生产部署。
- 优设部分内容依据可见搜索索引整理，部分原页抓取超时；视频仅核对到的元信息和公开文字已在相应条目标明。
- 对官方页面的引用仅表示来源身份，不表示其营销性效果描述已被独立实验验证。
- main 分支与产品界面会变动。将资源用于长期项目时，建议记录实际采用的提交版本与截图日期。
- 目录只提供原始链接、简要摘要与用途判断，不包含转载全文、第三方商标包或字体文件。
