# we can use optional "else" clause in exception handlin along with try...catch
# the code in else block is executed only if try block doesn't raise an exception
try:
	# accept name & age from user and display his age next year
	name = input("Enter your name :- ")
	age = int(input("Enter your age :- "))
	# protected code, checks for any additional exceptions
	print("Dear",name,", next year your age will be",age+1)

except ValueError:
	print("Pls enter your age in figs only")
#else:
#	unprotected code, no checks for exceptions	
#	print("Dear",name,", next year your age will be",age+1)

