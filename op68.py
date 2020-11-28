# define a class "Employee" with attributes name, type & gross_sal. Every employee is
# entitled for DA (Dearness Allowance - 20%) and HRA (House Rent Allowance - 40%) of
# his/her basic salary. Define a method to calculate the net salary of employee.
# define a class "Salesman" which inherits "Employee". The salesman is entitled for
# Travelling Allowance which is Rs. 300/- per day.
# define a class "Manager" which inherits "Employee". The manager is entitled for
# Commission on Monthly Sales. The commission is 2% on sales if sales <= Rs. 1 Lac.
# If the sales exceed Rs. 1 Lac, then he is entitled for slab1 + 1% on sales > Rs. 1 Lac.
from abc import ABC, abstractmethod

class Employee(ABC):
	def __init__(self,name,type,basic):
		self.name = name
		self.type = type
		da = basic * 0.2   # da is a local var in constructor
		hra = basic * 0.4
		self.gross_sal = basic + da + hra  # gross_sal is not a local var but
					# an attribute

	@abstractmethod
	def get_net_salary(self):
		pass

class Salesman(Employee):
	def __init__(self,name,basic,no_days):
		# call the super class constructor to initialise the common attributes
		super().__init__(name,"Salesman",basic)
		self.no_days = no_days

	# compulsory to override the abstract method of super class
	def get_net_salary(self):
		return self.gross_sal + self.no_days * 300

class Manager(Employee):
	def __init__(self,name,basic,mthly_sales):
		super().__init__(name,"Manager",basic)
		self.mthly_sales = mthly_sales

	def get_net_salary(self):
		if self.mthly_sales <= 100000:
			return self.gross_sal + self.mthly_sales * 0.02
		else:
			return self.gross_sal + 2000 + (self.mthly_sales-100000)*0.01

# main() scope
# store all the objects in a list & then display them all
l = [ ]   # blank list
nor = int(input("Enter the no of records :- "))
# accept data from user
for i in range(nor):
	name = input("Enter the name of employee :- ")
	type = input("Enter s/S for salesman OR m/M for manager :- ")
	basic = int(input("Enter the basic salary :- "))
	if type == 's' or type == 'S':
		no_days = int(input("Enter the no of days travelled :- "))
		e = Salesman(name,basic,no_days)
	else:
		mthly_sales = int(input("Enter the monthly sales :- "))
		e  = Manager(name,basic,mthly_sales)

	# add the object to list
	l.append(e)

print("Data of all emps is")
for i in range(nor):
	print(l[i].name,l[i].type,l[i].get_net_salary())  # common name as we have
				# resorted to overriding
				# dynamic method dispatch i.e. depending upon
				# whether l[i] refers to Salesman or Manager, that
				# method will be called














		








