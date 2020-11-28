# WAP which displays the no of times a function is called
def fn():
	print("No of times the fn() is called is",fn.cntr)  # this is same as getattr(fn,"cntr")
	fn.cntr += 1  # to access an attribute of function object from itself, syntax is
		    # fnname.attribute

fn.cntr = 1  # same as setattr(fn,"cntr",1)
for i in range(10):
	fn()
# same as
#fn()
#fn()
#fn()...... calling 10 times

