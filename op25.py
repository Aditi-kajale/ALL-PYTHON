# A decorator is a high order function i.e. a function which accepts another function as it's
#argument, adds some functionality to it & returns another function. All this without altering the
#source code of original / passed function. This is similar to packing a gift. The decorator 
#function acts like a wrapper. The nature of object that got decorated (i.e. actual gift inside)
#doesn't get altered. But now it's pretty, since it got decorated.
def make_pretty(func):
	def wrapper_fn():
		func()  # call the passed function to make_pretty()
		print("I got decorated")

	return wrapper_fn

#shortcut - i.e. to apply decorator to the gift() auto
@make_pretty
def gift():
	print("I am the gift")

#main scope
gift()  #OK, gift() is an independent function

#pretty_gift = make_pretty(gift) # pretty_gift will get the reference of wrapper_fn object
#pretty_gift()  # Will execute the wrapper fn


	