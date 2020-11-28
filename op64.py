# to examine the problem with super() in multiple inheritance
class A():      # default class inherited is object class
	def __init__(self):
		print("Invocation of constructor of class A")

class B(): 
	def __init__(self):
		print("Invocation of constructor of class B")

class C(A,B):
	def __init__(self):
		print("Invocation of constructor of class C")
		# A.__init__(self)     # works fine, self reqd bcoz instance methods
		# B.__init__(self)    # require object & we are calling init() using
				# class reference
		super().__init__()  # will invoke A's constructor only
		super().__init__()  # will invoke A's constructor only

objc = C()
print(C.__mro__)

