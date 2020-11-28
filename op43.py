# Write a generator function to generate the fibonacci series
# 0 1 1 2 3 5 8 13 21 34.......
# Note that the generator fn has no stopping point
def fibo():
	curr_term, next_term = 0, 1

	while True:
		yield curr_term # return curr_term & pause the function
		next_term = curr_term + next_term
		curr_term = next_term - curr_term


# accept the position of the fibonacci element to be displayed
pos = int(input("Enter the position of element :- "))

f = fibo() # the generation fn returns the generator object

for i in range(pos):
	el = next(f)  # in every call to generator fn, fetch the element/no

print("Element @ position",pos,"is",el)



		