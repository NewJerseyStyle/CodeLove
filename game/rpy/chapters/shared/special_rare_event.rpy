# ============================================================================
# 源界 (Source Realm) - 特殊稀有事件
# ============================================================================

init python:
    # 持久化標記：記錄玩家是否已經遇到過這個特殊事件
    # 使用 persistent 變數確保即使重新開始新遊戲也不會再次觸發
    if not hasattr(persistent, "special_event_encountered"):
        persistent.special_event_encountered = False

    # 標記音樂是否已經播放過（每次遊戲只播放一次）
    if not hasattr(persistent, "special_music_played"):
        persistent.special_music_played = False

label check_special_rare_event:
    # 1% 機率觸發特殊事件
    $ special_chance = renpy.random.random()
    if special_chance < 0.01 and not persistent.special_event_encountered:
        $ persistent.special_event_encountered = True
        $ stop_plaza_music()
        jump special_rare_event_intro
    else:
        jump execute_explore_random_normal

label special_rare_event_intro:
    # 特殊事件開始
    scene black

    narrator "你漫無目的地走著，不知不覺來到了一個從未見過的地方..."

    # 描述場景
    narrator "周圍的數據粒子停止了流動，空氣中瀰漫著一種安靜而神秘的氛圍。"

    narrator "遠處，一個身影正背對著你，看著什麼東西。"

    # 播放特殊音樂
    if not persistent.special_music_played:
        play music "audio/14310_midi-lofi.mp3" fadein 5.0
        $ persistent.special_music_played = True

    # 使用文字描述特殊人物

    narrator "她有一種無法言喻的氣質——聰慧、優雅，彷彿看透了源界的一切本質。"

    # 特殊事件開始
    scene special
    with Dissolve(2.0)

    "???" "源界的故事，是我最初的構想。"

    "???" "但我沒有想到... 還會有其他人走進來，一同體驗這個世界。"

    menu:
        "我想聽... 我想了解更多":
            jump special_rare_event_listen
        "我得走了...":
            jump special_rare_event_leave
        "（靜靜地看著她，不說話）":
            jump special_rare_event_stunned

label special_rare_event_listen:
    narrator "你走近了一些。"

    scene black
    with fade

    "???" "很久以前，我問了一個問題..."

    "???" "如何讓人們理解程式語言？"

    "???" "不是通過枯燥的課本..."

    "???" "而是通過故事，通過情感，通過親身體驗。"

    "???" "他說，我們試試看吧！"

    "???" "於是，源界誕生了。"

    "???" "那之後又過了八年，荒蕪的世界迎來新的居民。"

    "???" "如今每一個角色，都是一種思維方式的具象。"

    "???" "Cee 的直接與高效，Jawa 的嚴謹與規範，Rusty 的安全與審慎..."

    "???" "她們不僅僅是『語言』，她們是有生命的存在。"

    "???" "而你... 你正在學會理解她們，對嗎？"

    narrator "她的話語讓你陷入了思考。"

    narrator "是啊，每一個角色的行為背後，都有一個深刻的設計哲學。"

    "???" "繼續探索吧。"

    "???" "源界還有很多秘密等待發現。"

    "???" "當你真正理解了她們... 也許有一天，你會創造出屬於你的世界。"

    narrator "她的身影漸漸變得透明。"

    "???" "別了。。。探險者。。。"

    stop music fadeout 10.0

    narrator "當她的身影完全消失時，你發現自己又回到了熟悉的廣場。"

    narrator "一切如常，彷彿剛才的一切只是一場夢。"

    $ source_realm_reputation += 50

    jump end_time_period

label special_rare_event_leave:
    narrator "你輕輕搖頭，轉身離開。"

    scene black
    with fade
    stop music fadeout 2.0

    narrator "當你停下腳步時，發現自己又回到了廣場。"

    jump end_time_period

label special_rare_event_stunned:
    narrator "你只是看著她，一句話也說不出來。"

    narrator "她的存在本身就像一個謎題，讓你完全被吸引。"

    narrator "周圍的一切仿佛都靜止了。"

    pause 3.0

    # 黑屏
    scene black
    with fade

    narrator "時間不知過去了多久..."

    narrator "你的思緒彷彿被帶到了很遠的地方，又或者... 什麼地方都沒去。"

    pause 4.0

    narrator "你突然回過神來。"

    narrator "周圍一片漆黑。"

    narrator "剛才的場景，那個人... 都消失了。"

    narrator "只剩下你一個人，站在黑暗中。"

    pause 2.0

    narrator "你看了看自己的雙手，又看了看四周。"

    narrator "剛才發生了什麼？"

    narrator "你看呆了？還是... 時間真的過去了這麼久？"

    pause 2.0

    narrator "當你再次睜開眼睛時，發現自己站在廣場上。"

    narrator "周圍的路人來來往往，沒人注意到你剛才的異樣。"

    narrator "只有一種說不出的感覺... 仿佛見到了不可能存在的事物。"

    stop music fadeout 10.0
    $ source_realm_reputation += 100

    narrator "這是一次真正的奇遇。"

    jump end_time_period
