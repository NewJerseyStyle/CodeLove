# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/cee/C_08_recursion.rpy:10
translate english cee_C08_start_e284924d:

    # cee "（站在一個像俄羅斯娃娃一樣的貨架前，貨架上有一個小盒子，盒子裡還有更小的盒子）"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:12
translate english cee_C08_start_66fb6668:

    # cee "目標資料：存放在最深處的『原始碼核心』。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:14
translate english cee_C08_start_14982415:

    # cee "層級深度：未知。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:16
translate english cee_C08_start_0012959b:

    # cee "（正試圖用一個超長的迴圈 `for (int i=0; i<100; i++)` 來打開，但盒子層次似乎比 100 還要深）"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:21
translate english cee_C08_start_10d949fe:

    # rusty "天哪！Cee，你這樣一層一層算，萬一有一萬層，你的代碼就得寫一萬行了！"
    rusty ""

# game/rpy/chapters/cee/C_08_recursion.rpy:23
translate english cee_C08_start_f6bbb74f:

    # rusty "而且你根本不知道到底有幾層，這種結構（Tree/Fractal）簡直是迴圈的噩夢！"
    rusty ""

# game/rpy/chapters/cee/C_08_recursion.rpy:25
translate english cee_C08_start_e84a260e:

    # cee "（停下動作，看著深不見底的盒子）迴圈無法處理未知深度。邏輯崩潰。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:27
translate english cee_C08_start_a0491b5a:

    # narrator "你需要幫 Cee 建立一套能夠自我調用的邏輯結構：遞迴 (Recursion) 與 樹 (Tree)。"
    narrator ""

# game/rpy/chapters/cee/C_08_recursion.rpy:40
translate english cee_08_ask_jawa_0da3ddf3:

    # player "Jawa 的物件導向層級也很深，她怎麼解決的？"
    player ""

# game/rpy/chapters/cee/C_08_recursion.rpy:42
translate english cee_08_ask_jawa_475dace2:

    # cee "（搖頭）那是類的繼承。這是資料的巢狀。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:44
translate english cee_08_ask_jawa_e60dc728:

    # cee "我需要直接在棧（Stack）空間進行自我調用。這才是算法的極致。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:49
translate english cee_08_suggest_recursion_72051c20:

    # player "Cee，我們建立一個叫 `open_box` 的動作。"
    player ""

# game/rpy/chapters/cee/C_08_recursion.rpy:51
translate english cee_08_suggest_recursion_7614e36c:

    # player "如果盒子裡還有盒子，就讓 `open_box` 再去觸發 `open_box` 動作處理那個小盒子。"
    player ""

# game/rpy/chapters/cee/C_08_recursion.rpy:53
translate english cee_08_suggest_recursion_8698e46d:

    # player "這就是『遞迴』——動作會一直重複自己，直到找到核心為止！"
    player ""

# game/rpy/chapters/cee/C_08_recursion.rpy:55
translate english cee_08_suggest_recursion_30dcaf77:

    # cee "（眼睛一亮）"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:57
translate english cee_08_suggest_recursion_f09de43c:

    # cee "定義基底情況（Base Case）。自我調用（Self-Calling）。棧幀入棧。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:59
translate english cee_08_suggest_recursion_43982d1a:

    # cee "（她迅速寫下這段代碼，開始快速、精確地拆解層層疊疊的盒子）"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:61
translate english cee_08_suggest_recursion_b8bb4c16:

    # cee "進入第 1 層... 進入第 10 層... 進入第 1000 層..."
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:65
translate english cee_08_suggest_recursion_c225aee4:

    # cee "（終於，她從最深處拿出了一個閃爍著金光的核心）"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:67
translate english cee_08_suggest_recursion_61cf9104:

    # cee "找到『原始碼核心』。解構完成。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:69
translate english cee_08_suggest_recursion_50898ea6:

    # cee "（微微喘氣）雖然對棧空間消耗很大，但非常優雅。這就是算法的美感。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:80
translate english cee_08_suggest_brute_force_67511414:

    # player "砸了吧，太麻煩了。"
    player ""

# game/rpy/chapters/cee/C_08_recursion.rpy:82
translate english cee_08_suggest_brute_force_146771c0:

    # cee "（嚴肅地）暴力無法解決邏輯問題。資料完整性是我的底線。"
    cee ""

# game/rpy/chapters/cee/C_08_recursion.rpy:100
translate english cee_08_end_cc0cdec6:

    # teaching "你學會了：遞迴（Recursion）是函數調用自身的編程技術。它非常適合處理像樹（Tree）或圖（Graph）這種具有自我相似結構的資料。雖然遞迴會消耗內存棧空間，但在解決複雜的巢狀問題時，它的代碼往往比迴圈更簡潔、更強大。"
    teaching ""

translate english strings:

    # game/rpy/chapters/cee/C_08_recursion.rpy:30
    old "建議使用『複製自己並進入下一層』 (Recursion) 的方法"
    new "Suggest using the 'Copy yourself and enter the next layer' (Recursion) method"

    # game/rpy/chapters/cee/C_08_recursion.rpy:33
    old "建議她拿個大錘子把盒子全砸了"
    new "Suggest she uses a big hammer to smash all the boxes"

    # game/rpy/chapters/cee/C_08_recursion.rpy:36
    old "問她為什麼不叫 Jawa 用對象導向解決？"
    new "Ask her why not ask Jawa to use object-oriented solutions?"

    # game/rpy/chapters/cee/C_08_recursion.rpy:91
    old "使用遞迴 (Recursion) 算法"
    new "Use recursion (Recursion) algorithm"

