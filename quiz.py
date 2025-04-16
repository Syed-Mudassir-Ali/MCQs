# import random

# # Questions list
# questions = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["London", "Berlin", "Paris", "Madrid"],
#         "answer": "Paris"
#     },
#     {
#         "question": "Which language is used for web apps?",
#         "options": ["Python", "Java", "JavaScript", "C++"],
#         "answer": "JavaScript"
#     },
#     {
#         "question": "Who wrote Romeo and Juliet?",
#         "options": ["Charles Dickens", "Shakespeare", "J.K. Rowling", "Leo Tolstoy"],
#         "answer": "Shakespeare"
#     }
# ]

# # Shuffle questions
# random.shuffle(questions)

# score = 0

# # Ask questions
# for q in questions:
#     print("\n" + q["question"])
#     for i, option in enumerate(q["options"], 1):
#         print(f"{i}. {option}")
    
#     try:
#         choice = int(input("Enter your choice (1-4): "))
#         if q["options"][choice - 1].lower() == q["answer"].lower():
#             print("✅ Correct!")
#             score += 1
#         else:
#             print(f"❌ Wrong! Correct answer: {q['answer']}")
#     except:
#         print("❌ Invalid input.")

# # Final score
# print("\n🎉 Quiz Finished!")
# print(f"Your Score: {score}/{len(questions)}")


import streamlit as st
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

# Shuffle questions once and save in session state
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = []

st.title("🧠 Simple Quiz App")

# Current question
if st.session_state.current_q < len(st.session_state.shuffled_questions):
    q = st.session_state.shuffled_questions[st.session_state.current_q]
    st.subheader(f"Q{st.session_state.current_q + 1}: {q['question']}")

    user_answer = st.radio("Choose an option:", q["options"])

    if st.button("Submit"):
        correct = user_answer.lower() == q["answer"].lower()
        st.session_state.answers.append((q["question"], user_answer, q["answer"], correct))

        if correct:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")

        st.session_state.current_q += 1
        st.experimental_rerun()

else:
    st.header("🎉 Quiz Finished!")
    st.write(f"Your Score: **{st.session_state.score} / {len(questions)}**")

    with st.expander("Show Answers"):
        for idx, (ques, user_ans, correct_ans, correct) in enumerate(st.session_state.answers, 1):
            st.markdown(f"**Q{idx}: {ques}**")
            st.markdown(f"- Your answer: `{user_ans}`")
            st.markdown(f"- Correct answer: `{correct_ans}`")
            st.markdown(f"- Result: {'✅' if correct else '❌'}")
            st.write("---")

    if st.button("Restart Quiz"):
        del st.session_state.shuffled_questions
        del st.session_state.current_q
        del st.session_state.score
        del st.session_state.answers
        st.experimental_rerun()
