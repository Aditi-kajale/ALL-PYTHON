# Write a prog to print all prime nos from 2-n
n = int(input("Enter the last term :- "))

print("Prime nos from 2 -",n,"are")
# loop to generate nos from 2-n
for no in range(2,n+1):
	# here we need to generate the divisors for the no
	# max divisor of any no is 1/2 of that no
	for i in range(2,no//2+1):
		# divisibility test
		if no % i == 0:   # found divisor, no is not prime
			break   # terminate the inner loop
	else:   # else of for loop
		print(no,end=" ")
			
