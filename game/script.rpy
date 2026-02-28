# 源界 (Source Realm) - 主腳本入口

# ============================================================================
# 導入所有系統文件
# ============================================================================

# 系統初始化
init:
    # 系統文件會被 Ren'Py 自動加載
    # 00_setup.rpy - 初始化和變量定義
    # 01_characters.rpy - 角色定義
    # 02_timeline.rpy - 時間線系統
    # 03_fsm.rpy - FSM 狀態機
    # 04_consequence.rpy - 後果系統
    # 05_algorithm_interaction.rpy - 算法互動系統

    # 章節腳本
    # chapters/prologue.rpy - 序章
    # chapters/cee/*.rpy - Cee 線章節
    # chapters/jawa/*.rpy - Jawa 線章節
    # chapters/shared/*.rpy - 共同事件

    # 結局腳本
    # endings/*.rpy - 各種結局

    pass

# ============================================================================
# 遊戲開始
# ============================================================================

label start:
    # 從序章開始
    jump prologue_start
