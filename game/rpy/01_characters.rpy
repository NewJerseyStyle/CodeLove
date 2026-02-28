# ============================================================================
# 源界 (Source Realm) - 01: 角色定義
# ============================================================================

# ============================================================================
# 1. Cee（C 語言）
# ============================================================================

define cee = Character(
    "Cee",
    color="#FF6B6B",  # 珊瑚紅 - 既有活力又專業
)

# Cee 表情系統（待實際立繪資源後啟用）
# define cee_neutral = Character("Cee", image="cee neutral", color="#FF6B6B")
# define cee_thinking = Character("Cee", image="cee thinking", color="#FF6B6B")
# define cee_evaluating = Character("Cee", image="cee evaluating", color="#FF6B6B")
# define cee_freeze = Character("Cee", image="cee freeze", color="#FF6B6B")

# ============================================================================
# 2. Jawa（Java 語言）
# ============================================================================

define jawa = Character(
    "Jawa",
    color="#6B5B95",  # 深紫色 - 穩重、專業、可靠
)

# Jawa 表情系統
# define jawa_neutral = Character("Jawa", image="jawa neutral", color="#6B5B95")
# define jawa_formal = Character("Jawa", image="jawa formal", color="#6B5B95")
# define jawa_gc_pause = Character("Jawa", image="jawa gc pause", color="#6B5B95")
# define jawa_thinking = Character("Jawa", image="jawa thinking", color="#6B5B95")

# ============================================================================
# 3. Rusty（Rust 語言） - Cee 的後輩
# ============================================================================

define rusty = Character(
    "Rusty",
    color="#FFA502",  # 橘色 - 年輕、充滿活力但謹慎
)

# Rusty 表情系統
# define rusty_neutral = Character("Rusty", image="rusty neutral", color="#FFA502")
# define rusty_cautious = Character("Rusty", image="rusty cautious", color="#FFA502")
# define rusty_confirmed = Character("Rusty", image="rusty confirmed", color="#FFA502")

# ============================================================================
# 4. Golly（Go 語言）
# ============================================================================

define golly = Character(
    "Golly",
    color="#00D2D3",  # 淺藍色 - 輕鬆、直接、高效
)

# Golly 表情系統
# define golly_neutral = Character("Golly", image="golly neutral", color="#00D2D3")
# define golly_thinking = Character("Golly", image="golly thinking", color="#00D2D3")
# define golly_multitasking = Character("Golly", image="golly multitasking", color="#00D2D3")

# ============================================================================
# 5. 阿源（Source） - 現實世界的錨點
# ============================================================================

define source = Character(
    "阿源",
    color="#26DE81",  # 綠色 - 現實、接地氣、穩定
)

# 阿源表情系統
# define source_neutral = Character("阿源", image="source neutral", color="#26DE81")
# define source_concerned = Character("阿源", image="source concerned", color="#26DE81")
# define source_serious = Character("阿源", image="source serious", color="#26DE81")

# ============================================================================
# 6. 玩家（主角）
# ============================================================================

define player = Character(
    "你",
    color="#FFEAA7",  # 淡黃色 - 中性、溫和
)

# 玩家內心獨白
define thought = Character(
    None,  # 無名字，只顯示內容
    what_prefix="（",
    what_suffix="）",
    who_color="#FFEAA7",
    what_italic=True
)

# 系統提示（用於教學、後果說明等）
define system = Character(
    "系統",
    color="#95A5A6",  # 灰色 - 中性、客觀
    what_prefix="【",
    what_suffix="】"
)

# 教學卡片（用於技術概念教學）
define teaching = Character(
    "知識點",
    color="#E74C3C",  # 紅色 - 重要資訊
    what_prefix="▶ ",
    what_suffix=""
)

# 便條（用於顯示便條內容）
define note = Character(
    "便條",
    color="#2C3E50",  # 深藍灰色 - 像紙張的顏色
)

# ============================================================================
# 7. 敘事者（旁白）
# ============================================================================

define narrator = Character(None)

# ============================================================================
# 8. 角色關係 FSM 變量
# ============================================================================

# Cee 關係狀態：UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER/CLOSE_ALLY
default cee_relationship = "UNMET"

# Jawa 關係狀態：UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER/DEEP_ALLY
default jawa_relationship = "UNMET"

# Rusty 關係狀態（簡化版本）
default rusty_relationship = "UNMET"

# Golly 關係狀態（簡化版本）
default golly_relationship = "UNMET"

# ============================================================================
# 9. 角色狀態變量（用於 FSM 狀態機）
# ============================================================================

# Cee 當前狀態（用於對話分支）
default cee_current_state = "neutral"

# Jawa 當前狀態
default jawa_current_state = "formal"

# Jawa 是否在 GC 暫停中
default jawa_in_gc_pause = False

# Jawa GC 暫停持續時間（剩餘 ST）
default jawa_gc_pause_duration = 0

# ============================================================================
# 10. 角色特有能力變量
# ============================================================================

# Cee 的執行速度倍數（基礎 1.0，受玩家算法建議影響）
default cee_execution_speed = 1.0

# Cee 的記憶體空間利用率
default cee_memory_usage = 0.7

# Jawa 的規格文件完成度
default jawa_specs_completed = 0.5

# Jawa 的 GC 頻率（0-1）
default jawa_gc_frequency = 0.3

# Rusty 的安全審查嚴格度（0-1）
default rusty_strictness = 0.8

# Golly 的並行任務數量
default golly_concurrent_tasks = 0

# ============================================================================
# 11. 角色系統函數 - 關係 FSM 管理
# ============================================================================

init python:
    def set_relationship(character, state):
        """設置角色關係狀態"""
        setattr(store, character + "_relationship", state)

    def get_relationship(character):
        """獲取角色關係狀態"""
        return getattr(store, character + "_relationship", "UNMET")

    def can_progress_relationship(character, current_state, next_state):
        """檢查是否可以進入下一個關係階段"""
        fsm_transitions = {
            "cee": {
                "UNMET": ["FIRST_CONTACT"],
                "FIRST_CONTACT": ["FUNCTIONAL"],
                "FUNCTIONAL": ["RELIABLE"],
                "RELIABLE": ["RESONANT"],
                "RESONANT": ["PARTNER", "CLOSE_ALLY"]
            },
            "jawa": {
                "UNMET": ["FORMAL_CONTACT"],
                "FORMAL_CONTACT": ["VERIFIED"],
                "VERIFIED": ["TRUSTED"],
                "TRUSTED": ["SYNCHRONIZED"],
                "SYNCHRONIZED": ["PARTNER", "DEEP_ALLY"]
            }
        }

        valid_transitions = fsm_transitions.get(character, {})
        current_valid_transitions = valid_transitions.get(current_state, [])

        return next_state in current_valid_transitions

    def progress_relationship(character, new_state):
        """嘗試進入下一個關係階段"""
        current_state = get_relationship(character)

        if can_progress_relationship(character, current_state, new_state):
            set_relationship(character, new_state)
            return True
        else:
            # 不合法的狀態轉換，記錄錯誤
            return False

    def get_cee_dialogue_style():
        """根據 Cee 當前關係狀態返回對話風格"""
        state = store.cee_relationship

        if state == "UNMET":
            return "neutral"  # 極度中性，字句短
        elif state == "FIRST_CONTACT":
            return "formal"  # 型別確認語氣
        elif state == "FUNCTIONAL":
            return "functional"  # 偶爾有簡短觀察
        elif state == "RELIABLE":
            return "reliable"  # 術語減少，更直接
        elif state in ["RESONANT", "PARTNER", "CLOSE_ALLY"]:
            return "resonant"  # 話更少，但每句都精準
        else:
            return "neutral"

    def get_jawa_dialogue_style():
        """根據 Jawa 當前關係狀態返回對話風格"""
        state = store.jawa_relationship

        if state == "UNMET":
            return "formal"
        elif state == "FORMAL_CONTACT":
            return "very_formal"  # 極度正式
        elif state == "VERIFIED":
            return "standard_formal"  # 標準正式
        elif state == "TRUSTED":
            return "semi_formal"  # 半正式
        elif state in ["SYNCHRONIZED", "PARTNER", "DEEP_ALLY"]:
            return "trust"  # 信任但仍保持結構
        else:
            return "formal"

# ============================================================================
# 12. 角色系統函數 - 特殊行為
# ============================================================================

init python:
    def is_jawa_in_gc_pause():
        """檢查 Jawa 是否在 GC 暫停中"""
        return store.jawa_in_gc_pause

    def trigger_jawa_gc_pause(duration):
        """觸發 Jawa GC 暫停"""
        store.jawa_in_gc_pause = True
        store.jawa_gc_pause_duration = duration

    def update_jawa_gc_pause(amount):
        """更新 Jawa GC 暫停狀態"""
        if store.jawa_in_gc_pause:
            store.jawa_gc_pause_duration -= amount
            if store.jawa_gc_pause_duration <= 0:
                store.jawa_in_gc_pause = False
                store.jawa_gc_pause_duration = 0

    def get_cee_available_time():
        """獲取 Cee 當前可用時間（受後果影響）"""
        base_time = 100  # 基礎可用時間
        reduction = store.cee_available_time_reduction
        return max(0, base_time - reduction)

    def can_cee_interact():
        """檢查 Cee 是否可以進行互動（受時間和後果影響）"""
        if store.cee_available_time_reduction > 50:
            return False
        if store.current_consequence in ["severe", "fatal"] and store.cee_affected_by_consequence:
            return False
        return True

# ============================================================================
# 13. 角色系統函數 - 對話助手
# ============================================================================

init python:
    def cee_says(dialogue, style_override=None):
        """Cee 對話助手（自動根據關係調整風格）"""
        style = style_override or get_cee_dialogue_style()

        # 根據不同風格添加前綴或修改語氣
        if style == "neutral":
            cee(dialogue)
        elif style == "formal":
            # 型別確認語氣，簡短直接
            cee(dialogue)
        elif style == "functional":
            # 偶爾有簡短評價
            cee(dialogue)
        elif style == "reliable":
            # 術語減少
            cee(dialogue)
        elif style == "resonant":
            # 精準、極簡
            cee(dialogue)
        else:
            cee(dialogue)

    def jawa_says(dialogue, style_override=None):
        """Jawa 對話助手（自動根據關係調整風格）"""
        style = style_override or get_jawa_dialogue_style()

        if store.jawa_in_gc_pause:
            # GC 暫停時不回應，返回一個標記
            return "gc_pause"

        # 直接返回對話文本和角色
        return (jawa, dialogue)

# ============================================================================
# 14. 角色登場/退場函數
# ============================================================================

label show_character(character, position, expression="neutral"):
    python hide:
        # 根據角色和表情顯示對應立繪
        # 這裡先使用文字占位符，待實際立繪資源後替換
        pass

label hide_character(character):
    python hide:
        # 隱藏角色
        pass
