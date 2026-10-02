with open ("story.txt", "r") as f:
    story_template = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story_template):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story_template[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Please enter a {word}: ")
    answers[word] = answer

for word in words:
    story_template = story_template.replace(word, answers[word])

print("\nHere is your story:\n")
print(story_template)