# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 1: 類型約束 (Type Constraint)
# ============================================================================

label jawa_J01_start:
    scene bg contract_office

    show jawa normal at left
    show rusty normal at right

    jawa "（手持一份清單，對著貨架上的包裹進行核對）"

    rusty "（抱著一個發光的圓球，試圖塞進一個方形的盒子裡）"

    rusty "奇怪...塞不進去..."

    jawa "（推了推眼鏡，平靜地看著 Rusty）"

    jawa "Rusty。那是 `String` (字串) 類型的資料。盒子是 `int` (整數) 類型的容量。"

    rusty "（用力擠壓）可是它們都是資料啊！為什麼不能放一起？"

    jawa "（突然停止說話，眼神空白，手停在半空）"

    pause 3.0

    jawa "（若無其事地繼續）...安全性考量。類型不符會導致溢位。"

    jawa "（轉向你）你。空白指標。"

    jawa "你覺得應該怎麼處理這堆不相容的資料？"

    menu:
        "建議使用強大的分類規則（強型別）":
            jump jawa_01_suggest_strict

        "建議將所有東西都包裝成一個通用容器（Object/Interface）":
            jump jawa_01_suggest_interface

        "靜靜看著 Rusty 繼續嘗試":
            jump jawa_01_continue_observing

label jawa_01_suggest_strict:
    player "我覺得應該聽 Jawa 的。不同的資料就該放在不同的盒子裡。"

    player "如果把字串塞進數字盒子，之後要計算時會出大問題的。"

    jawa "（點頭，眼神流露出一絲讚許）"

    jawa "正確。強類型確保了資料的純淨。"

    jawa "（遞給 Rusty 一套有顏色標記的盒子）"

    jawa "藍色放數字。紅色放文字。嚴格執行。"

    rusty "（嘆口氣，開始重新分類）好吧...雖然麻煩，但確實清楚多了。"

    # 追蹤：學會的概念
    $ track_learned_concept("strong_typing")

    $ jawa_relationship = "VERIFIED"
    $ track_affection("jawa", 10)

    jump jawa_01_end

label jawa_01_suggest_interface:
    player "如果資料種類太多，每個都準備盒子太累了。"

    player "不如定義一個『標準規格』？只要符合這個規格的東西，都能放進通用盒子裡。"

    jawa "（思考 2 秒）"

    jawa "（突然停止說話，眼神空白，手停在半空）"

    pause 3.0

    jawa "（若無其事地繼續）介面 (Interface) 概念。"

    jawa "定義共同特徵，忽略具體差異。"

    jawa "（翻開手冊，快速勾選幾項）"

    jawa "只要是『可儲存物件』，就視為同一類。"

    rusty "（眼睛一亮）喔！所以我只要幫這些資料貼上『可儲存』標籤，就能用同一個大箱子裝了？"

    jawa "理論上可行。靈活性增加，但存取時需要額外確認類型。"

    jawa "（看著你）很有遠見。這在處理複雜系統時很有效率。"

    # 追蹤：學會的概念
    $ track_learned_concept("java_interfaces")

    $ jawa_relationship = "RELIABLE"
    $ track_affection("jawa", 15)

    jump jawa_01_end

label jawa_01_continue_observing:
    narrator "你決定不干涉，看著 Rusty 滿頭大汗地嘗試。"

    jawa "（在旁邊翻閱手冊，不時發出輕微的嘆息）"

    rusty "（終於把圓球塞進去了，但盒子裂開了）"

    jawa "（看著裂開的盒子）類型衝突。資料損毀。"

    jawa "（轉頭看著你）看見了嗎？這就是缺乏規則的後果。"

    # 追蹤：觀察
    $ track_choice("observation", is_optimal=False)

    $ jawa_relationship = "FORMAL_CONTACT"

    jump jawa_01_end

label jawa_01_end:
    scene black
    with Dissolve(2.0)

    narrator "J_01 章節完成。"

    teaching "你學會了：Java 強調類型的安全性（強型別）。不同類型的資料不能混用。"

    teaching "但透過『介面』(Interface)，可以讓不同的資料以統一的規格被處理。"

    pause 2.0

    jump time_choice_menu
