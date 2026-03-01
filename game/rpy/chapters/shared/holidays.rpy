# ============================================================================
# 源界 (Source Realm) - 日常與假日事件 (Daily Slices & Holidays)
# ============================================================================

init python:
    import random

# ============================================================================
# Jawa 的日常
# ============================================================================

label holiday_A:
    $ event_variant = random.choice(["reading", "coffee"])
    jump expression f"jawa_daily_{event_variant}"

label jawa_daily_reading:
    scene bg information_square_afternoon
    show jawa normal at center
    narrator "你在資訊廣場偶遇了 Jawa。她正專心地讀著一本厚厚的手冊。"
    jawa "（抬頭）是你。今天不是工作時間，為什麼不休息一下？"
    player "看到你在這，就過來打個招呼。你在讀什麼？"
    jawa "一些關於『分散式共識算法』的論文。雖然是假日，但系統的優化是永無止境的。"
    player "Jawa，你總是這麼認真。休息也是優化的一部分哦。"
    jawa "（沉默片刻）休息也是優化... 很有趣的說法。我會考慮的。"
    $ track_affection("jawa", 5)
    jump end_time_period

label jawa_daily_coffee:
    scene bg coffee_shop_interior
    show jawa normal at center
    narrator "你在咖啡廳遇到了正在精確測量咖啡溫度的 Jawa。"
    jawa "精確到 88.5 度是萃取的最佳規範。溫度誤差超過 0.5 度都會導致口感的非預期行為。"
    player "這聽起來像是某種嚴格的編譯檢查。"
    jawa "（露出極淡的微笑）你可以這麼理解。規則讓咖啡更美味。"
    $ track_affection("jawa", 8)
    jump end_time_period

# ============================================================================
# Cee 的日常
# ============================================================================

label holiday_B:
    $ event_variant = random.choice(["river", "sorting"])
    jump expression f"cee_daily_{event_variant}"

label cee_daily_river:
    scene bg memory_warehouse_river
    show cee normal at center
    narrator "你在記憶倉庫的最深處找到了 Cee。她正看著前方流動的『記憶之河』。"
    cee "位址流動。0 到 無限。這就是源界的生命線。"
    player "這裡很美，Cee。"
    cee "（轉頭）工作之外。觀察資料的自然演化。這能幫我理解系統的邊界。"
    $ track_affection("cee", 5)
    jump end_time_period

label cee_daily_sorting:
    scene bg memory_warehouse_aisle
    show cee normal at center
    narrator "你看到 Cee 正在強迫症發作般地調整一排書的高度。"
    cee "（小聲）這本書的位址雖然正確，但物理高度偏離了 2 毫米。無效率的視覺佈局。"
    player "我幫你一起搬吧。"
    cee "（臉紅）嗯。手動對齊。加速中。"
    $ track_affection("cee", 8)
    jump end_time_period

# ============================================================================
# Rusty 的日常
# ============================================================================

label rusty_daily_safety:
    scene bg information_square_corner
    show rusty normal at center
    narrator "你看到 Rusty 正在檢查廣場噴泉的圍欄。"
    rusty "萬一有人在這裡發生空指針引用掉下去怎麼辦！我必須安裝更多的溢位保護！"
    player "你真的很注重安全呢，Rusty。"
    rusty "（認真地）因為安全是不可變的權利！"
    $ track_affection("rusty", 5)
    jump end_time_period

# ============================================================================
# Py 的日常
# ============================================================================

label py_daily_nap:
    scene bg information_square_park
    show py normal at center
    narrator "Py 正在草地上尋找最完美的午睡陰影。"
    py "這裡的光線縮排剛好是四格，完美。新來的，要一起躺會兒嗎？"
    player "你每天都在睡覺嗎？"
    py "這叫『延遲載入（Lazy Loading）』。不到真正需要的時候，絕對不浪費能量。"
    $ track_affection("py", 5)
    jump end_time_period
