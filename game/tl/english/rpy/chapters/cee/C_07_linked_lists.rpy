# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/cee/C_07_linked_lists.rpy:10
translate english cee_C07_start_5a11ec57:

    # cee "（正看著一排擠得滿滿的箱子，汗流浹背）"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:12
translate english cee_C07_start_4f367cb8:

    # cee "任務：在索引 5 的位置插入新資料。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:14
translate english cee_C07_start_9e9ab73b:

    # cee "（開始把索引 5 之後的每一個箱子，一個一個往右邊挪動一個位址）"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:16
translate english cee_C07_start_aeb4eb07:

    # cee "搬移中... 位址 0x7005 移到 0x7006... 位址 0x7006 移到 0x7007..."
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:21
translate english cee_C07_start_a7f03bcd:

    # rusty "天哪！Cee，你這樣搬，如果這排箱子有一萬個，你得搬到明年去吧？"
    rusty ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:23
translate english cee_C07_start_5792551d:

    # rusty "陣列（Array）雖然讀取快，但在中間插隊簡直是地獄！"
    rusty ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:25
translate english cee_C07_start_5dfda363:

    # cee "（停下動作，喘氣）記憶體必須連續。不挪動就沒空間。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:27
translate english cee_C07_start_e7304a23:

    # narrator "你需要幫 Cee 建立一套不需要連續記憶體的動態結構：連結串列 (Linked List)。"
    narrator ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:40
translate english cee_07_ask_why_no_gaps_f4fa16b9:

    # player "為什麼不一開始就每五個箱子空出一個位置？"
    player ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:42
translate english cee_07_ask_why_no_gaps_14d1c260:

    # cee "（搖頭）浪費空間。記憶體碎片化（Fragmentation）。我追求的是高密度存儲。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:47
translate english cee_07_suggest_linked_list_b9da7dc2:

    # player "Cee，我們別管記憶體連不連續了。我們在每個箱子裡放一張『紙條』(Pointer)。"
    player ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:49
translate english cee_07_suggest_linked_list_ab6864c2:

    # player "紙條上寫著下一個箱子在哪裡。這樣你只要把上一個箱子的紙條改成新箱子的位址，再讓新箱子指向原本的下一個，插入就完成了！"
    player ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:51
translate english cee_07_suggest_linked_list_30dcaf77:

    # cee "（眼睛一亮）"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:53
translate english cee_07_suggest_linked_list_0ac12899:

    # cee "動態分配。鏈式存取。`struct Node { int data; struct Node *next; };`"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:55
translate english cee_07_suggest_linked_list_ba295d9a:

    # cee "（她迅速調整了幾個箱子內部的指針，不再需要搬動任何重物）"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:57
translate english cee_07_suggest_linked_list_1c796d1a:

    # cee "插入完成。時間複雜度從 O(n) 降到 O(1)。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:59
translate english cee_07_suggest_linked_list_47b7e0d4:

    # cee "有效率。雖然讀取時需要逐一沿著鏈條找，但修改非常快。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:61
translate english cee_07_suggest_linked_list_6007cb28:

    # rusty "哇，這招太聰明了！雖然找東西變慢了一點點，但搬家的痛苦消失了！"
    rusty ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:72
translate english cee_07_suggest_destructive_5b5778ea:

    # player "就把剩下的箱子全扔了吧，反正也沒人看。"
    player ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:74
translate english cee_07_suggest_destructive_95057e01:

    # cee "（嚴肅地）資料遺失不可接受。我是管理員，不是破壞者。"
    cee ""

# game/rpy/chapters/cee/C_07_linked_lists.rpy:92
translate english cee_07_end_f4952f2f:

    # teaching "你學會了：連結串列（Linked List）是一種動態資料結構，它透過指針將非連續的記憶體區塊連接起來。相比陣列，連結串列在插入和刪除操作上具有極高的效率，但隨機訪問則較慢。"
    teaching ""

translate english strings:

    # game/rpy/chapters/cee/C_07_linked_lists.rpy:30
    old "建議使用『寻寶圖』的方式連接箱子 (Linked List)"
    new ""

    # game/rpy/chapters/cee/C_07_linked_lists.rpy:33
    old "建議她把剩下的箱子全扔了，重新買一批"
    new ""

    # game/rpy/chapters/cee/C_07_linked_lists.rpy:36
    old "問她為什麼不一開始就留點空格？"
    new ""

    # game/rpy/chapters/cee/C_07_linked_lists.rpy:83
    old "使用連結串列 (Linked List)"
    new ""

