math_quiz = [
    {
        "question": "What is 8 + 7 * 2?",
        "options": ["A) 30", "B) 22", "C) 16", "D) 25"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 144?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 14"],
        "answer": "C"
    },
    {
        "question": "Solve for x: 3x - 6 = 9",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "C"
    },
    {
        "question": "What is 15% of 200?",
        "options": ["A) 15", "B) 20", "C) 25", "D) 30"],
        "answer": "D"
    },
    {
        "question": "What is 2 to the power of 4 (2^4)?",
        "options": ["A) 8", "B) 12", "C) 16", "D) 32"],
        "answer": "C"
    }
]

score = 0
for question in math_quiz:
    print(question["question"])
    for option in question["options"]:
        print(option)
    ans = input("Select your answer\n").upper()
    if ans == question["answer"]:
        print("Correct")
        score +=1
    else:
        print("Wrong")
        
print(f"Game Over, your final score is {score}/5!")
