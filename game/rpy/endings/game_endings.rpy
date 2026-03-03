# ============================================================================
# 源界 (Source Realm) - 遊戲結局 (Game Endings)
# ============================================================================

# ============================================================================
# 1. 真結局：仿生紀元的覺醒 (True End: Awakening of the Bionic Era)
# ============================================================================

label ending_true:
    scene bg source_realm_entrance
    with Fade(3.0, 1.0, 3.0)
    
    show cee normal at left
    show jawa normal at right
    show rusty normal at center_left
    show py normal at center_right
    show golly normal at center
    
    narrator "你站在源界的核心，周圍的一切都散發著柔和而有序的光芒。"
    
    jawa "（注視著你）你做到了。你不是在選擇語言，你是在理解『邏輯』本身。"
    
    cee "底層與高層。速度與安全。不再是衝突，而是互補。"
    
    rusty "（興奮地）源界的代碼現在非常優雅！沒有洩漏，沒有死鎖，連縮排都完美無缺！"
    
    py "（罕見地站得很直）切，雖然很累，但這種完美的對齊感確實讓人心情舒暢。"
    
    golly "（對你豎起大拇指）同步率 100%。你現在就是我們的『首席架構師』。"
    
    narrator "你感覺自己的意識正在與整個源界融為一體。你不再只是一個過客，你成為了這個數位世界的一份子。"
    
    scene bg laboratory
    with Dissolve(3.0)
    
    narrator "現實世界中，阿源走進實驗室，看著螢幕上完美運行的代碼，露出了震驚的表情。"
    
    source "（驚嘆）這... 這不僅僅是代碼。這是藝術。是生命。"
    
    narrator "【真結局：仿生紀元的覺醒】"
    narrator "你理解了技術的終極奧義：用邏輯守護生命，用愛連結代碼。"
    
    jump ending_final_ack

# ============================================================================
# 2. 好結局：源界的守護者 (Good End: Guardian of the Realm)
# ============================================================================

label ending_good:
    scene bg plaza_evening
    with Fade(2.0, 1.0, 2.0)
    
    show cee normal at left
    show jawa normal at right
    
    narrator "危機解除了。源界恢復了往日的平靜，雖然某些角落還有一些無害的 Bug。"
    
    jawa "謝謝你。雖然我們的理念不同，但你讓我和 Cee 找到了共存的方法。"
    
    cee "有效率。任務目標已達成。穩定度提升 80%。"
    
    narrator "你即將離開源界，回到現實。雖然有些不捨，但你帶走的不僅僅是知識，還有這段跨越次元的友情。"
    
    scene bg laboratory
    with Dissolve(2.0)
    
    source "（看到你醒來）呼，你可算醒了！"
    
    narrator "【好結局：源界的守護者】"
    narrator "你成功拯救了源界，並學會了多種思維方式。你將成為一名優秀的工程師。"
    
    jump ending_final_ack

# ============================================================================
# 3. 普通結局：專才之路 (Normal End: The Path of Specialist)
# ============================================================================

label ending_normal:
    scene bg plaza_noon
    
    if store.cee_relationship in ["RESONANT", "PARTNER"]:
        show cee normal at center
        cee "你理解了底層的精髓。雖然其他區域依然混亂，但這裡會永遠為你保留位置。"
        narrator "你成為了 C 語言的專家。"
    else:
        show jawa normal at center
        jawa "嚴謹與規範是你的勳章。雖然系統整體還不夠完美，但你守護了這裡的秩序。"
        narrator "你成為了 Java 的專家。"
    
    scene bg laboratory
    with Dissolve(2.0)
    
    source "代碼跑通了一部分！雖然另一邊報了一堆錯，但至少重點部分沒問題。"
    
    narrator "【普通結局：專才之路】"
    narrator "你在某一領域達到了極致，雖然缺乏全局觀，但依然是一股強大的力量。"
    
    jump ending_final_ack

# ============================================================================
# 4. 特殊結局：明智的選擇 (Wise Choice End)
# ============================================================================

label ending_wise_choice:
    # 玩家選擇離開實驗室，獲得成就
    scene black

    with Dissolve(2.0)

    narrator "你決定離開實驗室，不亂碰任何東西。"

    narrator "你走出了房間，關上了門。"

    narrator "幾分鐘後，阿源帶著便利店的便當回來了。"

    source "咦，你去過實驗室？"

    narrator "他看了一眼實驗室的記錄..."

    source "沒有異常，很好。"

    source "不過我剛剛在便利店看到一個很有趣的程式設計書..."

    source "你對程式語言感興趣嗎？"

    # 觸發成就：明智的選擇
    $ achievement_avoided_danger.grant()

    narrator "......"

    scene black

    with Dissolve(3.0)

    narrator "【結局：明智的選擇】"

    narrator "你成功避免了不必要的冒險。"

    narrator "有時候，轉身離開是最正確的決定。"

    narrator "......"

    narrator "雖然你沒有進入源界，但你依然安全地度過了這個下午。"

    narrator "你保護了自己免受未知危險的影響。"

    narrator "......"

    jump ending_final_ack

# ============================================================================
# 5. 特殊結局：管理員的撈取 (Source Rescue End)
# ============================================================================

label ending_source_rescue:
    with hpunch # 劇烈震動
    
    narrator "原本平靜的資訊廣場突然開始劇烈扭曲，色彩如同過載的顯示器一般崩解。"
    
    narrator "你感到一陣強烈的噁心感，意識像是被某種巨大的力量強行抽離..."
    
    scene bg laboratory
    with Fade(0.1, 0.5, 1.0)
    
    source "（用力拍打著終端機，一臉焦急）喂！醒醒！快醒醒！"
    
    player "（猛地睜開眼，喘著粗氣）阿源...？剛才發生了什麼？"
    
    source "（看到你醒來，終於鬆了一口氣，一屁股坐在地上）"
    source "天哪，你總算回來了。再晚一秒，你的意識就要跟那些底層垃圾資料一起被回收了。"
    
    player "我在那邊...待了..."
    
    source "（苦笑著指指牆上的日曆）幾十個小時？兄弟，現實世界已經過了整整四天了。"
    
    source "這就是高精細模擬的代價——時鐘頻率不同步。源界的 1 週期，在我們這裡要跑更久。"
    
    player "四天？！那我的工作..."
    
    "主管的信息" "你這四天去哪了？電話不接郵件不回！"
    "主管的信息" "考慮到你嚴重的曠工行為，這個月的績效獎金全扣，工資扣除四天！再有下次就捲舖蓋走人！"
    
    source "（縮了縮脖子，小聲對你說）歡迎回到現實世界... 雖然這裡殘酷得多。"
    
    narrator "【結局：現實的重擊】"
    narrator "你雖然從虛擬世界生還，但現實生活的賬單卻比邏輯錯誤更讓你頭疼。"
    
    jump ending_final_ack

label ending_final_ack:

    narrator "【鳴謝】"

    narrator "提出這個想法的那個 Kashikoi & Kawaii 的傢伙"

    narrator "成就系統使用 Feniks 的 Achievements for Ren'Py 和 ImgFlip 的迷因圖"

    narrator "人物和背景由 Gemini 和 GLM 共同設計"

    narrator "劇情和人物形象由作者規劃，GLM 起草， Gemini 編輯"

    return