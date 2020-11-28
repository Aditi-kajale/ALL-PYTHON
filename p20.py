# accept a no from user & determine whether it is a Prime No or not
no = int(input("Enter the no :- "))

# here we need to generate the divisors for the no
# max divisor of any no is 1/2 of that no
for i in range(2,no//2+1):
	# divisibility test
	if no % i == 0:   # found divisor, no is not prime
		print("No",no,"is not a Prime No")
		break   # terminate the process
else:   # else of for loop
	print("No",no,"is a Prime No")
			
