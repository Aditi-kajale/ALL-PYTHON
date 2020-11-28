# an eg of Call By Value
def fn(str):
	str += "Sir"
	print("In fn(), str contains",str,"and it's adr in memory is",id(str)) #HelloSir, 1000

str = "Hello"
print("Before fn() in main(), str contains",str,"and it's adr in memory is",id(str)) #Hello, 1200
fn(str)
print("After fn() in main(), str contains",str,"and it's adr in memory is",id(str)) #Hello, 1200