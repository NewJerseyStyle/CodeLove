# ============================================================================
# 源界 (Source Realm) - 玩家操作追蹤系統
# ============================================================================
# 此系統追蹤玩家在遊戲中的各種操作，用於成就和統計
# ============================================================================

init -500 python:
    # 玩家操作統計數據
    if not hasattr(persistent, "player_stats"):
        persistent.player_stats = {
            # 基本操作
            "total_choices": 0,              # 總選擇次數
            "total_dialogues": 0,           # 總對話選擇次數
            "save_count": 0,                # 存檔次數
            "load_count": 0,                # 讀檔次數
            "skip_count": 0,                # 跳過文本次數
            "rollback_count": 0,            # 回滾次數

            # 學習進度
            "concepts_learned": [],          # 學會的概念列表
            "chapters_completed": [],         # 完成的章節列表
            "algorithms_provided": 0,        # 提供的算法解決方案數量
            "optimal_choices": 0,            # 最優選擇次數
            "wrong_choices": 0,              # 錯誤選擇次數

            # 社交互動
            "dialogues_with_cee": 0,        # 與 Cee 對話次數
            "dialogues_with_jawa": 0,       # 與 Jawa 對話次數
            "dialogues_with_rusty": 0,       # 與 Rusty 對話次數
            "dialogues_with_golly": 0,       # 與 Golly 對話次數
            "holidays_participated": 0,       # 參與假日次數
            "observations": 0,               # 選擇觀察而非干預的次數

            # 後果系統
            "consequences_minor": 0,          # 輕微後果次數
            "consequences_moderate": 0,      # 中等後果次數
            "consequences_severe": 0,       # 嚴重後果次數
            "consequences_fatal": 0,         # 致命後果次數

            # 特殊行為
            "hidden_options_found": 0,       # 發現隱藏選項次數
            "no_hint_completion": 0,         # 不使用提示完成的章節數
            "consecutive_correct": 0,         # 當前連續正確選擇
            "max_consecutive_correct": 0,     # 最高連續正確選擇

            # 關係進度
            "cee_affection": 0,             # Cee 好感度
            "jawa_affection": 0,            # Jawa 好感度
            "rusty_affection": 0,            # Rusty 好感度
            "golly_affection": 0,            # Golly 好感度

            # 遊戲統計
            "game_time_spent": 0,           # 遊戲時間（分鐘）
            "fastest_chapter_time": None,     # 最快完成章節時間
            "total_words_read": 0,           # 閱讀字數（估算）
        }

    # ============================================================================
    # 玩家操作追蹤函數
    # ============================================================================

    def track_choice(choice_type="dialogue", is_optimal=False):
        """
        追蹤玩家的選擇

        參數：
            choice_type: 選擇類型 ("dialogue", "algorithm", "observation")
            is_optimal: 是否為最優選擇
        """
        # 確保 player_stats 已初始化
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return

        persistent.player_stats["total_choices"] += 1

        if choice_type == "dialogue":
            persistent.player_stats["total_dialogues"] += 1
        elif choice_type == "algorithm":
            persistent.player_stats["algorithms_provided"] += 1
            # 更新算法導師成就進度
            achievement_algorithm_tutor.add_progress(1)
        elif choice_type == "observation":
            persistent.player_stats["observations"] += 1

        if is_optimal:
            persistent.player_stats["optimal_choices"] += 1
            persistent.player_stats["consecutive_correct"] += 1
            # 更新最高連續正確記錄
            if persistent.player_stats["consecutive_correct"] > persistent.player_stats["max_consecutive_correct"]:
                persistent.player_stats["max_consecutive_correct"] = persistent.player_stats["consecutive_correct"]
        else:
            persistent.player_stats["wrong_choices"] += 1
            persistent.player_stats["consecutive_correct"] = 0

        # 檢查相關成就
        _check_choice_achievements()

    def track_learned_concept(concept_name):
        """
        追蹤學會的概念

        參數：
            concept_name: 概念名稱（如 "pointers", "binary_search"）
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if concept_name not in persistent.player_stats["concepts_learned"]:
            persistent.player_stats["concepts_learned"].append(concept_name)
            _check_learning_achievements()

    def track_chapter_completed(chapter_id):
        """
        追蹤完成的章節

        參數：
            chapter_id: 章節 ID（如 "C_01", "J_01"）
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if chapter_id not in persistent.player_stats["chapters_completed"]:
            persistent.player_stats["chapters_completed"].append(chapter_id)
            _check_chapter_achievements()

    def track_consequence(level):
        """
        追蹤觸發的後果

        參數：
            level: 後果等級 ("minor", "moderate", "severe", "fatal")
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if level == "minor":
            persistent.player_stats["consequences_minor"] += 1
        elif level == "moderate":
            persistent.player_stats["consequences_moderate"] += 1
        elif level == "severe":
            persistent.player_stats["consequences_severe"] += 1
        elif level == "fatal":
            persistent.player_stats["consequences_fatal"] += 1

        _check_consequence_achievements()

    def track_dialogue(character_name):
        """
        追蹤與角色的對話

        參數：
            character_name: 角色名稱（"cee", "jawa", "rusty", "golly"）
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        char_key = f"dialogues_with_{character_name}"
        if char_key in persistent.player_stats:
            persistent.player_stats[char_key] += 1

    def track_affection(character_name, amount):
        """
        追蹤角色好感度變化

        參數：
            character_name: 角色名稱（"cee", "jawa", "rusty", "golly"）
            amount: 變化量（正數增加，負數減少）
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        aff_key = f"{character_name}_affection"
        if aff_key in persistent.player_stats:
            persistent.player_stats[aff_key] += amount

    def track_save_load(action):
        """
        追蹤存檔/讀檔操作

        參數：
            action: "save" 或 "load"
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if action == "save":
            persistent.player_stats["save_count"] += 1
        elif action == "load":
            persistent.player_stats["load_count"] += 1

    def track_skip_rollback(action):
        """
        追蹤跳過/回滾操作

        參數：
            action: "skip" 或 "rollback"
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if action == "skip":
            persistent.player_stats["skip_count"] += 1
        elif action == "rollback":
            persistent.player_stats["rollback_count"] += 1

    def track_hidden_option():
        """追蹤發現隱藏選項"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        persistent.player_stats["hidden_options_found"] += 1
        if persistent.player_stats["hidden_options_found"] == 1:
            # 第一次發現隱藏選項
            achievement_hidden_explorer.grant()

    def track_no_hint_completion(chapter_id):
        """
        追蹤不使用提示完成的章節

        參數：
            chapter_id: 章節 ID
        """
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        if chapter_id not in persistent.player_stats["concepts_learned"]:
            persistent.player_stats["concepts_learned"].append(f"no_hint_{chapter_id}")
            persistent.player_stats["no_hint_completion"] += 1

    def get_player_stats():
        """獲取玩家統計數據（用於顯示）"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return {}
        return persistent.player_stats.copy()

    # ============================================================================
    # 成就檢查函數
    # ============================================================================

    def _check_choice_achievements():
        """檢查與選擇相關的成就"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        stats = persistent.player_stats

        # 檢查連續正確選擇成就
        if stats["max_consecutive_correct"] >= 5:
            achievement_consecutive_correct.grant()
        if stats["max_consecutive_correct"] >= 10:
            achievement_perfect_decisions.grant()

    def _check_learning_achievements():
        """檢查與學習相關的成就"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        stats = persistent.player_stats

        # 檢查概念學習成就
        if len(stats["concepts_learned"]) >= 5:
            achievement_quick_learner.grant()
        if len(stats["concepts_learned"]) >= 10:
            achievement_knowledge_seeker.grant()

    def _check_chapter_achievements():
        """檢查與章節相關的成就"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        stats = persistent.player_stats

        # 檢查章節完成數量
        completed_count = len(stats["chapters_completed"])
        if completed_count >= 3:
            achievement_first_steps.grant()
        if completed_count >= 6:
            achievement_dedicated_player.grant()
        if completed_count >= 10:
            achievement_explorer.grant()

    def _check_consequence_achievements():
        """檢查與後果相關的成就"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return
        stats = persistent.player_stats

        # 檢查安全玩家成就（沒有嚴重或致命後果）
        if stats["consequences_severe"] == 0 and stats["consequences_fatal"] == 0:
            # 結束時檢查（在終章）
            pass

    # ============================================================================
    # 統計顯示函數
    # ============================================================================

    def get_stats_summary():
        """獲取統計摘要（用於結局畫面）"""
        if not hasattr(persistent, "player_stats") or persistent.player_stats is None:
            return {}
        stats = persistent.player_stats

        summary = {
            "total_playtime": stats.get("game_time_spent", 0),
            "chapters_completed": len(stats.get("chapters_completed", [])),
            "concepts_learned": len(stats.get("concepts_learned", [])),
            "algorithms_provided": stats.get("algorithms_provided", 0),
            "consecutive_correct": stats.get("max_consecutive_correct", 0),
            "total_choices": stats.get("total_choices", 0),
            "optimal_ratio": 0,
        }

        # 計算最優選擇比例
        if summary["total_choices"] > 0:
            summary["optimal_ratio"] = int(
                (stats.get("optimal_choices", 0) / summary["total_choices"]) * 100
            )

        return summary
