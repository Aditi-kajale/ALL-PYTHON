# An eg of keyword arguments
# Here the caller identifies the arguments by parameter name i.e. while calling the function, 
# parameter  name/arg name is passed along with the value
def info(name,age,salary):
	age += 1
	salary += salary * 0.1
	print("Next year,",name,"will be",age,"years old and will draw a salary of Rs.",salary)

info(salary=10000.50,name="Ajay",age=25)  # fn call is independent of position of args
# ensure that the name of argument is correct
#Mixed Call i.e. in function call, we can have both positional & keyword arguments
#However, note that the positional args cannot follow the keyword args, otherwise it leads to error
#info("Suresh",age=29,20000) # Syntax Error
info("Suresh",salary=20000,age=29) #OK, 1 positional & 2 keyword args
info("Paresh",30,salary=10000) # OK, 2 positional & 1 keyword args