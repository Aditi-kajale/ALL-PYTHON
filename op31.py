# write a decorator function which calculates the running time of any given function
# For eg if we want to add a given no of fibonacci terms to a list
import time

def time_cost(func):  # decorator fn, pls revise op18 & op21 progs...
	def calc(*args,**kwargs):  # wrapper fn should always contain *args & **kwargs so
				# that we can pass any fn to decorator fn which will
				# have any no & type of args
		start_time = time.time()  # time() of time module (time.py) returns the
					# current time of system
		func(*args,**kwargs) # func is a generic name of fn to be called
		end_time = time.time()
		print("Total time taken by",func.__name__,"is",end_time-start_time)  #__name__ is a built in attribute which returns the name of calling object

	return calc

@time_cost  # apply the decorator to fibo()
def fibo(*args,**kwargs): # args is a tuple which supports indexing
	no_terms = args[0] # access only the reqd argument from *args & **kwargs
	curr_term = 0
	next_term = 1
	l = [ ]   # empty list
	for i in range(no_terms):
		l.append(curr_term)
		next_term = curr_term + next_term
		curr_term = next_term - curr_term

	print("1st",no_terms,"no of terms of fibo series are",l)

@time_cost
def pow_fn(*args,**kwargs): # kwargs is a dictionary. To get the 'value' from dict, supply the 'key'
	base = kwargs['b']
	no_terms = kwargs['n']
	pv = 1
	l = []
	for i in range(no_terms):  # i --> 0 1 2 3 4 5 6....... no_terms-1
		l.append(base ** i)

	print("PV of",base,"for",no_terms,"is",l)


no = int(input("Enter the no of terms reqd :- "))
fibo(no)
base = int(input("Enter the base no :- "))		
#pow_fn(base,no) # positional or reqd args
pow_fn(b=base,n=no)  # keyword args

