# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 8: 遠程協定 (The Remote Protocol)
# ============================================================================

label jawa_J08_start:
    scene bg contract_office
    
    scene black with fade
    show jawa normal at left
    show rusty normal at center
    
    jawa "（正對著遠方一片漆黑的虛空呼喊，試圖傳遞一份重要的備忘錄）"
    
    jawa "接收方：源界東區。資料包 001：內容為『系統升級』。請確認！"
    
    narrator "虛空中傳來一陣雜亂的電流聲，沒有任何回應。"
    
    jawa "（眉頭緊鎖）通訊丟失。重試次數：5。網路延遲過高，或資料在傳輸中損毀。"
    
    # Rusty 出現
    show rusty normal at center
    
    rusty "Jawa 姐，對面太遠了，而且中間有很多噪聲（Noise）！你這樣乾喊，他們根本聽不清呀！"
    
    jawa "（推眼鏡）遠程調用（Remote Call）的基礎不牢。我需要一套標準的握手協議。"
    
    narrator "你需要幫 Jawa 建立一套穩健的遠程通訊機制：協定 (Protocol) 與 校驗 (Checksum)。"

    menu:
        "建議建立『三向握手』 (Handshake) 確保連線":
            jump jawa_08_suggest_handshake

        "建議 Jawa 換個更大的喇叭喊":
            jump jawa_08_suggest_volume

        "問她為什麼不叫 Golly 跑腿去送？":
            jump jawa_08_ask_golly

label jawa_08_ask_golly:
    player "讓 Golly 跑一趟不就得了？他跑得那麼快。"
    
    jawa "（搖頭）實體移動太慢。我們需要的是光速的資料交換。這是分佈式系統（Distributed Systems）的基礎。"
    
    jump jawa_08_suggest_alternative

label jawa_08_suggest_handshake:
    player "Jawa，我們定個規矩。先問對面『在嗎？』，等對面回『在，你呢？』，你再回『我也在，開始發資料吧！』"
    
    player "這就是『三向握手』。然後每一份資料後面都加個『檢查碼』，讓對面算一算對不對，不對就重發！"
    
    jawa "（點頭，接著一動不動）……"
    
    pause 2.0
    
    jawa "（若無其事地繼續）...TCP 思想。傳輸控制協定。"
    
    jawa "（在終端機上敲下指令，幾道藍色的電波穩定地射向虛空）"
    
    jawa "連線建立。資料包傳輸中... 校驗正確。ACK（確認字元）已收到。"
    
    rusty "哇！雖然速度慢了一點點，但每一行資料都清清楚楚地送到了！這就是網路的奧秘嗎？"
    
    jawa "（露出自信的神情）只要協議正確，距離就不再是阻礙。"
    
    # 追蹤
    $ track_learned_concept("networking")
    $ track_affection("jawa", 10)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_08", "completed")
    
    jump jawa_08_end

label jawa_08_suggest_volume:
    player "再大聲點！他們肯定能聽到的！"
    
    jawa "（喊到嗓子沙啞）無效。物理限制無法透過蠻力突破。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_08", "skipped")
    
    jump jawa_08_end

label jawa_08_suggest_alternative:
    menu:
        "建立標準通訊協定 (Protocol)":
            jump jawa_08_suggest_handshake
        "繼續觀察":
            jump jawa_08_end

label jawa_08_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：在 Java（以及所有現代語言）中，網路通訊是核心能力之一。透過建立標準的通訊協定（如 TCP/IP）與錯誤檢查機制，分佈在不同位置的系統可以像在同一台機器上一樣協同工作。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
