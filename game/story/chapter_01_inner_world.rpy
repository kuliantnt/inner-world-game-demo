# 第一章：进入里世界并完成核心角色的第一次亮相。

label chapter_01_inner_world:

    $ current_chapter = "第一章 里世界"

    scene bg inner_world
    with dissolve

    "意识重新聚拢时，你站在一条看不见尽头的白色长廊里。"
    "脚下没有影子，头顶也没有天花板，四周像被雾包住一样空旷。"

    show guide idle at char_single
    with dissolve

    guide "欢迎来到里世界。"
    guide "你可以把这里理解成现实背面留下来的缝隙。"
    guide "情绪、执念、没有说出口的话，都会在这里留下痕迹。"

    "你张了张口，喉咙却像是被什么堵住。"

    menu:
        "你最先想问的是……"

        "这里到底是什么地方？":
            "你强迫自己冷静下来，盯着眼前唯一能交流的身影。"
            guide "一个会把人真正模样照出来的地方。"

        "为什么是我？":
            "这个问题脱口而出，比恐惧更先一步占据你的脑海。"
            guide "因为门先回应了你。"
            guide "能听见里世界声音的人，本来就不多。"

    "长廊尽头传来轻微的脚步声。"
    "一道、两道、三道，最后像潮水一样逐渐靠近。"

    hide guide idle
    with dissolve

    show lianlian idle at char_duo_left
    show qingchuan idle at char_duo_right
    with dissolve

    lianlian "就是他？看着快站不稳了。别一下子围这么近，吓坏了最后还是我收场。"
    qingchuan "听见没有？她这人开口像在挑刺，实际上是在让你先别怕。"

    hide lianlian idle
    hide qingchuan idle
    show xiaoyu idle at char_duo_left
    show xuexue idle at char_duo_right
    with dissolve

    xiaoyu "他手都在抖诶。你们不要摆出一副审讯样子，好像下一秒就要把他拆开看。"
    xuexue "结论：惊吓过量，信息处理超载。先降低刺激，再解释规则。"

    hide xiaoyu idle
    hide xuexue idle
    show yaxuan idle at char_trio_left
    show mengmeng idle at char_trio_center
    show lulu idle at char_trio_right
    with dissolve

    yaxuan "先让他把呼吸缓下来。话不用一次说完，人先稳住。"
    mengmeng "嗯，先接住他。能不能留下来，也该等他不那么害怕再说。"
    lulu "原来这次来的，是会把门也吵醒的类型。"

    "七道目光几乎同时落在你身上。"
    "明明每个人的语气都不同，但你却莫名感觉到一种一致的压迫。"

    hide yaxuan idle
    hide mengmeng idle
    hide lulu idle
    show guide idle at char_single
    with dissolve

    guide "介绍一下，她们就是现在守着里世界的人。"
    guide "脸脸、晴川、小雨、雪雪、雅轩、梦梦，还有露露。"
    guide "而你，是最近唯一一个被门主动带进来的人。"

    "你本能地后退半步，却发现退路早就消失了。"

    hide guide idle
    show lianlian idle at char_duo_left
    show qingchuan idle at char_duo_right
    with dissolve

    lianlian "紧张可以，别硬撑。你要是真在这里失控，我还得把你从门边拽回来。"
    qingchuan "翻译一下，她是在告诉你，这里暂时不会把你一个人丢着。"

    hide lianlian idle
    hide qingchuan idle
    show xiaoyu idle at char_duo_left
    show yaxuan idle at char_duo_right
    with dissolve

    xiaoyu "想回去就回去呀，但你别假装今晚什么都没发生。那样最笨了。"
    yaxuan "见过门的人，很难再把自己骗回原样。"

    "你沉默了几秒，最终还是抬起头。"
    "你低声问出那个最现实的问题。"
    "如果我想回去呢？"

    "长廊里短暂地安静了一瞬。"

    hide xiaoyu idle
    hide yaxuan idle 
    show guide idle at char_single

    guide "可以。"
    guide "但门已经记住你了。"
    guide "从今晚开始，里世界会一遍遍出现在你的梦里，直到你主动做出选择。"

    hide guide idle
    show mengmeng idle at char_single
    with dissolve

    mengmeng "所以现在最重要的，不是把你留下。"
    mengmeng "而是让你知道，你已经站进门里了，不用再一个人装作没事。"

    "雾气深处忽然传来一声细微的碎裂声。"
    "所有人的表情同时变了。"

    hide mengmeng idle
    hide guide idle
    show xuexue idle at char_trio_left
    show lulu idle at char_trio_center
    show yaxuan idle at char_trio_right
    with dissolve

    xuexue "波动提前了。比预测时间早。"
    lulu "门缝在闻新的回响。它对他很好奇。"
    yaxuan "闲聊到此为止。先把他带离中心区域。"

    hide xuexue idle
    hide lulu idle
    hide yaxuan idle
    show guide idle at char_single
    with dissolve

    guide "记住现在这一刻。"
    guide "从你踏进里世界开始，现实就已经不再只有一层了。"

    "还没等你追问，整个长廊猛地震动起来。"
    "白色墙面像镜子一样出现裂纹，黑色的潮水正从裂缝另一端缓慢渗出。"

    hide guide idle
    with dissolve

    "第一章，到这里才算真正开始。"

    jump chapter_02_door_echo
