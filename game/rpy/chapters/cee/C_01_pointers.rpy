# ============================================================================
# 源界 (Source Realm) - Cee Chapter 1: 指標分配 (Pointer Assignment)
# ============================================================================

label cee_C01_start:
    scene bg memory_warehouse_office

    show cee normal at center

    cee "（看著桌上一疊厚厚的文件，眉頭微蹙）"

    cee "外部請求。來自契約局。"

    cee "需要傳輸資料區塊 0x7000 到 0x700A 的內容。"

    cee "（拿起一支筆，開始在一張窄小的申請表上快速書寫）"

    narrator "你看到 Cee 正在把箱子裡的內容一個字一個字地抄寫到申請表上。"

    narrator "那張申請表非常窄小，很快就寫滿了，但箱子裡的內容還有一大半。"

    cee "（停下筆，看著寫滿的表格）空間不足。"

    cee "需要申請更大的表格。或者分批抄寫。"

    cee "（計算中）分批抄寫預計耗時：15 小時。"

    pause 1.0

    narrator "抄寫整個資料內容（傳值）非常低效，且受限於接收方的空間大小。"

    menu:
        "建議只寫下位址，讓他們派人來閱讀資料":
            jump cee_01_suggest_pointer

        "問她為什麼不能直接把箱子給對方？":
            jump cee_01_ask_why_copy

        "靜靜觀察她分批抄寫":
            jump cee_01_continue_observing

label cee_01_ask_why_copy:
    player "為什麼不能直接把整個箱子搬給契約局？"

    cee "（停下動作，看著你）跨區權限限制。"

    cee "實體箱子不能離開倉庫。"

    cee "只能傳遞資訊。"

    cee "（低頭）所以必須抄寫。"

    jump cee_01_suggest_alternative

label cee_01_suggest_pointer:
    player "Cee，不用抄寫內容。"

    player "在那張表上，直接寫下這些箱子的位址編號。"

    player "（指著表單）就像這樣：『位址：0x7000』。"

    cee "（看著表單，又看看箱子上的貼紙）"

    cee "（停頓 2 秒）"

    cee "只傳遞位址標記..."

    player "對。這樣對方拿到表單，就能順著編號過來直接讀取內容。"

    player "你不需要搬動任何資料，也不用擔心表格寫不下。"

    cee "（眼睛微微亮起）"

    cee "（快速在表單上寫下位址）"

    cee "傳輸中..."

    cee "（放下筆）接收方回報：已透過位址存取資料。"

    cee "耗時：6 秒。"

    cee "（看著你，停留 2 秒）"

    cee "有效率。"

    cee "（把筆收回腰間）指標。很有用的工具。"

    # 追蹤：學會的概念
    $ track_learned_concept("pointers")

    # 關係進展
    $ cee_relationship = "FUNCTIONAL"
    $ set_chapter_status("C_01", "completed")
    $ last_algorithm_choice = "pointer_passing"

    # 追蹤：章節完成
    $ track_chapter_completed("C_01")

    # 追蹤：Cee 好感度增加
    $ track_affection("cee", 15)

    # 觸發成就：指標大師
    $ achievement_binary_search.grant()

    jump cee_01_end

label cee_01_continue_observing:
    narrator "你決定看她如何完成工作。"

    cee "（繼續分批抄寫，動作極快但枯燥）"

    cee "（5 小時後）第一批傳輸完成。"

    cee "（10 小時後）第二批傳輸完成。"

    cee "（15 小時後）全部完成。"

    cee "（放下筆，甩了甩手）結束。"

    cee "（看著你）這就是標準流程。雖然慢，但安全。"

    # 追蹤：觀察
    $ track_choice("observation", is_optimal=False)

    $ cee_relationship = "FIRST_CONTACT"
    $ set_chapter_status("C_01", "skipped")
    $ last_algorithm_choice = "pass_by_value"

    jump cee_01_end

label cee_01_suggest_alternative:
    menu:
        "建議使用位址指標":
            jump cee_01_suggest_pointer

        "讓她繼續抄寫":
            jump cee_01_continue_observing

label cee_01_end:
    scene black
    with Dissolve(2.0)

    teaching "你學會了：傳遞位址（指標）比複製整個資料內容（傳值）快得多，且節省空間。"

    teaching "指標就是資料的『位址標籤』。"

    pause 2.0

    # 推進時間
    $ advance_time_to_next_period()

    jump time_choice_menu
