import random

while True:

    user = input("Wanna play the game? (yes/no): ").lower()

    if user != "yes":
        print("Okay, maybe next time. Goodbye lad!")
        break

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nI have selected a number for you to guess between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print(
                f"Congratulations! You've guessed the number {number} in {attempts} attempts!"
            )
            break

        print("Attempts left:", max_attempts - attempts)

    else:
        print(f"\nHaha! Game Over! The number was {number}")

    print("\nRound finished!\n")