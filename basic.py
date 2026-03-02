import random

option = ("rock","paper","scissor")
running = True

while running:

    computer = random.choice(option)
    player_value = input("choose the value: ").lower().strip()

    while  player_value not in option:
        print(f"the {player_value} is not valid. ")
        player_value = input("choose the value: ").lower().strip()

    if player_value == computer:
        print("tie! ")
    elif player_value == "rock" and computer == "scissor":
        print("you win ")
    elif player_value == "paper" and computer == "rock":
        print("you win ")
    elif player_value == "scissor" and computer == "paper":
        print("you win ")
    else:
        print("computer win! ")

    play_again = input("play again? (y/n): ")
    if play_again == "y":
        running = False

print("thanks for playing ")








