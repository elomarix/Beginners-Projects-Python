'''
This is one of the simple python projects yet an exciting one.
You can even call it a mini-game. Make a program in which the
computer randomly chooses a number between 1 to 10, 1 to 100,
or any range. Then give users a hint to guess the number.
Every time the user guesses wrong, he gets another clue,
and his score gets reduced. The clue can be multiples,
divisible, greater or smaller, or a combination of all.
'''

from random import randint


def guess_num(n):

	print("Welcome !")
	g = randint(1,n)
	guess = int(input(f"Guess a number between 1 and {n} : "))
	while guess != g:
		if guess > g:
			print("Sorry guess again, too low.")
		elif guess < g:
			print("Sorry guess again, too high.")
		guess = int(input(f"Guess a number between 1 and {n} : "))
	print(f"Yay, cangrats. you have guessed the number {g} correctly 🎇")
	print("Play again ...")

guess_num(100)
