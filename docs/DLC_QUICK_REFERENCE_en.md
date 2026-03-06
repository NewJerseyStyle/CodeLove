# Source Realm - DLC Development Quick Reference

> 📌 One-page quick reference, for detailed explanations see [DLC_DEVELOPER_GUIDE_en.md](DLC_DEVELOPER_GUIDE_en.md)

---

## Region-Oriented Design (Recommended)

DLC uses **region-oriented** design, each DLC has its own independent region.

```
Plaza (Main Game Hub)
    ├── Memory Warehouse (Cee)
    ├── Contract Office (Jawa)
    └── [Go to Other Regions]        ← Automatically displays registered DLC regions
            ├── Zen Garden (Py-DLC)
            └── Your Region
```

---

## Register Region

```python
# config.rpy
init python:
    register_dlc_region("your_region", {
        "name": "Your Region",
        "description": "Description",
        "dlc_id": "your_dlc",
        "entry_label": "enter_your_region",
        "unlock_condition": lambda: store.c_01_status == "completed",
    })
```

---

## Dynamic Menu Notes

Ren'Py's `renpy.display_menu()` **does not support blank indentation**.

**Incorrect Approach** (blanks are ignored):
```python
choices = [
    ("  Sub-option 1", "option1"),  # ❌ Blanks ignored
    ("    Sub-option 2", "option2"),  # ❌ Blanks ignored
]
selection = renpy.display_menu(choices)
```

**Correct Approach** (use full-width space `　`):
```python
choices = [
    (u"　Sub-option 1", "option1"),     # ✅ Use full-width space
    (u"　　Sub-option 2", "option2"),  # ✅ Multiple full-width spaces
]
selection = renpy.display_menu(choices)
```

**Other Whitespace Character Options**:
- `\u2003` (EM SPACE) - Wider space
- `\u3000` (IDEOGRAPHIC SPACE) - Full-width space (recommended)

---

## Region Entry Template

```renpy
# events/region_hub.rpy

label enter_your_region:
    scene bg your_region with fade
    narrator "You have arrived at Your Region."
    jump your_region_hub

label your_region_hub:
    scene bg your_region
    show your_char normal at center

    menu:
        "Learn with Your Char":
            jump your_event
        "Return to Plaza":
            jump return_to_plaza

label return_to_plaza:
    scene black with fade
    narrator "You have returned to the plaza."
    jump time_choice_menu
```

---

## DLC Registration API

```python
init python:
    # Register DLC
    register_dlc({
        "id": "my_dlc",
        "name": "My DLC",
        "version": "1.0.0",
        "author": "Developer",
        "ending_checker": my_dlc_check_ending,  # Optional
    })

    # Register region
    register_dlc_region("region_id", {...})

    # Register character
    register_dlc_character("char_id", {...})

    # Register random event
    register_dlc_random_event("event_label", weight=1.0)
```

---

## Core Variables

```python
# Time
store.source_time           # Current ST (0-36+ main game)

# Relationship State
store.cee_relationship      # UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER
store.jawa_relationship     # UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER

# Chapter State
store.c_01_status           # "unstarted", "in_progress", "completed", "skipped"
```

---

## Common APIs

### Time
```python
advance_source_time(2)      # +2 ST
get_current_time_period()   # "ST_09-12"
```

### Relationships
```python
$ cee_relationship = "FUNCTIONAL"              # Directly set
track_affection("cee", 10)                     # +10 affection
```

### Chapters
```python
complete_chapter("c_01")    # Mark complete
```

### Consequences
```python
apply_consequence("minor", ["cee"], duration=0)
```

---

## File Structure

```
rpy/dlc/your_dlc/
├── config.rpy          # DLC configuration + region registration
├── characters.rpy      # New characters
├── events/
│   ├── region_hub.rpy  # Region hub (required)
│   └── CHAPTER_01.rpy  # Chapter events
└── endings.rpy         # Endings
```

---

## Label Naming Conventions

| Type | Format | Example |
|------|------|------|
| Region Entry | `enter_region_name` | `enter_zen_garden` |
| Region Hub | `region_hub` | `zen_garden_hub` |
| Chapter | `CHAPTER_ID` | `PY_01` |
| Ending | `ending_name` | `ending_py_partner` |

---

## Relationship Progress Template

```python
# Main game characters
Cee:   UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER
Jawa:  UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER

# DLC characters
default my_char_relationship = "UNMET"
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
```

---

## Quick Checklist

- [ ] Register with `register_dlc()`
- [ ] Register region with `register_dlc_region()`
- [ ] Create region entry label (`enter_your_region`)
- [ ] Create region hub menu (`your_region_hub`)
- [ ] Provide "Return to Plaza" option (`jump return_to_plaza`)
- [ ] Declare character variables with `default`
- [ ] Place images in `images/YourLanguage/`

---

## Complete Example

See [CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC) - Complete runnable region-oriented DLC example
