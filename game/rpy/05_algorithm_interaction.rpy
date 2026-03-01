# ============================================================================
# 源界 (Source Realm) - 05: 算法互動系統
# ============================================================================

# ============================================================================
# 1. 算法定義數據結構
# ============================================================================

init python:
    # 算法選項定義
    algorithm_options = {
        "linear_search": {
            "name": "線性搜尋",
            "time_complexity": "O(n)",
            "description": "逐一檢查每個元素",
            "efficiency": 1.0,
            "suitable_for": "小型、未排序的資料",
            "is_brute_force": True,  # Cee 的暴力解法
            "teaching_points": [
                "最簡單的搜尋方式",
                "每個元素都要檢查",
                "如果資料在後面，需要很長時間"
            ]
        },
        "binary_search": {
            "name": "二分搜尋",
            "time_complexity": "O(log n)",
            "description": "每次排除一半的可能性",
            "efficiency": 5.0,  # 比線性搜尋快 5 倍
            "suitable_for": "已排序的資料",
            "is_brute_force": False,
            "prerequisites": ["sorted_data"],
            "teaching_points": [
                "需要資料已排序",
                "每次檢查中間元素",
                "效率遠高於線性搜尋",
                "但前提是資料有序"
            ]
        },
        "hash_index": {
            "name": "哈希索引",
            "time_complexity": "O(1) 平均",
            "description": "使用哈希函數直接定位",
            "efficiency": 10.0,  # 最快
            "suitable_for": "頻繁查找",
            "is_brute_force": False,
            "prerequisites": ["hash_function", "extra_memory"],
            "teaching_points": [
                "需要額外記憶體建立索引",
                "查找速度極快",
                "適合頻繁查找的場景",
                "但建立索引需要前期投入"
            ]
        },
        "bubble_sort": {
            "name": "氣泡排序",
            "time_complexity": "O(n²)",
            "description": "相鄰元素比較交換",
            "efficiency": 1.0,
            "suitable_for": "小型資料",
            "is_brute_force": True,
            "teaching_points": [
                "最直觀但效率最低的排序",
                "重複比較相鄰元素",
                "大型資料時非常慢"
            ]
        },
        "quick_sort": {
            "name": "快速排序",
            "time_complexity": "O(n log n) 平均",
            "description": "分治法，選基準點",
            "efficiency": 8.0,
            "suitable_for": "一般排序需求",
            "is_brute_force": False,
            "teaching_points": [
                "分治法的應用",
                "選一個基準點",
                "比基準小的放左邊，大的放右邊",
                "遞歸處理兩邊"
            ]
        },
        "merge_sort": {
            "name": "合併排序",
            "time_complexity": "O(n log n)",
            "description": "分治法，合併有序子陣列",
            "efficiency": 7.0,
            "suitable_for": "穩定排序需求",
            "is_brute_force": False,
            "teaching_points": [
                "先分割，再合併",
                "合併時保持順序",
                "適合外部排序（大檔案）"
            ]
        },
        "recursive": {
            "name": "遞迴解法",
            "time_complexity": "視問題而定",
            "description": "函數調用自身解決問題",
            "efficiency": 5.0,  # 取決於問題
            "suitable_for": "可分割的問題",
            "is_brute_force": False,
            "prerequisites": ["base_case"],
            "teaching_points": [
                "需要基礎案例（base case）",
                "每個遞迴調用都要更接近基礎案例",
                "如果沒有基礎案例會導致無限遞迴"
            ]
        },
        "iterative": {
            "name": "迭代解法",
            "time_complexity": "視問題而定",
            "description": "使用循環重複執行",
            "efficiency": 4.0,
            "suitable_for": "可重複的任務",
            "is_brute_force": True,  # Cee 的默認方式
            "teaching_points": [
                "使用 while 或 for 循環",
                "顯式控制流程",
                "通常比遞迴更省記憶體"
            ]
        }
    }

    # 問題定義（每個章節對應一個問題）
    problems = {
        "C_01_find_book": {
            "name": "倉庫找書",
            "description": "Cee 需要找一本特定的書",
            "context": "書架按位址順序排列",
            "available_algorithms": ["linear_search", "binary_search", "hash_index"],
            "brute_force": "linear_search",
            "optimal_solution": "binary_search",  # 這個情境下最合適
            "teaching_topic": "指標與位址",
            "cee_default_behavior": "從第一格開始逐一翻找"
        },
        "C_04_move_boxes": {
            "name": "搬運危機",
            "description": "Cee 需要搬運一批新書，但推車不夠用",
            "context": "固定記憶體用完",
            "available_algorithms": ["stack_overflow", "malloc_free"],
            "brute_force": "stack_overflow",
            "optimal_solution": "malloc_free",
            "teaching_topic": "動態記憶體管理",
            "cee_default_behavior": "繼續往上疊，可能倒塌"
        },
        "C_08_sort_items": {
            "name": "物品排序",
            "description": "Cee 需要整理一批物品",
            "context": "物品目前無序",
            "available_algorithms": ["bubble_sort", "quick_sort", "merge_sort"],
            "brute_force": "bubble_sort",
            "optimal_solution": "quick_sort",
            "teaching_topic": "排序演算法",
            "cee_default_behavior": "用氣泡排序逐一比較交換"
        },
        "J_03_define_interface": {
            "name": "定義介面",
            "description": "Jawa 需要定義與外部溝通的介面",
            "context": "不同族群需要合作",
            "available_algorithms": ["loose_interface", "strict_interface"],
            "brute_force": "loose_interface",  # 雖然不是暴力，但 Jawa 的困難點
            "optimal_solution": "strict_interface",
            "teaching_topic": "介面與型別安全",
            "jawa_default_behavior": "過於嚴謹，導致溝通困難"
        }
    }

# ============================================================================
# 2. 算法互動變量
# ============================================================================

# 玩家選擇的算法
default player_algorithm_choice = "none"

# 算法執行結果
default algorithm_execution_result = "none"

# 效率倍數（用於視覺化）
default current_efficiency_multiplier = 1.0

# 當前問題 ID
default current_problem_id = "none"

# 是否正在執行算法
default algorithm_executing = False

# 算法執行時間（模擬）
default algorithm_execution_time = 0

# ============================================================================
# 3. 算法互動系統函數
# ============================================================================

init python:
    def get_problem(problem_id):
        """獲取問題定義"""
        return problems.get(problem_id, {})

    def get_available_algorithms(problem_id):
        """獲取問題可用的算法選項"""
        problem = get_problem(problem_id)
        available = problem.get("available_algorithms", [])

        # 將算法 ID 轉換為算法定義
        return [algorithm_options.get(algo) for algo in available]

    def get_brute_force_solution(problem_id):
        """獲取問題的暴力解法"""
        problem = get_problem(problem_id)
        brute = problem.get("brute_force", "")
        return algorithm_options.get(brute)

    def get_optimal_solution(problem_id):
        """獲取問題的最優解"""
        problem = get_problem(problem_id)
        optimal = problem.get("optimal_solution", "")
        return algorithm_options.get(optimal)

    def select_algorithm(algorithm_id):
        """玩家選擇算法"""
        store.player_algorithm_choice = algorithm_id
        store.last_algorithm_choice = algorithm_id

        # 計算效率倍數
        algo_def = algorithm_options.get(algorithm_id, {})
        efficiency = algo_def.get("efficiency", 1.0)
        store.current_efficiency_multiplier = efficiency

        return True

    def execute_algorithm(algorithm_id, problem_id):
        """執行算法"""
        store.algorithm_executing = True

        # 模擬執行時間（效率越高，時間越短）
        algo_def = algorithm_options.get(algorithm_id, {})
        efficiency = algo_def.get("efficiency", 1.0)
        base_time = 10.0  # 基礎時間（秒）
        store.algorithm_execution_time = base_time / efficiency

        # 確定執行結果
        problem_def = problems.get(problem_id, {})
        optimal = problem_def.get("optimal_solution", "")

        if algorithm_id == optimal:
            store.algorithm_execution_result = "optimal"
        else:
            store.algorithm_execution_result = "acceptable"

        store.algorithm_executing = False

        return store.algorithm_execution_result

    def is_brute_force(algorithm_id):
        """檢查是否為暴力解法"""
        algo_def = algorithm_options.get(algorithm_id, {})
        return algo_def.get("is_brute_force", False)

    def get_algorithm_teaching_points(algorithm_id):
        """獲取算法教學點"""
        algo_def = algorithm_options.get(algorithm_id, {})
        return algo_def.get("teaching_points", [])

# ============================================================================
# 4. 算法選擇菜單
# ============================================================================

label algorithm_choice_menu(problem_id):
    # 顯示算法選擇菜單
    python hide:
        problem = get_problem(problem_id)
        problem_name = problem.get("name", "未知問題")
        problem_desc = problem.get("description", "")
        problem_context = problem.get("context", "")

        available = get_available_algorithms(problem_id)

    scene bg algorithm_menu

    narrator "問題：[problem_name]"

    narrator "[problem_desc]"

    narrator "情境：[problem_context]"

    narrator "Cee 的做法："

    python hide:
        brute = get_brute_force_solution(problem_id)
        if brute:
            store.brute_desc = brute.get("description", "")

    if brute:
        narrator "  [brute_desc]"

    narrator "你能提供什麼算法建議？"

    menu:
        "選擇算法："

        # 實際菜單選項需要在 Ren'Py 中靜態定義
        # 這裡只是框架，實際需要根據具體問題編寫
        "（選項將根據具體問題顯示）":
            pass

    return

# ============================================================================
# 5. 算法執行視覺化
# ============================================================================

label show_algorithm_execution:
    # 從全局變量獲取算法 ID 和問題 ID
    python hide:
        algo_def = algorithm_options.get(store.current_algorithm_id, {})
        store.algo_name = algo_def.get("name", "未知")

        efficiency = algo_def.get("efficiency", 1.0)
        store.execution_time = 10.0 / efficiency  # 秒
        store.algo_efficiency = efficiency

    scene bg algorithm_execution

    narrator "執行中：[algo_name]"

    # 根據效率顯示不同的動畫效果
    if algo_efficiency <= 1.0:
        # 暴力解法 - 緩慢
        with Dissolve(1.0)
        narrator "Cee 開始逐一處理..."

        pause 2.0
        narrator "繼續處理..."

        pause 2.0
        narrator "還在處理..."

        pause 2.0
        narrator "快完成了..."

        pause 1.0
        narrator "完成。"

    elif algo_efficiency <= 5.0:
        # 中等效率 - 正常
        with Fade(0.5)
        narrator "Cee 理解後快速執行。"

        pause 1.0
        narrator "第一步..."

        pause 0.5
        narrator "第二步..."

        pause 0.5
        narrator "完成！"

    else:
        # 高效率 - 快速
        with Fade(0.3)
        narrator "Cee 瞬間理解並執行。"

        pause 0.3
        narrator "完成。速度提升了 [algo_efficiency] 倍！"

    python hide:
        # 執行算法並獲取結果
        result = execute_algorithm(store.current_algorithm_id, store.current_problem_id)

    # 顯示結果
    if store.algorithm_execution_result == "optimal":
        cee "有效率。"

        if algo_efficiency >= 5.0:
            cee "這比我預期的快很多。"

    elif store.algorithm_execution_result == "acceptable":
        cee "完成了。"

        if algo_efficiency < 2.0:
            cee "雖然可行，但不是很有效率。"

    return

# ============================================================================
# 6. 算法教學卡片
# ============================================================================

label show_algorithm_teaching(algorithm_id):
    # 顯示算法教學卡片
    python hide:
        algo_def = algorithm_options.get(algorithm_id, {})
        algo_name = algo_def.get("name", "未知")
        time_complexity = algo_def.get("time_complexity", "")
        description = algo_def.get("description", "")
        suitable = algo_def.get("suitable_for", "")
        teaching_points = algo_def.get("teaching_points", [])

    scene bg teaching_card

    teaching "演算法：[algo_name]"

    narrator "時間複雜度：[time_complexity]"

    narrator "描述：[description]"

    narrator "適用情境：[suitable]"

    if teaching_points:
        narrator "核心概念："

        python hide:
            store.teaching_point_index = 0

    label teaching_point_loop:
        if store.teaching_point_index < len(teaching_points):
            $ store.current_point_text = teaching_points[teaching_point_index]
            python hide:
                narrator("- " + store.current_point_text)
            $ teaching_point_index += 1
            jump teaching_point_loop

    return

# ============================================================================
# 7. 效率對比顯示
# ============================================================================

label show_efficiency_comparison(algorithm_id, problem_id):
    # 顯示效率對比
    python hide:
        selected_algo = algorithm_options.get(algorithm_id, {})
        brute_algo = get_brute_force_solution(problem_id)

        selected_eff = selected_algo.get("efficiency", 1.0)
        brute_eff = brute_algo.get("efficiency", 1.0) if brute_algo else 1.0

        improvement = selected_eff / brute_eff

    scene bg efficiency_comparison

    if improvement > 1.0:
        narrator "效率提升：[improvement]x"

        python hide:
            store.selected_name = selected_algo.get("name", "未知")
            store.brute_name = brute_algo.get("name", "暴力解法") if brute_algo else "暴力解法"

        narrator "使用 [selected_name] 比 [brute_name] 快 [improvement] 倍！"

        if improvement >= 5.0:
            narrator "這是巨大的效率提升。"

            cee "這正是我需要的。"

    elif improvement == 1.0:
        narrator "效率相同。"

    else:
        narrator "效率較低。"

    return

# ============================================================================
# 9. 跨語言指令錯誤互動
# ============================================================================

label show_cross_language_error(error_type, source_language, target_language):
    # 顯示跨語言指令錯誤的教學
    python hide:
        error_messages = {
            "gc_to_c": [
                "你試圖用 Java 的 GC 概念告訴 Cee：",
                "",
                "「Cee，用完的推車不用手動還回去，",
                "系統會自動回收的。」",
                "",
                "Cee 執行了你的指令...",
                "但 C 沒有 GC！"
            ],
            "pointer_to_jawa": [
                "你試圖用 C 的指標邏輯直接操作 Jawa 的物件：",
                "",
                "「這個物件的位址，直接修改裡面的內容。」",
                "",
                "Jawa 拒絕執行：",
                "「型別不符。無法直接訪問私有成員。」"
            ],
            "dynamic_type_to_c": [
                "你試圖用 Python 的動態型別概念和 Cee 溝通：",
                "",
                "「這個變數可以是任何型別，隨意使用。」",
                "",
                "Cee 執行了，但結果型別完全錯誤...",
                "記憶體損壞！"
            ]
        }

    scene bg cross_language_error

    python hide:
        messages = error_messages.get(error_type, ["跨語言指令錯誤"])
        store.error_message_index = 0

    label error_message_loop:
        if store.error_message_index < len(messages):
            $ store.current_error_text = messages[error_message_index]
            python hide:
                narrator(store.current_error_text)
            $ error_message_index += 1
            jump error_message_loop

    $ cross_language_error_occurred = True
    $ cross_language_error_type = error_type

    # 觸發後果
    if error_type == "gc_to_c":
        $ apply_consequence("memory_leak", "moderate", "使用 Java GC 概念指揮 Cee")
        call show_consequence_notification("memory_leak", "moderate")
    elif error_type == "pointer_to_jawa":
        $ apply_consequence("type_mismatch", "minor", "使用 C 指標邏輯操作 Jawa")
        call show_consequence_notification("type_mismatch", "minor")
    elif error_type == "dynamic_type_to_c":
        $ apply_consequence("buffer_overflow", "severe", "動態型別導致 C 記憶體損壞")
        call show_consequence_notification("buffer_overflow", "severe")

    # 顯示教學
    call show_consequence_teaching(error_type)

    # 顯示角色反應
    if target_language == "cee":
        call show_consequence_reaction("cee", "memory_leak" if error_type == "gc_to_c" else "buffer_overflow")

    return
