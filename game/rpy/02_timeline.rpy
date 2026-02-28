# ============================================================================
# 源界 (Source Realm) - 02: 並行時間線系統
# ============================================================================

# ============================================================================
# 1. 時間線數據結構
# ============================================================================

# 時間線定義（每個時段的可用選項和事件）
init python:
    # 時間線數據：每個 ST 範圍的事件安排
    timeline_data = {
        "ST_00-01": {
            "available_lines": ["prologue"],  # 只有序章
            "cee_event": None,
            "jawa_event": None,
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_01-03": {
            "available_lines": ["cee"],  # Cee 線開啟
            "cee_event": "C_01",
            "jawa_event": None,  # Jawa 在處理自己的事，玩家無法介入
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_03-05": {
            "available_lines": ["jawa"],  # Jawa 線開啟
            "cee_event": None,  # 自動推進
            "jawa_event": "J_01",
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_05-07": {
            "available_lines": ["cee"],
            "cee_event": "C_02",
            "jawa_event": "GC_PAUSE",  # Jawa GC 暫停
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_07-09": {
            "available_lines": ["jawa"],
            "cee_event": None,  # 自動推進 C_03 評估
            "jawa_event": "J_02",
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_09-12": {
            "available_lines": ["cee", "jawa"],  # 玩家可選擇
            "cee_event": "C_04",
            "jawa_event": "J_03",
            "shared_event": "RACE_CONDITION",  # 共同事件
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_12-15": {
            "available_lines": ["jawa"],
            "cee_event": None,  # 自動推進
            "jawa_event": "J_04",
            "shared_event": None,
            "is_holiday": True,
            "holiday_id": "holiday_A"  # Jawa 假日
        },
        "ST_15-18": {
            "available_lines": ["cee"],
            "cee_event": "C_05",
            "jawa_event": None,  # 自動推進
            "shared_event": None,
            "is_holiday": True,
            "holiday_id": "holiday_B"  # Cee 假日
        },
        "ST_18-21": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_06",
            "jawa_event": "J_05",
            "shared_event": "LANGUAGE_DEBATE",  # 語言辯論
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_21-25": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_07",
            "jawa_event": "J_06",
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_25-29": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_08",
            "jawa_event": "J_07",
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_29-33": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_09",
            "jawa_event": "J_08",
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_33-36": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "END_SEQUENCE",  # Cee 終章
            "jawa_event": "J_09",  # Jawa 終章
            "shared_event": None,
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_36-38": {
            "available_lines": ["ending"],  # 結局評估
            "cee_event": None,
            "jawa_event": None,
            "shared_event": "ENDING_EVALUATION",
            "is_holiday": False,
            "holiday_id": None
        },
        "ST_38+": {
            "available_lines": ["ending"],
            "cee_event": None,
            "jawa_event": None,
            "shared_event": "BAD_END_A_CHECK",
            "is_holiday": False,
            "holiday_id": None
        }
    }

# ============================================================================
# 2. 當前時間段追蹤
# ============================================================================

default current_time_period = "ST_00-01"

# 玩家選擇的線（在該時間段）
default chosen_line = "none"

# 是否已處理當前時間段
default time_period_processed = False

# ============================================================================
# 3. 時間線系統函數
# ============================================================================

init python:
    def get_current_time_period():
        """根據 source_time 返回當前時間段"""
        st = store.source_time

        if st < 1:
            return "ST_00-01"
        elif st < 3:
            return "ST_01-03"
        elif st < 5:
            return "ST_03-05"
        elif st < 7:
            return "ST_05-07"
        elif st < 9:
            return "ST_07-09"
        elif st < 12:
            return "ST_09-12"
        elif st < 15:
            return "ST_12-15"
        elif st < 18:
            return "ST_15-18"
        elif st < 21:
            return "ST_18-21"
        elif st < 25:
            return "ST_21-25"
        elif st < 29:
            return "ST_25-29"
        elif st < 33:
            return "ST_33-36"
        elif st < 36:
            return "ST_36-38"
        else:
            return "ST_38+"

    def get_time_period_data(period):
        """獲取時間段數據"""
        return timeline_data.get(period, {})

    def get_available_lines(period):
        """獲取當前時間段可用的線"""
        data = get_time_period_data(period)
        return data.get("available_lines", [])

    def get_cee_event(period):
        """獲取 Cee 線事件"""
        data = get_time_period_data(period)
        return data.get("cee_event")

    def get_jawa_event(period):
        """獲取 Jawa 線事件"""
        data = get_time_period_data(period)
        return data.get("jawa_event")

    def get_shared_event(period):
        """獲取共同事件"""
        data = get_time_period_data(period)
        return data.get("shared_event")

    def is_holiday_period(period):
        """檢查是否是假日時段"""
        data = get_time_period_data(period)
        return data.get("is_holiday", False)

    def get_holiday_id(period):
        """獲取假日 ID"""
        data = get_time_period_data(period)
        return data.get("holiday_id")

    def advance_time_to_next_period():
        """推進到下一個時間段"""
        current = get_current_time_period()

        # 根據當前時間段計算下一個
        period_order = [
            "ST_00-01", "ST_01-03", "ST_03-05", "ST_05-07", "ST_07-09",
            "ST_09-12", "ST_12-15", "ST_15-18", "ST_18-21", "ST_21-25",
            "ST_25-29", "ST_29-33", "ST_33-36", "ST_36-38", "ST_38+"
        ]

        try:
            current_index = period_order.index(current)
            if current_index + 1 < len(period_order):
                next_period = period_order[current_index + 1]
                # 根據下一個時間段的起點設置 ST
                next_st_value = float(next_period.split("_")[1].split("-")[0])
                set_source_time(next_st_value)
                return True
        except ValueError:
            pass

        return False

    def process_player_absent_effects():
        """處理玩家不在場時的影響"""
        current = get_current_time_period()

        # 如果玩家選擇了某條線，另一條線的事件會自動推進
        if store.chosen_line == "cee":
            # Jawa 線自動推進
            jawa_event = get_jawa_event(current)
            if jawa_event:
                process_auto_advance_jawa(jawa_event)

        elif store.chosen_line == "jawa":
            # Cee 線自動推進
            cee_event = get_cee_event(current)
            if cee_event:
                process_auto_advance_cee(cee_event)

        # 處理共同事件（如果玩家沒有親身參與）
        shared_event = get_shared_event(current)
        if shared_event and not store.player_participated:
            process_shared_event_autonomous(shared_event)

    def process_auto_advance_cee(event_id):
        """處理 Cee 線的自動推進"""
        # 根據事件 ID 進行相應的自動推進
        # 自動推進不會提升關係狀態
        if event_id and event_id != "None":
            # 標記事件為自動推進完成
            chapter_status = event_id.lower() + "_status"
            set_chapter_status(event_id.lower(), "skipped")

            # Cee 可能會有一些評論（在玩家回來後）
            pass

    def process_auto_advance_jawa(event_id):
        """處理 Jawa 線的自動推進"""
        if event_id and event_id != "None":
            # 標記事件為自動推進完成
            chapter_status = event_id.lower() + "_status"
            set_chapter_status(event_id.lower(), "skipped")

            # Jawa 繼續處理契約局的事務
            pass

    def process_shared_event_autonomous(event_id):
        """處理共同事件的自主推進（玩家不在場）"""
        if event_id == "RACE_CONDITION":
            # 競態條件在玩家不在場時自動解決（可能不是最優解）
            pass
        elif event_id == "LANGUAGE_DEBATE":
            # 語言辯論在玩家不在場時持續
            pass

# ============================================================================
# 4. 時間選擇菜單 - 重新設計為情感化選擇
# ============================================================================

label time_choice_menu:
    # 顯示當前時間信息（更具體）
    $ current = get_current_time_period()
    $ available = get_available_lines(current)
    $ cee_event = get_cee_event(current)
    $ jawa_event = get_jawa_event(current)
    $ shared = get_shared_event(current)
    $ holiday = is_holiday_period(current)

    # 更新當前時間段
    $ current_time_period = current
    $ time_period_processed = False

    # 根據時間段顯示不同的背景
    if current in ["ST_00-01", "ST_01-03"]:
        scene bg plaza_morning
        $ time_description = "第一天清晨"
    elif current in ["ST_03-05", "ST_05-07"]:
        scene bg plaza_noon
        $ time_description = "第一天中午"
    elif current in ["ST_07-09", "ST_09-12"]:
        scene bg plaza_afternoon
        $ time_description = "第一天下午"
    elif current in ["ST_12-15", "ST_15-18"]:
        scene bg plaza_evening
        $ time_description = "第一天傍晚"
    else:
        scene bg plaza_night
        $ time_description = "第一天晚上"

    # 更具體的時間描述
    narrator "源界時間：[time_description]"

    if holiday:
        narrator "⚠️ 假日時段 - 你可以選擇休息或與角色互動"

    # 顯示各線的狀態（情感化描述）
    if cee_event:
        if cee_relationship == "FUNCTIONAL":
            narrator "記憶倉庫：Cee 正在[cee_event]，她似乎習慣你的幫助了"
        elif cee_relationship in ["RELIABLE", "RESONANT"]:
            narrator "記憶倉庫：Cee 正在[cee_event]，看到你會很開心"
        else:
            narrator "記憶倉庫：Cee 正在[cee_event]，她需要幫助"

    if jawa_event:
        if jawa_relationship == "VERIFIED":
            narrator "契約局：Jawa 正在[jawa_event]，她尊重你的意見"
        elif jawa_relationship in ["TRUSTED", "SYNCHRONIZED"]:
            narrator "契約局：Jawa 正在[jawa_event]，她很信任你"
        else:
            narrator "契約局：Jawa 正在[jawa_event]，她需要建議"

    if shared:
        narrator "⚠️ 重要事件：[shared]正在發生，建議盡快前往"

    narrator "你站在資訊廣場，思考下一步..."

    # 主選擇菜單
    menu:
        "去記憶倉庫找 Cee" if cee_event:
            $ chosen_line = "cee"
            $ current_line = "cee"
            $ player_participated = True
            $ current_cee_event_id = cee_event
            jump execute_cee_chapter_entry

        "去契約局找 Jawa" if jawa_event:
            $ chosen_line = "jawa"
            $ current_line = "jawa"
            $ player_participated = True
            $ current_jawa_event_id = jawa_event
            jump execute_jawa_chapter_entry

        "前往共同事件" if shared:
            $ chosen_line = "shared"
            $ current_line = "shared"
            $ player_participated = True
            $ current_shared_event_id = shared
            jump execute_shared_event_entry

        "在廣場休息一下 - 思考目前的情況":
            $ chosen_line = "rest"
            jump execute_rest

        "看看其他地方 - 漫步源界":
            $ chosen_line = "explore"
            jump execute_explore

label execute_cee_chapter_entry:
    jump execute_cee_chapter

label execute_jawa_chapter_entry:
    jump execute_jawa_chapter

label execute_shared_event_entry:
    jump execute_shared_event

label execute_holiday_entry:
    jump execute_holiday

label execute_rest:
    # 休息選項：根據時間和關係狀態顯示不同內容
    scene black

    narrator "你決定在資訊廣場休息一下..."

    # 根據時間段顯示不同的氛圍描述
    python:
        current = get_current_time_period()
        time_description = ""

        if current in ["ST_00-01", "ST_01-03"]:
            time_description = "晨光"
        elif current in ["ST_03-05", "ST_05-07"]:
            time_description = "午後"
        elif current in ["ST_07-09", "ST_09-12"]:
            time_description = "下午"
        elif current in ["ST_12-15", "ST_15-18"]:
            time_description = "傍晚"
        else:
            time_description = "夜裡"

    narrator "[time_description]的微風輕輕吹過..."

    # 根據關係狀態顯示不同的思考內容
    if cee_relationship == "FUNCTIONAL" and jawa_relationship == "VERIFIED":
        narrator "Cee 似乎習慣了你的幫助。Jawa 開始尊重你的意見。"
    elif cee_relationship in ["RELIABLE", "RESONANT"]:
        narrator "想到 Cee，你心中湧起一種信任感..."
    elif jawa_relationship in ["TRUSTED", "SYNCHRONIZED"]:
        narrator "Jawa 的嚴謹中帶著一絲溫柔..."

    pause 2.0

    narrator "休息讓你思路更清晰了。"

    # 標記時間段已處理
    $ time_period_processed = True

    jump end_time_period

label execute_explore:
    # 探索選項：漫步源界
    scene black

    narrator "你決定到處走走，探索源界的其他角落..."

    # 根據時間段顯示不同的探索場景
    python:
        current = get_current_time_period()
        exploration_description = ""

        if current in ["ST_00-01", "ST_01-03"]:
            exploration_description = "清晨的源界安靜而神秘"
        elif current in ["ST_03-05", "ST_05-07"]:
            exploration_description = "午後的街道上，各族群的人來來往往"
        elif current in ["ST_07-09", "ST_09-12"]:
            exploration_description = "下午的倉庫區，聽到傳送帶的運轉聲"
        elif current in ["ST_12-15", "ST_15-18"]:
            exploration_description = "傍晚的廣場，燈光漸漸亮起"
        else:
            exploration_description = "夜裡的源界，星光從虛空中灑落"

    narrator "[exploration_description]。"

    # 根據已探索的章節顯示不同的發現
    if store.chapter_status.get("C_01") == "completed":
        narrator "你路過記憶倉庫，遠遠看到 Cee 在整理書籍..."
    if store.chapter_status.get("J_01") == "completed":
        narrator "你路過契約局，聽到 Jawa 正在和某個居民爭論合約條款..."

    narrator "雖然沒有深入接觸，但你對源界有了更深的了解。"

    # 標記時間段已處理
    $ time_period_processed = True

    jump end_time_period

label observe_auto_advance:
    # 觀察自動推進的結果
    call process_player_absent_effects

    # 顯示自動推進的結果摘要
    scene bg observation

    narrator "你選擇了在這個時段旁觀..."

    python hide:
        current = get_current_time_period()
        cee_event = get_cee_event(current)
        jawa_event = get_jawa_event(current)

    if cee_event and chosen_line != "cee":
        narrator "Cee 線的 [cee_event] 已經自動推進。"

    if jawa_event and chosen_line != "jawa":
        narrator "Jawa 線的 [jawa_event] 已經自動推進。"

    # 標記時間段已處理
    $ time_period_processed = True

    # 繼續到下一個時間段
    jump end_time_period

label end_time_period:
    # 更新現實時間計數器
    $ reality_weeks_passed += 1

    # 檢查是否達成任何線的 FUNCTIONAL 狀態
    python hide:
        if (store.cee_relationship in ["RELIABLE", "RESONANT", "PARTNER", "CLOSE_ALLY"] or
            store.jawa_relationship in ["TRUSTED", "SYNCHRONIZED", "PARTNER", "DEEP_ALLY"]):
            store.any_line_completed_functional = True

    # 檢查是否需要觸發結局
    $ current_ending = check_ending_conditions()

    if current_ending != "none":
        jump trigger_ending

    # 推進到下一個時間段
    $ advance_time_to_next_period()

    # 如果還沒到結局，繼續時間選擇
    if source_time < 38:
        jump time_choice_menu
    else:
        jump check_ending_manually

label check_ending_manually:
    $ current_ending = check_ending_conditions()
    if current_ending == "none":
        jump ending_default
    jump trigger_ending

label trigger_ending:
    $ record_ending(current_ending)

    if current_ending == "true_end":
        jump ending_true
    elif current_ending == "good_end":
        jump ending_good
    elif current_ending == "normal_end":
        jump ending_normal
    elif current_ending == "bad_end_a":
        jump ending_bad_a
    else:
        jump ending_default

# ============================================================================
# 5. 章節執行入口
# ============================================================================

label execute_cee_chapter:
    # 從全局變量獲取事件 ID
    if current_cee_event_id == "C_01":
        jump cee_C01_start
    elif current_cee_event_id == "C_02":
        jump cee_C02_start
    elif current_cee_event_id == "C_03":
        jump cee_C03_start
    elif current_cee_event_id == "C_04":
        jump cee_C04_start
    elif current_cee_event_id == "C_05":
        jump cee_C05_start
    elif current_cee_event_id == "C_06":
        jump cee_C06_start
    elif current_cee_event_id == "C_07":
        jump cee_C07_start
    elif current_cee_event_id == "C_08":
        jump cee_C08_start
    elif current_cee_event_id == "C_09":
        jump cee_C09_start
    elif current_cee_event_id == "END_SEQUENCE":
        jump cee_end_sequence
    else:
        jump time_choice_menu

label execute_jawa_chapter:
    # 從全局變量獲取事件 ID
    if current_jawa_event_id == "J_01":
        jump jawa_J01_start
    elif current_jawa_event_id == "J_02":
        jump jawa_J02_start
    elif current_jawa_event_id == "J_03":
        jump jawa_J03_start
    elif current_jawa_event_id == "J_04":
        jump jawa_J04_start
    elif current_jawa_event_id == "J_05":
        jump jawa_J05_start
    elif current_jawa_event_id == "J_06":
        jump jawa_J06_start
    elif current_jawa_event_id == "J_07":
        jump jawa_J07_start
    elif current_jawa_event_id == "J_08":
        jump jawa_J08_start
    elif current_jawa_event_id == "J_09":
        jump jawa_J09_start
    else:
        jump time_choice_menu

label execute_shared_event:
    # 從全局變量獲取事件 ID
    if current_shared_event_id == "RACE_CONDITION":
        jump shared_race_condition
    elif current_shared_event_id == "LANGUAGE_DEBATE":
        jump shared_language_debate
    elif current_shared_event_id == "ENDING_EVALUATION":
        jump shared_ending_evaluation
    else:
        jump time_choice_menu

label execute_holiday:
    # 從全局變量獲取假日 ID
    if current_holiday_id == "holiday_A":
        jump holiday_A  # Jawa 假日
    elif current_holiday_id == "holiday_B":
        jump holiday_B  # Cee 假日
    else:
        jump time_choice_menu
