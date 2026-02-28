# TODO: Translation updated at 2026-02-28 10:30

# game/rpy/chapters/cee/C_01_pointers.rpy:10
translate english cee_C01_start_484a6068:

    # cee "（看著桌上一疊厚厚的文件，眉頭微蹙）"
    cee "(Looking at a thick stack of documents on desk, eyebrows slightly furrowed)"

# game/rpy/chapters/cee/C_01_pointers.rpy:12
translate english cee_C01_start_9a01756e:

    # cee "外部請求。來自契約局。"
    cee "External request. From Contract Bureau."

# game/rpy/chapters/cee/C_01_pointers.rpy:14
translate english cee_C01_start_357db6a2:

    # cee "需要傳輸資料區塊 0x7000 到 0x700A 的內容。"
    cee "Need to transmit content of data blocks 0x7000 to 0x700A."

# game/rpy/chapters/cee/C_01_pointers.rpy:16
translate english cee_C01_start_7e0d636c:

    # cee "（拿起一支筆，開始在一張窄小的申請表上快速書寫）"
    cee "(Picks up a pen, starts writing quickly on a narrow application form)"

# game/rpy/chapters/cee/C_01_pointers.rpy:18
translate english cee_C01_start_de869611:

    # narrator "你看到 Cee 正在把箱子裡的內容一個字一個字地抄寫到申請表上。"
    narrator "You see Cee is copying the contents of the boxes character by character onto the application form."

# game/rpy/chapters/cee/C_01_pointers.rpy:20
translate english cee_C01_start_433b2c29:

    # narrator "那張申請表非常窄小，很快就寫滿了，但箱子裡的內容還有一大半。"
    narrator "That application form is very narrow, it's quickly filled up, but there's still more than half of the content in the boxes."

# game/rpy/chapters/cee/C_01_pointers.rpy:22
translate english cee_C01_start_a7d21172:

    # cee "（停下筆，看著寫滿的表格）空間不足。"
    cee "(Stops pen, looking at the filled form) Insufficient space."

# game/rpy/chapters/cee/C_01_pointers.rpy:24
translate english cee_C01_start_b8e37812:

    # cee "需要申請更大的表格。或者分批抄寫。"
    cee "Need to apply for a larger form. Or copy in batches."

# game/rpy/chapters/cee/C_01_pointers.rpy:26
translate english cee_C01_start_881dd7f6:

    # cee "（計算中）分批抄寫預計耗時：15 小時。"
    cee "(Calculating) Batch copying estimated time: 15 hours."

# game/rpy/chapters/cee/C_01_pointers.rpy:30
translate english cee_C01_start_68238cc3:

    # narrator "抄寫整個資料內容（傳值）非常低效，且受限於接收方的空間大小。"
    narrator "Copying entire data content (pass by value) is very inefficient, and limited by the receiver's space size."

# game/rpy/chapters/cee/C_01_pointers.rpy:43
translate english cee_01_ask_why_copy_836e74ce:

    # player "為什麼不能直接把整個箱子搬給契約局？"
    player "Why can't you just give the entire box to the Contract Bureau?"

# game/rpy/chapters/cee/C_01_pointers.rpy:45
translate english cee_01_ask_why_copy_977b1079:

    # cee "（停下動作，看著你）跨區權限限制。"
    cee "(Stops movement, looking at you) Cross-zone permission restrictions."

# game/rpy/chapters/cee/C_01_pointers.rpy:47
translate english cee_01_ask_why_copy_2a4a4f7c:

    # cee "實體箱子不能離開倉庫。"
    cee "Physical boxes cannot leave the warehouse."

# game/rpy/chapters/cee/C_01_pointers.rpy:49
translate english cee_01_ask_why_copy_a17b39e4:

    # cee "只能傳遞資訊。"
    cee "Can only transmit information."

# game/rpy/chapters/cee/C_01_pointers.rpy:51
translate english cee_01_ask_why_copy_b5ae296d:

    # cee "（低頭）所以必須抄寫。"
    cee "(Lowers head) So must copy."

# game/rpy/chapters/cee/C_01_pointers.rpy:56
translate english cee_01_suggest_pointer_c3dac6e0:

    # player "Cee，不用抄寫內容。"
    player "Cee, don't copy the content."

# game/rpy/chapters/cee/C_01_pointers.rpy:58
translate english cee_01_suggest_pointer_02d797d9:

    # player "在那張表上，直接寫下這些箱子的位址編號。"
    player "On that form, directly write down the address numbers of these boxes."

# game/rpy/chapters/cee/C_01_pointers.rpy:60
translate english cee_01_suggest_pointer_eb290569:

    # player "（指著表單）就像這樣：『位址：0x7000』。"
    player "(Points to form) Like this: 'Address: 0x7000'."

# game/rpy/chapters/cee/C_01_pointers.rpy:62
translate english cee_01_suggest_pointer_3b1fb7d6:

    # cee "（看著表單，又看看箱子上的貼紙）"
    cee "(Looking at form, then looking at the stickers on the boxes)"

# game/rpy/chapters/cee/C_01_pointers.rpy:64
translate english cee_01_suggest_pointer_df98c2c2:

    # cee "（停頓 2 秒）"
    cee "(Pauses for 2 seconds)"

# game/rpy/chapters/cee/C_01_pointers.rpy:66
translate english cee_01_suggest_pointer_5e3da6b2:

    # cee "只傳遞位址標記..."
    cee "Only transmitting address markers..."

# game/rpy/chapters/cee/C_01_pointers.rpy:68
translate english cee_01_suggest_pointer_65720a49:

    # player "對。這樣對方拿到表單，就能順著編號過來直接讀取內容。"
    player "Right. That way when they receive the form, they can follow the numbers to directly read the content."

# game/rpy/chapters/cee/C_01_pointers.rpy:70
translate english cee_01_suggest_pointer_1f03c26d:

    # player "你不需要搬動任何資料，也不用擔心表格寫不下。"
    player "You don't need to move any data, and you don't have to worry about the form being too small."

# game/rpy/chapters/cee/C_01_pointers.rpy:72
translate english cee_01_suggest_pointer_fab2e548:

    # cee "（眼睛微微亮起）"
    cee "(Eyes light up slightly)"

# game/rpy/chapters/cee/C_01_pointers.rpy:74
translate english cee_01_suggest_pointer_babb28ec:

    # cee "（快速在表單上寫下位址）"
    cee "(Quickly writes down addresses on the form)"

# game/rpy/chapters/cee/C_01_pointers.rpy:76
translate english cee_01_suggest_pointer_aa09d40c:

    # cee "傳輸中..."
    cee "Transmitting..."

# game/rpy/chapters/cee/C_01_pointers.rpy:80
translate english cee_01_suggest_pointer_a752d064:

    # cee "（放下筆）接收方回報：已透過位址存取資料。"
    cee "(Puts down pen) Receiver report: Data accessed via address."

# game/rpy/chapters/cee/C_01_pointers.rpy:82
translate english cee_01_suggest_pointer_c8c7b4c3:

    # cee "耗時：6 秒。"
    cee "Time taken: 6 seconds."

# game/rpy/chapters/cee/C_01_pointers.rpy:84
translate english cee_01_suggest_pointer_0d4c1c55:

    # cee "（看著你，停留 2 秒）"
    cee "(Looking at you, lingers for 2 seconds)"

# game/rpy/chapters/cee/C_01_pointers.rpy:86
translate english cee_01_suggest_pointer_9f6c7075:

    # cee "有效率。"
    cee "Efficient."

# game/rpy/chapters/cee/C_01_pointers.rpy:88
translate english cee_01_suggest_pointer_b9bb9096:

    # cee "（把筆收回腰間）指標。很有用的工具。"
    cee "(Returns pen to waist) Pointers. Very useful tool."

# game/rpy/chapters/cee/C_01_pointers.rpy:110
translate english cee_01_continue_observing_806adcae:

    # narrator "你決定看她如何完成工作。"
    narrator "You decide to watch her complete the work."

# game/rpy/chapters/cee/C_01_pointers.rpy:112
translate english cee_01_continue_observing_4d503f0b:

    # cee "（繼續分批抄寫，動作極快但枯燥）"
    cee "(Continues batch copying, movements extremely fast but tedious)"

# game/rpy/chapters/cee/C_01_pointers.rpy:114
translate english cee_01_continue_observing_832f24bc:

    # cee "（5 小時後）第一批傳輸完成。"
    cee "(5 hours later) First batch transmission complete."

# game/rpy/chapters/cee/C_01_pointers.rpy:116
translate english cee_01_continue_observing_a106e69c:

    # cee "（10 小時後）第二批傳輸完成。"
    cee "(10 hours later) Second batch transmission complete."

# game/rpy/chapters/cee/C_01_pointers.rpy:118
translate english cee_01_continue_observing_52d8eca9:

    # cee "（15 小時後）全部完成。"
    cee "(15 hours later) All complete."

# game/rpy/chapters/cee/C_01_pointers.rpy:120
translate english cee_01_continue_observing_ac4b33ef:

    # cee "（放下筆，甩了甩手）結束。"
    cee "(Puts down pen, shakes hand) Finished."

# game/rpy/chapters/cee/C_01_pointers.rpy:122
translate english cee_01_continue_observing_650e2b20:

    # cee "（看著你）這就是標準流程。雖然慢，但安全。"
    cee "(Looking at you) This is the standard procedure. Though slow, it's safe."

# game/rpy/chapters/cee/C_01_pointers.rpy:145
translate english cee_01_end_279459f7:

    # narrator "C_01 章節完成。"
    narrator "C_01 chapter complete."

# game/rpy/chapters/cee/C_01_pointers.rpy:147
translate english cee_01_end_1b627a48:

    # teaching "你學會了：傳遞位址（指標）比複製整個資料內容（傳值）快得多，且節省空間。"
    teaching "You learned: Passing addresses (pointers) is much faster than copying entire data content (pass by value), and saves space."

# game/rpy/chapters/cee/C_01_pointers.rpy:149
translate english cee_01_end_bf768910:

    # teaching "指標就是資料的『位址標籤』。"
    teaching "Pointers are simply 'address labels' of data."

translate english strings:

    # game/rpy/chapters/cee/C_01_pointers.rpy:33
    old "建議只寫下位址，讓他們派人來閱讀資料"
    new "Suggest writing only addresses, so they can send people to read data"

    # game/rpy/chapters/cee/C_01_pointers.rpy:36
    old "問她為什麼不能直接把箱子給對方？"
    new "Ask why she can't just give the box to the other party?"

    # game/rpy/chapters/cee/C_01_pointers.rpy:39
    old "靜靜觀察她分批抄寫"
    new "Quietly observe her batch copying"

    # game/rpy/chapters/cee/C_01_pointers.rpy:135
    old "建議使用位址指標"
    new "Suggest using address pointers"

    # game/rpy/chapters/cee/C_01_pointers.rpy:138
    old "讓她繼續抄寫"
    new "Let her continue copying"

