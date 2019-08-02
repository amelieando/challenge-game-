#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

timer = 3
win = False
while timer > 0:

	guess = input("Guess a number between 1 and 20 (inclusive): ")
	# checks if a string is only digits 0 to 9
	if not guess.isnumeric():
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer

	if guess < aRandomNumber:
		print("number is too low")
		timer -= 1
	elif int(guess) > aRandomNumber:
		print("number is too high")
		timer -= 1
	elif int(guess) == aRandomNumber:
		print("number was correct " + str(aRandomNumber) + "!")
		win = True


	
