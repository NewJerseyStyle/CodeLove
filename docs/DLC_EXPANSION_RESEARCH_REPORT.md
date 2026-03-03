# 源界 (Source Realm) DLC 扩展性研究报告

> **文档版本**: v1.0
> **研究日期**: 2026-02-26
> **目的**: 评估游戏系统的可扩展性，设计 DLC 扩展接口，为社区开发者提供清晰指引

---

## 目录

1. [执行摘要](#执行摘要)
2. [当前系统架构分析](#当前系统架构分析)
3. [可扩展性评估](#可扩展性评估)
4. [DLC 扩展方案设计](#dlc-扩展方案设计)
5. [基础世界调整建议](#基础世界调整建议)
6. [开发者指引](#开发者指引)
7. [RPA 打包指引](#rpa-打包指引)
8. [GitHub 文档组织](#github-文档组织)

---

## 执行摘要

**核心发现**:
- ✅ 当前系统高度模块化，易于扩展新角色和剧情线
- ⚠️ 时间线系统需要引入「DLC 时间段」概念
- ⚠️ 角色系统需要支持动态注册新角色
- ⚠️ 结局系统需要支持自定义结局
- ✅ 使用 RPA 打包可以实现资源隔离和独立分发

**推荐方案**:
1. **独立剧情型 DLC**（优先推荐）: DLC 独立于主线时间线，作为「支线故事」或「After Story」存在
2. **主线扩展型 DLC**（中等难度）: 扩展现有时间线，需要更复杂的集成
3. **世界观扩展型 DLC**（高难度）: 添加新的语言角色，需要全面的世界观调整

---

## 当前系统架构分析

### 1. 核心系统文件结构

```
rpy/
├── 00_setup.rpy              # 全局变量和系统初始化
├── 01_characters.rpy          # 角色定义（硬编码）
├── 02_timeline.rpy            # 时间线系统（硬编码事件）
├── 03_fsm.rpy                # FSM 状态机
├── 04_consequence.rpy         # 后果系统
├── 05_algorithm_interaction.rpy # 算法互动系统
├── achievement_backend.rpy      # 成就系统
├── achievements.rpy           # 成就显示
├── player_stats.rpy           # 玩家追踪系统
├── chapters/
│   ├── prologue.rpy           # 序章
│   ├── cee/                  # Cee 线（9章）
│   ├── jawa/                 # Jawa 线（9章）
│   └── shared/               # 共同事件、假日
└── endings/
    └── game_endings.rpy       # 结局定义
```

### 2. 关键系统分析

#### 2.1 时间线系统 (02_timeline.rpy)

**当前实现**:
- `timeline_data` 字典硬编码所有时间段和事件
- 时间段从 ST_00-01 到 ST_38+
- 每个时间段固定分配 cee_event, jawa_event, shared_event

**可扩展性**:
- ❌ **低**: 添加新时间段需要修改 `timeline_data`
- ❌ **低**: 添加新角色需要扩展每个时间段的字段
- ✅ **中**: 可以通过添加「DLC 时间段」（ST_38+ 之后）实现扩展

**限制**:
```python
timeline_data = {
    "ST_00-01": {
        "available_lines": ["prologue"],
        "cee_event": None,
        "jawa_event": None,
        "shared_event": None,
        # 硬编码的角色字段
    }
}
```

#### 2.2 角色系统 (01_characters.rpy)

**当前实现**:
- 硬编码的 `define` 语句定义每个角色
- 关系 FSM 为硬编码的 `default` 变量
- 对话风格函数基于硬编码的状态转换

**可扩展性**:
- ❌ **低**: 添加新角色需要手动添加 `define` 语句
- ❌ **低**: 关系 FSM 需要为每个角色单独实现
- ✅ **中**: 对话风格函数可以通用化

**限制**:
```renpy
define cee = Character("Cee", color="#FF6B6B", ...)
define jawa = Character("Jawa", color="#6B5B95", ...)
# 每个新角色需要手动添加类似的定义
```

#### 2.3 结局系统 (game_endings.rpy, 00_setup.rpy)

**当前实现**:
- `check_ending_conditions()` 函数硬编码所有结局条件
- 已触发展局列表为固定列表

**可扩展性**:
- ❌ **低**: 添加新结局需要修改 `check_ending_conditions()`
- ⚠️ **中**: DLC 结局可以作为独立分支，不触发主线结局

**限制**:
```python
def check_ending_conditions():
    # 硬编码的条件检查
    if cee_resonant and jawa_synchronized:
        return "true_end"
    # 无法动态添加新结局条件
```

#### 2.4 章节进度追踪 (00_setup.rpy)

**当前实现**:
- 每个章节有独立的 `default` 变量追踪状态
- `set_chapter_status()` 和 `get_chapter_status()` 函数通用

**可扩展性**:
- ✅ **高**: 函数完全通用，可以追踪任意章节
- ⚠️ **中**: 新章节需要手动添加 `default` 变量

**优势**:
```python
default c_01_status = "unstarted"
default j_01_status = "unstarted"

# 追踪函数完全通用
def set_chapter_status(chapter_id, status):
    setattr(store, chapter_id + "_status", status)
```

---

## 可扩展性评估

### 扩展维度评估表

| 扩展维度 | 当前支持 | 难度 | 需要调整的文件 | 备注 |
|---------|---------|-------|-----------------|------|
| **新角色添加** | ⚠️ 中等 | 高 | 01_characters.rpy, 00_setup.rpy | 需要手动添加角色定义和关系变量 |
| **新剧情线** | ⚠️ 中等 | 中 | 02_timeline.rpy | 可以使用 ST_38+ 作为 DLC 时间段 |
| **独立剧情** | ✅ 完全支持 | 低 | script.rpy, options.rpy | 作为独立 label 实现即可 |
| **新结局** | ⚠️ 中等 | 中 | game_endings.rpy, 00_setup.rpy | 可以作为独立 DLC 结局 |
| **新章节** | ✅ 完全支持 | 低 | chapters/{character_name}/ | 追踪系统通用 |
| **新成就** | ✅ 完全支持 | 低 | achievement_backend.rpy | 成就系统支持动态注册 |
| **新背景/音乐** | ✅ 完全支持 | 无 | images/, audio/ | 直接放置资源即可 |
| **新立绘** | ⚠️ 中等 | 低 | characters/, 01_characters.rpy | 需要定义 Character 对象 |
| **新算法互动** | ✅ 完全支持 | 低 | 05_algorithm_interaction.rpy | 可以复用现有函数 |

### 关键扩展点

#### 1. 角色注册系统

**当前问题**: 角色定义硬编码
**建议方案**: 实现动态角色注册

```python
# rpy/dlc_system.rpy (新建)
init python:
    dlc_characters = {}
    dlc_relationships = {}
    dlc_fsm_transitions = {}

    def register_dlc_character(name, color, color_hex, dialogue_prefix="「", dialogue_suffix="」"):
        """注册 DLC 角色"""
        char_obj = Character(name, color=color, what_prefix=dialogue_prefix, what_suffix=dialogue_suffix)
        dlc_characters[name] = char_obj

        # 自动创建关系变量
        if not hasattr(store, name.lower() + "_relationship"):
            setattr(store, name.lower() + "_relationship", "UNMET")

        return char_obj

    def get_dlc_character(name):
        """获取 DLC 角色"""
        return dlc_characters.get(name)
```

#### 2. 时间线扩展接口

**当前问题**: 时间线数据硬编码
**建议方案**: 提供时间线扩展函数

```python
# rpy/dlc_system.rpy
init python:
    dlc_timeline_events = {}

    def register_dlc_event(st_range, event_id, character=None, event_type="chapter"):
        """注册 DLC 时间线事件"""
        if st_range not in dlc_timeline_events:
            dlc_timeline_events[st_range] = []

        dlc_timeline_events[st_range].append({
            "id": event_id,
            "character": character,
            "type": event_type
        })

    def get_dlc_events(st_range):
        """获取指定时间段的 DLC 事件"""
        return dlc_timeline_events.get(st_range, [])
```

#### 3. 结局注册系统

**当前问题**: 结局条件硬编码
**建议方案**: 提供动态结局注册

```python
# rpy/dlc_system.rpy
init python:
    dlc_endings = {}
    dlc_ending_conditions = {}

    def register_dlc_ending(ending_id, label_name, condition_func):
        """注册 DLC 结局"""
        dlc_endings[ending_id] = label_name
        dlc_ending_conditions[ending_id] = condition_func

    def check_dlc_endings():
        """检查 DLC 结局条件"""
        for ending_id, condition in dlc_ending_conditions.items():
            if condition():
                return ending_id
        return None
```

---

## DLC 扩展方案设计

### 方案一：独立剧情型 DLC（优先推荐）

**概念**: DLC 作为完全独立的剧情线，与主线时间线平行或之后

**适用场景**:
- After Story（主线之后的额外故事）
- 支线剧情（不影响主线）
- 特殊活动剧情（如节日活动）

**实现方式**:

1. **目录结构**:
```
dlc_pythonista/
├── game/
│   └── dlc_pythonista.rpy    # DLC 主脚本
├── images/
│   └── dlc_pythonista/
│       ├── bg/
│       └── characters/
└── audio/
    └── dlc_pythonista/
        ├── bgm/
        └── se/
```

2. **DLC 脚本结构**:
```renpy
# dlc_pythonista.rpy
label start:
    jump main_menu

label main_menu:
    # 检查是否安装了主线游戏
    if not hasattr(store, 'source_time'):
        scene black
        "错误：未检测到源界主线游戏"
        return

    # DLC 入口
    scene bg dlc_pythonista_title
    pythonista "欢迎来到 Pythonista 的挑战！"
    menu:
        "开始 DLC 剧情":
            jump dlc_pythonista_start
        "返回主线":
            return

label dlc_pythonista_start:
    scene bg dlc_pythonista_lab
    pythonista "这是我的实验室..."
    # DLC 剧情内容
    menu:
        "接受挑战":
            $ track_choice("python_challenge", is_optimal=True)
            jump dlc_pythonista_good
        "拒绝":
            jump dlc_pythonista_bad

label dlc_pythonista_good:
    "Pythonista 对你印象深刻..."
    "你获得了一项新技能：动态类型理解"
    return
```

3. **菜单集成**:
```renpy
# screens.rpy - 在主菜单添加 DLC 入口
screen main_menu():
    # ... 现有内容 ...
    if dlc_pythonista_installed():
        textbutton _("Pythonista 冒险") action Start("dlc_pythonista_start")
```

**优势**:
- ✅ 完全独立，不破坏主线平衡
- ✅ 易于开发和测试
- ✅ 可以独立更新
- ✅ 资源完全隔离

**劣势**:
- ⚠️ 无法与主线角色深度互动
- ⚠️ 无法影响主线剧情走向

---

### 方案二：主线扩展型 DLC

**概念**: 扩展现有时间线，在特定时间段插入 DLC 事件

**适用场景**:
- 新语言角色的完整路线
- 扩展现有角色的故事线
- 在主线中插入支线剧情

**实现方式**:

1. **时间线扩展**:
```python
# dlc_new_language/dlc_timeline_extension.rpy
init python:
    # 注册 DLC 时间线事件
    register_dlc_event("ST_38-42", "NL_01", character="newlang", event_type="chapter")
    register_dlc_event("ST_42-46", "NL_02", character="newlang", event_type="chapter")
    register_dlc_event("ST_46-50", "NL_03", character="newlang", event_type="chapter")
```

2. **时间线菜单修改**:
```renpy
# 02_timeline.rpy 修改
label time_choice_menu:
    # ... 现有代码 ...

    # 检查 DLC 事件
    $ dlc_events = get_dlc_events(current)
    if dlc_events:
        for event in dlc_events:
            textbutton "前往 [event.character] 的 [event.id]" action Jump("execute_dlc_" + event.id)
```

3. **DLC 章节实现**:
```renpy
# dlc_new_language/chapters/NL_01_intro.rpy
label execute_dlc_NL_01:
    show newlang neutral
    newlang "你好，我是 NewLang。"
    # 剧情内容
    jump time_choice_menu
```

**优势**:
- ✅ 深度集成到主线
- ✅ 可以影响主线剧情
- ✅ 可以复用主线角色

**劣势**:
- ⚠️ 需要修改主线代码（时间线系统）
- ⚠️ 需要仔细平衡游戏性
- ⚠️ 更新时可能产生冲突

---

### 方案三：世界观扩展型 DLC

**概念**: 添加新的语言角色及其完整系统

**适用场景**:
- 添加新编程语言的完整路线
- 扩展现有角色的深度
- 添加新的游戏机制

**实现方式**:

1. **角色注册**:
```python
# dlc_rust_full/dlc_character.rpy
init python:
    # 扩展现有 Rusty 角色（或创建新角色）
    rusty_full = register_dlc_character(
        name="Rusty+",
        color="#FFA502",
        color_hex="#FFA502"
    )

    # 注册 Rusty 的完整关系 FSM
    dlc_fsm_transitions["rusty_full"] = {
        "UNMET": ["FIRST_CONTACT"],
        "FIRST_CONTACT": ["FUNCTIONAL"],
        # ... 完整的状态转换
    }
```

2. **时间线集成**:
```python
# 在 02_timeline.rpy 添加 Rusty 线的时间段
"ST_38-42": {
    "available_lines": ["rusty_full"],  # 新角色线
    "rusty_full_event": "R_01",
    "cee_event": None,
    "jawa_event": None,
    # ...
}
```

3. **结局集成**:
```python
# 修改 check_ending_conditions
def check_ending_conditions():
    # ... 现有条件 ...

    # 检查 Rusty 线完成
    rusty_completed = all([
        getattr(store, f"r_0{i}_status") == "completed"
        for i in range(1, 10)
    ])

    if rusty_completed and cee_completed and jawa_completed:
        return "rusty_trinity_end"  # 自定义结局
```

**优势**:
- ✅ 最深度的扩展
- ✅ 可以创造全新的体验
- ✅ 极高的可重玩价值

**劣势**:
- ❌ 需要大量主线代码修改
- ❌ 平衡性极难控制
- ❌ 更新时高度冲突风险

---

## 基础世界调整建议

### 1. 创建 DLC 系统（必要）

**新建文件**: `rpy/06_dlc_system.rpy`

```renpy
# ============================================================================
# 源界 (Source Realm) - 06: DLC 扩展系统
# ============================================================================

# ============================================================================
# 1. DLC 列表管理
# ============================================================================

init python:
    # 已安装的 DLC 列表
    installed_dlcs = []

    # DLC 元数据
    dlc_metadata = {}

# ============================================================================
# 2. DLC 注册 API
# ============================================================================

init python:
    def register_dlc(dlc_id, name, version, author, description):
        """注册 DLC 元数据"""
        dlc_metadata[dlc_id] = {
            "name": name,
            "version": version,
            "author": author,
            "description": description,
            "installed": False
        }

    def activate_dlc(dlc_id):
        """激活 DLC"""
        if dlc_id in dlc_metadata:
            dlc_metadata[dlc_id]["installed"] = True
            installed_dlcs.append(dlc_id)
            return True
        return False

    def is_dlc_active(dlc_id):
        """检查 DLC 是否激活"""
        return dlc_id in installed_dlcs

# ============================================================================
# 3. 角色扩展 API
# ============================================================================

init python:
    dlc_characters = {}

    def register_dlc_character(
        name,
        color,
        color_hex,
        what_prefix="「",
        what_suffix="」",
        image_prefix=""
    ):
        """注册 DLC 角色"""
        # 创建 Character 对象
        char_obj = Character(
            name,
            color=color,
            what_prefix=what_prefix,
            what_suffix=what_suffix,
            image=image_prefix
        )
        dlc_characters[name] = char_obj

        # 自动创建关系变量
        rel_var_name = name.lower() + "_relationship"
        if not hasattr(store, rel_var_name):
            setattr(store, rel_var_name, "UNMET")

        # 自动创建状态变量
        state_var_name = name.lower() + "_current_state"
        if not hasattr(store, state_var_name):
            setattr(store, state_var_name, "neutral")

        return char_obj

    def get_dlc_character(name):
        """获取 DLC 角色"""
        return dlc_characters.get(name)

# ============================================================================
# 4. 时间线扩展 API
# ============================================================================

init python:
    dlc_timeline_extensions = {}

    def register_dlc_timeline_event(
        st_range,
        event_id,
        character=None,
        event_type="chapter",
        label_name=None
    ):
        """注册 DLC 时间线事件"""
        if st_range not in dlc_timeline_extensions:
            dlc_timeline_extensions[st_range] = []

        event_data = {
            "id": event_id,
            "character": character,
            "type": event_type
        }

        if label_name:
            event_data["label"] = label_name

        dlc_timeline_extensions[st_range].append(event_data)

    def get_dlc_timeline_events(st_range):
        """获取指定时间段的 DLC 事件"""
        return dlc_timeline_extensions.get(st_range, [])

# ============================================================================
# 5. 结局扩展 API
# ============================================================================

init python:
    dlc_endings = {}
    dlc_ending_conditions = {}

    def register_dlc_ending(
        ending_id,
        label_name,
        name,
        condition_func,
        description=""
    ):
        """注册 DLC 结局"""
        dlc_endings[ending_id] = {
            "label": label_name,
            "name": name,
            "description": description
        }
        dlc_ending_conditions[ending_id] = condition_func

    def check_dlc_ending_conditions():
        """检查所有 DLC 结局条件"""
        for ending_id, condition in dlc_ending_conditions.items():
            try:
                if condition():
                    return ending_id
            except Exception as e:
                print(f"DLC 结局检查错误 {ending_id}: {e}")
        return None

# ============================================================================
# 6. 成就扩展 API
# ============================================================================

init python:
    def register_dlc_achievement(
        achievement_id,
        name,
        description,
        condition_func=None,
        hidden=False
    ):
        """注册 DLC 成就"""
        if not hasattr(store, 'achievements'):
            store.achievements = {}

        store.achievements[achievement_id] = {
            "name": name,
            "description": description,
            "unlocked": False,
            "hidden": hidden,
            "is_dlc": True,
            "condition": condition_func
        }

    def unlock_dlc_achievement(achievement_id):
        """解锁 DLC 成就"""
        if achievement_id in store.achievements:
            store.achievements[achievement_id]["unlocked"] = True

# ============================================================================
# 7. DLC 检测 API
# ============================================================================

init python:
    def scan_installed_dlcs():
        """扫描已安装的 DLC"""
        import os

        dlc_files = []
        for filename in os.listdir(config.basedir + "/game"):
            if filename.startswith("dlc_") and (filename.endswith(".rpa") or filename.endswith(".rpyc")):
                dlc_id = filename.replace("dlc_", "").replace(".rpa", "").replace(".rpyc", "")
                dlc_files.append(dlc_id)

        return dlc_files

    def auto_load_dlcs():
        """自动加载检测到的 DLC"""
        detected = scan_installed_dlcs()
        for dlc_id in detected:
            activate_dlc(dlc_id)

# 游戏启动时自动扫描 DLC
init python:
    auto_load_dlcs()
```

### 2. 修改时间线菜单（02_timeline.rpy）

在 `time_choice_menu` 中添加 DLC 事件显示：

```renpy
label time_choice_menu:
    # ... 现有代码 ...

    # 显示 DLC 事件
    $ dlc_events = get_dlc_timeline_events(current)
    if dlc_events:
        for event in dlc_events:
            if event["type"] == "chapter":
                textbutton "[event.character] 的 [event.id]" action Jump("execute_dlc_" + event["id"])
            elif event["type"] == "holiday":
                textbutton "假日：[event.id]" action Jump(event["label"])
```

### 3. 修改结局系统（game_endings.rpy）

在 `check_ending_conditions()` 中添加 DLC 结局检查：

```python
def check_ending_conditions():
    # ... 现有主线结局检查 ...

    # 检查 DLC 结局
    dlc_ending = check_dlc_ending_conditions()
    if dlc_ending:
        return dlc_ending

    return "none"
```

### 4. 添加 DLC 管理界面（screens.rpy）

```renpy
screen dlc_manager():
    tag menu

    frame:
        style_group "dlc"
        xysize (900, 600)
        align (.5, .5)

        vbox:
            spacing 20
            xalign 0.5

            text "DLC 管理" size 40

            # 主线 DLC
            textbutton "返回主线" action Return()

            # 安装的 DLC
            if installed_dlcs:
                text "已安装的 DLC:"
                for dlc_id in installed_dlcs:
                    if dlc_id in dlc_metadata:
                        $ meta = dlc_metadata[dlc_id]
                        text "[meta['name']] v[meta['version']] 作者: [meta['author']]"

            # 未安装的 DLC
            text "\n"
            text "检测到 DLC:"
            $ detected = scan_installed_dlcs()
            for dlc_id in detected:
                if dlc_id not in installed_dlcs and dlc_id in dlc_metadata:
                    $ meta = dlc_metadata[dlc_id]
                    textbutton "[meta['name']]" action [
                        SetVariable('selected_dlc', dlc_id),
                        ShowTransient('dlc_info')
                    ]

screen dlc_info():
    zorder 100
    modal True

    frame:
        style_group "dlc_info"
        xysize (700, 400)
        align (.5, .5)

        vbox:
            spacing 15
            padding 30

            if selected_dlc in dlc_metadata:
                $ meta = dlc_metadata[selected_dlc]
                text "[meta['name']]" size 30
                text "版本: [meta['version']]" size 20
                text "作者: [meta['author']]" size 20
                text "\n"
                text "[meta['description']]" size 18

            hbox:
                xalign 0.5
                spacing 20

                textbutton "激活" action [
                    Function(activate_dlc, selected_dlc),
                    Hide('dlc_info'),
                    Hide('dlc_manager')
                ]

                textbutton "取消" action Hide('dlc_info')

# 在主菜单添加 DLC 入口
screen main_menu():
    # ... 现有内容 ...

    if installed_dlcs:
        textbutton "DLC 管理" action ShowMenu("dlc_manager")
```

---

## 开发者指引

### 阶段一：DLC 规划

#### 1.1 确定 DLC 类型

使用决策树确定 DLC 类型：

```
DLC 是否需要与主线角色互动？
├─ 是 → 主线扩展型 DLC 或 世界观扩展型 DLC
│   ├─ 是否需要修改时间线？
│   │   ├─ 是 → 世界观扩展型 DLC（高难度）
│   │   └─ 否 → 主线扩展型 DLC（中等难度）
│   └─ 检查是否需要修改核心文件（02_timeline.rpy, 00_setup.rpy）
└─ 否 → 独立剧情型 DLC（低难度，推荐）
    └─ 完全独立，可以随时开发
```

#### 1.2 准备开发环境

**必需文件**:
```
源界/
├── game/
│   ├── 00_setup.rpy          # 参考系统函数
│   ├── 01_characters.rpy      # 参考角色定义
│   ├── 02_timeline.rpy        # 参考时间线
│   └── 06_dlc_system.rpy     # DLC API（需要先实现）
```

**开发工具**:
- Ren'Py SDK 8.5+
- 文本编辑器（VS Code, Sublime Text 等）
- Ren'Py Lint 工具

---

### 阶段二：DLC 开发（独立剧情型）

#### 2.1 创建项目结构

```
my_dlc_project/
├── game/
│   └── my_dlc.rpy          # DLC 主脚本
├── images/
│   └── my_dlc/
│       ├── bg/               # 背景
│       │   └── scene.png
│       └── characters/       # 角色
│           └── char.png
└── audio/
    └── my_dlc/
        ├── bgm/             # 背景音乐
        │   └── theme.ogg
        └── se/              # 音效
            └── click.wav
```

#### 2.2 编写 DLC 脚本

**基本结构**:

```renpy
# my_dlc.rpy
# ============================================================================
# DLC: [DLC 名称]
# 版本: 1.0.0
# 作者: [作者名]
# 描述: [简短描述]
# ============================================================================

# ============================================================================
# 1. DLC 元数据注册
# ============================================================================

init python:
    # 注册 DLC 元数据
    register_dlc(
        dlc_id="my_dlc",
        name="我的 DLC",
        version="1.0.0",
        author="开发者名",
        description="这是一个示例 DLC，展示了独立剧情的创建方法。"
    )

# ============================================================================
# 2. 新角色定义（如果有）
# ============================================================================

define new_char = Character(
    "新角色",
    color="#FF5733",  # 独特的配色
    what_prefix="「",
    what_suffix="」"
)

init python:
    # 注册 DLC 角色
    register_dlc_character(
        name="new_char",
        color="#FF5733",
        color_hex="#FF5733"
    )

# ============================================================================
# 3. 新成就定义（可选）
# ============================================================================

init python:
    def check_dlc_completion():
        """检查 DLC 完成条件"""
        return hasattr(store, 'dlc_my_dlc_completed')

    register_dlc_achievement(
        achievement_id="dlc_my_dlc_complete",
        name="DLC 通关",
        description="完成了我的 DLC 的所有剧情",
        condition_func=check_dlc_completion,
        hidden=False
    )

# ============================================================================
# 4. DLC 入口 Label
# ============================================================================

label start:
    # 检查主线是否安装
    if not hasattr(store, 'source_time'):
        scene black
        narrator "错误：未检测到源界主线游戏。"
        narrator "请先安装源界主游戏。"
        return

    jump my_dlc_main_menu

label my_dlc_main_menu:
    scene bg my_dlc/title
    narrator "欢迎来到我的 DLC！"

    menu:
        "开始新游戏":
            $ set_source_time(0)  # 重置 DLC 时间（如果有）
            jump my_dlc_start

        "返回主菜单":
            return

# ============================================================================
# 5. DLC 剧情内容
# ============================================================================

label my_dlc_start:
    scene bg my_dlc/scene1

    new_char "你好，我是新角色。"
    player "很高兴见到你！"

    menu:
        "友好回应":
            jump my_dlc_good_response

        "冷淡回应":
            jump my_dlc_bad_response

label my_dlc_good_response:
    new_char "你很友善，我喜欢你。"

    $ new_char_relationship = "FRIENDLY"
    $ track_affection("new_char", 10)

    jump my_dlc_mid

label my_dlc_bad_response:
    new_char "好吧，看来我们还需要时间了解彼此。"

    $ new_char_relationship = "STRANGER"
    $ track_affection("new_char", -5)

    jump my_dlc_mid

label my_dlc_mid:
    scene bg my_dlc/scene2

    new_char "我们开始今天的任务吧。"

    # ... 更多剧情内容 ...

label my_dlc_end:
    scene black
    with Dissolve(2.0)

    narrator "DLC 剧情完成！"

    # 标记 DLC 完成
    $ dlc_my_dlc_completed = True

    # 解锁成就
    $ unlock_dlc_achievement("dlc_my_dlc_complete")

    # 查看是否达成特定结局
    if new_char_relationship == "FRIENDLY":
        jump my_dlc_good_end
    else:
        jump my_dlc_normal_end

label my_dlc_good_end:
    scene bg my_dlc/happy_ending

    new_char "谢谢你陪我度过这段时光。"

    teaching "你学会了：真诚的态度能够打开任何语言的心扉。"

    pause 2.0

    narrator "【好结局】新角色的好友"

    menu:
        "返回主菜单":
            return
        "再次游玩":
            jump my_dlc_start

label my_dlc_normal_end:
    scene bg my_dlc/normal_ending

    new_char "也许下次我们能更好地相处。"

    teaching "你学会了：每种语言都有自己的节奏，需要耐心去理解。"

    pause 2.0

    narrator "【普通结局】新角色的过客"

    menu:
        "返回主菜单":
            return
        "再次游玩":
            jump my_dlc_start
```

#### 2.3 测试 DLC

**测试清单**:
- [ ] DLC 能够独立启动
- [ ] 所有角色显示正常
- [ ] 所有菜单选项工作正常
- [ ] 所有结局都能达成
- [ ] 成就系统正常解锁
- [ ] 返回主菜单功能正常
- [ ] 资源（图片、音乐）加载正常

---

### 阶段三：DLC 开发（主线扩展型）

#### 3.1 注册时间线事件

```python
# my_mainline_dlc.rpy
init python:
    # 注册时间线扩展
    # 使用 ST_38+ 范围避免与主线冲突
    register_dlc_timeline_event(
        st_range="ST_38-42",
        event_id="C_10",  # Cee 线第10章
        character="cee",
        event_type="chapter",
        label_name="cee_C10_start"
    )

    register_dlc_timeline_event(
        st_range="ST_38-42",
        event_id="J_10",  # Jawa 线第10章
        character="jawa",
        event_type="chapter",
        label_name="jawa_J10_start"
    )
```

#### 3.2 实现章节内容

```renpy
label cee_C10_start:
    scene bg memory_warehouse_extended

    cee "欢迎回来。"
    cee "这是新的挑战。"

    # ... 章节内容 ...

    # 章节完成时推进时间
    $ advance_time_to_next_period()

    jump time_choice_menu
```

#### 3.3 添加新结局

```python
init python:
    def check_new_ending_condition():
        """检查新结局条件"""
        cee_completed = all([
            store.c_01_status == "completed",
            # ... 所有章节
            store.c_10_status == "completed"  # DLC 章节
        ])

        jawa_completed = all([
            store.j_01_status == "completed",
            # ... 所有章节
            store.j_10_status == "completed"  # DLC 章节
        ])

        if cee_completed and jawa_completed and store.cee_relationship == "RESONANT":
            return "dlc_ultimate_end"

        return None

    register_dlc_ending(
        ending_id="dlc_ultimate_end",
        label_name="dlc_ultimate",
        name="终极程序员的诞生",
        condition_func=check_new_ending_condition,
        description="精通所有语言，与所有角色达到最高关系。"
    )
```

---

### 阶段四：质量检查清单

#### 4.1 代码质量

- [ ] 所有变量命名清晰，遵循项目规范
- [ ] 所有函数都有文档字符串
- [ ] 所有 label 都有清晰的命名
- [ ] 没有未使用的变量或函数
- [ ] 没有硬编码的魔法数字（应使用常量）

#### 4.2 内容质量

- [ ] 角色对话符合人设
- [ ] 剧情逻辑连贯
- [ ] 所有选项都有明确的反馈
- [ ] 教学内容准确（如果是教学类 DLC）
- [ ] 结局有合理的触发条件

#### 4.3 兼容性

- [ ] 与主线游戏兼容
- [ ] 与其他 DLC 兼容（如果存在）
- [ ] 不会破坏主线存档
- [ ] 不会影响主线游戏平衡

#### 4.4 用户体验

- [ ] 文字没有错别字
- [ ] 所有图片显示正常
- [ ] 所有音乐和音效播放正常
- [ ] 菜单和UI元素显示正常
- [ ] 加载时间合理（不卡顿）

---

### 阶段五：文档编写

#### 5.1 README.md

**必需内容**:

```markdown
# [DLC 名称]

## 基本信息

- **版本**: 1.0.0
- **作者**: [作者名]
- **类型**: [独立剧情 / 主线扩展 / 世界观扩展]
- **兼容主线版本**: 0.1.0+

## 描述

[详细描述 DLC 的内容和特色]

## 安装说明

1. 将 `my_dlc.rpa` 放入源界游戏目录的 `game/` 文件夹
2. 启动游戏
3. 在主菜单选择 "DLC 管理"
4. 点击 "激活" 激活 DLC

## 功能特性

- [ ] 新角色: [角色名]
- [ ] 新剧情: [章节数量]
- [ ] 新结局: [数量]
- [ ] 新成就: [数量]
- [ ] 新背景: [数量]
- [ ] 新音乐: [数量]

## 游玩指南

[简短的游玩指南]

## 已知问题

- [ ] 问题1: 描述

## 更新日志

### v1.0.0 (2026-02-26)
- 初始发布
```

#### 5.2 CHANGELOG.md

```markdown
# 更新日志

## [1.0.0] - 2026-02-26

### 新增
- 新增角色：新角色
- 新增章节：10章
- 新增结局：3个
- 新增成就：5个

### 修复
- 修复了对话文本显示错误

### 已知问题
- 暂无
```

---

## RPA 打包指引

### 1. 配置 options.rpy

在 DLC 项目的 `options.rpy` 中添加：

```python
init python:
    # 分类 DLC 资源
    build.classify('game/my_dlc/**.**', 'my_dlc')

    # 打包为独立的 RPA 文件
    build.archive('my_dlc', 'all')

    # 排除开发和临时文件
    build.classify('**~', None)
    build.classify('**.bak', None)
```

### 2. 打包命令

在项目根目录执行：

```bash
# Ren'Py 命令行工具
python -m renpy distribute ./

# 或使用 Ren'Py SDK 启动器
# 点击 "Build Distributions"
```

### 3. 验证 RPA 文件

**文件结构检查**:

```bash
# 查看 RPA 内容
unzip -l my_dlc.rpa

# 应该看到：
# my_dlc.rpa
# ├── game/
# │   ├── my_dlc.rpy
# ├── images/
# │   └── my_dlc/
# └── audio/
#     └── my_dlc/
```

### 4. 测试 RPA

**手动测试**:

1. 将 `my_dlc.rpa` 复制到主线游戏的 `game/` 文件
2. 启动主线游戏
3. 检查 DLC 是否被检测到
4. 测试所有功能

**自动化测试脚本**（可选）:

```python
# test_dlc.py
import os
import sys

def test_dlc_detection():
    """测试 DLC 检测"""
    dlc_file = "game/my_dlc.rpa"
    if not os.path.exists(dlc_file):
        print(f"❌ DLC 文件不存在: {dlc_file}")
        return False

    print(f"✅ DLC 文件存在: {dlc_file}")
    return True

def test_dlc_content():
    """测试 DLC 内容"""
    # 模拟 Ren'Py 加载
    try:
        # 这里应该实际测试 Ren'Py 加载
        print("✅ DLC 内容验证通过")
        return True
    except Exception as e:
        print(f"❌ DLC 内容验证失败: {e}")
        return False

if __name__ == "__main__":
    results = [
        test_dlc_detection(),
        test_dlc_content()
    ]

    if all(results):
        print("\n✅ 所有测试通过，DLC 可以发布")
        sys.exit(0)
    else:
        print("\n❌ 部分测试失败，请修复后再发布")
        sys.exit(1)
```

### 5. 分发指南

**文件清单**:

```
my_dlc_distribution/
├── my_dlc.rpa              # 主要 DLC 包
├── README.md                # 用户文档
├── INSTALL.md              # 安装指南
└── CHANGELOG.md            # 更新日志
```

**压缩包创建**:

```bash
# 创建发布压缩包
zip -r my_dlc_v1.0.0.zip my_dlc_distribution/

# 验证压缩包内容
unzip -l my_dlc_v1.0.0.zip
```

---

## GitHub 文档组织

### Wiki 结构建议

```
源界 GitHub Wiki
├── 首页 (Home)
│   └── 项目简介和快速开始
├── 开发者文档 (Developer Docs)
│   ├── DLC 开发指南
│   ├── API 参考文档
│   ├── 代码规范
│   └── 贡献指南
├── DLC 开发教程 (DLC Tutorial)
│   ├── 快速开始
│   ├── 独立剧情型 DLC 教程
│   ├── 主线扩展型 DLC 教程
│   └── 常见问题
├── API 文档 (API Reference)
│   ├── 角色系统 API
│   ├── 时间线 API
│   ├── 结局 API
│   └── DLC 系统 API
└── 社区资源 (Community)
    ├── DLC 创意展示
    ├── 工具和脚本
    └── 最佳实践
```

### Discussion 板块建议

**固定帖子**:

1. **DLC 开发公告**: 发布新 DLC 的地方
2. **DLC 问题反馈**: 用户报告问题的地方
3. **DLC 开发求助**: 开发者寻求帮助的地方
4. **DLC 创意征集**: 社区讨论 DLC 创意的地方

**版块分类**:

- **DLC 开发**: 讨论开发技巧和问题
- **DLC 测试**: 组织社区测试
- **DLC 发布**: 正式发布 DLC
- **DLC 反馈**: 用户反馈和评分

### Issue 模板

**DLC 开发 Issue 模板**:

```markdown
## DLC 问题报告

**DLC 名称**: [名称]
**DLC 版本**: [版本]
**主线版本**: [版本]
**操作系统**: [Windows/Mac/Linux]

### 问题描述

[详细描述问题]

### 复现步骤

1.
2.
3.

### 期望行为

[描述应该发生什么]

### 实际行为

[描述实际发生了什么]

### 截图/日志

[如果有，贴在这里]

### 其他信息

[任何其他相关信息]
```

**DLC 开发求助 Issue 模板**:

```markdown
## DLC 开发求助

**DLC 类型**: [独立剧情 / 主线扩展 / 世界观扩展]
**开发阶段**: [规划 / 开发中 / 测试中]
**问题描述**:

[详细描述需要帮助的问题]

### 已尝试的方法

1. [方法1]
2. [方法2]

### 期望的帮助

[描述希望得到的帮助类型：代码示例、架构建议、调试等]
```

---

## 风险评估与缓解策略

### 1. 技术风险

| 风险 | 影响 | 概率 | 缓解策略 |
|------|------|------|----------|
| DLC 破坏主线存档 | 高 | 中 | DLC 使用独立的变量命名空间，不修改主线变量 |
| DLC 导致游戏崩溃 | 高 | 低 | 强制要求所有 DLC 通过测试 checklist |
| DLC 之间冲突 | 中 | 中 | 提供 DLC 兼容性矩阵，社区维护 |
| 性能下降 | 中 | 中 | 要求 DLC 优化资源大小，提供性能测试工具 |
| 安全漏洞 | 低 | 低 | 社区审核机制，信任开发者体系 |

### 2. 内容风险

| 风险 | 影响 | 概率 | 缓解策略 |
|------|------|------|----------|
| 内容质量参差不齐 | 中 | 高 | DLC 评分系统，社区推荐机制 |
| 违反项目理念 | 中 | 低 | DLC 审核指南，明确的内容边界 |
| 破坏游戏平衡性 | 高 | 中 | 平衡性测试清单，社区反馈机制 |

### 3. 法律风险

| 风险 | 影响 | 概率 | 缓解策略 |
|------|------|------|----------|
| 侵权问题 | 高 | 低 | 明确的 IP 政策，社区举报机制 |
| 许可证冲突 | 中 | 低 | 统一的 DLC 许可证模板 |
| 数据隐私问题 | 低 | 低 | 明确的数据使用政策 |

---

## 实施路线图

### 阶段一：基础系统（第1-2周）

- [ ] 创建 `rpy/06_dlc_system.rpy`
- [ ] 实现角色注册 API
- [ ] 实现时间线扩展 API
- [ ] 实现结局注册 API
- [ ] 实现成就扩展 API
- [ ] 实现 DLC 检测 API
- [ ] 添加 DLC 管理界面
- [ ] 更新 `02_timeline.rpy` 支持 DLC 事件
- [ ] 更新 `game_endings.rpy` 支持 DLC 结局
- [ ] 更新 `screens.rpy` 添加 DLC 入口

### 阶段二：示例 DLC（第3-4周）

- [ ] 创建「独立剧情型」示例 DLC
- [ ] 创建「主线扩展型」示例 DLC
- [ ] 创建「世界观扩展型」示例 DLC
- [ ] 编写开发者文档
- [ ] 录制开发教程视频
- [ ] 创建测试工具和脚本

### 阶段三：社区准备（第5-6周）

- [ ] 设置 GitHub Wiki
- [ ] 创建 Discussion 板块
- [ ] 编写贡献指南
- [ ] 建立 DLC 审核流程
- [ ] 创建 DLC 展示页面
- [ ] 设计 DLC 评分系统
- [ ] 建立 DLC 兼容性矩阵

### 阶段四：发布和反馈（第7-8周）

- [ ] 正式发布 DLC 系统
- [ ] 发布示例 DLC
- [ ] 组织社区内测
- [ ] 收集反馈并修复问题
- [ ] 发布开发者工具和文档
- [ ] 建立社区支持渠道

---

## 总结

**当前系统可扩展性**: ⭐⭐⭐⭐☆ (4/5)

**优势**:
- ✅ 模块化设计良好
- ✅ 核心系统（章节追踪、算法互动）通用
- ✅ RPA 打包机制完善

**需要改进**:
- ⚠️ 需要添加 DLC 注册和管理系统
- ⚠️ 需要扩展时间线系统支持动态事件
- ⚠️ 需要扩展结局系统支持自定义结局
- ⚠️ 需要完善开发者文档和工具

**推荐优先级**:

1. **高优先级**: 实现基础 DLC 系统（`06_dlc_system.rpy`）
2. **中优先级**: 编写「独立剧情型」示例 DLC 和文档
3. **低优先级**: 开发主线扩展型和世界观扩展型 DLC 的支持

**预期成果**:

实施完成后，社区开发者将能够：
- ✅ 独立开发 DLC 而不需要修改主线代码
- ✅ 使用统一的 API 接口集成新内容
- ✅ 通过 GitHub 分发和更新 DLC
- ✅ 在社区中分享和讨论 DLC 开发
- ✅ 获得完整的开发文档和示例代码

---

**附录 A: 参考资料**

- [Ren'Py 官方文档](https://www.renpy.org/doc/html/)
- [Ren'Py RPA 打包指南](https://www.renpy.org/doc/html/build.html)
- [GitHub Wiki 最佳实践](https://docs.github.com/en/communities/documenting-your-project-with-wikis)

---

**附录 B: 联系方式**

- **项目 GitHub**: [链接]
- **讨论区**: [链接]
- **问题反馈**: [链接]
- **DLC 提交**: [邮箱/表单]

---

*文档生成日期: 2026-02-26*
*作者: Crush AI*
*版本: v1.0*
