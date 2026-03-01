# ============================================================================
# 源界 (Source Realm) - 漫步隨機事件系統 v2
# ============================================================================

init python:
    import random

    # 追蹤已看過的事件，避免重疊
    if 'seen_explore_events' not in globals():
        seen_explore_events = []

    def get_random_explore_event():
        all_events = [
            "event_rusty_safety_check",
            "event_py_one_liner",
            "event_witness_leetcode",
            "event_locked_area_hint",
            "event_pub_quiz_trigger",
            "event_golly_concurrent_pizza",
            "event_jawa_gc_truck",
            "event_cee_memory_leak_waterfall",
            "event_py_zen_garden",
            "event_rusty_borrow_panic",
            "event_shared_stack_vs_heap",
            "event_world_hello_monument"
        ]
        
        # 篩選掉最近看過的 3 個事件
        available = [e for e in all_events if e not in seen_explore_events[-3:]]
        if not available:
            available = all_events
            
        choice = random.choice(available)
        seen_explore_events.append(choice)
        return choice

# ============================================================================
# 漫步入口轉接
# ============================================================================

label execute_explore_random:
    # 首先檢查是否觸發特殊稀有事件（1% 機率，只觸發一次）
    jump check_special_rare_event

# ============================================================================
# 隨機事件 1: Rusty 的安全檢查
# ============================================================================

label event_rusty_safety_check:
    scene bg information_square_corner
    show rusty normal at center
    narrator "你看到 Rusty 蹲在一個轉角處，正對著一個不斷冒煙的緩衝區發愁。"
    rusty "（自言自語）所有權轉移失敗... 借用檢查器報錯... 這裡應該用不可變借用才對..."
    player "需要幫忙嗎？"
    show rusty shock
    rusty "啊！沒、沒什麼，只是在處理一個生命週期的問題。"
    $ track_affection("rusty", 5)
    jump end_time_period

# ============================================================================
# 隨機事件 2: Py 的一行解決方案
# ============================================================================

label event_py_one_liner:
    scene bg information_square_park
    show py normal at center
    narrator "Py 正躺在草地上，身旁圍繞著幾個正在處理複雜矩陣運算的機器人。"
    py "result = [[x**2 for x in matrix if x %% 2 == 0]]。好了，去玩吧。"
    py "（注意到你）喲，新來的。代碼就該像午睡一樣簡單。"
    $ track_affection("py", 5)
    jump end_time_period

# ============================================================================
# 隨機事件 3: 見證 LeetCode 解法
# ============================================================================

label event_witness_leetcode:
    scene bg information_square_forum
    narrator "布告欄前擠滿了人，大家正在討論如何優化一個『兩數之和』的任務。"
    narrator "路人 A：『用兩個嵌套迴圈，時間複雜度 O(n^2)。』"
    narrator "路人 B：『太慢了！用哈希表一次遍歷搞定，O(n) 才是優雅！』"
    $ track_learned_concept("hash_map_intro")
    jump end_time_period

# ============================================================================
# 隨機事件 4: 隱藏場景提示
# ============================================================================

label event_locked_area_hint:
    scene bg information_square_gate
    narrator "你走到了一個被銀色流光封鎖的大門前。"
    if cee_relationship in ["RESONANT", "PARTNER"]:
        narrator "門上的標籤寫著：『底層核心 - 0x0000』。現在你有權限進入。"
    else:
        narrator "門上的標籤寫著：『底層核心 - 0x0000』。你的權限不足。"
    jump end_time_period

# ============================================================================
# 隨機事件 5: Golly 的並行外送
# ============================================================================

label event_golly_concurrent_pizza:
    scene bg information_square_noon
    show golly normal at center
    narrator "你看到 Golly 站在廣場中央，打了個響指。"
    golly "一千個 Goroutine，啟動！"
    narrator "瞬間，無數個 Golly 的虛影閃過，提著披薩盒消失在不同的巷子裡。"
    $ track_affection("golly", 5)
    jump end_time_period

# ============================================================================
# 隨機事件 6: Jawa 的 GC 大掃除
# ============================================================================

label event_jawa_gc_truck:
    scene bg information_square_morning
    narrator "一輛巨大的紫色清潔車開過街道，車身上印著：『Garbage Collector』。"
    narrator "所有路人都停下了腳步（Stop the World）。"
    show jawa normal at center
    jawa "（推眼鏡）別緊張，只是例行的記憶體清理。"
    jump end_time_period

# ============================================================================
# 隨機事件 7: 記憶體洩漏瀑布
# ============================================================================

label event_cee_memory_leak_waterfall:
    scene bg memory_warehouse_river
    show cee normal at center
    narrator "Cee 站在一個不斷湧出藍色數據流的裂縫前。"
    cee "位址溢出。某個進程忘了執行 free()。這就是記憶體洩漏。"
    $ track_affection("cee", 5)
    jump end_time_period

# ============================================================================
# 隨機事件 8: Py 的禪意花園
# ============================================================================

label event_py_zen_garden:
    scene bg information_square_park
    show py normal at center
    py "來，念一遍。《The Zen of Python》。"
    py "『Beautiful is better than ugly.』"
    $ track_affection("py", 5)
    jump end_time_period

# ============================================================================
# 隨機事件 9: Rusty 的借用恐慌
# ============================================================================

label event_rusty_borrow_panic:
    scene bg information_square_corner
    show rusty shock at center
    rusty "不不不！你不能同時擁有兩個可變借用！這會導致未定義行為！"
    $ track_affection("rusty", 10)
    jump end_time_period

# ============================================================================
# 隨機事件 10: 堆疊 vs 堆積 (Stack vs Heap)
# ============================================================================

label event_shared_stack_vs_heap:
    scene bg information_square_forum
    narrator "你路過一個公園，看到兩個小孩在玩遊戲。"
    narrator "小孩 A：『看！這是 Stack！速度快但容量小！』"
    narrator "小孩 B：『這是 Heap！想放多少就放多少！』"
    jump end_time_period

# ============================================================================
# 隨機事件 11: Hello World 紀念碑
# ============================================================================

label event_world_hello_monument:
    scene bg information_square_gate
    narrator "你來到廣場盡頭，看到一座古老的方尖碑。"
    narrator "上面刻著無數種語言的同一個句子：『printf(\"Hello, World!\");』"
    $ source_realm_reputation += 5
    jump end_time_period

# ============================================================================
# 隨機事件 12: 酒館語法對決 (Pub Quiz)
# ============================================================================

label event_pub_quiz_trigger:
    scene bg pub_interior
    narrator "酒館裡傳來陣陣歡呼聲，大家正在舉行一場『語法大師』挑戰賽。"
    $ current_quiz_char = random.choice(["Cee", "Jawa", "Rusty", "Py"])
    "NPC 酒保" "嘿！要不要挑戰一下關於 [current_quiz_char] 的語法測試？"
    
    menu:
        "接受挑戰！":
            if current_quiz_char == "Cee":
                jump quiz_cee
            elif current_quiz_char == "Jawa":
                jump quiz_jawa
            elif current_quiz_char == "Rusty":
                jump quiz_rusty
            else:
                jump quiz_py
        "下次一定":
            jump end_time_period

# ----------------------------------------------------------------------------
# Cee 語法測驗 (基礎與內存)
# ----------------------------------------------------------------------------
label quiz_cee:
    $ score = 0
    "第一題：在 C 語言中，如何宣告一個指向整數的指標？"
    menu:
        "int* p;":
            $ score += 1
        "int &p;":
            pass
            
    "第二題：哪一個符號用於獲取變數的位址？"
    menu:
        "*":
            pass
        "&":
            $ score += 1
            
    "第三題：用於動態分配記憶體的函數是？"
    menu:
        "alloc()":
            pass
        "malloc()":
            $ score += 1
            
    "第四題：如何獲取一個型別或變數所佔用的位元組大小？"
    menu:
        "sizeof()":
            $ score += 1
        "length()":
            pass
            
    "第五題：字串 \"Hello\" 在記憶體中實際占用多少位元組？"
    menu:
        "5":
            pass
        "6 (包含 \\0)":
            $ score += 1

    "第六題：哪一個運算子用於透過指標存取結構體成員？"
    menu:
        ".":
            pass
        "->":
            $ score += 1

    "第七題：malloc 函數失敗時會回傳什麼？"
    menu:
        "-1":
            pass
        "NULL":
            $ score += 1

    "第八題：標準輸入輸出函數所在的標頭檔是？"
    menu:
        "stdio.h":
            $ score += 1
        "stdlib.h":
            pass

    "第九題：在 C 語言中，數組索引是從幾開始的？"
    menu:
        "0":
            $ score += 1
        "1":
            pass

    "第十題：哪一個關鍵字用於定義自定義型別別名？"
    menu:
        "typedef":
            $ score += 1
        "define":
            pass
            
    jump quiz_result

# ----------------------------------------------------------------------------
# Jawa 語法測驗 (物件與規範)
# ----------------------------------------------------------------------------
label quiz_jawa:
    $ score = 0
    "第一題：在 Java 中，實現繼承的關鍵字是什麼？"
    menu:
        "implements":
            pass
        "extends":
            $ score += 1
            
    "第二題：如何引用當前物件本身？"
    menu:
        "this":
            $ score += 1
        "super":
            pass
            
    "第三題：宣告常數（不可修改的變數）的關鍵字是？"
    menu:
        "final":
            $ score += 1
        "const":
            pass
            
    "第四題：被 static 修飾的方法屬於？"
    menu:
        "類別本身 (Class)":
            $ score += 1
        "物件實體 (Instance)":
            pass
            
    "第五題：Java 程式編譯後產生的檔案副檔名是？"
    menu:
        ".exe":
            pass
        ".class":
            $ score += 1

    "第六題：捕獲異常（Exception）應使用哪一組關鍵字？"
    menu:
        "try-catch":
            $ score += 1
        "check-fail":
            pass

    "第七題：Java 中所有類別的共同祖先是？"
    menu:
        "Base":
            pass
        "Object":
            $ score += 1

    "第八題：建立物件實體時使用的關鍵字是？"
    menu:
        "new":
            $ score += 1
        "create":
            pass

    "第九題：實現介面 (Interface) 的關鍵字是？"
    menu:
        "implements":
            $ score += 1
        "extends":
            pass

    "第十題：Java 是否支持多重類別繼承（Class Multiple Inheritance）？"
    menu:
        "支持":
            pass
        "不支持":
            $ score += 1
            
    jump quiz_result

# ----------------------------------------------------------------------------
# Rusty 語法測驗 (安全與所有權)
# ----------------------------------------------------------------------------
label quiz_rusty:
    $ score = 0
    "第一題：在 Rust 中，變數預設是？"
    menu:
        "可變的 (Mutable)":
            pass
        "不可變的 (Immutable)":
            $ score += 1
            
    "第二題：哪一個符號用於調用巨集 (Macro)？"
    menu:
        "!":
            $ score += 1
        "#":
            pass
            
    "第三題：如何解開一個 Option 或 Result 型別（如果失敗則崩潰）？"
    menu:
        ".unwrap()":
            $ score += 1
        ".get()":
            pass
            
    "第四題：Rust 處理多分支選擇最常用的關鍵字是？"
    menu:
        "switch":
            pass
        "match":
            $ score += 1
            
    "第五題：當一個變數被賦值給另一個變數時，原本的變數會？"
    menu:
        "繼續有效 (Copy)":
            pass
        "失效 (Move，除非實現了 Copy 特徵)":
            $ score += 1

    "第六題：Rust 的專案管理工具名稱是？"
    menu:
        "Cargo":
            $ score += 1
        "RustPM":
            pass

    "第七題：哪一個關鍵字用於定義共享行為（類似介面）？"
    menu:
        "interface":
            pass
        "trait":
            $ score += 1

    "第八題：用於輸出到控制台的巨集是？"
    menu:
        "println!()":
            $ score += 1
        "print()":
            pass

    "第九題：函數不回傳任何值時，其回傳型別是？"
    menu:
        "void":
            pass
        "() (Unit type)":
            $ score += 1

    "第十題：執行不安全操作（如解引用原始指標）需要放在什麼區塊中？"
    menu:
        "unsafe":
            $ score += 1
        "raw":
            pass
            
    jump quiz_result

# ----------------------------------------------------------------------------
# Py 語法測驗 (簡潔與慣用法)
# ----------------------------------------------------------------------------
label quiz_py:
    $ score = 0
    "第一題：Python 使用什麼來區分代碼塊？"
    menu:
        "縮排 (Indentation)":
            $ score += 1
        "大括號 {}":
            pass
            
    "第二題：如何定義一個函數？"
    menu:
        "def name():":
            $ score += 1
        "function name():":
            pass
            
    "第三題：在類別方法中，第一個參數通常命名為？"
    menu:
        "this":
            pass
        "self":
            $ score += 1
            
    "第四題：如何獲取列表 list 的長度？"
    menu:
        "len(list)":
            $ score += 1
        "list.size()":
            pass
            
    "第五題：哪一種是正確的列表切片方式（獲取前三個元素）？"
    menu:
        "list[0:3]":
            $ score += 1
        "list.slice(3)":
            pass

    "第六題：哪一個關鍵字用於導入模組？"
    menu:
        "import":
            $ score += 1
        "include":
            pass

    "第七題：哪一個魔術方法（Dunder method）用於初始化物件？"
    menu:
        "__init__":
            $ score += 1
        "__new__":
            pass

    "第八題：Python 3 中如何獲取用戶輸入？"
    menu:
        "input()":
            $ score += 1
        "scanf()":
            pass

    "第九題：哪一個運算子用於整數除法（無餘數）？"
    menu:
        "/":
            pass
        "//":
            $ score += 1

    "第十題：哪一個內置函數可以列出物件的所有屬性與方法？"
    menu:
        "dir()":
            $ score += 1
        "list()":
            pass
            
    jump quiz_result

# ----------------------------------------------------------------------------
# 測驗結算
# ----------------------------------------------------------------------------
label quiz_result:
    if score == 10:
        "NPC 酒保" "我的天啊！10 題全對！這簡直是神蹟！"
        "NPC 酒保" "你對 [current_quiz_char] 的理解已經達到了造物主級別！"
        $ source_realm_reputation += 100
        if current_quiz_char == "Cee":
            $ mastery_cee = 100
            $ crush_cee = True
        elif current_quiz_char == "Jawa":
            $ mastery_jawa = 100
            $ crush_jawa = True
        elif current_quiz_char == "Rusty":
            $ mastery_rusty = 100
            $ crush_rusty = True
        elif current_quiz_char == "Py":
            $ mastery_py = 100
            $ crush_py = True
        narrator "全源界現在都在傳頌你那無與倫比的語法造詣。"
    elif score >= 7:
        "NPC 酒保" "拿到了 [score] 分！非常優秀的成績，你已經是個專家了。"
    elif score >= 4:
        "NPC 酒保" "拿到了 [score] 分。中規中矩，還有進步空間。"
    else:
        "NPC 酒保" "只拿到了 [score] 分... 看來你還需要跟代碼多磨合磨合。"
    
    jump end_time_period

# ============================================================================
# 廣場小憩與遇見系統 (ST 同步版)
# ============================================================================

label execute_plaza_encounter:
    python:
        st = store.source_time
        st_in_day = st % 15
        if st_in_day < 3:
            time_feeling = "清晨的空氣帶著一絲涼意，數據霧氣還沒散去。"
            renpy.show("bg plaza_morning")
        elif st_in_day < 7:
            time_feeling = "正午的陽光（模擬光源）有些刺眼，廣場上人來人往。"
            renpy.show("bg plaza_noon")
        elif st_in_day < 10:
            time_feeling = "下午的陽光變得柔和，資料流動的聲音像遠處的蟬鳴。"
            renpy.show("bg plaza_afternoon")
        elif st_in_day < 13:
            time_feeling = "傍晚的餘暉將一切都染成了橙紫色，居民們正準備結束一天的工作。"
            renpy.show("bg plaza_evening")
        else:
            time_feeling = "深夜的廣場非常安靜，只有偶爾閃過的系統提示音。"
            renpy.show("bg plaza_night")

    narrator "[time_feeling]"
    narrator "你找了一張長椅坐下，放鬆緊繃的神經。"
    
    # 決定是普通的坐一會兒還是觸發事件
    menu:
        "閉目養神，讓時間流逝":
            narrator "你閉上眼，靜靜感受著源界的律動..."
            if st_in_day >= 13:
                menu:
                    "強打精神，再坐一會兒":
                        narrator "夜晚的風吹過，讓你稍微清醒了一些。"
                        jump end_time_period
                    "順從睡意":
                        jump execute_sleep_in_plaza
            else:
                jump end_time_period
                
        "看看周圍有沒有認識的人":
            $ encounter_chance = random.random()
            if encounter_chance < 0.5:
                $ visitor = random.choice(["cee", "jawa", "rusty", "py"])
                jump expression f"encounter_{visitor}"
            else:
                narrator "周圍都是忙碌的陌生面孔，沒看到熟悉的人。"
                jump end_time_period

# ----------------------------------------------------------------------------
# 遇見 Cee
# ----------------------------------------------------------------------------
label encounter_cee:
    show cee normal at center
    if cee_relationship == "UNMET" or cee_relationship == "FIRST_CONTACT":
        cee "（停下腳步，看著你的坐姿）"
        cee "空間佔用中。無效的操作。你為什麼在這裡浪費週期？"
    else:
        cee "（在你身邊坐下，保持一小段距離）"
        cee "短暫的休眠。有效率。我陪你一會兒。"
    $ track_affection("cee", 2)
    jump end_time_period

# ----------------------------------------------------------------------------
# 遇見 Jawa
# ----------------------------------------------------------------------------
label encounter_jawa:
    show jawa normal at center
    if jawa_relationship == "UNMET" or jawa_relationship == "FORMAL_CONTACT":
        jawa "（推眼鏡）公共長椅的使用守則第 4 條：禁止長時間無目的滯留。"
        jawa "但如果你是在整理邏輯，我可以破例不進行清理。"
    else:
        jawa "（手拿一杯熱咖啡，遞給你一罐）"
        jawa "適度的異步等待有助於系統穩定. 辛苦了。"
    $ track_affection("jawa", 2)
    jump end_time_period

# ----------------------------------------------------------------------------
# 遇見 Rusty
# ----------------------------------------------------------------------------
label encounter_rusty:
    show rusty normal at center
    rusty "嘿！是在進行安全檢查嗎？"
    rusty "（小聲）還是說... 你累了？如果你睡著了，我會幫你守著，不讓別人隨便『借用』你的錢包的！"
    $ track_affection("rusty", 5)
    jump end_time_period

# ----------------------------------------------------------------------------
# 遇見 Py
# ----------------------------------------------------------------------------
label encounter_py:
    show py normal at center
    py "（打了個哈欠，直接擠在長椅另一頭）"
    py "這才對嘛。生活就該像我的代碼一樣，能坐著絕對不站著，能躺著絕對不坐著。"
    py "縮排四格，給我留點位置。"
    $ track_affection("py", 5)
    jump end_time_period

# ============================================================================
# 深夜睡眠系統
# ============================================================================

label execute_sleep_in_plaza:
    scene bg plaza_night
    narrator "深夜的廣場安靜得只能聽到資料流動的嗡鳴聲。"
    narrator "周圍的溫度調節到了最適合睡眠的數值。"
    narrator "你不自覺地閉上了眼睛，在長椅上陷入了沉睡..."
    
    scene black with fade
    pause 3.0
    
    # 睡覺時被發現的隨機小劇情
    $ finder = random.choice(["cee", "jawa", "rusty", "py", "npc"])
    jump expression f"sleep_found_by_{finder}"

label sleep_found_by_cee:
    cee "（腳步聲停在你面前）"
    if mastery_cee < 50:
        cee "偵測到未定義物體。型別：流浪漢？"
        cee "不。是那個 void* 指標。"
    else:
        cee "（輕輕幫你把外套拉好）資料已緩存。晚安。"
    jump sleep_to_morning

label sleep_found_by_jawa:
    jawa "（輕微的嘆息聲）"
    jawa "違反了《源界安居條例》... 但遺棄的物件不應被隨意清理。"
    jawa "（放下了一條薄毯子，上面貼著規格標籤）"
    jump sleep_to_morning

label sleep_found_by_rusty:
    rusty "（驚呼）哇！他怎麼睡在這裡！萬一被當成垃圾回收了怎麼辦！"
    rusty "我得在這裡守著... 這是不可變借用... 直到他醒來..."
    jump sleep_to_morning

label sleep_found_by_py:
    py "謔，這傢伙比我還能睡。"
    py "（在你旁邊拍了一張照片）這絕對是我這週見過最 Pythonic 的場景。自然、隨性。"
    jump sleep_to_morning

label sleep_found_by_npc:
    "路人 NPC" "快看，廣場上又多了一個被代碼折磨到神智不清的傢伙。"
    jump sleep_to_morning

label sleep_to_morning:
    scene black
    pause 2.0
    narrator "當模擬陽光的溫度再次觸碰你的皮膚時，你醒了過來。"
    
    # 睡醒後自動推進時間到清晨
    jump end_time_period
