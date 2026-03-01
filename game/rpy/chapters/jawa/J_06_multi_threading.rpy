# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 6: 分身術 (Cloning the Process)
# ============================================================================

label jawa_J06_start:
    scene bg contract_office
    
    show jawa normal at left
    show rusty normal at center
    show golly normal at right
    
    jawa "（手速極快地處理著文件，但桌上的文件堆得比人還高）"
    
    jawa "隊列積壓嚴重。目前已處理 150/10000 份合約。"
    
    golly "（懶洋洋地靠在門邊）哎呀，Jawa 姐，你還在一個一個地處理啊？"
    
    golly "要是我，早就開一千個分身同時開工了。看！"
    
    # Golly 瞬間模糊，像是出現了幾個殘影，同時處理了幾份文件
    golly "（殘影重合）一秒鐘，搞定。"
    
    jawa "（推眼鏡）Golly。你的並行處理雖然快，但極度不安全。萬一兩個人同時改同一份資料怎麼辦？"
    
    jawa "會出現競態條件（Race Condition）。那是資料的毀滅。"
    
    narrator "Jawa 想要提升速度，但又對多個分身（執行緒）同時存取資源感到擔憂。你需要幫她建立一套『安全的多執行緒』機制。"

    menu:
        "建議開啟『執行緒助手』 (Threads) 並配備『互斥鎖』 (Synchronized)":
            jump jawa_06_suggest_threads

        "建議 Jawa 直接加速，跑得比 Golly 還快":
            jump jawa_06_suggest_overclock

        "問她為什麼不把合約都交給 Golly 處理？":
            jump jawa_06_ask_golly

label jawa_06_ask_golly:
    player "既然 Golly 那麼快，就把合約都給他吧。"
    
    jawa "（嚴肅地）不行。Golly 的並行太隨性了。契約局需要的是精確的同步和狀態管理。"
    
    jawa "這不是單純的速度問題，是可靠性的問題。"
    
    jump jawa_06_suggest_alternative

label jawa_06_suggest_threads:
    player "Jawa，我們開啟『多執行緒』吧。讓多個助手同時批改合約。"
    
    player "為了防止他們打架，我們規定：每當要動同一個資料櫃時，助手必須先拿到『互斥鎖』 (Synchronized)。"
    
    player "拿到鎖的人才能動，其他人排隊。這樣既能變快，資料也是安全的！"
    
    jawa "（眼睛一亮）"
    
    jawa "互斥訪問。執行緒安全。`synchronized(this)`。"
    
    jawa "（在終端機上敲下指令，幾道紫色的光芒從她身上分離出來，化作幾個同樣神情的助手）"
    
    jawa "（助手們開始有條不紊地處理文件，每當碰到共用的帳本，都會先進行『加鎖』動作）"
    
    pause 1.0
    
    jawa "處理進度：1500/10000。吞吐量提升了 10 倍。"
    
    golly "（挑眉）喔？雖然還是比我保守，但這套同步機制確實挺穩的嘛。"
    
    jawa "（平靜地）安全才是契約的根本。"
    
    # 追蹤
    $ track_learned_concept("multi_threading")
    $ track_affection("jawa", 10)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_06", "completed")
    
    jump jawa_06_end

label jawa_06_suggest_overclock:
    player "Jawa，跑快點！別輸給 Golly！"
    
    jawa "（汗水滴落）單核頻率已達極限。這不是體力能解決的問題，是架構問題。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_06", "skipped")
    
    jump jawa_06_end

label jawa_06_suggest_alternative:
    menu:
        "使用多執行緒 (Threads) 與同步 (Synchronized)":
            jump jawa_06_suggest_threads
        "繼續觀察":
            jump jawa_06_end

label jawa_06_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 支援原生多執行緒（Multi-threading）。透過將任務分配給不同的執行緒並使用 `synchronized` 關鍵字來保護共享資源，可以讓程式在多核心處理器上發揮巨大的效能，同時保證資料的一致性。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
