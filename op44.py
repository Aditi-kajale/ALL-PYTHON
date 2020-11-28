# Write a generator fn to generate the factorial values
# In main(), accept the no & display it's factorial value
def fact():
	no = 1
	fv = 1
	while True:
		yield fv
		no += 1
		fv *= no

#main scope
no = int(input("Enter a no :- "))
g = fact()  # obtain a generator object from generator fn

for i in range(no):
	fv = next(g)  # gets the fv of no generated @ run time / calculated on the fly
	print("FV of no",i+1,"is",fv)

print("Factorial value of no",no,"is",fv)





