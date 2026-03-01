# ============================================================================
# 源界 (Source Realm) - Cee Chapter 4: 資料打包 (Packing Data)
# ============================================================================

label cee_C04_start:
    # 檢查之前的後果狀態
    if store.cee_consequence_state == "affected":
        scene bg memory_warehouse_packaging_clutter
        show cee tired at center
        
        cee "（搬運資料時動作緩慢）"
        cee "記憶體問題還在影響效率。"
        
        narrator "Cee 還在處理之前的後果，無法專心處理新的任務。"
        
        # Rusty 出現，她會更加嚴格
        show rusty worried at right
        
        rusty "Cee，你之前的記憶體問題還沒解決？"
        rusty "（看著你）是你讓她搞成這樣的吧？"
        
        menu:
            "解釋並承擔責任":
                jump cee_04_take_responsibility
            "先幫 Cee 清理後果":
                jump cee_04_help_cleanup_first
            "直接開始新的任務":
                jump cee_04_continue_with_consequence
    
    # 檢查 Rusty 的後果狀態
    if store.rusty_consequence_state == "affected":
        scene bg memory_warehouse_packaging
        show cee normal at center
        
        # Rusty 出現，她會更加嚴格
        show rusty angry at right
        
        rusty "（看著 Cee）上次緩衝區溢位，我的資料被覆蓋了。"
        rusty "（轉頭看著你）這次你們再搞出問題，我真的會向管理員報告的。"
        
        cee "（低頭）抱歉。"
        
        # 繼續正常流程
    else:
        # 正常流程
        scene bg memory_warehouse_packaging
        
        show cee normal at center
        
        # Rusty 出現
        show rusty normal at right
    
    cee "（正在處理一件複雜的貨物：一本舊書）"
    
    cee "編號位址：0x4000。價格位址：0x4010。作者位址：0x4020。"
    
    cee "（跑來跑去，試圖同時拿住這三個不同位址的東西）"
    
    cee "位置分散。傳輸低效。需要手動同步。"
    
label cee_04_take_responsibility:
    player "對，是我的建議導致了記憶體問題。"
    player "我承擔責任，會幫忙解決的。"
    
    rusty "（點頭）承認錯誤是第一步。"
    rusty "C 沒有安全網，操作者必須負責任。"
    rusty "你能理解這點，很好。"
    
    cee "（看著你）你會幫忙。理解了。"
    
    # 增加好感度
    $ track_affection("rusty", 10)
    $ track_affection("cee", 5)
    
    jump cee_04_main_task

label cee_04_help_cleanup_first:
    scene bg memory_warehouse_cleaning
    
    player "我們先清理之前的問題。"
    
    cee "（快速清理）釋放中..."
    
    # 清除後果
    python hide:
        for consequence in store.active_consequences:
            if consequence['type'] in ['memory_leak', 'buffer_overflow']:
                clear_consequence(consequence['id'])
    
    cee "（空間變得乾淨了）清理完成。"
    
    rusty "（點頭）做得好。負責任的開發者才是好開發者。"
    
    # 增加好感度
    $ track_affection("rusty", 15)
    $ track_affection("cee", 10)
    $ cee_available_time_reduction = 0
    
    jump cee_04_main_task

label cee_04_continue_with_consequence:
    cee "（勉強開始處理）"
    
    rusty "（搖頭）Cee，你這樣效率會很低。"
    rusty "而且很可能又出問題。"
    
    narrator "Cee 還在處理之前的後果，無法專心處理這個新任務。"
    
    # 追蹤
    $ track_choice("observation", is_optimal=False)
    
    jump cee_04_main_task

label cee_04_main_task:
    # Rusty 的對話根據之前的後果狀態有所不同
    if store.rusty_consequence_state == "affected":
        rusty "（嚴厲地）Cee，你這樣分開搬，萬一中間漏掉一個，這本書就不完整了！"
        rusty "（看著你）別再讓我的資料被覆蓋了，明白嗎？"
    else:
        rusty "呼... Cee，你這樣分開搬，万一中間漏掉一個，這本書就不完整了呀！"
        rusty "就像一個人，你不能把他的頭、手、腳分開存放在不同的儲存櫃裡吧？"
    
    cee "（停下來，思考）資料關聯性。它們屬於同一個實體。"
    
    narrator "你需要幫 Cee 將這些相關但類型不同的資料『打包』在一起。"

    menu:
        "建議使用『複合箱子』 (Struct)":
            jump cee_04_suggest_struct

        "建議使用『變身箱子』 (Union) 來節省空間":
            jump cee_04_suggest_union

        "問她為什麼不把所有東西都轉成字串存放在一起？":
            jump cee_04_ask_why_no_string_blob

label cee_04_ask_why_no_string_blob:
    player "為什麼不把它們全部轉成文字，塞進一個大箱子裡？"
    
    cee "（搖頭）解析成本太高。我需要直接存取原始數值。"
    
    cee "整數就是整數。浮點數就是浮點數。混合存儲會失去類型資訊。"
    
    jump cee_04_suggest_alternative

label cee_04_suggest_struct:
    player "Cee，我們定義一個『結構體』(Struct) 吧。"
    
    player "這是一個大箱子，裡面有專門放編號的小格、放價格的小格和放作者名的小格。"
    
    player "這樣你只要搬動這個大箱子，裡面的資料就會一起移動，而且位置是固定的！"
    
    cee "（眼睛一亮）"
    
    cee "自定義型別。記憶體對齊。0x4000 偏移量存取。"
    
    cee "（迅速將資料打包）打包完成。存取 `book.price`。一次到位。"
    
    cee "有效率。相關性 100%。"
    
    # 追蹤
    $ track_learned_concept("structs")
    $ track_affection("cee", 10)
    $ set_chapter_status("C_04", "completed")
    
    jump cee_04_end

label cee_04_suggest_union:
    player "如果這本書現在只有『編號』或是『名稱』其中一個，我們可以用『共同體』(Union)。"
    
    player "這是一個共用空間的箱子，它的大小取決於最大的那個成員。雖然一次只能存一個，但非常省空間！"
    
    cee "（計算中）空間利用率最大化。適合互斥資料。"
    
    cee "（嘗試使用 Union）節省了 40 位元組。不錯。"
    
    # 追蹤
    $ track_learned_concept("unions")
    $ track_affection("cee", 5)
    $ set_chapter_status("C_04", "completed")
    
    jump cee_04_end

label cee_04_suggest_alternative:
    menu:
        "使用結構體 (Struct) 打包":
            jump cee_04_suggest_struct
        "繼續觀察":
            jump cee_04_end

label cee_04_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：C 語言的 `struct` 允許你將不同型別的資料組合成一個邏輯單元。而 `union` 則讓不同成員共享同一塊記憶體，以節省空間。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
