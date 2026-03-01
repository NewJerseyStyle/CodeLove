# ============================================================================
# 源界 (Source Realm) - Cee Chapter 3: 字串列車 (String Train)
# ============================================================================

label cee_C03_start:
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
    
    jump cee_03_end

label cee_03_suggest_alternative:
    menu:
        "加上終止符 (\\0)":
            jump cee_03_suggest_terminator
        "繼續觀察":
            jump cee_03_end

label cee_03_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：C 語言的字串是以 '\\0' 結尾的字元陣列。存取陣列時如果不注意邊界，會發生『緩衝區溢位』，這是一個嚴重的安全漏洞。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
