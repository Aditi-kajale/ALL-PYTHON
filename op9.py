# an eg in which local & global variables have same names. How to resolve the conflict?
a = 10  # global var

def fn():
	a = 20 # new local var
	d = globals() # this built in function returns a dictionary object of all global vars
			# (keys) and their values
	d['a'] += 5 # for dictionary object, if we pass key, we get the value
	print("In fn(), local var a = ",a,"and global var a =",d['a']) #20, 15

fn()
print("In main(), global var a = ",a) #15
