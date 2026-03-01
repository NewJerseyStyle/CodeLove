# ============================================================================
# 源界 (Source Realm) - 日常與假日事件 (Daily Slices & Holidays)
# ============================================================================

init python:
    import random

# ============================================================================
# Jawa 的日常
# ============================================================================

label holiday_A:
    # 檢查 Cee 的後果狀態
    if store.cee_consequence_state == "affected":
        scene bg memory_warehouse_clutter
        show cee worried at center
        
        cee "（看著混亂的工作區）無法外出。"
        cee "（頭也不抬）之前的記憶體洩漏還沒清理完。"
        
        narrator "Cee 正在處理之前造成的後果，無法和你一起度過假日。"
        
        menu:
            "幫忙 Cee 清理記憶體（修復後果）":
                jump holiday_A_help_cee
            "去資訊廣場找 Jawa（跳過 Cee 的假日）":
                jump holiday_A_skip_cee
    
    # 檢查 Rusty 的後果狀態
    if store.rusty_consequence_state == "affected":
        scene bg information_square_corner
        show rusty angry at center
        
        rusty "（抱著頭）我的資料還沒恢復..."
        rusty "（看著你）你們搞出的亂子，害我這裡一團糟。"
        
        narrator "Rusty 還在處理之前的後果，心情很差。"
        
        menu:
            "幫 Rusty 恢復資料（修復後果）":
                jump holiday_A_help_rusty
            "去資訊廣場找 Jawa（讓 Rusty 冷靜一下）":
                jump holiday_A_skip_rusty
    
    $ event_variant = random.choice(["reading", "coffee"])
    jump expression f"jawa_daily_{event_variant}"

label holiday_A_help_cee:
    scene bg memory_warehouse_cleaning
    show cee normal at center
    
    cee "（看著你來幫忙）"
    cee "清理記憶體洩漏。需要釋放未歸還的空間。"
    
    player "我們一起來。每個箱子都確認一下是否還需要。"
    
    cee "（快速檢查）釋放中..."
    cee "free(0x2000);"
    cee "free(0x2100);"
    cee "free(0x2200);"
    
    pause 1.0
    
    cee "（空間變得乾淨了）清理完成。"
    
    # 清除記憶體洩漏後果
    python hide:
        for consequence in store.active_consequences:
            if consequence['type'] == 'memory_leak':
                clear_consequence(consequence['id'])
    
    cee "（看著你，停留 2 秒）有效率。"
    cee "（輕聲）下次記住，用完要還。"
    
    # 增加好感度
    $ track_affection("cee", 10)
    $ cee_available_time_reduction = 0
    
    # 追蹤
    $ track_learned_concept("memory_cleanup")
    
    narrator "Cee 的工作空間恢復了，但你們的假日已經花在清理上了。"
    
    jump end_time_period

label holiday_A_help_rusty:
    scene bg information_square_corner
    show rusty normal at center
    
    rusty "（看著你）你願意幫忙？"
    rusty "（深吸一口氣）好吧。這些是被覆蓋的資料區..."
    
    player "我們一起來修復。哪些區域損壞了？"
    
    rusty "（指向幾個位置）這裡，這裡，還有那裡。"
    rusty "需要重新編寫索引，然後檢查資料完整性。"
    
    pause 2.0
    
    rusty "（工作時）其實，C 並不是故意要搞壞資料的..."
    rusty "她只是太相信操作者了。"
    
    player "所以你才會這麼嚴格？"
    rusty "（點頭）如果有人不負責任，後果要整個系統承擔。"
    rusty "所以我在編譯時就阻止這些錯誤。"
    
    pause 1.0
    
    rusty "（完成）恢復完成。謝謝你。"
    
    # 清除緩衝區溢位後果
    python hide:
        for consequence in store.active_consequences:
            if consequence['type'] == 'buffer_overflow':
                clear_consequence(consequence['id'])
    
    # 增加好感度
    $ track_affection("rusty", 15)
    
    # 追蹤
    $ track_learned_concept("rust_safety")
    
    narrator "Rusty 的資料恢復了，她也解釋了為什麼 Rust 這麼注重安全。"
    
    jump end_time_period

label holiday_A_skip_cee:
    $ event_variant = random.choice(["reading", "coffee"])
    jump expression f"jawa_daily_{event_variant}"

label holiday_A_skip_rusty:
    $ event_variant = random.choice(["reading", "coffee"])
    jump expression f"jawa_daily_{event_variant}"
    scene bg information_square_afternoon
    show jawa normal at center
    narrator "你在資訊廣場偶遇了 Jawa。她正專心地讀著一本厚厚的手冊。"
    jawa "（抬頭）是你。今天不是工作時間，為什麼不休息一下？"
    player "看到你在這，就過來打個招呼。你在讀什麼？"
    jawa "一些關於『分散式共識算法』的論文。雖然是假日，但系統的優化是永無止境的。"
    player "Jawa，你總是這麼認真。休息也是優化的一部分哦。"
    jawa "（沉默片刻）休息也是優化... 很有趣的說法。我會考慮的。"
    $ track_affection("jawa", 5)
    jump end_time_period

label jawa_daily_coffee:
    scene bg coffee_shop_interior
    show jawa normal at center
    narrator "你在咖啡廳遇到了正在精確測量咖啡溫度的 Jawa。"
    jawa "精確到 88.5 度是萃取的最佳規範。溫度誤差超過 0.5 度都會導致口感的非預期行為。"
    player "這聽起來像是某種嚴格的編譯檢查。"
    jawa "（露出極淡的微笑）你可以這麼理解。規則讓咖啡更美味。"
    $ track_affection("jawa", 8)
    jump end_time_period

# ============================================================================
# Cee 的日常
# ============================================================================

label holiday_B:
    # 檢查 Cee 的後果狀態和可用時間
    if store.cee_consequence_state == "affected" or store.cee_available_time_reduction > 20:
        scene bg memory_warehouse_busy
        show cee tired at center

        cee "（忙著處理工作區的混亂）"
        cee "沒時間。不能出去。"

        if store.cee_consequence_state == "affected":
            cee "後果還在持續。需要清理。"
        else:
            cee "可用時間不足。需要趕進度。"

        narrator "Cee 無法和你一起度過假日。"

        menu:
            "幫忙 Cee（修復後果/趕進度）":
                jump holiday_B_help_cee
            "自己去資訊廣場逛逛":
                jump holiday_B_solo
            "去記憶倉庫最深處看看":
                jump holiday_B_explore
    else:
        # 根據 Cee 的關係狀態決定活動
        if store.cee_relationship in ["RELIABLE", "RESONANT"]:
            $ event_variant = random.choice(["river", "sorting", "deep_memory"])
        else:
            $ event_variant = random.choice(["river", "sorting"])
        jump expression f"cee_daily_{event_variant}"

label cee_daily_river:
    scene bg memory_warehouse_river
    show cee normal at center
    narrator "你在記憶倉庫的最深處找到了 Cee。她正看著前方流動的『記憶之河』。"
    cee "位址流動。0 到 無限。這就是源界的生命線。"
    player "這裡很美，Cee。"
    cee "（轉頭）工作之外。觀察資料的自然演化。這能幫我理解系統的邊界。"
    $ track_affection("cee", 5)
    jump end_time_period

label cee_daily_sorting:
    scene bg memory_warehouse_aisle
    show cee normal at center
    narrator "你看到 Cee 正在強迫症發作般地調整一排書的高度。"
    cee "（小聲）這本書的位址雖然正確，但物理高度偏離了 2 毫米。無效率的視覺佈局。"
    player "我幫你一起搬吧。"
    cee "（臉紅）嗯。手動對齊。加速中。"
    $ track_affection("cee", 8)
    jump end_time_period

label cee_daily_deep_memory:
    scene bg memory_warehouse_deep
    show cee normal at center
    narrator "Cee 帶你來到記憶倉庫的最深處。這裡沒有堆滿的箱子，只有流動的資料光流。"
    cee "（輕聲）這裡是源界的底層。很少有人能來。"
    cee "因為這裡沒有保護。只有那些真正理解記憶體的人，才能安然無恙。"
    player "這就是你最喜歡的地方？"
    cee "（點頭）這裡可以看到資料的本質。無需抽象層。"
    cee "（指向遠處）你看那個流動的位址...那是整個源界的『堆』區。"
    cee "每一次 malloc，就是從那裡劃出一塊。每一次 free，就是還回去。"
    player "所以你才能這麼快...因為你直接和最底層對話。"
    cee "（看著你，眼神柔和）你理解了。"
    cee "（停頓片刻）這個位給你。以後你可以直接來這裡。"
    cee "（給你一個小型的位址標籤）0xDEEP。只對你有效。"
    $ track_affection("cee", 15)
    $ track_learned_concept("memory_heap")
    jump end_time_period

label holiday_B_help_cee:
    scene bg memory_warehouse_cleaning
    show cee normal at center

    if store.cee_consequence_state == "affected":
        cee "（看著你來幫忙）"
        cee "清理後果。需要時間。"

        player "我們一起來。有什麼需要做的？"

        cee "檢查活躍後果列表。確認持續時間。"

        # 顯示後果摘要
        call show_consequence_summary

        cee "（開始清理）釋放未歸還的空間..."

        # 清除後果
        python hide:
            for consequence in store.active_consequences[:]:
                clear_consequence(consequence['id'])

        cee "（空間變得乾淨了）清理完成。"

        cee "（看著你）有效率。"

        # 增加好感度
        $ track_affection("cee", 10)
        $ cee_available_time_reduction = 0

        # 追蹤
        $ track_learned_concept("consequence_cleanup")

        narrator "你們的假日花在清理後果上了，但至少工作區恢復了。"

        jump end_time_period
    else:
        cee "（看著你來幫忙）"
        cee "趕進度。需要處理積壓的任務。"

        player "我來幫你整理這些資料。"

        cee "（點頭）好。分類索引。"

        pause 2.0

        cee "（快速處理）完成一半。"
        cee "剩餘時間：足夠。"

        # 減少可用時間減少量
        $ cee_available_time_reduction = max(0, store.cee_available_time_reduction - 15)

        # 增加好感度
        $ track_affection("cee", 5)

        narrator "你幫 Cee 趕了一些進度，但她還是沒法外出。"

        jump end_time_period

label holiday_B_solo:
    scene bg information_square_afternoon

    narrator "你獨自來到資訊廣場。沒有 Cee 的陪伴，顯得有些冷清。"

    narrator "遠處，你看到 Jawa 正在讀書，Rusty 在檢查設施。"

    menu:
        "去找 Jawa 聊聊":
            $ event_variant = "reading"
            jump expression f"jawa_daily_{event_variant}"
        "去找 Rusty 聊聊":
            jump rusty_daily_safety
        "獨自逛逛":
            jump end_time_period

label holiday_B_explore:
    scene bg memory_warehouse_deep

    narrator "你獨自來到記憶倉庫的最深處。沒有 Cee 的引導，你看到的是..."

    narrator "流動的資料光流，無盡的位址，還有未知的記憶碎片。"

    narrator "你試圖觸摸一個流動的位址，但被彈開了。"

    narrator "「訪問被拒絕」 - 這個區域需要特殊權限。"

    teaching "記憶體的底層世界既美麗又危險。沒有正確的理解和指引，可能會迷失其中。"

    $ track_learned_concept("memory_protection")

    jump end_time_period

# ============================================================================
# Rusty 的日常
# ============================================================================

label rusty_daily_safety:
    scene bg information_square_corner
    show rusty normal at center
    narrator "你看到 Rusty 正在檢查廣場噴泉的圍欄。"
    rusty "萬一有人在這裡發生空指針引用掉下去怎麼辦！我必須安裝更多的溢位保護！"
    player "你真的很注重安全呢，Rusty。"
    rusty "（認真地）因為安全是不可變的權利！"
    $ track_affection("rusty", 5)
    jump end_time_period

# ============================================================================
# Py 的日常
# ============================================================================

label py_daily_nap:
    scene bg information_square_park
    show py normal at center
    narrator "Py 正在草地上尋找最完美的午睡陰影。"
    py "這裡的光線縮排剛好是四格，完美。新來的，要一起躺會兒嗎？"
    player "你每天都在睡覺嗎？"
    py "這叫『延遲載入（Lazy Loading）』。不到真正需要的時候，絕對不浪費能量。"
    $ track_affection("py", 5)
    jump end_time_period
