# ============================================================================
# 源界 (Source Realm) - 03: 關係狀態定義
# ============================================================================
#
# 關係狀態說明：
#
# Cee (C 語言) 關係進程：
#   UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER/CLOSE_ALLY
#
# Jawa (Java) 關係進程：
#   UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER/DEEP_ALLY
#
# 使用方式（在章節中直接賦值）：
#   $ cee_relationship = "FUNCTIONAL"
#   $ jawa_relationship = "TRUSTED"
#
# 檢查關係狀態（在條件判斷中使用）：
#   if cee_relationship in ["RELIABLE", "RESONANT"]:
#       # 觸發高好感度對話
#
# 注意：複雜的 FSM 轉換系統已移除，採用直接賦值方式。
# 如需擴展新角色，請參考現有章節模板。
# ============================================================================

# 關係狀態已在 00_setup.rpy 中定義：
# default cee_relationship = "UNMET"
# default jawa_relationship = "UNMET"

# ============================================================================
# 關係進展輔助函數
# ============================================================================

init python:
    def get_relationship_tier(character):
        """
        獲取關係等級數值（用於比較）

        Cee:  UNMET=0, FIRST_CONTACT=1, FUNCTIONAL=2, RELIABLE=3, RESONANT=4, PARTNER=5
        Jawa: UNMET=0, FORMAL_CONTACT=1, VERIFIED=2, TRUSTED=3, SYNCHRONIZED=4, PARTNER=5
        """
        tiers = {
            "UNMET": 0,
            "FIRST_CONTACT": 1, "FORMAL_CONTACT": 1,
            "FUNCTIONAL": 2, "VERIFIED": 2,
            "RELIABLE": 3, "TRUSTED": 3,
            "RESONANT": 4, "SYNCHRONIZED": 4,
            "PARTNER": 5, "CLOSE_ALLY": 5, "DEEP_ALLY": 5
        }

        relationship = getattr(store, character + "_relationship", "UNMET")
        return tiers.get(relationship, 0)

    def is_high_relationship(character, minimum_tier=3):
        """
        檢查是否達到指定關係等級

        minimum_tier: 0=UNMET, 1=*_CONTACT, 2=FUNCTIONAL/VERIFIED,
                      3=RELIABLE/TRUSTED, 4=RESONANT/SYNCHRONIZED, 5=PARTNER
        """
        return get_relationship_tier(character) >= minimum_tier
