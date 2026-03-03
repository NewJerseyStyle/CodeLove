# 源界 (Source Realm) - DLC 開發快速參考

> 📌 一頁式快速參考，詳細說明請見 [DLC_DEVELOPER_GUIDE.md](DLC_DEVELOPER_GUIDE.md)

---

## 區域導向設計（推薦）

DLC 採用**區域導向**設計，每個 DLC 擁有自己的獨立區域。

```
廣場（主線樞紐）
    ├── 記憶倉庫（Cee）
    ├── 契約局（Jawa）
    └── [前往其他區域]        ← 自動顯示已註冊的 DLC 區域
            ├── Zen Garden（Py-DLC）
            └── 你的區域
```

---

## 註冊區域

```python
# config.rpy
init python:
    register_dlc_region("your_region", {
        "name": "Your Region",
        "description": "描述",
        "dlc_id": "your_dlc",
        "entry_label": "enter_your_region",
        "unlock_condition": lambda: store.c_01_status == "completed",
    })
```

---

## 動態菜單注意事項

Ren'Py 的 `renpy.display_menu()` **不支持空白縮排**。

**錯誤做法**（空白會被忽略）：
```python
choices = [
    ("  子選項 1", "option1"),  # ❌ 空白被忽略
    ("    子選項 2", "option2"),  # ❌ 空白被忽略
]
selection = renpy.display_menu(choices)
```

**正確做法**（使用全角空格 `　`）：
```python
choices = [
    (u"　子選項 1", "option1"),     # ✅ 使用全角空格
    (u"　　子選項 2", "option2"),  # ✅ 多個全角空格
]
selection = renpy.display_menu(choices)
```

**其他空白字符選項**：
- `\u2003` (EM SPACE) - 較寬的空格
- `\u3000` (IDEOGRAPHIC SPACE) - 全角空格（推薦）

---

## 區域入口模板

```renpy
# events/region_hub.rpy

label enter_your_region:
    scene bg your_region with fade
    narrator "你來到了 Your Region。"
    jump your_region_hub

label your_region_hub:
    scene bg your_region
    show your_char normal at center

    menu:
        "和 Your Char 學習":
            jump your_event
        "返回廣場":
            jump return_to_plaza

label return_to_plaza:
    scene black with fade
    narrator "你返回了廣場。"
    jump time_choice_menu
```

---

## DLC 註冊 API

```python
init python:
    # 註冊 DLC
    register_dlc({
        "id": "my_dlc",
        "name": "我的 DLC",
        "version": "1.0.0",
        "author": "開發者",
        "ending_checker": my_dlc_check_ending,  # 可選
    })

    # 註冊區域
    register_dlc_region("region_id", {...})

    # 註冊角色
    register_dlc_character("char_id", {...})

    # 註冊隨機事件
    register_dlc_random_event("event_label", weight=1.0)
```

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
get_current_time_period()   # "ST_09-12"
```

### 關係
```python
$ cee_relationship = "FUNCTIONAL"              # 直接設置
track_affection("cee", 10)                     # +10 好感
```

### 章節
```python
complete_chapter("c_01")    # 標記完成
```

### 後果
```python
apply_consequence("minor", ["cee"], duration=0)
```

---

## 文件結構

```
rpy/dlc/your_dlc/
├── config.rpy          # DLC 配置 + 區域註冊
├── characters.rpy      # 新角色
├── events/
│   ├── region_hub.rpy  # 區域樞紐（必需）
│   └── CHAPTER_01.rpy  # 章節事件
└── endings.rpy         # 結局
```

---

## Label 命名規範

| 類型 | 格式 | 範例 |
|------|------|------|
| 區域入口 | `enter_region_name` | `enter_zen_garden` |
| 區域樞紐 | `region_hub` | `zen_garden_hub` |
| 章節 | `CHAPTER_ID` | `PY_01` |
| 結局 | `ending_name` | `ending_py_partner` |

---

## 關係進程模板

```python
# 主線角色
Cee:   UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER
Jawa:  UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER

# DLC 角色
default my_char_relationship = "UNMET"
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
```

---

## 快速檢查清單

- [ ] 使用 `register_dlc()` 註冊
- [ ] 使用 `register_dlc_region()` 註冊區域
- [ ] 創建區域入口 label（`enter_your_region`）
- [ ] 創建區域樞紐菜單（`your_region_hub`）
- [ ] 提供「返回廣場」選項（`jump return_to_plaza`）
- [ ] 角色變量用 `default` 聲明
- [ ] 圖片放在 `images/YourLanguage/`

---

## 完整範例

見 [CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC) - 完整可運行的區域導向 DLC 範例
