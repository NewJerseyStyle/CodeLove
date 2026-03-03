# 源界 (Source Realm) - DLC 開發快速參考

> 📌 一頁式快速參考，詳細說明請見 [DLC_DEVELOPER_GUIDE.md](DLC_DEVELOPER_GUIDE.md)

---

## 核心變量

```python
# 時間
store.source_time           # 當前 ST (0-36+ 主線)

# 關係狀態
store.cee_relationship      # UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER
store.jawa_relationship     # UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER

# 章節狀態
store.c_01_status           # "unstarted", "in_progress", "completed", "skipped"
```

---

## 常用 API

### 時間
```python
advance_source_time(2)      # +2 ST
set_source_time(10)         # ST = 10
get_current_time_period()   # "ST_09-12"
```

### 關係
```python
$ cee_relationship = "FUNCTIONAL"              # 直接設置
get_relationship_tier("cee")                   # 0-5
is_high_relationship("cee", minimum_tier=3)    # True/False
track_affection("cee", 10)                     # +10 好感
```

### 章節
```python
complete_chapter("c_01")    # 標記完成
skip_chapter("c_01")        # 標記跳過
get_chapter_status("c_01")  # 獲取狀態
```

### 後果
```python
apply_consequence("minor", ["cee"], duration=0)
apply_consequence("moderate", ["cee", "jawa"], duration=3)
clear_consequence()
```

### 結局
```python
check_ending_conditions()   # 返回結局 ID 或 "none"
record_ending("true_end")   # 記錄結局
```

---

## DLC 註冊

```python
init python:
    register_dlc({
        "id": "my_dlc",
        "name": "我的 DLC",
        "version": "1.0.0",
        "author": "開發者",
        "ending_checker": my_dlc_check_ending,
        "timeline_data": {
            "ST_38-42": {"dlc_event": "DLC_01", ...}
        }
    })
```

---

## Label 命名規範

| 類型 | 格式 | 範例 |
|------|------|------|
| 章節開始 | `角色_章節_start` | `cee_C01_start` |
| 選擇分支 | `角色_章節_選項` | `cee_C01_choice_a` |
| 隨機事件 | `event_描述` | `event_rusty_safety_check` |
| 結局 | `ending_名稱` | `ending_true` |

---

## 標準章節結構

```python
label dlc_DLC01_start:
    # 1. 前置檢查
    if store.source_time < 10:
        jump time_choice_menu

    # 2. 場景設置
    scene bg location
    show char normal at center

    # 3. 對話
    char "對話內容"

    # 4. 選項
    menu:
        "選項 A":
            jump dlc_DLC01_a
        "選項 B":
            jump dlc_DLC01_b

label dlc_DLC01_a:
    # 5. 更新狀態
    $ char_relationship = "FRIEND"
    $ track_affection("char", 10)
    $ complete_chapter("dlc_01")

    # 6. 結束
    jump end_time_period
```

---

## 圖片命名

```
images/
└── YourLanguage/
    ├── char normal.png     # show char normal
    ├── char happy.png      # show char happy
    └── char sad.png        # show char sad
```

---

## 文件結構

```
rpy/dlc/your_dlc/
├── config.rpy          # DLC 配置
├── characters.rpy      # 新角色
├── events/             # 事件文件
├── endings.rpy         # 結局
└── hooks.rpy           # 鉤子
```

---

## 關係進程模板

```python
# 主線角色
Cee:   UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER
Jawa:  UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER

# 自定義角色
default my_char_relationship = "UNMET"
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
```

---

## 快速檢查清單

- [ ] 使用 `register_dlc()` 註冊
- [ ] 角色變量用 `default` 聲明
- [ ] Label 遵循命名規範
- [ ] 章節結束用 `jump end_time_period`
- [ ] 更新關係用 `$ char_relationship = "X"`
- [ ] 完成章節用 `complete_chapter("id")`
- [ ] 圖片放在 `images/YourLanguage/`
