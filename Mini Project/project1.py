import random
import time  # Import time module for animation effect


def roll():
    min_value = 1
    max_value = 6

    # Dice rolling animation
    print("Rolling...", end="", flush=True)
    for _ in range(3):  # Show 3 rolling dots
        time.sleep(0.5)  # Delay for animation effect
        print(" 🎲", end="", flush=True)
    
    time.sleep(0.5)  # Short delay before showing the result
    roll = random.randint(min_value, max_value)
    
    print(f"\nYou rolled a {roll}!")  # Show result on a new line
    return roll


# Get the number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]
game_active = True  # Flag to track if the game is still running

def display_leaderboard():
    """Sort and display the leaderboard after every round."""
    sorted_scores = sorted(
        enumerate(player_scores, start=1), key=lambda x: x[1], reverse=True
    )
    print("\n🏆 Leaderboard 🏆")
    for rank, (player, score) in enumerate(sorted_scores, start=1):
        print(f"{rank}. Player {player} - {score} points")
    print("-" * 20)


while game_active and max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y) or quit (q)? ").lower()
            if should_roll == "q":
                game_active = False  # Stop the game
                break
            if should_roll != "y":
                break
            
            value = roll()  # Now uses the animated dice roll function
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

    if not game_active:
        break  # Exit the main game loop if someone quits

    display_leaderboard()  # Show leaderboard after each round

# Determine the winner (even if the game ends early)
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nGame over! Player number", winning_idx + 1, 
      "is the winner with a score of:", max_score)
