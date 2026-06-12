import random

while True:

    cscore = 0
    hscore = 0

    print("\n" + "=" * 40)
    print("🎮 ROCK PAPER SCISSORS 🎮")
    print("First to 5 points wins!")
    print("=" * 40)

    while True:

        print(f"\n🏆 Score: You {hscore} - {cscore} Computer")

        user = int(
            input(
                "\nChoose:\n"
                "1. 🪨 Rock\n"
                "2. 📄 Paper\n"
                "3. ✂️ Scissors\n"
                "\nYour choice: "
            )
        )

        if user < 1 or user > 3:
            print("❌ Invalid choice!")
            continue

        com = random.randint(1, 3)

        print("\nRock...")
        print("Paper...")
        print("Scissors...")
        print("🔥 SHOOT! 🔥\n")

        if user == 1:
            print("You chose      : 🪨 Rock")
        elif user == 2:
            print("You chose      : 📄 Paper")
        else:
            print("You chose      : ✂️ Scissors")

        if com == 1:
            print("Computer chose : 🪨 Rock")
        elif com == 2:
            print("Computer chose : 📄 Paper")
        else:
            print("Computer chose : ✂️ Scissors")

        print()

        if user == 1 and com == 3:
            hscore += 1
            print("🎉 You won this round!")

        elif user == 2 and com == 1:
            hscore += 1
            print("🎉 You won this round!")

        elif user == 3 and com == 2:
            hscore += 1
            print("🎉 You won this round!")

        elif user == com:
            print("🤝 It's a draw!")

        else:
            cscore += 1
            print("💀 Computer won this round!")

        if hscore == 5:
            print("\n" + "=" * 40)
            print("🏅 CONGRATULATIONS!")
            print("🎉 YOU WON THE GAME!")
            print("=" * 40)
            break

        elif cscore == 5:
            print("\n" + "=" * 40)
            print("👿 GAME OVER!")
            print("💀 COMPUTER WON THE GAME!")
            print("=" * 40)
            break

    again = input("\n🔄 Play again? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thanks for playing!")
        break
