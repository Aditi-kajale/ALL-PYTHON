# define an overloaded method which returns the sum of 2 or 3 nos in a class
class Total:
	
	def sum(self,a,b):
		return a + b

	def sum(self,a,b,c):
		return a + b + c


#main scope
t = Total()
print("Sum of nos 10, 20 & 30 is",t.sum(10,20,30)) # 60
#print("Sum of nos 10 & 20 is",t.sum(10,20)) # error, sum() missing 1 reqd positional arg 'c'