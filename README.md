# 🧠 Python Quiz Application

A beginner-friendly Python command-line quiz application that tests Python knowledge using multiple-choice questions, checks answers, and calculates the final score.

This project uses **Python dictionaries, lists, functions, loops, conditional statements, and modular programming** to build an interactive quiz.

This project is part of my **Python → Data Science → Machine Learning → AI** learning journey.

---

## 🚀 Project Overview

The Python Quiz Application presents a set of multiple-choice questions to the user.

For each question, the application:

- Displays the question and its options.
- Accepts the user's answer.
- Checks whether the answer is correct.
- Displays feedback.
- Updates the score when the answer is correct.

After all questions have been answered, the application calculates the final score and percentage and displays a performance message.

### Application Workflow

```text
Start Application
       ↓
Load Quiz Questions
       ↓
Display Question
       ↓
Show Multiple-Choice Options
       ↓
Accept User Answer
       ↓
Normalize Answer
       ↓
Check Correctness
       ↓
Update Score
       ↓
Repeat Until All Questions Finish
       ↓
Calculate Percentage
       ↓
Display Final Results
       ↓
End Application
```

---

## 🎯 Objective

The main objective of this project is to strengthen Python programming fundamentals by developing a functional quiz application.

The project demonstrates:

- Storing structured information using dictionaries
- Managing multiple questions using lists
- Defining reusable functions
- Iterating through questions using loops
- Accepting and processing user input
- Comparing answers using conditional statements
- Tracking scores using variables
- Calculating percentages
- Organizing code into separate modules

---

## 🧠 Python Concepts Used

### 1. Dictionaries

Each question is stored as a dictionary containing the question, options, and correct answer.

Example:

```python
question = {
    "question": "What is the capital of India?",
    "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    "answer": "B"
}
```

Dictionaries store information as key-value pairs.

In this project:

- `question` stores the question text.
- `options` stores the available answers.
- `answer` stores the correct option.

This keeps related information together and makes it easier to access.

### 2. Lists

The application stores multiple question dictionaries inside a list.

```python
QUESTIONS = [
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]
```

Lists allow the application to manage and iterate through multiple questions.

### 3. Functions

Functions divide the application into reusable tasks.

The project includes:

```python
def check_answer(user_answer, correct_answer):
    return user_answer.strip().upper() == correct_answer
```

The answer-checking function returns `True` when the normalized answer matches the correct answer and `False` otherwise.

### 4. String Methods

The application uses:

```python
user_answer.strip().upper()
```

- `strip()` removes leading and trailing whitespace.
- `upper()` converts letters to uppercase.

Therefore, answers such as `b`, `B`, and ` B ` can be checked consistently.

### 5. Loops

The application uses a `for` loop to process questions one by one.

```python
for number, question in enumerate(QUESTIONS, start=1):
    print(f"Question {number}: {question['question']}")
```

`enumerate()` provides both the question number and the question itself.

### 6. Conditional Statements

The application uses `if` and `else` to determine whether an answer is correct.

```python
if check_answer(user_answer, question["answer"]):
    score += 1
else:
    print("Wrong answer!")
```

The score increases only when the answer is correct.

### 7. Score Calculation

The application calculates the percentage using:

```python
def calculate_percentage(score, total):
    if total == 0:
        return 0
    return (score / total) * 100
```

This function also avoids division by zero if the total number of questions is zero.

---

## 🧮 Scoring System

The application starts with a score of zero.

For every correct answer, the score increases by one.

The final percentage is calculated using:

```text
Percentage = (Correct Answers / Total Questions) × 100
```

The current application displays performance messages according to these thresholds:

| Percentage | Message |
|---|---|
| 80% or higher | Excellent work! |
| 50% to below 80% | Good effort! Keep practicing. |
| Below 50% | Keep learning. You can improve! |

These messages provide simple feedback based on the final score.

---

## 📊 Example Output

The following is an example of the application running in a terminal.

```text
===== PYTHON QUIZ APPLICATION =====
Total questions: 5

Question 1: What is the capital of India?
A. Mumbai
B. Delhi
C. Kolkata
D. Chennai
Your answer (A/B/C/D): b
Correct! 🎉
```

After all questions have been answered, the application displays the final results.

```text
===== QUIZ RESULTS =====
Your score: 4/5
Percentage: 80.00%
Excellent work!
```

The actual score depends on the user's answers.

---

## 🗂️ Project Structure

```text
python-quiz-application/
│
├── main.py
├── quiz_app.py
├── .gitignore
└── README.md
```

### `main.py`

Responsible for:

- Starting the quiz
- Displaying questions and options
- Accepting user input
- Displaying feedback
- Tracking the score
- Calculating the final percentage
- Displaying the final results

### `quiz_app.py`

Contains the quiz data and reusable application logic:

- Storing quiz questions
- Checking answers
- Calculating percentages

### `.gitignore`

Specifies generated files and directories that Git should ignore, including Python cache files and virtual environments.

### `README.md`

Documents the project, its features, setup instructions, examples, and learning outcomes.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-quiz-application.git
```

### 2. Open the project directory

```bash
cd python-quiz-application
```

### 3. Check Python installation

```bash
python --version
```

Python 3.10 or newer is recommended.

No external Python packages are required for the current implementation.

---

## ▶️ Run the Project

Run the application using:

```bash
python main.py
```

The quiz starts in the terminal and displays the questions.

Enter your answer using `A`, `B`, `C`, or `D`.

The application accepts lowercase answers and ignores leading or trailing spaces.

After the last question, the application displays your final score and percentage.

---

## 🧰 Technologies Used

- **Python** — Core programming language
- **Dictionaries** — Store structured question data
- **Lists** — Organize multiple questions
- **Functions** — Reusable application logic
- **Loops** — Process questions
- **Conditional Statements** — Check answers and determine feedback
- **String Methods** — Normalize user input
- **Command-Line Interface** — User interaction

---

## 📦 Requirements

The project uses Python's built-in functionality and requires no third-party libraries.

```text
Python >= 3.10
```

---

## 📚 What I Learned

Through this project, I practiced:

1. Creating and accessing dictionaries
2. Storing multiple records inside a list
3. Defining and calling functions
4. Using loops to process questions
5. Using `enumerate()` to track question numbers
6. Normalizing user input with `strip()` and `upper()`
7. Comparing user answers with correct answers
8. Updating a score using conditional statements
9. Calculating percentages
10. Separating application logic into modules
11. Running and testing a Python command-line application

---

## 🔄 Learning Journey

This project is part of my ongoing Python project portfolio.

The broader learning journey includes:

### Python Fundamentals

```text
Variables and Data Types
        ↓
Conditions and Loops
        ↓
Functions
        ↓
Lists and Dictionaries
        ↓
File Handling
        ↓
Modular Programming
```

### Long-Term Roadmap

```text
Python
   ↓
Data Analysis
   ↓
Data Science
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
LLMs
   ↓
RAG
   ↓
Agentic AI
```

The goal is to build practical projects while understanding the concepts behind them step by step.

---

## ⚠️ Limitations

This project is designed for learning Python fundamentals.

Current limitations include:

- The quiz questions are predefined in the source code.
- The application uses a command-line interface.
- There is no database or persistent score history.
- There are no user accounts or leaderboards.
- Invalid answers are not repeatedly requested until valid input is entered.
- Questions cannot currently be added through the application itself.

---

## 🔮 Future Improvements

Possible improvements include:

- Add more Python questions and difficulty levels
- Randomize question order
- Add a timer for each question
- Validate answers and allow retries
- Store questions in a JSON file
- Save quiz results to a CSV file
- Track scores across multiple attempts
- Add categories such as Python, DSA, and Machine Learning
- Add negative marking and custom scoring
- Build a graphical interface using Tkinter
- Build a web-based quiz using Streamlit

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [https://github.com/ayushman-ece](https://github.com/ayushman-ece)

---

## 🛣️ My Goal

My goal is to improve my programming skills by building projects consistently, strengthening problem-solving abilities, and progressing from Python fundamentals toward Data Science, Machine Learning, and AI.

**One project at a time. One concept at a time. 🚀**