#  Dice Roller — Multiplayer CLI Game

A feature-rich terminal-based dice rolling game built in Python. Roll dice, compete with friends, track your scores, and enjoy ASCII art dice faces — all from the command line!

---

##  Preview

```
=============================================
          WELCOME TO DICE ROLLER  
=============================================

How many players? (1-4): 2
Enter name for Player 1: Alice
Enter name for Player 2: Bob

─────────────────────────────────────────────
    Alice's Turn
─────────────────────────────────────────────
  Roll the dice? (y/n): y

  Dice 1       Dice 2
  ┌─────────┐   ┌─────────┐
  │  ●   ●  │   │  ●      │
  │    ●    │   │    ●    │
  │  ●   ●  │   │      ●  │
  └─────────┘   └─────────┘

  ● Result     : 5 + 3 = 8
  ● Rolls      : 1
  ● Total Score: 8
```

---

##      Features

- 🎨 **ASCII Art Dice Faces** — Visual dice representation for all values 1–6
- ➕ **Dice Total Display** — Automatically shows the sum of both dice after each roll
- 🔢 **Roll Counter** — Tracks how many times each player has rolled
- 👥 **Multiplayer Support** — Supports 1 to 4 named players with turn rotation
- 🚪 **Dynamic Player Exit** — Players can leave at any time by typing `n`; the game continues for remaining players
- 🏆 **End Game Summary** — Final results displayed when all players exit

---

##  How to Play

1. **Launch** the game using the command above
2. **Enter** the number of players (1–4)
3. **Enter** a name for each player
4. Players take turns in order — on your turn:
   - Press **`y`** to roll both dice
   - Press **`n`** to step out of the game
5. The game ends when **all players** have exited
6. Final scores and roll counts are displayed at the end

---

##  Built With

- **Language:** Python 3
- **Module:** `random` (standard library)
- **Interface:** Command Line (CLI)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

---

## 💡 Possible Improvements

- [ ] Add a **high score leaderboard** saved to a file
- [ ] Implement a **betting/wagering system**
- [ ] Add **special rules** (e.g., doubles = roll again)
- [ ] Create a **GUI version** using Tkinter or PyGame
- [ ] Add **sound effects** for dice rolls

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

##  Author

**Shujaat Hussain (Ai-Engineer)**
- GitHub: [@your-username](https://github.com/Shujaa93)

---

> Made with ❤️ and Python — Happy Rolling! 
