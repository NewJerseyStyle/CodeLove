# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 3: 血脈與變身 (Bloodlines and Transformation)
# ============================================================================

label jawa_J03_start:
    scene bg contract_office_archive
    
    show jawa normal at left
    show rusty normal at right
    
    rusty "（正看著一堆不同形狀的儲存袋發愁）"
    
    rusty "這個是『加密袋』，那個是『壓縮袋』，還有一個是『透明袋』。"
    
    rusty "我得幫每一種袋子寫一套不同的『打開方法』，好麻煩呀！"
    
    jawa "（手拿一本層級圖，平靜地看著她）"
    
    jawa "Rusty。它們都是『袋子』(Container)。"
    
    jawa "既然它們都有共通的行為，你就不應該重複工作。"
    
    jawa "（轉向你）你。空白指標。"
    
    jawa "這就是『繼承』(Inheritance) 的力量。所有的袋子，其實都流著同一個家族的血脈。"

    menu:
        "建議定義『父類別』並讓各個袋子『繼承』 (Inheritance)":
            jump jawa_03_suggest_inheritance

        "建議使用『萬用說明書』來根據不同袋子執行不同動作 (Polymorphism)":
            jump jawa_03_suggest_polymorphism

        "問她為什麼不把所有袋子都改成同一種？":
            jump jawa_03_ask_why_no_uniformity

label jawa_03_ask_why_no_uniformity:
    player "把所有袋子都統一成一種，不就不用寫這麼多方法了嗎？"
    
    jawa "（推眼鏡）世界是多元的。有些袋子需要加密，有些需要快速存取。"
    
    jawa "統一會導致功能的平庸。我們需要的是『具備共通性的差異』。"
    
    jump jawa_03_suggest_alternative

label jawa_03_suggest_inheritance:
    player "Jawa，我們做一個『超類別：基本袋子』吧。"
    
    player "所有的袋子（加密、壓縮）都『繼承』它。基本袋子裡寫好最通用的打開方法。"
    
    player "這樣 Rusty 只要幫特定袋子寫它『特別』的地方就好了！"
    
    jawa "（點頭，眼神讚賞）"
    
    jawa "正確。`extends Container`。"
    
    jawa "（在終端機上敲下幾行字，層級圖瞬間自動補完）"
    
    rusty "哇！我只要在加密袋裡寫『解密』，其他的『拉開拉鍊』動作都自動繼承了！"
    
    jawa "這就是程式碼的重用性。減少了重複，就減少了錯誤。"
    
    # 追蹤
    $ track_learned_concept("inheritance")
    $ track_affection("jawa", 10)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_03", "completed")
    
    jump jawa_03_end

label jawa_03_suggest_polymorphism:
    player "Jawa，我們可以用『多型』(Polymorphism)。"
    
    player "雖然它們在程式裡都叫『袋子』，但系統在運行時會自動辨識它是哪種袋子，並執行對應的『開啟』動作！"
    
    jawa "（眼睛微亮）"
    
    jawa "動態繫結 (Dynamic Binding)。"
    
    jawa "不論它是什麼袋子，我們只需要呼叫 `open()`。袋子會自己決定怎麼開。"
    
    rusty "這太神奇了！我就像有一根萬能鑰匙，插進去它就會自己變形成正確的鑰匙！"
    
    jawa "很好的洞察力。這能讓系統更有彈性。"
    
    # 追蹤
    $ track_learned_concept("polymorphism")
    $ track_affection("jawa", 15)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_03", "completed")
    
    jump jawa_03_end

label jawa_03_suggest_alternative:
    menu:
        "使用繼承與多型 (OOP)":
            jump jawa_03_suggest_polymorphism
        "繼續觀察":
            jump jawa_03_end

label jawa_03_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 的『繼承』允許子類別獲得父類別的特性。而『多型』則讓同一種訊息 (例如 open) 根據物件的不同類型而產生不同的行為。這大大提升了系統的擴充性。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
