# to prove that class/static vars cannot be modified using instance/object of that class
class Student:
	stream = "IT Engg"  # these (attributes) are tied to class  

	def __init__(self,rollno,name):
		self.rollno = rollno  # these are tied to object
		self.name = name

	def __str__(self):
		return "Rollno - " + str(self.rollno) + ", Name - " + self.name

#main scope
s1 = Student(1,"Paresh")
s1.stream = "BCS"

s2 = Student(2,"Sandesh")

print("s1 contains ",s1)
print("Stream of Paresh is",s1.stream) # BCS
print("s2 contains ",s2)
print("Stream of Sandesh is",s2.stream)  # IT Engg