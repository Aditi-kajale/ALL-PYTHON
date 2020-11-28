#unpacking the values from a tuple returned by a function
def fn():
	return 'abc',123,[10,20,30] # packing values in a tuple (CSV - comma separated values)

result = fn()
print("result contains",result)
print("type of result is",type(result)) # <class 'tuple'>

a,b,c = result  # unpacking the tuple back to values

print("a contains",a)
print("type of a is",type(a))

print("b contains",b)
print("type of b is",type(b))

print("c contains",c)
print("type of c is",type(c))

x, *y = result # To unpack a tuple if no of vars are not known
	# y becomes a list object

print("x contains",x)
print("type of x is",type(x))
print("y contains",y)
print("type of y is",type(y))


