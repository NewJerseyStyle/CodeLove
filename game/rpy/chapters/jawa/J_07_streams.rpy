# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 7: 數據流轉 (Data in Motion)
# ============================================================================

label jawa_J07_start:
    scene bg plaza_rest
    
    show jawa normal at left
    show rusty normal at center
    show py normal at right
    
    jawa "（手拿一卷長得看不見盡頭的遊客名單，正在費力地進行篩選）"
    
    jawa "首先，遍歷名單... 如果遊客 ID 有效... 存入暫存列表... 然後，對暫存列表進行排序..."
    
    jawa "（手忙腳亂地翻閱著代碼手冊）這段迴圈邏輯太長了，我快要找不到我的過濾條件在哪裡了。"
    
    py "（懶洋洋地在一旁喝著果汁）哎呀，Jawa 姐，你還在寫那種老古董的 `for` 迴圈啊？"
    
    py "你看我的：`list(filter(lambda x: x.is_valid(), visitors))`。一行搞定，多優雅！"
    
    jawa "（皺眉）Py，雖然你的寫法很簡潔，但在 Java 中，我們需要結構化的方式..."
    
    narrator "Jawa 想要一種更現代、更簡潔的方式來處理大規模資料。你需要幫她引入『串流 API』 (Streams API) 與 『Lambda 表達式』。"

    menu:
        "建議使用『數據加工流水線』 (Streams & Lambda)":
            jump jawa_07_suggest_streams

        "建議 Jawa 繼續寫傳統的迴圈，確保萬無一失":
            jump jawa_07_suggest_traditional

        "問她為什麼不叫 Cee 幫忙排序？":
            jump jawa_07_ask_cee

label jawa_07_ask_cee:
    player "Cee 最擅長算法了，讓她幫你排不是更快？"
    
    jawa "（搖頭）Cee 的排序雖然快，但那是底層操作。我這裡需要的是與物件導向結合的高層次邏輯處理。"
    
    jump jawa_07_suggest_alternative

label jawa_07_suggest_streams:
    player "Jawa，我們來建立一條『資料加工流水線』 (Stream) 吧。"
    
    player "我們不用管怎麼遍歷，只要告訴流水線：過濾 (filter) 無效 ID、轉換 (map) 格式、最後收集 (collect) 結果。"
    
    player "具體的過濾規則，我們用一種簡單的『匿名小標籤』 (Lambda) 來寫就好了！"
    
    jawa "（眼神嚴肅，好像很努力在思考）……"
    
    pause 2.0
    
    jawa "（若無其事地繼續）...宣告式編程。這就是 `stream().filter().collect()` 的魅力。"
    
    jawa "（在終端機上敲下簡潔的指令，長長的名單自動飛入流水線，另一端整齊地吐出了篩選後的結果）"
    
    rusty "哇！代碼從十幾行縮減到了三行，而且讀起來就像讀英文句子一樣順暢！"
    
    py "（挑眉）謔，沒想到 Java 也能寫出這麼漂亮的代碼，我收回之前的嘲笑。"
    
    jawa "（微微一笑）這就是進化的力量。簡潔與結構並不衝突。"
    
    # 追蹤
    $ track_learned_concept("lambdas_and_streams")
    $ track_affection("jawa", 15)
    $ jawa_relationship = "SYNCHRONIZED"
    $ set_chapter_status("J_07", "completed")
    
    jump jawa_07_end

label jawa_07_suggest_traditional:
    player "穩紮穩打比較好，繼續用迴圈吧。"
    
    jawa "（嘆氣）雖然穩健，但維護起來真的很痛苦..."
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_07", "skipped")
    
    jump jawa_07_end

label jawa_07_suggest_alternative:
    menu:
        "使用串流 API (Streams & Lambda)":
            jump jawa_07_suggest_streams
        "繼續觀察":
            jump jawa_07_end

label jawa_07_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 8 引入的串流 API (Streams) 和 Lambda 表達式極大地簡化了集合資料的處理。這種函數式編程風格讓開發者可以用『做什麼』而非『怎麼做』的方式來描述邏輯，提高了代碼的可讀性和效率。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
