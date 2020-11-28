# an eg of positional/required args - These are the arguments which have to be passed to the
# function in correct positional order
def info(name,age,salary):
	age += 1
	salary += salary * 0.1  # salary incremented by 10%
	print("Next year,",name,"is",age,"years old and draws a salary of Rs.",salary)

#info()  # error, missing 3 positional args
#info(25,"Ajay",10000.55) # error bcoz args are not in correct order
info("Ajay",25,10000.55)
