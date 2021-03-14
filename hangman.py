'''
This is more of a “guess the word” game. The core concepts you have to use while developing 
this project are variables, random, integer, strings, char, input and output, and boolean. 
In the game, users have to enter letter guesses, and each user will have a limited number 
of guesses (a counter variable is needed for limiting the guesses). This is one of the 
interesting python projects to begin with. 

Remember, you must create a file '.txt' in which to put the names to choose from

'''

import random

def paly():

    with open('wordlist.txt', 'r') as f:
      words = f.readlines()
    word = random.choice(words)[:-1]
    
    allowed_errors = len(word)
    guess = []
    done = False

    print("Welcome in my game 👏")
    print("Try to guess the word by entering the letters that make up this word.")
    print("Let's Go ...")

    while not done:

        for litter in word:
            if litter.lower() in guess:
                print(litter, end=' ')
            else:
                print('_', end=' ')
        print("")

        guesses = input(f"Allowed errors left {allowed_errors}. Next guess : ")
        while len(guesses) > 1 or guesses.isnumeric():
            print("Please enter one character 'A - Z' !")
            guesses = input(f"Allowed errors left {allowed_errors}. Next guess : ")
        guess.append(guesses.lower())
        if guesses.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                print(" ")
                break

        done = True
        for litter in word:
            if litter.lower() not in guess:
                done = False

    if done:
        print("\nSuper 🙂")
        print(f"Yay, Congrats. you found the word it was '{word}' .")

    else:
        print("\nSorry ☹")
        print(f"Game over! the word it was '{word}' !")

paly()
answer  = input("\nDo you want to play again? [y/n] > ").lower()
while answer == 'y':
    print("")
    paly()
    answer = input("\nDo you want to play again? [y/n] > ").lower()
if answer == 'n':
    print("\nThe programm will me closed...")
else:
    print("\ninvalid input !")
    print("The programm will me closed...")


