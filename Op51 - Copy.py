# write an overloaded method to calculate the area of a rectangle, square and a circle
class Compute:

	def area(self,dim1=None,dim2=None):  # default values for args, can be 0 also
					# these values are considered if those
					# args are missing in method call
		# rectangle
		if dim1 != None and dim2 != None:
			return dim1 * dim2
		elif dim1 != None and type(dim1) == int:  # square
			return dim1 * dim1
		else:   # circle
			return 3.14 * dim1 * dim1

obj = Compute()
print("Area of rect with l=20 & b=5 is",obj.area(20,5))  # 100
print("Area of square with s=15 is",obj.area(15)) # 225
print("Area of circle with r=15 is",obj.area(15.0)) # 706.5