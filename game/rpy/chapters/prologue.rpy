# ============================================================================
# 源界 (Source Realm) - 序章
# ============================================================================

# ============================================================================
# 標籤定義
# ============================================================================

label prologue_start:
    # 序章開始
    # 設置場景：阿源的實驗室（現實世界）

    # 停止背景音樂（如果有的話）
    stop music

    # 顯示實驗室場景
    scene bg laboratory

    # 顯示阿源留的便條
    show note paper at center

    narrator "你走進實驗室，桌上有一張便條。"

    # 便條內容
    note "我去便利店了，馬上回來。"

    note "別亂碰任何東西，特別是那個頭盔。"

    hide note

    narrator "看樣子阿源又要很久才回來。"

    narrator "你在實驗室裡四處看了看..."

    # 玩家靠近終端機
    narrator "角落裡有一台終端機，旁邊放著一個奇怪的頭盔裝置。"

    # 玩家選擇
    menu:
        "靠近終端機":
            # 追蹤選擇（非最優，因為觸發了數位化）
            $ track_choice("dialogue", is_optimal=False)
            jump prologue_approach_terminal

        "離開實驗室":
            # 追蹤選擇（最優，避免了風險）
            $ track_choice("dialogue", is_optimal=True)
            jump ending_wise_choice

label prologue_approach_terminal:
    # 玩家靠近終端機
    narrator "你好奇地走向終端機..."

    narrator "你看到有一個按鈕：『開始掃描』"

    player "新玩具！我要狠狠地試試，然後評論一番他的設計"

    # 追蹤選擇（非最優，觸發數位化）
    $ track_choice("dialogue", is_optimal=False)
    jump prologue_scan_start


label prologue_scan_start:
    # 開始掃描和數位化過程

    narrator "你按下了按鈕..."

    pause 1.0

    # TRON 風格的數位化動畫開始
    # 使用 Ren'Py 的 ATL (Animation Transformation Language) 實現

    # 第一階段：掃描
    show scan_beam at center:

        # 光束從上到下掃描
        yalign 0.0
        alpha 0.8
        ease 2.0 yalign 1.0

        # 重複掃描幾次
        repeat 3

    narrator "「開始全身掃描...」"

    hide scan_beam

    # 第四階段：進入源界
    scene bg source_realm_entrance

    # 觸發成就：踏入源界
    $ achievement_entered_source_realm.grant()

    # 追蹤：進入新世界（學會的概念）
    $ track_learned_concept("source_realm_entry")

    # 觸發中等後果（被意外傳送到源界）
    $ track_consequence("moderate")

    # 黑屏過渡
    scene black

    pause 2.0

    narrator "（你的意識開始模糊...）"

    narrator "（感覺自己被分解成無數數據流...）"

    narrator "（然後重新組合...）"

    pause 3.0

    # 進入源界 - Cee 的記憶倉庫
    scene bg memory_warehouse

    # 淡入效果
    with Dissolve(2.0)

    narrator "當你睜開眼時，周圍是一片巨大的空間。"

    narrator "就像一個無盡延伸的圖書館，但這裡不是書，而是一排排無盡的貨架。"

    narrator "每個貨架上擺滿了箱子。"

    narrator "箱子的大小不一，有的像火柴盒，有的像櫃子。"

    narrator "每個箱子上面都貼著一張標籤。"

    narrator "標籤上寫著奇怪的代碼，比如：7FF4A、7FF4B、7FF4C..."

    narrator "但你也能看到標籤上還有一行小字，寫著實際的內容："

    narrator "- 7FF4A：圖書館目錄"

    narrator "- 7FF4B：城市地圖"

    narrator "- 7FF4C：天氣預報"

    narrator "有些箱子在閃爍。"

    narrator "有些箱子是空的。"

    pause 2.0

    narrator "遠處有人影在快速移動——那移動速度令人驚訝。"

    # Cee 發現玩家
    show cee normal at left

    # Cee 注意到異常
    cee "......"

    pause 1.0

    # Cee 停下工作，文件掉落
    show cee shock at left
    with Dissolve(0.5)

    cee "......"

    # Cee 進入 Freeze 狀態（Segmentation Fault → Core Dump → Freeze）
    narrator "（她突然停止了所有動作，眼神空白，像電腦死機了一樣）"

    narrator "（手中的文件掉落在地）"

    narrator "（然後，她整個人的姿勢定格了）"

    pause 2.0

    narrator "（這狀態持續了幾秒鐘...）"

    pause 2.0

    # Cee 重啟
    show cee normal at left
    with Dissolve(1.0)

    # 觸發成就：初次相遇
    $ achievement_met_cee.grant()

    # 追蹤：第一次與 Cee 對話
    $ track_dialogue("cee")

    # 追蹤：學會的概念（C 語言的型別系統）
    $ track_learned_concept("c_type_system")

    cee "（快速眨眼）"

    cee "（上下打量你）沒有標籤。沒有型別元資料。"

    cee "（抬頭）你是什麼『種類』的？"

    menu:
        "我是人類，這是什麼地方":
            # 追蹤選擇
            $ track_choice("dialogue", is_optimal=True)
            jump prologue_player_explain

        "（不安地保持沉默）":
            # 追蹤選擇
            $ track_choice("dialogue", is_optimal=False)
            jump prologue_player_silent

label prologue_player_explain:
    player "我是個人類。"

    cee "（歪頭）...人類？"

    cee "（搜尋中...查無此型別）"

    cee "沒有標頭檔定義。型別：未知。"

    cee "（合上手冊）暫時標記為：通用容器。"

    jump prologue_rusty_appears

label prologue_player_silent:
    cee "......"

    pause 2.0

    cee "（等了三秒）無回應。"

    cee "（轉身）預設為空物件。標記：NULL。"

    jump prologue_rusty_appears

label prologue_rusty_appears:
    # Rusty 登場
    show rusty normal at right
    with MoveTransition(1.0)

    rusty "等一下，Cee！別那麼快就把人家標記成 NULL 啦！"

    cee "（轉頭）Rusty。工作時間。"

    rusty "（轉向你，有些不好意思地笑了笑）嘿，別介意。她不是討厭你，她只是習慣用『系統語言』說話。"

    rusty "我叫 Rusty。我是這裡的實習管理員。"

    rusty "她剛剛說你沒有『型別』，意思是你還沒有被這裡的系統認可，就像是一本沒有封面的書。"

    jump prologue_cee_accept

label prologue_cee_accept:
    cee "（指著貨架）你現在就像這張白紙。"

    cee "沒有內容。沒有大小。在系統中佔據了空間，卻沒有定義。"

    rusty "所以啦，如果你想在源界走動，至少要先給自己寫個『標籤』。"

    rusty "不然 Master Control Program 的薩克會把你當成垃圾資料消滅掉的！"

    # 玩家可以問問題
    menu:
        "這是哪裡？":
            jump prologue_ask_location

        "我要怎麼出去？":
            jump prologue_ask_exit

label prologue_ask_location:
    player "這裡是什麼地方？為什麼到處都是箱子？"

    rusty "這裡是『記憶倉庫』。源界所有運行的資料都存在這裡。"

    cee "資料的物理存放區。"

    rusty "（吐舌頭）她又開始了。簡單說，這裡是源界的底層。你想去的地方、看到的人，其實都是從這裡的資料『長』出來的。"

    jump prologue_more_questions

label prologue_ask_exit:
    player "我要怎麼離開這裡？"

    cee "資訊廣場。位址 4092。"

    rusty "那是源界的核心區，也就是大家生活的地方。"

    rusty "但是...（指著遠方扭曲的空間）現在通道的索引壞掉了。就像地圖被撕碎了。"

    rusty "如果你不知道如何透過編號『找路』，你可能會迷失在無盡的空白位址裡。"

    jump prologue_teaching_address

label prologue_more_questions:
    menu:
        "我要怎麼出去？":
            jump prologue_ask_exit

        "我想學習如何幫你":
            jump prologue_teaching_address

        "我就在這裡看":
            jump prologue_just_watch

label prologue_teaching_address:
    cee "（走向一個箱子，指著上面的貼紙）"

    cee "每個箱子都有這種編號。"

    cee "（展示貼紙）1024。"

    cee "這不是內容。這是它的位址。也就是它在貨架上的位置。"

    rusty "這就是我們說的『位址』。如果你要叫 Cee 幫你拿東西，你只要報號碼，她就能瞬間飛過去！"

    cee "搬動整個箱子太慢。記住編號，直接讀取內容。這才有效率。"

    rusty "所以，在去資訊廣場之前，你要先幫 Cee 處理一些『損毀的標籤』。"

    rusty "這也是為了讓系統重新認識你，幫你建立一個正確的『標籤』。"

    menu:
        "好，我試試看":
            jump prologue_start_C01

        "先在旁邊觀察一下":
            jump prologue_just_watch

label prologue_just_watch:
    narrator "你決定在旁邊觀察 Cee 的工作方式。"

    cee "（拿著一本書）演算法導論。分類：A。"

    cee "（看著一排排不見盡頭的貨架）"

    cee "一個一個找吧。"

    cee "（走向第一個箱子）編號 0x0001。內容：A 語言入門。"

    cee "不是。"

    cee "（走向第二個箱子）編號 0x0002。內容：C++ 入門。"

    cee "不是。"

    narrator "你觀察著貨架，發現它們是有順序的。"

    narrator "每個區域的標籤按字母順序排列，像索引一樣。"

    narrator "區域 1：A-D。區域 2：E-H。區域 3：I-L。區域 4：M-Z。"

    narrator "既然書是 A 開頭，應該直接去區域 1。"

    menu:
        "建議按索引區域找":
            jump prologue_suggest_binary_search

        "繼續觀察":
            jump prologue_continue_watching

label prologue_suggest_binary_search:
    player "Cee，看這裡。貨架是按字母分區的。"

    player "A-D 在區域 1，E-H 在區域 2。"

    player "你手裡的書是 A 開頭，直接去區域 1 找就好了。"

    cee "（停下動作，看著貨架的分區標記）"

    cee "（思考 2 秒）"

    cee "（走向區域 1，直接找到位置）"

    cee "有效率。"

    cee "（轉身看向你）"

    cee "你對結構很有感覺。"

    # 追蹤：學會的概念
    $ track_learned_concept("binary_search")

    # 追蹤：算法推薦（最優選擇）
    $ track_choice("algorithm", is_optimal=True)

    # 關係進展
    $ cee_relationship = "FUNCTIONAL"
    $ set_chapter_status("C_01", "completed")
    $ last_algorithm_choice = "binary_search"

    # 追蹤：章節完成
    $ track_chapter_completed("C_01")

    # 追蹤：Cee 好感度增加
    $ track_affection("cee", 10)

    jump prologue_end

label prologue_continue_watching:
    narrator "你決定不說話，看她繼續工作。"

    cee "（繼續一個一個檢查，動作很快但機械）"

    narrator "（10 分鐘後）"

    cee "找到了。"

    cee "（轉頭看著你）花了很長時間。"

    cee "（低頭）沒關係。只要能找到。"

    # 追蹤：觀察
    $ track_choice("observation", is_optimal=False)

    $ cee_relationship = "FIRST_CONTACT"
    $ set_chapter_status("C_01", "skipped")
    $ last_algorithm_choice = "linear_search"

    jump prologue_end

label prologue_start_C01:
    cee "想學怎麼操作位址？"

    cee "那就從這個開始。"

    cee "（指向一疊待處理的文件）"

    cee "這是一個任務。位址分配。"

    cee "跟我來。"

    menu:
        "準備好了":
            jump cee_C01_start

        "我還需要一點時間":
            jump prologue_just_watch

label prologue_end:
    # 序章結束，轉入時間線系統
    scene black

    with Dissolve(2.0)

    narrator "你了解了源界的基本情況..."

    narrator "以及 Cee 的工作方式。"

    narrator "現在，你需要在源界中找到回家的路……又或者展開冒險。"

    # 進入時間線系統
    jump time_choice_menu
