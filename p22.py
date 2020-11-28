# print the first "n" terms of Fibonacci series
n = int(input("Enter the no of terms :- "))

# for any series program, always start with some assumption
curr_term = 0
next_term = 1

for i in range(n):   # 0 to n-1 i.e. n terms
	print(curr_term,end=" ")
	# move curr_term & next_term to next 2 places
	next_term = curr_term + next_term
	curr_term = next_term - curr_term

	