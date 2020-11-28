#An eg of an outer function which returns a reference of inner function
def outer_fn(msg):
	def inner_fn():
		print(msg)

	return inner_fn  # no brackets i.e. ( ) are missing after inner_fn, which means 
		# outer_fn is not executing inner_fn & returning the result but instead
		# returning a reference to inner_fn object

#main scope
my_func = outer_fn("Hello") # my_func object gets a reference to inner_fn object
			# this means any operation performed on my_func is
			# actually performed on inner_fn

my_func() # execute inner_fn
del outer_fn  # delete the outer_fn object
outer_fn("Hi")  # error, Name "outer_fn" not defined
my_func()  # OK, prints "Hello"

#Note - Here the inner_fn is also called as a "closure". A closure is a function object of a nested
#function that remembers the values in outer function even if the outer function is not in memory.
#These closure functions are used to write/create decorators.

	