# 角色定义统一放在这里，避免散落到章节脚本中。

default active_speaker = None

init python:
    import renpy.store as store

    def make_speaker_callback(char_id):
        # 发言开始时记录当前角色，发言结束后清空，供立绘层判断明暗状态。
        def speaker_callback(event, interact=True, **kwargs):
            if not interact:
                return

            if event == "show":
                store.active_speaker = char_id
            elif event == "end" and store.active_speaker == char_id:
                store.active_speaker = None

        return speaker_callback

define guide = Character("引导者", color="#8ec5ff", callback=make_speaker_callback("guide"))
define lianlian = Character("脸脸", color="#CEAC95", callback=make_speaker_callback("lianlian"))
define qingchuan = Character("晴川", color="#E9D499", callback=make_speaker_callback("qingchuan"))
define xiaoyu = Character("小雨", color="#C6E2D5", callback=make_speaker_callback("xiaoyu"))
define xuexue = Character("雪雪", color="#BFCCD8", callback=make_speaker_callback("xuexue"))
define yaxuan = Character("雅轩", color="#F2D9D0", callback=make_speaker_callback("yaxuan"))
define mengmeng = Character("梦梦", color="#D1C9DB", callback=make_speaker_callback("mengmeng"))
define lulu = Character("露露", color="#C9B1B8", callback=make_speaker_callback("lulu"))
