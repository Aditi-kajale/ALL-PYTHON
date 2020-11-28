# an eg of a function to modify a global variable
a = 10

def fn():
	#a *= 5  # error bcoz global vars are accessible but not modifiable by function code locally
	global a  #global keyword is not compulsory only if you want to access the global var
		# but to modify it, "global" keyword is essential
	a *= 5 # OK, assignments can be done
	print("Value of global var a after modification is",a) #50

print("Value of global var a before modification is",a) #10
fn()