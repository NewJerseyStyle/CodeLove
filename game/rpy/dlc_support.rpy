# ============================================================================
# 源界 (Source Realm) - DLC 支援系統
# ============================================================================
#
# 此文件提供 DLC 擴展所需的介面和鉤子。
# DLC 開發者應參考 docs/DLC_DEVELOPER_GUIDE.md
# ============================================================================

# ============================================================================
# 1. DLC 註冊系統
# ============================================================================

init python:
    # 已註冊的 DLC 列表
    if 'registered_dlcs' not in dir():
        registered_dlcs = []

    # DLC 結局檢查函數列表
    if 'dlc_ending_checkers' not in dir():
        dlc_ending_checkers = []

    # DLC 時間線擴展
    if 'dlc_timeline_extensions' not in dir():
        dlc_timeline_extensions = {}

    def register_dlc(dlc_info):
        """
        註冊 DLC

        dlc_info 應包含:
        - id: DLC 唯一標識符
        - name: DLC 顯示名稱
        - version: 版本號
        - author: 作者
        - description: 描述
        - ending_checker: 結局檢查函數 (可選)
        - timeline_data: 時間線擴展 (可選)
        """
        # 檢查是否已註冊
        for existing in registered_dlcs:
            if existing.get("id") == dlc_info.get("id"):
                return False

        registered_dlcs.append(dlc_info)

        # 註冊結局檢查器
        if "ending_checker" in dlc_info:
            dlc_ending_checkers.append(dlc_info["ending_checker"])

        # 註冊時間線擴展
        if "timeline_data" in dlc_info:
            dlc_timeline_extensions.update(dlc_info["timeline_data"])

        return True

    def get_registered_dlcs():
        """獲取所有已註冊的 DLC"""
        return registered_dlcs

    def is_dlc_installed(dlc_id):
        """檢查 DLC 是否已安裝"""
        for dlc in registered_dlcs:
            if dlc.get("id") == dlc_id:
                return True
        return False

# ============================================================================
# 2. 動態結局系統
# ============================================================================

init python:
    # 是否禁用主線結局強制觸發（DLC 可設置）
    default dlc_disable_main_ending = False

    # DLC 自定義結局時間（超過此時間才觸發結局評估）
    default dlc_custom_ending_threshold = 36

    def check_all_endings():
        """
        檢查所有結局（主線 + DLC）

        返回: 結局 ID 或 "none"
        """
        # 1. 先檢查 DLC 結局
        for checker in dlc_ending_checkers:
            result = checker()
            if result and result != "none":
                return result

        # 2. 檢查是否應延後主線結局
        if dlc_disable_main_ending:
            # DLC 請求延後結局
            if store.source_time < dlc_custom_ending_threshold:
                return "none"

        # 3. 使用主線結局邏輯
        return check_ending_conditions()

    def should_force_ending():
        """
        檢查是否應該強制進入結局評估

        用於 time_choice_menu 中判斷是否顯示結局選項
        """
        # 如果有 DLC 禁用主線結局，使用 DLC 閾值
        if dlc_disable_main_ending:
            return store.source_time >= dlc_custom_ending_threshold

        # 否則使用主線邏輯 (ST 36+)
        return store.source_time >= 36

    def get_available_endings():
        """
        獲取當前可用的結局列表

        返回: [(ending_id, ending_name, is_unlocked), ...]
        """
        endings = [
            ("true_end", "真結局：仿生紀元", store.true_end_unlocked),
            ("good_end", "好結局：源界守護者", store.good_end_unlocked),
            ("normal_end", "普通結局：專才之路", True),
            ("bad_end_a", "壞結局：現實重擊", not store.any_line_completed_functional),
        ]

        # 添加 DLC 結局
        for dlc in registered_dlcs:
            if "endings" in dlc:
                for ending_id, ending_info in dlc["endings"].items():
                    endings.append((
                        ending_id,
                        ending_info.get("name", ending_id),
                        ending_info.get("condition", lambda: True)()
                    ))

        return endings

# ============================================================================
# 3. 時間線擴展系統
# ============================================================================

init python:
    def get_extended_timeline():
        """
        獲取擴展後的時間線（主線 + DLC）
        """
        # 複製主時間線
        extended = dict(timeline_data)

        # 添加 DLC 擴展
        extended.update(dlc_timeline_extensions)

        return extended

    def get_available_lines_for_period(period):
        """
        獲取指定時間段可用的故事線
        """
        timeline = get_extended_timeline()
        period_data = timeline.get(period, {})

        lines = list(period_data.get("available_lines", []))

        # 添加 DLC 故事線
        for dlc in registered_dlcs:
            dlc_id = dlc.get("id")
            if dlc_id and dlc_id not in lines:
                # 檢查 DLC 是否在此時間段有事件
                if f"{dlc_id}_event" in period_data:
                    lines.append(dlc_id)

        return lines

# ============================================================================
# 4. 角色擴展系統
# ============================================================================

init python:
    # DLC 角色註冊表
    if 'dlc_characters' not in dir():
        dlc_characters = {}

    def register_dlc_character(char_id, char_info):
        """
        註冊 DLC 角色

        char_info 應包含:
        - name: 顯示名稱
        - color: 對話框顏色
        - language: 語言原型
        - traits: 語言特性
        - relationship_states: 關係狀態列表
        """
        dlc_characters[char_id] = char_info

        # 創建關係變量（如果不存在）
        var_name = f"{char_id}_relationship"
        if not hasattr(store, var_name):
            setattr(store, var_name, "UNMET")

    def get_dlc_character(char_id):
        """獲取 DLC 角色信息"""
        return dlc_characters.get(char_id)

    def get_all_characters():
        """獲取所有角色（主線 + DLC）"""
        main_chars = {
            "cee": {"name": "Cee", "language": "C"},
            "jawa": {"name": "Jawa", "language": "Java"},
            "rusty": {"name": "Rusty", "language": "Rust"},
            "golly": {"name": "Golly", "language": "Go"},
            "py": {"name": "Py", "language": "Python"},
        }

        all_chars = dict(main_chars)
        all_chars.update(dlc_characters)

        return all_chars

# ============================================================================
# 5. 場景擴展系統
# ============================================================================

init python:
    # DLC 場景註冊表
    if 'dlc_locations' not in dir():
        dlc_locations = {}

    def register_dlc_location(location_id, location_info):
        """
        註冊 DLC 場景

        location_info 應包含:
        - name: 顯示名稱
        - description: 描述
        - bg_image: 背景圖片
        - available_from: 可從哪些地方前往
        - unlock_condition: 解鎖條件函數
        """
        dlc_locations[location_id] = location_info

    def get_available_locations():
        """獲取當前可用的場景列表"""
        available = []

        # 主線場景
        main_locations = [
            ("memory_warehouse", "記憶倉庫", "cee"),
            ("contract_office", "契約局", "jawa"),
        ]

        for loc_id, name, line in main_locations:
            available.append({
                "id": loc_id,
                "name": name,
                "line": line,
                "is_dlc": False
            })

        # DLC 場景
        for loc_id, loc_info in dlc_locations.items():
            unlock_cond = loc_info.get("unlock_condition", lambda: True)
            if unlock_cond():
                available.append({
                    "id": loc_id,
                    "name": loc_info.get("name", loc_id),
                    "line": loc_info.get("dlc_id", "dlc"),
                    "is_dlc": True
                })

        return available

# ============================================================================
# 6. 事件擴展系統
# ============================================================================

init python:
    # DLC 隨機事件列表
    if 'dlc_random_events' not in dir():
        dlc_random_events = []

    def register_dlc_random_event(event_label, weight=1.0, condition=None):
        """
        註冊 DLC 隨機事件

        event_label: 事件 label 名稱
        weight: 事件權重（影響觸發概率）
        condition: 觸發條件函數
        """
        dlc_random_events.append({
            "label": event_label,
            "weight": weight,
            "condition": condition or (lambda: True)
        })

    def get_all_random_events():
        """獲取所有隨機事件（主線 + DLC）"""
        # 主線事件
        main_events = [
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

        # 添加 DLC 事件
        all_events = list(main_events)
        for event in dlc_random_events:
            if event["condition"]():
                all_events.append(event["label"])

        return all_events

# ============================================================================
# 7. 鉤子系統
# ============================================================================

# 這些 label 可被 DLC 覆蓋或擴展

# 在時間選擇菜單前執行
label hook_before_time_menu:
    # DLC 可覆蓋此 label 添加自定義邏輯
    return

# 在結局評估前執行
label hook_before_ending:
    # DLC 可覆蓋此 label 攔截結局流程
    # 如果跳轉到其他 label，則不執行主線結局
    return

# 在章節完成後執行
label hook_after_chapter_complete:
    # chapter_id 在 store.current_chapter_id 中
    return

# 在假日開始時執行
label hook_holiday_start:
    # DLC 可覆蓋此 label 添加假日選項
    return

# ============================================================================
# 8. 調試工具
# ============================================================================

label debug_dlc_status:
    scene black

    narrator "=== DLC 狀態 ==="

    python hide:
        narrator(f"已安裝 DLC 數量: {len(registered_dlcs)}")

        for dlc in registered_dlcs:
            narrator(f"  - {dlc.get('name', dlc.get('id', 'Unknown'))} v{dlc.get('version', '?')}")

        narrator(f"DLC 角色數量: {len(dlc_characters)}")
        narrator(f"DLC 場景數量: {len(dlc_locations)}")
        narrator(f"DLC 隨機事件數量: {len(dlc_random_events)}")

    narrator "=== 主線狀態 ==="

    narrator "源界時間: [source_time]"
    narrator "Cee 關係: [cee_relationship]"
    narrator "Jawa 關係: [jawa_relationship]"

    return
