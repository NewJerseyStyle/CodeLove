# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 2: 藍圖與實體 (Blueprints and Instances)
# ============================================================================

label jawa_J02_start:
    scene bg contract_office_workshop
    
    show jawa normal at left
    show rusty normal at right
    
    rusty "（正滿頭大汗地用零件組裝一個複雜的掃描器）"
    
    rusty "呼...呼...第十個了...每次都要從螺絲開始轉，好累啊。"
    
    jawa "（手持一本厚厚的規格書，平靜地看著她）"
    
    jawa "Rusty。這是不合時宜的。你應該先定義一個『範本』。"
    
    rusty "範本？但我需要的是會動的工具，不是圖紙啊！"
    
    jawa "（轉向你）你。空白指標。"
    
    jawa "你看，她正在逐一製造每個東西（Procedural）。"
    
    jawa "在我的世界裡，我們會先創造一個『類別』(Class)，然後讓系統自動『產出』(Instantiate) 它。"

    menu:
        "建議使用『藍圖與複製品』(Class & Object) 系統":
            jump jawa_02_suggest_oop

        "問她為什麼不直接影印一個現成的工具？":
            jump jawa_02_ask_why_no_cloning

        "靜靜看著 Rusty 繼續手動組裝":
            jump jawa_02_continue_manual

label jawa_02_ask_why_no_cloning:
    player "直接影印一個工具不是更快嗎？"
    
    jawa "（推眼鏡）單純的複製是不夠的。每個工具雖然功能相同，但它們的使用狀況（狀態）是不一樣的。"
    
    jawa "複製品會共享同一個記憶體位址，但『物件』擁有獨立的屬性。"
    
    jawa "這就是『封裝』的基礎。"
    
    jump jawa_02_suggest_alternative

label jawa_02_suggest_oop:
    player "Jawa，我們來幫 Rusty 做一個『掃描器藍圖』吧。"
    
    player "藍圖規定了掃描器有什麼按鈕、什麼顏色。只要有藍圖，系統一秒鐘就能生出一百個掃描器。"
    
    jawa "（點頭，眼神讚賞）"
    
    jawa "正確。`Scanner myScanner = new Scanner();`"
    
    jawa "（在終端機上敲下幾行字，一道光芒閃過，工作台上瞬間出現了十個整齊的掃描器）"
    
    rusty "（目瞪口呆）哇！這就是...物件導向嗎？"
    
    jawa "這只是開始。現在每個掃描器都是獨立的，你可以單獨修改其中一個的電力，而不影響其他個。"
    
    rusty "太方便了！這樣我再也不用手動轉螺絲了！"
    
    # 追蹤
    $ track_learned_concept("classes_and_objects")
    $ track_affection("jawa", 10)
    $ jawa_relationship = "TRUSTED"
    $ set_chapter_status("J_02", "completed")
    
    jump jawa_02_end

label jawa_02_continue_manual:
    narrator "你決定不干涉。Rusty 繼續辛苦地組裝，Jawa 則在一旁默默記錄她的錯誤率。"
    
    jawa "（對著你搖頭）低效。且容易出錯。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_02", "skipped")
    
    jump jawa_02_end

label jawa_02_suggest_alternative:
    menu:
        "建議使用藍圖系統 (OOP)":
            jump jawa_02_suggest_oop
        "繼續觀察":
            jump jawa_02_continue_manual

label jawa_02_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 是物件導向語言。『類別』(Class) 是藍圖，而『物件』(Object) 是根據藍圖產出的實體。透過封裝，我們可以更好地管理資料的狀態。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
