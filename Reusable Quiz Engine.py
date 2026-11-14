
score = 0

def display_question(question):
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i + 1}. {option}")

def validate_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_answer(question, answer):
    if answer == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is: {question['options'][question['answer'] - 1]}")

def update_score():
    global score
    score += 1

def display_score():
    print(f"Your final score is: {score}")

def run_quiz(questions):
    for question in questions:
        display_question(question)
        answer = validate_answer()
        check_answer(question, answer)

        if answer == question['answer']:
            update_score()

    display_score()

def five_questions():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 3
        },
        {
            "question": "What is the sum of 2 + 2 ? ",
            "options": ["3", "4", "5", "6"],
            "answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 4
        },
        {
            "question": "which river is the longest in the world ?",
            "options": ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"],
            "answer": 1
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "NaCl"],
            "answer": 2
        }
    ]
    run_quiz(questions)
five_questions()
