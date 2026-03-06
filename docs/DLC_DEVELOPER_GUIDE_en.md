# Source Realm - DLC Developer Guide

> This document provides a complete extension guide for community DLC developers, ensuring DLCs can seamlessly integrate into the main game.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Timeline System and Dynamic Endings](#2-timeline-system-and-dynamic-endings)
3. [Character Extension](#3-character-extension)
4. [Event and Chapter Creation](#4-event-and-chapter-creation)
5. [Custom Endings](#5-custom-endings)
6. [Consequence System Integration](#6-consequence-system-integration)
7. [File Structure Specifications](#7-file-structure-specifications)
8. [API Reference](#8-api-reference)
9. [Best Practices](#9-best-practices)
10. [Example Templates](#10-example-templates)

---

## 1. Architecture Overview

### 1.1 Core System Files

| File | Purpose | DLC Modifiable |
|------|--------|-----------|
| `rpy/00_setup.rpy` | Global variables, system functions | ⚠️ Add only, don't modify |
| `rpy/01_characters.rpy` | Character definitions | ✅ Add new characters |
| `rpy/02_timeline.rpy` | Timeline system | ✅ Extend time periods |
| `rpy/03_fsm.rpy` | Relationship state helpers | ✅ Use helper functions |
| `rpy/04_consequence.rpy` | Consequence system | ✅ Call existing functions |

### 1.2 Chapter Directory Structure

```
rpy/chapters/
├── prologue.rpy          # Prologue
├── cee/                  # Cee line (C language)
│   ├── C_01_pointers.rpy
│   ├── C_02_memory.rpy
│   └── ...
├── jawa/                 # Jawa line (Java)
│   ├── J_01_types.rpy
│   └── ...
├── shared/               # Shared events
│   ├── explore_events.rpy
│   ├── holidays.rpy
│   └── shared_events.rpy
└── endings/              # Endings
    └── game_endings.rpy
```

### 1.3 DLC Directory Recommendation

```
rpy/dlc/
├── your_dlc_name/
│   ├── characters.rpy    # New character definitions
│   ├── events/           # Event files
│   ├── timeline.rpy      # Timeline extensions
│   ├── endings.rpy       # DLC-specific endings
│   └── config.rpy        # DLC configuration
```

---

## 2. Timeline System and Dynamic Endings

### 2.1 Source Time (ST) Concept

Source Time is the main progress indicator of the game:
- ST 0-36: Main storyline
- ST 36-38: Ending evaluation
- ST 38+: Bad End A check

### 2.2 Dynamic Ending Calculation (Key Improvement)

**Problem**: Original design forces ending evaluation at ST 36, limiting DLC extensions.

**Solution**: DLC can disable forced triggering of main game endings:

```python
# In your DLC config.rpy
init python:
    # Disable forced triggering of main game endings
    dlc_disable_main_ending_force = True

    # Set DLC custom ending time
    dlc_custom_ending_time = 50  # DLC endings trigger at ST 50

    # Add DLC ending conditions
    def dlc_check_ending():
        if store.source_time >= dlc_custom_ending_time:
            if store.dlc_relationship == "MAX":
                return "dlc_true_end"
            elif store.dlc_relationship in ["HIGH", "MAX"]:
                return "dlc_good_end"
        return None
```

### 2.3 Extending Timeline

Add in `dlc/your_dlc_name/timeline.rpy`:

```python
init python:
    # Extend main timeline data
    dlc_timeline_extensions = {
        "ST_38-42": {
            "available_lines": ["dlc_character"],
            "dlc_event": "DLC_01",
            "is_holiday": False
        },
        "ST_42-46": {
            "available_lines": ["dlc_character", "cee"],
            "dlc_event": "DLC_02",
            "cee_event": None,  # Can run in parallel with main line
            "is_holiday": False
        },
        # ... more time periods
    }

    # Register to main timeline
    for period, data in dlc_timeline_extensions.items():
        timeline_data[period] = data
```

### 2.4 Completely Independent Timeline

If your DLC is completely independent and doesn't need to interact with the main line:

```python
# At DLC entry point
label dlc_start:
    # Save main line state
    $ main_source_time = store.source_time
    $ main_current_line = store.current_line

    # Set DLC independent state
    $ store.source_time = 0
    $ store.current_line = "dlc_independent"
    $ store.dlc_independent_mode = True

    jump dlc_prologue

# When DLC ends
label dlc_end:
    # Restore main line state (if player chooses to return)
    $ store.source_time = main_source_time
    $ store.current_line = main_current_line
    $ store.dlc_independent_mode = False

    jump time_choice_menu
```

---

## 3. Character Extension

### 3.1 Adding New Characters

In `dlc/your_dlc_name/characters.rpy`:

```python
# ============================================================================
# New Character Definition
# ============================================================================

define new_char = Character(
    "New Character Name",  # Display name
    color="#FF6B6B",      # Dialogue box color
    what_prefix="「",     # Dialogue prefix
    what_suffix="」"      # Dialogue suffix
)

# ============================================================================
# Character Relationship State
# ============================================================================

# Add in 00_setup.rpy (or use default)
default new_char_relationship = "UNMET"

# Relationship progress definition (for reference, actual use is direct assignment)
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER

# ============================================================================
# Character Trait Definition
# ============================================================================

init python:
    # Character language traits (used for cross-language instruction errors)
    new_char_language_traits = {
        "language": "YourLanguage",
        "has_gc": True,           # Has garbage collection
        "strong_typing": True,    # Strong typing
        "memory_safety": True,    # Memory safe
        "concurrency_model": "async"  # Concurrency model
    }
```

### 3.2 Using Existing Characters

DLC can directly use main game characters:

```python
label dlc_event_with_cee:
    scene bg memory_warehouse

    show cee normal at center

    # Check relationship state
    if cee_relationship in ["RELIABLE", "RESONANT", "PARTNER"]:
        cee "You've come. How can I help?"
    else:
        cee "Need something?"

    # Use affection system
    $ track_affection("cee", 10)

    jump end_time_period
```

### 3.3 Character Sprite Specifications

```
images/
├── YourLanguage/
│   ├── char_name normal.png    # Default expression
│   ├── char_name happy.png     # Happy
│   ├── char_name sad.png       # Sad
│   └── char_name thinking.png  # Thinking
```

**Naming Conventions**:
- Use lowercase + spaces (Ren'Py handles automatically)
- Format: `character_name expression.png`
- Use in code: `show char_name happy`

---

## 4. Event and Chapter Creation

### 4.1 Main Event Template

```python
# ============================================================================
# DLC_01: Chapter Title
# ============================================================================

label dlc_DLC01_start:
    # Set scene
    scene bg your_location

    # Show character
    show new_char normal at center

    # Opening narration
    narrator "Description of scene..."

    new_char "Character's first line"

    # Player choice
    menu:
        "Option A":
            jump dlc_DLC01_choice_a

        "Option B":
            jump dlc_DLC01_choice_b

        # Conditional option (requires specific relationship)
        "Special Option (needs friendly relationship)" if new_char_relationship in ["FRIEND", "CLOSE", "PARTNER"]:
            jump dlc_DLC01_choice_special

label dlc_DLC01_choice_a:
    new_char "You chose A"

    # Update relationship
    $ new_char_relationship = "ACQUAINTED"
    $ track_affection("new_char", 5)

    # Mark chapter complete
    $ complete_chapter("dlc_01")

    jump end_time_period

label dlc_DLC01_choice_b:
    new_char "You chose B"

    # May trigger consequences
    $ apply_consequence("minor", ["new_char"], duration=1)

    $ complete_chapter("dlc_01")
    jump end_time_period
```

### 4.2 Random Event Template

```python
# Add to all_events list in explore_events.rpy

label event_dlc_random_01:
    scene bg your_location
    show new_char normal at center

    narrator "Random event description..."

    new_char "A line"

    $ track_affection("new_char", 5)

    jump end_time_period
```

### 4.3 Holiday Event Template

```python
label holiday_dlc:
    scene bg your_location

    if new_char_relationship in ["CLOSE", "PARTNER"]:
        # High affection: Character actively invites
        narrator "New character comes to find you..."

        new_char "Nothing to do today, want to..."

        menu:
            "Agree":
                jump holiday_dlc_together

            "Decline":
                jump holiday_dlc_decline

    else:
        # Low affection: Character does their own thing
        narrator "New character seems busy with their own thing..."

        jump end_time_period

label holiday_dlc_together:
    # Special scene
    scene bg special_location

    narrator "You spent a pleasant time together..."

    $ new_char_relationship = "CLOSE"
    $ track_affection("new_char", 20)

    jump end_time_period
```

---

## 5. Custom Endings

### 5.1 DLC-Exclusive Endings

```python
# dlc/your_dlc_name/endings.rpy

# ============================================================================
# DLC True End
# ============================================================================

label ending_dlc_true:
    scene bg dlc_final_location
    with Fade(3.0, 1.0, 3.0)

    show new_char happy at center

    narrator "Ending description..."

    new_char "Last line"

    narrator "【DLC Ending: Ending Name】"
    narrator "Ending meaning..."

    # Record ending
    $ record_ending("dlc_true_end")

    jump ending_final_ack  # Use main game credits screen

# ============================================================================
# DLC Normal End
# ============================================================================

label ending_dlc_normal:
    scene bg dlc_location

    if new_char_relationship in ["FRIEND", "CLOSE"]:
        show new_char normal at center
        new_char "Not a bad ending"
    else:
        narrator "Ordinary ending..."

    narrator "【DLC Ending: Normal Ending】"

    $ record_ending("dlc_normal_end")

    jump ending_final_ack
```

### 5.2 Integration with Main Game Endings

```python
# Modify check_ending_conditions() behavior
init python:
    def check_dlc_ending_conditions():
        # Check DLC endings first
        dlc_ending = dlc_check_ending()
        if dlc_ending:
            return dlc_ending

        # If DLC mode enabled, delay main game ending
        if getattr(store, 'dlc_independent_mode', False):
            return "none"

        # Otherwise use main game ending logic
        return check_ending_conditions()
```

### 5.3 Multi-Ending Condition Design

```python
init python:
    def dlc_check_ending():
        # Get all relevant states
        dlc_rel = getattr(store, 'new_char_relationship', 'UNMET')
        main_cee = store.cee_relationship
        main_jawa = store.jawa_relationship
        st = store.source_time

        # True End: DLC character highest + main game two characters both high
        if dlc_rel == "PARTNER":
            if main_cee in ["RESONANT", "PARTNER"] and main_jawa in ["SYNCHRONIZED", "PARTNER"]:
                return "dlc_true_end_integration"  # Integration ending

        # Good End: DLC character high
        if dlc_rel in ["CLOSE", "PARTNER"]:
            return "dlc_good_end"

        # Normal End: Complete DLC main line
        if getattr(store, 'dlc_main_completed', False):
            return "dlc_normal_end"

        # Bad End: DLC character low but time's up
        if st >= 50 and dlc_rel in ["UNMET", "ACQUAINTED"]:
            return "dlc_bad_end"

        return None
```

---

## 6. Consequence System Integration

### 6.1 Consequence Levels

| Level | Affected Scope | Use Case |
|------|---------|---------|
| `minor` | Current task | Small error, can retry |
| `moderate` | Character available time | Medium error, affects subsequent interactions |
| `severe` | Affects other characters | Serious error, triggers branch conflicts |
| `fatal` | Triggers emergency event | Fatal error, forces entry to special chapter |

### 6.2 Using Consequence System

```python
# Minor consequence
$ apply_consequence("minor", ["new_char"], duration=0)

# Moderate consequence
$ apply_consequence("moderate", ["new_char", "cee"], duration=3)

# Severe consequence
$ apply_consequence("severe", ["new_char", "cee", "jawa"], duration=5)

# Check if there are uncleared consequences
if current_consequence != "none":
    narrator "Previous errors are still affecting this place..."
```

### 6.3 Cross-Language Instruction Errors

```python
# Demo: Use C's pointer logic to operate new character (if new character is high-level language)
label dlc_cross_language_error_demo:
    narrator "You try to directly manipulate new character's internal data..."

    if new_char_language_traits["strong_typing"]:
        new_char "Type mismatch. Cannot access directly."

        # Trigger consequence
        $ apply_consequence("minor", ["new_char"], duration=0)
        $ cross_language_error_occurred = True
        $ cross_language_error_type = "pointer_to_high_level"

        jump dlc_error_recovery
```

---

## 7. File Structure Specifications

### 7.1 Complete DLC Structure

```
rpy/dlc/your_dlc_name/
├── config.rpy              # DLC configuration and metadata
├── characters.rpy          # New character definitions
├── variables.rpy           # DLC-specific variables
├── timeline.rpy            # Timeline extensions
├── events/
│   ├── DLC_01_intro.rpy    # Chapter 1
│   ├── DLC_02_xxx.rpy      # Chapter 2
│   ├── random_events.rpy   # Random events
│   └── holidays.rpy        # Holiday events
├── endings.rpy             # Endings
└── hooks.rpy               # Hooks with main game
```

### 7.2 config.rpy Template

```python
# ============================================================================
# DLC Configuration File
# ============================================================================

init python:
    # DLC metadata
    dlc_info = {
        "id": "your_dlc_name",
        "name": "DLC Display Name",
        "version": "1.0.0",
        "author": "Author Name",
        "description": "DLC description",
        "dependencies": [],  # Other DLCs this depends on
        "conflicts": []      # Conflicting DLCs
    }

    # DLC options
    dlc_options = {
        "disable_main_ending": False,     # Disable main game ending
        "independent_timeline": False,    # Independent timeline
        "custom_ending_time": 50,         # Custom ending time
        "integrate_with_main": True       # Integrate with main game
    }

    # Register DLC
    if 'registered_dlcs' not in globals():
        registered_dlcs = []

    registered_dlcs.append(dlc_info)
```

### 7.3 hooks.rpy Template

```python
# ============================================================================
# DLC Hooks - Integration Points with Main Game
# ============================================================================

# Add DLC location to plaza menu in main game time selection menu
init python:
    # Add DLC location to plaza menu
    dlc_location_options = [
        {
            "text": "Go to New Location",
            "condition": "store.source_time >= 5",  # Unlock condition
            "jump": "dlc_location_entry"
        }
    ]

# Execute before main game ending evaluation
label hook_before_ending_evaluation:
    # Check DLC ending conditions
    if hasattr(store, 'dlc_check_ending'):
        $ dlc_ending = dlc_check_ending()
        if dlc_ending:
            jump expression dlc_ending

    # Continue main game ending evaluation
    jump shared_ending_evaluation

# Add DLC character options in main game holidays
label hook_holiday_options:
    menu:
        "Find New Character" if new_char_relationship != "UNMET":
            jump holiday_dlc

        "Continue Main Line":
            return
```

---

## 8. API Reference

### 8.1 Time System

```python
# Advance time
advance_source_time(amount)      # Increase ST
set_source_time(st)              # Set ST

# Get time information
get_current_time_period()        # Returns "ST_XX-XX"
get_time_period()                # Returns time period description

# Time period judgment
if store.source_time < 36:       # During main game
if store.source_time >= 36:      # During ending
```

### 8.2 Relationship System

```python
# Directly set relationship
$ cee_relationship = "FUNCTIONAL"
$ new_char_relationship = "FRIEND"

# Get relationship tier value
tier = get_relationship_tier("cee")  # 0-5

# Check relationship tier
if is_high_relationship("cee", minimum_tier=3):  # RELIABLE+
    # High affection logic

# Track affection changes
$ track_affection("cee", 10)  # +10 affection
```

### 8.3 Chapter Progress

```python
# Set chapter status
set_chapter_status("c_01", "completed")
get_chapter_status("c_01")  # Returns "unstarted", "in_progress", "completed", "skipped"

# Convenience functions
complete_chapter("c_01")
skip_chapter("c_01")
```

### 8.4 Consequence System

```python
# Apply consequence
apply_consequence(level, affected_characters, duration)

# Clear consequence
clear_consequence()

# Reduce consequence duration
reduce_consequence_duration(amount)

# Check consequence
if current_consequence != "none":
    # Has unhandled consequences
```

### 8.5 Ending System

```python
# Check ending conditions
ending = check_ending_conditions()  # Returns ending ID or "none"

# Record ending
record_ending("true_end")

# Get triggered endings
triggered_endings  # List
```

---

## 9. Best Practices

### 9.1 Naming Conventions

| Type | Convention | Example |
|------|------|------|
| Label | `character_chapterID_action` | `cee_C01_start`, `dlc_DLC01_choice_a` |
| Variable | `character_purpose` | `cee_relationship`, `dlc_main_completed` |
| File | `purpose_description.rpy` | `C_01_pointers.rpy`, `DLC_01_intro.rpy` |
| Image | `character expression.png` | `cee normal.png`, `new_char happy.png` |

### 9.2 Compatibility Check

```python
# Check compatibility when DLC starts
label dlc_start:
    # Check main game version
    if config.version < "0.2.0":
        narrator "This DLC requires main game version 0.2.0 or higher"
        return

    # Check conflicting DLCs
    if "conflicting_dlc" in [d["id"] for d in registered_dlcs]:
        narrator "This DLC conflicts with installed DLC"
        return

    jump dlc_prologue
```

### 9.3 Save Compatibility

```python
# Use getattr to handle potentially non-existent variables
dlc_var = getattr(store, 'dlc_custom_var', default_value)

# Use hasattr to check if feature exists
if hasattr(store, 'some_dlc_function'):
    $ some_dlc_function()
```

### 9.4 Performance Considerations

```python
# Avoid complex calculations in code executed every frame
# Use flag variables to cache results

default dlc_computed_once = False
default dlc_cached_result = None

init python:
    def dlc_expensive_check():
        if not store.dlc_computed_once:
            # Complex calculation
            store.dlc_cached_result = complex_computation()
            store.dlc_computed_once = True
        return store.dlc_cached_result
```

---

## 10. Example Templates

### 10.1 Minimal DLC Template

```python
# rpy/dlc/minimal_dlc/config.rpy
init python:
    dlc_info = {
        "id": "minimal_dlc",
        "name": "Minimal DLC Example",
        "version": "1.0.0",
        "author": "Developer"
    }

# rpy/dlc/minimal_dlc/characters.rpy
define mini_char = Character("Mini", color="#00FF00")
default mini_relationship = "UNMET"

# rpy/dlc/minimal_dlc/events/DLC_01.rpy
label mini_DLC01_start:
    scene bg plaza_noon
    show cee normal at left
    show mini_char normal at right

    cee "This is Mini, the newcomer."
    mini_char "Hello!"

    menu:
        "Welcome":
            $ mini_relationship = "FRIEND"
            mini_char "Thanks!"

        "Nod":
            $ mini_relationship = "ACQUAINTED"
            mini_char "..."

    $ complete_chapter("mini_01")
    jump end_time_period
```

### 10.2 Complete Chapter Template

```python
# ============================================================================
# DLC_01: Complete Chapter Template
# ============================================================================

# Chapter metadata (used for debugging and documentation generation)
# CHAPTER_META:
#   id: DLC_01
#   title: Chapter Title
#   character: new_char
#   tech_concept: Technical Concept
#   source_time: ST_XX-XX
#   consequence_level: minor/moderate/severe

label dlc_DLC01_start:
    # ===== Prerequisite Check =====
    if store.source_time < 10:
        narrator "This event is not unlocked yet."
        jump time_choice_menu

    # ===== Scene Setup =====
    scene bg dlc_location
    with Fade(1.0)

    # ===== Character Entrance =====
    show new_char normal at center

    # ===== Opening Narration =====
    narrator "Describe what the player sees after entering the scene..."

    # ===== Character First Dialogue =====
    new_char "Character's opening line..."

    # ===== Scene Development =====
    narrator "Further description..."

    # ===== Core Interaction =====
label dlc_DLC01_main_interaction:
    new_char "Now there's a problem that needs solving..."

    # Show "brute force solution"
    narrator "New character's current approach is... (inefficient solution)"

    menu:
        "Option A - Provide optimized solution":
            jump dlc_DLC01_optimal

        "Option B - Let them continue with original plan":
            jump dlc_DLC01_brute_force

        "Option C - Propose another solution":
            jump dlc_DLC01_alternative

        # Conditional option
        "Special Option (requires high relationship)" if new_char_relationship in ["CLOSE", "PARTNER"]:
            jump dlc_DLC01_special

# ===== Branch A: Optimal Solution =====
label dlc_DLC01_optimal:
    narrator "You propose a more efficient solution..."

    new_char "That's a great idea!"

    # Execution succeeds
    narrator "New character executes your solution, significant results..."

    # Update state
    $ new_char_relationship = "FRIEND"
    $ track_affection("new_char", 15)
    $ efficiency_multiplier = 5.0

    jump dlc_DLC01_end_good

# ===== Branch B: Brute Force Solution =====
label dlc_DLC01_brute_force:
    narrator "New character continues with original plan..."

    # Slow execution
    narrator "A long time passes..."

    new_char "Done. Not very efficient."

    # Minor consequence
    $ track_affection("new_char", 5)

    jump dlc_DLC01_end_neutral

# ===== Branch C: Alternative Solution =====
label dlc_DLC01_alternative:
    narrator "You propose another solution..."

    new_char "This solution works, but has limitations..."

    # Medium effect
    $ track_affection("new_char", 10)
    $ efficiency_multiplier = 2.0

    jump dlc_DLC01_end_neutral

# ===== Branch D: Special Option =====
label dlc_DLC01_special:
    narrator "Based on your deep relationship, you directly point out the core issue..."

    new_char "You're right. I've been going in circles."

    # Best effect
    $ new_char_relationship = "CLOSE"
    $ track_affection("new_char", 25)
    $ efficiency_multiplier = 10.0

    jump dlc_DLC01_end_good

# ===== Ending A: Good Ending =====
label dlc_DLC01_end_good:
    scene bg dlc_location
    show new_char happy at center

    new_char "Thanks for your help. I learned a lot."

    narrator "Your relationship with the new character has grown closer..."

    $ complete_chapter("dlc_01")

    jump end_time_period

# ===== Ending B: Normal Ending =====
label dlc_DLC01_end_neutral:
    scene bg dlc_location
    show new_char normal at center

    new_char "Task completed."

    $ complete_chapter("dlc_01")

    jump end_time_period
```

GitHub repository development template: https://github.com/NewJerseyStyle/CodeLove-DLC

---

## Appendix: Existing Character Reference

### Character List

| ID | Name | Language | Relationship Variable | Relationship Progress |
|----|------|------|---------|---------|
| cee | Cee | C | `cee_relationship` | UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER |
| jawa | Jawa | Java | `jawa_relationship` | UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER |
| rusty | Rusty | Rust | `rusty_relationship` | UNMET → ACQUAINTED → TRUSTED → BORROWED → OWNED |
| golly | Golly | Go | `golly_relationship` | UNMET → CONCURRENT → CHANNELLED → SYNCED |
| py | Py | Python | `py_relationship` | UNMET → IMPORTED → RUNNING → PYTHONIC |

### Scene List

| ID | Scene Name | Purpose |
|----|--------|------|
| `bg memory_warehouse` | Memory Warehouse | Cee's main location |
| `bg contract_office` | Contract Office | Jawa's main location |
| `bg plaza_morning/noon/afternoon/evening/night` | Information Plaza | Main menu |
| `bg laboratory` | Laboratory | Real world |
| `bg source_realm_entrance` | Source Realm Entrance | Transition |

---

**Version**: 1.0.0
**Last Updated**: 2025-02-25
