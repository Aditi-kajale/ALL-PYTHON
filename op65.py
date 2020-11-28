# to remove the problem with super() in multiple inheritance using mro
class A():      # default class inherited is object class
	def __init__(self):
		print("Invocation of constructor of class A")
		super().__init__()  # will invoke B's constructor

class B(): 
	def __init__(self):
		print("Invocation of constructor of class B")
		super().__init__()  # will invoke object's constructor i.e. a class
				# which is parent of all classes
class C(A,B):
	def __init__(self):
		print("Invocation of constructor of class C")
		super().__init__()  # will invoke A's constructor only

objc = C()

# Note - However in commercial application, 2 base classes may have a different set & type
# of arguments. Hence in such cases, we use *args & **kwargs which represent var length
# positional & keyword args.
