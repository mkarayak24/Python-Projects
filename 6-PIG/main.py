import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players<= 4:
            break
        else:
            print("Invalid input. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

print(f"Starting a game with {players} players.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print(f"\nPlayer {i + 1}'s turn: \n")
        print(f"Current score: {player_scores[i]} \n")
        current_score = 0
        while True:
            should_continue = input("Do you want to roll the dice? (y/n): ")
            if should_continue.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is over and you lose your points for this round.")
                current_score = 0
                break
            else:
                print(f"You rolled a {value}.")
                current_score += value
            
            print(f"Your score is {current_score}.")

        player_scores[i] += current_score
        print(f"Player {i + 1}'s total score is now {player_scores[i]}.")

max_score_player = player_scores.index(max(player_scores)) + 1
print(f"\nPlayer {max_score_player} wins with a score of {player_scores[max_score_player - 1]}!")