# ============================================================================
# 源界 (Source Realm) - Cee Chapter 5: 模組化與重複 (Modularization and Repetition)
# ============================================================================

label cee_C05_start:
    scene bg memory_warehouse
    
    show cee normal at center
    
    cee "（正跑來跑去，在不同的貨架上執行相同的動作：貼標籤、加封條、記錄編號）"
    
    cee "貨架 A。動作：貼標籤。加封條。記錄編號。"
    
    cee "（跑到另一邊）貨架 B。動作：貼標籤。加封條。記錄編號。"
    
    # Rusty 出現
    show rusty normal at right
    
    rusty "Cee！你這樣跑來跑去太累了吧？而且萬一你有一次忘了『加封條』，那這批資料就毀了！"
    
    cee "（停下動作，喘氣）重複勞動。邏輯完全一致。但必須在不同位址執行。"
    
    narrator "Cee 正在重複執行一段相同的邏輯，這不僅低效，而且容易出錯。你需要幫她把這段動作『封裝』起來。"

    menu:
        "建議定義一個『標準動作』 (Function) 並重複調用":
            jump cee_05_suggest_function

        "建議她寫一張大字報貼在牆上提醒自己":
            jump cee_05_suggest_note

        "問她為什麼不叫 Py 寫個腳本自動化？":
            jump cee_05_ask_py

label cee_05_ask_py:
    player "為什麼不叫 Py 幫你寫個腳本？她最擅長自動化了。"
    
    cee "（搖頭）Py 的腳本依賴太多。我需要底層的、快速的執行方式。"
    
    cee "函數呼叫。棧幀切換。這才是我的風格。"
    
    jump cee_05_suggest_alternative

label cee_05_suggest_function:
    player "Cee，我們把『貼標籤、加封條、記錄編號』這三個動作定義成一個『動作包』吧。"
    
    player "給它起個名字叫 `secure_shelf`。你只要告訴它哪一排貨架，它就會自動執行完所有動作！"
    
    cee "（眼睛微亮）"
    
    cee "宣告。參數傳遞。返回位址。"
    
    cee "（快速寫下一張 SOP 卡片）"
    
    cee "調用 `secure_shelf(Shelf_C)`。"
    
    cee "（動作瞬間變得流暢，不再需要反覆思考細節）"
    
    cee "有效率。邏輯一致性 100%。"
    
    # 追蹤
    $ track_learned_concept("functions")
    $ track_affection("cee", 10)
    $ cee_relationship = "RESONANT"
    $ set_chapter_status("C_05", "completed")
    
    jump cee_05_end

label cee_05_suggest_note:
    player "你可以在牆上寫張大字報：『記得加封條！』，這樣就不會忘了。"
    
    cee "（看著大字報）輔助提醒。但無法減少移動路徑。"
    
    $ track_choice("observation", is_optimal=False)
    $ set_chapter_status("C_05", "skipped")
    
    jump cee_05_end

label cee_05_suggest_alternative:
    menu:
        "定義標準動作 (Function)":
            jump cee_05_suggest_function
        "繼續觀察":
            jump cee_05_suggest_note

label cee_05_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：在 C 語言中，函數（Function）是基本的邏輯單元。透過將重複的代碼封裝成函數，可以提高代碼的可讀性、重用性，並減少錯誤。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
