# ============================================================================
# 源界 (Source Realm) - Jawa Chapter 4: 安全網 (Safety Nets)
# ============================================================================

label jawa_J04_start:
    scene bg contract_office
    
    show jawa normal at left
    show rusty normal at center
    show py normal at right
    
    jawa "（正在批改一大疊合約，神情專注）"
    
    jawa "合約 A：通過。合約 B：通過。"
    
    py "（隨手遞過來一份合約）Jawa 姐，這份我剛寫好的，幫我也過一下？"
    
    jawa "（接過合約，讀到一半，突然整個人僵住，瞳孔放大）"
    
    show rusty shock at center
    rusty "（尖叫）Jawa 姐！你的系統正在報錯！『除以零』錯誤！"
    
    jawa "（聲音顫抖）錯誤不可控... 系統即將崩潰... 終止所有進程..."
    
    py "（撓頭）哎呀，我只是隨手寫了個分母為 0 的公式，有這麼嚴重嗎？"
    
    narrator "在 Jawa 的世界裡，如果不對錯誤進行處理，整個系統會因為一個小小的例外而徹底停擺。你需要幫她建立一套『例外處理機制』。"

    menu:
        "建議建立『捕獲網』 (Try-Catch) 攔截錯誤":
            jump jawa_04_suggest_try_catch

        "建議 Py 以後寫合約要先檢查有沒有 0":
            jump jawa_04_suggest_precheck

        "問她為什麼不直接忽略這個錯誤？":
            jump jawa_04_ask_why_no_ignore

label jawa_04_ask_why_no_ignore:
    player "為什麼不直接忽略這個 0？就當它沒發生過。"
    
    jawa "（艱難地重啟中）不... 不行。那是邏輯空洞。如果不處理，後續的合約計算全都會出錯。"
    
    rusty "忽略錯誤會導致資料汙染！這是最不安全的做法！"
    
    jump jawa_04_suggest_alternative

label jawa_04_suggest_try_catch:
    player "Jawa，我們給你的工作流程加個『捕獲網』吧。"
    
    player "把這段危險的計算放在『Try』區塊裡，萬一出錯了，我們就用『Catch』把它抓住，而不是讓它毀掉整個系統。"
    
    jawa "（恢復冷靜，深呼吸）"
    
    jawa "嘗試... 捕獲... 處理..."
    
    jawa "（重新開始批改，這次她周圍出現了一層紫色的光網）"
    
    jawa "合約 C：出錯（除以零）。異常被捕獲。回傳錯誤報告，繼續處理合約 D。"
    
    jawa "（看向 Py）你的合約被退回了，但我的系統依然穩健。"
    
    py "哇，這招不錯耶，那我以後可以隨便寫了？"
    
    jawa "（嚴厲地）不，你仍然應該寫好你的邏輯。"
    
    # 追蹤
    $ track_learned_concept("exceptions")
    $ track_affection("jawa", 10)
    $ jawa_relationship = "TRUSTED"
    $ set_chapter_status("J_04", "completed")
    
    jump jawa_04_end

label jawa_04_suggest_precheck:
    player "Py，以後你算公式前，先看看分母是不是 0 嘛。"
    
    py "（吐舌頭）太麻煩了啦，我哪記得住這麼多細節。"
    
    jawa "預防勝於治療。但我們仍然需要備份方案。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("J_04", "skipped")
    
    jump jawa_04_end

label jawa_04_suggest_alternative:
    menu:
        "建立捕獲網 (Try-Catch)":
            jump jawa_04_suggest_try_catch
        "繼續觀察":
            jump jawa_04_end

label jawa_04_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：Java 提供了強大的例外處理（Exception Handling）機制。透過 `try-catch` 區塊，程式可以優雅地處理運行時發生的錯誤，而不是直接崩潰。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
