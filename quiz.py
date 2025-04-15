import random

# Questions list
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "options": ["Charles Dickens", "Shakespeare", "J.K. Rowling", "Leo Tolstoy"],
        "answer": "Shakespeare"
    }
]

# Shuffle questions
random.shuffle(questions)

score = 0

# Ask questions
for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
        if q["options"][choice - 1].lower() == q["answer"].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    except:
        print("❌ Invalid input.")

# Final score
print("\n🎉 Quiz Finished!")
print(f"Your Score: {score}/{len(questions)}")
