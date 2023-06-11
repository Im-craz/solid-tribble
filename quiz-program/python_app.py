quiz = {
    "question_one": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question_two": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question_three": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question_four": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question_five": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question_six": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question_seven": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Ansuer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct\n")
        score += 1
        print(f'Your score is: {score}')
        print("\n")
    else:
        print("Wrong!\n")
        print(f"The answer is: {value['answer']}")
        print(f'Your score is: {score}')
        print("\n")


print(f'You got {score} out of 7 questions correctly')
print(f'Your percentage is {int(score / 7 * 100)}%')
