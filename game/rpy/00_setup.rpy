# ============================================================================
# 源界 (Source Realm) - 00: 初始化和系統設置
# ============================================================================

# ============================================================================
# 2. 全局變量 - 時間系統
# ============================================================================

# 源界時間 (Source Time, ST)
# ST 00-38 是遊戲主要時段
default source_time = 0

# 時間是否正在流動
default time_flowing = True

# 時間流逝速度（每幀增加多少 ST）
default time_flow_speed = 0.001

# ============================================================================
# 3. 全局變量 - 遊戲狀態
# ============================================================================

# 當前所在線（"prologue", "cee", "jawa", "none"）
default current_line = "prologue"

# 是否在時間選擇菜單
default in_time_menu = False

# 玩家是否參與了當前事件
default player_participated = False

# ============================================================================
# 4. 全局變量 - 後果系統
# ============================================================================

# 當前後果等級（"none", "minor", "moderate", "severe", "fatal"）
default current_consequence = "none"

# 各角色受後果影響的程度
default cee_affected_by_consequence = False
default jawa_affected_by_consequence = False
default rusty_affected_by_consequence = False
default golly_affected_by_consequence = False

# 後果持續時間（ST 單位）
default consequence_duration = 0

# Cee 的可用時間減少量（中等後果影響）
default cee_available_time_reduction = 0

# ============================================================================
# 5. 全局變量 - 算法互動
# ============================================================================

# 玩家選擇的算法方案（用於追蹤和回饋）
default last_algorithm_choice = "none"

# 算法效率提升倍數
default efficiency_multiplier = 1.0

# 是否發生過跨語言指令錯誤
default cross_language_error_occurred = False

# 跨語言錯誤類型（記錄錯誤類型用於教學）
default cross_language_error_type = ""

# 當前正在顯示的後果類型（用於教學卡片）
default current_consequence_type = ""

# 當前教學行（用於循環顯示教學內容）
default current_teaching_line = ""

# 當前反應的角色和後果類型（用於 show_consequence_reaction）
default current_reaction_character = ""
default current_reaction_consequence = ""
default current_reaction_line = ""

# ============================================================================
# 6. 全局變量 - 假日系統
# ============================================================================

# 是否是假日時段
default is_holiday = False

# 當前假日 ID
default current_holiday_id = ""

# 假日選擇（玩家選擇了哪個角色的假日）
default holiday_choice = "none"

# 當前章節事件 ID（用於時間線系統跳轉）
default current_cee_event_id = ""
default current_jawa_event_id = ""
default current_shared_event_id = ""

# 當前結局 ID
default current_ending = "none"

# ============================================================================
# 7. 全局變量 - Bad End A 計時器
# ============================================================================

# 現實時間計數器（阿源在便利店幾週後會發現）
default reality_weeks_passed = 0

# 是否觸發 Bad End A
default bad_end_a_triggered = False

# 是否已完成至少一條線到 FUNCTIONAL 狀態（避免 Bad End A）
default any_line_completed_functional = False

# ============================================================================
# 8. 全局變量 - 章節進度追蹤
# ============================================================================

# Cee 線章節狀態（"unstarted", "in_progress", "completed", "skipped"）
default c_01_status = "unstarted"
default c_02_status = "unstarted"
default c_03_status = "unstarted"
default c_04_status = "unstarted"
default c_05_status = "unstarted"
default c_06_status = "unstarted"
default c_07_status = "unstarted"
default c_08_status = "unstarted"
default c_09_status = "unstarted"

# Jawa 線章節狀態
default j_01_status = "unstarted"
default j_02_status = "unstarted"
default j_03_status = "unstarted"
default j_04_status = "unstarted"
default j_05_status = "unstarted"
default j_06_status = "unstarted"
default j_07_status = "unstarted"
default j_08_status = "unstarted"
default j_09_status = "unstarted"

# 共同事件狀態
default shared_race_condition_status = "unready"

# ============================================================================
# 9. 全局變量 - 結局追蹤
# ============================================================================

# 已觸發的結局列表
default triggered_endings = []

# 最後觸發的結局
default last_ending = "none"

# 是否達成真結局條件（所有角色最高好感度）
default true_end_unlocked = False

# 是否達成好結局條件（兩條語言線都完成）
default good_end_unlocked = False

# ============================================================================
# 10. 系統函數 - 時間管理
# ============================================================================

init python:
    def advance_source_time(amount):
        """推進源界時間"""
        global source_time
        source_time += amount
        return source_time

    def set_source_time(st):
        """設置源界時間"""
        global source_time
        source_time = st

    def get_time_period():
        """根據 ST 返回時段描述"""
        if source_time < 1:
            return "ST 00-01: 序章"
        elif source_time < 3:
            return "ST 01-03"
        elif source_time < 5:
            return "ST 03-05"
        elif source_time < 7:
            return "ST 05-07"
        elif source_time < 9:
            return "ST 07-09"
        elif source_time < 12:
            return "ST 09-12"
        elif source_time < 15:
            return "ST 12-15"
        elif source_time < 18:
            return "ST 15-18"
        elif source_time < 21:
            return "ST 18-21"
        elif source_time < 25:
            return "ST 21-25"
        elif source_time < 29:
            return "ST 29-33"
        elif source_time < 33:
            return "ST 33-36"
        elif source_time < 36:
            return "ST 36-38"
        else:
            return "ST 38+"

# ============================================================================
# 11. 系統函數 - 後果系統
# ============================================================================

init python:
    def apply_consequence(level, affected_characters, duration=0):
        """應用後果"""
        global current_consequence, consequence_duration

        current_consequence = level
        consequence_duration = duration

        # 設置受影響角色
        if "cee" in affected_characters:
            store.cee_affected_by_consequence = True
        if "jawa" in affected_characters:
            store.jawa_affected_by_consequence = True
        if "rusty" in affected_characters:
            store.rusty_affected_by_consequence = True
        if "golly" in affected_characters:
            store.golly_affected_by_consequence = True

        # 中等以上後果減少 Cee 可用時間
        if level == "moderate" or level == "severe":
            store.cee_available_time_reduction = duration * 0.5

        # 更新章節進度（影響後續互動機會）
        update_consequence_effects(level)

    def update_consequence_effects(level):
        """根據後果等級更新遊戲狀態"""
        # 輕微後果：僅影響當前任務
        if level == "minor":
            pass  # 任務失敗可重試，不影響其他

        # 中等後果：影響 Cee 工作空間
        elif level == "moderate":
            store.cee_available_time_reduction += 3  # 減少 3 ST 的互動機會

        # 嚴重後果：波及其他角色
        elif level == "severe":
            store.cee_available_time_reduction += 5
            # 影響其他支線進度（在具體章節中處理）

        # 致命後果：觸發緊急事件
        elif level == "fatal":
            # 觸發緊急事件章節
            pass

    def reduce_consequence_duration(amount):
        """減少後果持續時間"""
        global consequence_duration
        consequence_duration = max(0, consequence_duration - amount)

        # 如果後果結束，重置影響
        if consequence_duration == 0:
            clear_consequence()

    def clear_consequence():
        """清除後果影響"""
        global current_consequence
        current_consequence = "none"

        store.cee_affected_by_consequence = False
        store.jawa_affected_by_consequence = False
        store.rusty_affected_by_consequence = False
        store.golly_affected_by_consequence = False

# ============================================================================
# 12. 系統函數 - 章節進度
# ============================================================================

init python:
    def set_chapter_status(chapter_id, status):
        """設置章節狀態"""
        setattr(store, chapter_id + "_status", status)

    def get_chapter_status(chapter_id):
        """獲取章節狀態"""
        return getattr(store, chapter_id + "_status", "unstarted")

    def complete_chapter(chapter_id):
        """標記章節完成"""
        set_chapter_status(chapter_id, "completed")

    def skip_chapter(chapter_id):
        """跳過章節（玩家不在場時）"""
        set_chapter_status(chapter_id, "skipped")

# ============================================================================
# 13. 系統函數 - 結局判斷
# ============================================================================

init python:
    def check_ending_conditions():
        """檢查結局觸發條件"""
        # 檢查 True End 條件：所有角色最高好感度
        cee_resonant = (store.cee_relationship == "RESONANT")
        jawa_synchronized = (store.jawa_relationship == "SYNCHRONIZED")
        rusty_max = (store.rusty_relationship == "MAX")
        golly_max = (store.golly_relationship == "MAX")

        if cee_resonant and jawa_synchronized and rusty_max and golly_max:
            return "true_end"

        # 檢查 Good End 條件：兩條語言線都完成
        cee_completed = all([
            store.c_01_status == "completed",
            store.c_02_status == "completed",
            store.c_03_status == "completed",
            store.c_04_status == "completed",
            store.c_05_status == "completed",
            store.c_06_status == "completed",
            store.c_07_status == "completed",
            store.c_08_status == "completed",
            store.c_09_status == "completed"
        ])

        jawa_completed = all([
            store.j_01_status == "completed",
            store.j_02_status == "completed",
            store.j_03_status == "completed",
            store.j_04_status == "completed",
            store.j_05_status == "completed",
            store.j_06_status == "completed",
            store.j_07_status == "completed",
            store.j_08_status == "completed",
            store.j_09_status == "completed"
        ])

        if cee_completed and jawa_completed:
            return "good_end"

        # 檢查 Bad End A 條件：沒有任何線達到 FUNCTIONAL
        if not store.any_line_completed_functional and source_time >= 38:
            return "bad_end_a"

        # Normal End：任一語言線完成
        if cee_completed or jawa_completed:
            return "normal_end"

        return "none"

    def record_ending(ending_id):
        """記錄觸發的結局"""
        global last_ending
        last_ending = ending_id

        if ending_id not in store.triggered_endings:
            store.triggered_endings.append(ending_id)

# ============================================================================
# 14. 遊戲初始化
# ============================================================================

label game_start:
    # 設置初始時間
    $ set_source_time(0)

    # 設置初始狀態
    $ current_line = "prologue"
    $ current_consequence = "none"
    $ time_flowing = True

    # 跳轉到序章
    jump prologue_start
