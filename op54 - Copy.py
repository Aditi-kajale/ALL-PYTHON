# Overload the '+' operator to add 2 Fraction objects, overload > operator to compare 2 fraction objects
# The + operator is overloaded only for predefined types like number, string, list, etc.
# not for user defined class object
class Fraction:

	def __init__(self,n,d):
		self.numer = n
		self.denom = d

	def __str__(self):
		return str(self.numer) + "/" + str(self.denom)

	# overload the binary operator '+' to add 2 fractions
	def __add__(self,other):
		numer = self.numer * other.denom + other.numer * self.denom
		denom = self.denom * other.denom
		return Fraction(numer,denom)  # create a new fraction object &
				# return it to f3 in main scope

	def __gt__(self,other):
		return self.numer/self.denom > other.numer/other.denom


f1 = Fraction(2,3)  # 0.67
print("f1 contains",f1)
f2 = Fraction(1,4) # 0.25
print("f2 contains",f2)
#f3 = f1.__add__(f2)  # OK but not preferred 
f3 = f1 + f2   # if the operator '+' is not overloaded for Fraction type, we get compile error
print("f3 contains",f3)
print("Is f1 > f2?",f1>f2) # if the operator '>' is not overloaded for Fraction type, we get compile error