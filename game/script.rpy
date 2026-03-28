# 游戏入口文件。
# 这里负责启动流程控制，不直接堆放具体章节内容。

label start:

    call game_bootstrap
    jump chapter_01_prologue


label game_bootstrap:

    window hide
    scene black
    with fade

    return
