# 开发与验证

以下命令均从仓库根目录运行。

## 本地验证

Python 3.10+；脚本只使用标准库。以下操作只检查本包，不运行第三方安装器：

```bash
python scripts/build_sources.py --check
python scripts/build_spec.py --check
python scripts/build_tokens.py --check
python scripts/validate_package.py
python -m unittest discover -s tests -v
python skills/humanist-frontend/scripts/check_contrast.py
```

修改 JSON 后先执行 `python scripts/build_tokens.py` 更新 CSS。对比度脚本只检查列明的不透明 sRGB 色对，不能证明整页 WCAG 合规。

## 来源与验证范围

来源台账保留 50 条资料记录，并区分正文、节选、未取得材料与共同来源；详见 [覆盖统计](../research/coverage.json) 和 [来源记录](../research/SOURCE_AUDIT.md)。这些是随包研究记录，本次发布仅抽查部分公开页面，未重新核验全部资料。规范中的主题数值属于原创默认，不代表官方 token。

本地检查覆盖结构、生成物一致性、安装、打包及列明的 88 个纯色色对。18 个 Agent 评估场景尚未执行，也未完成宿主实机加载、下游页面视觉、真实输入法或读屏测试。不能据此宣称视觉质量提升或整页 WCAG 合规。

版本变化见 [CHANGELOG](../CHANGELOG.md)，补读整合过程见 [合并说明](MERGE_NOTES.md)，历史材料保留在 [研究归档](../research/history/README.md)。

## 本地重新打包

完成上面的检查后，运行：

```bash
python scripts/build_release.py --output ../releases
```

输出完整仓库 ZIP、独立 Skill ZIP 与外部 SHA-256 校验文件。两个 ZIP 各带逐文件 `SHA256SUMS`。默认拒绝覆盖；只有确实需要覆盖同名产物时才加 `--overwrite`。输出目录必须在源码目录之外。

同一源码快照、Python/zlib 环境下打包使用固定文件顺序与时间字段；日志变动会正常改变校验值。打包脚本本身不替代测试、浏览器验收或宿主加载。

## 维护

修改规范的权威入口为 `skills/humanist-frontend/references/01-05`；`DESIGN_SPEC.md` 是便于通读的汇编。更新后运行 `python scripts/build_spec.py`。来源以 `research/sources.json` 为入口，运行 `python scripts/build_sources.py` 同步当前审计、覆盖统计和独立 Skill 的来源文件。不要形成内容矛盾的两份规范。

来源更新可能改变建议；新增规则需交代适用范围、证据或原创假设和验收方法。新增字体/图标/截图/第三方代码须核对许可，不能直接复制品牌资产。

原创部分使用 [MIT](../LICENSE)，第三方名称与素材的边界见 [声明](../THIRD_PARTY_NOTICES.md)。
