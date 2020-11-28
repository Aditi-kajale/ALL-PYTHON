# write a simple game to accept a no from user between 0-99 & predict
# or guess the no. which our program has assumed. Display after how
# much attempts, the user gets it right
import random   # random is a standard module

guess_no = random.randint(0,99)
# print("Guess no is",guess_no)
no_attempts = 0
user_no = -1

while user_no != guess_no:
	user_no = int(input("Enter the no (0-99) type -ve no to quit "))
	if user_no < 0:
		print("It seems you have given up!")
		break
	elif user_no > guess_no:
		print("Your no > no to guess")
	elif user_no < guess_no:
		print("Your no < no to guess")

	no_attempts += 1
else:
	print("Congrats, you guessed the no right after",no_attempts,"attempts")



