#WAP to flatten a nested list

l = [[1,2,3,4],[5,6],[7,8,9,10]]
print("Nested list is",l)
temp = []   # empty list

for row in l:
	for col in row:
		temp.append(col)


l = temp

del temp
print("Flattened list is",l)


