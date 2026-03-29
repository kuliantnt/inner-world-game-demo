# 第三章：把第二章抛出的陌生语音落到现实场景里，
# 让主角第一次在现实中追查“门”的对应入口。

label chapter_03_voice_trace:

    $ current_chapter = "第三章 语音落点"

    scene bg rental_room_night
    with fade

    "你盯着那条未读语音，指尖悬在屏幕上方，迟迟没有点下去。"
    "房间里安静得过分，像连空气都在等你做决定。"
    "手腕内侧那道灰白色的门印仍旧泛着凉意，比刚醒来时更清晰了一点。"

    menu:
        "你最后还是决定……"

        "立刻点开语音。":
            "你不想再把这件事往后拖。"
            "哪怕只是再听见一次那个声音，也总比继续靠猜来得干净。"

        "先深呼吸，再点开语音。":
            "你逼着自己把呼吸压稳。"
            "可当指尖真正落下去时，你还是感觉到心口猛地一紧。"

    $ listened_to_voice_note = True

    "语音长度只有七秒。"
    "前两秒几乎全是杂音，像收音很差的旧设备贴在谁的衣领边。"
    "第三秒开始，里面传来三下很轻的敲门声。"
    "然后是一个被电流撕得有些失真的声音。"

    "我在门外。"
    "这次，别再装作没听见。"

    "最后一秒里，还有一声短促的金属碰撞。"
    "像是老旧安全门在没有彻底关严时，被风轻轻顶了一下。"

    "语音自动播放结束。"
    "可那一小段带着回音的杂声，却像钩子一样卡在你耳边，迟迟散不掉。"

    "你几乎是下意识地抬头，看向出租屋的房门。"
    "门外没有脚步，也没有人敲门。"
    "可你非常确定，语音背景里的空间感，不像街边，也不像室外。"
    "更像一条狭窄、空荡、带着混响的楼道。"

    show xuexue idle at char_single
    with dissolve

    xuexue "你听出来了。"
    xuexue "不是普通录音。背景回声很近，混响长度也不对。"
    xuexue "声源大概率在封闭楼道，且门体较重。"

    "你猛地攥紧手机。"
    "雪雪的声音不是从门外传来的。"
    "它是顺着手腕上那道门印，直接贴进你脑海里的。"

    hide xuexue idle
    show qingchuan idle at char_single
    with dissolve

    qingchuan "先别慌。能听见我们，说明门印只是把感应连上了。"
    qingchuan "你现在站着的地方还是现实，不会一下子整个人掉回去。"

    hide qingchuan idle
    show lianlian idle at char_single
    with dissolve

    lianlian "把门打开。"
    lianlian "既然线索自己送到门口，就别磨蹭。"

    hide lianlian idle
    with dissolve

    "你走到玄关，手落在门把上时，门印忽然狠狠刺了一下。"
    "不是疼，更像冰针沿着皮肤往里扎。"
    "你咬了咬牙，把房门拉开。"

    scene bg apartment_corridor_night
    with dissolve

    "楼道里的感应灯慢了半拍才亮。"
    "昏黄的灯光把狭长走廊切成一段一段，墙面上还有旧水渍留下的暗痕。"
    "这一层总共只有四户。"
    "此刻却安静得像整层楼只剩你一个人。"

    "你低头又把那段语音放了一遍。"
    "第三秒响起的那三下敲门声，在空楼道里几乎和现实里的回音重叠到一起。"
    "而最后那声金属轻撞，分明来自走廊尽头那扇平时几乎没人碰的安全门。"

    $ reality_anchor_clue = "楼道尽头的安全门"

    "你抬起头。"
    "安全门上方的绿色指示牌闪得很弱，像随时会熄掉。"
    "那扇门平常一直关着，通往废弃了很久的旧楼梯间。"
    "你明明住在这里这么久，却几乎从没认真看过它。"

    show guide idle at char_single
    with dissolve

    guide "找到对应点了。"
    guide "门缝没有直接开在你房间门口。"
    guide "它借了你现实里最接近那段记忆的位置，先把锚落下来。"

    hide guide idle
    show mengmeng idle at char_single
    with dissolve

    mengmeng "别一下子逼自己想起全部。"
    mengmeng "先确认这里留下了什么，再往前走。"

    hide mengmeng idle
    with dissolve

    "你一步步朝走廊尽头走过去。"
    "越靠近那扇安全门，手腕上的凉意就越明显。"
    "直到只剩最后两步时，你忽然停住。"
    "门板靠近把手的位置，有一道新鲜的灰痕。"
    "像是谁刚用湿冷的手，在上面重重按过一次。"

    scene bg old_stairwell_door
    with dissolve

    menu:
        "你准备怎么确认它？"

        "直接伸手去碰门把。":
            "你没再让自己后退。"
            "手指碰到门把的一瞬间，掌心立刻窜起一股刺骨凉意。"

        "先贴近门缝听里面的动静。":
            "你先把耳朵贴了上去。"
            "门板另一侧一片死寂，直到你抬手碰上门把，寒意才猛地顺着指骨爬上来。"

    "下一秒，杂乱的画面猛地撞进脑海。"
    "昏暗楼道，急促呼吸，门外有人一下又一下拍着门。"
    "你看不清对方的脸，只听得见一句几乎失真的质问。"

    "你明明在里面，为什么不开门？"

    "你踉跄着后退半步，后背重重撞在墙上。"
    "安全门却在这一瞬间自己开出了一条细缝。"
    "门后没有人。"
    "只有旧楼梯间里一股陈年的灰尘味，混着很淡的潮气慢慢漫出来。"

    show xiaoyu idle at char_duo_left
    show yaxuan idle at char_duo_right
    with dissolve

    xiaoyu "它不是要把你拖进去。"
    xiaoyu "它是在让你看，这里真的有东西。"
    yaxuan "别怕。先看门口。"

    hide xiaoyu idle
    hide yaxuan idle
    with dissolve

    "你顺着雅轩的话低下头。"
    "门缝后侧的地面上，静静躺着一枚很旧的黄铜钥匙牌。"
    "牌子边缘已经磨花了，正中只剩下还能辨认的三个字。"

    "二一七。"

    "你的呼吸在那一刻彻底乱了。"
    "凌晨两点十七分。"
    "反复出现的时间。"
    "还有现在躺在你脚边、像从某段旧记忆里掉出来的钥匙牌。"

    "你弯腰把它捡起来时，门印不再发冷。"
    "那股逼得人心口发紧的压迫感，反而短暂地安静了下去。"

    show lulu idle at char_single
    with dissolve

    lulu "它满意了。"
    lulu "第一把钥匙，终于回到你手里。"

    hide lulu idle
    show guide idle at char_single
    with dissolve

    guide "记住这两个线索。"
    guide "时间，二一七。"
    guide "以及这枚钥匙牌原本对应的门。"

    hide guide idle
    show lianlian idle at char_duo_left
    show xuexue idle at char_duo_right
    with dissolve

    lianlian "今天到这里。别继续往楼梯间里钻。"
    lianlian "你现在的状态，进去只会被下一段回响狠狠干扰。"
    xuexue "建议成立。"
    xuexue "现阶段目标从‘确认异常’更新为‘追查 217 对应的现实位置’。"

    hide lianlian idle
    hide xuexue idle
    show qingchuan idle at char_single
    with dissolve

    qingchuan "至少这次你没再站在门前装作什么都没发生。"
    qingchuan "回房间吧。天亮以后，把和 217 有关的地方一个个排掉。"

    hide qingchuan idle
    with dissolve

    "你握紧那枚冰凉的钥匙牌，重新看向那扇半开的安全门。"
    "它没有再发出任何声音。"
    "可你已经知道，真正要找的那扇门，不在梦里。"
    "它就藏在现实某个你本来最不愿回头的地方。"

    scene black
    with fade

    "第三章结束时，你终于拿到了第一个能被现实握住的答案。"
    "而下一个问题，也比前两夜都更具体。"
    "二一七，究竟是哪一扇门？"

    return
