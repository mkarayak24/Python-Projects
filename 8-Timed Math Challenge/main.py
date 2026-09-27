import random
import time

OPERATORS  = ['+', '-', '*']
MIN_OPERAND = 1
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def generate_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    question = f"{left} {operator} {right}"
    answer = eval(question)
    return question, answer

wrong_answers = 0
print("Welcome to the Timed Math Challenge!")
print(f"You will be asked {TOTAL_QUESTIONS} questions. Try to answer them as quickly as possible.")
print("Let's begin!")
input("Press Enter to start the challenge...")
print("---------------------------------------")

start_time = time.time()
for i in range(TOTAL_QUESTIONS):
    question, answer = generate_question()
    while True:
        guess = input(f"Question {i + 1}: {question} = ")
        if guess == str(answer):
            print("Correct!")
            break
        wrong_answers += 1
    
end_time = time.time()

print("---------------------------------------")
print("Challenge completed!")

print(f"Time taken: {end_time - start_time:.2f} seconds")
print(f"Wrong answers: {wrong_answers}")