# an eg of a wrapper fn which can accept "n" args
def make_pretty(func):
	def wrapper(*gifts,**kwgifts): #1st is var length arg accepted as a tuple
				#2nd is var length key word arg accepted as a dict obj 
		func(*gifts,**kwgifts)
		print("We all got decorated")

	return wrapper

#@make_pretty   # short cut to apply a decorator
def gift(*gifts,**kwgifts):
	for el in gifts:
		print("I am",el)

	for key in kwgifts:  # for each key in the dictionary
		print("I am",kwgifts[key])  #for each value corresponding to a key


#gift("doll","perfume","pen drive")
#long cut
prettier_gifts = make_pretty(gift) 
#prettier_gifts() # we can pass 0 to n no of args
prettier_gifts("doll","perfume","pen drive",g1="puzzle",g2="spellofun")