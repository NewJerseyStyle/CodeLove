# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 1: 類型約束 (Type Constraint)
# ============================================================================

label jawa_J01_start:
    scene bg contract_office

    show jawa normal at left
    show rusty normal at center
    show py normal at right

    jawa "（手持一份清單，對著貨架上的包裹進行核對）"

    py "（手裡抓著一個塞得滿滿的『混合箱』，試圖遞給 Jawa）"

    py "Jawa 姐，這是你要的資料清單，我把整數、字串和幾張照片都裝在一起了。多省事！"

    jawa "（推了推眼鏡，眉頭微蹙）Py，你知道我不能接收這種『內容不明』的包裹。"

    jawa "我的接口規定了這裡只能放『整數』。你塞進去的字串會讓我的邏輯報錯。"

    show rusty shock at center
    rusty "（臉色蒼白）這不只是報錯的問題！這會導致記憶體溢位！我根本不知道要分配多少空間給這堆...這堆『雜物』！"

    py "（懶洋洋地嘆了口氣）你們這些靜態型別的人就是活得太累了。打開看一下不就知道是什麼了嗎？"

    py "（突然盯著 Rusty 的站位，眼神變得犀利）"

    py "還有，Rusty，你往左移了兩個像素。"

    rusty "（愣住）啊？"

    py "（語氣變得急促且充滿強迫症）退後！對齊！你的腳跟沒跟地板的縫隙平行！這會導致 IndentationError（縮排錯誤）！我的世界會崩潰的！"

    rusty "（嚇得趕緊跳回原位）對、對不起！我這就對齊！"

    jawa "（嘆氣，轉向你）你。空白指標。"

    jawa "你看到了。Py 的『豐富』對我們來說是災難，而她的執著點...也非常奇特。"

    jawa "你覺得應該怎麼處理這堆不符合規範的資料？"

    menu:
        "支持 Jawa 的嚴格分類（強型別安全）":
            jump jawa_01_suggest_strict

        "建議定義一套『標準容器規則』（Interface）":
            jump jawa_01_suggest_interface

label jawa_01_suggest_strict:
    player "我覺得應該聽 Jawa 的。Py，你的『混合箱』雖然方便，但我們沒辦法處理它。"

    player "如果把字串塞進數字盒子，Jawa 會因為無法執行加法而當機的。"

    jawa "（點頭）正確。這就是型別檢查的價值：在錯誤發生前攔截它。"

    jawa "（遞給 Py 一套有顏色標記的盒子）"

    jawa "藍色放數字。紅色放文字。而且，請務必...對齊。"

    py "（聳聳肩）好吧，既然是在 Jawa 的地盤。不過那個盒子沒放正，歪了 5 度...（強迫症發作中）"

    # 追蹤
    $ track_learned_concept("strong_typing")
    $ jawa_relationship = "VERIFIED"
    $ track_affection("jawa", 10)
    $ track_affection("rusty", 5)

    jump jawa_01_end

label jawa_01_suggest_interface:
    player "Jawa，既然 Py 想要靈活，我們不如定義一個『通用容器規則』？"

    player "只要盒子標記為『可存取物件』，不管是數字還是文字都能放，但 Py 必須在裡面附上一張說明書。"

    jawa "……"

    pause 3.0

    jawa "（若無其事地繼續）...介面 (Interface) 模式。"

    jawa "允許不同型別的資料共存，但必須符合統一的呼叫契約。這能解決 Py 的混亂。"

    py "（眼睛一亮）喔！這聽起來不錯，只要我對齊了說明書，你們就能用了？"

    rusty "（小聲）雖然還是有點危險，但至少有了『契約』，系統就不會隨便崩潰了..."

    # 追蹤
    $ track_learned_concept("java_interfaces")
    $ jawa_relationship = "RELIABLE"
    $ track_affection("jawa", 15)

    jump jawa_01_end

label jawa_01_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 結合了強型別的安全與介面 (Interface) 的靈活性。這讓它既能保持嚴謹，又能處理來自像 Python 這種動態語言的複雜資料需求。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
