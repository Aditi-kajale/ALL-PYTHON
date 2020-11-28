#Variable length arguments
# This feature is especially useful when we are not sure in advance as to how many arguments
# would be passed while calling the function. Such args are defined using * symbol
#define a function which returns the sum of "n" integers/floats

def sum(*nos): # type of nos is tuple
	#print("Type of nos is",type(nos))
	total = 0
	for i in range(len(nos)):
		total += nos[i]

	return total

print("Sum of 1st 5 natural nos is",sum(1,2,3,4,5))
print("Sum of 1st 10 natural nos is",sum(1,2,3,4,5,6,7,8,9,10))

# eg-2, print a greeting message for each person using a function
def greet(*names):
	for el in names: # here el refers to the value of element & not it's position as seen earlier
			#this loop is better known as "for each loop"
		print("Hello",el,", Welcome to Online Python Trg Prog")


greet("dhanesh","rohan","priya","aditi","dhanashri","pranjal")

		







