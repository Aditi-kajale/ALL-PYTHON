# An eg in which the function to be wrapped i.e. gift() has arguments/parameters
def make_pretty(func):  # gift fn object
	def wrapper_fn(gift1,gift2):
		func(gift1,gift2)  # calls gift()
		print("We got decorated")

	return wrapper_fn

#short cut
#@make_pretty
def gift(gift1,gift2):
	print("I am the",gift1)
	print("I am the",gift2)


#long cut
gift("doll","wrist watch")

pretty_gifts = make_pretty(gift)  # pretty_gifts is a reference to wrapper_fn object
#pretty_gifts()  # compile error, gift() has 2 positional args which are missing
pretty_gifts("doll","wrist watch")


#Note - The decorator function accepts a function as it's argument & if that function has any
#arguments/parameters, these parameters are to be specified to wrapper_fn