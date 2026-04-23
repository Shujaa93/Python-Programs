import random

def get_dice_art(value):
    dice_art = {
        1: [
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"
        ],
        2: [
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"
        ],
        3: [
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"
        ],
        4: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        5: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"
        ],
        6: [
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"
        ]
    }
    return dice_art[value]

def display_dice(die1, die2):
    art1 = get_dice_art(die1)
    art2 = get_dice_art(die2)
    print("\n  Dice 1       Dice 2")
    for row1, row2 in zip(art1, art2):
        print(f"  {row1}   {row2}")

def get_players():
    while True:
        try:
            num = int(input("\nHow many players? (1-4): "))
            if 1 <= num <= 4:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Enter a number.")

    players = []
    for i in range(num):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        players.append(name if name else f"Player {i + 1}")
    return players

def play_game():
    print("=" * 45)
    print("        🎲  WELCOME TO DICE ROLLER  🎲")
    print("=" * 45)

    players = get_players()
    scores = {player: 0 for player in players}
    roll_counts = {player: 0 for player in players}

    print("\nLet's roll!\n")

    current_index = 0

    while True:
        current_player = players[current_index]
        print(f"\n{'─' * 45}")
        print(f"  🎮  {current_player}'s Turn")
        print(f"{'─' * 45}")

        choice = input("  Roll the dice? (y/n): ").strip().lower()

        if choice == 'y':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2

            display_dice(die1, die2)

            roll_counts[current_player] += 1
            scores[current_player] += total

            print(f"\n  ● Result  : {die1} + {die2} = {total}")
            print(f"  ● Rolls   : {roll_counts[current_player]}")
            print(f"  ● Total Score: {scores[current_player]}")

            # Move to the next player
            current_index = (current_index + 1) % len(players)

        elif choice == 'n':
            print(f"\n  {current_player} steps out.")

            # Remove the player
            players.pop(current_index)
            del scores[current_player]
            del roll_counts[current_player]

            if not players:
                break

            # Adjust index if needed
            current_index = current_index % len(players)

        else:
            print("  ⚠ Invalid choice! Enter 'y' or 'n'.")

    print("\n" + "=" * 45)
    print("           🏆  GAME OVER — RESULTS  🏆")
    print("=" * 45)

play_game()
