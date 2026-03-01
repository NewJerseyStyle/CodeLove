# ============================================================================
# 源界 (Source Realm) - 共同事件 (Shared Events)
# ============================================================================

label shared_race_condition:
    scene bg information_square_glitch
    
    show cee normal at left
    show jawa normal at right
    
    narrator "資訊廣場中央的一個資源箱正在劇烈閃爍。"
    
    cee "（準備衝過去）我的。位址 0x5000。"
    
    jawa "（同時伸手）等一下。這份資料已經在我的排程清單裡了。"
    
    # 兩人同時伸手碰觸箱子，箱子發出刺耳的警報聲
    play sound "audio/glitch_alarm.ogg"
    
    narrator "兩人同時存取同一個資源，導致了嚴重的『競態條件』(Race Condition)。"
    
    jawa "（皺眉）Cee，你太快了。這會破壞資料的一致性。"
    
    cee "速度就是一切。慢了就沒意義。"
    
    rusty "（在旁邊著急）大家冷靜點！這樣下去資源會鎖死(Deadlock)的！"
    
    menu:
        "支持 Jawa 的『互斥鎖』(Mutex) 方案":
            jump shared_race_support_jawa
            
        "支持 Cee 的『原子操作』(Atomic) 方案":
            jump shared_race_support_cee
            
        "自己嘗試手動協調":
            jump shared_race_manual

label shared_race_support_jawa:
    player "Jawa 說得對。我們需要一個『鎖』。誰先拿到鑰匙，誰就先用，另一個人排隊。"
    
    jawa "（點頭）這就是 synchronized 的重要性。確保同步。"
    
    cee "（雖然不情願，但還是停手了）排隊。真慢。"
    
    narrator "資料最終安全地被 Jawa 處理了。"
    
    $ track_affection("jawa", 10)
    $ track_affection("cee", -5)
    jump shared_race_end

label shared_race_support_cee:
    player "沒時間排隊了！用 Cee 的方法，這是一個單次操作，直接交換資料，不給衝突留機會！"
    
    cee "（瞬間完成操作）完成。無鎖化。"
    
    jawa "（推眼鏡）太危險了。雖然這次成功了，但如果資料量大..."
    
    narrator "資料被 Cee 瞬間奪走並處理。"
    
    $ track_affection("cee", 15)
    $ track_affection("jawa", -5)
    jump shared_race_end

label shared_race_manual:
    narrator "你試圖擋在兩人中間，結果被兩人同時推開。"
    
    player "哎喲！"
    
    rusty "（嘆氣）看來在源界，邏輯比肉體碰撞更管用..."
    
    $ track_choice("observation", is_optimal=False)
    jump shared_race_end

label shared_race_end:
    narrator "衝突暫時平息。但兩位管理員的理念差異似乎更明顯了。"

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu

# 其他共同事件暫代...
label shared_language_debate:
    scene bg information_square_forum
    
    show cee normal at left
    show jawa normal at center_left
    show py normal at right
    show golly normal at center_right
    
    narrator "資訊廣場正在舉行一場激烈的辯論，主題是『誰才是未來的核心』。"
    
    cee "（冷冷地）編譯型。預先處理。極致的速度。底層的控制權。這是不可替代的。"
    
    py "（打了個哈欠）哎呀，Cee，現在硬體這麼強，慢那幾毫秒誰在乎啊？開發效率才是王道！我寫一行，你們得寫十行。"
    
    jawa "（嚴肅地）效率必須建立在規範之上。我的中介碼（Bytecode）兼顧了平台無關性與性能。這才是工業級的平衡。"
    
    golly "（笑著插話）大家別爭了。我的並行原生支援和快速編譯，才是為了雲端時代而生的。簡潔且強大，不是嗎？"
    
    narrator "四位管理員看向你，似乎想聽聽你的看法。"
    
    menu:
        "支持 Cee：效率與速度是系統的基石":
            $ track_affection("cee", 10)
            player "我認為在資源受限的環境下，Cee 的精確控制是必不可少的。"
            
        "支持 Py：開發者的時間比機器的時間更寶貴":
            $ track_affection("py", 10)
            player "人類的創造力不應該浪費在分號和記憶體管理上，Py 的簡潔才是未來。"
            
        "支持 Jawa：嚴謹的架構才能承載大型文明":
            $ track_affection("jawa", 10)
            player "當系統變得巨大時，只有 Jawa 的規範能保證它不會自我崩潰。"
            
        "支持 Golly：並行與現代化是唯一的出路":
            $ track_affection("golly", 10)
            player "面對海量的資料流，Golly 的並行思維才是解決之道。"

    narrator "辯論在一片討論聲中結束。你發現，每種語言的存在都有其獨特的價值。"
    jump time_choice_menu

label shared_ending_evaluation:
    scene bg source_realm_core
    with Dissolve(2.0)
    
    narrator "你站在源界的核心，周圍閃爍著你旅途中做出的所有決定的數據碎片。"

    python hide:
        # 計算玩家的表現 - 直接存儲到 store 使全局可訪問
        if hasattr(persistent, "player_stats") and persistent.player_stats:
            total_concepts = len(persistent.player_stats.get("concepts_learned", []))
        else:
            total_concepts = 0
        store.total_concepts = total_concepts

    narrator "你一共掌握了 [total_concepts] 個核心編程概念。"

    if store.cee_relationship in ["RESONANT", "PARTNER"] and store.jawa_relationship in ["SYNCHRONIZED", "PARTNER"]:
        narrator "你展現了驚人的平衡感，在底層與高層之間遊刃有餘。"
        jump trigger_ending
    elif store.cee_relationship in ["RESONANT", "PARTNER"]:
        narrator "你深入了世界的根基，成為了底層邏輯的掌控者。"
        jump trigger_ending
    elif store.jawa_relationship in ["SYNCHRONIZED", "PARTNER"]:
        narrator "你建構了宏大的秩序，成為了架構設計的大師。"
        jump trigger_ending
    else:
        narrator "你在源界的數據結構中顯得如此不穩定..."
        narrator "你既沒有深入底層的根基，也沒有融入宏大的秩序。"
        
        # 觸發管理員撈取
        jump ending_source_rescue
        
    pause 2.0

    jump end_time_period

label shared_bad_end_a_check:
    # 這是最後一個時段的觸發，如果還沒達成結局，強制進入結算
    $ current_ending = check_ending_conditions()
    if current_ending == "none":
        # 如果時間到了還沒達成任何結局，就是管理員救出結局
        jump ending_source_rescue
    else:
        jump trigger_ending
