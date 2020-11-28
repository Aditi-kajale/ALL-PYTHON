# an eg of both constructor & destructor
class Point:
	# constructor
	def __init__(self,x=0,y=0):   # If coords for a point are not specified, then the
				# default coordinates are 0,0
		self.x = x
		self.y = y
		print("A new Point object is created")

	# string representation for Point obj
	def __str__(self):
		return str(self.x) + ", " + str(self.y)

	# destructor
	def __del__(self):
		print("All objects of class Point with same reference destroyed")

#main scope
p1 = Point()  # default coords of 0, 0 assigned
print("Coords of p1 are",p1)
p2 = p1  # here constructor is not called bcoz no new memory is allocated. Internally the
	# __init__() calls __new__() which actually allocates memory & constructor is
	# used only to initialise the attributes of object
print("Adr of p1 is",id(p1),"and of p2 is",id(p2)) # same

p3 = Point(250,100)
print("Adr of p3 is",id(p3)) # different from that of p1 or p2

del p1   # Destructor of p1 is not called bcoz the memory location of p1 has 1 more ref i.e. p2
del p2 # Destructor called immediately before executing next statement bcoz 
			# ref count is ZERO
print("Coords of p3 are",p3)
