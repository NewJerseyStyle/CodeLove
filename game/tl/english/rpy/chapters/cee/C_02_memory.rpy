# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/cee/C_02_memory.rpy:10
translate english cee_C02_start_424edf4f:

    # cee "（站在一堆亂七八糟的空箱子中間，看起來有些困惑）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:12
translate english cee_C02_start_7e4aa7c0:

    # cee "位址 0x2000 到 0x2FFF。標記為：已使用。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:14
translate english cee_C02_start_1fe383d4:

    # cee "但內容物已清空。系統回報：空間不足。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:20
translate english cee_C02_start_ddbfe09e:

    # rusty "唉呀，Cee，你又忘記『釋放』空間了！"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:22
translate english cee_C02_start_d37c8227:

    # rusty "這些箱子明明已經沒用了，但你沒有清理掉，位置當然沒辦法用啊。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:24
translate english cee_C02_start_71ef9eb2:

    # cee "（無視位置上原本有的舊箱子，試圖把一個新貨件塞進去，結果撞到了舊箱子）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:26
translate english cee_C02_start_53b16a1e:

    # cee "錯誤。存取衝突。Segmentation Fault。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:28
translate english cee_C02_start_139e59da:

    # narrator "Cee 陷入了短暫的凍結狀態。"
    narrator ""

# game/rpy/chapters/cee/C_02_memory.rpy:32
translate english cee_C02_start_9ca01d4f:

    # rusty "看吧！如果不手動清理，倉庫很快就會被這些『幽靈資料』塞滿的。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:34
translate english cee_C02_start_63d86672:

    # rusty "在 Cee 的世界裡，沒有人會幫你自動打掃。借了東西就要還，佔了位置就要清。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:47
translate english cee_02_ask_why_no_gc_c5878be2:

    # player "為什麼不找個專門打掃的人（GC）定期清理呢？"
    player ""

# game/rpy/chapters/cee/C_02_memory.rpy:49
translate english cee_02_ask_why_no_gc_d64ba6a7:

    # rusty "（苦笑）那得要像 Jawa 那樣的高級辦公室才請得起『清潔工』。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:51
translate english cee_02_ask_why_no_gc_86d20a74:

    # rusty "Cee 追求的是極致的速度，她覺得清潔工太慢了，會打斷她的節奏。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:53
translate english cee_02_ask_why_no_gc_7877fc69:

    # cee "（重啟完成）清潔工會掃描所有位址。浪費週期。我自己來。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:58
translate english cee_02_suggest_manual_cleanup_4753bdce:

    # player "Cee，我們用這招：每次你要用新空間時，先寫一張『借用證』(malloc)。"
    player ""

# game/rpy/chapters/cee/C_02_memory.rpy:60
translate english cee_02_suggest_manual_cleanup_8aa13113:

    # player "等東西搬走了，你一定要親手撕掉這張證件，把位址還給倉庫 (free)。"
    player ""

# game/rpy/chapters/cee/C_02_memory.rpy:62
translate english cee_02_suggest_manual_cleanup_ec787cae:

    # cee "（思考 2 秒）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:64
translate english cee_02_suggest_manual_cleanup_50381b15:

    # cee "手動請求。手動歸還。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:66
translate english cee_02_suggest_manual_cleanup_7749d64d:

    # cee "（開始快速清理標有『已過期』的箱子）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:68
translate english cee_02_suggest_manual_cleanup_d969e085:

    # cee "free(0x2000);"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:69
translate english cee_02_suggest_manual_cleanup_d73681f8:

    # cee "free(0x2100);"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:73
translate english cee_02_suggest_manual_cleanup_14221675:

    # cee "（空間瞬間變得整齊了）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:75
translate english cee_02_suggest_manual_cleanup_f7554e74:

    # cee "現在... malloc(1024); "
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:77
translate english cee_02_suggest_manual_cleanup_434f64c2:

    # cee "（順利地將新貨件放進了乾淨的位置）"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:79
translate english cee_02_suggest_manual_cleanup_b2e9fff8:

    # cee "有效率。權限掌握在自己手裡。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:81
translate english cee_02_suggest_manual_cleanup_60f23df9:

    # rusty "太棒了！這樣就不會再有『記憶體洩漏』的問題了。"
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:100
translate english cee_02_let_it_be_72ed0000:

    # narrator "你決定不干涉。Cee 在幾分鐘後自行重啟。"
    narrator ""

# game/rpy/chapters/cee/C_02_memory.rpy:102
translate english cee_02_let_it_be_6031b47d:

    # cee "（把舊箱子強行推到角落）暫時忽略。優先處理新貨件。"
    cee ""

# game/rpy/chapters/cee/C_02_memory.rpy:104
translate english cee_02_let_it_be_5d8f9f1d:

    # rusty "（小聲）這樣下去，倉庫遲早會炸掉的..."
    rusty ""

# game/rpy/chapters/cee/C_02_memory.rpy:140
translate english cee_02_end_b592bb87:

    # teaching "你學會了：在 C 語言中，記憶體必須手動分配與釋放。忘記釋放會導致『記憶體洩漏』，而錯誤的存取會導致『段錯誤』(Segmentation Fault)。"
    teaching ""

translate english strings:

    # game/rpy/chapters/cee/C_02_memory.rpy:37
    old "建議一套清理機制：佔用與歸還(malloc/free)"
    new ""

    # game/rpy/chapters/cee/C_02_memory.rpy:40
    old "問她為什麼不叫人來幫忙打掃？"
    new ""

    # game/rpy/chapters/cee/C_02_memory.rpy:43
    old "讓她自己想辦法重啟"
    new ""

    # game/rpy/chapters/cee/C_02_memory.rpy:131
    old "建議使用手動清理 (malloc/free)"
    new ""

