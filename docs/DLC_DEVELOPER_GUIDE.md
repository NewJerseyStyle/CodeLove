# 源界 (Source Realm) - DLC 開發者指南

> 本文件為社區 DLC 開發者提供完整的擴展指南，確保 DLC 能夠無縫整合到主遊戲中。

---

## 目錄

1. [架構概述](#1-架構概述)
2. [時間線系統與動態結局](#2-時間線系統與動態結局)
3. [角色擴展](#3-角色擴展)
4. [事件與章節創建](#4-事件與章節創建)
5. [自定義結局](#5-自定義結局)
6. [後果系統整合](#6-後果系統整合)
7. [文件結構規範](#7-文件結構規範)
8. [API 參考](#8-api-參考)
9. [最佳實踐](#9-最佳實踐)
10. [範例模板](#10-範例模板)

---

## 1. 架構概述

### 1.1 核心系統文件

| 文件 | 用途 | DLC 可修改 |
|------|------|-----------|
| `rpy/00_setup.rpy` | 全局變量、系統函數 | ⚠️ 僅添加，不修改 |
| `rpy/01_characters.rpy` | 角色定義 | ✅ 添加新角色 |
| `rpy/02_timeline.rpy` | 時間線系統 | ✅ 擴展時間段 |
| `rpy/03_fsm.rpy` | 關係狀態輔助 | ✅ 使用輔助函數 |
| `rpy/04_consequence.rpy` | 後果系統 | ✅ 調用現有函數 |

### 1.2 章節目錄結構

```
rpy/chapters/
├── prologue.rpy          # 序章
├── cee/                  # Cee 線 (C 語言)
│   ├── C_01_pointers.rpy
│   ├── C_02_memory.rpy
│   └── ...
├── jawa/                 # Jawa 線 (Java)
│   ├── J_01_types.rpy
│   └── ...
├── shared/               # 共享事件
│   ├── explore_events.rpy
│   ├── holidays.rpy
│   └── shared_events.rpy
└── endings/              # 結局
    └── game_endings.rpy
```

### 1.3 DLC 目錄建議

```
rpy/dlc/
├── your_dlc_name/
│   ├── characters.rpy    # 新角色定義
│   ├── events/           # 事件文件
│   ├── timeline.rpy      # 時間線擴展
│   ├── endings.rpy       # DLC 專屬結局
│   └── config.rpy        # DLC 配置
```

---

## 2. 時間線系統與動態結局

### 2.1 源界時間 (ST) 概念

源界時間是遊戲的主要進度指標：
- ST 0-36：主線劇情
- ST 36-38：結局評估
- ST 38+：Bad End A 檢查

### 2.2 動態結局計算（關鍵改進）

**問題**：原設計在 ST 36 強制進入結局評估，限制了 DLC 擴展。

**解決方案**：DLC 可以禁用主線結局強制觸發：

```python
# 在你的 DLC config.rpy 中
init python:
    # 禁用主線結局強制觸發
    dlc_disable_main_ending_force = True

    # 設置 DLC 自定義結局時間
    dlc_custom_ending_time = 50  # ST 50 才觸發 DLC 結局

    # 添加 DLC 結局條件
    def dlc_check_ending():
        if store.source_time >= dlc_custom_ending_time:
            if store.dlc_relationship == "MAX":
                return "dlc_true_end"
            elif store.dlc_relationship in ["HIGH", "MAX"]:
                return "dlc_good_end"
        return None
```

### 2.3 擴展時間線

在 `dlc/your_dlc_name/timeline.rpy` 中添加：

```python
init python:
    # 擴展主時間線數據
    dlc_timeline_extensions = {
        "ST_38-42": {
            "available_lines": ["dlc_character"],
            "dlc_event": "DLC_01",
            "is_holiday": False
        },
        "ST_42-46": {
            "available_lines": ["dlc_character", "cee"],
            "dlc_event": "DLC_02",
            "cee_event": None,  # 可以與主線並行
            "is_holiday": False
        },
        # ... 更多時間段
    }

    # 註冊到主時間線
    for period, data in dlc_timeline_extensions.items():
        timeline_data[period] = data
```

### 2.4 完全獨立時間線

如果你的 DLC 完全獨立，不需要與主線交互：

```python
# 在 DLC 入口處
label dlc_start:
    # 保存主線狀態
    $ main_source_time = store.source_time
    $ main_current_line = store.current_line

    # 設置 DLC 獨立狀態
    $ store.source_time = 0
    $ store.current_line = "dlc_independent"
    $ store.dlc_independent_mode = True

    jump dlc_prologue

# DLC 結束時
label dlc_end:
    # 恢復主線狀態（如果玩家選擇返回）
    $ store.source_time = main_source_time
    $ store.current_line = main_current_line
    $ store.dlc_independent_mode = False

    jump time_choice_menu
```

---

## 3. 角色擴展

### 3.1 添加新角色

在 `dlc/your_dlc_name/characters.rpy` 中：

```python
# ============================================================================
# 新角色定義
# ============================================================================

define new_char = Character(
    "新角色名",          # 顯示名稱
    color="#FF6B6B",      # 對話框顏色
    what_prefix="「",     # 對話前綴
    what_suffix="」"      # 對話後綴
)

# ============================================================================
# 角色關係狀態
# ============================================================================

# 在 00_setup.rpy 中添加（或使用 default）
default new_char_relationship = "UNMET"

# 關係進程定義（供參考，實際使用直接賦值）
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER

# ============================================================================
# 角色特性定義
# ============================================================================

init python:
    # 角色語言特性（用於跨語言指令錯誤）
    new_char_language_traits = {
        "language": "YourLanguage",
        "has_gc": True,           # 是否有垃圾回收
        "strong_typing": True,    # 是否強型別
        "memory_safety": True,    # 是否記憶體安全
        "concurrency_model": "async"  # 並發模型
    }
```

### 3.2 使用現有角色

DLC 可以直接使用主線角色：

```python
label dlc_event_with_cee:
    scene bg memory_warehouse

    show cee normal at center

    # 檢查關係狀態
    if cee_relationship in ["RELIABLE", "RESONANT", "PARTNER"]:
        cee "你來了。有什麼需要幫忙的？"
    else:
        cee "有事？"

    # 使用好感度系統
    $ track_affection("cee", 10)

    jump end_time_period
```

### 3.3 角色立繪規範

```
images/
├── YourLanguage/
│   ├── char_name normal.png    # 默認表情
│   ├── char_name happy.png     # 開心
│   ├── char_name sad.png       # 難過
│   └── char_name thinking.png  # 思考
```

**命名規則**：
- 使用小寫 + 空格（Ren'Py 會自動處理）
- 格式：`角色名 表情.png`
- 在代碼中使用：`show char_name happy`

---

## 4. 事件與章節創建

### 4.1 主線事件模板

```python
# ============================================================================
# DLC_01: 章節標題
# ============================================================================

label dlc_DLC01_start:
    # 設置場景
    scene bg your_location

    # 顯示角色
    show new_char normal at center

    # 開場白
    narrator "描述場景..."

    new_char "角色的第一句話"

    # 玩家選擇
    menu:
        "選項 A":
            jump dlc_DLC01_choice_a

        "選項 B":
            jump dlc_DLC01_choice_b

        # 條件選項（需要特定關係）
        "特殊選項（需要友好關係）" if new_char_relationship in ["FRIEND", "CLOSE", "PARTNER"]:
            jump dlc_DLC01_choice_special

label dlc_DLC01_choice_a:
    new_char "你選擇了 A"

    # 更新關係
    $ new_char_relationship = "ACQUAINTED"
    $ track_affection("new_char", 5)

    # 標記章節完成
    $ complete_chapter("dlc_01")

    jump end_time_period

label dlc_DLC01_choice_b:
    new_char "你選擇了 B"

    # 可能觸發後果
    $ apply_consequence("minor", ["new_char"], duration=1)

    $ complete_chapter("dlc_01")
    jump end_time_period
```

### 4.2 隨機事件模板

```python
# 添加到 explore_events.rpy 的 all_events 列表

label event_dlc_random_01:
    scene bg your_location
    show new_char normal at center

    narrator "隨機事件描述..."

    new_char "一句話"

    $ track_affection("new_char", 5)

    jump end_time_period
```

### 4.3 假日事件模板

```python
label holiday_dlc:
    scene bg your_location

    if new_char_relationship in ["CLOSE", "PARTNER"]:
        # 高好感度：角色主動邀請
        narrator "新角色主動來找你..."

        new_char "今天沒什麼事，要不要一起..."

        menu:
            "答應":
                jump holiday_dlc_together

            "婉拒":
                jump holiday_dlc_decline

    else:
        # 低好感度：角色自己做自己的事
        narrator "新角色似乎在忙自己的事..."

        jump end_time_period

label holiday_dlc_together:
    # 特殊場景
    scene bg special_location

    narrator "你們一起度過了愉快的時光..."

    $ new_char_relationship = "CLOSE"
    $ track_affection("new_char", 20)

    jump end_time_period
```

---

## 5. 自定義結局

### 5.1 DLC 專屬結局

```python
# dlc/your_dlc_name/endings.rpy

# ============================================================================
# DLC True End
# ============================================================================

label ending_dlc_true:
    scene bg dlc_final_location
    with Fade(3.0, 1.0, 3.0)

    show new_char happy at center

    narrator "結局描述..."

    new_char "最後一句話"

    narrator "【DLC 結局：結局名稱】"
    narrator "結局寓意..."

    # 記錄結局
    $ record_ending("dlc_true_end")

    jump ending_final_ack  # 使用主線鳴謝畫面

# ============================================================================
# DLC Normal End
# ============================================================================

label ending_dlc_normal:
    scene bg dlc_location

    if new_char_relationship in ["FRIEND", "CLOSE"]:
        show new_char normal at center
        new_char "還不錯的結局"
    else:
        narrator "普通的結局..."

    narrator "【DLC 結局：普通結局】"

    $ record_ending("dlc_normal_end")

    jump ending_final_ack
```

### 5.2 與主線結局整合

```python
# 修改 check_ending_conditions() 的行為
init python:
    def check_dlc_ending_conditions():
        # 先檢查 DLC 結局
        dlc_ending = dlc_check_ending()
        if dlc_ending:
            return dlc_ending

        # 如果 DLC 模式啟用，延後主線結局
        if getattr(store, 'dlc_independent_mode', False):
            return "none"

        # 否則使用主線結局邏輯
        return check_ending_conditions()
```

### 5.3 多結局條件設計

```python
init python:
    def dlc_check_ending():
        # 獲取所有相關狀態
        dlc_rel = getattr(store, 'new_char_relationship', 'UNMET')
        main_cee = store.cee_relationship
        main_jawa = store.jawa_relationship
        st = store.source_time

        # True End: DLC 角色最高 + 主線兩角色都高
        if dlc_rel == "PARTNER":
            if main_cee in ["RESONANT", "PARTNER"] and main_jawa in ["SYNCHRONIZED", "PARTNER"]:
                return "dlc_true_end_integration"  # 融合結局

        # Good End: DLC 角色高
        if dlc_rel in ["CLOSE", "PARTNER"]:
            return "dlc_good_end"

        # Normal End: 完成 DLC 主線
        if getattr(store, 'dlc_main_completed', False):
            return "dlc_normal_end"

        # Bad End: DLC 角色低但時間到了
        if st >= 50 and dlc_rel in ["UNMET", "ACQUAINTED"]:
            return "dlc_bad_end"

        return None
```

---

## 6. 後果系統整合

### 6.1 後果等級

| 等級 | 影響範圍 | 使用場景 |
|------|---------|---------|
| `minor` | 當前任務 | 小錯誤，可重試 |
| `moderate` | 角色可用時間 | 中等錯誤，影響後續互動 |
| `severe` | 波及其他角色 | 嚴重錯誤，觸發支線衝突 |
| `fatal` | 觸發緊急事件 | 致命錯誤，強制進入特殊章節 |

### 6.2 使用後果系統

```python
# 輕微後果
$ apply_consequence("minor", ["new_char"], duration=0)

# 中等後果
$ apply_consequence("moderate", ["new_char", "cee"], duration=3)

# 嚴重後果
$ apply_consequence("severe", ["new_char", "cee", "jawa"], duration=5)

# 檢查是否有未清除的後果
if current_consequence != "none":
    narrator "之前的錯誤還在影響著這裡..."
```

### 6.3 跨語言指令錯誤

```python
# 示範：用 C 的指標邏輯操作新角色（如果新角色是高級語言）
label dlc_cross_language_error_demo:
    narrator "你試圖直接操作新角色的內部數據..."

    if new_char_language_traits["strong_typing"]:
        new_char "型別不符。無法直接訪問。"

        # 觸發後果
        $ apply_consequence("minor", ["new_char"], duration=0)
        $ cross_language_error_occurred = True
        $ cross_language_error_type = "pointer_to_high_level"

        jump dlc_error_recovery
```

---

## 7. 文件結構規範

### 7.1 DLC 完整結構

```
rpy/dlc/your_dlc_name/
├── config.rpy              # DLC 配置和元數據
├── characters.rpy          # 新角色定義
├── variables.rpy           # DLC 專用變量
├── timeline.rpy            # 時間線擴展
├── events/
│   ├── DLC_01_intro.rpy    # 第一章節
│   ├── DLC_02_xxx.rpy      # 第二章節
│   ├── random_events.rpy   # 隨機事件
│   └── holidays.rpy        # 假日事件
├── endings.rpy             # 結局
└── hooks.rpy               # 與主線的鉤子
```

### 7.2 config.rpy 模板

```python
# ============================================================================
# DLC 配置文件
# ============================================================================

init python:
    # DLC 元數據
    dlc_info = {
        "id": "your_dlc_name",
        "name": "DLC 顯示名稱",
        "version": "1.0.0",
        "author": "作者名",
        "description": "DLC 簡介",
        "dependencies": [],  # 依賴的其他 DLC
        "conflicts": []      # 衝突的 DLC
    }

    # DLC 選項
    dlc_options = {
        "disable_main_ending": False,     # 是否禁用主線結局
        "independent_timeline": False,    # 是否獨立時間線
        "custom_ending_time": 50,         # 自定義結局時間
        "integrate_with_main": True       # 是否與主線整合
    }

    # 註冊 DLC
    if 'registered_dlcs' not in globals():
        registered_dlcs = []

    registered_dlcs.append(dlc_info)
```

### 7.3 hooks.rpy 模板

```python
# ============================================================================
# DLC 鉤子 - 與主線的整合點
# ============================================================================

# 在主線時間選擇菜單中添加選項
init python:
    # 添加 DLC 地點到廣場菜單
    dlc_location_options = [
        {
            "text": "前往新地點",
            "condition": "store.source_time >= 5",  # 解鎖條件
            "jump": "dlc_location_entry"
        }
    ]

# 在主線結局評估前執行
label hook_before_ending_evaluation:
    # 檢查 DLC 結局條件
    if hasattr(store, 'dlc_check_ending'):
        $ dlc_ending = dlc_check_ending()
        if dlc_ending:
            jump expression dlc_ending

    # 繼續主線結局評估
    jump shared_ending_evaluation

# 在主線假日中添加 DLC 角色選項
label hook_holiday_options:
    menu:
        "找新角色" if new_char_relationship != "UNMET":
            jump holiday_dlc

        "繼續主線":
            return
```

---

## 8. API 參考

### 8.1 時間系統

```python
# 推進時間
advance_source_time(amount)      # 增加 ST
set_source_time(st)              # 設置 ST

# 獲取時間信息
get_current_time_period()        # 返回 "ST_XX-XX"
get_time_period()                # 返回時段描述

# 時間段判斷
if store.source_time < 36:       # 主線期間
if store.source_time >= 36:      # 結局期間
```

### 8.2 關係系統

```python
# 直接設置關係
$ cee_relationship = "FUNCTIONAL"
$ new_char_relationship = "FRIEND"

# 獲取關係等級數值
tier = get_relationship_tier("cee")  # 0-5

# 檢查關係等級
if is_high_relationship("cee", minimum_tier=3):  # RELIABLE+
    # 高好感度邏輯

# 追蹤好感度變化
$ track_affection("cee", 10)  # +10 好感
```

### 8.3 章節進度

```python
# 設置章節狀態
set_chapter_status("c_01", "completed")
get_chapter_status("c_01")  # 返回 "unstarted", "in_progress", "completed", "skipped"

# 便捷函數
complete_chapter("c_01")
skip_chapter("c_01")
```

### 8.4 後果系統

```python
# 應用後果
apply_consequence(level, affected_characters, duration)

# 清除後果
clear_consequence()

# 減少後果持續時間
reduce_consequence_duration(amount)

# 檢查後果
if current_consequence != "none":
    # 有未處理的後果
```

### 8.5 結局系統

```python
# 檢查結局條件
ending = check_ending_conditions()  # 返回結局 ID 或 "none"

# 記錄結局
record_ending("true_end")

# 獲取已觸發的結局
triggered_endings  # 列表
```

---

## 9. 最佳實踐

### 9.1 命名規範

| 類型 | 規範 | 範例 |
|------|------|------|
| Label | `角色_章節ID_動作` | `cee_C01_start`, `dlc_DLC01_choice_a` |
| 變量 | `角色_用途` | `cee_relationship`, `dlc_main_completed` |
| 文件 | `用途_描述.rpy` | `C_01_pointers.rpy`, `DLC_01_intro.rpy` |
| 圖片 | `角色 表情.png` | `cee normal.png`, `new_char happy.png` |

### 9.2 相容性檢查

```python
# 在 DLC 開始時檢查相容性
label dlc_start:
    # 檢查主線版本
    if config.version < "0.2.0":
        narrator "此 DLC 需要主遊戲版本 0.2.0 或更高"
        return

    # 檢查衝突 DLC
    if "conflicting_dlc" in [d["id"] for d in registered_dlcs]:
        narrator "此 DLC 與已安裝的 DLC 衝突"
        return

    jump dlc_prologue
```

### 9.3 存檔相容

```python
# 使用 getattr 處理可能不存在的變量
dlc_var = getattr(store, 'dlc_custom_var', default_value)

# 使用 hasattr 檢查功能是否存在
if hasattr(store, 'some_dlc_function'):
    $ some_dlc_function()
```

### 9.4 效能考量

```python
# 避免在每幀執行的代碼中使用複雜計算
# 使用標誌變量緩存結果

default dlc_computed_once = False
default dlc_cached_result = None

init python:
    def dlc_expensive_check():
        if not store.dlc_computed_once:
            # 複雜計算
            store.dlc_cached_result = complex_computation()
            store.dlc_computed_once = True
        return store.dlc_cached_result
```

---

## 10. 範例模板

### 10.1 最小 DLC 模板

```python
# rpy/dlc/minimal_dlc/config.rpy
init python:
    dlc_info = {
        "id": "minimal_dlc",
        "name": "最小 DLC 範例",
        "version": "1.0.0",
        "author": "開發者"
    }

# rpy/dlc/minimal_dlc/characters.rpy
define mini_char = Character("Mini", color="#00FF00")
default mini_relationship = "UNMET"

# rpy/dlc/minimal_dlc/events/DLC_01.rpy
label mini_DLC01_start:
    scene bg plaza_noon
    show cee normal at left
    show mini_char normal at right

    cee "這位是新來的 Mini。"
    mini_char "你好！"

    menu:
        "歡迎":
            $ mini_relationship = "FRIEND"
            mini_char "謝謝！"

        "點頭":
            $ mini_relationship = "ACQUAINTED"
            mini_char "..."

    $ complete_chapter("mini_01")
    jump end_time_period
```

### 10.2 完整章節模板

```python
# rpy/dlc/template/events/DLC_01_full.rpy

# ============================================================================
# DLC_01: 完整章節模板
# ============================================================================

# 章節元數據（用於調試和文檔生成）
# CHAPTER_META:
#   id: DLC_01
#   title: 章節標題
#   character: new_char
#   tech_concept: 技術概念
#   source_time: ST_XX-XX
#   consequence_level: minor/moderate/severe

label dlc_DLC01_start:
    # ===== 前置條件檢查 =====
    if store.source_time < 10:
        narrator "這個事件還沒解鎖。"
        jump time_choice_menu

    # ===== 場景設置 =====
    scene bg dlc_location
    with Fade(1.0)

    # ===== 角色登場 =====
    show new_char normal at center

    # ===== 開場敘述 =====
    narrator "描述玩家進入場景後看到的景象..."

    # ===== 角色初次對話 =====
    new_char "角色的開場白..."

    # ===== 場景展開 =====
    narrator "進一步描述..."

    # ===== 核心互動 =====
label dlc_DLC01_main_interaction:
    new_char "現在有一個問題需要解決..."

    # 展示「暴力解法」
    narrator "新角色目前的做法是...（低效方案）"

    menu:
        "選項 A - 提供優化解法":
            jump dlc_DLC01_optimal

        "選項 B - 讓他繼續用原方案":
            jump dlc_DLC01_brute_force

        "選項 C - 提出另一種方案":
            jump dlc_DLC01_alternative

        # 條件選項
        "特殊選項（需要高關係）" if new_char_relationship in ["CLOSE", "PARTNER"]:
            jump dlc_DLC01_special

# ===== 分支 A：最優解 =====
label dlc_DLC01_optimal:
    narrator "你提出了更高效的方案..."

    new_char "這個想法很好！"

    # 執行成功
    narrator "新角色執行了你的方案，效果顯著..."

    # 更新狀態
    $ new_char_relationship = "FRIEND"
    $ track_affection("new_char", 15)
    $ efficiency_multiplier = 5.0

    jump dlc_DLC01_end_good

# ===== 分支 B：暴力解法 =====
label dlc_DLC01_brute_force:
    narrator "新角色繼續用原方案..."

    # 執行緩慢
    narrator "過了很久..."

    new_char "完成了。不是很有效率。"

    # 輕微後果
    $ track_affection("new_char", 5)

    jump dlc_DLC01_end_neutral

# ===== 分支 C：替代方案 =====
label dlc_DLC01_alternative:
    narrator "你提出了另一種方案..."

    new_char "這個方案可行，但有局限..."

    # 中等效果
    $ track_affection("new_char", 10)
    $ efficiency_multiplier = 2.0

    jump dlc_DLC01_end_neutral

# ===== 分支 D：特殊選項 =====
label dlc_DLC01_special:
    narrator "基於你們的深厚關係，你直接指出了核心問題..."

    new_char "你說得對。我一直在繞彎路。"

    # 最佳效果
    $ new_char_relationship = "CLOSE"
    $ track_affection("new_char", 25)
    $ efficiency_multiplier = 10.0

    jump dlc_DLC01_end_good

# ===== 結局 A：好結局 =====
label dlc_DLC01_end_good:
    scene bg dlc_location
    show new_char happy at center

    new_char "謝謝你的幫助。我學到了很多。"

    narrator "你和新角色的關係更加親密了..."

    $ complete_chapter("dlc_01")

    jump end_time_period

# ===== 結局 B：普通結局 =====
label dlc_DLC01_end_neutral:
    scene bg dlc_location
    show new_char normal at center

    new_char "任務完成了。"

    $ complete_chapter("dlc_01")

    jump end_time_period
```

---

## 附錄：現有角色參考

### 角色列表

| ID | 名稱 | 語言 | 關係變量 | 關係進程 |
|----|------|------|---------|---------|
| cee | Cee | C | `cee_relationship` | UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER |
| jawa | Jawa | Java | `jawa_relationship` | UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER |
| rusty | Rusty | Rust | `rusty_relationship` | UNMET → ACQUAINTED → TRUSTED → BORROWED → OWNED |
| golly | Golly | Go | `golly_relationship` | UNMET → CONCURRENT → CHANNELLED → SYNCED |
| py | Py | Python | `py_relationship` | UNMET → IMPORTED → RUNNING → PYTHONIC |

### 場景列表

| ID | 場景名 | 用途 |
|----|--------|------|
| `bg memory_warehouse` | 記憶倉庫 | Cee 主場 |
| `bg contract_office` | 契約局 | Jawa 主場 |
| `bg plaza_morning/noon/afternoon/evening/night` | 資訊廣場 | 主選單 |
| `bg laboratory` | 實驗室 | 現實世界 |
| `bg source_realm_entrance` | 源界入口 | 過場 |

---

**版本**: 1.0.0
**最後更新**: 2025-02-25
**維護者**: CodeLoveGame Team
