# Application - 2 of decorator fn
# Write a decorator fn to check whether all the args passed to a function are numbers only
def chk_data(func):    # decorator function
	def validate(*args):  # wrapper function
		flag = True   # boolean var
		for el in args:
			if type(el) != int and type(el) != float:
				flag = False  # found invalid arg for the function
				print("arg",el,"is not a number")

		#outcome of loop is success (flag remains True)/failure (flag is False)
		if not flag:   # rejection is handled first
			return "Sum cannot be determined"

		return "Sum of given nos is " + str(func(*args)) # returns the result of evaluation of add_fn() to main()

	return validate 	

@chk_data
def add_fn(*args):   # args is a tuple with numeric args only
	sum = 0
	for no in args:
		sum += no

	return sum

print(add_fn(1,'2',3,4,'d'))
print(add_fn(1,2,3,-4.15))

