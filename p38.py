# WAP to find the sum of nos in a list using a user defined function "sum"
#function defn - anywhere in code before it is called
def sum(l):
	s = 0 # local var
	for i in range(len(l)):
		s += l[i]

	return s

# scope of main
l1 = [1,2,3,4,5]
s = sum(l1)
print("Sum of nos in list l1 is",s)

l2 = [1,2,3,4,5,6,7,8,9,10]
#s = sum(l2)
#print("Sum of nos in list l2 is",s)
#nested fn call, save on memory
print("Sum of nos in list l2 is",sum(l2))




	