# user defined exceptions - It is possible to define our own exceptions by creating a
# new class which is derived from Base class "Exception". This is necessary bcoz
# for many user requirements, we may not have std exceptions. Hence the need
# for user defined exception. For eg suppose the username should be between 5-8
# characters only & alphanumeric, accept the age of a person to be insured betn
# 10-60 years only, ......
# The exception can be thrown for some condition using "raise" statement
# Validate the username for above conditions
class UserNameError(Exception):
	def __init__(self,msg):  # constructor
		self.msg = msg

	def __str__(self):  # string representation of object
		return self.msg

un = input("Enter username betn 5-8 chars only (without symbols) :- ")

try:
	if (len(un) < 5):
		raise UserNameError("Length of Username too less")

	if (len(un) > 8):
		raise UserNameError("Length of Username too large")

	if not un.isalnum():  # alnum means alpha numeric, boolean method
		raise UserNameError("Invalid char in Username")

except UserNameError as e:  # e is a reference to UserNameError object 
			# thrown @ runtime
		print(e.msg)  # only e will also do
else:
	print("Username is Valid")




	
	
		
		