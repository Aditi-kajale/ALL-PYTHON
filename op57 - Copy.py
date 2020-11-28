# application of a class var
# WAP to display the no of instances created from class Circle
class Circle:
	count = 0  # shared vars bcoz they can accessed from every object

	def __init__(self,r):
		self.r = r
		print("Circle of radius",r,"created")
		Circle.count += 1  # class vars are referred using class name


# main scope
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(15)
print("No of circles created are",Circle.count) # 3


