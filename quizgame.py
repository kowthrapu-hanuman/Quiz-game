def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")
    print(f"\nYour final score: {score}/{len(questions)}")

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. London", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    }
]
if __name__ == "__main__":
    print("🎉 Welcome to the Quiz Game!")

    run_quiz(quiz_questions)
