# define a class "Shape" to manage 2D shapes & a method to calculate area of a shape
# define a class "Rectangle" which inherits "Shape" & display it's area
# define a class "Triangle" which inherits "Shape" & display it's area
# Note - Here as the implementation of calculating area for different shapes is different,
# the method to calculate area is abstract & hence the class "Shape" also becomes abstract
from abc import ABC, abstractmethod   # class & decorator method for defining abstract class

class Shape(ABC):
	def __init__(self,dim1,dim2):
		self.dim1 = dim1
		self.dim2 = dim2

	@abstractmethod   # will force the sub class to provide it's implementation
	def getarea(self):   # i.e. we need to override this method in sub class
		pass	# no implementation

class Rectangle(Shape):
	def __init__(self,dim1,dim2):
		super().__init__(dim1,dim2)

	# compulsory
	def getarea(self):
		return self.dim1 * self.dim2

class Triangle(Shape):
	def __init__(self,dim1,dim2):
		super().__init__(dim1,dim2)

	def getarea(self):
		return 0.5 * self.dim1 * self.dim2

r = Rectangle(20,10)
t = Triangle(13,5)

print("Area of rect r with l=20 and b=10 is",r.getarea())
print("Area of triangle t with b=13 and ht=5 is",t.getarea())

s = Shape(20,10)  # error, Shape is abstract cannot instantiate

#Note - If the inherited sub class is also to be made abstract, then do not override the
# abstract method of it's super class






