# 可选实现资产：Token

两套预设用于演示规范的落地方式，不代表 Anthropic / Kimi 的完整主题或一一对应关系。先确定信息架构与交互，再决定是否采用；使用设计方法不要求导入这些变量。

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

品牌色与操作色分开；`border-subtle` 只用于非必要分隔，输入轮廓使用 `border-control`。`surface-inverse` / `on-inverse` 用于刻意的对比展示带（代码、示例、页脚），一页里少量出现，不替代画布。

| 方向 | 画布与表面 | 操作 | 强调与展示带 |
|---|---|---|---|
| `editorial-warm` | 纸色画布，次级区域深一级 | 墨色按钮、纸色文字 | 陶土色只用于品牌、链接、焦点与选中；墨色展示带 |
| `precise-light` | 暖白画布、中性灰阶 | 与品牌蓝同色相的深蓝 | 蓝色只做操作与高亮；深海军蓝展示带 |

暖纸底容易成为惯性选择，只在确实需要阅读与纸面感时使用 `editorial-warm`。默认 2 种方向 × 明暗 2 种模式；没有要求暗色的项目不必额外增加维护范围。这些是原创实现起点，不是官方精确抽取值，也不宣称完整 DTCG 兼容。


[返回首页](../README.md)
