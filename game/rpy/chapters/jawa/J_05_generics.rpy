# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 5: 萬能容器 (The Universal Container)
# ============================================================================

label jawa_J05_start:
    scene bg contract_office
    
    show jawa normal at left
    show rusty normal at center
    show py normal at right
    
    rusty "（正看著兩大排櫃子嘆氣）"
    
    rusty "這一排只能裝『整數』，那一排只能裝『文字』... 萬一我有一種『又像整數又像文字』的東西，該放哪裡呀？"
    
    jawa "（手拿一疊空標籤，平靜地看著她）"
    
    jawa "Rusty。這就是強型別的嚴謹性。你不能讓一個容器變得模糊不清。"
    
    py "（懶洋洋地拿出一個麻布袋）哎呀，用我的『萬用袋』嘛！什麼都能往裡塞，管它是整數還是貓咪。"
    
    jawa "（嚴肅地）Py，你的麻布袋在取出資料時會因為『不知道是什麼』而導致轉型錯誤。"
    
    narrator "Jawa 想要一種既能裝下任何東西，又能在取出時保證型別安全的『萬能容器』。你需要幫她引入『泛型』(Generics) 的概念。"

    menu:
        "建議使用『可調整規格的標籤』 (Generics)":
            jump jawa_05_suggest_generics

        "建議使用 Py 的『萬用麻布袋』":
            jump jawa_05_suggest_python_list

        "問她為什麼不直接把所有櫃子都改成大的？":
            jump jawa_05_ask_why_no_big_box

label jawa_05_ask_why_no_big_box:
    player "把所有櫃子都做成超大型，能裝下任何東西不就行了？"
    
    jawa "（搖頭）浪費空間，且缺乏語義。如果一個櫃子什麼都能裝，它就失去了解釋資料的能力。"
    
    jump jawa_05_suggest_alternative

label jawa_05_suggest_generics:
    player "Jawa，我們做一種『帶參數的櫃子』吧。"
    
    player "在定義櫃子時，我們留一個空白位 `<T>`。等真正要用的時候，我們再決定這個 `T` 是整數還是文字。"
    
    player "這樣一個櫃子的設計圖就能生產出各種專屬型別的櫃子，既靈活又安全！"
    
    jawa "（炯炯有神，好像在思考什麼）……"
    
    pause 2.0
    
    jawa "（若無其事地繼續）...型別參數化。這就是 `List<T>` 的精髓。"
    
    jawa "（在終端機上敲下指令，一排透明的、會根據內容物自動變色的櫃子出現了）"
    
    rusty "哇！我現在可以定義一個 `List<Integer>`，它就只能裝整數，而且我拿出來的時候，系統保證它一定是整數！"
    
    jawa "正確。不需要強制轉型。安全性與靈活性的平衡。"
    
    py "（歪頭）雖然還是很囉唆，但看在它會自動變色的份上，挺酷的。"
    
    # 追蹤
    $ track_learned_concept("generics")
    $ track_affection("jawa", 15)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_05", "completed")
    
    jump jawa_05_end

label jawa_05_suggest_python_list:
    player "我覺得 Py 的麻布袋挺好用的，簡單暴力。"
    
    jawa "（皺眉）那是在玩火。在取出資料時，你必須祈禱你還記得它原本是什麼。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_05", "skipped")
    
    jump jawa_05_end

label jawa_05_suggest_alternative:
    menu:
        "使用泛型 (Generics) 容器":
            jump jawa_05_suggest_generics
        "繼續觀察":
            jump jawa_05_end

label jawa_05_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 的泛型（Generics）允許你在定義類別或方法時不指定具體的型別，而是使用型別參數。這提供了編譯時期的型別檢查，減少了運行時期的錯誤，並增加了代碼的重用性。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
