#an eg of a function which returns multiple values
def fn():
	#return 'abc'
	#return 123
	#return [10,20,30]
	# this will not give error, but the return statements below the 1st ones will fail to execute
	#bcoz the 1st return will terminate the function
	return 'abc',123,[10,20,30] #returns a tuple of values (comma separated values)

result = fn()
print("result is",result)
print("type of result is",type(result)) # tuple
print(result[0])
print(type(result[0]))
print(result[1])
print(type(result[1]))
print(result[2])
print(type(result[2]))
