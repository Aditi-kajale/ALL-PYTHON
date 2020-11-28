# an eg of single inheritance
# design a class "Person" with attributes id & name
# design a class "Employee" which inherits "Person" & with additional attributes desgn 
# & salary. Create object/s of class Employee & display his/her details
class Person:
	def __init__(self,id,name):
		self.id = id
		self.name = name

class Employee(Person):  # class Person is the super class of Employee
	pass


#main scope
e1 = Employee(123,"Paresh")  # OK will not give error even if class Employee doesn't have
			# a constructor bcoz by virtue of inheritance, the super class's
			# constructor becomes available auto
print("ID - ",e1.id,", Name - ",e1.name) # by virtue of inheritance, attributes of super class are
				# available


