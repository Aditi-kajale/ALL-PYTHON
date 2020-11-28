# define a class "Rectangle" with attributes "length" & "breadth" & methods to assign & 
# calculate & return area of any given rectangle
class Rectangle:
	# do not declare attributes of object here like in CPP or Java. Attributes declared
	# here are treated as "class" / "static" vars
	# method to set the attributes
	def setDim(self,l,b):  # 1st arg should be "self" for instance methods
		self.length = l  # object which calls this method, it's length is set to l
		self.breadth = b  # length & breadth are attributes of object

	def getArea(self):
		return self.length * self.breadth


#main scope
# create objects of class Rectangle
r1 = Rectangle()
r2 = Rectangle()  # only 1 object can be created at a time

r1.setDim(20,10)  # r1 will have 2 attributes defined/created for itself i.e. length & breadth
print("Length & breadth of r1 are",r1.length,r1.breadth)  # python has no concept of access
			# specifiers like private, public, etc.

print("Area of r1 is",r1.getArea()) # "self" parameter is auto passed by r1 itself

#print("Length & breadth of r2 are",r2.length,r2.breadth)  # error, no such attributes "length"
				# and "breadth" for object r2

"""
Note - This means different objects can have different set of attributes i.e. python gives the developer to have different attributes for different objects with a common set of methods/functionalities.
However if you want create all objects with same set of attributes, then we need to define a special method in class called as "constructor"
"""






