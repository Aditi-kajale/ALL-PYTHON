# an eg in which the function has to accept "n" var length args & also "m" keyword var length
# args (Mixed call)
def fn(*args,**kwargs):   # args & kwargs are not keywords but by convention, developers refer
		     # to var length args (positional) using the name "args" & keyword var
		     # length args by the name "kwargs"
	#display data of each on different lines
	print("type of args is",type(args))  #tuple
	print("Data of args is")
	#for i in range(len(args)):
	#	print(args[i])  # use indexing to fetch each element of a tuple

	for el in args:   # for each element in args, display the element
		print(el)

	print("type of kwargs is",type(kwargs)) #dict
	print("Data of kwargs is")
	for key in kwargs:   # for each key in dict kwargs
		print(key," - ",kwargs[key])  #pass key to dict name to fetch value

#imp, while calling the function, positional args should preceed the keyword args
#fn()  # the advantage of * & ** syntax is the args to fn are not compulsory (offers flexibility for
	# calling functions)

#fn("paresh","joshi",27,30000.45)  # OK, keyword args are missing
fn("paresh","joshi",27,30000.45,gender="M",marital_status="Unmarried")


