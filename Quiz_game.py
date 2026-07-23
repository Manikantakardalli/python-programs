questions = {
    "Which language is known as the King of Programming?": "C",
    "Which keyword is used to define a function in Python?": "def",
    "What is the extension of Python files?": ".py",
    "Which data type stores True or False?": "bool",
    "Which symbol is used for comments in Python?": "#"
}

score = 0

print("===== PYTHON QUIZ GAME =====")

for question in questions:
    print("\n" + question)
    answer = input("Your Answer: ")

    if answer.lower() == questions[question].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", questions[question])

print("\n===== RESULT =====")
print("Total Questions :", len(questions))
print("Correct Answers :", score)
print("Wrong Answers   :", len(questions) - score)

percentage = (score / len(questions)) * 100
print("Percentage      :", percentage, "%")

if percentage >= 50:
    print("Result : PASS")
else:
    print("Result : FAIL")