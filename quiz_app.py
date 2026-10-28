QUESTIONS = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which loop repeats while a condition is true?",
        "options": ["A. if", "B. else", "C. while", "D. break"],
        "answer": "C"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["A. append()", "B. add()", "C. insert_end()", "D. attach()"],
        "answer": "A"
    }
]


def check_answer(user_answer, correct_answer):
    return user_answer.strip().upper() == correct_answer


def calculate_percentage(score, total):
    if total == 0:
        return 0
    return (score / total) * 100