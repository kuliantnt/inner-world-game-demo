# 第二章：门缝第一次真正回应主角，并把现实线索抛出来。

label chapter_02_door_echo:

    $ current_chapter = "第二章 门缝回响"

    scene bg inner_world
    with dissolve

    "黑色潮水沿着裂缝一点点漫出来，像墨一样浸进原本纯白的长廊。"
    "空气忽然变得很重，连呼吸都像被什么压住。"

    show guide idle at char_single
    with dissolve

    guide "退后。"
    guide "这不是普通的门缝扩散。"
    guide "它在回应你。"

    "你愣了一下，还没反应过来，脚下的地面已经传来细碎的震动。"

    hide guide idle
    show lianlian idle at char_duo_left
    show qingchuan idle at char_duo_right
    with dissolve

    lianlian "才来第一晚就被门盯上，运气真够烂。你先站稳，别乱碰裂缝。"
    qingchuan "听她的。现在不是逞强的时候，先别让它把你牵走。"

    hide lianlian idle
    hide qingchuan idle
    show xiaoyu idle at char_duo_left
    show xuexue idle at char_duo_right
    with dissolve

    xiaoyu "不对，它不是在往外扩。"
    xiaoyu "它在认人，像闻到熟悉味道以后死咬着不放。"
    xuexue "更准确一点，是记忆匹配。"
    xuexue "门缝碰到他之后，被某段未处理完成的残留记忆勾住了。"

    "你听见最后那句话，胸口无端地收紧。"
    "仿佛有一只手，正从更深的地方把某个你不愿想起的夜晚硬生生拽出来。"

    hide xiaoyu idle
    hide xuexue idle
    show yaxuan idle at char_trio_left
    show mengmeng idle at char_trio_center
    show lulu idle at char_trio_right
    with dissolve

    yaxuan "引导者，你带他稳住视线。"
    yaxuan "脸脸和晴川负责封边，小雨、雪雪继续判断回响来源。"
    mengmeng "如果真是他的回响，就不能硬切。痛感会全砸回他身上。"
    lulu "而且门会记仇。被这样撕开的东西，通常不会只开一次。"

    "你猛地抬头。"
    "露露说这句话时语气很轻，像在说一件早就见过很多次的事。"

    hide yaxuan idle
    hide mengmeng idle
    hide lulu idle
    show guide idle at char_single
    with dissolve

    guide "看着我。"
    guide "接下来无论你听见什么，都不要立刻否认。"
    guide "里世界最擅长把人拼命藏起来的东西，原封不动地照出来。"

    "裂缝里传出模糊的声响。"
    "一开始像风，再后来，竟慢慢变成了人声。"

    "你为什么没有开门？"

    "那声音轻得几乎像错觉。"
    "可你全身的血却在一瞬间凉了下去。"

    "长廊深处浮出一扇半透明的门。"
    "它没有实体，门把上却沾着湿漉漉的黑色痕迹，像刚被谁用力握过。"

    guide "看见了吗？"
    guide "这就是回响。"
    guide "它不会凭空制造答案，只会把你没说出口的话重新摆到你面前。"

    "你的喉咙发紧，连视线都开始轻微发颤。"
    "你确定自己从来没见过这扇门。"
    "可更可怕的是，你又觉得自己早就站在它面前很多次。"

    menu:
        "面对那扇门时，你最先承认的是……"

        "我那晚其实听见了声音。":
            $ first_confession = "heard_voice"
            "记忆像被撕开一道口子。"
            "你想起那晚自己站在门外，手已经抬起来，却在最后一秒停住。"
            "因为你听见了声音。"
            "也正因为听见了，你才比任何时候都清楚，自己最后还是退开了。"

        "我一直在假装，那件事和我无关。":
            $ first_confession = "pretend_unrelated"
            "你第一次承认，自己这些日子并不是忘了。"
            "而是假装没看见，假装没参与，假装只要闭口不提，一切就不会再追上来。"
            "可那种自欺在这条长廊里薄得像纸，一碰就破。"

        "我根本不敢想，门后到底发生过什么。":
            $ first_confession = "fear_truth"
            "你始终没有真正去回想那个夜晚。"
            "不是因为记不清，而是因为你知道，一旦想起来，就必须面对某个答案。"
            "而你直到现在都还没准备好。"

    "裂缝里的黑潮忽然停了一瞬。"
    "像是某种盘踞已久的东西，终于等到了你亲口说出的那句话。"

    hide guide idle
    show mengmeng idle at char_single
    with dissolve

    mengmeng "它安静下来了。"
    mengmeng "不是被压住，是终于等到他肯开口。"

    hide mengmeng idle
    show xuexue idle at char_duo_left
    show yaxuan idle at char_duo_right
    with dissolve

    xuexue "回响完成了第一轮锁定。"
    yaxuan "继续。让他自己给那扇门一个方向。"

    "你怔住。"
    "那扇半透明的门仍停在前方，门缝里只有一片看不透的黑。"
    "可你忽然明白，她们说的不是让你真的去碰一扇门。"
    "而是让你第一次别再后退。"

    hide xuexue idle
    hide yaxuan idle
    show guide idle at char_single
    with dissolve

    guide "你可以什么都想不起来。"
    guide "但你至少要告诉它，你这次不逃。"

    "你盯着那扇门，缓慢地吸了一口气。"
    "胸口仍旧发紧，可那股想要转身逃走的冲动，第一次被你硬生生压了下去。"

    "你朝那扇门伸出手。"

    "如果那天晚上，我真的漏掉了什么……"
    "那我会回去亲自确认。"

    "话音落下的瞬间，整条长廊像被什么重重敲了一下。"
    "黑潮骤然倒卷，裂缝里的人声也在同一秒破碎开来。"

    hide guide idle
    show lianlian idle at char_duo_left
    show qingchuan idle at char_duo_right
    with dissolve

    lianlian "暂时收回去了。下次它再扑出来，你先给我退到安全线后面。"
    qingchuan "别被她语气骗到。意思是，她已经把你算进保护范围了。"
    qingchuan "不过她说得对，它还会再来。"

    hide lianlian idle
    hide qingchuan idle
    show xiaoyu idle at char_duo_left
    show lulu idle at char_duo_right
    with dissolve

    xiaoyu "你手上有东西！刚才还没有的。"
    lulu "呀，门印。它喜欢把看中的人先圈起来。"

    "你低头看去，手腕内侧不知何时多出一道灰白色的细纹。"
    "它像一枚没有闭合的圆环，边缘微微发冷，像刚从雾里拿出来。"

    $ inner_world_mark = True

    hide xiaoyu idle
    hide lulu idle
    show guide idle at char_single
    with dissolve

    guide "门记住你了。"
    guide "从现在开始，你不只是能听见里世界的人。"
    guide "你还是它的锚点。"

    "你还没来得及问清“锚点”是什么意思，雅轩已经接过了话。"

    hide guide idle
    show yaxuan idle at char_single
    with dissolve

    yaxuan "意思就是，现实里的某个地方，很可能存在与你这段回响对应的入口。"
    yaxuan "你必须把它找出来。"
    yaxuan "否则下一次门缝扩大，出来的就不只是声音了。"

    hide yaxuan idle
    show qingchuan idle at char_duo_left
    show mengmeng idle at char_duo_right
    with dissolve

    qingchuan "别一下子把重量全压给他。"
    qingchuan "至少刚刚那一波，他是真的自己站住了。"
    mengmeng "而且他已经给了里世界一个答案。"
    mengmeng "接下来，轮到现实慢慢把后面的那句补上了。"

    hide qingchuan idle
    hide mengmeng idle
    show guide idle at char_single
    with dissolve

    guide "今晚到此为止。"
    guide "回去之后，想办法找到一个线索。"
    guide "一扇门、一个名字、一段被你刻意绕开的记忆，什么都可以。"
    guide "下次再见时，我们从那个线索开始。"

    "白色长廊重新变得安静。"
    "仿佛刚才那场几乎要把你吞进去的黑潮，从头到尾都只是幻觉。"
    "只有手腕上的灰白印记还在提醒你，事情并没有结束。"

    scene black
    with fade

    "视野坠入黑暗之前，你最后听见的，是那句熟悉却终于清晰起来的低语。"
    "找到那扇门。"

    "你猛地从床上坐起。"
    "房间和入睡前没有任何区别，连窗帘缝里漏进来的夜色都安静得过分。"
    "可手机屏幕正亮着。"
    "时间是凌晨两点十七分。"
    "通知栏最上面只有一条陌生号码发来的未读语音。"

    "而那条语音的标题，只有短短四个字。"

    "门外等你。"

    jump chapter_03_voice_trace
