# an eg of a wrapper fn which can accept "n" args
def make_pretty(func):
	def wrapper(*gifts):  # gifts is nothing but a tuple of args passed by main() to
				# wrapper fn
		func(*gifts)
		print("We all got decorated")

	return wrapper

#@make_pretty   # short cut to apply a decorator
def gift(*gifts):
	for el in gifts:
		print("I am",el)


#gift("doll","perfume","pen drive")
#long cut
prettier_gifts = make_pretty(gift) # returns a reference to wrapper fn
prettier_gifts("doll","perfume","pen drive") # flexible, pass any no of gifts as we have used var
				# length args in wrapper fn

