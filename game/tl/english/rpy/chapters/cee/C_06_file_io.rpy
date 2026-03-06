# TODO: Translation updated at 2026-03-05 23:43

# game/rpy/chapters/cee/C_06_file_io.rpy:10
translate english cee_C06_start_378d2c9e:

    # cee "（正搬著一個發光的巨大方塊，那是累積了很久的系統日誌）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:12
translate english cee_C06_start_e80123bb:

    # cee "暫存空間（RAM）即將溢位。必須轉移到持久化儲存區。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:14
translate english cee_C06_start_41d4b9ea:

    # cee "（試圖一口氣把方塊塞進一個沉重的石門後，石門紋絲不動）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:16
translate english cee_C06_start_beb9a43f:

    # cee "存取速度受限。吞吐量過載。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:21
translate english cee_C06_start_d827f3c7:

    # rusty "Cee！持久化儲存區（硬碟）是很慢的！你不能像搬家一樣一次全塞進去。"
    rusty ""

# game/rpy/chapters/cee/C_06_file_io.rpy:23
translate english cee_C06_start_313d6acd:

    # rusty "萬一搬到一半斷電了，你手裡的資料就全丟了！"
    rusty ""

# game/rpy/chapters/cee/C_06_file_io.rpy:25
translate english cee_C06_start_e2ec00ac:

    # cee "（看著沉重的石門，露出疲憊的神色）每次只能刻錄一個位元組。太慢了。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:27
translate english cee_C06_start_885e38ab:

    # narrator "你需要幫 Cee 建立一套穩健的資料傳輸機制：串流 (Stream) 與 緩衝 (Buffer)。"
    narrator ""

# game/rpy/chapters/cee/C_06_file_io.rpy:40
translate english cee_06_ask_jawa_ad175073:

    # player "Jawa 的辦公室有高級的資料庫，不能存那裡嗎？"
    player ""

# game/rpy/chapters/cee/C_06_file_io.rpy:42
translate english cee_06_ask_jawa_75cecd2d:

    # cee "（搖頭）那需要太多握手協議（Handshake）。我需要最直接、無格式的二進位存取。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:44
translate english cee_06_ask_jawa_9e9b4382:

    # cee "檔案系統。最原始、最快速。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:49
translate english cee_06_suggest_buffering_1fbb9adb:

    # player "Cee，我們用個『小桶子』(Buffer) 來接資料。"
    player ""

# game/rpy/chapters/cee/C_06_file_io.rpy:51
translate english cee_06_suggest_buffering_b2bc341c:

    # player "你先把資料填滿這個小桶子，然後一次性倒進石門裡。這樣你就不用每次都去推門，效率會高很多！"
    player ""

# game/rpy/chapters/cee/C_06_file_io.rpy:53
translate english cee_06_suggest_buffering_30dcaf77:

    # cee "（眼睛一亮）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:55
translate english cee_06_suggest_buffering_d3c41fa6:

    # cee "緩衝區寫入。減少系統調用。開門（Open）、寫入（Write）、關門（Close）。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:57
translate english cee_06_suggest_buffering_dfeb07fd:

    # cee "（她拿出一組漏斗和水桶，開始有節奏地傳輸資料）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:59
translate english cee_06_suggest_buffering_71af1c5e:

    # cee "串流建立。`FILE *fp = fopen(\"log.dat\", \"wb\");`"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:63
translate english cee_06_suggest_buffering_639d29b5:

    # cee "（資料穩健地被刻錄進石門，石門發出低沉的運轉聲）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:65
translate english cee_06_suggest_buffering_b4c1f4e2:

    # cee "完成。資料已持久化。即使我重啟，它也會在那裡。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:67
translate english cee_06_suggest_buffering_18d125a3:

    # rusty "呼，總算不用擔心日誌丟失了。Cee，你這次做得真仔細。"
    rusty ""

# game/rpy/chapters/cee/C_06_file_io.rpy:78
translate english cee_06_suggest_brute_force_192d125f:

    # player "你就慢慢搬吧，勤能補拙。"
    player ""

# game/rpy/chapters/cee/C_06_file_io.rpy:80
translate english cee_06_suggest_brute_force_32f13bc8:

    # cee "（繼續笨拙地搬運，石門不時卡住）"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:82
translate english cee_06_suggest_brute_force_a53834d7:

    # cee "低效。系統可能在完成前崩潰。"
    cee ""

# game/rpy/chapters/cee/C_06_file_io.rpy:100
translate english cee_06_end_a6fe5f3b:

    # teaching "你學會了：在 C 語言中，檔案操作（File I/O）是實現資料持久化的關鍵。透過使用緩衝區（Buffering）和串流（Streams），可以平衡內存與磁碟之間的巨大速度差異，提高傳輸效率。"
    teaching ""

translate english strings:

    # game/rpy/chapters/cee/C_06_file_io.rpy:30
    old "建議使用『小桶接水』 (Buffering) 的方式傳輸"
    new "Suggest using the 'Small bucket water transfer' (Buffering) method"

    # game/rpy/chapters/cee/C_06_file_io.rpy:33
    old "建議她一直搬到搬完為止"
    new "Suggest she keeps moving until she finishes"

    # game/rpy/chapters/cee/C_06_file_io.rpy:36
    old "問她為什麼不叫 Jawa 用資料庫？"
    new "Ask her why not ask Jawa to use a database?"

    # game/rpy/chapters/cee/C_06_file_io.rpy:91
    old "使用緩衝區 (Buffer) 傳輸"
    new "Use buffer (Buffer) transfer"

