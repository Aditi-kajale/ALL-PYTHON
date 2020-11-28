# an eg of a nested function

def outer_fn():
	msg = "Hello"
	def inner_fn():
		print("msg contains",msg)

	inner_fn()  # command to execute inner_fn

# global / main namespace
#inner_fn()  # error, inner_fn() not defined/found
outer_fn()  # call outer_fn() which in turn call/invoke inner_fn()

# Steps of execution by Python Interpreter
#1. main() is called
#2. outer_fn() is called
#3. msg is initialised to "Hello"
#4. inner() is called
