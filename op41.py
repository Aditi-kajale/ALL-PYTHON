# prog to demonstrate difference between a normal & generator fn
def reg_fn():
	return "only call"
	return "another call"  # This statement will not be read by compiler
			# Other prog langs give error "Unreachable Statement"
			# Unfortunately Python doesn't give error but will ignore all
			# code after 1st return statement

def gen_fn():
	yield "First call"
	yield "Second call"
	yield "Third call"

print("On 1st call reg_fn",reg_fn())  # only call
print("On 2nd call reg_fn",reg_fn())  # only call
print("On 3rd call reg_fn",reg_fn())  # only call


g = gen_fn() # returns an object of type generator
print("g contains",g)
print("On 1st call of gen_fn",next(g)) # First call
print("On 2nd call of gen_fn",next(g)) # Second call
print("On 3rd call of gen_fn",next(g)) # Third call


