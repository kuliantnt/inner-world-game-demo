# AGENTS.md

本文件定义本仓库内代理的项目级工作规则。若与全局默认行为冲突，以本文件为准；若用户在当前对话中提出了更明确的要求，以用户要求为准。

## 1. 项目概况

- 项目类型：Ren'Py 视觉小说 Demo
- 当前引擎结构：以 `game/` 为主目录，脚本、角色、UI、资源声明分离
- 当前重点：剧情脚本迭代、立绘与背景接入、UI 持续细化

## 2. 目录约定

- 入口脚本：`game/script.rpy`
- 角色定义：`game/characters.rpy`
- 全局状态：`game/data/game_state.rpy`
- 章节脚本：`game/story/`
- 立绘声明：`game/images_characters.rpy`
- 背景声明：`game/images_backgrounds.rpy`
- GUI 参数：`game/gui.rpy`
- 屏幕与菜单：`game/screens.rpy`
- 背景资源：`game/images/bg/`
- 角色资源：`game/images/characters/`

## 3. 修改边界

- 改剧情时，优先修改 `game/story/`，不要把章节内容重新堆回 `game/script.rpy`
- 改角色信息时，优先修改 `game/characters.rpy` 与 `game/images_characters.rpy`
- 改背景图接入时，优先修改 `game/images_backgrounds.rpy`
- 改 UI 时，优先修改 `game/gui.rpy` 和 `game/screens.rpy`
- 除非用户明确要求，不要随意删除现有图片、重命名资源文件、或改动已存在的图片路径

## 4. 脚本规范

- 所有新增注释、说明、占位文本统一使用中文
- Ren'Py 脚本按功能拆分，不把角色定义、剧情流程、界面逻辑混写在同一文件
- 新章节文件命名延续现有风格，例如：`chapter_02_xxx.rpy`
- 新图片声明保持“资源文件名稳定，声明层可读”的原则，优先在声明文件中新增 `image` 语句，不在剧情里直接硬编码路径
- 角色登场优先复用现有变换，例如 `char_single`、`char_duo_left`、`char_duo_right`

## 5. UI 规范

- 当前 UI 已经从默认 Ren'Py 模板改为偏悬浮面板风格，后续修改要保持统一，不要把默认蓝色模板样式混回去
- 文本框、快捷栏、主菜单、系统菜单的视觉语言应统一：深色半透明面板、冷色高亮、较克制的装饰
- 优先通过 `gui.rpy` 调整尺寸、间距、颜色；仅在需要改结构时修改 `screens.rpy`
- 如果用户反馈“比例不对”，优先从 `gui.textbox_height`、`gui.dialogue_ypos`、`gui.name_ypos`、`style window` 的 padding 入手
- 移动端样式已存在 `variant "small"` / `variant "touch"`，改 PC UI 时注意不要破坏移动端覆盖逻辑

## 6. 资源处理规则

- 正式资源未完全定稿前，尽量保持文件名稳定，避免频繁重命名导致声明层和剧情层联动修改
- 新增背景图放入 `game/images/bg/`
- 新增立绘放入 `game/images/characters/`
- 若替换占位图，优先“同名替换”，避免同时修改多处脚本
- 不要在未获用户确认的情况下批量覆盖或压缩现有美术资源

## 7. Git 与提交规则

- 本仓库可能长期处于脏工作区，提交前必须先看 `git status --short`
- 只提交与当前任务直接相关的文件，不要顺手把用户别的改动一起提交
- 提交信息尽量简洁明确，推荐前缀：`feat:`、`fix:`、`chore:`
- 如果任务只涉及 UI，通常只应提交 `game/gui.rpy`、`game/screens.rpy` 及必要资源

## 8. 验证要求

- 优先做静态核查：`git diff --check`
- 若环境允许，再进行 Ren'Py 运行验证
- 如果本机无法直接调用 `renpy`，要明确说明“仅完成静态检查，未做运行验证”
- 对于图片、文本框比例、菜单布局类修改，优先依据截图反馈继续微调

## 9. 协作要求

- 默认使用中文与用户沟通
- 回答保持简洁，先给结果，再补必要说明
- 遇到以下情况要先停下来确认：批量重命名资源、覆盖用户已有未提交修改、删除图片或脚本或存档相关内容、把未提交的大量本地改动一起提交或推送

## 10. 当前项目事实

- 当前主分支为 `main`
- GitHub 远端已配置为私有仓库 `inner-world-game-demo`
- 当前项目已存在基础剧情文件：`game/story/chapter_01_prologue.rpy`、`game/story/chapter_01_inner_world.rpy`
- 当前项目已存在背景声明：`image bg inner_world = "images/bg/endless_white_corridor_1920x1080.png"`

后续代理开始工作时，先读本文件，再读 `README.md`、`game/script.rpy`、目标改动对应的 `.rpy` 文件。
