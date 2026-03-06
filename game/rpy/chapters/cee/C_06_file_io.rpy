# ============================================================================
# 源界 (Source Realm) - Cee Chapter 6: 永久記憶 (Persistent Memory)
# ============================================================================

label cee_C06_start:
    scene bg memory_warehouse
    
    show cee normal at center
    
    cee "（正搬著一個發光的巨大方塊，那是累積了很久的系統日誌）"
    
    cee "暫存空間（RAM）即將溢位。必須轉移到持久化儲存區。"
    
    cee "（試圖一口氣把方塊塞進一個沉重的石門後，石門紋絲不動）"
    
    cee "存取速度受限。吞吐量過載。"
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "Cee！持久化儲存區（硬碟）是很慢的！你不能像搬家一樣一次全塞進去。"
    
    rusty "萬一搬到一半斷電了，你手裡的資料就全丟了！"
    
    cee "（看著沉重的石門，露出疲憊的神色）每次只能刻錄一個位元組。太慢了。"
    
    narrator "你需要幫 Cee 建立一套穩健的資料傳輸機制：串流 (Stream) 與 緩衝 (Buffer)。"

    menu:
        "建議使用『小桶接水』 (Buffering) 的方式傳輸":
            jump cee_06_suggest_buffering

        "建議她一直搬到搬完為止":
            jump cee_06_suggest_brute_force

        "問她為什麼不叫 Jawa 用資料庫？":
            jump cee_06_ask_jawa

label cee_06_ask_jawa:
    player "Jawa 的辦公室有高級的資料庫，不能存那裡嗎？"
    
    cee "（搖頭）那需要太多握手協議（Handshake）。我需要最直接、無格式的二進位存取。"
    
    cee "檔案系統。最原始、最快速。"
    
    jump cee_06_suggest_alternative

label cee_06_suggest_buffering:
    player "Cee，我們用個『小桶子』(Buffer) 來接資料。"
    
    player "你先把資料填滿這個小桶子，然後一次性倒進石門裡。這樣你就不用每次都去推門，效率會高很多！"
    
    cee "（眼睛一亮）"
    
    cee "緩衝區寫入。減少系統調用。開門（Open）、寫入（Write）、關門（Close）。"
    
    cee "（她拿出一組漏斗和水桶，開始有節奏地傳輸資料）"
    
    cee "串流建立。`FILE *fp = fopen(\"log.dat\", \"wb\");`"
    
    pause 1.0
    
    cee "（資料穩健地被刻錄進石門，石門發出低沉的運轉聲）"
    
    cee "完成。資料已持久化。即使我重啟，它也會在那裡。"
    
    rusty "呼，總算不用擔心日誌丟失了。Cee，你這次做得真仔細。"
    
    # 追蹤
    $ track_learned_concept("file_io")
    $ track_affection("cee", 10)
    $ cee_relationship = "RESONANT"
    $ set_chapter_status("C_06", "completed")
    
    jump cee_06_end

label cee_06_suggest_brute_force:
    player "你就慢慢搬吧，勤能補拙。"
    
    cee "（繼續笨拙地搬運，石門不時卡住）"
    
    cee "低效。系統可能在完成前崩潰。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("C_06", "skipped")
    
    jump cee_06_end

label cee_06_suggest_alternative:
    menu:
        "使用緩衝區 (Buffer) 傳輸":
            jump cee_06_suggest_buffering
        "繼續觀察":
            jump cee_06_suggest_brute_force

label cee_06_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：在 C 語言中，檔案操作（File I/O）是實現資料持久化的關鍵。透過使用緩衝區（Buffering）和串流（Streams），可以平衡內存與磁碟之間的巨大速度差異，提高傳輸效率。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
