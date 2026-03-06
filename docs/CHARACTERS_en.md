# Source Realm - Character Design Document

> This document consolidates design specifications for all language characters, for reference by DLC developers and writers.

---

## Table of Contents

1. [Cee (C Language)](#1-cee-c-language)
2. [Jawa (Java)](#2-jawa-java)
3. [Rusty (Rust)](#3-rusty-rust)
4. [Golly (Go)](#4-golly-go)
5. [Py (Python)](#5-py-python)
6. [Source (阿源)](#6-source-阿源)

---

## 1. Cee (C Language)

**Occupation**: Memory Warehouse Manager
**First Appearance**: Prologue

### Core Characteristics

| Characteristic | Behavior |
|--------|---------|
| Manual Memory Management | Resources must be manually returned after use, otherwise they continue to occupy |
| No GC | No automatic cleanup, player must give explicit instructions |
| Direct Hardware Access | Instant arrival, bit-level precision operations |
| No Runtime Safety Net | Accepts any instructions without question, no safety checks |
| Consequences Affect Everyone | Errors affect other characters in the vicinity |

### Dialogue Style

- **Extremely Concise**: Never says two words when one will do
- **No Warnings, No Judgments, No Comforting**: Only executes and describes
- **Key Phrases**: "Efficient." "Address of Information Plaza."

### Relationship FSM

```
UNMET → FIRST_CONTACT → FUNCTIONAL → RELIABLE → RESONANT → PARTNER/CLOSE_ALLY
```

---

## 2. Jawa (Java)

**Occupation**: Contract Office Architect
**First Appearance**: J_01

### Core Characteristics

| Characteristic | Behavior |
|--------|---------|
| Automatic GC | Periodically enters "garbage collection" state, stops responding |
| Strong Typing | Refuses any operations with undefined types |
| Interface | Prefers defining interfaces first, then implementing details |
| Cross-platform JVM | Behavior is completely consistent in any environment |
| synchronized | Requires pre-defined synchronization rules for multitasking |

### Dialogue Style

- **Rigorous and Formal**: Like a lawyer or architect
- **Requires Clear Definitions**: "What is your interface definition?"
- **After GC Pause**: "Sorry, GC."

### Relationship FSM

```
UNMET → FORMAL_CONTACT → VERIFIED → TRUSTED → SYNCHRONIZED → PARTNER/DEEP_ALLY
```

---

## 3. Rusty (Rust)

**Occupation**: Memory Warehouse Apprentice Manager (Cee's Junior)
**First Appearance**: C_04

### Core Characteristics

| Characteristic | Behavior |
|--------|---------|
| Ownership System | Confirms "who owns this resource" before doing anything |
| Borrow Checking | Marks resources when borrowed, unmarks when returned |
| Compile-time Safety | Some errors are rejected before execution |
| No GC but Safe | Manual release required, but with compiler protection |

### Dialogue Style

- **Gentle but Firm**: Speaks more gently than Cee, but never compromises on principles
- **Confirms Ownership**: "Has the owner of this resource been confirmed?"
- **Refuses Unsafe Operations**: "This is not safe."

### Relationship FSM

```
UNMET → CAUTIOUS → TRUSTING → RELIABLE → PROTECTED → PARTNER/CLOSE_GUARDIAN
```

---

## 4. Golly (Go)

**Occupation**: Parallel System Engineer
**First Appearance**: J_05

### Core Characteristics

| Characteristic | Behavior |
|--------|---------|
| Goroutine | Can handle multiple things simultaneously |
| Channel Communication | Needs explicit channels to synchronize |
| Simple Syntax | Dislikes tedious specifications |
| Fast Compilation | Can start working immediately |
| GC | Has GC but simpler than Java |

### Dialogue Style

- **Cheerful and Energetic**: Direct and friendly
- **Dislikes Tediousness**: "Too troublesome! Just do it directly!"
- **Likes Parallelism**: "I like parallelism!"

### Relationship FSM

```
UNMET → QUICK_HELLO → PARALLEL_WORK → CHANNEL_SYNC → CONCURRENT_MASTER → PARTNER/GO_BUDDY
```

---

## 5. Py (Python)

**Occupation**: Automation Scripter / Data Scientist
**First Appearance**: J_01 (as a contrasting character)

### Core Characteristics

| Characteristic | Behavior |
|--------|---------|
| Dynamic Typing | Freely changes labels on things |
| Indentation Syntax | Very hierarchical speech, obsessive about alignment |
| Garbage Collection | Just tosses used items |
| GIL | Can only do one thing at a time, multitasking crashes |
| Simple and Easy to Learn | The most friendly character to players |

### Dialogue Style

- **Lazy and Casual**: Like a smart but somewhat slack university student
- **Values Simplicity**: "Simple, elegant."
- **Indentation OCD**: "Back four spaces! Do you want my world to collapse?"

---

## 6. Source (阿源)

**Occupation**: Programming Language Researcher / Source Realm Administrator
**First Appearance**: Prologue (leaves a note)

### Appearance Timing (Strictly Limited)

1. **Prologue**: Leaves note, laboratory scene
2. **Bad End A**: Weeks later in reality, forcibly terminates program to save player
3. **Mid-game System Logs** (Optional): Comedy element, hints at Source's existence in reality

**Main Line**: Source is at the convenience store (always on the way to the convenience store)

### Core Characteristics

- **Administrator Privileges**: Highest execution authority in the Source Realm, almost never used
- **Enthusiastic but Forgetful**: Often says "be right back" then stays away for a long time
- **Strong Sense of Responsibility**: Very concerned about player safety

### Dialogue Style

- **Prologue Note**: Concise and direct, somewhat hurried
- **Bad End A**: Anxious, self-blaming, urgent

---

## Character Relationship Quick Reference

| Character A | Character B | Relationship Description |
|--------|--------|---------|
| Cee | Rusty | Senior and Junior; Rusty admires Cee's speed but doesn't agree with her methods |
| Cee | Jawa | Memory Warehouse vs Contract Office; Direct execution vs defining protocols |
| Jawa | Golly | Rigorous specs vs simple and direct; debate in J_05 |
| Py | Everyone | The ultimate in flexibility; provides "cheat-like simplified solutions" |

---

## Writer Quick Checklist

- [ ] Do character reactions completely match their language characteristics?
- [ ] Are technical concepts presented as scene metaphors (not code)?
- [ ] Is the dialogue style correct for the corresponding affection level?
- [ ] Do consequences affect other characters or the environment?
