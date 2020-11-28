# define an overloaded method without using a class definition & which returns the sum of
# 'n' nos or join 'n' strings
# Even without a class defn, python supports method overloading
def add(*args):   # var length argument to a method
	# check the type of argument
	if type(args[0]) == int:
		result = 0   # running total
	else:
		result = ""  # empty string

	# read the value of each argument
	for i in range(len(args)):
		result += args[i]   # if result is int, addition will take place
			     # if result is string, concantenation will take place

	return result



print("Addition of nos 10-60 is",add(10,20,30,40,50,60))  # nested function call
print("Concantenation of 3 strings is",add('i','like','python')) # 'i like python'
