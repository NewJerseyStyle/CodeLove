# ============================================================================
# 源界 (Source Realm) - 04: 後果系統
# ============================================================================

# ============================================================================
# 1. 後果系統數據結構
# ============================================================================

init python:
    # 後果等級定義
    consequence_levels = {
        "none": {
            "name": "無",
            "color": "#95A5A6",
            "description": "沒有任何後果",
            "affected_characters": [],
            "duration": 0,
            "impact_description": ""
        },
        "minor": {
            "name": "輕微",
            "color": "#F1C40F",
            "description": "只影響當前任務",
            "affected_characters": [],
            "duration": 0,
            "impact_description": "任務失敗可重試"
        },
        "moderate": {
            "name": "中等",
            "color": "#E67E22",
            "description": "影響 Cee 的工作空間，需要時間清理",
            "affected_characters": ["cee"],
            "duration": 3,  # ST 單位
            "impact_description": "Cee 的可用時間減少，影響後續互動機會"
        },
        "severe": {
            "name": "嚴重",
            "color": "#E74C3C",
            "description": "影響附近其他角色",
            "affected_characters": ["cee", "rusty", "jawa"],
            "duration": 5,
            "impact_description": "其他 NPC 受到波及，影響支線進度"
        },
        "fatal": {
            "name": "致命",
            "color": "#C0392B",
            "description": "源界局部區域崩潰",
            "affected_characters": ["all"],
            "duration": 10,
            "impact_description": "觸發緊急事件，所有角色進入危機狀態"
        }
    }

    # 後果類型定義（具體錯誤情境）
    consequence_types = {
        "segmentation_fault": {
            "name": "段錯誤",
            "default_level": "moderate",
            "description": "訪問無效位址",
            "typical_scene": "Cee 操作時觸發"
        },
        "memory_leak": {
            "name": "記憶體洩漏",
            "default_level": "moderate",
            "description": "未釋放已分配的記憶體",
            "typical_scene": "Cee 使用 malloc 後忘記 free"
        },
        "buffer_overflow": {
            "name": "緩衝區溢出",
            "default_level": "severe",
            "description": "寫入超出陣列邊界",
            "typical_scene": "Cee 忽略邊界檢查"
        },
        "null_pointer": {
            "name": "空指標",
            "default_level": "minor",
            "description": "使用未初始化的指標",
            "typical_scene": "Cee 嘗試存取空指標"
        },
        "race_condition": {
            "name": "競態條件",
            "default_level": "severe",
            "description": "多執行緒同時存取共享資源",
            "typical_scene": "Cee 和 Jawa 同時更新同一記錄"
        },
        "type_mismatch": {
            "name": "型別不符",
            "default_level": "minor",
            "description": "錯誤的型別轉換或使用",
            "typical_scene": "玩家用 Java 概念指揮 Cee"
        },
        "garbage_collection_overflow": {
            "name": "GC 溢出",
            "default_level": "moderate",
            "description": "Jawa GC 暫停時間過長",
            "typical_scene": "Jawa 在關鍵時刻進入長時間 GC"
        }
    }

# ============================================================================
# 2. 後果系統變量
# ============================================================================

# 當前後果列表（可能有多個同時存在）
default active_consequences = []

# 後果歷史記錄
default consequence_history = []

# 角色受影響狀態
default cee_consequence_state = "normal"  # normal, affected, recovering
default jawa_consequence_state = "normal"
default rusty_consequence_state = "normal"
default golly_consequence_state = "normal"

# ============================================================================
# 3. 後果系統函數
# ============================================================================

init python:
    def apply_consequence(consequence_type, level=None, context=""):
        """應用後果"""
        # 獲取後果類型定義
        type_def = consequence_types.get(consequence_type, {})

        if not type_def:
            return False

        # 確定後果等級
        if level is None:
            level = type_def.get("default_level", "minor")

        # 獲取後果等級定義
        level_def = consequence_levels.get(level, {})

        if not level_def:
            return False

        # 創建後果實例
        consequence_id = consequence_type + "_" + str(store.source_time)
        consequence_instance = {
            "id": consequence_id,
            "type": consequence_type,
            "level": level,
            "context": context,
            "start_time": store.source_time,
            "duration": level_def.get("duration", 0),
            "affected_characters": level_def.get("affected_characters", [])
        }

        # 添加到活躍後果列表
        store.active_consequences.append(consequence_instance)

        # 更新全局後果等級（取最高的）
        update_global_consequence_level()

        # 更新角色受影響狀態
        update_character_consequence_states()

        # 記錄到歷史
        store.consequence_history.append(consequence_instance.copy())

        # 更新遊戲狀態
        update_consequence_effects(level)

        return True

    def clear_consequence(consequence_id):
        """清除特定後果"""
        store.active_consequences = [
            c for c in store.active_consequences
            if c["id"] != consequence_id
        ]

        # 更新全局後果等級
        update_global_consequence_level()

        # 更新角色受影響狀態
        update_character_consequence_states()

    def clear_all_consequences():
        """清除所有後果"""
        store.active_consequences = []
        store.current_consequence = "none"
        update_character_consequence_states()

    def update_global_consequence_level():
        """更新全局後果等級（取活躍後果中最高等級）"""
        if not store.active_consequences:
            store.current_consequence = "none"
            return

        # 等級優先順序
        level_priority = ["none", "minor", "moderate", "severe", "fatal"]

        max_level = "none"
        for consequence in store.active_consequences:
            current_level = consequence["level"]
            if level_priority.index(current_level) > level_priority.index(max_level):
                max_level = current_level

        store.current_consequence = max_level

    def update_character_consequence_states():
        """更新角色受影響狀態"""
        # 重置所有角色狀態
        store.cee_consequence_state = "normal"
        store.jawa_consequence_state = "normal"
        store.rusty_consequence_state = "normal"
        store.golly_consequence_state = "normal"

        # 根據活躍後果更新角色狀態
        for consequence in store.active_consequences:
            affected = consequence["affected_characters"]
            level = consequence["level"]

            for char in affected:
                if char == "cee":
                    if store.cee_consequence_state != "affected":
                        store.cee_consequence_state = "affected"
                elif char == "jawa":
                    if store.jawa_consequence_state != "affected":
                        store.jawa_consequence_state = "affected"
                elif char == "rusty":
                    if store.rusty_consequence_state != "affected":
                        store.rusty_consequence_state = "affected"
                elif char == "golly":
                    if store.golly_consequence_state != "affected":
                        store.golly_consequence_state = "affected"
                elif char == "all":
                    # 影響所有角色
                    store.cee_consequence_state = "affected"
                    store.jawa_consequence_state = "affected"
                    store.rusty_consequence_state = "affected"
                    store.golly_consequence_state = "affected"

    def advance_consequence_time(amount):
        """推進後果時間"""
        consequences_to_clear = []

        for consequence in store.active_consequences:
            consequence["duration"] -= amount

            if consequence["duration"] <= 0:
                consequences_to_clear.append(consequence["id"])

        # 清除已結束的後果
        for consequence_id in consequences_to_clear:
            clear_consequence(consequence_id)

    def get_consequence_description(consequence_id):
        """獲取後果描述"""
        for consequence in store.active_consequences:
            if consequence["id"] == consequence_id:
                return consequence_types.get(consequence["type"], {}).get("description", "")
        return ""

    def get_active_consequences():
        """獲取活躍後果列表"""
        return store.active_consequences.copy()

    def is_character_affected(character):
        """檢查角色是否受影響"""
        character_states = {
            "cee": store.cee_consequence_state,
            "jawa": store.jawa_consequence_state,
            "rusty": store.rusty_consequence_state,
            "golly": store.golly_consequence_state
        }

        return character_states.get(character, "normal") == "affected"

# ============================================================================
# 4. 後果顯示系統
# ============================================================================

label show_consequence_notification(consequence_type, level):
    # 顯示後果通知
    python hide:
        type_def = consequence_types.get(consequence_type, {})
        level_def = consequence_levels.get(level, {})

        name = level_def.get("name", "未知")
        description = type_def.get("description", "")
        impact = level_def.get("impact_description", "")

    scene black
    narrator "▶ [name] 後果"

    narrator "[description]"

    if impact:
        narrator "影響：[impact]"

    return
