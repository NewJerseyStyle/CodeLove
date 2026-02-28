# ============================================================================
# 源界 (Source Realm) - 03: FSM 狀態機系統
# ============================================================================

# ============================================================================
# 1. FSM 系統數據結構
# ============================================================================

init python:
    # 關係 FSM 定義（Cee）
    cee_relationship_fsm = {
        "UNMET": {
            "next_states": ["FIRST_CONTACT"],
            "transitions": {
                "FIRST_CONTACT": {
                    "trigger": "first_encounter",
                    "required": None,
                    "effect": lambda: progress_relationship("cee", "FIRST_CONTACT")
                }
            }
        },
        "FIRST_CONTACT": {
            "next_states": ["FUNCTIONAL"],
            "transitions": {
                "FUNCTIONAL": {
                    "trigger": "successful_collaboration",
                    "required": None,
                    "effect": lambda: progress_relationship("cee", "FUNCTIONAL")
                }
            }
        },
        "FUNCTIONAL": {
            "next_states": ["RELIABLE"],
            "transitions": {
                "RELIABLE": {
                    "trigger": "consistent_efficiency",
                    "required": None,
                    "effect": lambda: progress_relationship("cee", "RELIABLE")
                }
            }
        },
        "RELIABLE": {
            "next_states": ["RESONANT"],
            "transitions": {
                "RESONANT": {
                    "trigger": "deep_understanding",
                    "required": None,
                    "effect": lambda: progress_relationship("cee", "RESONANT")
                }
            }
        },
        "RESONANT": {
            "next_states": ["PARTNER", "CLOSE_ALLY"],
            "transitions": {
                "PARTNER": {
                    "trigger": "commitment_choice",
                    "required": "choose_partner",
                    "effect": lambda: progress_relationship("cee", "PARTNER")
                },
                "CLOSE_ALLY": {
                    "trigger": "ally_choice",
                    "required": "choose_ally",
                    "effect": lambda: progress_relationship("cee", "CLOSE_ALLY")
                }
            }
        }
    }

    # 關係 FSM 定義（Jawa）
    jawa_relationship_fsm = {
        "UNMET": {
            "next_states": ["FORMAL_CONTACT"],
            "transitions": {
                "FORMAL_CONTACT": {
                    "trigger": "first_encounter",
                    "required": None,
                    "effect": lambda: progress_relationship("jawa", "FORMAL_CONTACT")
                }
            }
        },
        "FORMAL_CONTACT": {
            "next_states": ["VERIFIED"],
            "transitions": {
                "VERIFIED": {
                    "trigger": "successful_verification",
                    "required": None,
                    "effect": lambda: progress_relationship("jawa", "VERIFIED")
                }
            }
        },
        "VERIFIED": {
            "next_states": ["TRUSTED"],
            "transitions": {
                "TRUSTED": {
                    "trigger": "proven_reliability",
                    "required": None,
                    "effect": lambda: progress_relationship("jawa", "TRUSTED")
                }
            }
        },
        "TRUSTED": {
            "next_states": ["SYNCHRONIZED"],
            "transitions": {
                "SYNCHRONIZED": {
                    "trigger": "deep_sync",
                    "required": None,
                    "effect": lambda: progress_relationship("jawa", "SYNCHRONIZED")
                }
            }
        },
        "SYNCHRONIZED": {
            "next_states": ["PARTNER", "DEEP_ALLY"],
            "transitions": {
                "PARTNER": {
                    "trigger": "commitment_choice",
                    "required": "choose_partner",
                    "effect": lambda: progress_relationship("jawa", "PARTNER")
                },
                "DEEP_ALLY": {
                    "trigger": "ally_choice",
                    "required": "choose_ally",
                    "effect": lambda: progress_relationship("jawa", "DEEP_ALLY")
                }
            }
        }
    }

    # 章節 FSM 模板（用於各個章節）
    def create_chapter_fsm(chapter_id, nodes, transitions):
        """創建章節 FSM"""
        return {
            "chapter_id": chapter_id,
            "nodes": nodes,  # {node_id: {type, description, transition_to, ...}}
            "transitions": transitions  # {from_node: {condition: to_node}}
        }

# ============================================================================
# 2. FSM 狀態追蹤
# ============================================================================

# Cee 線當前所在的 FSM 節點
default cee_fsm_current_node = "start"

# Jawa 線當前所在的 FSM 節點
default jawa_fsm_current_node = "start"

# 當前章節 FSM（每個章節有自己的 FSM）
default current_chapter_fsm = None
default current_chapter_node = "start"

# FSM 歷史記錄（用於調試和回放）
default fsm_history = []

# ============================================================================
# 3. FSM 系統函數
# ============================================================================

init python:
    def get_fsm_state(character):
        """獲取角色的 FSM 狀態"""
        return getattr(store, character + "_fsm_current_node", "start")

    def set_fsm_state(character, node_id):
        """設置角色的 FSM 狀態"""
        setattr(store, character + "_fsm_current_node", node_id)

        # 記錄到歷史
        store.fsm_history.append({
            "character": character,
            "node_id": node_id,
            "timestamp": store.source_time
        })

    def can_transition_fsm(character, from_node, condition):
        """檢查是否可以進行 FSM 轉換"""
        fsm_def = getattr(store, character + "_relationship_fsm", None)

        if fsm_def and from_node in fsm_def:
            node_def = fsm_def[from_node]
            transitions = node_def.get("transitions", {})

            # 檢查是否有符合條件的轉換
            for trans_name, trans_def in transitions.items():
                if trans_def.get("trigger") == condition:
                    return True, trans_name

        return False, None

    def execute_fsm_transition(character, condition):
        """執行 FSM 轉換"""
        current_node = get_fsm_state(character)

        # 嘗試轉換
        can_transition, trans_name = can_transition_fsm(character, current_node, condition)

        if can_transition:
            fsm_def = getattr(store, character + "_relationship_fsm", None)
            node_def = fsm_def[current_node]
            transitions = node_def.get("transitions", {})
            trans_def = transitions[trans_name]

            # 執行轉換效果
            effect = trans_def.get("effect")
            if effect and callable(effect):
                effect()

            return True
        else:
            return False

    def get_available_transitions(character):
        """獲取可用的轉換選項"""
        current_node = get_fsm_state(character)
        fsm_def = getattr(store, character + "_relationship_fsm", None)

        available = []

        if fsm_def and current_node in fsm_def:
            node_def = fsm_def[current_node]
            transitions = node_def.get("transitions", {})

            for trans_name, trans_def in transitions.items():
                trigger = trans_def.get("trigger", "")
                available.append({
                    "name": trans_name,
                    "trigger": trigger,
                    "required": trans_def.get("required", None)
                })

        return available

# ============================================================================
# 4. 章節 FSM 管理函數
# ============================================================================

init python:
    def load_chapter_fsm(chapter_id):
        """加載章節 FSM（從定義中讀取）"""
        # 這裡需要實際實現章節 FSM 的加載邏輯
        # 可以從 JSON 文件或硬編碼定義中讀取
        pass

    def chapter_fsm_transition(condition):
        """執行章節 FSM 轉換"""
        if not store.current_chapter_fsm:
            return False

        current_node = store.current_chapter_node
        transitions = store.current_chapter_fsm.get("transitions", {})

        if current_node in transitions:
            node_transitions = transitions[current_node]

            # 尋找符合條件的轉換
            for cond, target_node in node_transitions.items():
                if cond == condition:
                    store.current_chapter_node = target_node
                    return True

        return False

    def get_current_chapter_node():
        """獲取當前章節節點"""
        return store.current_chapter_node

    def set_current_chapter_node(node_id):
        """設置當前章節節點"""
        store.current_chapter_node = node_id

# ============================================================================
# 5. FSM 觸發條件定義
# ============================================================================

# 關係進展觸發條件（用於檢查是否可以進入下一階段）
init python:
    def check_cee_relationship_progress():
        """檢查 Cee 關係是否可以進展"""
        current = store.cee_relationship

        # UNMET → FIRST_CONTACT：首次遭遇
        if current == "UNMET":
            return "first_encounter"

        # FIRST_CONTACT → FUNCTIONAL：成功合作
        elif current == "FIRST_CONTACT":
            if (store.c_01_status == "completed" and
                store.last_algorithm_choice in ["binary_search", "hash_index"]):
                return "successful_collaboration"

        # FUNCTIONAL → RELIABLE：持續效率
        elif current == "FUNCTIONAL":
            completed_cee_chapters = sum([
                1 for status in [
                    store.c_01_status, store.c_02_status, store.c_03_status,
                    store.c_04_status, store.c_05_status
                ] if status == "completed"
            ])
            if completed_cee_chapters >= 3 and store.efficiency_multiplier >= 2.0:
                return "consistent_efficiency"

        # RELIABLE → RESONANT：深度理解
        elif current == "RELIABLE":
            completed_cee_chapters = sum([
                1 for status in [
                    store.c_01_status, store.c_02_status, store.c_03_status,
                    store.c_04_status, store.c_05_status, store.c_06_status
                ] if status == "completed"
            ])
            if completed_cee_chapters >= 5 and not store.cross_language_error_occurred:
                return "deep_understanding"

        # RESONANT → PARTNER/CLOSE_ALLY：最終選擇
        elif current == "RESONANT":
            # 這需要玩家主動選擇
            return "commitment_choice"

        return None

    def check_jawa_relationship_progress():
        """檢查 Jawa 關係是否可以進展"""
        current = store.jawa_relationship

        # UNMET → FORMAL_CONTACT：首次接觸
        if current == "UNMET":
            return "first_encounter"

        # FORMAL_CONTACT → VERIFIED：成功驗證
        elif current == "FORMAL_CONTACT":
            if store.j_01_status == "completed":
                return "successful_verification"

        # VERIFIED → TRUSTED：證明可靠性
        elif current == "VERIFIED":
            completed_jawa_chapters = sum([
                1 for status in [
                    store.j_01_status, store.j_02_status, store.j_03_status
                ] if status == "completed"
            ])
            if completed_jawa_chapters >= 3 and not store.jawa_in_gc_pause:
                return "proven_reliability"

        # TRUSTED → SYNCHRONIZED：深度同步
        elif current == "TRUSTED":
            completed_jawa_chapters = sum([
                1 for status in [
                    store.j_01_status, store.j_02_status, store.j_03_status,
                    store.j_04_status, store.j_05_status
                ] if status == "completed"
            ])
            if completed_jawa_chapters >= 5:
                return "deep_sync"

        # SYNCHRONIZED → PARTNER/DEEP_ALLY：最終選擇
        elif current == "SYNCHRONIZED":
            return "commitment_choice"

        return None

# ============================================================================
# 6. FSM 關係進展自動檢查
# ============================================================================

label check_all_relationships:
    python hide:
        # 檢查 Cee 關係
        cee_trigger = check_cee_relationship_progress()
        if cee_trigger:
            execute_fsm_transition("cee", cee_trigger)

        # 檢查 Jawa 關係
        jawa_trigger = check_jawa_relationship_progress()
        if jawa_trigger:
            execute_fsm_transition("jawa", jawa_trigger)

    return

# ============================================================================
# 7. FSM 關係選擇菜單
# ============================================================================

label relationship_choice_menu(character):
    python hide:
        available_transitions = get_available_transitions(character)
        # 記錄可用的轉換數量
        store.available_transition_count = len(available_transitions)
        # 記錄第一個轉換（如果有）
        if available_transitions:
            store.first_transition_name = available_transitions[0].get("name", "")
            store.first_transition_trigger = available_transitions[0].get("trigger", "")
        else:
            store.first_transition_name = ""
            store.first_transition_trigger = ""

    narrator "[character] 線關係選擇"

    if store.available_transition_count > 0:
        menu:
            "選擇關係進展方向："

            "[first_transition_name] - [first_transition_trigger]":
                # 這裡需要根據實際轉換處理
                pass

    return

# ============================================================================
# 8. FSM 調試功能（開發用）
# =================================================================##

label debug_fsm_state:
    # 顯示當前 FSM 狀態（開發調試用）
    scene bg debug

    narrator "=== FSM 狀態調試 ==="

    narrator "Cee 關係：[cee_relationship]"
    narrator "Jawa 關係：[jawa_relationship]"

    narrator "當前時間段：[current_time_period]"
    narrator "源界時間：[source_time]"

    narrator "Cee 線已完成章節："
    python hide:
        cee_completed_list = []
        for i in range(1, 10):
            status = getattr(store, "c_0" + str(i) + "_status", "unstarted")
            if status == "completed":
                cee_completed_list.append("C_0" + str(i))

    if len(cee_completed_list) > 0:
        python hide:
            store.cee_display_index = 0

        label cee_display_loop:
            if store.cee_display_index < len(cee_completed_list):
                $ store.current_cee_item = cee_completed_list[cee_display_index]
                python hide:
                    narrator(store.current_cee_item)
                $ cee_display_index += 1
                jump cee_display_loop
    else:
        narrator "  無"

    narrator "Jawa 線已完成章節："
    python hide:
        jawa_completed_list = []
        for i in range(1, 10):
            status = getattr(store, "j_0" + str(i) + "_status", "unstarted")
            if status == "completed":
                jawa_completed_list.append("J_0" + str(i))

    if len(jawa_completed_list) > 0:
        python hide:
            store.jawa_display_index = 0

        label jawa_display_loop:
            if store.jawa_display_index < len(jawa_completed_list):
                $ store.current_jawa_item = jawa_completed_list[jawa_display_index]
                python hide:
                    narrator(store.current_jawa_item)
                $ jawa_display_index += 1
                jump jawa_display_loop
    else:
        narrator "  無"

    narrator "後果等級：[current_consequence]"
    narrator "後果持續時間：[consequence_duration] ST"

    return
