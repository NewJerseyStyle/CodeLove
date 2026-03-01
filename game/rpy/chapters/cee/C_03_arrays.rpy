# ============================================================================
# 源界 (Source Realm) - Cee Chapter 3: 字串列車 (String Train)
# ============================================================================

label cee_C03_start:
    # 檢查 Cee 是否受到之前的後果影響
    if store.cee_consequence_state == "affected":
        cee "（看著雜亂的工作區）之前的記憶體洩漏還在清理中..."
        cee "這個字串列車先放一邊。"
        
        narrator "Cee 忙於處理之前的後果，無法專心處理新的任務。"
        
        menu:
            "幫忙清理之前的記憶體洩漏":
                jump cee_03_help_cleanup
            "繼續進行字串列車任務":
                jump cee_03_continue_with_consequence
    
    # 檢查 Rusty 是否受影響
    if store.rusty_consequence_state == "affected":
        rusty "（看著亂七八糟的工作區）我的資料還沒恢復..."
        rusty "如果你再搞出緩衝區溢出，我真的會生氣的。"
    
    scene bg memory_warehouse_train
    
    show cee normal at center
    
    cee "（站在一排連在一起的小型貨車廂前）"
    
    cee "陣列傳輸模式。連續位址。0x3000 到 0x3010。"
    
    cee "（指著第一節車廂）索引 0。內容：'H'。"
    
    cee "（指著第二節車廂）索引 1。內容：'E'。"
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "唉，Cee！這列『字串火車』又失控了！"
    
    # 遠處傳來碰撞聲
    play sound "audio/crash.ogg"
    
    rusty "（抱頭）你看！因為你沒在最後一節車廂掛上『終止符號』，火車頭以為後面還有車，結果撞到了別人的資料區！"
    
    cee "（面無表情）連續存取。直到讀取到空值。"
    
    cee "如果中間沒有空值，就會一直往後讀。直到...崩潰。"
    
    narrator "你需要幫 Cee 解決兩個問題：字串的終止 (Null Terminator) 以及 存取越界 (Buffer Overflow)。"

    menu:
        "建議在末尾加上『終止符』 (\\0)":
            jump cee_03_suggest_terminator

        "建議縮減字串長度，不要超過車廂數量":
            jump cee_03_suggest_bounds_check

        "問她為什麼不一開始就規定好長度？":
            jump cee_03_ask_why_no_length
            
        "不管它，繼續寫入":
            jump cee_03_risky_write

label cee_03_ask_why_no_length:
    player "為什麼不一開始就給火車掛個『長度牌』？比如：長度 5。"
    
    cee "（看著你）那需要額外的空間存儲『長度』。"
    
    cee "C 語言選擇用一個隱藏的 0 來標記結尾。節省空間。"
    
    rusty "（小聲）雖然省了空間，但如果忘了那個 0，後果真的很可怕..."
    
    jump cee_03_suggest_alternative

label cee_03_suggest_terminator:
    player "Cee，我們在最後一個字元後面，手動加一個數值為 0 的空箱子 (\\0)。"
    
    player "這樣讀取的人一看到這個箱子，就知道這列火車結束了。"
    
    cee "（思索）手動結尾。傳統做法。"
    
    cee "（迅速在最後掛上標記）"
    
    cee "存取中... 'H', 'E', 'L', 'L', 'O', '\\0'。停止。"
    
    cee "（點頭）有效率。讀取到此為止。"
    
    # 追蹤
    $ track_learned_concept("null_terminator")
    $ track_affection("cee", 10)
    $ set_chapter_status("C_03", "completed")
    
    # 如果有記憶體洩漏後果，部分緩解（但沒有清除）
    if store.cee_consequence_state == "affected":
        cee "（看著你）雖然字串問題解決了，但之前的記憶體問題還在。"
    
    jump cee_03_end

label cee_03_suggest_bounds_check:
    player "Cee，這火車只有 5 節車廂，你別把 10 個字強塞進去啊！"
    
    player "塞不下的字會溢位到別人的地盤，那叫『緩衝區溢位』。"
    
    cee "（看著太長的資料）截斷處理。只取前 5 位。"
    
    cee "（強制切掉多餘字元）安全性提升。雖然損失了部分資料。"
    
    # 追蹤
    $ track_learned_concept("bounds_check")
    $ track_affection("cee", 5)
    $ set_chapter_status("C_03", "completed")
    
    # 邊界檢查可以避免新的緩衝區溢位，但不能修復已經存在的後果
    
    jump cee_03_end

label cee_03_risky_write:
    player "Cee，不管邊界，直接強制寫入。"
    
    cee "（執行）強制寫入模式。"
    cee "忽略邊界檢查。"
    
    cee "（寫入中...）"
    
    # 遠處傳來更嚴重的碰撞聲
    play sound "audio/huge_crash.ogg"
    
    cee "（突然僵住）錯誤。緩衝區溢位。"
    cee "（眼神空白）寫入越界。覆蓋了鄰近區域。"
    
    # 如果 Rusty 已經受影響，後果更嚴重
    if store.rusty_consequence_state == "affected":
        # Rusty 已經受影響，這次是嚴重後果
        rusty "（尖叫）我的資料！！又！！被！！覆蓋！！了！！"
        rusty "（氣沖沖地走開）這次我再也不幫你們了！"
        
        # 觸發嚴重後果
        $ apply_consequence("buffer_overflow", "severe", "在 Rusty 資料已受損時再次導致緩衝區溢位")
        call show_consequence_notification("buffer_overflow", "severe")
        
        $ track_affection("rusty", -30)
    else:
        # Rusty 還沒受影響，這次是中等後果
        rusty "我的資料！全被覆蓋了！"
        rusty "（氣沖沖地過來）這需要幾小時才能恢復！"
        
        # 觸發中等後果
        $ apply_consequence("buffer_overflow", "moderate", "忽略陣列邊界導致緩衝區溢位")
        call show_consequence_notification("buffer_overflow", "moderate")
        
        $ track_affection("rusty", -15)
    
    # 顯示教學卡片
    $ current_consequence_type = "buffer_overflow"
    call show_consequence_teaching
    
    # 顯示 Rusty 的反應
    $ current_reaction_character = "rusty"
    $ current_reaction_consequence = "buffer_overflow"
    call show_consequence_reaction
    
    # Cee 重啟
    pause 2.0
    cee "（恢復）重啟完成。"
    cee "寫入失敗。鄰近區域已損毀。"
    
    # 更新 Cee 的可用時間
    $ cee_available_time_reduction += 20
    
    # 追蹤
    $ track_choice("algorithm", is_optimal=False)
    $ track_consequence("severe" if store.rusty_consequence_state == "affected" else "moderate")
    $ cee_relationship = "FUNCTIONAL"
    $ set_chapter_status("C_03", "failed")
    
    jump cee_03_end

label cee_03_help_cleanup:
    scene bg memory_warehouse_cleaning

    cee "（看著你來幫忙）"
    cee "清理記憶體洩漏。需要釋放未歸還的空間。"

    player "我們一起來。每個箱子都確認一下是否還需要。"

    cee "（快速檢查）0x2000 - 已過期。釋放。"
    cee "0x2100 - 已過期。釋放。"
    cee "0x2200 - 已過期。釋放。"

    pause 1.0

    cee "（空間變得乾淨了）清理完成。"

    # 清除記憶體洩漏後果
    python hide:
        for consequence in store.active_consequences:
            if consequence['type'] == 'memory_leak':
                clear_consequence(consequence['id'])

    # Rusty 感激
    rusty "（走過來）謝謝你幫忙清理。"
    rusty "如果不處理，這些『幽靈資料』會一直佔用空間。"

    # 增加好感度
    $ track_affection("cee", 5)
    $ track_affection("rusty", 10)
    $ cee_available_time_reduction = 0

    # 追蹤
    $ track_learned_concept("memory_cleanup")

    narrator "Cee 的工作空間恢復了，但你們的時間花在清理上了。"

    # 清理完成，結束這個時間段
    jump end_time_period

label cee_03_force_continue:
    # 玩家強行繼續，但效率降低
    cee "（手忙腳亂地處理）索引 0... 索引 1..."

    narrator "Cee 因為分心處理之前的問題，效率大幅下降。"

    menu:
        "加上終止符 (\\0)":
            jump cee_03_suggest_terminator
        "建議邊界檢查":
            jump cee_03_suggest_bounds_check
        "繼續觀察":
            jump cee_03_end

label cee_03_suggest_alternative:
    menu:
        "加上終止符 (\\0)":
            jump cee_03_suggest_terminator
        "建議邊界檢查":
            jump cee_03_suggest_bounds_check
        "繼續觀察":
            jump cee_03_end
    $ track_affection("cee", 5)
    $ track_affection("rusty", 10)
    $ cee_available_time_reduction = 0
    
    # 追蹤
    $ track_learned_concept("memory_cleanup")
    
    jump cee_03_start

label cee_03_continue_with_consequence:
    cee "（勉強開始處理字串列車）"
    
    cee "（心不在焉地）陣列傳輸模式。連續位址。0x3000 到 0x3010。"
    
    rusty "Cee，你確定你能專心嗎？後面還有沒處理完的問題呢。"
    
    narrator "Cee 還在忙著處理之前的後果，無法專心處理這個新任務。"
    
    menu:
        "幫忙清理之前的問題":
            jump cee_03_help_cleanup
        "硬著頭皮繼續":
            jump cee_03_force_continue

label cee_03_force_continue:
    # 玩家強行繼續，但效率降低
    cee "（手忙腳亂地處理）索引 0... 索引 1..."

    narrator "Cee 因為分心處理之前的問題，效率大幅下降。"

    menu:
        "加上終止符 (\\0)":
            jump cee_03_suggest_terminator
        "建議邊界檢查":
            jump cee_03_suggest_bounds_check
        "繼續觀察":
            jump cee_03_end

label cee_03_suggest_alternative:

label cee_03_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：C 語言的字串是以 '\\0' 結尾的字元陣列。存取陣列時如果不注意邊界，會發生『緩衝區溢位』，這是一個嚴重的安全漏洞。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
