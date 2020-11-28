# using constructor to declare & initialise the attributes of an object
# define a class "Fraction" with suitable attributes & a method to display the fraction object
# and also a method to evaluate it
class Fraction:
	# constructor
	def __init__(self,n,d):
		self.numer = n
		self.denom = d
		print("A new fraction object with numer =",self.numer,"and denom = ",self.denom,"created")

	def display(self):
		print("Fraction object is",self.numer,"/",self.denom)

	def eval(self):
		return self.numer / self.denom

#main scope
f1 = Fraction(5,2)   # self initialised but we can accept numer & denom from user also
f1.display()  # to confirm whether the attributes numer & denom are initialised or not
print("Evaluation of f1 is",f1.eval())  # 2.5

#f2 = Fraction() # error, __init__ () missing 2 reqd positional args 'n' & 'd'
		# This ensures that all fraction objects will have same attributes i.e.
		# numer & denom and not like class Rectangle

print("f1 contains",f1) # It will display the address of Fraction object "f1" in memory
# for built in types, when we display the object name, we get it's contents
no = 1234
msg = 'i like python'
print('no contains',no)
print('msg contains',msg)


	
