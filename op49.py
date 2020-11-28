# A python prog which displays the contents of a user defined class object, simply by using
# it's name i.e. no need to use display()
class Fraction:

	def __init__(self,n,d):
		self.numer = n
		self.denom = d

	# just like __init__(), we have another special method __str__() which is
	# used for string representation of any object
	def __str__(self):
		return str(self.numer) + "/" + str(self.denom)  # imp all parameters are
				# to be of string type only. + means join operator

f = Fraction(5,2)
print("f contains",f)  # f contains 5/2

# __init__() & __str__() are also called as magical/dunder methods (double underscore 
# methods) bcoz they are built in methods & are called at certain times only. The __ is
# used so that the method names do not conflict with user defined methods in a class defn.


