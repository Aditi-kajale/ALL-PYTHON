# an eg of chaining of decorators i.e. applying multiple decorators to a given function
def decor1(func):
	def wrapper_fn1():
		print("$$$$$$$$$$$$$$$$$$$$")
		func()
		print("$$$$$$$$$$$$$$$$$$$$")

	return wrapper_fn1


def decor2(func):
	def wrapper_fn2():
		print("###################")
		func()
		print("###################")

	return wrapper_fn2



def msg_fn1():
	print("Databyte Computers")


"""
def msg_fn2():
	print("Online Python Batch")
"""
# long cut
d1 = decor1(msg_fn1) # d1 is nothing but a reference to wrapper fn1 waiting to be executed
d2 = decor2(d1) # d2 is nothing but a reference to wrapper fn2 waiting to be executed
d2() # executes wrapper fn2



