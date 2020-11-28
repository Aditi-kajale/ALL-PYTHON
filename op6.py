# an eg of local variable

def fn():
	a = 10  # local var, accessible only to code of this function
	print("In fn() i.e. local scope, a =",a)

# main / global namespace/scope
fn()
#print("In main() i.e. global scope, a =",a) # error, var a not found/defined
