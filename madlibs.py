# This is a sample Python script.

'''
One of the best ideas to start experimenting you hands-on python projects for students
is working on Mad Libs Generator. This is the perfect project for beginners who are just
starting out with software development. Primarily focused on strings, variables, and
concatenation, this project will teach you how to manipulate user-inputted data.
The program design is such that it will ask users to enter a series of inputs that
will be considered as a Mad Lib. Mab lib is one of the python projects for beginners.
'''

print("Welcome to my first game !")

name = input("What is your name ? ").capitalize()
age = int(input("What is your age ? "))
print(f"Hello {name}, you are {age} years old ❤")

if age >= 18:

	print("You are old enough to play ...")
	ans = input("Do you want to play ? yes/no : ").lower()
	if ans == "yes":

		print("Let's Go 👏")
		print("I will try to guess the number I chose ;)")
		print("Just click enter to pass to the next process ...")
		print("Remember don't write the number, just memorize it in your mind .")
		print("Now let's go ...")
		print("Choose a number from 1 to 10, and press enter : ")
		input("Multiply by 2 ... press enter")
		input("Add to it the number 8 ... press enter")
		input("Divide the number by 2 ... press enter")
		input("Now the result you got Subtract from it the number you chose at the beginning ")
		print("I guess the number is 4 😋")
		print("Let's go again 💛")

	else:

		print("See you again ⏳")

else:

	print("Sorry you are not old enough to play :(")