# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:12
translate english jawa_J06_start_ccbae718:

    # jawa "（手速極快地處理著文件，但桌上的文件堆得比人還高）"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:14
translate english jawa_J06_start_c2d902c0:

    # jawa "隊列積壓嚴重。目前已處理 150/10000 份合約。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:16
translate english jawa_J06_start_66d7ddff:

    # golly "（懶洋洋地靠在門邊）哎呀，Jawa 姐，你還在一個一個地處理啊？"
    golly ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:18
translate english jawa_J06_start_2cec0f26:

    # golly "要是我，早就開一千個分身同時開工了。看！"
    golly ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:21
translate english jawa_J06_start_b10deb34:

    # golly "（殘影重合）一秒鐘，搞定。"
    golly ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:23
translate english jawa_J06_start_bdb3c101:

    # jawa "（推眼鏡）Golly。你的並行處理雖然快，但極度不安全。萬一兩個人同時改同一份資料怎麼辦？"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:25
translate english jawa_J06_start_f0e36e65:

    # jawa "會出現競態條件（Race Condition）。那是資料的毀滅。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:27
translate english jawa_J06_start_0bca7c7f:

    # narrator "Jawa 想要提升速度，但又對多個分身（執行緒）同時存取資源感到擔憂。你需要幫她建立一套『安全的多執行緒』機制。"
    narrator ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:40
translate english jawa_06_ask_golly_4a4942bf:

    # player "既然 Golly 那麼快，就把合約都給他吧。"
    player ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:42
translate english jawa_06_ask_golly_6315b685:

    # jawa "（嚴肅地）不行。Golly 的並行太隨性了。契約局需要的是精確的同步和狀態管理。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:44
translate english jawa_06_ask_golly_87cf0647:

    # jawa "這不是單純的速度問題，是可靠性的問題。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:49
translate english jawa_06_suggest_threads_b4483092:

    # player "Jawa，我們開啟『多執行緒』吧。讓多個助手同時批改合約。"
    player ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:51
translate english jawa_06_suggest_threads_eaf857b4:

    # player "為了防止他們打架，我們規定：每當要動同一個資料櫃時，助手必須先拿到『互斥鎖』 (Synchronized)。"
    player ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:53
translate english jawa_06_suggest_threads_66a06092:

    # player "拿到鎖的人才能動，其他人排隊。這樣既能變快，資料也是安全的！"
    player ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:55
translate english jawa_06_suggest_threads_6cae6e2d:

    # jawa "（眼睛一亮）"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:57
translate english jawa_06_suggest_threads_f13ee10a:

    # jawa "互斥訪問。執行緒安全。`synchronized(this)`。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:59
translate english jawa_06_suggest_threads_72bd27c5:

    # jawa "（在終端機上敲下指令，幾道紫色的光芒從她身上分離出來，化作幾個同樣神情的助手）"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:61
translate english jawa_06_suggest_threads_a70c8e73:

    # jawa "（助手們開始有條不紊地處理文件，每當碰到共用的帳本，都會先進行『加鎖』動作）"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:65
translate english jawa_06_suggest_threads_4d3526d9:

    # jawa "處理進度：1500/10000。吞吐量提升了 10 倍。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:67
translate english jawa_06_suggest_threads_976cc83e:

    # golly "（挑眉）喔？雖然還是比我保守，但這套同步機制確實挺穩的嘛。"
    golly ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:69
translate english jawa_06_suggest_threads_4ed65890:

    # jawa "（平靜地）安全才是契約的根本。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:80
translate english jawa_06_suggest_overclock_9d6a6ee9:

    # player "Jawa，跑快點！別輸給 Golly！"
    player ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:82
translate english jawa_06_suggest_overclock_d594f868:

    # jawa "（汗水滴落）單核頻率已達極限。這不是體力能解決的問題，是架構問題。"
    jawa ""

# game/rpy/chapters/jawa/J_06_multi_threading.rpy:100
translate english jawa_06_end_621a1c06:

    # teaching "你學會了：Java 支援原生多執行緒（Multi-threading）。透過將任務分配給不同的執行緒並使用 `synchronized` 關鍵字來保護共享資源，可以讓程式在多核心處理器上發揮巨大的效能，同時保證資料的一致性。"
    teaching ""

translate english strings:

    # game/rpy/chapters/jawa/J_06_multi_threading.rpy:30
    old "建議開啟『執行緒助手』 (Threads) 並配備『互斥鎖』 (Synchronized)"
    new "Suggest turning on 'Thread Helper' (Threads) and equipping 'Mutex' (Synchronized)"

    # game/rpy/chapters/jawa/J_06_multi_threading.rpy:33
    old "建議 Jawa 直接加速，跑得比 Golly 還快"
    new "Suggest Jawa speed up directly, run faster than Golly"

    # game/rpy/chapters/jawa/J_06_multi_threading.rpy:36
    old "問她為什麼不把合約都交給 Golly 處理？"
    new "Ask her why not give all the contracts to Golly to handle?"

    # game/rpy/chapters/jawa/J_06_multi_threading.rpy:91
    old "使用多執行緒 (Threads) 與同步 (Synchronized)"
    new "Use multi-threading (Threads) and synchronization (Synchronized)"

