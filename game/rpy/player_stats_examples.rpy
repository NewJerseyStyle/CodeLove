# ============================================================================
# 源界 (Source Realm) - 玩家操作追蹤使用範例
# ============================================================================
# 此文件展示如何在遊戲中使用 player_stats 追蹤系統
# ============================================================================

# ============================================================================
# 基本用法範例
# ============================================================================

# 範例 1：追蹤對話選擇
# ------------------------------------
label example_dialogue_choice:
    menu:
        # 普通對話選擇（非算法相關）
        "選擇觀察":
            # 追蹤對話選擇，非最優
            $ track_choice("dialogue", is_optimal=False)

            narrator "你選擇觀察..."

        "選擇幫忙":
            # 追蹤對話選擇，最優
            $ track_choice("dialogue", is_optimal=True)

            narrator "你決定幫忙..."

    jump continue_story


# 範例 2：追蹤算法推薦
# ------------------------------------
label example_algorithm_choice:
    cee "這個箱子太多了，我需要一個更有效率的方法。"

    menu:
        # 算法選擇
        "讓她繼續慢慢找":
            # 錯誤/非最優選擇
            $ track_choice("algorithm", is_optimal=False)

            cee "好。"

            pause 2.0

            # 觸發輕微後果（花費更多時間）
            $ track_consequence("minor")
            narrator "過了很久，Cee 才找到要找的東西。"

        "建議用二分搜尋":
            # 最優選擇，算法推薦
            $ track_choice("algorithm", is_optimal=True)

            # 追蹤學會的概念
            $ track_learned_concept("binary_search")

            cee "二分搜尋？好主意。"

            pause 1.5

            # 算法導師成就自動更新（因為在 track_choice 中調用了）
            cee "找到了！這樣快多了。"

    jump continue_story


# 範例 3：追蹤觀察 vs 干預
# ------------------------------------
label example_observation:
    cee "我在整理這些索引。"

    menu:
        "觀察她的工作":
            # 追蹤觀察選擇
            $ track_choice("observation", is_optimal=True)

            $ track_dialogue("cee")
            narrator "你安靜地看著 Cee 工作..."

        "提供建議":
            # 追蹤干預選擇
            $ track_choice("dialogue", is_optimal=False)

            $ track_dialogue("cee")
            narrator "你向 Cee 提供了一些建議..."

    jump continue_story


# 範例 4：追蹤後果系統
# ------------------------------------
label example_consequences:
    # 輕微後果（影響當前任務）
    $ track_consequence("minor")
    narrator "這個錯誤讓任務失敗了，但可以重試。"

    # 中等後果（波及角色工作空間）
    $ track_consequence("moderate")
    narrator "Cee 需要花時間清理這些混亂，她的可用時間減少了。"

    # 嚴重後果（波及其他角色）
    $ track_consequence("severe")
    narrator "這個錯誤波及了 Rusty 的區域，她很生氣。"

    # 致命後果（系統崩潰）
    $ track_consequence("fatal")
    narrator "整個區域崩潰了，這是一個嚴重的問題。"

    jump continue_story


# 範例 5：追蹤章節完成
# ------------------------------------
label example_chapter_complete:
    # 章節結束時調用
    $ track_chapter_completed("C_01")

    # 追蹤學會的概念
    $ track_learned_concept("pointers")

    # 檢查是否不使用提示完成
    if not used_hint:
        $ track_no_hint_completion("C_01")

    narrator "你完成了 C_01 章節。"

    jump next_chapter


# 範例 6：追蹤角色好感度
# ------------------------------------
label example_affection:
    cee "你的建議很有用。"

    menu:
        "繼續幫忙":
            # 增加好感度
            $ track_affection("cee", 5)

            cee "謝謝。"

        "我只是在觀察":
            # 不變好感度
            cee "嗯。"

        "這其實很簡單":
            # 減少好感度
            $ track_affection("cee", -2)

            cee "..."

    jump continue_story


# 範例 7：追蹤假日參與
# ------------------------------------
label example_holiday:
    # 假日開始
    narrator "今天沒有特別的任務，Cee 在休息。"

    menu:
        "找 Cee 聊天":
            # 追蹤假日參與
            $ persistent.player_stats["holidays_participated"] += 1

            $ track_dialogue("cee")
            $ track_affection("cee", 10)

            cee "哦，是你。有什麼事嗎？"

            menu:
                "聊聊她的工作":
                    $ track_dialogue("cee")
                    cee "倉庫的管理其實很複雜..."

                "詢問關於源界的事":
                    $ track_dialogue("cee")
                    cee "源界...那是很深的層面。"

        "自己四處走走":
            # 不追蹤假日參與
            narrator "你決定自己探索一下。"

    jump continue_story


# 範例 8：發現隱藏選項
# ------------------------------------
label example_hidden_option:
    narrator "你注意到角落裡有些不對勁。"

    menu:
        "仔細查看":
            $ track_hidden_option()

            narrator "你發現了一個隱藏的開關！"

            menu:
                "按下開關":
                    # 隱藏選項的後果
                    narrator "一道暗門打開了..."

                "保持沉默":
                    pass

        "離開":
            pass

    jump continue_story


# 範例 9：在結局時顯示統計
# ------------------------------------
label example_end_stats:
    # 獲取統計摘要
    $ stats = get_stats_summary()

    scene black

    with Dissolve(1.0)

    narrator "=== 遊戲統計 ==="

    narrator "遊戲時間：[stats['total_playtime']] 分鐘"

    narrator "完成章節：[stats['chapters_completed']] 個"

    narrator "學會概念：[stats['concepts_learned']] 個"

    narrator "算法解決方案：[stats['algorithms_provided']] 次"

    narrator "最高連續正確：[stats['consecutive_correct']] 次"

    narrator "總選擇次數：[stats['total_choices']] 次"

    narrator "最優選擇比例：[stats['optimal_ratio']]%"

    pause 3.0

    narrator "=================="

    # 根據統計數據給予評價
    if stats['optimal_ratio'] >= 80:
        narrator "你是一位傑出的決策者！"
    elif stats['optimal_ratio'] >= 60:
        narrator "你做出的大部分決定都是正確的。"
    else:
        narrator "你需要更多經驗來做出更好的決定。"

    pause 3.0

    jump credits


# 範例 10：檢查成就是否已解鎖
# ------------------------------------
label example_check_achievement:
    if achievement_avoided_danger.has_granted():
        narrator "你已經獲得了「明智的選擇」成就。"
    else:
        narrator "你還沒有獲得「明智的選擇」成就。"

    jump continue_story


# ============================================================================
# 高級用法範例
# ============================================================================

# 範例 11：自定義統計追蹤
# ------------------------------------
label example_custom_tracking:
    # 直接訪問 persistent.player_stats
    $ persistent.player_stats["custom_stat"] += 1

    # 檢查統計數據
    if persistent.player_stats["custom_stat"] >= 10:
        # 觸發自定義事件
        pass

    jump continue_story


# 範例 12：複雜條件成就觸發
# ------------------------------------
label example_complex_condition:
    # 需要多個條件同時滿足才能觸發
    if (len(persistent.player_stats["chapters_completed"]) >= 3 and
        len(persistent.player_stats["concepts_learned"]) >= 5 and
        persistent.player_stats["optimal_choices"] >= 10):

        # 觸發特殊成就或事件
        $ achievement_custom_event_granted = True

    jump continue_story


# 範例 13：根據統計數據調整劇情
# ------------------------------------
label example_dynamic_story:
    # 根據玩家的選擇風格調整對話
    if persistent.player_stats["observations"] > persistent.player_stats["total_dialogues"] / 2:
        # 玩家傾向於觀察
        cee "你總是很安靜地看著..."
    elif persistent.player_stats["optimal_choices"] / persistent.player_stats["total_choices"] > 0.8:
        # 玩家傾向於做最優選擇
        cee "你的判斷總是很準確..."
    else:
        # 普通玩家
        cee "你在學習中..."

    jump continue_story


# 範例 14：時間追蹤（可選）
# ------------------------------------
init python:
    # 在遊戲開始時記錄開始時間
    def start_game_timer():
        if not hasattr(persistent, "game_start_time"):
            persistent.game_start_time = time.time()

    # 在遊戲暫停/保存時更新時間
    def update_game_time():
        if hasattr(persistent, "game_start_time"):
            elapsed = int((time.time() - persistent.game_start_time) / 60)  # 分鐘
            persistent.player_stats["game_time_spent"] += elapsed
            persistent.game_start_time = time.time()


# ============================================================================
# 範例標籤
# ============================================================================

label continue_story:
    narrator "故事繼續..."

    jump prologue_end
