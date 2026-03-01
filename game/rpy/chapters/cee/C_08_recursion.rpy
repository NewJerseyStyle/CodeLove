# ============================================================================
# 源界 (Source Realm) - Cee Chapter 8: 無限迴圈的奧秘 (The Mystery of Recursion)
# ============================================================================

label cee_C08_start:
    scene bg memory_warehouse_fractal
    
    show cee normal at center
    
    cee "（站在一個像俄羅斯娃娃一樣的貨架前，貨架上有一個小盒子，盒子裡還有更小的盒子）"
    
    cee "目標資料：存放在最深處的『原始碼核心』。"
    
    cee "層級深度：未知。"
    
    cee "（正試圖用一個超長的迴圈 `for (int i=0; i<100; i++)` 來打開，但盒子層次似乎比 100 還要深）"
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "天哪！Cee，你這樣一層一層算，萬一有一萬層，你的代碼就得寫一萬行了！"
    
    rusty "而且你根本不知道到底有幾層，這種結構（Tree/Fractal）簡直是迴圈的噩夢！"
    
    cee "（停下動作，看著深不見底的盒子）迴圈無法處理未知深度。邏輯崩潰。"
    
    narrator "你需要幫 Cee 建立一套能夠自我調用的邏輯結構：遞迴 (Recursion) 與 樹 (Tree)。"

    menu:
        "建議使用『複製自己並進入下一層』 (Recursion) 的方法":
            jump cee_08_suggest_recursion

        "建議她拿個大錘子把盒子全砸了":
            jump cee_08_suggest_brute_force

        "問她為什麼不叫 Jawa 用對象導向解決？":
            jump cee_08_ask_jawa

label cee_08_ask_jawa:
    player "Jawa 的物件導向層級也很深，她怎麼解決的？"
    
    cee "（搖頭）那是類的繼承。這是資料的巢狀。"
    
    cee "我需要直接在棧（Stack）空間進行自我調用。這才是算法的極致。"
    
    jump cee_08_suggest_alternative

label cee_08_suggest_recursion:
    player "Cee，我們寫一個叫 `open_box` 的動作。"
    
    player "如果盒子裡還有盒子，就讓 `open_box` 再去呼叫 `open_box` 處理那個小盒子。"
    
    player "這就是『遞迴』——動作會一直重複自己，直到找到核心為止！"
    
    cee "（眼睛一亮）"
    
    cee "定義基底情況（Base Case）。自我調用（Self-Calling）。棧幀入棧。"
    
    cee "（她迅速寫下這段代碼，開始快速、精確地拆解層層疊疊的盒子）"
    
    cee "進入第 1 層... 進入第 10 層... 進入第 1000 層..."
    
    pause 1.0
    
    cee "（終於，她從最深處拿出了一個閃爍著金光的核心）"
    
    cee "找到『原始碼核心』。解構完成。"
    
    cee "（微微喘氣）雖然對棧空間消耗很大，但非常優雅。這就是算法的美感。"
    
    # 追蹤
    $ track_learned_concept("recursion")
    $ track_affection("cee", 15)
    $ cee_relationship = "RESONANT"
    $ set_chapter_status("C_08", "completed")
    
    jump cee_08_end

label cee_08_suggest_brute_force:
    player "砸了吧，太麻煩了。"
    
    cee "（嚴肅地）暴力無法解決邏輯問題。資料完整性是我的底線。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("C_08", "skipped")
    
    jump cee_08_end

label cee_08_suggest_alternative:
    menu:
        "使用遞迴 (Recursion) 算法":
            jump cee_08_suggest_recursion
        "繼續觀察":
            jump cee_08_end

label cee_08_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：遞迴（Recursion）是函數調用自身的編程技術。它非常適合處理像樹（Tree）或圖（Graph）這種具有自我相似結構的資料。雖然遞迴會消耗內存棧空間，但在解決複雜的巢狀問題時，它的代碼往往比迴圈更簡潔、更強大。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
