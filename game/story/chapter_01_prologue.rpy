# 序章：负责把玩家带入里世界。

label chapter_01_prologue:

    $ current_chapter = "序章"

    scene black
    with fade

    "夜里两点十七分，你又一次从那场相同的梦里惊醒。"
    "窗外没有风，房间里安静得只剩下自己逐渐放缓的呼吸声。"
    "可这一次，梦里的那句低语没有随着清醒一起消失。"

    show guide idle at char_single
    with dissolve
    guide "你终于听见了。"
    guide "别害怕，这里不是现实，但也不是梦。"
    hide guide idle

    "黑暗像水面一样裂开，一道细长的光从脚边蔓延出去。"
    "你来不及后退，身体已经被那道光拖入更深的地方。"

    jump chapter_01_inner_world

    return
