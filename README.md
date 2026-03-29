# 里世界 / Inner World Story

一个基于 Ren'Py 开发的视觉小说 Demo。

本项目当前以“内在系统群像”作为核心概念，故事重点不是传统攻略流程，而是围绕主角误入“里世界”后，与多位性格、功能和情感表达截然不同的成员建立理解、信任与共存关系。

## 项目状态

- 当前版本：`0.1.0`
- 当前形态：可继续迭代的剧情 Demo
- 当前重点：章节脚本推进、角色塑造、立绘与背景接入、UI 细化
- 当前已实现：
  - 启动入口与基础引导流程
  - 序章、第一章、第二章、第三章的连续剧情骨架
  - 多角色登场与对白颜色配置
  - 基于当前发言角色的立绘高亮逻辑
  - 一套偏深色半透明面板风格的 UI 基础资源

## 故事方向

主角在凌晨两点十七分反复梦见同一场景，并被“门”带入名为“里世界”的空间。这里会映照情绪、执念与未被承认的记忆。随着“门缝回响”不断扩大，主角必须在现实与里世界之间寻找线索，逐步面对被自己回避的过去。

当前已出场的核心角色包括：

- 引导者
- 脸脸
- 晴川
- 小雨
- 雪雪
- 雅轩
- 梦梦
- 露露

更完整的人设与剧情功能说明见 [docs/角色设定总表.md](docs/角色设定总表.md)。

## 目录结构

```text
.
├─ docs/                        策划文档与角色设定
├─ game/
│  ├─ data/                     全局状态与运行期变量
│  ├─ images/                   背景与角色资源
│  ├─ story/                    分章节剧情脚本
│  ├─ characters.rpy            角色定义与发言回调
│  ├─ images_backgrounds.rpy    背景声明
│  ├─ images_characters.rpy     角色立绘声明
│  ├─ gui.rpy                   GUI 参数
│  ├─ screens.rpy               屏幕与菜单结构
│  ├─ options.rpy               项目基础配置
│  └─ script.rpy                游戏启动入口
└─ README.md
```

## 当前章节结构

- `game/script.rpy`：仅保留启动与流程跳转
- `game/story/chapter_01_prologue.rpy`：序章，主角首次被拖入里世界
- `game/story/chapter_01_inner_world.rpy`：第一章，核心成员初次亮相
- `game/story/chapter_02_door_echo.rpy`：第二章，门缝回响与现实线索抛出
- `game/story/chapter_03_voice_trace.rpy`：第三章，陌生语音落到现实楼道，主角拿到“217”钥匙牌线索

这意味着后续新增剧情时，应该继续在 `game/story/` 下按章节拆分，而不是把内容重新堆回入口文件。

## 运行方式

### 方式一：使用 Ren'Py Launcher

1. 安装 Ren'Py。
2. 在 Launcher 中打开本项目目录。
3. 选择项目后直接运行。

### 方式二：使用命令行

如果本机已经配置好 Ren'Py 命令行环境，可在项目目录执行对应启动命令。不同版本的 Ren'Py 启动方式略有差异，建议以本机实际安装路径为准。

## 开发约定

- 剧情内容优先放在 `game/story/`
- 角色定义优先维护在 `game/characters.rpy`
- 背景与立绘声明分别维护在 `game/images_backgrounds.rpy`、`game/images_characters.rpy`
- 角色设定、人设方向、个人线规划统一维护在 `docs/`
- UI 调整优先修改 `game/gui.rpy`，需要改结构时再动 `game/screens.rpy`
- 新增注释、说明、占位文本统一使用中文

## 当前资源情况

- 背景：已接入 `inner_world` 背景声明
- 角色：已存在多名角色的 `idle` 立绘占位资源
- 音频：目录约定已预留，正式 BGM / SFX 仍可继续补充

## 建议迭代顺序

1. 继续推进第四章及后续章节，把“217 对应的现实位置”继续往下追。
2. 补全角色个人线钩子，拉开不同角色的情感功能差异。
3. 按剧情需求逐步替换占位立绘、背景和 CG。
4. 在已有 UI 风格基础上继续细化文本框、菜单和系统界面。
5. 视版本目标补充分支、存档点、音频和发布配置。

## 协作说明

- 仓库当前可能长期处于脏工作区，提交前先检查 `git status --short`
- 不要随意批量重命名资源文件或改动既有图片路径
- 若需调整剧情风格或角色方向，先同步更新 `docs/角色设定总表.md`

## 相关文件

- [项目入口](game/script.rpy)
- [角色定义](game/characters.rpy)
- [角色设定总表](docs/角色设定总表.md)
- [第一章：序章](game/story/chapter_01_prologue.rpy)
- [第一章：里世界](game/story/chapter_01_inner_world.rpy)
- [第二章：门缝回响](game/story/chapter_02_door_echo.rpy)
- [第三章：语音落点](game/story/chapter_03_voice_trace.rpy)
