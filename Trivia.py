import random

def generate_question():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
        # Add more questions as needed
    ]
    return random.choice(questions)

def main():
    print("Welcome to the Trivia Game!\n")

    question_data = generate_question()
    question = question_data["question"]
    correct_answer = question_data["answer"]

    print(question)
    user_answer = input("Your Answer: ")

    if user_answer.lower() == correct_answer.lower():
        print("\nCongratulations! Your answer is correct.")
    else:
        print(f"\nOops! The correct answer is: {correct_answer}")

if __name__ == "__main__":
    main()
