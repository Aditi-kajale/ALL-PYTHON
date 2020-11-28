# define a class Point, create 2 points & find the distance between them
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.x) + ", " + str(self.y)

	# overload operator '-' (binary operator)
	def __sub__(self,other):
		distx = self.x - other.x
		disty = self.y - other.y
		dist = (distx ** 2 + disty ** 2) ** 0.5
		return dist  # return value here is a number

# main scope
p1 = Point(2,3)
p2 = Point(1,5)

print("Coords of p1 are",p1)
print("Coords of p2 are",p2)
print("Distance between p1 and p2 is",p1-p2) # unsupported operand type(s) for -: 'Point' and 'Point', Error only if operator '-' is not overloaded
print("Distance between p1 and p2 is",p1.__sub__(p2))  # OK but not preferred

