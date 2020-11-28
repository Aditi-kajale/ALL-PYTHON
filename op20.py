# In Python, a bare "*" in function arg list is used to force the caller (calling fn) to use keyword args
# for args following "*"
def locations(vil1,vil2,*,vil3,vil4):
	print("Village1 is",vil1)
	print("Village2 is",vil2)
	print("Village3 is",vil3)
	print("Village4 is",vil4)

#locations("Khed","Mulshi","Paud","Kamshet") # Error, vil3 & vil4 must be keyword args

locations("Khed","Mulshi",vil4="Paud",vil3="Kamshet") # in keyword arg, names of actual & formal
					# args must match


