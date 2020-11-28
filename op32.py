# Write a high order function (decorator) to determine the no of times a function is called
# Attributes of fn object - setattr(), getattr(), delattr() and hasattr()
# We will define an attribute "count" for wrapper function & increment it when a function is
# called
def count_fn(func):
	def wrapper_fn(*args,**kwargs):
		wrapper_fn.count += 1
		func(*args,**kwargs)

	wrapper_fn.count = 0   # OR   setattr(wrapper_fn,"count",0)	
	return wrapper_fn

@count_fn
def fn1(*args,**kwargs):
	pass

@count_fn
def fn2(*args,**kwargs):
	#no = args[0]   # in case you want to read the no passed as an arg to fn2()
	pass

fn1()
fn2(120)
fn1()
fn1()

print("No of times fn1 is called is ",fn1.count) # 3
print("No of times fn2 is called is ",fn2.count) # 1
