# Ren'Py 项目初始化说明

这是一个已完成基础初始化的 Ren'Py 项目，目标是让后续剧情、美术与系统脚本可以按模块扩展，而不是继续堆在默认模板文件里。

## 当前约定

- 入口脚本：`game/script.rpy`
- 角色定义：`game/characters.rpy`
- 全局变量：`game/data/game_state.rpy`
- 章节脚本：`game/story/`
- 美术资源：`game/images/bg`、`game/images/characters`、`game/images/cg`
- 音频资源：`game/audio/bgm`、`game/audio/sfx`

## 建议开发流程

1. 先在 `game/characters.rpy` 补全角色定义。
2. 按章节在 `game/story/` 新增脚本文件。
3. 将背景、立绘、CG、BGM、音效分别放入约定目录。
4. 每完成一个可玩的段落，再补存档点、分支和 UI 定制。

## 当前状态

- 已移除默认模板对白。
- 已建立章节入口和占位序章。
- 已补充基础 Git 忽略规则。
- 仍未接入正式剧情、美术、音频资源。
