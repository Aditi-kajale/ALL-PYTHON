#define a class Student with constructor to accept the name & percent of student & a method
# to display the details of the student along with grade obtained. The user may enter the name
# and percent OR name & marks of 3 subjects. (Class Method)
# Grades - If per >= 75, Grade A, If per >= 60 but per < 75, Grade B, If per < 60, Grade C - 
# (Static Method)
class Student:
	def __init__(self,name,per):
		self.name = name
		self.per = per
		self.grade = self.getGrade(per)

	def __str__(self):  # this method returns the string representation of an object
		return "Student " + self.name + " scored " + str(self.per) + " and got the grade " + self.grade;   # str can concatenate with str only

                # as python doesn't support method/constructor overloading, it can be compensated
	# using a class method
	@classmethod
	def byMarks(cls,name,m1,m2,m3):    # or use list_marks
		sum = m1 + m2 + m3
		per = sum / 3   # float division operator
		per = round(per,2)
		return cls(name,per)  # will return the object of class Student after
				# calling it's constructor

	@staticmethod
	def getGrade(per):  # no object or class parameter
		if per >= 75:
			return "A"
		elif per >= 60:
			return "B"
		else:
			return "C"
#main scope
s1 = Student("Manisha",80) # has implicit object "self" as 1st parameter
s2 = Student.byMarks("Prakash",67,65,70)  # has implicit class "cls" as 1st parameter
print(s1)
print(s2)



		
		





