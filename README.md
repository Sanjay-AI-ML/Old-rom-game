# 🎮 Retro ROM-Style Adventure Game (Python)

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white) ![OOP](https://img.shields.io/badge/design-oop-blue) ![JSON](https://img.shields.io/badge/storage-json-blue) ![Save⁄Load](https://img.shields.io/badge/persistence-save--load-green)

A text-based adventure game inspired by classic Pokémon Fire Red, built entirely in Python using Object-Oriented Programming (OOP). Explore a randomized world, battle enemies, manage inventory, and upgrade your character in this engaging retro RPG prototype.

---

## 🎯 What You're Doing

You are an adventurer exploring a mysterious world. Each playthrough is different:
- **Explore** random paths and encounter enemies
- **Battle** turn-based combat with randomized encounters
- **Collect** items and equipment from shops
- **Progress** by gaining experience and upgrading your character
- **Survive** increasingly difficult challenges

---

## 🚀 Quick Start

### Requirements
- Python 3.8+
- No external dependencies (built-in libraries only)

### Installation & Run

```bash
# Clone the repo
git clone https://github.com/Sanjay-AI-ML/Old-rom-game.git
cd Old-rom-game

# Run the game
python main_game.py
```

The game starts with an intro story and drops you into an exploration menu.

---

## 🎮 Gameplay

### Main Menu Options

| Action | What It Does |
|--------|-----------|
| **Explore** | Move in random directions, encounter enemies |
| **Battle** | Engage turn-based combat with current enemy |
| **Shop** | Buy/sell items and equipment |
| **Inventory** | Check your items and stats |
| **Rest** | Heal health (limited rests) |
| **Status** | View current character stats |
| **Quit** | Exit the game |

### Combat System

```
Turn-based Battle Flow:
1. Player attacks (1d20 roll for accuracy)
2. Deal damage based on weapon and stats
3. Enemy counter-attacks
4. Repeat until one side defeated
5. Claim experience and loot
```

**Victory Rewards:**
- Experience points (XP)
- Gold coins
- Random item drops

### Character Progression

- **Health** — Increases as you level up
- **Attack Power** — Improves with weapons and experience
- **Defense** — Mitigates incoming damage
- **Gold** — Currency for shop purchases
- **Experience** — Accumulates to level up

### Shop System

Buy items and equipment:
```
Available Items:
- Health Potions (restore HP)
- Weapons (increase attack)
- Armor (increase defense)
- Shields (damage reduction)
```

---

## 📁 Project Structure

```
Old-rom-game/
├── main_game.py              # Main game loop and entry point
├── game_class.py             # Game state and world management
├── game_controller.py        # Input handling
├── character_class.py        # Player and Enemy classes
├── item_class.py             # Item and Equipment classes
├── shop_class.py             # Shop and commerce system
├── map_class.py              # World/room generation
├── items.json                # Item database (weapons, armor, potions)
├── game_intro.txt            # Opening story
├── Files/                    # Game data directory
└── README.md                 # This file
```

---

## 🏗️ Code Architecture

### Class Hierarchy

```
Character (abstract)
├── Player
│   ├── Health
│   ├── Attack Power
│   ├── Inventory
│   └── Experience
└── Enemy
    ├── Health
    ├── Attack Power
    └── Loot Table

Game
├── Player (instance)
├── Enemies (list)
├── Shop (instance)
├── Map/World (instance)
└── Game Loop

Item
├── Equipment
│   ├── Weapon
│   └── Armor
└── Consumable
    └── Potion
```

### Object-Oriented Principles Demonstrated

- **Encapsulation** — Private attributes (health, attack) with getters/setters
- **Inheritance** — Enemy/Player extend Character base class
- **Polymorphism** — Different item types have specialized `use()` methods
- **Abstraction** — Complex battle logic hidden behind simple `battle()` method

---

## 📊 Game Mechanics

### Health & Combat
```python
Player HP: 100
Enemy HP: 50

Round 1:
  Player attacks: 15 damage → Enemy HP = 35
  Enemy attacks: 8 damage → Player HP = 92

Round 2:
  Player attacks: 20 damage → Enemy HP = 15
  Enemy attacks: 6 damage → Player HP = 86

Round 3:
  Player attacks: 18 damage → Enemy Defeated!
  Victory! +50 XP, +25 Gold, sword drop
```

### Experience & Leveling
```
Level 1 → 0 XP (needed: 100)
Level 2 → 100 XP (needed: 200 total)
Level 3 → 200 XP (needed: 350 total)
```

### Item System
Each item has:
- **Name** — Display identifier
- **Rarity** — Common/Uncommon/Rare/Legendary
- **Cost** — Gold price in shop
- **Effect** — Damage/healing/defense bonus
- **Quantity** — Stack count for consumables

---

## 🎮 Example Gameplay Session

```
========== WELCOME TO THE ADVENTURE ==========
Enter your name: Sanjay
Welcome, Sanjay!

[Story intro loads from game_intro.txt]

========== MAIN MENU ==========
1. Explore
2. Battle
3. Shop
4. Inventory
5. Rest
6. Status
7. Quit

>> 1
You moved EAST
Enemies Found!
A Wild Goblin appears! (HP: 30)

>> 2
========== BATTLE START ==========
Player HP: 100 | Goblin HP: 30

>> attack
Sanjay attacks! 15 damage dealt.
Goblin HP: 15

Goblin attacks! 5 damage dealt.
Sanjay HP: 95

>> attack
Sanjay attacks! 18 damage dealt.
Goblin HP: -3 (DEFEATED!)

Victory! +30 XP, +15 Gold
Loot: Iron Sword

>> 3
========== SHOP ==========
Gold: 40
Available Items:
1. Health Potion (20 Gold)
2. Iron Armor (50 Gold)
3. Wooden Shield (35 Gold)

>> 1
Purchased: Health Potion
Gold: 20

>> 5
Sanjay rests and recovers.
Health: 100/100

>> 6
========== STATUS ==========
Name: Sanjay
Level: 1
HP: 100/100
Attack: 15
Defense: 5
Gold: 20
Experience: 30/100
```

---

## 🧠 Key Concepts Demonstrated

| Concept | Usage |
|---------|-------|
| **Classes** | Character, Player, Enemy, Item, Shop |
| **Inheritance** | Player/Enemy inherit from Character |
| **Encapsulation** | Private health/attack with methods |
| **Polymorphism** | Different item `use()` implementations |
| **Randomization** | Random enemy generation, loot drops |
| **JSON** | items.json stores item database |
| **File I/O** | Load game intro, save game state |
| **Game Loop** | Main menu ↔ exploration ↔ battle cycle |

---

## 📚 Educational Value

This project teaches:
- ✅ **OOP Design Patterns** — Class architecture for game systems
- ✅ **Game Programming** — Loops, state management, turn systems
- ✅ **Data Structures** — Lists, dictionaries for inventory/enemies
- ✅ **JSON** — Load game data and configuration
- ✅ **Random Generation** — Procedural encounters and loot
- ✅ **User Interface** — Menu-driven terminal interactions
- ✅ **Debugging** — Complex game state tracking

---

## 🔧 Customization Ideas

### 1. Add New Item Types
Edit `items.json`:
```json
{
  "items": [
    {"name": "Diamond Sword", "type": "weapon", "damage": 25, "cost": 200},
    {"name": "Magic Potion", "type": "consumable", "healing": 50, "cost": 30}
  ]
}
```

### 2. Implement Save/Load System
```python
def save_game(filename):
    data = {
        "player": player.__dict__,
        "inventory": player.inventory,
        "level": player.level,
        "gold": player.gold
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_game(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    # Restore player state
```

### 3. Add Difficulty Levels
```python
if difficulty == "Easy":
    enemy_hp *= 0.8
    enemy_attack *= 0.8
elif difficulty == "Hard":
    enemy_hp *= 1.5
    enemy_attack *= 1.2
```

### 4. Create Boss Encounters
```python
class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.hp *= 3
        self.attack *= 1.5
        self.special_ability = "Fireball"
```

### 5. Migrate to Tkinter GUI
```python
# Replace terminal menus with graphical buttons
# Add sprite/sprite-like visual representation
# Real-time HP bars instead of text
```

### 6. Add Skills & Magic
```python
class Skill:
    def __init__(self, name, damage, cost_mp):
        self.name = name
        self.damage = damage
        self.cost_mp = cost_mp
```

---

## 🐛 Troubleshooting

### Game crashes on startup
```
Error: ModuleNotFoundError
→ Ensure all files (character_class.py, etc.) are in same directory
```

### Shop menu doesn't work
```
Error: KeyError in items.json
→ Verify items.json syntax (valid JSON format)
→ Check "items" key exists in file
```

### Enemy encounters too hard
- Modify enemy `hp` and `attack` in character_class.py
- Increase starting player stats
- Add more healing items to shop

### Game loop freezes
- Check for infinite loops in main_game.py
- Verify input validation (handle non-numeric input)
- Add timeout on input() calls if needed

---

## 🚀 Future Enhancements

- 🎨 **Tkinter GUI** — Graphical interface with animations
- 💾 **Save/Load System** — Persistent game state
- 🏆 **Leveling System** — Attribute points on level up
- ✨ **Skills & Magic** — Special abilities with cooldowns
- 🗺️ **Larger World** — Multi-room exploration with NPCs
- 🎯 **Quest System** — Objectives and story progression
- 🌟 **Rare Loot** — Legendary items with special effects
- 👥 **Multiplayer** — PvP or cooperative play
- 🎙️ **Sound Effects** — Audio for attacks, victories, level-up

---

## 📄 License

MIT — Free to use, modify, and share with attribution.

---

## 👤 Author

Built by [@Sanjay-AI-ML](https://github.com/Sanjay-AI-ML)

This project was created while learning class-based design and game programming in Python. Questions or feature ideas? Open an issue on GitHub!

**Happy adventuring!** ⚔️🎮
