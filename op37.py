# an eg of reduce()
# This function is not a part of core python built in functions
# It is a part of module functools
from functools import reduce

# eg - 1, calculate the sum of elements of a given list using reduce()
l = [-7,13,100,9,-34]

sum = reduce(lambda no1, no2 : no1 + no2,l)

print("Sum of nos from list l is",sum);

#eg - 2, determine the max element from a given list using reduce()
l = [-7,13,100,9,-34]
"""
def fn(no1,no2):
	if no1 > no2:
		return no1

	return no2

max = reduce(fn,l)
"""
max = reduce(lambda no1, no2 : no1 if no1 > no2 else no2,l)

print("max no is",max)

# eg - 3, determine the factorial value of any given no using reduce() - HW assignment

no = int(input("Enter the no of which factorial value is reqd :- "))

"""
 eg if no is 7, range(2,no+1) will generate series 2, 3, 4, 5, 6, 7 & 1st reduce() will multiply the
1st nos i.e. 2 & 3 to get result 6 which will again be used to multiply with next no in series i.e. 4,
and so on.... 
"""
fv = reduce(lambda x, y : x * y,range(2,no+1))

print("Factorial no is",fv)





