# 角色定义统一放在这里，避免散落到章节脚本中。
# Demo 阶段把“角色名显示”“说话颜色”“发言高亮逻辑”都集中在这里，
# 后面查角色相关配置时只需要看这一个文件。

# 这个变量不参与剧情分支，只负责 UI 表现。
# 当前正在发言的角色 id。
# 立绘层会读取这个状态，决定谁保持正常、谁进入半暗状态。
default active_speaker = None

init python:
    import renpy.store as store

    # 这里不直接给每个角色手写一套重复回调，
    # 而是用一个工厂函数按角色 id 批量生成，后续新增角色更省事。
    def make_speaker_callback(char_id):
        # 给每个 Character 生成一个专属回调。
        # 这样角色一开口时就能把自己登记为“当前发言者”。
        def speaker_callback(event, interact=True, **kwargs):
            # 非交互阶段的内部刷新不参与焦点切换，
            # 否则容易在界面刷新时把当前角色状态弄乱。
            if not interact:
                return

            # Ren'Py 在一段对白显示出来时会触发 show。
            if event == "show":
                store.active_speaker = char_id
            # 这段对白结束后清空，避免下一次界面刷新时误判。
            elif event == "end" and store.active_speaker == char_id:
                store.active_speaker = None

        return speaker_callback

# 下面这批 define 是“角色资料表”。
# 目前每个角色统一配置：
# 1. 对话框中显示的名字
# 2. 名字颜色
# 3. 发言时更新 active_speaker 的回调
#
# 剧情层写法保持普通 Ren'Py 习惯即可，例如：
# guide "你终于听见了。"
# lianlian "所以就是他？"
#
# 不需要在章节脚本里额外手动设置“谁变亮、谁变暗”。
# 每个角色都挂上 callback，后续章节里正常写对白即可自动切换立绘明暗。
define guide = Character("引导者", color="#8ec5ff", callback=make_speaker_callback("guide"))
define lianlian = Character("脸脸", color="#CEAC95", callback=make_speaker_callback("lianlian"))
define qingchuan = Character("晴川", color="#E9D499", callback=make_speaker_callback("qingchuan"))
define xiaoyu = Character("小雨", color="#C6E2D5", callback=make_speaker_callback("xiaoyu"))
define xuexue = Character("雪雪", color="#BFCCD8", callback=make_speaker_callback("xuexue"))
define yaxuan = Character("雅轩", color="#F2D9D0", callback=make_speaker_callback("yaxuan"))
define mengmeng = Character("梦梦", color="#D1C9DB", callback=make_speaker_callback("mengmeng"))
define lulu = Character("露露", color="#C9B1B8", callback=make_speaker_callback("lulu"))
