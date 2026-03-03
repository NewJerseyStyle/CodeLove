# Source Realm (源界) 🌐

> A Galgame-styled RPG that teaches programming through high-stakes digital romance

**Learn programming languages by dating their personified characters. Fail to understand concepts, face soul-crushing romantic rejection. Succeed, unlock the secrets of the Source Realm.**

---

[**中文版 README**](README.md) | Read in English

---

## 🎮 What is This Game?

**Source Realm** is a visual novel adventure that transforms learning programming into a dramatic Galgame experience.

- **Not your typical coding tutorial**: Instead of memorizing syntax, you learn by forming relationships with characters representing different programming languages
- **Consequences matter**: Wrong answers don't just give you an "X"—they trigger narrative consequences that ripple through the world
- **Learn by doing**: Provide optimized algorithms to characters who use brute-force solutions, then watch them execute with stunning efficiency
- **Multiple paths**: Your time is limited—choose which language lines to pursue and face different endings

**Inspired by a friend who wondered: "Why can't we play a Galgame to learn programming by failing to get girls and being punished for not knowing right concepts?"** 💖

---

## ✨ Core Features

### 🎯 Algorithm Interaction System
Characters have powerful execution abilities but lack planning skills. You observe their inefficient brute-force solutions (O(n²) and worse), then provide optimized algorithms they immediately implement.

### 💔 The Consequence System
- **Minor errors**: Affect only the current task
- **Moderate errors**: Flood Cee's workspace, she needs time to clean up
- **Severe errors**: Affect nearby NPCs, disrupt their work
- **Fatal errors**: Source Realm region crashes, all characters in crisis state

**Lesson**: Irresponsible code is dangerous to the whole community.

### ⏰ Parallel Timeline System
Each time period, you choose which storyline to pursue. Others continue without you—consequences of your mistakes persist regardless of which path you take.

### 🎭 Dynamic Relationships
Characters won't change to suit you. Their core programming language traits are immutable—you must learn to work with them as they are.

### 🎉 NEW: Community DLC System (v0.1.4)
**Create your own programming language characters and regions!**

- Design characters based on JavaScript, Ruby, Swift, or any language
- Build custom regions with their own menus and events
- Package as ZIP—users just extract and play
- No need to modify main game files

**First DLC Available**: **Python language character "Py"** with Zen Garden region!
- Download: [CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC/releases)

---

## 📖 The Story

You find yourself in an empty laboratory with a single note:

> "Went to convenience store. Be right back. Don't touch anything."

Curiosity leads you to the terminal. A scan triggers, and suddenly you're digitized—TRON-style—plunging into Source Realm, a parallel space where programming logic manifests as physical reality.

Here, memory is land, threads are roads, and compiler is law of nature.

You land in Cee's Memory Warehouse just as she freezes—the classic "Segmentation Fault → Core Dump" reaction to unexpected input. When she reboots, her first question isn't "Are you okay?"—it's:

> "What's your type?"

This isn't a greeting. This is a necessary type check. Welcome to Source Realm.

---

## 👥 Meet the Characters

Each character represents a programming language with immutable traits.

### Cee (C Language) 💾
**Profession**: Memory Warehouse Manager
**Traits**: Manual memory management, no GC, direct hardware access
**Behavior**: Accepts any instruction without questioning; consequences are your problem

> "Efficient." (Her highest compliment)

### Jawa (Java) ☕
**Profession**: Contract Office Architect
**Traits**: JVM bytecode, automatic GC, strong typing, cross-platform
**Behavior**: Needs specifications defined first; has unpredictable GC freeze periods

### Rusty (Rust) 🦀
**Profession**: Memory Warehouse Apprentice
**Traits**: Ownership system, compile-time safety, absolutely reliable
**Behavior**: Strictly checks resource ownership before agreeing to anything

### Golly (Go) 🔵
**Profession**: Parallel Systems Engineer
**Traits**: Goroutines, GC, simple syntax, handles many tasks simultaneously
**Behavior**: Practical and direct; dislikes bureaucracy

### Py (Python) 🐍 (NEW - DLC)
**Profession**: Automation Scripter
**Traits**: Dynamic typing, indentation syntax, GIL, pursues simplicity
**Behavior**: Extremely flexible but format-sensitive; enjoys teaching through simplicity

---

## 🏆 Endings

Your choices affect which ending you get:

| Ending | How to Unlock |
|--------|---------------|
| **Language Partner** (Normal) | Complete any language line, reach RELIABLE+ relationship |
| **????** (Secret) | All characters reach maximum affection (tribute to veteran programmers) |
| **Nothing happened** | No route reaches FUNCTIONAL |

---

## 🎲 Download & Play

### System Requirements
- **OS**: Windows / macOS / Linux
- **Dependencies**: None required (Ren'Py is self-contained)
- **Storage**: ~500 MB

### Installation
1. Download [latest version](https://github.com/NewJerseyStyle/CodeLove/releases/latest)
2. Extract and run `SourceRealm.exe` (Windows) or corresponding executable
3. Start playing!

### Optional: Install Py-DLC
1. Download [CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC/releases)
2. Extract to game directory (any subfolder works)
3. In-game, go to Plaza → "Go to Other Regions" → "Zen Garden"

---

## 📚 Documentation & Modding

**Want to create your own DLC?** We provide comprehensive tools:

| Resource | Description |
|----------|-------------|
| [DLC Developer Guide](https://github.com/NewJerseyStyle/codeLoveGame-GLM/blob/main/docs/DLC_DEVELOPER_GUIDE.md) | Complete step-by-step guide |
| [DLC Quick Reference](https://github.com/NewJerseyStyle/codeLoveGame-GLM/blob/main/docs/DLC_QUICK_REFERENCE.md) | One-page reference |
| [DLC Template](https://github.com/NewJerseyStyle/CodeLove-DLC) | Ready-to-use template |
| [DLC Example](https://github.com/NewJerseyStyle/CodeLove-Py-DLC) | Complete working example |

**What You Can Create**:
- New programming language characters
- Custom regions (towns, districts, buildings)
- Unique storylines teaching specific concepts
- Special endings tied to your character

---

## 📞 Community & Support

- **[Discussions](https://github.com/NewJerseyStyle/CodeLove/discussions)**: Share ideas, report bugs, discuss DLC

**We're actively looking for community DLC creators!** If you build something amazing, let us know—we may feature it on the main page!

---

## 📜 Changelog

### v0.1.4 (Current)
- ✨ NEW: Community DLC system
- ✨ NEW: Python DLC with Zen Garden region
- 🐛 Fixed: Character sprite leaks in encounters
- 🐛 Fixed: Init priority issues
- 🐛 Fixed: DLC region unlock conditions
- 📚 Added: Complete DLC development documentation

### v0.1.3
- Enhanced consequence system
- Improved algorithm interaction feedback
- Added more random events

### v0.1.2
- Initial release with Cee, Jawa, Rusty, Golly

---

## 💡 Why This Game Exists

Most programming tutorials are dry, abstract, and disconnected from real use. They teach syntax without philosophy, rules without reason.

**Source Realm** takes a different approach:

- **Emotional engagement**: Consequences feel real because they affect characters you care about
- **Philosophy over syntax**: Learn *why* languages are designed this way, not just *how* to write code
- **Interactive learning**: Provide solutions, watch them execute, see immediate impact
- **Multiple perspectives**: Each language has strengths and weaknesses—you learn to choose, right tool

It's a tribute to complexity and beauty of programming languages, wrapped in the format of a Galgame.

---

> "Code isn't written for machines, it's written for people."
> — An ancient wise programmer

> "Why can't we play a Galgame to learn programming by failing to get girls and being punished for not knowing right concepts?"
> — The friend who started it all 💖

---

**Created with love, logic, and a touch of dramatic flair.**
