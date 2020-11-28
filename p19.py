# accept 5 values from user & display their square roots
#import math

count = 0
while True:     # self initialised / unconditional loop
	print("Enter a no of which square root is reqd :- ",end=" ")
	no = float(input())
	if no < 0:
		print("We cannot find square root of -ve no")
		continue

	#print("The square root of no",no,"is",math.sqrt(no))
	print("The square root of no",no,"is",no**0.5)  # OK
	count = count+1
	if count == 5:
		break

	