# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/cee/C_03_arrays.rpy:8
translate english cee_C03_start_00f49fbe:

    # cee "（看著雜亂的工作區）之前的記憶體洩漏還在清理中..."
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:9
translate english cee_C03_start_25620777:

    # cee "這個字串列車先放一邊。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:11
translate english cee_C03_start_33dd586d:

    # narrator "Cee 忙於處理之前的後果，無法專心處理新的任務。"
    narrator ""

# game/rpy/chapters/cee/C_03_arrays.rpy:21
translate english cee_C03_start_b751f10b:

    # rusty "（看著亂七八糟的工作區）我的資料還沒恢復..."
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:22
translate english cee_C03_start_667b6331:

    # rusty "如果你再搞出緩衝區溢出，我真的會生氣的。"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:28
translate english cee_C03_start_8862f3c1:

    # cee "（站在一排連在一起的小型貨車廂前）"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:30
translate english cee_C03_start_f162ce9e:

    # cee "陣列傳輸模式。連續位址。0x3000 到 0x3010。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:32
translate english cee_C03_start_3080da86:

    # cee "（指著第一節車廂）索引 0。內容：'H'。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:34
translate english cee_C03_start_226b690e:

    # cee "（指著第二節車廂）索引 1。內容：'E'。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:39
translate english cee_C03_start_cebc1a3c:

    # rusty "唉，Cee！這列『字串火車』又失控了！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:44
translate english cee_C03_start_eb01241b:

    # rusty "（抱頭）你看！因為你沒在最後一節車廂掛上『終止符號』，火車頭以為後面還有車，結果撞到了別人的資料區！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:46
translate english cee_C03_start_90f3caee:

    # cee "（面無表情）連續存取。直到讀取到空值。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:48
translate english cee_C03_start_3984a01a:

    # cee "如果中間沒有空值，就會一直往後讀。直到...崩潰。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:50
translate english cee_C03_start_e6b41d64:

    # narrator "你需要幫 Cee 解決兩個問題：字串的終止 (Null Terminator) 以及 存取越界 (Buffer Overflow)。"
    narrator ""

# game/rpy/chapters/cee/C_03_arrays.rpy:66
translate english cee_03_ask_why_no_length_a81e2f28:

    # player "為什麼不一開始就給火車掛個『長度牌』？比如：長度 5。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:68
translate english cee_03_ask_why_no_length_e54733d7:

    # cee "（看著你）那需要額外的空間存儲『長度』。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:70
translate english cee_03_ask_why_no_length_49f8062e:

    # cee "C 語言選擇用一個隱藏的 0 來標記結尾。節省空間。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:72
translate english cee_03_ask_why_no_length_051f14d1:

    # rusty "（小聲）雖然省了空間，但如果忘了那個 0，後果真的很可怕..."
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:77
translate english cee_03_suggest_terminator_6479d600:

    # player "Cee，我們在最後一個字元後面，手動加一個數值為 0 的空箱子 (\\0)。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:79
translate english cee_03_suggest_terminator_36f1b753:

    # player "這樣讀取的人一看到這個箱子，就知道這列火車結束了。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:81
translate english cee_03_suggest_terminator_0b3f9043:

    # cee "（思索）手動結尾。傳統做法。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:83
translate english cee_03_suggest_terminator_e34902f1:

    # cee "（迅速在最後掛上標記）"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:85
translate english cee_03_suggest_terminator_d37f12ec:

    # cee "存取中... 'H', 'E', 'L', 'L', 'O', '\\0'。停止。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:87
translate english cee_03_suggest_terminator_0e11149e:

    # cee "（點頭）有效率。讀取到此為止。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:96
translate english cee_03_suggest_terminator_1a2b6f49:

    # cee "（看著你）雖然字串問題解決了，但之前的記憶體問題還在。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:101
translate english cee_03_suggest_bounds_check_4ea33c6e:

    # player "Cee，這火車只有 5 節車廂，你別把 10 個字強塞進去啊！"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:103
translate english cee_03_suggest_bounds_check_881e9b2d:

    # player "塞不下的字會溢位到別人的地盤，那叫『緩衝區溢位』。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:105
translate english cee_03_suggest_bounds_check_c95852f0:

    # cee "（看著太長的資料）截斷處理。只取前 5 位。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:107
translate english cee_03_suggest_bounds_check_ec780f52:

    # cee "（強制切掉多餘字元）安全性提升。雖然損失了部分資料。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:119
translate english cee_03_risky_write_11965e95:

    # player "Cee，不管邊界，直接強制寫入。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:121
translate english cee_03_risky_write_c59830c3:

    # cee "（執行）強制寫入模式。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:122
translate english cee_03_risky_write_522ab3c2:

    # cee "忽略邊界檢查。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:124
translate english cee_03_risky_write_86ff2b81:

    # cee "（寫入中...）"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:129
translate english cee_03_risky_write_cc2cab3e:

    # cee "（突然僵住）錯誤。緩衝區溢位。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:130
translate english cee_03_risky_write_28d9eb83:

    # cee "（眼神空白）寫入越界。覆蓋了鄰近區域。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:135
translate english cee_03_risky_write_18e159bd:

    # rusty "（尖叫）我的資料！！又！！被！！覆蓋！！了！！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:136
translate english cee_03_risky_write_5e39d87f:

    # rusty "（氣沖沖地走開）這次我再也不幫你們了！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:145
translate english cee_03_risky_write_69c0ef88:

    # rusty "我的資料！全被覆蓋了！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:146
translate english cee_03_risky_write_ea14ec80:

    # rusty "（氣沖沖地過來）這需要幾小時才能恢復！"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:165
translate english cee_03_risky_write_fefe0e87:

    # cee "（恢復）重啟完成。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:166
translate english cee_03_risky_write_1a4068e6:

    # cee "寫入失敗。鄰近區域已損毀。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:182
translate english cee_03_help_cleanup_14eb62a7:

    # cee "（看著你來幫忙）"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:183
translate english cee_03_help_cleanup_63449ce0:

    # cee "清理記憶體洩漏。需要釋放未歸還的空間。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:185
translate english cee_03_help_cleanup_5a1b859a:

    # player "我們一起來。每個箱子都確認一下是否還需要。"
    player ""

# game/rpy/chapters/cee/C_03_arrays.rpy:187
translate english cee_03_help_cleanup_e0abc75b:

    # cee "（快速檢查）0x2000 - 已過期。釋放。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:188
translate english cee_03_help_cleanup_7dadeda2:

    # cee "0x2100 - 已過期。釋放。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:189
translate english cee_03_help_cleanup_135363e8:

    # cee "0x2200 - 已過期。釋放。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:193
translate english cee_03_help_cleanup_029ee5fd:

    # cee "（空間變得乾淨了）清理完成。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:202
translate english cee_03_help_cleanup_5ca20b7f:

    # rusty "（走過來）謝謝你幫忙清理。"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:203
translate english cee_03_help_cleanup_0c91010e:

    # rusty "如果不處理，這些『幽靈資料』會一直佔用空間。"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:213
translate english cee_03_help_cleanup_3c14855c:

    # narrator "Cee 的工作空間恢復了，但你們的時間花在清理上了。"
    narrator ""

# game/rpy/chapters/cee/C_03_arrays.rpy:220
translate english cee_03_force_continue_db44a87f:

    # cee "（手忙腳亂地處理）索引 0... 索引 1..."
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:222
translate english cee_03_force_continue_05cc95eb:

    # narrator "Cee 因為分心處理之前的問題，效率大幅下降。"
    narrator ""

# game/rpy/chapters/cee/C_03_arrays.rpy:250
translate english cee_03_continue_with_consequence_095fcaca:

    # cee "（勉強開始處理字串列車）"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:252
translate english cee_03_continue_with_consequence_67c5d43c:

    # cee "（心不在焉地）陣列傳輸模式。連續位址。0x3000 到 0x3010。"
    cee ""

# game/rpy/chapters/cee/C_03_arrays.rpy:254
translate english cee_03_continue_with_consequence_5b84fe1e:

    # rusty "Cee，你確定你能專心嗎？後面還有沒處理完的問題呢。"
    rusty ""

# game/rpy/chapters/cee/C_03_arrays.rpy:256
translate english cee_03_continue_with_consequence_0eebff74:

    # narrator "Cee 還在忙著處理之前的後果，無法專心處理這個新任務。"
    narrator ""

# game/rpy/chapters/cee/C_03_arrays.rpy:268
translate english cee_03_end_e70a9caf:

    # teaching "你學會了：C 語言的字串是以 '\\0' 結尾的字元陣列。存取陣列時如果不注意邊界，會發生『緩衝區溢位』，這是一個嚴重的安全漏洞。"
    teaching ""

translate english strings:

    # game/rpy/chapters/cee/C_03_arrays.rpy:14
    old "幫忙清理之前的記憶體洩漏"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:16
    old "繼續進行字串列車任務"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:53
    old "建議在末尾加上『終止符』 (\\0)"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:56
    old "建議縮減字串長度，不要超過車廂數量"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:59
    old "問她為什麼不一開始就規定好長度？"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:62
    old "不管它，繼續寫入"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:225
    old "加上終止符 (\\0)"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:227
    old "建議邊界檢查"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:259
    old "幫忙清理之前的問題"
    new ""

    # game/rpy/chapters/cee/C_03_arrays.rpy:261
    old "硬著頭皮繼續"
    new ""

