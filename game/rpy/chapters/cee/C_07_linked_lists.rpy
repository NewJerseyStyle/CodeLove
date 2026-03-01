# ============================================================================
# 源界 (Source Realm) - Cee Chapter 7: 數據之鍊 (The Chain of Data)
# ============================================================================

label cee_C07_start:
    scene bg memory_warehouse_aisle
    
    show cee normal at center
    
    cee "（正看著一排擠得滿滿的箱子，汗流浹背）"
    
    cee "任務：在索引 5 的位置插入新資料。"
    
    cee "（開始把索引 5 之後的每一個箱子，一個一個往右邊挪動一個位址）"
    
    cee "搬移中... 位址 0x7005 移到 0x7006... 位址 0x7006 移到 0x7007..."
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "天哪！Cee，你這樣搬，如果這排箱子有一萬個，你得搬到明年去吧？"
    
    rusty "陣列（Array）雖然讀取快，但在中間插隊簡直是地獄！"
    
    cee "（停下動作，喘氣）記憶體必須連續。不挪動就沒空間。"
    
    narrator "你需要幫 Cee 建立一套不需要連續記憶體的動態結構：連結串列 (Linked List)。"

    menu:
        "建議使用『寻寶圖』的方式連接箱子 (Linked List)":
            jump cee_07_suggest_linked_list

        "建議她把剩下的箱子全扔了，重新買一批":
            jump cee_07_suggest_destructive

        "問她為什麼不一開始就留點空格？":
            jump cee_07_ask_why_no_gaps

label cee_07_ask_why_no_gaps:
    player "為什麼不一開始就每五個箱子空出一個位置？"
    
    cee "（搖頭）浪費空間。記憶體碎片化（Fragmentation）。我追求的是高密度存儲。"
    
    jump cee_07_suggest_alternative

label cee_07_suggest_linked_list:
    player "Cee，我們別管記憶體連不連續了。我們在每個箱子裡放一張『紙條』(Pointer)。"
    
    player "紙條上寫著下一個箱子在哪裡。這樣你只要把上一個箱子的紙條改成新箱子的位址，再讓新箱子指向原本的下一個，插入就完成了！"
    
    cee "（眼睛一亮）"
    
    cee "動態分配。鏈式存取。`struct Node { int data; struct Node *next; };`"
    
    cee "（她迅速調整了幾個箱子內部的指針，不再需要搬動任何重物）"
    
    cee "插入完成。時間複雜度從 O(n) 降到 O(1)。"
    
    cee "有效率。雖然讀取時需要逐一沿著鏈條找，但修改非常快。"
    
    rusty "哇，這招太聰明了！雖然找東西變慢了一點點，但搬家的痛苦消失了！"
    
    # 追蹤
    $ track_learned_concept("linked_lists")
    $ track_affection("cee", 15)
    $ cee_relationship = "RESONANT"
    $ set_chapter_status("C_07", "completed")
    
    jump cee_07_end

label cee_07_suggest_destructive:
    player "就把剩下的箱子全扔了吧，反正也沒人看。"
    
    cee "（嚴肅地）資料遺失不可接受。我是管理員，不是破壞者。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("C_07", "skipped")
    
    jump cee_07_end

label cee_07_suggest_alternative:
    menu:
        "使用連結串列 (Linked List)":
            jump cee_07_suggest_linked_list
        "繼續觀察":
            jump cee_07_end

label cee_07_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：連結串列（Linked List）是一種動態資料結構，它透過指針將非連續的記憶體區塊連接起來。相比陣列，連結串列在插入和刪除操作上具有極高的效率，但隨機訪問則較慢。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
