import random
import string

def generate_password(min_lenght, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ''
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(password) < min_lenght:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return password

min_length = int(input("Enter the minimum length of the password: "))
has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
has_special = input("Include special characters? (y/n): ").lower() == 'y'
generated_password = generate_password(min_length, numbers=has_numbers, special_characters=has_special)

print("Generated Password:", generated_password)



 