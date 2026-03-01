# ============================================================================
# 源界 (Source Realm) - Cee Chapter 2: 記憶碎片 (Memory Fragments)
# ============================================================================

label cee_C02_start:
    scene bg memory_warehouse_clutter
    
    show cee normal at center
    
    cee "（站在一堆亂七八糟的空箱子中間，看起來有些困惑）"
    
    cee "位址 0x2000 到 0x2FFF。標記為：已使用。"
    
    cee "但內容物已清空。系統回報：空間不足。"
    
    # Rusty 出現
    show rusty normal at right
    with MoveTransition(0.5)
    
    rusty "唉呀，Cee，你又忘記『釋放』空間了！"
    
    rusty "這些箱子明明已經沒用了，但你沒有清理掉，位置當然沒辦法用啊。"
    
    cee "（無視位置上原本有的舊箱子，試圖把一個新貨件塞進去，結果撞到了舊箱子）"
    
    cee "錯誤。存取衝突。Segmentation Fault。"
    
    narrator "Cee 陷入了短暫的凍結狀態。"
    
    pause 2.0
    
    rusty "看吧！如果不手動清理，倉庫很快就會被這些『幽靈資料』塞滿的。"
    
    rusty "在 Cee 的世界裡，沒有人會幫你自動打掃。借了東西就要還，佔了位置就要清。"
    
    menu:
        "建議一套清理機制：佔用與歸還(malloc/free)":
            jump cee_02_suggest_manual_cleanup

        "問她為什麼不叫人來幫忙打掃？":
            jump cee_02_ask_why_no_gc

        "讓她自己想辦法重啟":
            jump cee_02_let_it_be

label cee_02_ask_why_no_gc:
    player "為什麼不找個專門打掃的人（GC）定期清理呢？"
    
    rusty "（苦笑）那得要像 Jawa 那樣的高級辦公室才請得起『清潔工』。"
    
    rusty "Cee 追求的是極致的速度，她覺得清潔工太慢了，會打斷她的節奏。"
    
    cee "（重啟完成）清潔工會掃描所有位址。浪費週期。我自己來。"
    
    jump cee_02_suggest_alternative

label cee_02_suggest_manual_cleanup:
    player "Cee，我們用這招：每次你要用新空間時，先寫一張『借用證』(malloc)。"
    
    player "等東西搬走了，你一定要親手撕掉這張證件，把位址還給倉庫 (free)。"
    
    cee "（思考 2 秒）"
    
    cee "手動請求。手動歸還。"
    
    cee "（開始快速清理標有『已過期』的箱子）"
    
    cee "free(0x2000);"
    cee "free(0x2100);"
    
    pause 0.5
    
    cee "（空間瞬間變得整齊了）"
    
    cee "現在... malloc(1024); "
    
    cee "（順利地將新貨件放進了乾淨的位置）"
    
    cee "有效率。權限掌握在自己手裡。"
    
    rusty "太棒了！這樣就不會再有『記憶體洩漏』的問題了。"
    
    # 追蹤
    $ track_learned_concept("manual_memory_management")
    $ track_affection("cee", 10)
    $ track_affection("rusty", 5)
    $ cee_relationship = "RELIABLE"
    $ set_chapter_status("C_02", "completed")
    
    # 如果之前有記憶體洩漏後果，清除它（玩家修復了問題）
    python hide:
        for consequence in store.active_consequences:
            if consequence['type'] == 'memory_leak':
                clear_consequence(consequence['id'])
                narrator "（Cee 的工作空間變得乾淨了）"
    
    jump cee_02_end

label cee_02_let_it_be:
    narrator "你決定不干涉。Cee 在幾分鐘後自行重啟。"
    
    cee "（把舊箱子強行推到角落）暫時忽略。優先處理新貨件。"
    
    rusty "（小聲）這樣下去，倉庫遲早會炸掉的..."
    
    # 觸發記憶體洩漏後果 - 中等級別，影響 Cee 的工作空間
    $ apply_consequence("memory_leak", "moderate", "Cee 忘記釋放舊記憶體")
    call show_consequence_notification("memory_leak", "moderate")
    
    # 顯示教學卡片
    $ current_consequence_type = "memory_leak"
    call show_consequence_teaching
    
    # 顯示 Rusty 的反應
    $ current_reaction_character = "rusty"
    $ current_reaction_consequence = "memory_leak"
    call show_consequence_reaction
    
    # 更新 Cee 的可用時間（中等後果影響）
    $ cee_available_time_reduction = 30
    
    # 追蹤
    $ track_choice("observation", is_optimal=False)
    $ track_consequence("moderate")
    $ set_chapter_status("C_02", "skipped")
    
    jump cee_02_end

label cee_02_suggest_alternative:
    menu:
        "建議使用手動清理 (malloc/free)":
            jump cee_02_suggest_manual_cleanup
        "繼續觀察":
            jump cee_02_let_it_be

label cee_02_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：在 C 語言中，記憶體必須手動分配與釋放。忘記釋放會導致『記憶體洩漏』，而錯誤的存取會導致『段錯誤』(Segmentation Fault)。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
