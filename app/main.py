from app.questions import get_random_question

def run_game():
    total_questions = 5
    score = 0

    print("Welcome to NFL Trivia!")

    for question_number in range(1, total_questions + 1):
        question = get_random_question()

        print(f"Question {question_number}: {question['question']}")

        for index in range(len(question["options"])):
            print(f"{index + 1}. {question['options'][index]}")

        user_input = input("Enter your answer (1–4): ")

        # protect against invalid inputs / used GPT to find isdigit()
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(question["options"]):
                selected = question["options"][choice - 1]
                if selected == question["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong. The correct answer was: {question['answer']}")
            else:
                print("Invalid input")
        else:
            print("Invalid input")

    print(f"Game over. You got {score} out of {total_questions} correct.")

if __name__ == "__main__":
    run_game()
