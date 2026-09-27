import random

user_win_count = 0
computer_win_count = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Type Rock/Paper/Scissors) or Q to quit: ").lower()
    
    if user_choice == 'q':
        break
    
    if user_choice  not in options:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        continue

    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_win_count += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_win_count += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        user_win_count += 1
    else:
        print("You lost!")
        computer_win_count += 1

print(f"Your score: {user_win_count}, Computer score: {computer_win_count}")
print(f"Final score - You: {user_win_count}, Computer: {computer_win_count}")
print("Thanks for playing!")