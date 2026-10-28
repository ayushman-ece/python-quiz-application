from quiz_app import QUESTIONS, check_answer, calculate_percentage


def run_quiz():
    score = 0
    total = len(QUESTIONS)

    print("\n===== PYTHON QUIZ APPLICATION =====")
    print(f"Total questions: {total}")

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ")

        if check_answer(user_answer, question["answer"]):
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! Correct answer: {question['answer']}")

    percentage = calculate_percentage(score, total)

    print("\n===== QUIZ RESULTS =====")
    print(f"Your score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 50:
        print("Good effort! Keep practicing.")
    else:
        print("Keep learning. You can improve!")


if __name__ == "__main__":
    run_quiz()