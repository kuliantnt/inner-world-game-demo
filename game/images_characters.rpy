# 人物立绘占位图声明。
# 后续替换正式立绘时，保持文件名不变即可无缝替换。
#
# 这个文件做两件事：
# 1. 定义人物站位 transform，统一控制单人/双人/三人时的摆放位置
# 2. 定义人物立绘 image，并在这里接入“当前说话角色高亮”的视觉效果

init python:
    import renpy.store as store

    # ------------------------------
    # 立绘明暗切换逻辑
    # ------------------------------
    #
    # 设计思路：
    # - 剧情层继续正常写 `show lianlian idle at char_duo_left`
    # - 发言时由 characters.rpy 更新 active_speaker
    # - 本文件根据 active_speaker 自动决定该显示正常图还是半暗图
    #
    # 这样脚本作者只管写剧情，不用在每句对白前后手动切图。

    # 缓存“原图 / 半暗图”两套显示对象，避免每次刷新界面都重新创建。
    _character_sprite_cache = {}

    def get_character_sprite_pair(image_path):
        # 每张立绘第一次用到时生成一套“正常 / 半暗”版本，
        # 后续直接复用缓存，减少重复创建显示对象的开销。
        sprite_pair = _character_sprite_cache.get(image_path)

        if sprite_pair is None:
            normal_sprite = store.Image(image_path)
            dim_sprite = store.Transform(
                normal_sprite,
                # 非当前发言角色只做轻度退后处理，保留五官和服装细节。
                # 这里故意不压成纯黑，因为常见 gal 更偏向“退后一步”而不是“剪影化”。
                matrixcolor=store.SaturationMatrix(0.45) * store.BrightnessMatrix(-0.28),
                alpha=0.88
            )
            sprite_pair = {
                "normal": normal_sprite,
                "dim": dim_sprite,
            }
            _character_sprite_cache[image_path] = sprite_pair

        return sprite_pair

    def character_focus_displayable(st, at, image_path, char_id):
        # DynamicDisplayable 每次刷新时都会调用这里。
        # 根据 active_speaker 判断当前该返回正常图还是半暗图。
        #
        # 返回值格式是：
        # (要显示的对象, 下次建议刷新时间)
        sprite_pair = get_character_sprite_pair(image_path)
        active_speaker = getattr(store, "active_speaker", None)

        # 没有人在说话，或者当前就是自己在说话时，保持正常显示。
        if active_speaker is None or active_speaker == char_id:
            return sprite_pair["normal"], 0.05

        # 其他在场角色进入半暗状态，形成常见 gal 的视觉焦点切换。
        return sprite_pair["dim"], 0.05

# ------------------------------
# 角色站位
# ------------------------------
#
# 这些 transform 只负责“摆位和缩放”，不负责明暗切换。
# 后续如果觉得立绘离边缘太近、人物太大/太小，优先改这里。

# 单人站位：角色居中。
transform char_single:
    xalign 0.5
    yalign 1.0
    zoom 0.62

# 双人站位：左侧角色。
transform char_duo_left:
    xalign 0.24
    yalign 1.0
    zoom 0.62

# 双人站位：右侧角色。
transform char_duo_right:
    xalign 0.76
    yalign 1.0
    zoom 0.62

# 三人站位：左侧角色。
transform char_trio_left:
    xalign 0.18
    yalign 1.0
    zoom 0.62

# 三人站位：中间角色。
transform char_trio_center:
    xalign 0.5
    yalign 1.0
    zoom 0.62

# 三人站位：右侧角色。
transform char_trio_right:
    xalign 0.82
    yalign 1.0
    zoom 0.62

# ------------------------------
# 立绘声明
# ------------------------------
#
# 立绘声明统一走 DynamicDisplayable。
# 剧情层仍然正常写 `show xxx idle`，不用手动切换亮图和暗图。
#
# 后续如果某个角色新增：
# - 表情：可以继续扩展成 `image xxx smile`
# - 换装：也可以沿用同样写法继续包装成 DynamicDisplayable
image guide idle = DynamicDisplayable(character_focus_displayable, "images/characters/guide_idle.png", "guide")
image lianlian idle = DynamicDisplayable(character_focus_displayable, "images/characters/lianlian_idle.png", "lianlian")
image qingchuan idle = DynamicDisplayable(character_focus_displayable, "images/characters/qingchuan_idle.png", "qingchuan")
image xiaoyu idle = DynamicDisplayable(character_focus_displayable, "images/characters/xiaoyu_idle.png", "xiaoyu")
image xuexue idle = DynamicDisplayable(character_focus_displayable, "images/characters/xuexue_idle.png", "xuexue")
image yaxuan idle = DynamicDisplayable(character_focus_displayable, "images/characters/yaxuan_idle.png", "yaxuan")
image mengmeng idle = DynamicDisplayable(character_focus_displayable, "images/characters/mengmeng_idle.png", "mengmeng")
image lulu idle = DynamicDisplayable(character_focus_displayable, "images/characters/lulu_idle.png", "lulu")
