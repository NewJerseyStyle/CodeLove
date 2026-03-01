# ============================================================================
# 源界 (Source Realm) - 02: 並行時間線系統
# ============================================================================

# ============================================================================
# 1. 時間線數據結構
# ============================================================================

init python:
    # 時間線數據：每個 ST 範圍的事件安排
    timeline_data = {
        "ST_00-01": {
            "available_lines": ["prologue"],
            "cee_event": None,
            "jawa_event": None,
            "shared_event": None,
            "is_holiday": False
        },
        "ST_01-03": {
            "available_lines": ["cee"],
            "cee_event": "C_01",
            "jawa_event": None,
            "shared_event": None,
            "is_holiday": False
        },
        "ST_03-05": {
            "available_lines": ["jawa"],
            "cee_event": None,
            "jawa_event": "J_01",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_05-07": {
            "available_lines": ["cee"],
            "cee_event": "C_02",
            "jawa_event": "GC_PAUSE",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_07-09": {
            "available_lines": ["jawa"],
            "cee_event": None,
            "jawa_event": "J_02",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_09-12": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_04",
            "jawa_event": "J_03",
            "shared_event": "RACE_CONDITION",
            "is_holiday": False
        },
        "ST_12-15": {
            "available_lines": ["jawa"],
            "cee_event": None,
            "jawa_event": "J_04",
            "shared_event": None,
            "is_holiday": True,
            "holiday_id": "holiday_A"
        },
        "ST_15-18": {
            "available_lines": ["cee"],
            "cee_event": "C_05",
            "jawa_event": None,
            "shared_event": None,
            "is_holiday": True,
            "holiday_id": "holiday_B"
        },
        "ST_18-21": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_06",
            "jawa_event": "J_05",
            "shared_event": "LANGUAGE_DEBATE",
            "is_holiday": False
        },
        "ST_21-25": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_07",
            "jawa_event": "J_06",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_25-29": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_08",
            "jawa_event": "J_07",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_29-33": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_09",
            "jawa_event": "J_08",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_33-36": {
            "available_lines": ["cee", "jawa"],
            "cee_event": "C_09",
            "jawa_event": "J_09",
            "shared_event": None,
            "is_holiday": False
        },
        "ST_36-38": {
            "available_lines": ["ending"],
            "cee_event": None,
            "jawa_event": None,
            "shared_event": "ENDING_EVALUATION",
            "is_holiday": False
        },
        "ST_38+": {
            "available_lines": ["ending"],
            "cee_event": None,
            "jawa_event": None,
            "shared_event": "BAD_END_A_CHECK",
            "is_holiday": False
        }
    }

# ============================================================================
# 2. 當前時間段追蹤
# ============================================================================

default current_time_period = "ST_00-01"
default chosen_line = "none"
default time_period_processed = False

# ============================================================================
# 3. 時間線系統函數
# ============================================================================

init python:
    def get_current_time_period():
        st = store.source_time
        if st < 1: return "ST_00-01"
        elif st < 3: return "ST_01-03"
        elif st < 5: return "ST_03-05"
        elif st < 7: return "ST_05-07"
        elif st < 9: return "ST_07-09"
        elif st < 12: return "ST_09-12"
        elif st < 15: return "ST_12-15"
        elif st < 18: return "ST_15-18"
        elif st < 21: return "ST_18-21"
        elif st < 25: return "ST_21-25"
        elif st < 29: return "ST_25-29"
        elif st < 33: return "ST_29-33"
        elif st < 36: return "ST_33-36"
        elif st < 38: return "ST_36-38"
        else: return "ST_38+"

    def get_cee_event(period):
        return timeline_data.get(period, {}).get("cee_event")

    def get_jawa_event(period):
        return timeline_data.get(period, {}).get("jawa_event")

    def advance_time_to_next_period():
        current = get_current_time_period()
        period_order = [
            "ST_00-01", "ST_01-03", "ST_03-05", "ST_05-07", "ST_07-09",
            "ST_09-12", "ST_12-15", "ST_15-18", "ST_18-21", "ST_21-25",
            "ST_25-29", "ST_29-33", "ST_33-36", "ST_36-38", "ST_38+"
        ]
        try:
            idx = period_order.index(current)
            if idx + 1 < len(period_order):
                next_period = period_order[idx + 1]
                next_st = float(next_period.split("_")[1].split("-")[0])
                store.source_time = next_st
                return True
        except: pass
        return False

# ============================================================================
# 4. 時間選擇菜單
# ============================================================================

label time_choice_menu:
    $ current = get_current_time_period()
    $ current_time_period = current
    $ time_period_processed = False

    python:
        st = store.source_time
        day_count = int(st // 15) + 1
        st_in_day = st % 15

        if st >= 36:
            time_description = "系統不穩定時段"
            renpy.show("bg source_realm_core")
            renpy.say("narrator", "你感到空氣中的數據粒子變得異常狂暴，遠處的空間隱約透出裂縫。")
        elif st_in_day < 3:
            time_description = f"第 {day_count} 天 清晨"
            renpy.show("bg plaza_morning")
        elif st_in_day < 7:
            time_description = f"第 {day_count} 天 正午"
            renpy.show("bg plaza_noon")
        elif st_in_day < 10:
            time_description = f"第 {day_count} 天 下午"
            renpy.show("bg plaza_afternoon")
        elif st_in_day < 13:
            time_description = f"第 {day_count} 天 傍晚"
            renpy.show("bg plaza_evening")
        else:
            time_description = f"第 {day_count} 天 深夜"
            renpy.show("bg plaza_night")

    # 獲取當前重要事件 - 使用 $ 賦值使其在 menu 條件中可見
    $ shared = timeline_data.get(current, {}).get("shared_event")

    narrator "【[time_description]】你站在資訊廣場中央。"

    menu:
        "前往結局評估" if shared == "ENDING_EVALUATION":
            jump execute_shared_event
            
        "前往共同事件：[shared]" if shared and shared != "ENDING_EVALUATION" and shared != "BAD_END_A_CHECK":
            jump execute_shared_event

        "前往記憶倉庫":
            $ chosen_line = "cee"
            jump execute_location_check

        "前往契約局":
            $ chosen_line = "jawa"
            jump execute_location_check

        "在廣場坐一會兒":
            $ chosen_line = "rest"
            jump execute_rest

        "在源界隨處逛逛":
            $ chosen_line = "explore"
            jump execute_explore

label execute_location_check:
    $ current = get_current_time_period()
    # 結局時段 (ST 36+) 封鎖地點進入
    if store.source_time >= 36:
        narrator "源界的核心正在重組，所有區域暫時封鎖。你應該去參與最終評估。"
        jump time_choice_menu

    if chosen_line == "cee":
        $ event = get_cee_event(current)
        if event:
            $ current_cee_event_id = event
            jump execute_cee_chapter_entry
        else:
            # 沒有主線時，有機率觸發日常
            $ chance = renpy.random.random()
            if chance < 0.6:
                jump holiday_B
            else:
                narrator "記憶倉庫現在不對外開放，Cee 似乎不在這裡。"
                jump end_time_period
            
    elif chosen_line == "jawa":
        $ event = get_jawa_event(current)
        if event:
            $ current_jawa_event_id = event
            jump execute_jawa_chapter_entry
        else:
            $ chance = renpy.random.random()
            if chance < 0.6:
                jump holiday_A
            else:
                narrator "契約局的辦事處鎖著門，Jawa 應該在忙別的事。"
                jump end_time_period

label execute_rest:
    python:
        st = store.source_time
        st_in_day = st % 15
        is_late_night = st_in_day >= 13
        # 結局保底判定
        is_end_time = st >= 36
    
    if is_end_time:
        narrator "你感到一股不可抗拒的吸力從源界中心傳來..."
        jump shared_ending_evaluation
    elif is_late_night:
        jump execute_sleep_in_plaza
    else:
        jump execute_plaza_encounter

label end_time_period:
    $ advance_time_to_next_period()
    $ reality_weeks_passed += 1
    $ current_ending = check_ending_conditions()
    if current_ending != "none":
        jump trigger_ending
    jump time_choice_menu

# ============================================================================
# 5. 章節執行入口
# ============================================================================

label execute_cee_chapter_entry:
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
    elif current_cee_event_id == "C_09" or current_cee_event_id == "END_SEQUENCE":
        jump cee_C09_start
    else:
        jump time_choice_menu

label execute_jawa_chapter_entry:
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
    if current_shared_event_id == "RACE_CONDITION":
        jump shared_race_condition
    elif current_shared_event_id == "LANGUAGE_DEBATE":
        jump shared_language_debate
    elif current_shared_event_id == "ENDING_EVALUATION":
        jump shared_ending_evaluation
    elif current_shared_event_id == "BAD_END_A_CHECK":
        jump shared_bad_end_a_check
    else:
        jump time_choice_menu

label execute_explore:
    scene black
    narrator "你決定到處走走，探索源界的其他角落..."
    jump execute_explore_random

label trigger_ending:
    $ record_ending(current_ending)
    if current_ending == "true_end":
        jump ending_true
    elif current_ending == "good_end":
        jump ending_good
    elif current_ending == "normal_end":
        jump ending_normal
    elif current_ending == "bad_end_a":
        jump ending_source_rescue
    else:
        jump ending_default
