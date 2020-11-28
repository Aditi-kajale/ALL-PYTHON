# to prove that class and instance vars are distinct even if they have same name
# WAP to display the no of fruits of each type and also the total no of fruits added to a basket
class Fruits:
	count = 0 # total fruit count

	def __init__(self,name,count):  # count is a local arg
		self.name = name
		self.count = count # individual fruit count
		Fruits.count += self.count

# main scope
apples = Fruits("apple",3)
oranges = Fruits("orange",5)
bananas = Fruits("banana",2)

print("No of apples are",apples.count) # 3
print("No of oranges are",oranges.count) # 5
print("No of bananas are",bananas.count) # 2

print("Total no of fruits added to basket are",Fruits.count) # 10


