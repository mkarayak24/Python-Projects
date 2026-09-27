name = input("What is your name? ")
print(f"Hello, {name}! Let's start the adventure.")

answer = input("You are on a dirty road. Do you want to go left or right? (Type 'left' or 'right'): ").lower()

if answer == "left":
    answer = input("You encounter a river. Do you want to swim across or walk around? (Type 'swim' or 'walk'): ").lower()
    if answer == "swim":
        print("You tried to swim across but the current was too strong. You drowned. Game over.")
    elif answer == "walk":
        print("You walked around the river and safely crossed it. You win!")
    else:
        print("Invalid choice. Game over.")
elif answer == "right":
    answer = input("You encounter a bear. Do you want to run or play dead? (Type 'run' or 'play dead'): ").lower()
    if answer == "run":
        print("You ran away safely. You win!")
    elif answer == "play dead":
        print("The bear didn't notice you and you survived. You win!")
    else:
        print("Invalid choice. Game over.")
else:
    print("Invalid choice. Game over.")

print("Thank you for playing! Goodbye.")