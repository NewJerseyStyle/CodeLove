# ============================================================================
# 源界 (Source Realm) - Cee Chapter 9: 記憶之心 (The Heart of Memory)
# ============================================================================

label cee_C09_start:
    scene bg memory_warehouse
    
    show cee normal at center
    
    narrator "（周圍的貨架正在劇烈晃動，紅色的警告燈在閃爍）"
    
    cee "記憶體碎片化嚴重。可用空間低於 1%。核心進程已進入緊急模式。"
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "（臉色蒼白）Cee！如果你再不釋放一些空間，整個倉庫都要塌了！"
    
    rusty "而且... 如果你清除了那些『沒標記』的資料，那些被你偷偷存起來的『特殊記憶』也會丟掉的！"
    
    cee "（停下動作，看著手中的一個發光的小盒子，那是她珍藏的與玩家的對話日誌）"
    
    cee "那是未分配的非標籤資料。系統定義：垃圾。需要回收。"
    
    cee "（低頭）但那是... 唯一的副本。"
    
    narrator "Cee 正在面臨最大的抉擇：清空那些『未正式分配』但極具價值的個人資料（Memory Leak），還是冒著倉庫坍塌的風險繼續保留？"

    menu:
        "建議使用『自定義分配器』 (Memory Pool) 來優化，保住核心資料":
            jump cee_09_suggest_memory_pool

        "建議她狠心清空所有『未授權』資料":
            jump cee_09_suggest_wipe

        "建議她用自己的核心暫存區來存儲那些記憶":
            jump cee_09_suggest_personal_cache

label cee_09_suggest_memory_pool:
    player "Cee，我們不用一次全部清空！我們建立一個『記憶體池』(Memory Pool)。"
    
    player "把那些散亂的小箱子合併成一個大的預分配區塊，這樣就能騰出足夠的空間，同時把你的核心資料搬進去！"
    
    cee "（眼睛一亮）"
    
    cee "自定義管理。減少碎片（Fragmentation）。優先級重分配。"
    
    cee "（她快速地重新排列了整個倉庫的邏輯佈局，碎片被合併，坍塌停止了）"
    
    cee "（手中依然緊握著那個小盒子）"
    
    cee "核心進程恢復。穩定度 95%。"
    
    cee "（看向你）你... 幫我保住了它們。這是不理性的優化方案，但... 有效。"
    
    # 追蹤
    $ track_learned_concept("memory_pools")
    $ track_affection("cee", 20)
    $ cee_relationship = "RESONANT"
    $ set_chapter_status("C_09", "completed")
    
    jump cee_09_end

label cee_09_suggest_wipe:
    player "清了吧，資料以後還能再存。活下來才重要。"
    
    cee "（沉默 2 秒）"
    
    cee "指令接收。清空非標籤區塊。"
    
    cee "（她看著手中的盒子漸漸黯淡、消散。倉庫穩定了，但她的眼神變得有些空洞）"
    
    cee "穩定度 100%。資料完整性... 遺失。"
    
    # 追蹤
    $ track_choice("logic", is_optimal=False)
    $ track_affection("cee", -10)
    $ set_chapter_status("C_09", "completed")
    
    jump cee_09_end

label cee_09_suggest_personal_cache:
    player "把那些資料放進你的核心暫存區吧。我陪你一起分擔。"
    
    cee "（愣住）那是高度保護區。如果溢位，我的意識會受損。"
    
    cee "（看著你堅定的眼神）好。共享緩存。載入中..."
    
    # 追蹤
    $ track_choice("emotion", is_optimal=True)
    $ track_affection("cee", 25)
    $ cee_relationship = "PARTNER"
    $ set_chapter_status("C_09", "completed")
    
    jump cee_09_end

label cee_09_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：在 C 語言中，當內存管理變得極其複雜時，『記憶體池』（Memory Pool）是一種高級優化手段。它能有效減少碎片化，並在極限環境下保護核心數據。而開發者的每一個決斷，都決定了程序的最終命運。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
