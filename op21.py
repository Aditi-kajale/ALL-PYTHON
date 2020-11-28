#an eg of keyword variable length args to a function
def fn(**data):  # the data is not accepted in the form of tuple as in case of 1 '*' but it is accepted
	       # in the form of a dictionary (collection of key/value pairs)
	print(data)
	print("type of data is",type(data))

fn(name="sunil",surname="vaidya",age=30,ms="unmarried",salary=35000.45)  # "n" keyword args





	