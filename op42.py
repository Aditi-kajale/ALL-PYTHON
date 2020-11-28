# eg - 1, write a generator function to generate the square of natural nos (infinite squares)
def Square_fn():
	no = 1
	while True:     # unconditional loop
		yield no * no
		no += 1  # The next() when called from main(), will start it's execution
			# from this point


# code to test the generator fn
# the generator fn is iterable, so here we need not call next() explicit
for sq in Square_fn():
	if sq > 100:
		break

	print(sq)

"""
g = Square_fn()

print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 9
print(next(g)) # 16
print(next(g)) # 25
print(next(g)) # 36
print(next(g)) # 49
"""

