# an eg of global variable

a = 10 # shared variable

def fn():
	print("In fn() / local scope, a = ",a) # accessible only

print("In main() / global scope, a = ",a)
fn()
