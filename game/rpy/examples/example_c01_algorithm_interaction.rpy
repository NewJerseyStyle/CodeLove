# ============================================================================
# 範例：C_01 章節算法互動
# ============================================================================
#
# 這是一個專門為 C_01 章節（倉庫找書）設計的算法互動場景範例。
#
# 注意：這是範例代碼，並未被主劇情調用。
# 主劇情使用更通用的系統：
#   - algorithm_choice_menu(problem_id)
#   - show_algorithm_execution(algorithm_id, problem_id)
#   - show_algorithm_teaching(algorithm_id)
#
# 詳細說明參見：docs/C_01_ALGORITHM_INTERACTION.md
# ============================================================================

# ============================================================================
# C_01: 倉庫找書 - 章節特定算法互動
# ============================================================================

label example_c01_algorithm_interaction:
    $ current_problem_id = "C_01_find_book"

    python hide:
        problem = get_problem(current_problem_id)
        problem_desc = problem.get("description", "")
        context = problem.get("context", "")

    scene bg warehouse

    cee "需要找這本書。"

    python hide:
        brute = get_brute_force_solution(current_problem_id)
        if brute:
            store.brute_desc = brute.get('description', '')
            cee_says("我從第一格開始找。[brute_desc]")

    narrator "Cee 開始從第一個書架格子逐一翻找..."

    pause 1.0

    narrator "這樣要很久..."

    menu:
        "提供建議："

        "先看中間那格，再決定往左還是往右（二分搜尋）":
            $ select_algorithm("binary_search")
            $ current_efficiency_multiplier = 5.0

            cee "中間...確定比目標小。往右。"

            pause 0.5

            cee "再中間...比目標大。往左。"

            pause 0.5

            cee "找到了。"

            jump example_show_efficiency_comparison

        "給每本書做一個索引標籤（哈希索引）":
            $ select_algorithm("hash_index")
            $ current_efficiency_multiplier = 10.0

            cee "建立索引...需要額外空間。"

            pause 0.5

            cee "好了。下次可以直接查標籤。"

            narrator "索引建立完成，但佔用了部分倉庫空間。"

            jump example_show_efficiency_comparison

        "讓她繼續（線性搜尋）":
            $ select_algorithm("linear_search")
            $ current_efficiency_multiplier = 1.0

            narrator "Cee 繼續逐一翻找..."

            pause 2.0

            narrator "找到了，但花了很多時間。"

            jump example_show_efficiency_comparison

    label example_show_efficiency_comparison:
        python hide:
            improvement = store.current_efficiency_multiplier

        if improvement > 1.0:
            cee "有效率。"

            if improvement >= 5.0:
                cee "這方法更快。"

        $ execute_algorithm(player_algorithm_choice, current_problem_id)

        if player_algorithm_choice == "binary_search":
            jump example_show_binary_search_teaching
        elif player_algorithm_choice == "hash_index":
            jump example_show_hash_index_teaching
        else:
            return

    label example_show_binary_search_teaching:
        scene bg teaching_card

        teaching "二分搜尋（Binary Search）"

        narrator "時間複雜度：O(log n)"

        narrator "核心思想："

        narrator "- 每次檢查中間元素"

        narrator "- 如果中間元素等於目標，找到"

        narrator "- 如果中間元素小於目標，目標在右半邊"

        narrator "- 如果中間元素大於目標，目標在左半邊"

        narrator "前提條件：資料必須已排序"

        narrator "效率：每次都能排除一半的可能性"

        return

    label example_show_hash_index_teaching:
        scene bg teaching_card

        teaching "哈希索引（Hash Index）"

        narrator "時間複雜度：O(1) 平均"

        narrator "核心思想："

        narrator "- 使用哈希函數將資料映射到位址"

        narrator "- 直接存取，無需遍歷"

        narrator "優點：查找速度極快"

        narrator "缺點：需要額外記憶體建立索引"

        narrator "適用情境：頻繁查找的場景"

        return
