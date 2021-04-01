import random

print("Welcome to my game 👋")
print("We'll play rock 'r', paper 'p', and scissors 's' ...")


def play():

    choices = ["r", "p", "s"]
    score_player = 0
    score_computer = 0

    while score_player < 3 and score_computer < 3:

        computer = random.choice(choices)
        user = None

        user = input("\nWhat's your  choice 'r' or 'p' or 's' : ").lower()

        while user not in choices:
            user = input("Check your choice 'r' or 'p' or 's' : ").lower()
        print()
        if user == computer:

            print(f"Your chose {user} and computer chose {computer} so Tie!")

        elif user == "r":

            if computer == "s":
                print(f"Your chose {user} and computer chose {computer} so you Win !")
                score_player += 1
            elif computer == "p":
                print(f"Your chose {user} and computer chose {computer} so you Lose !")
                score_computer += 1

        elif user == "p":

            if computer == "s":
                print(f"Your chose {user} and computer chose {computer} so you Lose !")
                score_computer += 1
            elif computer == "r":
                print(f"Your chose {user} and computer chose {computer} so you Win !")
                score_player += 1

        elif user == "s":

            if computer == "r":
                print(f"Your chose {user} and computer chose {computer} so you Lose !")
                score_computer += 1
            elif computer == "p":
                print(f"Your chose {user} and computer chose {computer} so you Win !")
                score_player += 1

        print("\nScore is ")
        print(f"Comoputer : {score_computer}")
        print(f"User : {score_player}")

    print()
    if score_player == 3:
        print("congrats you win for total ... 🙂")
    else:
        print("sorry computer has won for total ... ☹")


answer = input("Want to play [y/n] : ").lower()
if answer == "y":
    while answer == "y":
        play()
        answer = input("\nWant to play again [y/n] : ").lower()

print("See you later 👋")


