# an eg of Call By Reference situation for immutable types
def fn(str):
	str += "Sir"
	return str  # imp

str = "Hello"
print("Before fn(), str is",str)  # Hello
str = fn(str) # assignment is as good as modification
print("After fn(), str is",str)  # HelloSir



