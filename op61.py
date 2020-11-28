# an application using all 3 kinds of methods of a class
# define a class "Person" to store name & age of any person alongwith his category
# Here the i/p should be accepted as age or year of birth
# Now the problem is that we use a constructor to create objects & we cannot overload them
# i.e. we cannot have 2 constructors, 1 to accept age & anoter to accept date of birth & then
# calculate age to create a person object
# Here we will make use of a class method to calculate the age from date of birth & return
# the object of Person to main()
from datetime import datetime

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.category = self.getCategory(age)

	def display(self):
		print(self.name,"'s age is",self.age," and he/she is a",self.category)

	# if the user gives date of birth, call this method
	@classmethod
	def byBirthDate(cls,name,dt_birth):
		curr_year = datetime.now().year
		yr = int(dt_birth[-4:])
		age = curr_year - yr
		return cls(name,age)  # will call constructor bcoz cls means class name
		#return Person(name,age)

	@staticmethod
	def getCategory(age):
		if age <= 30:
			return 'youngster'
		elif age < 60:
			return 'middle aged'
		else:
			return 'old'

# main scope
p1 = Person("Uma",25)  # directly calling constructor as format is OK
p2 = Person.byBirthDate("Geeta","20-December-1985")

p1.display()
p2.display()





