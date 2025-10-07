import os

print("Welcome to Rock Paper Scissors!")
print("First player to reach 3 points wins!")

options = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

player1_score = 0
player2_score = 0

while player1_score < 3 and player2_score < 3:
    print("\nOptions: 1. Rock   2. Paper   3. Scissors")

    pick1 = input("Enter Player 1's choice (1/2/3): ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    pick2 = input("Enter Player 2's choice (1/2/3): ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    # Validate input
    if pick1 not in options or pick2 not in options:
        print("Invalid input! Please enter 1, 2, or 3.")
        continue

    # If both choose same
    if pick1 == pick2:
        print("It's a tie! No points awarded.")
    else:
        # Determine winner
        if (pick1 == "1" and pick2 == "3") or \
           (pick1 == "2" and pick2 == "1") or \
           (pick1 == "3" and pick2 == "2"):
            print(f"Player 1 wins this round! ({options[pick1]} beats {options[pick2]})")
            player1_score += 1
        else:
            print(f"Player 2 wins this round! ({options[pick2]} beats {options[pick1]})")
            player2_score += 1

    print(f"\nScores: Player 1 = {player1_score} | Player 2 = {player2_score}")

# End game
print("\nGame Over!")
if player1_score == 3:
    print(" Player 1 wins the game! ")
else:
    print(" Player 2 wins the game! ")




