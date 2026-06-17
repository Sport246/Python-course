import random

while True:
    user = input("Enter your choice; rock, paper or scissors: ")
    possible = ["rock", "paper", "scissors"]
    comp = random.choice(possible)
    print("You chose:", user, "computer chose", comp)

    if user == comp:
        print("Both players selected", comp,". So its a tie!")
    elif user == "rock":
        if comp == "scissors":
            print("Rock smashes scissors. Your win!")
        else:
            print("Paper covers rock. You lose!")
    elif user == "paper":
        if comp == "rock":
            print("Paper covers Rock. You win!")
        else:
            print("Scissors cuts Paper. You lose!")
    elif user == "scissors":
        if comp == "paper":
            print("Scissors cuts Paper. You win!")
        else:
            print("Rock smashes Scissors. You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break