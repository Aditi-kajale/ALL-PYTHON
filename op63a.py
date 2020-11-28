# an eg of single inheritance
# design a class "Person" with attributes id & name
# design a class "Employee" which inherits "Person" & with additional attributes desgn 
# & salary. Create object/s of class Employee & display his/her details
class Person:
	def __init__(self,id,name):
		self.id = id
		self.name = name

class Employee(Person):  
	# we need to write the constructor here also bcoz of additional attributes reqd
	# in class Employee
	# overriding of constructor
	def __init__(self,id,name,desgn,salary):
		#Person.__init__(self,id,name) # invoking the super class constructor 
					#manually. Here the 1st parameter must
					# be "self" bcoz we are using a class
					# reference to call an instance method
		super().__init__(id,name)   # No self reqd as the __init__() is called 
		self.desgn = desgn		# using object reference
		self.salary = salary


#main scope
e1 = Employee(123,"Paresh","Manager",50000)  
print("ID - ",e1.id,", Name - ",e1.name,", Designation - ",e1.desgn,", Salary - ",e1.salary)


