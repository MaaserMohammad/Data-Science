import random

player_score = 0
computer_score = 0

while True:

    input("Press Enter to roll the dice...")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("You rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        player_score += 1
        print("You win this round!")

    elif computer > player:
        computer_score += 1
        print("Computer wins this round!")

    else:
        print("It's a tie!")

    print(f"Score: You {player_score} - {computer_score} Computer")

    if player_score == 5:
        print("You won the game!")
        break

    elif computer_score == 5:
        print("Computer won the game!")
        break