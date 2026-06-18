def quiz_game():
    questions = {
        "What is the capital of France?": ["Paris", "London", "Berlin", "Rome"],
        "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Venus"],
        "Who wrote 'Hamlet'?": ["Shakespeare", "Dickens", "Tolstoy", "Homer"]
    }

    answers = ["Paris", "Mars", "Shakespeare"]
    score = 0

    for i, (question, options) in enumerate(questions.items()):
        print(f"\nQ{i+1}: {question}")
        for j, option in enumerate(options):
            print(f"{j+1}. {option}")

        choice = input("Your answer (1-4): ")
        if options[int(choice)-1] == answers[i]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print(f"\nYour final score: {score}/{len(questions)}")

quiz_game()