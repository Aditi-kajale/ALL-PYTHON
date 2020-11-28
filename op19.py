# an eg of Mixed call of positional, keyword & variable length args to a function
# Note - positional args should preceed variable length args & keyword args should be trailing args
def locations(vil1,vil2,*metros,vil3,vil4):
	print("Village1 is",vil1)
	print("Village2 is",vil2)
	print("Village3 is",vil3)
	print("Village4 is",vil4)

	for city in metros:
		print(city,"is a metro city")

locations("Khed","Mulshi","Pune","Mumbai","Bangalore",vil3="Paud",vil4="Kamshet")

