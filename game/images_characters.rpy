# 人物立绘占位图声明。
# 后续替换正式立绘时，保持文件名不变即可无缝替换。

init python:
    import renpy.store as store

    _character_sprite_cache = {}

    def get_character_sprite_pair(image_path):
        sprite_pair = _character_sprite_cache.get(image_path)

        if sprite_pair is None:
            normal_sprite = store.Image(image_path)
            dim_sprite = store.Transform(
                normal_sprite,
                # 非当前发言角色只做轻度退后处理，保留五官和服装细节。
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
        sprite_pair = get_character_sprite_pair(image_path)
        active_speaker = getattr(store, "active_speaker", None)

        if active_speaker is None or active_speaker == char_id:
            return sprite_pair["normal"], 0.05

        return sprite_pair["dim"], 0.05

transform char_single:
    xalign 0.5
    yalign 1.0
    zoom 0.62

transform char_duo_left:
    xalign 0.24
    yalign 1.0
    zoom 0.62

transform char_duo_right:
    xalign 0.76
    yalign 1.0
    zoom 0.62

transform char_trio_left:
    xalign 0.18
    yalign 1.0
    zoom 0.62

transform char_trio_center:
    xalign 0.5
    yalign 1.0
    zoom 0.62

transform char_trio_right:
    xalign 0.82
    yalign 1.0
    zoom 0.62

image guide idle = DynamicDisplayable(character_focus_displayable, "images/characters/guide_idle.png", "guide")
image lianlian idle = DynamicDisplayable(character_focus_displayable, "images/characters/lianlian_idle.png", "lianlian")
image qingchuan idle = DynamicDisplayable(character_focus_displayable, "images/characters/qingchuan_idle.png", "qingchuan")
image xiaoyu idle = DynamicDisplayable(character_focus_displayable, "images/characters/xiaoyu_idle.png", "xiaoyu")
image xuexue idle = DynamicDisplayable(character_focus_displayable, "images/characters/xuexue_idle.png", "xuexue")
image yaxuan idle = DynamicDisplayable(character_focus_displayable, "images/characters/yaxuan_idle.png", "yaxuan")
image mengmeng idle = DynamicDisplayable(character_focus_displayable, "images/characters/mengmeng_idle.png", "mengmeng")
image lulu idle = DynamicDisplayable(character_focus_displayable, "images/characters/lulu_idle.png", "lulu")
