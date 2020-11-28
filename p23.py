# print the 1st "n" terms of prime nos starting from 2
n = int(input("Enter the no of prime terms reqd :- "))
no = 2
count = 0

# we do not know which is n" prime term
# This means we don not know the stop no
# go on generating nos & stop after the "n" th prime term
while True:
	for i in range(2,no//2+1):
		if no % i == 0:
			break    # terminate "for" loop
	else:
		print(no,end=" ")
		count += 1  # count only if prime
		if count == n:
			break   # to terminate "while" loop

	no += 1

