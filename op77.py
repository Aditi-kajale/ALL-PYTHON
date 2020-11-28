# an eg of multiple catch blocks for a single try block
# This is reqd if you are expecting multiple exceptions during the course of
# executing some code. Here every catch block is inspected in order & the one
# which matches the exception raised, gets executed
try:
	# here we are evaluating an expression for which we expect
	# a no from user
	no = int(input("Enter a no > 3 :- "))
	if no >= 3:
		result = no / (no-3)

	print("Result of expression is",result)

except:    
	import sys
	print("Oops," , sys.exc_info()[0].__name__ ,"has occured")

print("Processing of main() continues......")

"""
except ValueError:
	print("Enter the no in figs only")

except ZeroDivisionError:
	print("Division by Zero not possible")

except NameError:
	print("Var 'result' not found")
"""

# except : will catch all exceptions, To know the exception information, use
# the exc_info() method as it will tell you the actual cause of error. This method
# returns multiple values in the form "tuple" of which the element @
# pos 0 describes the actual exception type
# The dunder attribute __name__ returns the name of class (error) from
# canonical name i.e. <class 'NameError'>		
