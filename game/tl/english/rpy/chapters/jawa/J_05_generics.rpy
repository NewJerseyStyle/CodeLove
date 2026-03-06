# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/jawa/J_05_generics.rpy:12
translate english jawa_J05_start_0efe7190:

    # rusty "（正看著兩大排櫃子嘆氣）"
    rusty ""

# game/rpy/chapters/jawa/J_05_generics.rpy:14
translate english jawa_J05_start_62947438:

    # rusty "這一排只能裝『整數』，那一排只能裝『文字』... 萬一我有一種『又像整數又像文字』的東西，該放哪裡呀？"
    rusty ""

# game/rpy/chapters/jawa/J_05_generics.rpy:16
translate english jawa_J05_start_728d112c:

    # jawa "（手拿一疊空標籤，平靜地看著她）"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:18
translate english jawa_J05_start_cec7764c:

    # jawa "Rusty。這就是強型別的嚴謹性。你不能讓一個容器變得模糊不清。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:20
translate english jawa_J05_start_e30cc4b4:

    # py "（懶洋洋地拿出一個麻布袋）哎呀，用我的『萬用袋』嘛！什麼都能往裡塞，管它是整數還是貓咪。"
    py ""

# game/rpy/chapters/jawa/J_05_generics.rpy:22
translate english jawa_J05_start_cea8b2ce:

    # jawa "（嚴肅地）Py，你的麻布袋在取出資料時會因為『不知道是什麼』而導致轉型錯誤。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:24
translate english jawa_J05_start_de72fe74:

    # narrator "Jawa 想要一種既能裝下任何東西，又能在取出時保證型別安全的『萬能容器』。你需要幫她引入『泛型』(Generics) 的概念。"
    narrator ""

# game/rpy/chapters/jawa/J_05_generics.rpy:37
translate english jawa_05_ask_why_no_big_box_161df915:

    # player "把所有櫃子都做成超大型，能裝下任何東西不就行了？"
    player ""

# game/rpy/chapters/jawa/J_05_generics.rpy:39
translate english jawa_05_ask_why_no_big_box_afd7eac3:

    # jawa "（搖頭）浪費空間，且缺乏語義。如果一個櫃子什麼都能裝，它就失去了解釋資料的能力。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:44
translate english jawa_05_suggest_generics_3f265fb6:

    # player "Jawa，我們做一種『帶參數的櫃子』吧。"
    player ""

# game/rpy/chapters/jawa/J_05_generics.rpy:46
translate english jawa_05_suggest_generics_5ab45902:

    # player "在定義櫃子時，我們留一個空白位 `<T>`。等真正要用的時候，我們再決定這個 `T` 是整數還是文字。"
    player ""

# game/rpy/chapters/jawa/J_05_generics.rpy:48
translate english jawa_05_suggest_generics_ac631c36:

    # player "這樣一個櫃子的設計圖就能生產出各種專屬型別的櫃子，既靈活又安全！"
    player ""

# game/rpy/chapters/jawa/J_05_generics.rpy:50
translate english jawa_05_suggest_generics_a7fec609:

    # jawa "（炯炯有神，好像在思考什麼）……"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:54
translate english jawa_05_suggest_generics_76657519:

    # jawa "（若無其事地繼續）...型別參數化。這就是 `List<T>` 的精髓。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:56
translate english jawa_05_suggest_generics_afa527cd:

    # jawa "（在終端機上敲下指令，一排透明的、會根據內容物自動變色的櫃子出現了）"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:58
translate english jawa_05_suggest_generics_4d788e2f:

    # rusty "哇！我現在可以定義一個 `List<Integer>`，它就只能裝整數，而且我拿出來的時候，系統保證它一定是整數！"
    rusty ""

# game/rpy/chapters/jawa/J_05_generics.rpy:60
translate english jawa_05_suggest_generics_4c7cb742:

    # jawa "正確。不需要強制轉型。安全性與靈活性的平衡。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:62
translate english jawa_05_suggest_generics_8c625efa:

    # py "（歪頭）雖然還是很囉唆，但看在它會自動變色的份上，挺酷的。"
    py ""

# game/rpy/chapters/jawa/J_05_generics.rpy:73
translate english jawa_05_suggest_python_list_a8b5042a:

    # player "我覺得 Py 的麻布袋挺好用的，簡單暴力。"
    player ""

# game/rpy/chapters/jawa/J_05_generics.rpy:75
translate english jawa_05_suggest_python_list_f5b6518d:

    # jawa "（皺眉）那是在玩火。在取出資料時，你必須祈禱你還記得它原本是什麼。"
    jawa ""

# game/rpy/chapters/jawa/J_05_generics.rpy:93
translate english jawa_05_end_7e917226:

    # teaching "你學會了：Java 的泛型（Generics）允許你在定義類別或方法時不指定具體的型別，而是使用型別參數。這提供了編譯時期的型別檢查，減少了運行時期的錯誤，並增加了代碼的重用性。"
    teaching ""

translate english strings:

    # game/rpy/chapters/jawa/J_05_generics.rpy:27
    old "建議使用『可調整規格的標籤』 (Generics)"
    new "Suggest using 'Adjustable-Spec Label' (Generics)"

    # game/rpy/chapters/jawa/J_05_generics.rpy:30
    old "建議使用 Py 的『萬用麻布袋』"
    new "Suggest using Py's 'Universal Cloth Bag'"

    # game/rpy/chapters/jawa/J_05_generics.rpy:33
    old "問她為什麼不直接把所有櫃子都改成大的？"
    new "Ask her why she doesn't just make all the cabinets bigger?"

    # game/rpy/chapters/jawa/J_05_generics.rpy:84
    old "使用泛型 (Generics) 容器"
    new "Use generics (Generics) container"

