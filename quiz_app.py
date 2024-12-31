# -*- coding: utf-8 -*-
"""quiz_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KWdndJcLBy5poK3b8Vv1Whlyc_mWdZHZ
"""

import json
import os

# File to store questions and high scores
DATA_FILE = "quiz_data.json"

# Initialize data file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"questions": [], "high_scores": []}, file)


def load_data():
    """Load quiz data from the file."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Save quiz data to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_question():
    """Add a new question to the quiz."""
    question = input("Enter the question: ").strip()
    options = []
    for i in range(4):
        option = input(f"Enter option {i + 1}: ").strip()
        options.append(option)
    correct_index = int(input("Enter the correct option number (1-4): ").strip()) - 1

    data = load_data()
    data["questions"].append({"question": question, "options": options, "correct": correct_index})
    save_data(data)
    print("Question added successfully!")


def play_quiz():
    """Play the quiz."""
    data = load_data()
    questions = data["questions"]

    if not questions:
        print("No questions available. Please add some first.")
        return

    print("\n--- Quiz Time! ---")
    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"{j}. {option}")
        answer = int(input("Your answer (1-4): ").strip()) - 1

        if answer == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['options'][q['correct']]}")

    print(f"\nYour total score: {score}/{len(questions)}")

    # Save the score
    data["high_scores"].append(score)
    save_data(data)


def view_high_scores():
    """View high scores."""
    data = load_data()
    high_scores = data["high_scores"]

    if not high_scores:
        print("No high scores yet.")
        return

    print("\n--- High Scores ---")
    for i, score in enumerate(sorted(high_scores, reverse=True), start=1):
        print(f"{i}. {score}")


def main():
    """Main function to run the quiz app."""
    while True:
        print("\nQuiz App Menu")
        print("1. Add a Question")
        print("2. Play Quiz")
        print("3. View High Scores")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_question()
        elif choice == "2":
            play_quiz()
        elif choice == "3":
            view_high_scores()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()