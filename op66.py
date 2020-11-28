# define a class Person with attributes name & place
# define a class Employee with attributes id, desgn & salary
# define a class Leader which inherits Person & Employee & display all the details
class Person(object):   # specifying object class as a super class is not mandatory
	def __init__(self,*args,**kwargs):
		self.name = args[0]
		self.place = args[1]
		super().__init__(*args,**kwargs)  # imp, to call the constructor of
					# next super class of Leader i.e.
					# Employee

class Employee(object):
	def __init__(self,*args,**kwargs):
		self.id = args[2]
		self.desgn = args[3]
		self.salary = args[4]
		# optional to call object's constructor

class Leader(Person,Employee):
	def __init__(self,*args,**kwargs):
		# no special attributes for Leader class
		super().__init__(*args,**kwargs) # calls the constructor of Person

l = Leader("Kamlesh","Pune",123,"Manager",50000.45)
print("Details of our leader are")
print(l.id,",",l.name,",",l.desgn,",",l.salary,",",l.place)
print(Leader.__mro__)










		