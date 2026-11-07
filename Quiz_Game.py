Questions = (
    "What is 2+2?",
    "what is multiplication represented by?",
    "what does cow say?",
    "How many Alphabets are there in English?",
    "What is the 1st prime number?",
)
Options = (
    ("A. 4", "B. 5", "C. 6", "D. 7"),
    ("A. +", "B. -", "C. *", "D. /"),
    ("A. Moo", "B. Baah", "C. Neigh", "D. Roar"),
    ("A. 26", "B. 27", "C. 28", "D. 29"),
    ("A. 1", "B. 2", "C. 3", "D. 4"),
)
answers = ("A", "C", "A", "A", "B")
guesses = []
score = 0
Question_num = 0
for Question in Questions:
    print("-------------------------")
    print(Question)
    for option in Options[Question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[Question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[Question_num]} is the correct answer.")
    Question_num += 1
print("-------------------------")
print("RESULTS")
print(f"You scored {score} out of {len(Questions)}")
print(f"Your guesses: {guesses}")
print(f"Correct answers: {answers}")
